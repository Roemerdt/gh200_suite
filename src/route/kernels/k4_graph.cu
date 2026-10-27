#include <algorithm>
#include <cstdio>
#include <vector>

#include "k4_graph.h"

namespace suite {

// the input holds rows + 1 row pointers, nnz column indices, nnz values and x, in that order
__global__ void k4_spmv_kernel(const u64* in, u64 rows, u64 nnz, u64 row_begin, u64 row_end,
                               u64 tag, u64* y) {
  const u64* row_ptr = in;
  const u64* col = in + rows + 1;
  const u64* val = col + nnz;
  const u64* x = val + nnz;
  const u64 n = (u64)gridDim.x * blockDim.x;
  for (u64 r = row_begin + (u64)blockIdx.x * blockDim.x + threadIdx.x; r < row_end; r += n) {
    u64 acc = 0;
    const u64 end = row_ptr[r + 1];
    for (u64 j = row_ptr[r]; j < end; j++) { acc += val[j] * x[col[j]]; }
    y[r] = acc + (r == 0 ? tag : 0);
  }
}

class K4Graph : public RouteKernel {
  u64 rows_, nnz_, degree_;
  std::string generator_;
  LaunchShape shape_;
  u64 base_sum_ = 0;
  const u64* host_row_ptr_ = nullptr;  // the populated row pointers, for the parts of a pass

  // the lines of the input holding words [w0, w1)
  static std::pair<u64, u64> lines_of(u64 w0, u64 w1) {
    const u64 first = w0 / GPU_LINE_WORDS;
    return {first, (w1 + GPU_LINE_WORDS - 1) / GPU_LINE_WORDS - first};
  }

  // R-MAT edge by recursive descent over the index space, quadrant odds 0.57, 0.19, 0.19, 0.05
  static void rmat_edge(uint64_t& state, u64 n_log2, u64* row, u64* col) {
    u64 r = 0, c = 0;
    for (u64 level = 0; level < n_log2; level++) {
      const double u = (double)(splitmix64(state) >> 11) * (1.0 / 9007199254740992.0);
      const int quadrant = u < 0.57 ? 0 : u < 0.76 ? 1 : u < 0.95 ? 2 : 3;
      r = (r << 1) | (quadrant >> 1);
      c = (c << 1) | (quadrant & 1);
    }
    *row = r;
    *col = c;
  }
  // per-item generator state, the seed advanced by the item's index
  static uint64_t splitmix64_at(uint64_t seed, u64 item) {
    uint64_t s = seed ^ (item * 0x9E3779B97F4A7C15ull);
    splitmix64(s);
    return s;
  }

 public:
  K4Graph(size_t input_bytes, const std::string& generator, long degree, LaunchShape shape)
      : generator_(generator), degree_((u64)degree), shape_(shape) {
    // a row costs its pointer, its x word, and degree indices and values
    rows_ = input_bytes / (8 * (2 + 2 * degree_));
    nnz_ = rows_ * degree_;
    if (rows_ < 2) {
      fprintf(stderr, "k4 needs a footprint of at least two rows\n");
      exit(2);
    }
  }

  const char* name() const override { return "k4"; }
  std::string knob_header() const override { return "generator,degree,rows,nnz"; }
  std::string knob_values() const override {
    return generator_ + "," + std::to_string(degree_) + "," + std::to_string(rows_) + "," +
           std::to_string(nnz_);
  }
  u64 touched_lines() const override { return (rows_ + 1 + 2 * nnz_ + rows_) * 8 / GPU_LINE_BYTES; }
  size_t output_words() const override { return (size_t)rows_; }
  bool supports_parts() const override { return true; }
  // part k needs the pointers, indices and values of rows [r0, r1), part 0 also all of x
  void part_lines(int k, int parts, std::vector<std::pair<u64, u64>>* ranges) const override {
    const u64 r0 = rows_ * k / parts, r1 = rows_ * (k + 1) / parts;
    const u64 j0 = host_row_ptr_[r0], j1 = host_row_ptr_[r1];
    const u64 col0 = rows_ + 1, val0 = col0 + nnz_, x0 = val0 + nnz_;
    if (k == 0) { ranges->push_back(lines_of(x0, x0 + rows_)); }
    ranges->push_back(lines_of(r0, r1 + 1));
    ranges->push_back(lines_of(col0 + j0, col0 + j1));
    ranges->push_back(lines_of(val0 + j0, val0 + j1));
  }
  void launch_part(const u64* input, u64* output, u64 pass, int k, int parts,
                   cudaStream_t s) const override {
    k4_spmv_kernel<<<shape_.blocks, shape_.threads, 0, s>>>(
        input, rows_, nnz_, rows_ * k / parts, rows_ * (k + 1) / parts, tag_of(pass), output);
  }

