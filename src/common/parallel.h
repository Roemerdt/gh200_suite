// Work split over the CPU cores, one thread pinned to each core
#pragma once
#include <pthread.h>
#include <sched.h>

#include <algorithm>
#include <functional>
#include <thread>
#include <vector>

#include "pattern.h"

namespace suite {

static inline unsigned fill_workers() {
  return std::max(1u, std::thread::hardware_concurrency());
}

// fn(worker, begin, end) over [0, n), split into contiguous ranges, one thread per core
static inline void parallel_ranges(u64 n, const std::function<void(unsigned, u64, u64)>& fn) {
  const unsigned workers = fill_workers();
  const u64 per_worker = (n + workers - 1) / workers;
  std::vector<std::thread> threads;
  for (unsigned w = 0; w < workers; w++) {
    const u64 begin = std::min(n, (u64)w * per_worker), end = std::min(n, begin + per_worker);
    if (begin >= end) { break; }
    threads.emplace_back([=, &fn]() {
      cpu_set_t cs;
      CPU_ZERO(&cs);
      CPU_SET((int)w, &cs);
      pthread_setaffinity_np(pthread_self(), sizeof(cs), &cs);  // best effort
      fn(w, begin, end);
    });
  }
  for (std::thread& t : threads) { t.join(); }
}

// p[i] = word_value(i) for i < words, on all cores
static inline void fill_all_cores(u64* p, u64 words) {
  parallel_ranges(words, [p](unsigned, u64 begin, u64 end) {
    for (u64 i = begin; i < end; i++) { p[i] = word_value(i); }
  });
}

}  // namespace suite
