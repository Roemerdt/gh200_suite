// latency.cu - step 2 node check E-3 (PILOT_FINDINGS section E): the CPU load-latency probe (B-18) and
// the state each store pattern leaves (C-4). Pilot probe, not suite code, adapted from job 236704.
// Part A calibrates the probe: after a declared preparation (none = evicted long ago, dirty, clean,
// evicted) the preparing core times a dependent chain of loads over a random sample of 64 B lines.
// Part B writes runs of 128 B lines with two store patterns (one 8-byte store per 64 B line; every
// byte of the run with memset) at several run lengths, then probes written and unwritten lines, and
// separately times one GPU read pass over the region.
// Part C repeats the dirty state with eight writer cores and probes from the preparing core.
// usage: latency       (stdout: one line per trial)
#include <thread>

#include "common/common.h"

using namespace suite;
typedef unsigned long long u64;
static const size_t GiB = 1ull << 30, MiB = 1ull << 20, KiB = 1024;

static inline void store_word_per_line(char* r, size_t bytes, u64 v) {  // one STR per 64 B line
  for (size_t o = 0; o < bytes; o += 64) { ((volatile u64*)(r + o))[0] = v + o; }
}
static inline void clean_lines(char* r, size_t bytes) {  // write back, keep in the caches
  for (size_t o = 0; o < bytes; o += 64) { asm volatile("dc cvac, %0" ::"r"(r + o) : "memory"); }
  asm volatile("dsb sy" ::: "memory");
}
static inline void evict_lines(char* r, size_t bytes) {  // write back and invalidate
  for (size_t o = 0; o < bytes; o += 64) { asm volatile("dc civac, %0" ::"r"(r + o) : "memory"); }
  asm volatile("dsb sy" ::: "memory");
}
static inline u64 read_lines(char* r, size_t bytes) {
  u64 a = 0;
  for (size_t o = 0; o < bytes; o += 64) { a += ((volatile u64*)(r + o))[0]; }
  return a;
}
// ns per load of a dependent chain over the 64 B lines listed in idx (each line read once)
static double probe(char* r, const std::vector<size_t>& idx) {
  u64 dep = 0;
  uint64_t t0 = now_ns();
  for (size_t i = 0; i < idx.size(); i++) {
    u64 z;
    asm volatile("and %0, %1, xzr" : "=r"(z) : "r"(dep));
    dep = *(volatile u64*)(r + idx[i] * 64 + z);
  }
  uint64_t t1 = now_ns();
  sink(dep);
  return (double)(t1 - t0) / (double)idx.size();
}
// n distinct 64 B line indices drawn from those for which keep(line) holds
template <class F>
static std::vector<size_t> sample(Rng& rng, size_t lines, size_t n, F keep) {
  std::vector<size_t> idx;
  std::vector<char> used(lines, 0);
  size_t tries = 0;
  while (idx.size() < n && tries++ < 64 * n) {
    size_t l = rng.next() % lines;
    if (!used[l] && keep(l)) {
      used[l] = 1;
      idx.push_back(l);
    }
  }
  return idx;
}
// reads every word of the region once (the K1 pattern at f = 1)
__global__ void k_read(const u64* in, u64 n, u64* out) {
  const u64 nt = (u64)gridDim.x * blockDim.x;
  u64 acc = 0;
  for (u64 t = (u64)blockIdx.x * blockDim.x + threadIdx.x; t < n; t += nt) { acc += in[t]; }
  if (acc == ~0ull) { *out = acc; }
}

