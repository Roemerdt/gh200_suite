#include <cstdio>
#include <vector>

#include "k3p_page_sparse.h"

namespace suite {

static const u64 PAGE_BYTES_64K = 64ull << 10;
static const u64 LINES_PER_PAGE = PAGE_BYTES_64K / GPU_LINE_BYTES;  // 512
static const u64 WORDS_PER_PAGE = PAGE_BYTES_64K / 8;

// an entry packs a page and the line offset in it as page << 9 | line
// 16 consecutive threads read the line's words, 8 with 16-byte loads
// phase shifts the line inside every page
template <int LOAD_BYTES>
__global__ void k3p_kernel(const u64* in, const u64* entries, u64 pages, unsigned phase, u64 tag,
                           u64* out) {
  extern __shared__ u64 part[];
  constexpr u64 WORDS = LOAD_BYTES / 8;
  constexpr u64 SLOTS_PER_LINE = GPU_LINE_WORDS / WORDS;
  const u64 n = (u64)gridDim.x * blockDim.x;
  const u64 slots = pages * SLOTS_PER_LINE;
  u64 acc = 0;
  for (u64 t = (u64)blockIdx.x * blockDim.x + threadIdx.x; t < slots; t += n) {
    const u64 entry = entries[t / SLOTS_PER_LINE];
    const u64 page = entry >> 9;
    const u64 line = (entry & (LINES_PER_PAGE - 1)) + phase;
    const u64 line_in_page = line >= LINES_PER_PAGE ? line - LINES_PER_PAGE : line;
    const u64* p =
        in + page * WORDS_PER_PAGE + line_in_page * GPU_LINE_WORDS + (t % SLOTS_PER_LINE) * WORDS;
    acc += load_sum<LOAD_BYTES>(p);
  }
  store_block_sum(part, acc, tag, out);
}

class K3PPageSparse : public RouteKernel {
  u64 pages_;
  LaunchShape shape_;
  bool cursor_ = false;
  u64* d_entries_ = nullptr;
  bool owns_device_ = true;
  std::vector<unsigned> offset_;  // the seeded line offset of each page
  std::vector<u64> class_sums_;   // per phase, word sum of the lines a pass at that phase reads

  unsigned phase_of(u64 pass) const { return cursor_ ? (unsigned)(pass % LINES_PER_PAGE) : 0; }

 public:
  K3PPageSparse(size_t input_bytes, LaunchShape shape)
      : pages_(input_bytes / PAGE_BYTES_64K), shape_(shape) {
    if (pages_ < 1) {
      fprintf(stderr, "k3p needs a footprint of at least one 64 KB page\n");
      exit(2);
    }
  }
  ~K3PPageSparse() {
    if (owns_device_ && d_entries_) { CU(cudaFree(d_entries_)); }
  }

  const char* name() const override { return "k3p"; }
  std::string knob_header() const override { return "pages"; }
  std::string knob_values() const override { return std::to_string(pages_); }
  u64 touched_lines() const override { return pages_; }
  size_t output_words() const override { return (size_t)shape_.blocks; }
  size_t device_bytes() const override { return pages_ * sizeof(u64); }
  bool cursor() const override { return cursor_; }
  std::vector<int> load_widths() const override { return {8, 16}; }
  bool enable_cursor() override {
    cursor_ = true;
    return true;
  }

  // A line's phase class is its offset in its page minus the page's seeded offset
  void populate(u64* input) override {
    uint64_t state = fnv1a64("k3p:" + std::to_string(pages_));
    offset_.resize(pages_);
    for (u64 p = 0; p < pages_; p++) {
      offset_[p] = (unsigned)(splitmix64(state) % LINES_PER_PAGE);
    }
    std::vector<std::vector<u64>> sums(fill_workers(), std::vector<u64>(LINES_PER_PAGE, 0));
    parallel_ranges(pages_ * LINES_PER_PAGE, [&](unsigned worker, u64 begin, u64 end) {
      for (u64 line = begin; line < end; line++) {
        u64 sum = 0;
        for (u64 w = 0; w < GPU_LINE_WORDS; w++) {
          const u64 value = word_value(line * GPU_LINE_WORDS + w);
          input[line * GPU_LINE_WORDS + w] = value;
          sum += value;
        }
        const u64 page = line / LINES_PER_PAGE;
        const unsigned cls =
            (unsigned)((line % LINES_PER_PAGE + LINES_PER_PAGE - offset_[page]) % LINES_PER_PAGE);
        sums[worker][cls] += sum;
      }
    });
    class_sums_.assign(LINES_PER_PAGE, 0);
    for (const std::vector<u64>& s : sums) {
      for (u64 c = 0; c < LINES_PER_PAGE; c++) { class_sums_[c] += s[c]; }
    }
    std::vector<u64> entries(pages_);
    for (u64 p = 0; p < pages_; p++) { entries[p] = (p << 9) | offset_[p]; }
    for (u64 i = pages_ - 1; i > 0; i--) {
      std::swap(entries[i], entries[splitmix64(state) % (i + 1)]);
    }
    CU(cudaMalloc(&d_entries_, pages_ * sizeof(u64)));
    CU(cudaMemcpy(d_entries_, entries.data(), pages_ * sizeof(u64), cudaMemcpyHostToDevice));
  }

  void attach(const RouteKernel& populated) override {
    const K3PPageSparse& other = dynamic_cast<const K3PPageSparse&>(populated);
    if (other.pages_ != pages_) { refuse_attach("input"); }
    d_entries_ = other.d_entries_;
    owns_device_ = false;
    offset_ = other.offset_;
    class_sums_ = other.class_sums_;
  }

  void launch(const u64* input, u64* output, u64 pass, cudaStream_t s) const override {
    const size_t shared_bytes = (size_t)shape_.threads * sizeof(u64);
    if (shape_.load_bytes == 16) {
      k3p_kernel<16><<<shape_.blocks, shape_.threads, shared_bytes, s>>>(
          input, d_entries_, pages_, phase_of(pass), tag_of(pass), output);
    } else {
      k3p_kernel<8><<<shape_.blocks, shape_.threads, shared_bytes, s>>>(
          input, d_entries_, pages_, phase_of(pass), tag_of(pass), output);
    }
  }

  u64 expected_checksum(u64 pass) const override {
    return class_sums_[phase_of(pass)] + tag_of(pass);
  }

  // one line per page, at the page's offset shifted by the phase
  bool read_lines(u64 pass, std::vector<u64>& lines) const override {
    const unsigned phase = phase_of(pass);
    lines.resize(pages_);
    for (u64 p = 0; p < pages_; p++) {
      lines[p] = p * LINES_PER_PAGE + (offset_[p] + phase) % LINES_PER_PAGE;
    }
    return true;
  }
};

static std::unique_ptr<RouteKernel> make_k3p(const Args&, size_t input_bytes, LaunchShape shape) {
  return std::unique_ptr<RouteKernel>(new K3PPageSparse(input_bytes, shape));
}

static void k3p_set_level(Args&, const std::string& factor, const std::string&) {
  bad_flag_value("vary", factor, "is not a factor of k3p, which has none of its own");
}

const KernelEntry K3P_PAGE_SPARSE = {"k3p", {}, {}, make_k3p, k3p_set_level};

}  // namespace suite
