// route transient times the one-time cost of populating the input, per level, on a fresh mapping
// every round. Mapping and binding stay outside the timers
#pragma once
#include <glob.h>
#include <sys/mman.h>
#include <unistd.h>

#include <algorithm>
#include <cstdio>
#include <memory>
#include <string>
#include <vector>

#include "common/common.h"
#include "config.h"
#include "copy.h"
#include "kernel.h"

namespace suite {

static const int QUIET_READINGS = 4;     // identical fault-statistics readings in a row
static const int QUIET_POLL_US = 50000;  // between readings
static const int QUIET_MAX_POLLS = 200;  // at most 10 s
static const uintptr_t FRESH_BASE = 0x200000000000ull;  // fresh mappings are placed from 32 TiB up

__global__ void transient_fill_kernel(u64* p, u64 words) {
  const u64 n = (u64)gridDim.x * blockDim.x;
  for (u64 i = (u64)blockIdx.x * blockDim.x + threadIdx.x; i < words; i += n) {
    p[i] = word_value(i);
  }
}

struct TransientLevel {
  std::string name,
      fill;             // fill: cpu-all | cpu-one | gpu | register | copy | copy-calls | gpu-device
  int node = CPU_NODE;  // -1: unbound
  int thp = 0;
  int intended_node() const { return node < 0 ? GPU_NODE : node; }
};

// cpu-all      all cores fill, bound to the CPU node (the home recipe)
// cpu-one      one thread fills
// cpu-node1    all cores fill, bound to the GPU node
// gpu-bound    a GPU kernel fills, bound to the CPU node
// gpu-unbound  a GPU kernel fills an unbound mapping
// register     cudaHostRegister, then all cores fill
// copy         home recipe, one copy-in to cudaMalloc memory, the runs, one copy-out
// copy-calls   home recipe, then copy-in, kernel and copy-out every run
// gpu-device   a GPU kernel fills cudaMalloc memory, the runs, one copy-out
// -thp asks for 512 MB pages on the CPU, register and gpu-bound levels
// the copy-in is the frozen copy without its pipeline, registering is a timed step of its own
inline TransientLevel transient_level(const std::string& name) {
  TransientLevel l;
  l.name = name;
  std::string base = name;
  const std::string suffix = "-thp";
  if (base.size() > suffix.size() &&
      base.compare(base.size() - suffix.size(), suffix.size(), suffix) == 0) {
    base = base.substr(0, base.size() - suffix.size());
    l.thp = 1;
  }
  if (base == "cpu-all" || base == "cpu-one" || base == "register") {
    l.fill = base;
  } else if (base == "cpu-node1") {
    l.fill = "cpu-all";
    l.node = GPU_NODE;
  } else if (base == "gpu-bound") {
    l.fill = "gpu";
  } else if (base == "gpu-unbound" && !l.thp) {
    l.fill = "gpu";
    l.node = -1;
  } else if ((base == "copy" || base == "copy-calls" || base == "gpu-device") && !l.thp) {
    l.fill = base;
  } else {
    bad_flag_value("levels", name, "is not a population level");
  }
  return l;
}

// UVM fault statistics of every GPU, summed over sections (procfs, needs uvm_enable_debug_procfs)
struct FaultStats {
  bool ok = false;
  std::string text;
  long long faults = 0, pages_in = 0, pages_out = 0;
};

inline FaultStats read_fault_stats() {
  FaultStats s;
  glob_t g;
  if (glob("/proc/driver/nvidia-uvm/gpus/*/fault_stats", 0, nullptr, &g) != 0) { return s; }
  for (size_t i = 0; i < g.gl_pathc; i++) {
    FILE* f = fopen(g.gl_pathv[i], "r");
    if (!f) { continue; }
    s.ok = true;
    char line[256], key[64];
    long long value;
    while (fgets(line, sizeof line, f)) {
      s.text += line;
      if (sscanf(line, " %63s %lld", key, &value) != 2) { continue; }
      const std::string k = key;
      if (k == "replayable_faults" || k == "non_replayable_faults") { s.faults += value; }
      if (k == "num_pages_in") { s.pages_in += value; }
      if (k == "num_pages_out") { s.pages_out += value; }
    }
    fclose(f);
  }
  globfree(&g);
  return s;
}

// wait in ms until QUIET_READINGS readings in a row are identical, -1 when unreadable
inline double wait_until_quiet() {
  const uint64_t begin = now_ns();
  FaultStats last = read_fault_stats();
  if (!last.ok) { return -1; }
  int same = 1;
  for (int poll = 0; poll < QUIET_MAX_POLLS && same < QUIET_READINGS; poll++) {
    usleep(QUIET_POLL_US);
    FaultStats now = read_fault_stats();
    same = now.text == last.text ? same + 1 : 1;
    last = now;
  }
  return (double)(now_ns() - begin) / 1e6;
}

// where the sampled pages of a host mapping are, as n0=a;n1=b;absent=c;other=d
// move_pages reports an unpopulated page as -EFAULT on kernel 6.6 (FOLL_DUMP turns a hole into
// -EFAULT) and as -ENOENT on others
inline std::string page_census(const Buffer& b) {
  std::vector<void*> pages = sampled_pages(b);
  std::vector<int> status(pages.size(), 0);
  if (syscall(SYS_move_pages, 0, (unsigned long)pages.size(), pages.data(), (void*)0, status.data(),
              0) != 0) {
    return "move_pages_errno=" + std::to_string(errno);
  }
  int cpu = 0, gpu = 0, absent = 0, other = 0;
  for (int s : status) {
    if (s == CPU_NODE) {
      cpu++;
    } else if (s == GPU_NODE) {
      gpu++;
    } else if (s == -ENOENT || s == -EFAULT) {
      absent++;
    } else {
      other++;
    }
  }
  char text[96];
  snprintf(text, sizeof text, "n%d=%d;n%d=%d;absent=%d;other=%d", CPU_NODE, cpu, GPU_NODE, gpu,
           absent, other);
  return text;
}

// one timed step, the row's columns after the cell's fixed ones
struct StepRow {
  std::string step;
  int run = 0;
  bool gpu_clock = false;
  double ns = 0;
  long long faults = -1, pages_in = -1, pages_out = -1;  // -1: unreadable
  int checksum_ok = -1;                                  // -1: no checksum in this step
};

class TransientCell {
  Recorder& rec_;
  Counters& counters_;
  RouteKernel& direct_;  // its populate() gives the reference state
  RouteKernel& copy_;    // own launch shape, attached to the direct kernel's state
  const CopyConfig copy_config_;
  const size_t bytes_;
  const int runs_;
  cudaStream_t s_;
  cudaEvent_t e0_, e1_;
  Buffer host_out_;  // direct runs' output and copy-out target
  u64* dev_out_ = nullptr;
  u64 pass_ = 0;
  uintptr_t next_hint_ = FRESH_BASE;
  int checksum_failures_ = 0;
  double quiet_ms_max_ = 0;
  // the level and round of the rows being written
  std::string member_, pair_id_, alloc_id_, census_pre_, census_post_, status_, fixed_;
  int round_ = 0;
  double quiet_ms_ = -1;

