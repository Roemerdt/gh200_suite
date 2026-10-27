// migpace.cu - step 2 node check E-4 (PILOT_FINDINGS section E): migration pace of unbound memory for
// a K2-like kernel at 8 GiB. Pilot probe, not suite code, adapted from the probe of job 236703, which
// measured a streaming kernel only (B-13: 99 % on node 1 after 15 passes and 4.6 s of GPU time).
// Each series maps 8 GiB without a binding, populates it on one CPU thread (64 KB pages) and runs GPU
// passes until 99 % of 1024 sampled pages are on node 1, plus three more.
//   stream     one 16-byte load per element, grid-stride over the whole buffer (the K1 pattern, B-13's kernel)
//   reuse k=1  one block per SM, each block reads its own slice (8 GiB / 132) once per pass
//   reuse k=16 the same, 16 rereads of the slice per pass
// NOTE: on 5 Oct 2026 the node ran with AutoNUMA on (A-8). The stream series is the control against B-13.
// usage: migpace       (stdout: one line per pass, one RESULT line per series)
#include <map>

#include "common/common.h"

using namespace suite;
static const size_t GiB = 1ull << 30;

__global__ void k_reuse(const ulonglong2* base, size_t slice_elems, int k, unsigned long long* out) {
  extern __shared__ char pad[];
  if (threadIdx.x == 0) { pad[0] = 1; }
  unsigned long long acc = 0;
  const ulonglong2* p = base + (size_t)blockIdx.x * slice_elems;
  for (int j = 0; j < k; j++) {
    for (size_t i = threadIdx.x; i < slice_elems; i += blockDim.x) {
      ulonglong2 v = p[i];
      acc += (v.x ^ v.y) + j;
    }
    __syncthreads();
  }
  if (acc == 0x123456789ull) { out[0] = acc; }
}
__global__ void k_read(const int4* __restrict__ s, size_t n, unsigned long long* out) {
  size_t i = blockIdx.x * (size_t)blockDim.x + threadIdx.x, st = (size_t)gridDim.x * blockDim.x;
  unsigned long long a = 0;
  for (; i < n; i += st) {
    int4 v = s[i];
    a += (unsigned)v.x ^ (unsigned)v.w;
  }
  if (a == 0x123456789ull) { out[0] = a; }
}
static std::map<std::string, long> vmstat() {
  std::map<std::string, long> m;
  FILE* f = fopen("/proc/vmstat", "r");
  char k[128];
  long v;
  while (f && fscanf(f, "%127s %ld", k, &v) == 2) { m[k] = v; }
  if (f) { fclose(f); }
  return m;
}

int main() {
  CU(cudaSetDevice(0));
  CU(cudaFree(0));
  cudaDeviceProp pr;
  CU(cudaGetDeviceProperties(&pr, 0));
  const int NSM = pr.multiProcessorCount;
  cudaEvent_t e0, e1;
  CU(cudaEventCreate(&e0));
  CU(cudaEventCreate(&e1));
  unsigned long long* d_out;
  CU(cudaMalloc(&d_out, 64));
  pin_self(TIMED_CORE);
  const size_t smem = 116 * 1024;  // one block per SM (B-8)
  CU(cudaFuncSetAttribute(k_reuse, cudaFuncAttributeMaxDynamicSharedMemorySize, (int)smem));
  int occ = 0;
  CU(cudaOccupancyMaxActiveBlocksPerMultiprocessor(&occ, k_reuse, 1024, smem));
  printf("SMs=%d, reuse kernel: %d block per SM\n", NSM, occ);
  const size_t sz = 8 * GiB, se = ((sz / NSM) & ~(size_t)255) / 16;
  struct Cfg {
    const char* name;
    int kind, k;
  };
  const Cfg cfgs[] = {{"stream", 0, 1}, {"reuse_k1", 1, 1}, {"reuse_k16", 1, 16}};
  printf("kernel,series,pass,pass_ms,frac_node1,cum_gpu_s,wall_s\n");
  for (int series = 0; series < 2; series++) {
    for (const Cfg& c : cfgs) {
      auto v0 = vmstat();
      const size_t mapsz = sz + GiB;
      void* raw = mmap(nullptr, mapsz, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS | MAP_NORESERVE, -1, 0);
      if (raw == MAP_FAILED) {
        perror("mmap");
        return 1;
      }
      char* p = (char*)(((uintptr_t)raw + GiB - 1) & ~(uintptr_t)(GiB - 1));
      uint64_t t0 = now_ns();
      memset(p, 1, sz);
      const double tpop = (now_ns() - t0) / 1e9;
      const int NS = 1024;
      std::vector<void*> pg(NS);
      std::vector<int> st(NS);
      for (int i = 0; i < NS; i++) { pg[i] = p + (sz / 65536 - 1) * i / (NS - 1) * 65536; }
      auto frac1 = [&]() {
        syscall(SYS_move_pages, 0, (unsigned long)NS, pg.data(), (void*)0, st.data(), 0);
        int n1 = 0;
        for (int s : st) { n1 += (s == 1); }
        return n1 / (double)NS;
      };
      const double f0 = frac1();
      uint64_t tstart = now_ns();
      int p50 = -1, p99 = -1, pass = 0;
      double cum = 0, t50 = -1, t99 = -1, last = 0;
      bool capped = false;
      for (pass = 1; pass <= 200; pass++) {
        double ns = gpu_timed_ns(e0, e1, 0, [&]() {
          if (c.kind == 0) {
            k_read<<<NSM * 8, 256>>>((const int4*)p, sz / 16, d_out);
          } else {
            k_reuse<<<NSM, 1024, smem>>>((const ulonglong2*)p, se, c.k, d_out);
          }
        });
        cum += ns;
        last = ns;
        const double f = frac1();
        if (p50 < 0 && f >= 0.5) {
          p50 = pass;
          t50 = cum / 1e9;
        }
        if (p99 < 0 && f >= 0.99) {
          p99 = pass;
          t99 = cum / 1e9;
        }
        printf("%s,%d,%d,%.2f,%.3f,%.3f,%.2f\n", c.name, series, pass, ns / 1e6, f, cum / 1e9, (now_ns() - tstart) / 1e9);
        if (p99 > 0 && pass >= p99 + 3) { break; }
        if ((now_ns() - tstart) / 1e9 > 75) {
          capped = true;
          break;
        }
      }
      auto v1 = vmstat();
      printf("RESULT kernel=%s series=%d populate_s=%.2f frac_before=%.3f passes_to_50=%d gpu_s_to_50=%.2f passes_to_99=%d gpu_s_to_99=%.2f "
             "last_pass_ms=%.2f time_cap=%d numa_pte_updates=%+ld numa_hint_faults=%+ld numa_pages_migrated=%+ld pgmigrate_success=%+ld\n",
             c.name, series, tpop, f0, p50, t50, p99, t99, last / 1e6, (int)capped, v1["numa_pte_updates"] - v0["numa_pte_updates"],
             v1["numa_hint_faults"] - v0["numa_hint_faults"], v1["numa_pages_migrated"] - v0["numa_pages_migrated"],
             v1["pgmigrate_success"] - v0["pgmigrate_success"]);
      fflush(stdout);
      munmap(raw, mapsz);
    }
  }
  return 0;
}
