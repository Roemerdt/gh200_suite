// word i of a host buffer is a fixed hash of i, so a misplaced, missing or repeated line
// changes any checksum over the words
#pragma once
#include <cstddef>

#include <cuda_runtime.h>

namespace suite {

typedef unsigned long long u64;

static inline __host__ __device__ u64 word_value(u64 i) {
  u64 z = (i + 1) * 0x9E3779B97F4A7C15ull;
  z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ull;
  return z ^ (z >> 31);
}

// p[i] = word_value(i) for i < words, on the calling thread
static inline void fill_words(u64* p, u64 words) {
  for (u64 i = 0; i < words; i++) { p[i] = word_value(i); }
}

}  // namespace suite