  template <class F>
  double cpu_timed(F fn) {
    counters_.start();
    const uint64_t t0 = now_ns();
    fn();
    const uint64_t t1 = now_ns();
    counters_.stop();
    return (double)(t1 - t0);
  }

  template <class F>
  double gpu_timed(F fn) {
    counters_.start();
    CU(cudaEventRecord(e0_, s_));
    fn();
    CU(cudaEventRecord(e1_, s_));
    CU(cudaEventSynchronize(e1_));
    counters_.stop();
    return event_elapsed_ns(e0_, e1_);
  }

  template <class F>
  StepRow step(const std::string& name, int run, bool gpu_clock, F fn) {
    const FaultStats before = read_fault_stats();
    StepRow r;
    r.step = name;
    r.run = run;
    r.gpu_clock = gpu_clock;
    r.ns = gpu_clock ? gpu_timed(fn) : cpu_timed(fn);
    const FaultStats after = read_fault_stats();
    if (before.ok && after.ok) {
      r.faults = after.faults - before.faults;
      r.pages_in = after.pages_in - before.pages_in;
      r.pages_out = after.pages_out - before.pages_out;
    }
    return r;
  }

  // ahp: AnonHugePages after the step in kB, or NA
  void write(const StepRow& r, const std::string& ahp) {
    Interval iv;
    iv.interval_ns = r.ns;
    iv.batch = 1;
    iv.res_pre = census_pre_;
    iv.res_post = census_post_;
    iv.status = r.checksum_ok == 0 ? "VOID_CHECKSUM" : status_;
    if (r.checksum_ok == 0) { checksum_failures_++; }
    char cols[256];
    snprintf(cols, sizeof cols, "%s,%d,%s,%.1f,%s,%lld,%lld,%lld,%d", r.step.c_str(), r.run,
             r.gpu_clock ? "gpu" : "cpu", quiet_ms_, ahp.c_str(), r.faults, r.pages_in, r.pages_out,
             r.checksum_ok);
    iv.extra = fixed_ + "," + cols;
    rec_.row(pair_id_, alloc_id_, member_, round_, iv);
  }