int main() {
  CU(cudaSetDevice(0));
  CU(cudaFree(0));
  cudaStream_t st;
  CU(cudaStreamCreateWithFlags(&st, cudaStreamNonBlocking));
  cudaEvent_t e0, e1;
  CU(cudaEventCreate(&e0));
  CU(cudaEventCreate(&e1));
  u64* d_out;
  CU(cudaMalloc(&d_out, 8));
  pin_self(TIMED_CORE);
  Rng rng(7);
  ClockReader clk;
  clk.init(TIMED_CORE);
  printf("cpu0 kHz %ld\n", clk.cpu_khz());

  // ---------------------------------------------------------------- part A: calibration
  printf("\npart,node,region_kib,state,rep,prelude_ms,latency_ns\n");
  const char* SN[] = {"none", "dirty", "clean", "evicted"};
  struct Level {
    int node;
    size_t bytes;
  };
  const Level levels[] = {{0, 512 * KiB}, {0, 8 * MiB}, {0, 64 * MiB}, {1, 8 * MiB}, {1, 64 * MiB}, {1, 96 * MiB}};
  for (const Level& L : levels) {
    // a buffer of 8 regions, so that every trial uses a region the previous trial did not touch
    const size_t big = std::max((size_t)1 * GiB, 8 * L.bytes);
    Buffer b = sys_alloc(big, L.node, 0, GiB);
    memset(b.p, 1, big);
    evict_lines((char*)b.p, big);
    const size_t lines = L.bytes / 64, ns = std::min((size_t)2048, lines / 4);
    size_t cursor = 0;
    for (int rep = 0; rep < 6; rep++) {
      for (int s = 0; s < 4; s++) {
        char* reg = (char*)b.p + cursor;
        cursor = (cursor + L.bytes) % big;
        std::vector<size_t> idx = sample(rng, lines, ns, [](size_t) { return true; });
        // "none": evicted and not touched since. An earlier trial may have used this region, so the
        // eviction is repeated here, outside the timed preparation.
        if (s == 0) { evict_lines(reg, L.bytes); }
        uint64_t t0 = now_ns();
        if (s >= 1) { store_word_per_line(reg, L.bytes, rep); }
        if (s == 2) {
          clean_lines(reg, L.bytes);
          sink(read_lines(reg, L.bytes));
        }
        if (s == 3) { evict_lines(reg, L.bytes); }
        double pre = (now_ns() - t0) / 1e6;
        printf("A,%d,%zu,%s,%d,%.3f,%.1f\n", L.node, L.bytes / KiB, SN[s], rep, pre, probe(reg, idx));
      }
    }
    free_buffer(b);
  }

  // ---------------------------------------------------------------- part B: store patterns and run lengths
  printf("\npart,node,region_kib,pattern,run_lines,w,rep,write_ms,latency_written_ns,latency_unwritten_ns,gpu_pass_us\n");
  for (size_t bytes : {64 * MiB, 8 * MiB}) {
    Buffer b = sys_alloc(bytes, CPU_NODE, 0, GiB);
    memset(b.p, 1, bytes);
    char* reg = (char*)b.p;
    const size_t lines128 = bytes / 128, lines64 = bytes / 64;
    auto gpu_pass_us = [&]() {
      return gpu_timed_ns(e0, e1, st, [&]() { k_read<<<528, 256, 0, st>>>((const u64*)reg, bytes / 8, d_out); }) / 1e3;
    };
    for (int i = 0; i < 3; i++) { gpu_pass_us(); }
    // run_lines 0 stands for w = 1: the whole region as one run
    for (size_t run : {(size_t)0, (size_t)1, (size_t)8, (size_t)64, (size_t)512, (size_t)8192}) {
      for (int pattern = 0; pattern < 3; pattern++) {  // 0 word per 64 B line, 1 memset of the run, 2 no write
        if (pattern == 2 && run != 0) { continue; }
        for (int rep = 0; rep < 5; rep++) {
          double lat_w = -1, lat_u = -1, gpu = -1, wms = 0;
          // even trial halves probe with the CPU, odd ones time the GPU pass: the two do not mix
          for (int what = 0; what < 2; what++) {
            evict_lines(reg, bytes);
            auto written = [&](size_t l128) { return run == 0 || (l128 / run) % 2 == 0; };
            uint64_t t0 = now_ns();
            if (pattern < 2) {
              const size_t step = run == 0 ? lines128 : run;
              for (size_t l = 0; l < lines128; l += step) {
                if (!written(l)) { continue; }
                const size_t n = std::min(step, lines128 - l) * 128;
                if (pattern == 0) {
                  store_word_per_line(reg + l * 128, n, rep);
                } else {
                  memset(reg + l * 128, rep + 2, n);
                }
              }
            }
            wms = (now_ns() - t0) / 1e6;
            if (what == 0) {
              std::vector<size_t> iw = sample(rng, lines64, 2048, [&](size_t l64) { return pattern < 2 && written(l64 / 2); });
              std::vector<size_t> iu = sample(rng, lines64, 2048, [&](size_t l64) { return pattern == 2 || !written(l64 / 2); });
              if (!iw.empty()) { lat_w = probe(reg, iw); }
              if (!iu.empty()) { lat_u = probe(reg, iu); }
            } else {
              gpu = gpu_pass_us();
            }
          }
          printf("B,%d,%zu,%s,%zu,%s,%d,%.3f,%.1f,%.1f,%.1f\n", CPU_NODE, bytes / KiB,
                 pattern == 0 ? "word_per_line" : (pattern == 1 ? "memset" : "no_write"), run, run == 0 ? "1" : "0.5", rep,
                 wms, lat_w, lat_u, gpu);
        }
      }
    }
    free_buffer(b);
  }

  // ---------------------------------------------------------------- part C: eight writer cores
  printf("\npart,node,region_kib,writers,rep,write_ms,latency_ns,gpu_pass_us\n");
  {
    const size_t bytes = 64 * MiB;
    Buffer b = sys_alloc(bytes, CPU_NODE, 0, GiB);
    memset(b.p, 1, bytes);
    char* reg = (char*)b.p;
    for (int i = 0; i < 3; i++) {
      gpu_timed_ns(e0, e1, st, [&]() { k_read<<<528, 256, 0, st>>>((const u64*)reg, bytes / 8, d_out); });
    }
    for (int writers : {1, 8}) {
      for (int rep = 0; rep < 5; rep++) {
        double lat = -1, gpu = -1, wms = 0;
        for (int what = 0; what < 2; what++) {
          evict_lines(reg, bytes);
          uint64_t t0 = now_ns();
          std::vector<std::thread> th;
          for (int t = 0; t < writers; t++) {
            th.emplace_back([&, t]() {
              pin_self(writers == 1 ? TIMED_CORE : 1 + t);  // with eight writers the preparing core does not write
              const size_t c = bytes / writers;
              store_word_per_line(reg + t * c, c, rep);
            });
          }
          for (auto& x : th) { x.join(); }
          wms = (now_ns() - t0) / 1e6;
          if (what == 0) {
            lat = probe(reg, sample(rng, bytes / 64, 2048, [](size_t) { return true; }));
          } else {
            gpu = gpu_timed_ns(e0, e1, st, [&]() { k_read<<<528, 256, 0, st>>>((const u64*)reg, bytes / 8, d_out); }) / 1e3;
          }
        }
        printf("C,%d,%zu,%d,%d,%.3f,%.1f,%.1f\n", CPU_NODE, bytes / KiB, writers, rep, wms, lat, gpu);
      }
    }
    free_buffer(b);
  }
  return 0;
}
