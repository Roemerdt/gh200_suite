// Everything one cell needs to time its variants
#pragma once
#include <unistd.h>

#include <algorithm>
#include <cstring>
#include <memory>
#include <string>
#include <vector>

#include "common/common.h"
#include "config.h"
#include "copy.h"
#include "gpu_read.h"
#include "host_phase.h"
#include "kernel.h"

namespace suite {

struct HostSide {
  Buffer input, output;
  long anon_huge_kb = -1;  // AnonHugePages of the input after population
  bool registered = false;
  std::string key;  // what makes the buffer distinct
};

typedef std::vector<std::unique_ptr<RouteKernel>> Kernels;  // one instance per variant

static const int COPY_STREAMS = 4;

class RouteCell {
  const Config& cfg_;
  const Kernels& kernels_;
  cudaStream_t stream_;  // the timing stream
  cudaStream_t copy_streams_[COPY_STREAMS];
  cudaEvent_t begin_, end_, after_copy_in_, after_kernel_, after_copy_out_, start_;
  cudaEvent_t join_[COPY_STREAMS], part_ready_[2];
  std::vector<HostSide> host_;
  std::vector<int> host_of_;          // variant -> host buffer
  std::vector<u64> passes_;           // passes launched so far, per variant
  Buffer dev_input_;                  // shared by the basic-copy variants
  std::vector<Buffer> dev_stateful_;  // a stateful re-copy variant's own device copy
  u64* dev_output_ = nullptr;
  Buffer control_;              // the matched control's buffer, shared by the control variants
  std::vector<double> cpu_ns_;  // the host phases' time in the last interval, per variant
  std::vector<double> state_check_ns_;   // the state check's load latency, per variant
  double first_call_ns_[3] = {0, 0, 0};  // copy-in, kernel, copy-out of an interval's first call

 public:
  RouteCell(const Config& cfg, const Kernels& kernels)
      : cfg_(cfg),
        kernels_(kernels),
        host_of_(cfg.variants.size(), -1),
        passes_(cfg.variants.size(), 0),
        dev_stateful_(cfg.variants.size()),
        cpu_ns_(cfg.variants.size(), 0),
        state_check_ns_(cfg.variants.size(), -1) {
    check_capacity();
    CU(cudaStreamCreateWithFlags(&stream_, cudaStreamNonBlocking));
    for (cudaStream_t& s : copy_streams_) {
      CU(cudaStreamCreateWithFlags(&s, cudaStreamNonBlocking));
    }
    for (cudaEvent_t* e :
         {&begin_, &end_, &after_copy_in_, &after_kernel_, &after_copy_out_, &start_}) {
      CU(cudaEventCreate(e));
    }
    for (cudaEvent_t& e : join_) { CU(cudaEventCreateWithFlags(&e, cudaEventDisableTiming)); }
    for (cudaEvent_t& e : part_ready_) { CU(cudaEventCreateWithFlags(&e, cudaEventDisableTiming)); }
    allocate_hosts();
    if (needs_control()) { allocate_control(); }
    if (device_input_bytes() > 0) { dev_input_ = device_alloc(device_input_bytes()); }
    if (device_output_bytes() > 0) { CU(cudaMalloc(&dev_output_, device_output_bytes())); }
    for (int v = 0; v < variants(); v++) {
      if (spec(v).route == COPY && spec(v).recopy != "none") {
        if (spec(v).recopy == "runs" && !spec(v).host.control) {
          const LineSet set = phase_lines(v, 0);
          u64 runs = 0;
          set.for_each_run([&](u64, u64) { runs++; });
          if (runs > RECOPY_MAX_RUNS) {
            fprintf(stderr,
                    "variant %s: the per-run re-copy would issue %llu copy calls per pass (at most "
                    "%llu): cell refused\n",
                    variant_letter(v).c_str(), runs, RECOPY_MAX_RUNS);
            exit(2);
          }
        }
        dev_stateful_[v] = device_alloc(spec(v).input_bytes);
        CU(cudaMemcpy(dev_stateful_[v].p, host(v).input.p, spec(v).input_bytes,
                      cudaMemcpyHostToDevice));
      }
    }
    for (int v = 0; v < variants(); v++) {
      if (spec(v).node != GPU_NODE || host_of_[v] != first_variant_of(host_of_[v])) { continue; }
      gpu_read_all(host(v).input.p, spec(v).input_bytes, stream_);
      gpu_read_all(host(v).output.p, output_map_bytes(), stream_);
    }
    if (control_.p && placement_node(cfg_.placement) == GPU_NODE) {
      gpu_read_all(control_.p, control_.size, stream_);
    }
  }