  static std::string ahp_of(const void* p) {
    return std::to_string(smaps_anon_huge_kb(const_cast<void*>(p)));
  }

  static std::string address(const void* p) {
    char text[32];
    snprintf(text, sizeof text, "0x%lx", (unsigned long)(uintptr_t)p);
    return text;
  }

  static u64 sum_words(const u64* p, size_t n) {
    u64 sum = 0;
    for (size_t i = 0; i < n; i++) { sum += p[i]; }
    return sum;
  }

  bool delivered(const RouteKernel& k, u64 pass) const {
    return sum_words((const u64*)host_out_.p, k.delivered_words()) == k.expected_checksum(pass);
  }

  Buffer fresh_mapping(int node, int thp) {
    Buffer b = sys_alloc(bytes_, node, thp, HOME_ALIGN_BYTES, 0, (void*)next_hint_);
    next_hint_ += round_up(b.mapsz, HOME_ALIGN_BYTES) + HOME_ALIGN_BYTES;
    return b;
  }

  void gpu_fill(u64* p) {
    const LaunchShape fill;
    transient_fill_kernel<<<fill.blocks, fill.threads, 0, s_>>>(p, bytes_ / sizeof(u64));
    CU(cudaGetLastError());
  }

  void copy_in(const u64* host, u64* dev) {
    const u64 lines = bytes_ / GPU_LINE_BYTES;
    const size_t chunk = copy_config_.chunk_bytes();
    const u64 chunk_lines = chunk ? chunk / GPU_LINE_BYTES : lines;
    for (u64 first = 0; first < lines; first += chunk_lines) {
      CopyRegion r;
      r.first = first;
      r.count = std::min(chunk_lines, lines - first);
      copy_region(copy_config_, host, dev, r, s_);
    }
  }

  void copy_out() {
    copy_out_words(copy_config_, dev_out_, (u64*)host_out_.p, copy_.delivered_words(), s_);
  }

