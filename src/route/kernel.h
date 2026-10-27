// the interface a kernel implements to run by both routes, README.md says how to add one
#pragma once
#include <cstdio>
#include <cstdlib>
#include <memory>
#include <string>
#include <vector>

#include "common/common.h"

namespace suite {

static const size_t GPU_LINE_BYTES = 128;  // one GPU cache line
static const u64 GPU_LINE_WORDS = GPU_LINE_BYTES / 8;

// one load of LOAD_BYTES at p, summed
template <int LOAD_BYTES>
__device__ __forceinline__ u64 load_sum(const u64* p) {
  if (LOAD_BYTES == 16) {
    const ulonglong2 v = *(const ulonglong2*)p;
    return v.x + v.y;
  }
  return *p;
}

// out[b] = sum of block b's acc values through part, one shared word per thread
// block 0 adds the pass tag. ACCUMULATE adds to out[b], for a pass in parts
template <bool ACCUMULATE = false>
__device__ __forceinline__ void store_block_sum(u64* part, u64 acc, u64 tag, u64* out) {
  part[threadIdx.x] = acc;
  __syncthreads();
  if (threadIdx.x == 0) {
    u64 s = (blockIdx.x == 0) ? tag : 0;
    for (unsigned i = 0; i < blockDim.x; i++) { s += part[i]; }
    if (ACCUMULATE) {
      atomicAdd((unsigned long long*)&out[blockIdx.x], (unsigned long long)s);
    } else {
      out[blockIdx.x] = s;
    }
  }
}

// carveout hints of K2 and K5 in percent of the SM's unified L1/shared memory, overridden by
// SUITE_CARVEOUT_<K2|K5|K5_TILES> in the environment
// the driver picks the configuration from the hint and the kernel's own needs, ncu records it as
// launch__shared_mem_config_size
static inline int carveout_hint(const char* name, int fallback) {
  const char* v = getenv(name);
  return v && *v ? atoi(v) : fallback;
}

// load_bytes is 8 or 16 where the kernel offers the choice
struct LaunchShape {
  int blocks = 528;
  int threads = 256;
  int load_bytes = 8;

  std::string label() const {
    return std::to_string(blocks) + "x" + std::to_string(threads) + "x" +
           std::to_string(load_bytes);
  }
};

class RouteKernel {
 public:
  virtual ~RouteKernel() {}
  virtual const char* name() const = 0;
  // the kernel's own knobs as row columns, comma separated
  virtual std::string knob_header() const = 0;
  virtual std::string knob_values() const = 0;
  // 128 B lines of the input one pass reads
  virtual u64 touched_lines() const = 0;
  virtual size_t output_words() const = 0;
  // output words the copy route delivers to host and the checksum covers (K5 keeps a scratch grid)
  virtual size_t delivered_words() const { return output_words(); }
  // output is the input buffer (K6). The copy route copies it in and back, so both routes keep
  // the same cumulative state
  virtual bool updates_in_place() const { return false; }
  // CPU threads issue the pass (K6). launch() runs it synchronously and the cell times it on the
  // CPU clock
  virtual bool cpu_issued() const { return false; }
  // the kernel's own device memory, for the capacity check
  virtual size_t device_bytes() const { return 0; }
  // fills the input and the reference checksums of its passes
  virtual void populate(u64* input) = 0;
  // takes over another instance's prepared state, so variants with different launch shapes share
  // one buffer
  virtual void attach(const RouteKernel& populated) = 0;
  // with the cursor on, consecutive passes read disjoint regions of the input
  // false when the kernel has no cursor for this setting
  virtual bool enable_cursor() { return false; }
  virtual bool cursor() const { return false; }
  // pass counts this variant's passes from 0 and sets the cursor position and the output tag, so
  // a stale output fails the check
  virtual void launch(const u64* input, u64* output, u64 pass, cudaStream_t s) const = 0;
  // wrap-around sum of the output words after this pass, its tag included
  virtual u64 expected_checksum(u64 pass) const = 0;

  // a pass in parts for the pipelined copy route, where part_lines gives the (first, count) line
  // ranges part k reads. Only K1, K4 and K5 split by address range
  virtual bool supports_parts() const { return false; }
  virtual void part_lines(int, int, std::vector<std::pair<u64, u64>>*) const { refuse_parts(); }
  virtual void launch_part(const u64*, u64*, u64, int, int, cudaStream_t) const { refuse_parts(); }
  virtual std::vector<int> load_widths() const { return {8}; }
  // launch shapes the direct tuning tries, empty for the general space
  virtual std::vector<LaunchShape> shape_space() const { return {}; }
  // untimed launch check once the buffers exist (K2), false voids the cell
  virtual bool verify(const u64*, cudaStream_t) { return true; }
  // for the touched-lines copy, the width lines from offset in every period lines, for this pass
  // false if the touched set is unknown before the pass runs, leaving only the whole-input copy
  virtual bool touched_window(u64, u64*, u64*, u64*) const { return false; }
  // input is a window of the buffer and the rest is room for the cursor (K2)
  // the copy route's basic copy is then the touched copy of the window, and there is no whole copy
  virtual bool input_is_window() const { return false; }
  // lines [first, first + count) a pass reads, for a host phase that prepares the next pass
  virtual void read_span(u64, u64* first, u64* count, u64 input_lines) const {
    *first = 0;
    *count = input_lines;
  }
  // sparse lines a pass reads (one per page), filled when true
  virtual bool read_lines(u64, std::vector<u64>&) const { return false; }

 protected:
  u64 tag_of(u64 pass) const { return pass + 1; }
  [[noreturn]] void refuse_parts() const {
    fprintf(stderr, "%s cannot run a pass in parts\n", name());
    exit(2);
  }
  [[noreturn]] void refuse_attach(const char* other) const {
    fprintf(stderr, "%s: cannot attach to an instance with another %s\n", name(), other);
    exit(2);
  }
};

// knobs are the kernel's flags beyond the common route flags
// set_level rewrites them for one level of a factor, exit 2 for an unknown factor or level
struct KernelEntry {
  const char* name;
  std::vector<const char*> knobs;
  std::vector<const char*> factors;
  std::unique_ptr<RouteKernel> (*make)(const Args& args, size_t input_bytes, LaunchShape shape);
  void (*set_level)(Args& args, const std::string& factor, const std::string& level);
};

const std::vector<KernelEntry>& kernels();  // kernels.cu

}  // namespace suite