  ~RouteCell() {
    for (HostSide& h : host_) {
      if (h.registered) { CU(cudaHostUnregister(h.input.p)); }
      free_buffer(h.input);
      free_buffer(h.output);
    }
    free_buffer(dev_input_);
    for (Buffer& b : dev_stateful_) { free_buffer(b); }
    free_buffer(control_);
    if (dev_output_) { CU(cudaFree(dev_output_)); }
  }

  int variants() const { return (int)cfg_.variants.size(); }
  const VariantSpec& spec(int v) const { return cfg_.variants[v]; }
  const RouteKernel& kernel(int v) const { return *kernels_[v]; }
  const HostSide& host(int v) const { return host_[host_of_[v]]; }
  const double* first_call_ns() const { return first_call_ns_; }
  double cpu_ns(int v) const { return cpu_ns_[v]; }
  double state_check_ns(int v) const { return state_check_ns_[v]; }
  bool has_host_phases() const { return cfg_.host.kind != "none"; }

  // one event pair around the passes, or with host phases one pair per pass, summed, each after
  // the host phase on the CPU clock. Copy calls never overlap, the first is also timed in parts
  double interval_ns(int v, long passes) {
    if (!has_host_phases()) {
      if (spec(v).route == DIRECT) { return direct_passes_ns(v, passes); }
      const double t = gpu_timed_ns(begin_, end_, stream_, [&]() {
        for (long p = 0; p < passes; p++) { copy_call(v, p == 0); }
      });
      read_breakdown();
      return t;
    }
    double gpu = 0;
    cpu_ns_[v] = 0;
    for (long p = 0; p < passes; p++) {
      const uint64_t t0 = now_ns();
      host_phase(v, passes_[v]);
      cpu_ns_[v] += (double)(now_ns() - t0);
      if (spec(v).route == DIRECT) {
        gpu += direct_passes_ns(v, 1);
      } else {
        gpu += gpu_timed_ns(begin_, end_, stream_, [&]() { copy_call(v, p == 0); });
        if (p == 0) { read_breakdown(); }
      }
    }
    return gpu;
  }

  // with the device copy set to a sentinel one call must still deliver the checksum, so the copy
  // brings every word the kernel reads
  bool sentinel_check(int v) {
    if (spec(v).recopy != "none") { return recopy_check(v); }
    CU(cudaMemsetAsync(dev_input_.p, 0xAB, dev_input_.size, stream_));
    copy_call(v, false);
    CU(cudaStreamSynchronize(stream_));
    return delivered_checksum(v) == expected_checksum(v);
  }

  bool verify_launch(int v) { return kernels_[v]->verify((const u64*)host(v).input.p, stream_); }

  // The state check of a cache-state or CPU-writes cell: after the variant's host phase, the
  // median load latency of sampled lines of its region on the preparing core
  void state_check(int v) {
    if (cfg_.host.kind != "state" && cfg_.host.kind != "writes") { return; }
    host_phase(v, passes_[v]);
    const LineSet set = phase_lines(v, passes_[v]);
    state_check_ns_[v] = sampled_load_latency_ns(phase_base(v), set, 0x5747 + (uint64_t)v);
  }

  u64 delivered_checksum(int v) const {
    const u64* out =
        (const u64*)(kernel(v).updates_in_place() ? host(v).input.p : host(v).output.p);
    return sum_words(out, kernel(v).delivered_words());
  }

  u64 expected_checksum(int v) const { return kernel(v).expected_checksum(passes_[v] - 1); }

  // the input's residency, unless only the output moved
  Residency residency(int v) const {
    Residency in = residency_check(host(v).input), out = residency_check(host(v).output);
    return (in.ok && !out.ok) ? out : in;
  }