  // the direct route on a host mapping populated by the level
  void host_level(const TransientLevel& l) {
    Buffer b = fresh_mapping(l.node, l.thp);
    u64* p = (u64*)b.p;
    alloc_id_ = address(p);
    census_pre_ = page_census(b);
    std::vector<StepRow> population;
    if (l.fill == "register") {
      population.push_back(step("register", 0, false, [&]() {
        CU(cudaHostRegister(p, bytes_, cudaHostRegisterDefault));
      }));
    }
    if (l.fill == "gpu") {
      population.push_back(step("fill", 0, true, [&]() { gpu_fill(p); }));
    } else if (l.fill == "cpu-one") {
      population.push_back(step("fill", 0, false, [&]() { fill_words(p, bytes_ / sizeof(u64)); }));
    } else {
      population.push_back(
          step("fill", 0, false, [&]() { fill_all_cores(p, bytes_ / sizeof(u64)); }));
    }
    census_post_ = page_census(b);
    const std::string ahp = ahp_of(p);
    for (const StepRow& r : population) { write(r, ahp); }
    for (int run = 1; run <= runs_; run++) {
      const u64 pass = pass_++;
      StepRow r = step("run", run, true, [&]() { direct_.launch(p, (u64*)host_out_.p, pass, s_); });
      r.checksum_ok = delivered(direct_, pass);
      write(r, run == runs_ ? ahp_of(p) : "NA");
    }
    if (l.fill == "register") {
      write(step("unregister", 0, false, [&]() { CU(cudaHostUnregister(p)); }), "NA");
    }
    write(step("unmap", 0, false, [&]() { free_buffer(b); }), "NA");
  }

  // the copy route on a host mapping populated by the home recipe
  void copy_level(const TransientLevel& l) {
    Buffer b = fresh_mapping(CPU_NODE, 0);
    u64* p = (u64*)b.p;
    alloc_id_ = address(p);
    census_pre_ = page_census(b);
    const bool registered = copy_config_.memory == "registered";
    std::vector<StepRow> population;
    population.push_back(
        step("fill", 0, false, [&]() { fill_all_cores(p, bytes_ / sizeof(u64)); }));
    if (registered) {
      population.push_back(step("register", 0, false, [&]() {
        CU(cudaHostRegister(p, bytes_, cudaHostRegisterDefault));
      }));
    }
    census_post_ = page_census(b);
    const std::string ahp = ahp_of(p);
    for (const StepRow& r : population) { write(r, ahp); }
    u64* dev = nullptr;
    write(step("malloc", 0, false, [&]() { CU(cudaMalloc(&dev, bytes_)); }), "NA");
    if (l.fill == "copy") {
      write(step("copyin", 0, true, [&]() { copy_in(p, dev); }), "NA");
      u64 pass = 0;
      for (int run = 1; run <= runs_; run++) {
        pass = pass_++;
        write(step("run", run, true, [&]() { copy_.launch(dev, dev_out_, pass, s_); }), "NA");
      }
      StepRow r = step("copyout", 0, true, [&]() { copy_out(); });
      r.checksum_ok = delivered(copy_, pass);
      write(r, "NA");
    } else {
      for (int run = 1; run <= runs_; run++) {
        const u64 pass = pass_++;
        StepRow r = step("call", run, true, [&]() {
          copy_in(p, dev);
          copy_.launch(dev, dev_out_, pass, s_);
          copy_out();
        });
        r.checksum_ok = delivered(copy_, pass);
        write(r, "NA");
      }
    }
    write(step("free", 0, false, [&]() { CU(cudaFree(dev)); }), "NA");
    if (registered) {
      write(step("unregister", 0, false, [&]() { CU(cudaHostUnregister(p)); }), "NA");
    }
    write(step("unmap", 0, false, [&]() { free_buffer(b); }), "NA");
  }