  // The graph is drawn from a fixed seed per generator and footprint
  void populate(u64* input) override {
    u64* row_ptr = input;
    u64* col = input + rows_ + 1;
    u64* val = col + nnz_;
    u64* x = val + nnz_;
    uint64_t state =
        fnv1a64("k4:" + generator_ + ":" + std::to_string(rows_) + ":" + std::to_string(degree_));
    if (generator_ == "uniform") {
      for (u64 r = 0; r <= rows_; r++) { row_ptr[r] = r * degree_; }
      parallel_ranges(rows_, [&](unsigned, u64 begin, u64 end) {
        for (u64 r = begin; r < end; r++) {
          uint64_t s = splitmix64_at(state, r);
          for (u64 j = r * degree_; j < (r + 1) * degree_; j++) { col[j] = splitmix64(s) % rows_; }
        }
      });
    } else {
      u64 n_log2 = 0;
      while ((1ull << n_log2) < rows_) { n_log2++; }
      std::vector<u64> edge_row(nnz_), edge_col(nnz_);
      parallel_ranges(nnz_, [&](unsigned, u64 begin, u64 end) {
        for (u64 e = begin; e < end; e++) {
          uint64_t s = splitmix64_at(state, e);
          u64 r, c;
          do { rmat_edge(s, n_log2, &r, &c); } while (r >= rows_ || c >= rows_);
          edge_row[e] = r;
          edge_col[e] = c;
        }
      });
      std::vector<u64> degree(rows_ + 1, 0);
      for (u64 e = 0; e < nnz_; e++) { degree[edge_row[e] + 1]++; }
      row_ptr[0] = 0;
      for (u64 r = 0; r < rows_; r++) { row_ptr[r + 1] = row_ptr[r] + degree[r + 1]; }
      std::vector<u64> fill(rows_, 0);
      for (u64 e = 0; e < nnz_; e++) {
        col[row_ptr[edge_row[e]] + fill[edge_row[e]]++] = edge_col[e];
      }
    }
    parallel_ranges(nnz_, [&](unsigned, u64 begin, u64 end) {
      for (u64 j = begin; j < end; j++) { val[j] = word_value(j); }
    });
    parallel_ranges(rows_, [&](unsigned, u64 begin, u64 end) {
      for (u64 r = begin; r < end; r++) { x[r] = word_value(nnz_ + r); }
    });
    std::vector<u64> sums(fill_workers(), 0);
    parallel_ranges(rows_, [&](unsigned worker, u64 begin, u64 end) {
      for (u64 r = begin; r < end; r++) {
        u64 acc = 0;
        for (u64 j = row_ptr[r]; j < row_ptr[r + 1]; j++) { acc += val[j] * x[col[j]]; }
        sums[worker] += acc;
      }
    });
    base_sum_ = 0;
    for (u64 s : sums) { base_sum_ += s; }
    host_row_ptr_ = row_ptr;
  }

  void attach(const RouteKernel& populated) override {
    const K4Graph& other = dynamic_cast<const K4Graph&>(populated);
    if (other.rows_ != rows_ || other.generator_ != generator_ || other.degree_ != degree_) {
      refuse_attach("graph");
    }
    base_sum_ = other.base_sum_;
    host_row_ptr_ = other.host_row_ptr_;
  }

  void launch(const u64* input, u64* output, u64 pass, cudaStream_t s) const override {
    k4_spmv_kernel<<<shape_.blocks, shape_.threads, 0, s>>>(input, rows_, nnz_, 0, rows_,
                                                            tag_of(pass), output);
  }
  u64 expected_checksum(u64 pass) const override { return base_sum_ + tag_of(pass); }
};

static std::unique_ptr<RouteKernel> make_k4(const Args& args, size_t input_bytes,
                                            LaunchShape shape) {
  const long degree = args.geti("degree", 16);
  if (degree < 1) {
    fprintf(stderr, "--degree must be at least 1\n");
    exit(2);
  }
  return std::unique_ptr<RouteKernel>(new K4Graph(
      input_bytes, args.enum_arg("generator", "uniform", {"uniform", "rmat"}), degree, shape));
}

static void k4_set_level(Args& args, const std::string& factor, const std::string& level) {
  if (factor != "generator") {
    bad_flag_value("vary", factor, "is not a factor of k4 (generator)");
  }
  args.set("generator", level);
}

const KernelEntry K4_GRAPH = {"k4", {"generator", "degree"}, {"generator"}, make_k4, k4_set_level};

}  // namespace suite
