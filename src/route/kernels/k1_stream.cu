#include <algorithm>
#include <cstdio>
#include <vector>

#include "k1_stream.h"

namespace suite {

// touched word t is in touched line q = t / 16, buffer line (q / g) * G + (q % g + phase) mod G
// phase is 0 without the cursor and advances by g per pass with it
// the last group may be partial, so lines past the end are skipped
// thread i reads t = i, i + n, ..., so a warp reads 256 contiguous bytes per step with 8 B loads
template <int LOAD_BYTES, bool ACCUMULATE>
__global__ void k1_stream_kernel(const u64* in, u64 lines, u64 t_begin, u64 t_end, unsigned g,
                                 unsigned G, unsigned phase, u64 tag, u64* out) {
  extern __shared__ u64 part[];
  constexpr u64 WORDS = LOAD_BYTES / 8;  // words per load
  const u64 n = (u64)gridDim.x * blockDim.x * WORDS;
  u64 acc = 0;
  for (u64 t = t_begin + ((u64)blockIdx.x * blockDim.x + threadIdx.x) * WORDS; t < t_end; t += n) {
    const unsigned q = (unsigned)(t / GPU_LINE_WORDS);
    const unsigned group = q / g;
    unsigned r = q - group * g + phase;
    if (r >= G) { r -= G; }
    const u64 line = (u64)group * G + r;
    if (line < lines) {
      acc += load_sum<LOAD_BYTES>(in + line * GPU_LINE_WORDS + t % GPU_LINE_WORDS);
    }
  }
  store_block_sum<ACCUMULATE>(part, acc, tag, out);
}

class K1Stream : public RouteKernel {
  u64 lines_, g_, G_;
  LaunchShape shape_;
  bool cursor_ = false;
  std::vector<u64> residue_sums_;  // word sum of the lines per residue line % G

  unsigned phase_of(u64 pass) const { return cursor_ ? (unsigned)((pass * g_) % G_) : 0; }
  // touched words of a pass, the partial last group counted as whole
  u64 words_to_visit() const { return (lines_ + G_ - 1) / G_ * g_ * GPU_LINE_WORDS; }
  // the touched words of part k of parts, on line boundaries
  void part_words(int k, int parts, u64* begin, u64* end) const {
    const u64 q_total = words_to_visit() / GPU_LINE_WORDS;
    *begin = q_total * k / parts * GPU_LINE_WORDS;
    *end = q_total * (k + 1) / parts * GPU_LINE_WORDS;
  }

  template <bool ACCUMULATE>
  void launch_range(const u64* input, u64* output, u64 pass, u64 t_begin, u64 t_end, bool with_tag,
                    cudaStream_t s) const {
    const size_t shared_bytes = (size_t)shape_.threads * sizeof(u64);
    const u64 tag = with_tag ? tag_of(pass) : 0;
    if (shape_.load_bytes == 16) {
      k1_stream_kernel<16, ACCUMULATE><<<shape_.blocks, shape_.threads, shared_bytes, s>>>(
          input, lines_, t_begin, t_end, (unsigned)g_, (unsigned)G_, phase_of(pass), tag, output);
    } else {
      k1_stream_kernel<8, ACCUMULATE><<<shape_.blocks, shape_.threads, shared_bytes, s>>>(
          input, lines_, t_begin, t_end, (unsigned)g_, (unsigned)G_, phase_of(pass), tag, output);
    }
  }

 public:
  K1Stream(size_t input_bytes, long g, long G, LaunchShape shape)
      : lines_(input_bytes / GPU_LINE_BYTES), g_((u64)g), G_((u64)G), shape_(shape) {}

  const char* name() const override { return "k1"; }
  std::string knob_header() const override { return "f_num,f_den"; }
  std::string knob_values() const override { return std::to_string(g_) + "," + std::to_string(G_); }
  // at phase 0, another phase differs by at most g lines in the partial last group
  u64 touched_lines() const override { return lines_ / G_ * g_ + std::min(lines_ % G_, g_); }
  size_t output_words() const override { return (size_t)shape_.blocks; }
  bool cursor() const override { return cursor_; }
  std::vector<int> load_widths() const override { return {8, 16}; }
  bool supports_parts() const override { return true; }
  bool touched_window(u64 pass, u64* period, u64* width, u64* offset) const override {
    *period = G_;
    *width = g_;
    *offset = phase_of(pass);
    return true;
  }

