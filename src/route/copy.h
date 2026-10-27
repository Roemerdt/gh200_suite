// the copy route's configuration and the copies it issues
#pragma once
#include <cstddef>
#include <string>
#include <vector>

#include <cuda_runtime.h>

#include "kernel.h"

namespace suite {

struct CopyConfig {
  std::string mechanism = "ce";     // ce (copy engine) | kernel
  std::string memory = "pageable";  // pageable | registered
  int streams = 1;                  // 1 | 2 | 4, more than 1 only for registered memory with ce
  std::string chunk = "whole";      // whole | 4m | 16m | 64m | 256m
  std::string pipeline =
      "none";                  // none | pipe, which copies chunk i+1 beside the kernel on chunk i
  std::string form = "whole";  // whole | touched, which copies only the touched lines (K1)
  std::string out = "ce";      // ce | kernel, the copy-out mechanism when the output is large

  size_t chunk_bytes() const;  // 0 for whole
  std::string label()
      const;  // ce-pageable-1-whole-none-whole, -kernel appended for a kernel copy-out

  // exits naming the flag on a bad label
  static CopyConfig parse(const std::string& label, const char* flag);
  // every configuration the kernel allows
  static std::vector<CopyConfig> space(const RouteKernel& kernel);
  // tuned when the output is at least 1 MiB and 1/64 of the touched input (K4, K5, K6)
  static bool copy_out_matters(const RouteKernel& kernel);
};

// lines [first, first + count) of one part of a copy. The touched form copies only width lines
// from offset in every period, wrapping inside the group
struct CopyRegion {
  u64 first = 0, count = 0;
  u64 period = 1, width = 1, offset = 0;
};

// host to device, at the same offsets in both buffers
void copy_region(const CopyConfig& c, const u64* host, u64* device, const CopyRegion& r,
                 cudaStream_t s);

void copy_out_words(const CopyConfig& c, const u64* device, u64* host, u64 words, cudaStream_t s);

}  // namespace suite