 private:
  size_t output_bytes(int v) const {
    return kernel(v).updates_in_place() ? 0 : kernel(v).output_words() * sizeof(u64);
  }
  // every host output buffer holds the largest output of the cell, so variants can share one
  size_t output_map_bytes() const {
    size_t largest = 1;
    for (int v = 0; v < variants(); v++) { largest = std::max(largest, output_bytes(v)); }
    return round_up(largest, page_bytes());
  }
  static u64 sum_words(const u64* p, size_t n) {
    if (n < ((size_t)1 << 22)) {
      u64 sum = 0;
      for (size_t i = 0; i < n; i++) { sum += p[i]; }
      return sum;
    }
    std::vector<u64> sums(fill_workers(), 0);
    parallel_ranges(n, [&](unsigned worker, u64 begin, u64 end) {
      u64 s = 0;
      for (u64 i = begin; i < end; i++) { s += p[i]; }
      sums[worker] = s;
    });
    u64 sum = 0;
    for (u64 s : sums) { sum += s; }
    return sum;
  }
  double direct_passes_ns(int v, long passes) {
    u64* out = (u64*)(kernel(v).updates_in_place() ? host(v).input.p : host(v).output.p);
    if (kernel(v).cpu_issued()) {
      const uint64_t t0 = now_ns();
      for (long p = 0; p < passes; p++) { launch(v, host(v).input.p, out); }
      return (double)(now_ns() - t0);
    }
    return gpu_timed_ns(begin_, end_, stream_, [&]() {
      for (long p = 0; p < passes; p++) { launch(v, host(v).input.p, out); }
    });
  }
  size_t largest_input_bytes() const {
    size_t largest = 0;
    for (int v = 0; v < variants(); v++) { largest = std::max(largest, spec(v).input_bytes); }
    return largest;
  }
  bool needs_control() const {
    for (int v = 0; v < variants(); v++) {
      if (spec(v).host.kind != "none" && spec(v).host.control) { return true; }
    }
    return false;
  }

  // the variant is part of the key unless the cell shares buffers. An in-place kernel counts all
  // passes on a shared buffer, so a tuning cell's variants may share its table
  std::string host_key(int v) const {
    const VariantSpec& s = spec(v);
    std::string key = s.placement + ":" + std::to_string(s.input_bytes) + ":" + s.page_size + ":" +
                      s.alignment + ":" +
                      (s.route == COPY && s.copy.memory == "registered" ? "reg" : "page");
    for (const auto& fl : s.kernel_levels) { key += ":" + fl.first + "=" + fl.second; }
    return cfg_.shared_buffers ? key : key + "#" + std::to_string(v);
  }
  int first_variant_of(int h) const {
    for (int v = 0; v < variants(); v++) {
      if (host_of_[v] == h) { return v; }
    }
    return -1;
  }

  // one host buffer per key, populated by its first variant, the others attach to that state
  void allocate_hosts() {
    for (int v = 0; v < variants(); v++) {
      const std::string key = host_key(v);
      for (int h = 0; h < (int)host_.size(); h++) {
        if (host_[h].key == key) { host_of_[v] = h; }
      }
      if (host_of_[v] >= 0) {
        kernels_[v]->attach(*kernels_[first_variant_of(host_of_[v])]);
        continue;
      }
      const VariantSpec& s = spec(v);
      HostSide h;
      h.key = key;
      h.input = sys_alloc(s.input_bytes, s.node, s.thp, s.align_bytes, s.offset_bytes);
      kernels_[v]->populate((u64*)h.input.p);
      h.output = sys_alloc(output_map_bytes(), s.node, 0, HOME_ALIGN_BYTES);
      memset(h.output.p, 0, output_map_bytes());
      h.anon_huge_kb = smaps_anon_huge_kb(h.input.p);
      if (s.thp && (h.anon_huge_kb < 0 || (size_t)h.anon_huge_kb * 1024 < s.input_bytes)) {
        fprintf(stderr,
                "variant %s asked for 512 MB pages and got %ld kB of %zu bytes: cell refused\n",
                variant_letter(v).c_str(), h.anon_huge_kb, s.input_bytes);
        exit(EXIT_NO_HUGE_PAGES);
      }
      if (s.route == COPY && s.copy.memory == "registered") {
        CU(cudaHostRegister(h.input.p, s.input_bytes, cudaHostRegisterDefault));
        h.registered = true;
      }
      host_.push_back(h);
      host_of_[v] = (int)host_.size() - 1;
    }
  }