  void populate(u64* input) override {
    std::vector<std::vector<u64>> sums(fill_workers(), std::vector<u64>(G_, 0));
    parallel_ranges(lines_, [&](unsigned worker, u64 begin, u64 end) {
      for (u64 line = begin; line < end; line++) {
        u64 sum = 0;
        for (u64 w = 0; w < GPU_LINE_WORDS; w++) {
          const u64 value = word_value(line * GPU_LINE_WORDS + w);
          input[line * GPU_LINE_WORDS + w] = value;
          sum += value;
        }
        sums[worker][line % G_] += sum;
      }
    });
    residue_sums_.assign(G_, 0);
    for (const std::vector<u64>& s : sums) {
      for (u64 r = 0; r < G_; r++) { residue_sums_[r] += s[r]; }
    }
  }

  void attach(const RouteKernel& populated) override {
    const K1Stream& other = dynamic_cast<const K1Stream&>(populated);
    if (other.lines_ != lines_ || other.g_ != g_ || other.G_ != G_) {
      refuse_attach("input or fraction");
    }
    residue_sums_ = other.residue_sums_;
  }

  // consecutive passes read disjoint lines when a group holds at least two phases
  bool enable_cursor() override {
    if (G_ < 2 * g_) { return false; }
    cursor_ = true;
    return true;
  }

  void launch(const u64* input, u64* output, u64 pass, cudaStream_t s) const override {
    launch_range<false>(input, output, pass, 0, words_to_visit(), true, s);
  }

  // part k reads from the first group of its touched lines to the end of the last
  void part_lines(int k, int parts, std::vector<std::pair<u64, u64>>* ranges) const override {
    u64 begin, end;
    part_words(k, parts, &begin, &end);
    const u64 q0 = begin / GPU_LINE_WORDS, q1 = end / GPU_LINE_WORDS;
    const u64 first = (q0 / g_) * G_;
    const u64 last = q1 == q0 ? first : std::min(lines_, ((q1 - 1) / g_ + 1) * G_);
    ranges->push_back({first, last - first});
  }

  // parts add into the output, which the caller clears before the first part
  void launch_part(const u64* input, u64* output, u64 pass, int k, int parts,
                   cudaStream_t s) const override {
    u64 begin, end;
    part_words(k, parts, &begin, &end);
    launch_range<true>(input, output, pass, begin, end, k == 0, s);
  }

  u64 expected_checksum(u64 pass) const override {
    const unsigned phase = phase_of(pass);
    u64 sum = tag_of(pass);
    for (u64 j = 0; j < g_; j++) { sum += residue_sums_[(phase + j) % G_]; }
    return sum;
  }
};

static std::unique_ptr<RouteKernel> make_k1(const Args& args, size_t input_bytes,
                                            LaunchShape shape) {
  const long g = args.geti("f-num", 1), G = args.geti("f-den", 1);
  if (g < 1 || G < g) {
    fprintf(stderr, "--f-num and --f-den must give a fraction above 0 and at most 1\n");
    exit(2);
  }
  return std::unique_ptr<RouteKernel>(new K1Stream(input_bytes, g, G, shape));
}

// level <g>of<G> of factor f sets --f-num and --f-den
static void k1_set_level(Args& args, const std::string& factor, const std::string& level) {
  if (factor != "f") { bad_flag_value("vary", factor, "is not a factor of k1 (f)"); }
  long g, G;
  char tail;
  if (sscanf(level.c_str(), "%ldof%ld%c", &g, &G, &tail) != 2) {
    bad_flag_value("at", level, "is not a touched fraction written <g>of<G>");
  }
  args.set("f-num", std::to_string(g));
  args.set("f-den", std::to_string(G));
}

const KernelEntry K1_STREAM = {"k1", {"f-num", "f-den"}, {"f"}, make_k1, k1_set_level};

}  // namespace suite