  // data born on the GPU, filled and read in cudaMalloc memory
  void device_level() {
    census_pre_ = census_post_ = "NA_DEVICE";
    u64* dev = nullptr;
    const StepRow malloc_row = step("malloc", 0, false, [&]() { CU(cudaMalloc(&dev, bytes_)); });
    alloc_id_ = address(dev);
    write(malloc_row, "NA");
    write(step("fill", 0, true, [&]() { gpu_fill(dev); }), "NA");
    u64 pass = 0;
    for (int run = 1; run <= runs_; run++) {
      pass = pass_++;
      write(step("run", run, true, [&]() { copy_.launch(dev, dev_out_, pass, s_); }), "NA");
    }
    StepRow r = step("copyout", 0, true, [&]() { copy_out(); });
    r.checksum_ok = delivered(copy_, pass);
    write(r, "NA");
    write(step("free", 0, false, [&]() { CU(cudaFree(dev)); }), "NA");
  }

 public:
  TransientCell(Recorder& rec, Counters& counters, RouteKernel& direct, RouteKernel& copy,
                const CopyConfig& copy_config, size_t bytes, int runs)
      : rec_(rec),
        counters_(counters),
        direct_(direct),
        copy_(copy),
        copy_config_(copy_config),
        bytes_(bytes),
        runs_(runs) {
    CU(cudaStreamCreateWithFlags(&s_, cudaStreamNonBlocking));
    CU(cudaEventCreate(&e0_));
    CU(cudaEventCreate(&e1_));
    const size_t out_bytes = round_up(
        std::max(direct_.output_words(), copy_.output_words()) * sizeof(u64), page_bytes());
    host_out_ = sys_alloc(out_bytes, CPU_NODE, 0, HOME_ALIGN_BYTES);
    memset(host_out_.p, 0, out_bytes);
    CU(cudaMalloc(&dev_out_, out_bytes));
  }

  // reference state and one checked run of each route, on a scratch mapping freed afterwards
  bool prepare() {
    Buffer scratch = sys_alloc(bytes_, CPU_NODE, 0, HOME_ALIGN_BYTES);
    direct_.populate((u64*)scratch.p);
    copy_.attach(direct_);
    const u64 direct_pass = pass_++;
    direct_.launch((const u64*)scratch.p, (u64*)host_out_.p, direct_pass, s_);
    CU(cudaStreamSynchronize(s_));
    const bool direct_ok = delivered(direct_, direct_pass);
    u64* dev = nullptr;
    CU(cudaMalloc(&dev, bytes_));
    const u64 copy_pass = pass_++;
    copy_in((const u64*)scratch.p, dev);
    copy_.launch(dev, dev_out_, copy_pass, s_);
    copy_out();
    CU(cudaStreamSynchronize(s_));
    const bool copy_ok = delivered(copy_, copy_pass);
    CU(cudaFree(dev));
    free_buffer(scratch);
    if (!direct_ok || !copy_ok) {
      fprintf(stderr, "prepare: checksum direct=%d copy=%d: cell refused\n", direct_ok, copy_ok);
    }
    return direct_ok && copy_ok;
  }

  void run_level(const TransientLevel& l, int round) {
    round_ = round;
    member_ = l.name;
    pair_id_ = "round=" + std::to_string(round);
    status_ = round == 0 ? "WARMUP" : "OK";
    char fixed[512];
    snprintf(fixed, sizeof fixed, "%s,%zu,%s,%s,%s,%d,%d,%s", direct_.name(), bytes_,
             direct_.knob_values().c_str(), l.name.c_str(), l.fill.c_str(), l.node, l.thp,
             (l.fill == "copy" || l.fill == "copy-calls" || l.fill == "gpu-device")
                 ? copy_config_.label().c_str()
                 : "-");
    fixed_ = fixed;
    quiet_ms_ = wait_until_quiet();
    quiet_ms_max_ = std::max(quiet_ms_max_, quiet_ms_);
    if (l.fill == "gpu-device") {
      device_level();
    } else if (l.fill == "copy" || l.fill == "copy-calls") {
      copy_level(l);
    } else {
      host_level(l);
    }
  }

