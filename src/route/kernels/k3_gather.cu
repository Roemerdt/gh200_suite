#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

#include <cub/device/device_radix_sort.cuh>

#include "k3_gather.h"

namespace suite {

static const u64 GATHER_WINDOW_WORDS = (2ull << 30) / 8;  // a 2 GiB window of the partition level
static const int WINDOW_BIT = 28;                         // log2 of GATHER_WINDOW_WORDS

__global__ void k3_gather_kernel(const u64* in, const u64* idx, u64 gathers, u64 tag, u64* out) {
  extern __shared__ u64 part[];
  const u64 n = (u64)gridDim.x * blockDim.x;
  u64 acc = 0;
  for (u64 g = (u64)blockIdx.x * blockDim.x + threadIdx.x; g < gathers; g += n) {
    acc += in[idx[g]];
  }
  store_block_sum(part, acc, tag, out);
}

class K3Gather : public RouteKernel {
  u64 words_, lines_, gathers_;
  std::string page_order_, partition_, index_order_;
  LaunchShape shape_;
  u64* d_idx_ = nullptr;   // indices, ordered by the page-order and index-order levels
  u64* d_work_ = nullptr;  // sort output at set-up, bucketed indices during a pass
  void* d_temp_ = nullptr;
  size_t temp_bytes_ = 0;
  bool owns_device_ = true;  // false after attach, the arrays are another instance's
  int windows_ = 1;
  u64 base_sum_ = 0, touched_lines_ = 0;
  double setup_ns_ = 0;

  int window_bits() const {
    int bits = 0;
    while ((1 << bits) < windows_) { bits++; }
    return bits;
  }

  // the expected lines touched by uniform random gathers, for the cursor decision before population
  u64 estimated_touched_lines() const {
    const double expected = (double)lines_ * (1.0 - exp(-(double)gathers_ / (double)lines_));
    return (u64)expected;
  }

  void sort_on_device(cudaStream_t s, int begin_bit, int end_bit) {
    size_t needed = 0;
    CU(cub::DeviceRadixSort::SortKeys(nullptr, needed, d_idx_, d_work_, gathers_, begin_bit,
                                      end_bit, s));
    if (needed > temp_bytes_) {
      if (d_temp_) { CU(cudaFree(d_temp_)); }
      CU(cudaMalloc(&d_temp_, needed));
      temp_bytes_ = needed;
    }
    CU(cub::DeviceRadixSort::SortKeys(d_temp_, temp_bytes_, d_idx_, d_work_, gathers_, begin_bit,
                                      end_bit, s));
  }

 public:
  K3Gather(size_t input_bytes, long gathers, const std::string& page_order,
           const std::string& partition, const std::string& index_order, LaunchShape shape)
      : words_(input_bytes / sizeof(u64)),
        lines_(input_bytes / GPU_LINE_BYTES),
        gathers_((u64)gathers),
        page_order_(page_order),
        partition_(partition),
        index_order_(index_order),
        shape_(shape) {
    if (partition_ == "2g") {
      windows_ = (int)((words_ + GATHER_WINDOW_WORDS - 1) / GATHER_WINDOW_WORDS);
      if (windows_ < 2) {
        fprintf(
            stderr,
            "--partition=2g needs a footprint above 2 GiB: one window has nothing to partition\n");
        exit(2);
      }
    }
    if (index_order_ == "sorted" && page_order_ != "random") {
      fprintf(stderr,
              "--index-order=sorted leaves no page order to choose: use --page-order random\n");
      exit(2);
    }
  }

  ~K3Gather() {
    if (!owns_device_) { return; }
    if (d_idx_) { CU(cudaFree(d_idx_)); }
    if (d_work_) { CU(cudaFree(d_work_)); }
    if (d_temp_) { CU(cudaFree(d_temp_)); }
  }

  // sharing the index arrays and work space is safe, a cell's variants never run at once
  void attach(const RouteKernel& populated) override {
    const K3Gather& other = dynamic_cast<const K3Gather&>(populated);
    if (other.words_ != words_ || other.gathers_ != gathers_ || other.page_order_ != page_order_ ||
        other.partition_ != partition_ || other.index_order_ != index_order_) {
      refuse_attach("input or level");
    }
    d_idx_ = other.d_idx_;
    d_work_ = other.d_work_;
    d_temp_ = other.d_temp_;
    temp_bytes_ = other.temp_bytes_;
    owns_device_ = false;
    base_sum_ = other.base_sum_;
    touched_lines_ = other.touched_lines_;
    setup_ns_ = other.setup_ns_;
  }

