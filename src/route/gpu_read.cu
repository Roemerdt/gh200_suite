#include "common/common.h"
#include "gpu_read.h"

namespace suite {

__global__ void read_all_kernel(const u64* p, size_t words, u64* sink) {
  const size_t n = (size_t)gridDim.x * blockDim.x;
  u64 acc = 0;
  for (size_t i = (size_t)blockIdx.x * blockDim.x + threadIdx.x; i < words; i += n) { acc += p[i]; }
  if (acc == 0x5bd1e995ull) { sink[0] = acc; }  // keeps the loads
}

void gpu_read_all(const void* p, size_t bytes, cudaStream_t s) {
  u64* sink;
  CU(cudaMalloc(&sink, sizeof(u64)));
  read_all_kernel<<<SMS * 8, 256, 0, s>>>((const u64*)p, bytes / sizeof(u64), sink);
  CU(cudaGetLastError());
  CU(cudaStreamSynchronize(s));
  CU(cudaFree(sink));
}

}  // namespace suite