  void allocate_control() {
    const VariantSpec& home = spec(0);
    control_ =
        sys_alloc(largest_input_bytes(), home.node, home.thp, home.align_bytes, home.offset_bytes);
    fill_all_cores((u64*)control_.p, control_.size / sizeof(u64));
  }

  size_t device_input_bytes() const {
    size_t bytes = 0;
    for (int v = 0; v < variants(); v++) {
      if (spec(v).route == COPY && spec(v).recopy == "none") {
        bytes = std::max(bytes, spec(v).input_bytes);
      }
    }
    return bytes;
  }
  size_t device_output_bytes() const {
    size_t bytes = 0;
    for (int v = 0; v < variants(); v++) {
      if (spec(v).route == COPY) { bytes = std::max(bytes, output_bytes(v)); }
    }
    return bytes;
  }

  void launch(int v, const void* input, u64* output) {
    kernels_[v]->launch((const u64*)input, output, passes_[v]++, stream_);
  }

  void read_breakdown() {
    first_call_ns_[0] = event_elapsed_ns(begin_, after_copy_in_);
    first_call_ns_[1] = event_elapsed_ns(begin_, after_kernel_) - first_call_ns_[0];
    first_call_ns_[2] = event_elapsed_ns(after_kernel_, after_copy_out_);
  }

  // the lines this pass reads, as the kernel declares them
  CopyRegion region_of(int v, u64 first, u64 count, u64 pass) const {
    CopyRegion r;
    r.first = first;
    r.count = count;
    if (spec(v).copy.form == "touched" &&
        !kernel(v).touched_window(pass, &r.period, &r.width, &r.offset)) {
      fprintf(stderr, "%s does not know its touched lines in advance: no touched-lines copy\n",
              kernel(v).name());
      exit(2);
    }
    return r;
  }

  // writes hit one line in every 1/w, a cache state covers the lines the next pass reads
  LineSet phase_lines(int v, u64 pass) const {
    const VariantSpec& s = spec(v);
    const u64 lines = s.input_bytes / GPU_LINE_BYTES;
    LineSet set;
    if (s.host.kind == "writes") {
      set.first = 0;
      set.count = lines;
      set.period = std::max((u64)1, (u64)(1.0 / s.host.w + 0.5));
      set.width = 1;
    } else if (s.host.kind == "state") {
      if (!kernel(v).read_lines(pass, set.list)) {
        kernel(v).read_span(pass, &set.first, &set.count, lines);
      }
    }
    return set;
  }
  u64* phase_base(int v) const {
    return (u64*)(spec(v).host.control ? control_.p : host(v).input.p);
  }

  // shared phases work on the variant's input or output, control phases on the control buffer
  void host_phase(int v, u64 pass) {
    const VariantSpec& s = spec(v);
    if (s.host.kind == "none") { return; }
    if (s.host.kind == "reads") {
      const u64* p = s.host.control ? (const u64*)control_.p : (const u64*)host(v).output.p;
      volatile u64 sink = run_read_phase(p, kernel(v).delivered_words());
      (void)sink;
      return;
    }
    run_write_phase(phase_base(v), phase_lines(v, pass), s.host);
  }

  void recopy_written(int v, u64 pass, cudaStream_t s) {
    const VariantSpec& sp = spec(v);
    if (sp.host.control) { return; }  // the control writes elsewhere
    const LineSet set = phase_lines(v, pass);
    const u64* src = (const u64*)host(v).input.p;
    u64* dst = (u64*)dev_stateful_[v].p;
    if (sp.recopy == "runs") {
      set.for_each_run([&](u64 first, u64 count) {
        CU(cudaMemcpyAsync(dst + first * GPU_LINE_WORDS, src + first * GPU_LINE_WORDS,
                           count * GPU_LINE_BYTES, cudaMemcpyHostToDevice, s));
      });
      return;
    }
    CopyConfig c;
    c.mechanism = sp.recopy == "pitched" ? "ce" : "kernel";
    c.form = "touched";
    CopyRegion r;
    r.first = set.first;
    r.count = set.count;
    r.period = set.period;
    r.width = set.width;
    r.offset = set.offset;
    copy_region(c, src, dst, r, s);
  }