  const char* name() const override { return "k3"; }
  std::string knob_header() const override {
    return "gathers,page_order,partition,index_order,setup_ns";
  }
  std::string knob_values() const override {
    char buf[160];
    snprintf(buf, sizeof buf, "%llu,%s,%s,%s,%.0f", gathers_, page_order_.c_str(),
             partition_.c_str(), index_order_.c_str(), setup_ns_);
    return buf;
  }
  u64 touched_lines() const override {
    return touched_lines_ ? touched_lines_ : estimated_touched_lines();
  }
  size_t output_words() const override { return (size_t)shape_.blocks; }
  size_t device_bytes() const override {
    const bool two_arrays = partition_ == "2g" || index_order_ == "sorted";
    return gathers_ * sizeof(u64) * (two_arrays ? 2 : 1) + (64ull << 20);
  }

  // The indices come from a fixed seed, the same for every variant of the footprint
  void populate(u64* input) override {
    parallel_ranges(words_, [&](unsigned, u64 begin, u64 end) {
      for (u64 i = begin; i < end; i++) { input[i] = word_value(i); }
    });
    std::vector<u64> idx(gathers_);
    uint64_t state = fnv1a64("k3:" + std::to_string(words_) + ":" + std::to_string(gathers_));
    std::vector<uint64_t> touched((lines_ + 63) / 64, 0);
    base_sum_ = 0;
    for (u64 g = 0; g < gathers_; g++) {
      idx[g] = splitmix64(state) % words_;
      base_sum_ += word_value(idx[g]);
      const u64 line = idx[g] / GPU_LINE_WORDS;
      touched[line / 64] |= 1ull << (line % 64);
    }
    touched_lines_ = 0;
    for (uint64_t word : touched) { touched_lines_ += (u64)__builtin_popcountll(word); }
    if (page_order_ == "64k" || page_order_ == "2m") {
      const int shift = page_order_ == "64k" ? 13 : 18;  // log2 of words per 64 KB page, 2 MB block
      std::stable_sort(idx.begin(), idx.end(),
                       [shift](u64 a, u64 b) { return (a >> shift) < (b >> shift); });
    }
    CU(cudaMalloc(&d_idx_, gathers_ * sizeof(u64)));
    CU(cudaMemcpy(d_idx_, idx.data(), gathers_ * sizeof(u64), cudaMemcpyHostToDevice));
    if (partition_ == "2g" || index_order_ == "sorted") {
      CU(cudaMalloc(&d_work_, gathers_ * sizeof(u64)));
    }
    if (index_order_ == "sorted") {
      cudaEvent_t e0, e1;
      CU(cudaEventCreate(&e0));
      CU(cudaEventCreate(&e1));
      setup_ns_ = gpu_timed_ns(e0, e1, 0, [&]() { sort_on_device(0, 0, 64); });
      std::swap(d_idx_, d_work_);
      CU(cudaEventDestroy(e0));
      CU(cudaEventDestroy(e1));
    }
    if (partition_ == "2g") {
      sort_on_device(0, WINDOW_BIT, WINDOW_BIT + window_bits());
    }  // sizes the work space
    CU(cudaDeviceSynchronize());
  }

  void launch(const u64* input, u64* output, u64 pass, cudaStream_t s) const override {
    const u64* idx = d_idx_;
    if (partition_ == "2g") {
      size_t temp_bytes = temp_bytes_;
      CU(cub::DeviceRadixSort::SortKeys(d_temp_, temp_bytes, d_idx_, d_work_, gathers_, WINDOW_BIT,
                                        WINDOW_BIT + window_bits(), s));
      idx = d_work_;
    }
    const size_t shared_bytes = (size_t)shape_.threads * sizeof(u64);
    k3_gather_kernel<<<shape_.blocks, shape_.threads, shared_bytes, s>>>(input, idx, gathers_,
                                                                         tag_of(pass), output);
  }

  u64 expected_checksum(u64 pass) const override { return base_sum_ + tag_of(pass); }
};

static std::unique_ptr<RouteKernel> make_k3(const Args& args, size_t input_bytes,
                                            LaunchShape shape) {
  const long gathers = args.geti("gathers", 16777216);
  if (gathers < 1) {
    fprintf(stderr, "--gathers must be at least 1\n");
    exit(2);
  }
  return std::unique_ptr<RouteKernel>(new K3Gather(
      input_bytes, gathers, args.enum_arg("page-order", "random", {"random", "64k", "2m"}),
      args.enum_arg("partition", "none", {"none", "2g"}),
      args.enum_arg("index-order", "random", {"random", "sorted"}), shape));
}

// each factor is one knob
static void k3_set_level(Args& args, const std::string& factor, const std::string& level) {
  if (factor != "page-order" && factor != "partition" && factor != "index-order") {
    bad_flag_value("vary", factor, "is not a factor of k3 (page-order, partition, index-order)");
  }
  args.set(factor, level);
}

const KernelEntry K3_GATHER = {"k3",
                               {"gathers", "page-order", "partition", "index-order"},
                               {"page-order", "partition", "index-order"},
                               make_k3,
                               k3_set_level};

}  // namespace suite
