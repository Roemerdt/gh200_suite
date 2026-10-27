#include <cstdio>
#include <vector>

#include <cuda/atomic>

#include "k2_reuse.h"

namespace suite {

static const size_t K2_SHARED_BYTES = 116
                                      << 10;  // the request that leaves room for one block per SM
static const int K2_CARVEOUT =
    carveout_hint("SUITE_CARVEOUT_K2", 50);  // the hint that gives the 132 KiB configuration

enum K2Scope { SCOPE_NONE = 0, SCOPE_CTA = 1, SCOPE_GPU = 2, SCOPE_SYS = 3 };

template <int SCOPE>
__device__ __forceinline__ void acquire_fence() {
  if (SCOPE == SCOPE_CTA) {
    cuda::atomic_thread_fence(cuda::std::memory_order_acquire, cuda::thread_scope_block);
  }
  if (SCOPE == SCOPE_GPU) {
    cuda::atomic_thread_fence(cuda::std::memory_order_acquire, cuda::thread_scope_device);
  }
  if (SCOPE == SCOPE_SYS) {
    cuda::atomic_thread_fence(cuda::std::memory_order_acquire, cuda::thread_scope_system);
  }
}

// block b reads slice b of the window k times, or slice (b + j) mod blocks on read j when rotated
// a fence and a barrier follow every read, SCOPE_NONE keeps the barrier so only the fence differs
// with tiles the first read stages the slice in shared memory for the rereads
// COUNT records each block's SM and the reads per slice, for the launch check
template <int LOAD_BYTES, int SCOPE, bool COUNT>
__global__ void k2_reuse_kernel(const u64* in, u64 window_words, u64 slice_words, int k,
                                int rotated, int tiles, u64 tag, u64* out, unsigned* smid_of_block,
                                unsigned* reads_of_slice) {
  extern __shared__ u64 part[];
  u64* tile = part + blockDim.x;
  constexpr u64 WORDS = LOAD_BYTES / 8;
  const u64* window = in + window_words;
  u64 acc = 0;
  if (COUNT && threadIdx.x == 0) {
    unsigned smid;
    asm("mov.u32 %0, %%smid;" : "=r"(smid));
    smid_of_block[blockIdx.x] = smid;
  }
  for (int j = 0; j < k; j++) {
    const int s = rotated ? (int)((blockIdx.x + j) % gridDim.x) : (int)blockIdx.x;
    const u64* slice = window + (u64)s * slice_words;
    if (tiles && j > 0) {
      for (u64 w = (u64)threadIdx.x * WORDS; w < slice_words; w += (u64)blockDim.x * WORDS) {
        acc += load_sum<LOAD_BYTES>(tile + w);
      }
    } else {
      for (u64 w = (u64)threadIdx.x * WORDS; w < slice_words; w += (u64)blockDim.x * WORDS) {
        if (LOAD_BYTES == 16) {
          const ulonglong2 v = *(const ulonglong2*)(slice + w);
          acc += v.x + v.y;
          if (tiles) { *(ulonglong2*)(tile + w) = v; }
        } else {
          const u64 v = slice[w];
          acc += v;
          if (tiles) { tile[w] = v; }
        }
      }
    }
    if (COUNT && threadIdx.x == 0) { atomicAdd(&reads_of_slice[s], 1u); }
    acquire_fence<SCOPE>();
    __syncthreads();
  }
  store_block_sum(part, acc, tag, out);
}

class K2Reuse : public RouteKernel {
  u64 input_lines_, working_set_bytes_, slice_lines_, windows_;
  int k_, rotated_;
  std::string scope_, tiling_;
  LaunchShape shape_;
  bool cursor_ = false;
  std::vector<u64> window_sums_;  // word sum of each window's slices

  u64 window_of(u64 pass) const { return cursor_ ? pass % windows_ : 0; }
  u64 window_lines() const { return working_set_bytes_ / GPU_LINE_BYTES; }
  int scope_code() const {
    return scope_ == "cta"   ? SCOPE_CTA
           : scope_ == "gpu" ? SCOPE_GPU
           : scope_ == "sys" ? SCOPE_SYS
                             : SCOPE_NONE;
  }