  // changes the first word of each written line, checks the re-copy brings it, then restores them
  bool recopy_check(int v) {
    if (spec(v).host.control) { return true; }
    const LineSet set = phase_lines(v, passes_[v]);
    u64* input = (u64*)host(v).input.p;
    std::vector<u64> originals;  // first words of the written lines
    originals.reserve(set.lines());
    set.for_each_run([&](u64 first, u64 count) {
      for (u64 line = first; line < first + count; line++) {
        originals.push_back(input[line * GPU_LINE_WORDS]);
        input[line * GPU_LINE_WORDS] = 0xE70C000000000000ull | line;
      }
    });
    recopy_written(v, passes_[v], stream_);
    CU(cudaStreamSynchronize(stream_));
    bool ok = true;
    std::vector<u64> back(GPU_LINE_WORDS);
    u64 checked = 0;
    set.for_each_run([&](u64 first, u64 count) {
      for (u64 line = first; line < first + count && ok; line += std::max((u64)1, count / 4)) {
        CU(cudaMemcpy(back.data(), (const u64*)dev_stateful_[v].p + line * GPU_LINE_WORDS,
                      GPU_LINE_BYTES, cudaMemcpyDeviceToHost));
        ok = back[0] == (0xE70C000000000000ull | line);
        checked++;
      }
    });
    size_t i = 0;
    set.for_each_run([&](u64 first, u64 count) {
      for (u64 line = first; line < first + count; line++) {
        input[line * GPU_LINE_WORDS] = originals[i++];
      }
    });
    recopy_written(v, passes_[v], stream_);  // the device copy back to the originals
    CU(cudaStreamSynchronize(stream_));
    return ok && checked > 0;
  }

  // the copy streams wait for the previous call on the timing stream and join it before the
  // kernel. Pipelined, the kernel runs part k as soon as part k has arrived
  void copy_call(int v, bool breakdown) {
    const VariantSpec& s = spec(v);
    const CopyConfig& c = s.copy;
    const u64* src = (const u64*)host(v).input.p;
    const bool stateful = s.recopy != "none";
    u64* dst = (u64*)(stateful ? dev_stateful_[v].p : dev_input_.p);
    const bool in_place = kernel(v).updates_in_place();
    u64* out = in_place ? dst : dev_output_;  // an in-place kernel updates the device copy itself
    const u64 lines = s.input_bytes / GPU_LINE_BYTES;
    const u64 pass = passes_[v];
    CU(cudaEventRecord(start_, stream_));
    const int streams = c.streams;
    for (int i = 0; i < streams; i++) { CU(cudaStreamWaitEvent(copy_streams_[i], start_, 0)); }
    const size_t chunk = c.chunk_bytes();
    u64 chunk_lines = chunk ? chunk / GPU_LINE_BYTES : lines;
    if (c.form == "touched" && chunk) {
      // a chunk of the touched form starts on a group boundary, so its window stays in phase
      u64 period, width, offset;
      if (kernel(v).touched_window(pass, &period, &width, &offset) && period > 1) {
        chunk_lines = std::max(period, chunk_lines / period * period);
      }
    }
    if (stateful) {
      recopy_written(v, pass, copy_streams_[0]);
      CU(cudaEventRecord(join_[0], copy_streams_[0]));
      CU(cudaStreamWaitEvent(stream_, join_[0], 0));
      if (breakdown) { CU(cudaEventRecord(after_copy_in_, stream_)); }
      launch(v, dst, out);
      if (breakdown) { CU(cudaEventRecord(after_kernel_, stream_)); }
    } else if (c.pipeline == "pipe") {
      const int parts = (int)((s.input_bytes + chunk - 1) / chunk);
      CU(cudaMemsetAsync(dev_output_, 0, output_bytes(v), stream_));
      for (int k = 0; k < parts; k++) {
        std::vector<std::pair<u64, u64>> ranges;
        kernel(v).part_lines(k, parts, &ranges);
        for (const auto& fc : ranges) {
          copy_region(c, src, dst, region_of(v, fc.first, fc.second, pass), copy_streams_[0]);
        }
        CU(cudaEventRecord(part_ready_[k % 2], copy_streams_[0]));
        CU(cudaStreamWaitEvent(stream_, part_ready_[k % 2], 0));
        kernel(v).launch_part(dst, dev_output_, pass, k, parts, stream_);
      }
      passes_[v]++;
      if (breakdown) {
        CU(cudaEventRecord(after_copy_in_, copy_streams_[0]));
        CU(cudaEventRecord(after_kernel_, stream_));
      }
    } else {
      int i = 0;
      for (u64 first = 0; first < lines; first += chunk_lines, i++) {
        copy_region(c, src, dst, region_of(v, first, std::min(chunk_lines, lines - first), pass),
                    copy_streams_[i % streams]);
      }
      for (int j = 0; j < streams; j++) {
        CU(cudaEventRecord(join_[j], copy_streams_[j]));
        CU(cudaStreamWaitEvent(stream_, join_[j], 0));
      }
      if (breakdown) { CU(cudaEventRecord(after_copy_in_, stream_)); }
      launch(v, dst, out);
      if (breakdown) { CU(cudaEventRecord(after_kernel_, stream_)); }
    }
    if (in_place) {
      copy_out_words(c, dst, (u64*)host(v).input.p, s.input_bytes / sizeof(u64), stream_);
    } else {
      copy_out_words(c, dev_output_, (u64*)host(v).output.p, kernel(v).delivered_words(), stream_);
    }
    if (breakdown) { CU(cudaEventRecord(after_copy_out_, stream_)); }
  }

