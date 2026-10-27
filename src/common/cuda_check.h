// exits with the CUDA error text when a runtime call fails
#pragma once
#include <cstdio>
#include <cstdlib>

#include <cuda_runtime.h>

#define CU(x)                                                                                \
  do {                                                                                       \
    cudaError_t e_ = (x);                                                                    \
    if (e_ != cudaSuccess) {                                                                 \
      fprintf(stderr, "CUDA error %s:%d: %s\n", __FILE__, __LINE__, cudaGetErrorString(e_)); \
      exit(1);                                                                               \
    }                                                                                        \
  } while (0)