  template <int LOAD_BYTES, int SCOPE, bool COUNT>
  void launch_instance(const u64* input, u64* output, u64 pass, unsigned* smid, unsigned* reads,
                       cudaStream_t s) const {
    auto kernel = k2_reuse_kernel<LOAD_BYTES, SCOPE, COUNT>;
    CU(cudaFuncSetAttribute(kernel, cudaFuncAttributeMaxDynamicSharedMemorySize,
                            (int)K2_SHARED_BYTES));
    CU(cudaFuncSetAttribute(kernel, cudaFuncAttributePreferredSharedMemoryCarveout, K2_CARVEOUT));
    kernel<<<shape_.blocks, shape_.threads, K2_SHARED_BYTES, s>>>(
        input, window_of(pass) * window_lines() * GPU_LINE_WORDS, slice_lines_ * GPU_LINE_WORDS, k_,
        rotated_, tiling_ == "tiles" ? 1 : 0, tag_of(pass), output, smid, reads);
  }
  template <bool COUNT>
  void launch_by_scope(const u64* input, u64* output, u64 pass, unsigned* smid, unsigned* reads,
                       cudaStream_t s) const {
    const int scope = scope_code();
    if (shape_.load_bytes == 16) {
      if (scope == SCOPE_CTA) {
        launch_instance<16, SCOPE_CTA, COUNT>(input, output, pass, smid, reads, s);
      } else if (scope == SCOPE_GPU) {
        launch_instance<16, SCOPE_GPU, COUNT>(input, output, pass, smid, reads, s);
      } else if (scope == SCOPE_SYS) {
        launch_instance<16, SCOPE_SYS, COUNT>(input, output, pass, smid, reads, s);
      } else {
        launch_instance<16, SCOPE_NONE, COUNT>(input, output, pass, smid, reads, s);
      }
    } else {
      if (scope == SCOPE_CTA) {
        launch_instance<8, SCOPE_CTA, COUNT>(input, output, pass, smid, reads, s);
      } else if (scope == SCOPE_GPU) {
        launch_instance<8, SCOPE_GPU, COUNT>(input, output, pass, smid, reads, s);
      } else if (scope == SCOPE_SYS) {
        launch_instance<8, SCOPE_SYS, COUNT>(input, output, pass, smid, reads, s);
      } else {
        launch_instance<8, SCOPE_NONE, COUNT>(input, output, pass, smid, reads, s);
      }
    }
  }

 public:
  K2Reuse(size_t input_bytes, double working_set_mib, int k, int rotated, const std::string& scope,
          const std::string& tiling, LaunchShape shape)
      : input_lines_(input_bytes / GPU_LINE_BYTES),
        working_set_bytes_((u64)(working_set_mib * 1024.0 * 1024.0) / GPU_LINE_BYTES *
                           GPU_LINE_BYTES),
        k_(k),
        rotated_(rotated),
        scope_(scope),
        tiling_(tiling),
        shape_(shape) {
    shape_.blocks = SMS;  // one block per SM
    if (working_set_bytes_ > input_bytes) {
      fprintf(stderr, "--working-set-mib is larger than the footprint\n");
      exit(2);
    }
    slice_lines_ = window_lines() / (u64)SMS;
    if (slice_lines_ < 1) {
      fprintf(stderr, "the working set gives less than one line per SM\n");
      exit(2);
    }
    // the tile and the per-thread partial sums (up to 1024 threads) share the dynamic shared memory
    if (tiling_ == "tiles" &&
        (rotated_ || slice_lines_ * GPU_LINE_BYTES + 1024 * sizeof(u64) > K2_SHARED_BYTES)) {
      fprintf(stderr, "--tiling tiles needs a slice of at most %zu KiB and no rotation\n",
              (K2_SHARED_BYTES - 1024 * sizeof(u64)) >> 10);
      exit(2);
    }
    windows_ = input_lines_ / window_lines();
  }

  const char* name() const override { return "k2"; }
  std::string knob_header() const override {
    return "working_set_bytes,k,rotated,scope,tiling,slice_lines,carveout";
  }
  std::string knob_values() const override {
    return std::to_string(working_set_bytes_) + "," + std::to_string(k_) + "," +
           std::to_string(rotated_) + "," + scope_ + "," + tiling_ + "," +
           std::to_string(slice_lines_) + "," + std::to_string(K2_CARVEOUT);
  }
  u64 touched_lines() const override { return slice_lines_ * (u64)SMS; }
  size_t output_words() const override { return (size_t)SMS; }
  std::vector<int> load_widths() const override { return {8, 16}; }
  bool cursor() const override { return cursor_; }
  bool enable_cursor() override {
    if (windows_ < 2) { return false; }
    cursor_ = true;
    return true;
  }
  bool input_is_window() const override { return true; }
  // a pass touches its window, one group spanning the input
  bool touched_window(u64 pass, u64* period, u64* width, u64* offset) const override {
    *period = input_lines_;
    *width = slice_lines_ * (u64)SMS;
    *offset = window_of(pass) * window_lines();
    return true;
  }
  // one block per SM, so only the warps per block and the load width are tuned
  std::vector<LaunchShape> shape_space() const override {
    std::vector<LaunchShape> shapes;
    for (int threads : {32, 64, 128, 256, 512, 1024}) {
      for (int load : {8, 16}) { shapes.push_back({SMS, threads, load}); }
    }
    return shapes;
  }
  void read_span(u64 pass, u64* first, u64* count, u64) const override {
    *first = window_of(pass) * window_lines();
    *count = slice_lines_ * (u64)SMS;
  }

