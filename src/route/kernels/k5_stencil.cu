#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>

#include "k5_stencil.h"

namespace suite {

static const int TILE_X = 32, TILE_Y = 8;
// hints that give both tilings the 132 KiB shared-memory configuration
// with its static tile, the tiled kernel lands one configuration higher for the same hint
static const int K5_CARVEOUT = carveout_hint("SUITE_CARVEOUT_K5", 50);
static const int K5_CARVEOUT_TILES = carveout_hint("SUITE_CARVEOUT_K5_TILES", 40);

__device__ __forceinline__ double five_point(double c, double n, double s, double e, double w) {
  return ((((c + n) + s) + e) + w) * 0.2;
}

// one sweep over rows [row_begin, row_end), the border keeps its value
__global__ void k5_sweep_kernel(const double* src, double* dst, u64 side, u64 row_begin,
                                u64 row_end) {
  const u64 n = (u64)gridDim.x * blockDim.x;
  const u64 first = row_begin * side, last = row_end * side;
  for (u64 i = first + (u64)blockIdx.x * blockDim.x + threadIdx.x; i < last; i += n) {
    const u64 r = i / side, c = i % side;
    if (r == 0 || c == 0 || r == side - 1 || c == side - 1) {
      dst[i] = src[i];
    } else {
      dst[i] = five_point(src[i], src[i - side], src[i + side], src[i + 1], src[i - 1]);
    }
  }
}

// The same sweep with shared-memory tiles of TILE_X by TILE_Y elements plus a halo
__global__ void k5_sweep_tiled_kernel(const double* src, double* dst, u64 side, u64 row_begin,
                                      u64 row_end) {
  __shared__ double tile[TILE_Y + 2][TILE_X + 2];
  const u64 c = (u64)blockIdx.x * TILE_X + threadIdx.x;
  const u64 r = row_begin + (u64)blockIdx.y * TILE_Y + threadIdx.y;
  const int tx = threadIdx.x + 1, ty = threadIdx.y + 1;
  if (r < row_end && c < side) {
    tile[ty][tx] = src[r * side + c];
    if (threadIdx.x == 0 && c > 0) { tile[ty][0] = src[r * side + c - 1]; }
    if (threadIdx.x == TILE_X - 1 && c + 1 < side) { tile[ty][TILE_X + 1] = src[r * side + c + 1]; }
    if (threadIdx.y == 0 && r > 0) { tile[0][tx] = src[(r - 1) * side + c]; }
    if (threadIdx.y == TILE_Y - 1 && r + 1 < side) {
      tile[TILE_Y + 1][tx] = src[(r + 1) * side + c];
    }
  }
  __syncthreads();
  if (r >= row_end || c >= side) { return; }
  if (r == 0 || c == 0 || r == side - 1 || c == side - 1) {
    dst[r * side + c] = tile[ty][tx];
  } else {
    dst[r * side + c] = five_point(tile[ty][tx], tile[ty - 1][tx], tile[ty + 1][tx],
                                   tile[ty][tx + 1], tile[ty][tx - 1]);
  }
}

__global__ void k5_tag_kernel(u64* grid, u64 tag) {
  grid[0] += tag;
}

class K5Stencil : public RouteKernel {
  u64 side_;
  int sweeps_;
  std::string tiling_;
  LaunchShape shape_;
  u64 base_sum_ = 0;

  u64 cells() const { return side_ * side_; }
  // sweep s (from 1) reads grid from and writes grid to, so that sweep S writes grid 0
  void grids_of(int sweep, const double* input, double* output, const double** from,
                double** to) const {
    double* grid0 = output;
    double* grid1 = output + cells();
    const bool to_zero = (sweeps_ - sweep) % 2 == 0;
    *to = to_zero ? grid0 : grid1;
    *from = sweep == 1 ? input : (to_zero ? grid1 : grid0);
  }
  void sweep(int s, const double* input, double* output, u64 row_begin, u64 row_end,
             cudaStream_t stream) const {
    const double* from;
    double* to;
    grids_of(s, input, output, &from, &to);
    // the same shared-memory configuration for both tilings, so their L1 shares are equal
    CU(cudaFuncSetAttribute(k5_sweep_tiled_kernel, cudaFuncAttributePreferredSharedMemoryCarveout,
                            K5_CARVEOUT_TILES));
    CU(cudaFuncSetAttribute(k5_sweep_kernel, cudaFuncAttributePreferredSharedMemoryCarveout,
                            K5_CARVEOUT));
    if (tiling_ == "tiles") {
      const dim3 block(TILE_X, TILE_Y);
      const dim3 grid((unsigned)((side_ + TILE_X - 1) / TILE_X),
                      (unsigned)((row_end - row_begin + TILE_Y - 1) / TILE_Y));
      k5_sweep_tiled_kernel<<<grid, block, 0, stream>>>(from, to, side_, row_begin, row_end);
    } else {
      k5_sweep_kernel<<<shape_.blocks, shape_.threads, 0, stream>>>(from, to, side_, row_begin,
                                                                    row_end);
    }
  }
  static double five_point_host(double c, double n, double s, double e, double w) {
    const double a = c + n;
    const double b = a + s;
    const double d = b + e;
    const double f = d + w;
    return f * 0.2;
  }

 public:
  K5Stencil(size_t input_bytes, int sweeps, const std::string& tiling, LaunchShape shape)
      : sweeps_(sweeps), tiling_(tiling), shape_(shape) {
    side_ = (u64)sqrt((double)(input_bytes / 8));
    while (side_ * side_ * 8 > input_bytes) { side_--; }
    if (side_ < 3) {
      fprintf(stderr, "k5 needs a footprint of at least a 3 x 3 grid\n");
      exit(2);
    }
  }

