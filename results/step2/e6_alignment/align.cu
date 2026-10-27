// align.cu - step 2 node check E-6 (PILOT_FINDINGS section E): a first look at C-1 and C-2 with the
// start address controlled, to choose the default alignment and the population recipe. Pilot probe,
// not suite code, adapted from the probe of job 236821 (k3s.cu). The full measurement of C-1 belongs
// to the campaign.
// K3 gather: 16M random 8-byte reads from an 8 GiB buffer in CPU memory (64 KB pages, bound to node 0).
// Every trial maps a fresh buffer at a chosen offset inside a 16 GiB-aligned window of a reserved
// address range, populates it with the recipe, runs 8 gather passes (the first 2 are dropped) and
// unmaps it. Successive trials alternate between two windows.
// Part A: start offset. 1 GiB-aligned starts and starts 512 MiB past a 1 GiB boundary, inside one
//         window and crossing into the next. One populating thread.
// Part B: population recipe at 1 GiB-aligned starts: 1, 16 or 64 threads, 8 buffers each.
// usage: align      (stdout: one line per trial)
#include <thread>

#include "common/common.h"

using namespace suite;
typedef unsigned long long u64;
static const size_t GiB = 1ull << 30, MiB = 1ull << 20;

__global__ void k_initidx(u64* idx, size_t n, size_t words) {
  size_t i = blockIdx.x * (size_t)blockDim.x + threadIdx.x, st = (size_t)gridDim.x * blockDim.x;
  for (; i < n; i += st) {
    u64 z = 0x9E3779B97F4A7C15ull * (i + 1);
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ull;
    z = (z ^ (z >> 27)) * 0x94D049BB133111EBull;
    z ^= z >> 31;
    idx[i] = z % words;
  }
}
__global__ void k_gather(const u64* __restrict__ data, const u64* __restrict__ idx, size_t n, u64* out) {
  size_t i = blockIdx.x * (size_t)blockDim.x + threadIdx.x, st = (size_t)gridDim.x * blockDim.x;
  u64 a = 0;
  for (; i < n; i += st) { a += data[idx[i]]; }
  if (a == 0x123456789ull) { out[0] = a; }
}
static void populate(char* p, size_t sz, int threads) {
  std::vector<std::thread> th;
  const size_t chunk = sz / threads;
  for (int t = 0; t < threads; t++) {
    th.emplace_back([=]() {
      pin_self(t);
      memset(p + t * chunk, 1, chunk);
    });
  }
  for (auto& x : th) { x.join(); }
}

int main() {
  const size_t F = 8 * GiB, words = F / 8, NG = 16ull << 20, WIN = 16 * GiB;
  CU(cudaSetDevice(0));
  CU(cudaFree(0));
  cudaEvent_t e0, e1;
  CU(cudaEventCreate(&e0));
  CU(cudaEventCreate(&e1));
  u64 *d_out, *idx;
  CU(cudaMalloc(&d_out, 64));
  CU(cudaMalloc(&idx, NG * 8));
  k_initidx<<<132 * 8, 256>>>(idx, NG, words);
  CU(cudaDeviceSynchronize());
  pin_self(TIMED_CORE);
  Counters ctr;
  ctr.open("smmuv3_pmcg_16002/pcie_ats_trans_rq/", {});
  // an address range of five windows; buffers are mapped inside it at chosen addresses
  const size_t RES = 5 * WIN;
  char* res = (char*)mmap(nullptr, RES, PROT_NONE, MAP_PRIVATE | MAP_ANONYMOUS | MAP_NORESERVE, -1, 0);
  if (res == MAP_FAILED) {
    perror("reserve");
    return 1;
  }
  char* w0 = (char*)(((uintptr_t)res + WIN - 1) & ~(uintptr_t)(WIN - 1));
  printf("reserved %p, first window at %p\n", (void*)res, (void*)w0);
  printf("part,trial,recipe_threads,window,offset_mib,addr,off_1g_mib,crosses_window,populate_s,gather_ms_median,gather_ms_min,gather_ms_max,"
         "smmu_rq_per_gather,residency\n");
  int trial = 0;
  auto run = [&](const char* part, size_t off_mib, int threads) {
    const int win = trial % 2;  // alternate between two windows, so a trial never reuses the last one's range
    char* addr = w0 + (size_t)win * 2 * WIN + off_mib * MiB;
    char* p = (char*)mmap(addr, F, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS | MAP_NORESERVE | MAP_FIXED, -1, 0);
    if (p != addr) {
      perror("mmap fixed");
      exit(1);
    }
    unsigned long mask = 1ul << CPU_NODE;
    if (syscall(SYS_mbind, p, F, MPOL_BIND, &mask, sizeof(mask) * 8, 0) != 0) {
      perror("mbind");
      exit(1);
    }
    uint64_t t0 = now_ns();
    populate(p, F, threads);
    const double tpop = (now_ns() - t0) / 1e9;
    pin_self(TIMED_CORE);
    std::vector<double> T, S;
    for (int pass = 0; pass < 8; pass++) {
      ctr.start();
      double ns = gpu_timed_ns(e0, e1, 0, [&]() { k_gather<<<132 * 16, 256>>>((const u64*)p, idx, NG, d_out); });
      ctr.stop();
      if (pass < 2) { continue; }
      T.push_back(ns / 1e6);
      S.push_back(atof(ctr.values().c_str()) / (double)NG);
    }
    Buffer b;
    b.p = p;
    b.size = F;
    b.kind = Alloc::System;
    b.node = CPU_NODE;
    Residency r = residency_check(b);
    const size_t in_win = off_mib * MiB;
    printf("%s,%d,%d,%d,%zu,%p,%zu,%d,%.2f,%.2f,%.2f,%.2f,%.4f,%s\n", part, trial, threads, win, off_mib, (void*)p,
           (size_t)((uintptr_t)p % GiB) / MiB, (int)(in_win % WIN + F > WIN), tpop, summarize(T).median,
           *std::min_element(T.begin(), T.end()), *std::max_element(T.begin(), T.end()), summarize(S).median,
           r.detail.c_str());
    fflush(stdout);
    // give the pages back and restore the reservation
    if (mmap(addr, F, PROT_NONE, MAP_PRIVATE | MAP_ANONYMOUS | MAP_NORESERVE | MAP_FIXED, -1, 0) != addr) {
      perror("re-reserve");
      exit(1);
    }
    trial++;
  };
  // part A: start offsets within the window, two trials each
  const size_t offs_mib[] = {0,    1024, 4096,  7168,  8192,          // 1 GiB-aligned, inside one window
                             9216, 12288, 15360,                      // 1 GiB-aligned, crossing into the next
                             512,  3584, 7680,                        // 512 MiB past a boundary, inside
                             8704, 11776, 15872};                     // 512 MiB past a boundary, crossing
  for (int rep = 0; rep < 2; rep++) {
    for (size_t off : offs_mib) { run("A", off, 1); }
  }
  // part B: recipe, at 1 GiB-aligned starts
  for (int rep = 0; rep < 8; rep++) {
    for (int threads : {1, 16, 64}) { run("B", (size_t)(rep % 4) * 2048, threads); }
  }
  return 0;
}
