// copytrain.cu - pilot probe, 5 Oct 2026 (shake-down of the route slice, not suite code).
// Question: in the K1 route cell at f = 1/2 some copy-route calls inside an interval take about
// 1.95 ms longer than the first call. Which part of the call carries that time, and does it depend
// on how the calls are issued?
// One train = 7 back-to-back calls, as in the instrument. Every call is timed on the host clock:
// the pageable copies are host-synchronous, so the host times of the three API calls are the
// component times, without any extra event in the stream.
// usage: copytrain <out.csv>      (stdout: one summary block per configuration)
#include <sys/resource.h>

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

static long vmstat(const char* key) {
  FILE* f = fopen("/proc/vmstat", "r");
  if (!f) { return -1; }
  char k[128];
  long v, r = -1;
  while (fscanf(f, "%127s %ld", k, &v) == 2) {
    if (!strcmp(k, key)) { r = v; }
  }
  fclose(f);
  return r;
}
static void busy_us(double us) {
  uint64_t t = now_ns();
  while ((double)(now_ns() - t) < us * 1e3) {}
}
static void rusage(long* v) {
  struct rusage r;
  getrusage(RUSAGE_THREAD, &r);
  v[0] = r.ru_nvcsw;
  v[1] = r.ru_nivcsw;
  v[2] = r.ru_minflt;
}

enum Variant { INST, NOOUT, GAP300, EVENTS, CORE8, NODIRECT, REG, NVARIANTS };
static const char* VNAME[] = {"inst", "noout", "gap300", "events", "core8", "nodirect", "registered"};

int main(int argc, char** argv) {
  if (argc < 2) { return 2; }
  FILE* csv = fopen(argv[1], "w");
  fprintf(csv, "variant,f_num,f_den,train,call,copyin_us,launch_us,wait_us,total_us\n");
  const size_t bytes = 1ull << 30;
  const int B = 528, T = 256, N = 7, WARM = 3, R = 40;
  const size_t out_bytes = (size_t)B * 8, out_map = (size_t)page_sz();
  CU(cudaSetDevice(0));
  CU(cudaFree(0));
  cudaStream_t st;
  CU(cudaStreamCreateWithFlags(&st, cudaStreamNonBlocking));
  cudaEvent_t ev;
  CU(cudaEventCreate(&ev));
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
  u64 tag = 0;
  const long fr[][2] = {{1, 1}, {9, 10}, {3, 4}, {1, 2}, {1, 4}, {1, 10}};
  for (int v = 0; v < NVARIANTS; v++) {
    pin_self(v == CORE8 ? 8 : TIMED_CORE);
    if (v == REG) {
      CU(cudaHostRegister(host[1].p, bytes, cudaHostRegisterDefault));
      CU(cudaHostRegister(hout[1].p, out_map, cudaHostRegisterDefault));
    }
    for (auto& f : fr) {
      const unsigned g = (unsigned)f[0], G = (unsigned)f[1];
      const u64 lines = bytes / 128, touched_words = (lines / G * g + std::min<u64>(lines % G, g)) * 16;
      auto launch = [&](const void* in, u64* out) {
        k1_stream<<<B, T, (size_t)T * 8, st>>>((const u64*)in, touched_words, g, G, ++tag, out);
      };
      std::vector<double> tot[N], cin[N], wai[N];
      long ru0[3], ru1[3], numa0 = vmstat("numa_pte_updates"), hint0 = vmstat("numa_hint_faults");
      double kern_direct_us = 0;
      rusage(ru0);
      for (int r = -WARM; r < R; r++) {
        if (v != NODIRECT) {  // the direct interval that precedes a copy interval in the cell
          uint64_t d0 = now_ns();
          for (int p = 0; p < 14; p++) { launch(host[0].p, (u64*)hout[0].p); }
          CU(cudaStreamSynchronize(st));
          kern_direct_us = (double)(now_ns() - d0) / 14e3;
        }
        for (int c = 0; c < N; c++) {
          uint64_t t0 = now_ns();
          CU(cudaMemcpyAsync(dev, host[1].p, bytes, cudaMemcpyHostToDevice, st));
          if (v == EVENTS) { CU(cudaEventRecord(ev, st)); }
          uint64_t t1 = now_ns();
          launch(dev, dev_out);
          if (v == EVENTS) { CU(cudaEventRecord(ev, st)); }
          uint64_t t2 = now_ns();
          if (v == NOOUT) {
            CU(cudaStreamSynchronize(st));
          } else {
            CU(cudaMemcpyAsync(hout[1].p, dev_out, out_bytes, cudaMemcpyDeviceToHost, st));
            if (v == REG) { CU(cudaStreamSynchronize(st)); }
          }
          if (v == EVENTS) { CU(cudaEventRecord(ev, st)); }
          uint64_t t3 = now_ns();
          if (v == GAP300) { busy_us(300); }
          if (r >= 0) {
            double a = (t1 - t0) / 1e3, l = (t2 - t1) / 1e3, w = (t3 - t2) / 1e3;
            cin[c].push_back(a);
            wai[c].push_back(w);
            tot[c].push_back((t3 - t0) / 1e3);
            fprintf(csv, "%s,%u,%u,%d,%d,%.1f,%.1f,%.1f,%.1f\n", VNAME[v], g, G, r, c, a, l, w, (t3 - t0) / 1e3);
          }
        }
        CU(cudaGetLastError());
        busy_us(200);
      }
      rusage(ru1);
      // summary: a call is slow when it exceeds the fastest call of the configuration by 1 ms
      double fast = 1e30;
      for (int c = 0; c < N; c++) {
        for (double x : tot[c]) { fast = std::min(fast, x); }
      }
      int slow_by_call[N], nslow = 0;
      std::vector<double> ex_in, ex_wait, ex_tot, fast_in, fast_wait;
      for (int c = 0; c < N; c++) {
        slow_by_call[c] = 0;
        for (size_t i = 0; i < tot[c].size(); i++) {
          if (tot[c][i] > fast + 1000) {
            slow_by_call[c]++;
            nslow++;
            ex_in.push_back(cin[c][i]);
            ex_wait.push_back(wai[c][i]);
            ex_tot.push_back(tot[c][i]);
          } else {
            fast_in.push_back(cin[c][i]);
            fast_wait.push_back(wai[c][i]);
          }
        }
      }
      printf("%-10s f=%ld/%-2ld direct pass %7.1f us | fastest call %7.1f us | slow calls %3d of %d, by position",
             VNAME[v], f[0], f[1], kern_direct_us, fast, nslow, N * R);
      for (int c = 0; c < N; c++) { printf(" %d", slow_by_call[c]); }
      printf(" | fast: copy-in %.0f, wait %.0f us", summarize(fast_in).median, summarize(fast_wait).median);
      if (nslow) {
        printf(" | slow: total %.0f, copy-in %.0f, wait %.0f us", summarize(ex_tot).median,
               summarize(ex_in).median, summarize(ex_wait).median);
      }
      printf(" | ctx switches vol %ld invol %ld, minor faults %ld, numa_pte_updates %+ld, numa_hint_faults %+ld\n",
             ru1[0] - ru0[0], ru1[1] - ru0[1], ru1[2] - ru0[2], vmstat("numa_pte_updates") - numa0,
             vmstat("numa_hint_faults") - hint0);
      fflush(stdout);
    }
    if (v == REG) {
      CU(cudaHostUnregister(host[1].p));
      CU(cudaHostUnregister(hout[1].p));
    }
  }
  fclose(csv);
  return 0;
}