  const char* name() const override { return "k5"; }
  std::string knob_header() const override { return "sweeps,tiling,side,carveout"; }
  std::string knob_values() const override {
    return std::to_string(sweeps_) + "," + tiling_ + "," + std::to_string(side_) + "," +
           std::to_string(tiling_ == "tiles" ? K5_CARVEOUT_TILES : K5_CARVEOUT);
  }
  u64 touched_lines() const override { return cells() * 8 / GPU_LINE_BYTES; }
  size_t output_words() const override { return 2 * cells(); }
  size_t delivered_words() const override { return cells(); }
  std::vector<LaunchShape> shape_space() const override {
    if (tiling_ == "tiles") { return {{SMS * 8, TILE_X * TILE_Y, 8}}; }  // fixed by the tile
    return {};
  }
  bool supports_parts() const override { return true; }
  // part k of the first sweep covers rows [k * side / parts, (k + 1) * side / parts) and reads one
  // halo row on either side
  void part_lines(int k, int parts, std::vector<std::pair<u64, u64>>* ranges) const override {
    const u64 r0 = side_ * k / parts, r1 = side_ * (k + 1) / parts;
    const u64 from = r0 == 0 ? 0 : r0 - 1, to = std::min(side_, r1 + 1);
    const u64 w0 = from * side_, w1 = to * side_;
    const u64 first = w0 / GPU_LINE_WORDS;
    ranges->push_back({first, (w1 + GPU_LINE_WORDS - 1) / GPU_LINE_WORDS - first});
  }

  // The reference is the sum of the final grid's bit patterns, in the kernels' arithmetic order
  void populate(u64* input) override {
    const u64 n = cells();
    double* grid = (double*)input;
    parallel_ranges(n, [&](unsigned, u64 begin, u64 end) {
      for (u64 i = begin; i < end; i++) {
        grid[i] = (double)(word_value(i) >> 11) * (1.0 / 9007199254740992.0);
      }
    });
    std::vector<double> a(n), b(n);
    const double* from = grid;
    double* to = nullptr;
    for (int s = 1; s <= sweeps_; s++) {
      const bool to_a = (sweeps_ - s) % 2 == 0;  // grid 0 is a, grid 1 is b
      to = to_a ? a.data() : b.data();
      parallel_ranges(n, [&](unsigned, u64 begin, u64 end) {
        for (u64 i = begin; i < end; i++) {
          const u64 r = i / side_, c = i % side_;
          to[i] = (r == 0 || c == 0 || r == side_ - 1 || c == side_ - 1)
                      ? from[i]
                      : five_point_host(from[i], from[i - side_], from[i + side_], from[i + 1],
                                        from[i - 1]);
        }
      });
      from = to;
    }
    std::vector<u64> sums(fill_workers(), 0);
    parallel_ranges(n, [&](unsigned worker, u64 begin, u64 end) {
      u64 s = 0;
      for (u64 i = begin; i < end; i++) {
        u64 bits;
        memcpy(&bits, &a[i], 8);
        s += bits;
      }
      sums[worker] += s;
    });
    base_sum_ = 0;
    for (u64 s : sums) { base_sum_ += s; }
  }
  void attach(const RouteKernel& populated) override {
    const K5Stencil& other = dynamic_cast<const K5Stencil&>(populated);
    if (other.side_ != side_ || other.sweeps_ != sweeps_) { refuse_attach("grid or sweeps"); }
    base_sum_ = other.base_sum_;
  }

  void launch(const u64* input, u64* output, u64 pass, cudaStream_t s) const override {
    for (int sweep_no = 1; sweep_no <= sweeps_; sweep_no++) {
      sweep(sweep_no, (const double*)input, (double*)output, 0, side_, s);
    }
    k5_tag_kernel<<<1, 1, 0, s>>>(output, tag_of(pass));
  }
  // the first sweep in parts, the last part then runs the other sweeps and adds the tag
  void launch_part(const u64* input, u64* output, u64 pass, int k, int parts,
                   cudaStream_t s) const override {
    sweep(1, (const double*)input, (double*)output, side_ * k / parts, side_ * (k + 1) / parts, s);
    if (k == parts - 1) {
      for (int sweep_no = 2; sweep_no <= sweeps_; sweep_no++) {
        sweep(sweep_no, (const double*)input, (double*)output, 0, side_, s);
      }
      k5_tag_kernel<<<1, 1, 0, s>>>(output, tag_of(pass));
    }
  }
  u64 expected_checksum(u64 pass) const override { return base_sum_ + tag_of(pass); }
};

static std::unique_ptr<RouteKernel> make_k5(const Args& args, size_t input_bytes,
                                            LaunchShape shape) {
  const long sweeps = args.geti("sweeps", 8);
  if (sweeps < 1) {
    fprintf(stderr, "--sweeps must be at least 1\n");
    exit(2);
  }
  return std::unique_ptr<RouteKernel>(new K5Stencil(
      input_bytes, (int)sweeps, args.enum_arg("tiling", "none", {"none", "tiles"}), shape));
}

static void k5_set_level(Args& args, const std::string& factor, const std::string& level) {
  if (factor != "sweeps" && factor != "tiling") {
    bad_flag_value("vary", factor, "is not a factor of k5 (sweeps, tiling)");
  }
  args.set(factor, level);
}

const KernelEntry K5_STENCIL = {
    "k5", {"sweeps", "tiling"}, {"sweeps", "tiling"}, make_k5, k5_set_level};

}  // namespace suite
