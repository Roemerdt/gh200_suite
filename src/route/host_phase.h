// host phases between passes, where the CPU writes, prepares a cache state or reads the output
#pragma once
#include <pthread.h>
#include <sched.h>

#include <algorithm>
#include <cstdint>
#include <cstring>
#include <string>
#include <thread>
#include <vector>

#include "common/common.h"
#include "kernel.h"

namespace suite {

static const int WRITER_CORE_FIRST =
    8;  // clear of core 0, which takes interrupts and the timed thread
static const int STATE_CHECK_SAMPLES = 256;  // lines whose load latency the state check times
static const size_t CPU_LINE_BYTES = 64;

struct HostPhaseSpec {
  std::string kind = "none";     // none | writes | state | reads
  double w = 1.0;                // fraction of the lines written
  std::string pattern = "word";  // word stores 8 bytes per 64 B line, line writes whole lines
  int writers = 16;
  std::string state = "dirty";  // dirty | clean | evicted
  bool control = false;         // the same work on the control buffer

  std::string label() const {
    if (kind == "none") { return "none"; }
    std::string s = kind;
    if (kind == "writes") { s += ":w=" + std::to_string(w) + ":" + pattern; }
    if (kind == "state") { s += ":" + state + ":" + pattern; }
    return s + (control ? ":control" : ":shared");
  }
};

// width lines from offset in every group of period lines over [first, first + count), or a list
struct LineSet {
  u64 first = 0, count = 0, period = 1, width = 1, offset = 0;
  std::vector<u64> list;  // when not empty, the lines themselves

  // fn(first line, lines) per run. The window wraps inside its group and is cut at the set's end
  template <class F>
  void for_each_run(F fn) const {
    if (!list.empty()) {
      for (u64 line : list) { fn(line, (u64)1); }
      return;
    }
    if (width >= period) {  // one run over the whole set
      if (count > 0) { fn(first, count); }
      return;
    }
    for (u64 base = first; base < first + count; base += period) {
      const u64 end = std::min(first + count, base + period);
      const u64 window_end = offset + width;
      if (window_end <= period) {
        const u64 s = base + offset, e = std::min(end, base + window_end);
        if (s < e) { fn(s, e - s); }
      } else {
        const u64 s = base + offset;
        if (s < end) { fn(s, end - s); }
        const u64 e = std::min(end, base + (window_end - period));
        if (base < e) { fn(base, e - base); }
      }
    }
  }
  u64 lines() const {
    u64 n = 0;
    for_each_run([&](u64, u64 c) { n += c; });
    return n;
  }
};

static inline void pin_to_core(int core) {
  cpu_set_t cs;
  CPU_ZERO(&cs);
  CPU_SET(core, &cs);
  pthread_setaffinity_np(pthread_self(), sizeof(cs), &cs);  // best effort
}

// rewrites the first word of every 64 B CPU line in place, dirtying it without changing it
static inline void store_word_pattern(volatile u64* line_words) {
  for (u64 w = 0; w < GPU_LINE_WORDS; w += CPU_LINE_BYTES / 8) { line_words[w] = line_words[w]; }
}
static inline void store_line_pattern(u64* line_words) {
  u64 copy[GPU_LINE_WORDS];
  memcpy(copy, (const void*)line_words, GPU_LINE_BYTES);
  memcpy((void*)line_words, copy, GPU_LINE_BYTES);
}

#if defined(__aarch64__)
static inline void clean_cpu_line(const void* p) {
  asm volatile("dc cvac, %0" : : "r"(p) : "memory");
}
static inline void clean_invalidate_cpu_line(const void* p) {
  asm volatile("dc civac, %0" : : "r"(p) : "memory");
}
static inline void data_barrier() {
  asm volatile("dsb sy" : : : "memory");
}
#else
static inline void clean_cpu_line(const void*) {}
static inline void clean_invalidate_cpu_line(const void*) {}
static inline void data_barrier() {}
#endif

// one writer's share of the runs, then the cache maintenance for a clean or evicted state
static inline void prepare_lines(u64* base, const LineSet& set, const HostPhaseSpec& spec,
                                 int worker, int workers) {
  u64 run_index = 0;
  set.for_each_run([&](u64 first, u64 count) {
    if ((int)(run_index++ % workers) != worker) { return; }
    for (u64 line = first; line < first + count; line++) {
      u64* words = base + line * GPU_LINE_WORDS;
      if (spec.pattern == "line") {
        store_line_pattern(words);
      } else {
        store_word_pattern(words);
      }
      if (spec.kind == "state" && spec.state != "dirty") {
        for (u64 b = 0; b < GPU_LINE_BYTES; b += CPU_LINE_BYTES) {
          if (spec.state == "clean") {
            clean_cpu_line((const char*)words + b);
          } else {
            clean_invalidate_cpu_line((const char*)words + b);
          }
        }
      }
    }
  });
  if (spec.kind == "state" && spec.state != "dirty") { data_barrier(); }
  if (spec.kind == "state" && spec.state == "clean") {  // reread, so the lines are cached and clean
    volatile u64 sink = 0;
    run_index = 0;
    set.for_each_run([&](u64 first, u64 count) {
      if ((int)(run_index++ % workers) != worker) { return; }
      for (u64 line = first; line < first + count; line++) {
        for (u64 w = 0; w < GPU_LINE_WORDS; w += CPU_LINE_BYTES / 8) {
          sink += base[line * GPU_LINE_WORDS + w];
        }
      }
    });
  }
}

static inline void run_write_phase(u64* base, const LineSet& set, const HostPhaseSpec& spec) {
  std::vector<std::thread> threads;
  for (int w = 0; w < spec.writers; w++) {
    threads.emplace_back([=, &set, &spec]() {
      pin_to_core(WRITER_CORE_FIRST + w);
      prepare_lines(base, set, spec, w, spec.writers);
    });
  }
  for (std::thread& t : threads) { t.join(); }
}

// the returned sum keeps the reads
static inline u64 run_read_phase(const u64* output, size_t words) {
  u64 sum = 0;
  for (size_t i = 0; i < words; i++) { sum += output[i]; }
  return sum;
}

// The state check: on the preparing core, the median latency of dependent loads from a random
// sample of the set's lines that the preparation did not touch in the last step (a disjoint
// sample of the same region: every sampled line is one the phase prepared, read once)
static inline double sampled_load_latency_ns(const u64* base, const LineSet& set, uint64_t seed) {
  std::vector<u64> lines;
  set.for_each_run([&](u64 first, u64 count) {
    for (u64 line = first; line < first + count; line++) { lines.push_back(line); }
  });
  if (lines.empty()) { return 0; }
  uint64_t state = seed;
  std::vector<u64> sample;
  for (int i = 0; i < STATE_CHECK_SAMPLES; i++) {
    sample.push_back(lines[splitmix64(state) % lines.size()]);
  }
  pin_to_core(WRITER_CORE_FIRST);
  volatile u64 dependency = 0;
  const uint64_t t0 = now_ns();
  for (u64 line : sample) {
    const u64 v =
        base[line * GPU_LINE_WORDS + (dependency & 1)];  // each load waits for the previous one
    dependency = v;
  }
  const uint64_t t1 = now_ns();
  return (double)(t1 - t0) / (double)sample.size();
}

}  // namespace suite