  std::string summary(int rounds, int levels, int cpus) const {
    char line[256];
    snprintf(line, sizeof line,
             "transient rounds=%d levels=%d runs=%d checksum_failures=%d quiet_ms_max=%.0f "
             "cpus_allowed=%d",
             rounds, levels, runs_, checksum_failures_, quiet_ms_max_, cpus);
    return line;
  }
};

inline std::string transient_header(const RouteKernel& k) {
  return std::string("kernel,footprint_bytes,") + k.knob_header() +
         ",level,fill,node,thp,copy,step,run,clock,quiet_ms,ahp_kb,faults,pages_in,pages_out,"
         "checksum_ok";
}

// route transient --kernel <name> --footprint-mib F --levels <level>[+<level>...] [--runs m]
//                 [--rounds R] [--process N] [--shape ...] [--copy-shape ...] [--copy <label>]
//                 <the kernel's own flags> <the run-control flags>
inline int run_transient(const Args& args) {
  const KernelEntry* entry = find_kernel(args.get("kernel", "k1"));
  std::vector<const char*> known = {
      "kernel", "placement", "footprint-mib", "levels",         "runs", "rounds",  "process",
      "shape",  "shape-hbm", "copy-shape",    "copy-shape-hbm", "copy", "copy-hbm"};
  known.insert(known.end(), entry->knobs.begin(), entry->knobs.end());
  args.check_known(known);
  args.enum_arg("placement", "cpu", {"cpu"});  // populating system memory, so CPU placement only
  const RunCtl rc = RunCtl::from(args, "transient");
  const size_t bytes = footprint_bytes(args.getf("footprint-mib", 1024));
  const LaunchShape shape = parse_shape(args.get("shape", LaunchShape().label()), "shape");
  const LaunchShape copy_shape = parse_shape(args.get("copy-shape", shape.label()), "copy-shape");
  const CopyConfig copy = CopyConfig::parse(args.get("copy", CopyConfig().label()), "copy");
  std::vector<TransientLevel> levels;
  for (const std::string& name : split(args.get("levels", "cpu-all"), '+')) {
    levels.push_back(transient_level(name));
  }
  const int runs = (int)args.geti("runs", 10), rounds = (int)args.geti("rounds", 15);
  args.geti("process", 1);  // only a label in the cell id (harness/grids.py)
  char* end;
  const unsigned long long seed = strtoull(rc.seed.c_str(), &end, 10);
  if (runs < 1 || rounds < 1 || end == rc.seed.c_str() || *end != '\0') {
    fprintf(stderr,
            "--runs and --rounds must be at least 1, and --seed the campaign seed as a number\n");
    return 2;
  }

  cpu_set_t allowed;  // the fill on all cores pins one thread to each allowed core
  CPU_ZERO(&allowed);
  sched_getaffinity(0, sizeof allowed, &allowed);
  CU(cudaSetDevice(0));
  CU(cudaFree(0));
  pin_self(TIMED_CORE);
  std::unique_ptr<RouteKernel> direct = entry->make(args, bytes, shape),
                               copy_kernel = entry->make(args, bytes, copy_shape);
  if (direct->cpu_issued() || direct->updates_in_place()) {
    fprintf(stderr, "a transient cell runs a kernel that reads its input: cell refused\n");
    return 2;
  }
  Counters counters;
  counters.open(rc.events, {{"timed", {TIMED_CORE}}});
  Recorder rec;
  rec.open(rc, transient_header(*direct), counters, TIMED_CORE);
  TransientCell cell(rec, counters, *direct, *copy_kernel, copy, bytes, runs);
  if (!cell.prepare()) { return 3; }
  for (int round = 0; round <= rounds; round++) {
    for (int i : round_order(seed, rc.cell_id, (uint64_t)round, (int)levels.size())) {
      cell.run_level(levels[i], round);
    }
  }
  const std::string summary = cell.summary(rounds, (int)levels.size(), CPU_COUNT(&allowed));
  rec.done(summary);
  fprintf(stderr, "%s\n", summary.c_str());
  return 0;
}

}  // namespace suite
