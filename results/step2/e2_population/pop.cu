// pop.cu - step 2 node check E-2 (PILOT_FINDINGS section E): replicate the population check behind
// B-10. Pilot probe, not suite code, adapted from the probe of job 236697.
// Question: which page size does a mapping with MADV_HUGEPAGE get when the GPU populates it by
// reading or by writing, compared with CPU and registration population? B-10 saw 0 to 4096 MB of
// 8 GiB backed by 512 MB pages after GPU read population, in two repeats.
// Every trial uses a fresh 8 GiB mapping (munmap, mmap, madvise, mbind), then three GPU passes over
// it. AnonHugePages is read after each pass, with the kernel's THP event counters around the trial.
// usage: pop       (stdout: one line per trial)
#include <map>

#include "common/common.h"

using namespace suite;
static const size_t GiB = 1ull << 30, PG = 65536;

struct Map {
  char* p;
  char* raw;
  size_t len;
};
// node -1: no binding (first touch decides)
static Map mapit(size_t sz, int node, bool thp) {
  const size_t al = GiB;
  char* raw = (char*)mmap(0, sz + al, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS | MAP_NORESERVE, -1, 0);
  if (raw == MAP_FAILED) {
    perror("mmap");
    exit(1);
  }
  char* p = (char*)(((uintptr_t)raw + al - 1) & ~(uintptr_t)(al - 1));
  if (thp && madvise(p, sz, MADV_HUGEPAGE)) {
    perror("madvise");
    exit(1);
  }
  if (node >= 0) {
    unsigned long m = 1ul << node;
    if (syscall(SYS_mbind, p, sz, MPOL_BIND, &m, 64, 0)) {
      perror("mbind");
      exit(1);
    }
  }
  return {p, raw, sz + al};
}
static std::string where(void* p, size_t sz) {
  size_t np = sz / PG, n = 256;
  std::vector<void*> pg(n);
  std::vector<int> st(n, -99);
  for (size_t i = 0; i < n; i++) { pg[i] = (char*)p + ((np - 1) * i / (n - 1)) * PG; }
  long rc = syscall(SYS_move_pages, 0, n, pg.data(), nullptr, st.data(), 0);
  int c0 = 0, c1 = 0, oth = 0;
  for (int s : st) {
    if (s == 0) {
      c0++;
    } else if (s == 1) {
      c1++;
    } else {
      oth++;
    }
  }
  char b[96];
  snprintf(b, sizeof b, "node0=%d node1=%d other=%d%s", c0, c1, oth, rc ? " (move_pages failed)" : "");
  return b;
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
// one 8-byte word per 128 B line, as in the pilot
__global__ void k1read(const long long* p, size_t nlines, unsigned long long* out) {
  unsigned long long s = 0;
  for (size_t i = blockIdx.x * (size_t)blockDim.x + threadIdx.x; i < nlines; i += (size_t)gridDim.x * blockDim.x) {
    s += p[i * 16];
  }
  atomicAdd(out, s);
}
__global__ void k1write(long long* p, size_t nlines) {
  for (size_t i = blockIdx.x * (size_t)blockDim.x + threadIdx.x; i < nlines; i += (size_t)gridDim.x * blockDim.x) {
    p[i * 16] = (long long)i + 1;
  }
}

int main() {
  CU(cudaSetDevice(0));
  CU(cudaFree(0));
  pin_self(TIMED_CORE);
  cudaEvent_t a, b;
  CU(cudaEventCreate(&a));
  CU(cudaEventCreate(&b));
  unsigned long long* out;
  CU(cudaMalloc(&out, 8));
  const size_t sz = 8 * GiB, nl = sz / 128;
  const char* MN[4] = {"cpu_memset", "cuda_register", "gpu_write", "gpu_read"};
  const int trials[4] = {2, 2, 4, 8};
  const char* keys[] = {"thp_fault_alloc", "thp_fault_fallback", "thp_collapse_alloc", "thp_zero_page_alloc",
                        "thp_split_page", "pgfault", "numa_pte_updates", "pgmigrate_success"};
  printf("node,thp,method,trial,populate_s,pass1_ms,pass2_ms,pass3_ms,ahp_mb_after_pass1,ahp_mb_after_pass2,ahp_mb_after_pass3,"
         "ahp_mb_after_1s,rss_mb,where,vmstat_changes\n");
  for (int node : {0, 1, -1}) {
    for (int thp : {1, 0}) {
      for (int m = 0; m < 4; m++) {
        if (node == -1 && m == 1) { continue; }
        // the 64 KB level is the control: two trials per method are enough there
        const int n = thp ? trials[m] : 2;
        for (int t = 0; t < n; t++) {
          auto v0 = vmstat();
          Map mp = mapit(sz, node, thp);
          uint64_t t0 = now_ns();
          if (m == 0) { memset(mp.p, 1, sz); }
          if (m == 1) { CU(cudaHostRegister(mp.p, sz, cudaHostRegisterDefault)); }
          double tpop = (now_ns() - t0) / 1e9;
          float ms[3];
          long ahp[3];
          for (int pass = 0; pass < 3; pass++) {
            CU(cudaMemset(out, 0, 8));
            CU(cudaEventRecord(a));
            if (m == 2 && pass == 0) {
              k1write<<<132 * 4, 512>>>((long long*)mp.p, nl);
            } else {
              k1read<<<132 * 4, 512>>>((const long long*)mp.p, nl, out);
            }
            CU(cudaEventRecord(b));
            CU(cudaEventSynchronize(b));
            CU(cudaGetLastError());
            CU(cudaEventElapsedTime(&ms[pass], a, b));
            ahp[pass] = smaps_anon_huge_kb(mp.p) / 1024;
          }
          usleep(1000000);
          long ahp_late = smaps_anon_huge_kb(mp.p) / 1024;
          // Rss of the mapping
          long rss = -1;
          {
            FILE* f = fopen("/proc/self/smaps", "r");
            char line[512];
            bool in = false;
            while (f && fgets(line, sizeof line, f)) {
              unsigned long lo, hi;
              if (strchr(line, '-') && sscanf(line, "%lx-%lx", &lo, &hi) == 2) {
                in = ((uintptr_t)mp.p >= lo && (uintptr_t)mp.p < hi);
              } else if (in && strncmp(line, "Rss:", 4) == 0) {
                sscanf(line + 4, "%ld", &rss);
                break;
              }
            }
            if (f) { fclose(f); }
          }
          std::string w = where(mp.p, sz);
          if (m == 1) { CU(cudaHostUnregister(mp.p)); }
          munmap(mp.raw, mp.len);
          auto v1 = vmstat();
          std::string ch;
          for (const char* k : keys) {
            long d = v1[k] - v0[k];
            if (d) { ch += std::string(k) + "=" + std::to_string(d) + " "; }
          }
          printf("%d,%d,%s,%d,%.3f,%.2f,%.2f,%.2f,%ld,%ld,%ld,%ld,%ld,%s,%s\n", node, thp, MN[m], t, tpop, ms[0], ms[1],
                 ms[2], ahp[0], ahp[1], ahp[2], ahp_late, rss / 1024, w.c_str(), ch.c_str());
          fflush(stdout);
        }
      }
    }
  }
  return 0;
}