  // free GPU-node memory once it stops rising. A process that just exited returns its memory over
  // the first seconds, sometimes starting late, hence the minimum number of polls
  static size_t settled_free_bytes() {
    size_t last = 0;
    for (int poll = 0; poll < CAPACITY_SETTLE_POLLS; poll++) {
      size_t free_device = 0, total = 0;
      CU(cudaMemGetInfo(&free_device, &total));
      const size_t free_node = node_free_bytes(GPU_NODE);
      const size_t now = free_node ? std::min(free_node, free_device) : free_device;
      if (poll >= CAPACITY_SETTLE_MIN_POLLS && now <= last) { return std::max(now, last); }
      last = std::max(now, last);
      usleep(CAPACITY_SETTLE_US);
    }
    return last;
  }

  // device memory and host buffers bound to the GPU node draw on the same pool. A 512 MB-page
  // buffer counts twice, faulting it in briefly takes about twice its size
  void check_capacity() const {
    size_t demand = device_input_bytes() + device_output_bytes();
    std::vector<std::string> counted;
    for (int v = 0; v < variants(); v++) {
      demand += kernel(v).device_bytes();
      if (spec(v).route == COPY && spec(v).recopy != "none") { demand += spec(v).input_bytes; }
      const std::string key = host_key(v);
      if (spec(v).node == GPU_NODE &&
          std::find(counted.begin(), counted.end(), key) == counted.end()) {
        demand += spec(v).input_bytes * (spec(v).thp ? 2 : 1) + output_map_bytes();
        counted.push_back(key);
      }
    }
    if (needs_control() && placement_node(cfg_.placement) == GPU_NODE) {
      demand += largest_input_bytes() * (spec(0).thp ? 2 : 1);
    }
    const size_t free_bytes = settled_free_bytes();
    fprintf(
        stderr,
        "capacity: the cell needs %zu MiB of GPU-node memory (512 MB-page buffers counted twice), "
        "%zu MiB are free, %zu MiB must stay free\n",
        demand >> 20, free_bytes >> 20, CAPACITY_MARGIN_BYTES >> 20);
    if (demand + CAPACITY_MARGIN_BYTES > free_bytes) {
      fprintf(stderr, "capacity: declared gap\n");
      exit(EXIT_DECLARED_GAP);
    }
  }
};

}  // namespace suite
