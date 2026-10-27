// at HBM placement the first GPU pass over CPU-populated memory is slower than later ones, so
// every variant's buffers are read once after population, untimed
#pragma once
#include <cstddef>

#include <cuda_runtime.h>

namespace suite {

void gpu_read_all(const void* p, size_t bytes, cudaStream_t s);

}  // namespace suite
