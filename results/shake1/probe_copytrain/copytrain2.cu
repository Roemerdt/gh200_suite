// copytrain2.cu - second pilot probe, 5 Oct 2026 (shake-down of the route slice, not suite code).
// copytrain showed: a slow pageable copy-in takes two minor faults per 64 KB source page on the
// calling thread; registered memory never does; tier-1 copy-only cells never did.
// Question: does direct access by GPU kernels to system memory in the same process switch the
// pageable copy into that mode, and which kernel and driver counters move with it?
// Phases run in this order in one process; each prints the counters that changed during it.
// usage: copytrain2      (stdout only)
#include <glob.h>
#include <sys/resource.h>

#include <map>

#include "common/common.h"

using namespace suite;
typedef unsigned long long u64;
static const u64 GPU_LINE_WORDS = 16;

__global__ void k1_stream(const u64* in, u64 touched_words, unsigned g, unsigned G, u64 tag,
                          u64* out) {  // as in src/route/route.cu
  extern __shared__ u64 part[];
  const u64 n = (u64)gridDim.x * blockDim.x;
  u64 acc = 0;
  for (u64 t = (u64)blockIdx.x * blockDim.x + threadIdx.x; t < touched_words; t += n) {
    const unsigned q = (unsigned)(t / GPU_LINE_WORDS);
    const u64 line = (u64)(q / g) * G + q % g;
    acc += in[line * GPU_LINE_WORDS + t % GPU_LINE_WORDS];
  }
  part[threadIdx.x] = acc;
  __syncthreads();
  if (threadIdx.x == 0) {
    u64 s = (blockIdx.x == 0) ? tag : 0;
    for (unsigned i = 0; i < blockDim.x; i++) { s += part[i]; }
    out[blockIdx.x] = s;
  }
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
// every line of the UVM debug files of the GPU, keyed by file and line number
static std::map<std::string, std::string> uvm_files() {
  std::map<std::string, std::string> m;
  glob_t g;
  if (glob("/proc/driver/nvidia-uvm/gpus/*/*", 0, nullptr, &g) == 0) {
    for (size_t i = 0; i < g.gl_pathc; i++) {
      FILE* f = fopen(g.gl_pathv[i], "r");
      if (!f) { continue; }
      char line[512];
      int n = 0;
      const char* base = strrchr(g.gl_pathv[i], '/') + 1;
      while (fgets(line, sizeof line, f)) {
        line[strcspn(line, "\n")] = 0;
        m[std::string(base) + ":" + std::to_string(n++)] = line;
      }
      fclose(f);
    }
    globfree(&g);
  }
  return m;
}
static long minflt() {
  struct rusage r;
  getrusage(RUSAGE_THREAD, &r);
  return r.ru_minflt;
}

int main() {
  const size_t bytes = 1ull << 30;
  const int B = 528, T = 256, N = 7, R = 40;
  const size_t out_bytes = (size_t)B * 8, out_map = (size_t)page_sz();
  CU(cudaSetDevice(0));
  CU(cudaFree(0));
  cudaStream_t st;
  CU(cudaStreamCreateWithFlags(&st, cudaStreamNonBlocking));
  pin_self(TIMED_CORE);
  Buffer host[2], hout[2];
  for (int m = 0; m < 2; m++) {
    host[m] = sys_alloc(bytes, CPU_NODE, 0, 1ull << 30);
    u64* p = (u64*)host[m].p;
    for (u64 i = 0; i < bytes / 8; i++) { p[i] = i * 0x9E3779B97F4A7C15ull; }
    hout[m] = sys_alloc(out_map, CPU_NODE, 0, 1ull << 30);
    memset(hout[m].p, 0, out_map);
  }
  void* dev;
  u64* dev_out;
  CU(cudaMalloc(&dev, bytes));
  CU(cudaMalloc(&dev_out, out_bytes));
  printf("source buffer %p, direct buffer %p; UVM debug files: %zu lines\n", host[1].p, host[0].p,
         uvm_files().size());
  u64 tag = 0;
  const unsigned g = 1, G = 2;
  const u64 touched_words = (bytes / 128 / G * g) * 16;
  auto launch = [&](const void* in, u64* out) {
    k1_stream<<<B, T, (size_t)T * 8, st>>>((const u64*)in, touched_words, g, G, ++tag, out);
  };
  // phase flags: kernel on the device copy after each copy-in; direct interval before each train
  struct Phase {
    const char* name;
    bool kernel, direct, reg;
  };
  const Phase phases[] = {
      {"1 copy only, before any direct access", false, false, false},
      {"2 copy + kernel on the device copy, before any direct access", true, false, false},
      {"3 as the instrument: direct interval, then 7 calls", true, true, false},
      {"4 copy + kernel on the device copy, after direct access", true, false, false},
      {"5 copy only, after direct access", false, false, false},
      {"6 registered source, direct interval, then 7 calls", true, true, true},
      {"7 copy only again, pageable, after unregistering", false, false, false},
  };
  for (const Phase& ph : phases) {
    if (ph.reg) {
      CU(cudaHostRegister(host[1].p, bytes, cudaHostRegisterDefault));
      CU(cudaHostRegister(hout[1].p, out_map, cudaHostRegisterDefault));
    }
    auto v0 = vmstat();
    auto u0 = uvm_files();
    long f0 = minflt();
    std::vector<double> in_us;
    for (int r = 0; r < R; r++) {
      if (ph.direct) {
        for (int p = 0; p < 14; p++) { launch(host[0].p, (u64*)hout[0].p); }
        CU(cudaStreamSynchronize(st));
      }
      for (int c = 0; c < N; c++) {
        uint64_t t0 = now_ns();
        CU(cudaMemcpyAsync(dev, host[1].p, bytes, cudaMemcpyHostToDevice, st));
        if (ph.reg) { CU(cudaStreamSynchronize(st)); }
        in_us.push_back((now_ns() - t0) / 1e3);
        if (ph.kernel) {
          launch(dev, dev_out);
          CU(cudaMemcpyAsync(hout[1].p, dev_out, out_bytes, cudaMemcpyDeviceToHost, st));
        }
        CU(cudaStreamSynchronize(st));
      }
      CU(cudaGetLastError());
    }
    long faults = minflt() - f0;
    auto v1 = vmstat();
    auto u1 = uvm_files();
    double fast = *std::min_element(in_us.begin(), in_us.end());
    int slow = 0;
    for (double x : in_us) { slow += x > fast + 1000; }
    Residency res = residency_check(host[1]);
    printf("\n== phase %s\n   copy-in: fastest %.0f us, median %.0f us, slow %d of %d; minor faults on this thread %ld (%.2f per source page per slow copy); source residency %s\n",
           ph.name, fast, summarize(in_us).median, slow, N * R, faults,
           slow ? (double)faults / slow / 16384.0 : 0.0, res.detail.c_str());
    printf("   /proc/vmstat changes of 500 or more:");
    for (auto& kv : v1) {
      long d = kv.second - v0[kv.first];
      if (d >= 500 || d <= -500) { printf(" %s %+ld;", kv.first.c_str(), d); }
    }
    printf("\n   UVM debug lines that changed:\n");
    for (auto& kv : u1) {
      if (u0[kv.first] != kv.second) { printf("     %s | %s -> %s\n", kv.first.c_str(), u0[kv.first].c_str(), kv.second.c_str()); }
    }
    fflush(stdout);
    if (ph.reg) {
      CU(cudaHostUnregister(host[1].p));
      CU(cudaHostUnregister(hout[1].p));
    }
  }
  return 0;
}
