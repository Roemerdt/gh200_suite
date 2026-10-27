// CLOCK_MONOTONIC_RAW on the CPU, CUDA events around GPU launches
#pragma once
#include <pthread.h>
#include <sched.h>

#include <cstdint>
#include <cstdio>
#include <ctime>

#include <cuda_runtime.h>

#include "cuda_check.h"

namespace suite {

// seconds since the epoch, for row timestamps
static inline double now_epoch_s() {
  struct timespec ts;
  clock_gettime(CLOCK_REALTIME, &ts);
  return ts.tv_sec + ts.tv_nsec * 1e-9;
}

// monotonic nanoseconds, for host-side durations
static inline uint64_t now_ns() {
  struct timespec ts;
  clock_gettime(CLOCK_MONOTONIC_RAW, &ts);
  return (uint64_t)ts.tv_sec * 1000000000ull + (uint64_t)ts.tv_nsec;
}

static inline void pin_self(int core) {
  cpu_set_t cs;
  CPU_ZERO(&cs);
  CPU_SET(core, &cs);
  if (pthread_setaffinity_np(pthread_self(), sizeof(cs), &cs) != 0) {
    fprintf(stderr, "warning: cannot pin this thread to core %d\n", core);
  }
}

// both events must have completed
static inline double event_elapsed_ns(cudaEvent_t a, cudaEvent_t b) {
  float ms;
  CU(cudaEventElapsedTime(&ms, a, b));
  return (double)ms * 1e6;
}

// a failed launch shows only in cudaGetLastError, checked after e1, outside the timed span
template <class F>
static inline double gpu_timed_ns(cudaEvent_t e0, cudaEvent_t e1, cudaStream_t s, F fn) {
  CU(cudaEventRecord(e0, s));
  fn();
  CU(cudaEventRecord(e1, s));
  CU(cudaGetLastError());
  CU(cudaEventSynchronize(e1));
  return event_elapsed_ns(e0, e1);
}

}  // namespace suite