  void populate(u64* input) override {
    const u64 words = input_lines_ * GPU_LINE_WORDS;
    parallel_ranges(words, [&](unsigned, u64 begin, u64 end) {
      for (u64 i = begin; i < end; i++) { input[i] = word_value(i); }
    });
    window_sums_.assign(windows_, 0);
    const u64 read_words = slice_lines_ * (u64)SMS * GPU_LINE_WORDS;
    for (u64 w = 0; w < windows_; w++) {
      const u64 base = w * window_lines() * GPU_LINE_WORDS;
      u64 sum = 0;
      for (u64 i = 0; i < read_words; i++) { sum += word_value(base + i); }
      window_sums_[w] = sum;
    }
  }
  void attach(const RouteKernel& populated) override {
    const K2Reuse& other = dynamic_cast<const K2Reuse&>(populated);
    if (other.input_lines_ != input_lines_ || other.working_set_bytes_ != working_set_bytes_) {
      refuse_attach("input or working set");
    }
    window_sums_ = other.window_sums_;
  }

  void launch(const u64* input, u64* output, u64 pass, cudaStream_t s) const override {
    launch_by_scope<false>(input, output, pass, nullptr, nullptr, s);
  }
  u64 expected_checksum(u64 pass) const override {
    return (u64)k_ * window_sums_[window_of(pass)] + tag_of(pass);
  }

  // untimed counting pass, every SM must run exactly one block and every slice be read k times
  bool verify(const u64* input, cudaStream_t s) override {
    unsigned *smid, *reads;
    u64* out;
    CU(cudaMalloc(&smid, SMS * sizeof(unsigned)));
    CU(cudaMalloc(&reads, SMS * sizeof(unsigned)));
    CU(cudaMalloc(&out, SMS * sizeof(u64)));
    CU(cudaMemset(reads, 0, SMS * sizeof(unsigned)));
    launch_by_scope<true>(input, out, 0, smid, reads, s);
    CU(cudaGetLastError());
    CU(cudaStreamSynchronize(s));
    std::vector<unsigned> smids(SMS), counts(SMS);
    CU(cudaMemcpy(smids.data(), smid, SMS * sizeof(unsigned), cudaMemcpyDeviceToHost));
    CU(cudaMemcpy(counts.data(), reads, SMS * sizeof(unsigned), cudaMemcpyDeviceToHost));
    CU(cudaFree(smid));
    CU(cudaFree(reads));
    CU(cudaFree(out));
    std::vector<int> per_sm(SMS, 0);
    bool ok = true;
    for (unsigned id : smids) {
      if (id >= (unsigned)SMS) {
        ok = false;
      } else {
        per_sm[id]++;
      }
    }
    for (int sm = 0; sm < SMS && ok; sm++) { ok = per_sm[sm] == 1; }
    for (int sl = 0; sl < SMS && ok; sl++) { ok = counts[sl] == (unsigned)k_; }
    if (!ok) {
      fprintf(stderr,
              "k2: the blocks did not cover every SM once, or a slice was not read k times\n");
    }
    return ok;
  }
};

static std::unique_ptr<RouteKernel> make_k2(const Args& args, size_t input_bytes,
                                            LaunchShape shape) {
  const long k = args.geti("k", 16), rotated = args.geti("rotated", 0);
  if (k < 1 || (rotated != 0 && rotated != 1)) {
    fprintf(stderr, "--k must be at least 1 and --rotated 0 or 1\n");
    exit(2);
  }
  return std::unique_ptr<RouteKernel>(
      new K2Reuse(input_bytes, args.getf("working-set-mib", 32), (int)k, (int)rotated,
                  args.enum_arg("scope", "none", {"none", "cta", "gpu", "sys"}),
                  args.enum_arg("tiling", "none", {"none", "tiles"}), shape));
}

// each factor is one knob, working-set in MiB
static void k2_set_level(Args& args, const std::string& factor, const std::string& level) {
  if (factor == "working-set") {
    args.set("working-set-mib", level);
  } else if (factor == "k" || factor == "rotated" || factor == "scope" || factor == "tiling") {
    args.set(factor, level);
  } else {
    bad_flag_value("vary", factor,
                   "is not a factor of k2 (k, working-set, rotated, scope, tiling)");
  }
}

const KernelEntry K2_REUSE = {"k2",
                              {"working-set-mib", "k", "rotated", "scope", "tiling"},
                              {"k", "working-set", "rotated", "scope", "tiling"},
                              make_k2,
                              k2_set_level};

}  // namespace suite
