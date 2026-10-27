// seeded draws, the same fnv1a64 and round_order as in harness/grids.py
#pragma once
#include <cstdint>
#include <string>
#include <utility>
#include <vector>

namespace suite {

static inline uint64_t fnv1a64(const std::string& s) {
  uint64_t h = 1469598103934665603ull;
  for (unsigned char c : s) {
    h ^= c;
    h *= 1099511628211ull;
  }
  return h;
}

static inline uint64_t splitmix64(uint64_t& state) {
  uint64_t z = (state += 0x9E3779B97F4A7C15ull);
  z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ull;
  z = (z ^ (z >> 27)) * 0x94D049BB133111EBull;
  return z ^ (z >> 31);
}

// Fisher-Yates shuffle of 0..k-1 driven by splitmix64, seeded from <cell id>:<seed>:<round>
static inline std::vector<int> round_order(uint64_t seed, const std::string& cell_id,
                                           uint64_t round, int k) {
  uint64_t state = fnv1a64(cell_id + ":" + std::to_string(seed) + ":" + std::to_string(round));
  std::vector<int> order(k);
  for (int i = 0; i < k; i++) { order[i] = i; }
  for (int i = k - 1; i > 0; i--) {
    const int j = (int)(splitmix64(state) % (uint64_t)(i + 1));
    std::swap(order[i], order[j]);
  }
  return order;
}

}  // namespace suite
