// overlap.cu - step 2 node check E-1 (PILOT_FINDINGS section E): replicate B-2 on asynchronous copies.
// Pilot probe, not suite code. B-2 (job 236695, single run) used a spin kernel on one block. Here the
// kernel that runs beside the copy is one of:
//   one_sm    spin on 1 block (131 SMs idle), as in B-2
//   all_sms   spin on 4224 blocks of 64 threads (every SM full, no memory traffic)
//   reader    K1-like read of a 4 GiB device buffer on 528 blocks of 256 threads (every SM, HBM traffic)
// Host memory: pageable or registered, both system memory bound to node 0, CPU-populated, 1 GiB-aligned.
// Chunks: 4 MiB, 64 MiB, or the whole 4 GiB. Order: kernel launched first, or copies issued first.
// Each configuration is run 5 times. Events are taken against a reference event on both streams.
// Part 2 repeats B-2's stream test: 4 GiB split over 1, 2 and 4 streams, for both kinds of memory.
// usage: overlap     (stdout: one line per run, then medians)
#include <sys/resource.h>

#include <map>

#include "common/common.h"

using namespace suite;
typedef unsigned long long u64;
static const size_t GiB = 1ull << 30, MiB = 1ull << 20;

__global__ void spin(long long cyc, int* smids) {
  if (threadIdx.x == 0 && smids) {
    unsigned r;
    asm volatile("mov.u32 %0, %%smid;" : "=r"(r));
    smids[blockIdx.x] = (int)r;
  }
  long long t0 = clock64();
  while (clock64() - t0 < cyc) {}
}
// reads `passes` times over n words of a device buffer, grid-stride (the K1 pattern at f = 1)
__global__ void reader(const u64* in, u64 n, int passes, u64* out) {
  const u64 nt = (u64)gridDim.x * blockDim.x;
  u64 acc = 0;
  for (int p = 0; p < passes; p++) {
    for (u64 t = (u64)blockIdx.x * blockDim.x + threadIdx.x; t < n; t += nt) { acc += in[t]; }
  }
  if (acc == ~0ull) { *out = acc; }
}
static float ev_ms(cudaEvent_t a, cudaEvent_t b) {
  float m;
  CU(cudaEventElapsedTime(&m, a, b));
  return m;
}
static long minflt() {
  struct rusage r;
  getrusage(RUSAGE_THREAD, &r);
  return r.ru_minflt;
}
static double med(std::vector<double> v) { return summarize(v).median; }

int main() {
  const size_t total = 4 * GiB;
  CU(cudaSetDevice(0));
  CU(cudaFree(0));
  pin_self(TIMED_CORE);
  char *dev, *rbuf;
  CU(cudaMalloc(&dev, total));
  CU(cudaMalloc(&rbuf, total));
  CU(cudaMemset(rbuf, 1, total));
  int* d_smids;
  u64* d_out;
  CU(cudaMalloc(&d_smids, 8192 * sizeof(int)));
  CU(cudaMalloc(&d_out, 8));
  cudaStream_t sK, sC[4];
  CU(cudaStreamCreateWithFlags(&sK, cudaStreamNonBlocking));
  for (auto& s : sC) { CU(cudaStreamCreateWithFlags(&s, cudaStreamNonBlocking)); }
  cudaEvent_t ref, k0, k1, c0, c1;
  for (cudaEvent_t* e : {&ref, &k0, &k1, &c0, &c1}) { CU(cudaEventCreate(e)); }

  // how many SMs each spin shape occupies
  for (int blocks : {1, 4224}) {
    CU(cudaMemset(d_smids, 0xff, 8192 * sizeof(int)));
    spin<<<blocks, blocks == 1 ? 32 : 64, 0, sK>>>(2000000, d_smids);
    CU(cudaDeviceSynchronize());
    std::vector<int> h(blocks);
    CU(cudaMemcpy(h.data(), d_smids, blocks * sizeof(int), cudaMemcpyDeviceToHost));
    std::sort(h.begin(), h.end());
    printf("spin on %d blocks occupies %zu distinct SMs\n", blocks,
           (size_t)(std::unique(h.begin(), h.end()) - h.begin()));
  }
  // kernel durations per unit, to match the kernel's length to the copy's
  CU(cudaEventRecord(k0, sK));
  spin<<<1, 32, 0, sK>>>(10000000, nullptr);
  CU(cudaEventRecord(k1, sK));
  CU(cudaDeviceSynchronize());
  const double ms_per_mcyc = ev_ms(k0, k1) / 10.0;
  reader<<<528, 256, 0, sK>>>((const u64*)rbuf, total / 8, 1, d_out);
  CU(cudaDeviceSynchronize());
  CU(cudaEventRecord(k0, sK));
  reader<<<528, 256, 0, sK>>>((const u64*)rbuf, total / 8, 2, d_out);
  CU(cudaEventRecord(k1, sK));
  CU(cudaDeviceSynchronize());
  const double ms_per_readpass = ev_ms(k0, k1) / 2.0;
  printf("spin: %.4f ms per 1e6 cycles; reader: %.3f ms per pass over 4 GiB of device memory (%.0f GB/s)\n",
         ms_per_mcyc, ms_per_readpass, total / (ms_per_readpass * 1e6));

  const char* kinds[2] = {"pageable", "registered"};
  const char* kernels[3] = {"one_sm", "all_sms", "reader"};
  printf("\n=== part 1: overlap of chunked H2D copies (stream C) with a kernel (stream K)\n");
  printf("memory,chunk_mib,kernel,order,run,Tc_alone_ms,host_issue_alone_ms,GBps_alone,Tk_alone_ms,k_start,k_end,c_start,c_end,span_ms,overlap_ms,hidden_over_Tc,host_issue_ms,minor_faults\n");
  std::map<std::string, std::vector<double>> hid, rate, issue_ms, span, slow, flt;
  std::vector<std::string> keys;
  for (int kind = 0; kind < 2; kind++) {
    Buffer hb = sys_alloc(total, CPU_NODE, 0, GiB);
    char* h = (char*)hb.p;
    memset(h, 1, total);
    if (kind == 1) { CU(cudaHostRegister(h, total, cudaHostRegisterDefault)); }
    for (size_t chunk : {4 * MiB, 64 * MiB, total}) {
      const size_t nch = total / chunk;
      auto issue = [&]() {
        uint64_t t = now_ns();
        for (size_t i = 0; i < nch; i++) {
          CU(cudaMemcpyAsync(dev + i * chunk, h + i * chunk, chunk, cudaMemcpyHostToDevice, sC[0]));
        }
        return (now_ns() - t) / 1e6;
      };
      issue();
      CU(cudaDeviceSynchronize());
      for (int kn = 0; kn < 3; kn++) {
        for (int order = 0; order < 2; order++) {
          for (int run = 0; run < 5; run++) {
            // the copy alone, then the kernel alone at the copy's length
            CU(cudaEventRecord(c0, sC[0]));
            double iss_alone = issue();
            CU(cudaEventRecord(c1, sC[0]));
            CU(cudaDeviceSynchronize());
            const float Tc = ev_ms(c0, c1);
            const long long cyc = (long long)(Tc / ms_per_mcyc * 1e6);
            const int rpasses = std::max(1, (int)lround(Tc / ms_per_readpass));
            auto kernel = [&]() {
              if (kn == 0) {
                spin<<<1, 32, 0, sK>>>(cyc, nullptr);
              } else if (kn == 1) {
                spin<<<4224, 64, 0, sK>>>(cyc, nullptr);
              } else {
                reader<<<528, 256, 0, sK>>>((const u64*)rbuf, total / 8, rpasses, d_out);
              }
            };
            CU(cudaEventRecord(k0, sK));
            kernel();
            CU(cudaEventRecord(k1, sK));
            CU(cudaDeviceSynchronize());
            const float Tk = ev_ms(k0, k1);
            // together
            CU(cudaEventRecord(ref, sK));
            CU(cudaStreamWaitEvent(sC[0], ref, 0));
            long f0 = minflt();
            double iss;
            if (order == 0) {  // the kernel is launched first, then the copies are issued
              CU(cudaEventRecord(k0, sK));
              kernel();
              CU(cudaEventRecord(k1, sK));
              CU(cudaEventRecord(c0, sC[0]));
              iss = issue();
              CU(cudaEventRecord(c1, sC[0]));
            } else {  // the copies are issued first, then the kernel is launched
              CU(cudaEventRecord(c0, sC[0]));
              iss = issue();
              CU(cudaEventRecord(c1, sC[0]));
              CU(cudaEventRecord(k0, sK));
              kernel();
              CU(cudaEventRecord(k1, sK));
            }
            CU(cudaDeviceSynchronize());
            CU(cudaGetLastError());
            long faults = minflt() - f0;
            const float ks = ev_ms(ref, k0), ke = ev_ms(ref, k1), cs = ev_ms(ref, c0), ce = ev_ms(ref, c1);
            const float ov = std::max(0.f, std::min(ke, ce) - std::max(ks, cs));
            const float sp = std::max(ke, ce) - std::min(ks, cs);
            const char* ord = order == 0 ? "kernel_first" : "copy_first";
            printf("%s,%zu,%s,%s,%d,%.3f,%.3f,%.0f,%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,%.2f,%.3f,%ld\n", kinds[kind],
                   chunk / MiB, kernels[kn], ord, run, Tc, iss_alone, total / (Tc * 1e6), Tk, ks, ke, cs, ce, sp, ov,
                   ov / Tc, iss, faults);
            char key[96];
            snprintf(key, sizeof key, "%-10s chunk %4zu MiB  %-7s %-12s", kinds[kind], chunk / MiB, kernels[kn], ord);
            if (!hid.count(key)) { keys.push_back(key); }
            hid[key].push_back(ov / Tc);
            rate[key].push_back(total / (Tc * 1e6));
            issue_ms[key].push_back(iss);
            span[key].push_back(sp / (Tc + Tk));
            slow[key].push_back((ce - cs) / Tc);
            flt[key].push_back((double)faults);
          }
        }
      }
    }
    if (kind == 1) { CU(cudaHostUnregister(h)); }
    free_buffer(hb);
  }
  printf("\nmedians of 5 runs: hidden = overlap / copy time alone; span = time of both together / sum of both alone;\n"
         "copy stretch = copy time beside the kernel / copy time alone\n");
  for (auto& k : keys) {
    printf("%s | copy alone %4.0f GB/s | hidden %.2f | span %.2f | copy stretch %.2f | host issue %8.3f ms | minor faults %.0f\n",
           k.c_str(), med(rate[k]), med(hid[k]), med(span[k]), med(slow[k]), med(issue_ms[k]), med(flt[k]));
  }

  printf("\n=== part 2: 4 GiB H2D split over 1, 2 and 4 streams\n");
  for (int kind = 0; kind < 2; kind++) {
    Buffer hb = sys_alloc(total, CPU_NODE, 0, GiB);
    char* h = (char*)hb.p;
    memset(h, 1, total);
    if (kind == 1) { CU(cudaHostRegister(h, total, cudaHostRegisterDefault)); }
    for (int ns : {1, 2, 4}) {
      std::vector<double> w, is;
      for (int run = 0; run < 6; run++) {
        const size_t part = total / ns;
        CU(cudaDeviceSynchronize());
        uint64_t t0 = now_ns();
        for (int i = 0; i < ns; i++) {
          CU(cudaMemcpyAsync(dev + i * part, h + i * part, part, cudaMemcpyHostToDevice, sC[i]));
        }
        double iss = (now_ns() - t0) / 1e6;
        CU(cudaDeviceSynchronize());
        double t = (now_ns() - t0) / 1e6;
        if (run > 0) {  // the first run of each setting is a warm-up
          w.push_back(t);
          is.push_back(iss);
        }
      }
      printf("%-10s streams=%d wall median %.3f ms (%.0f GB/s), min %.3f max %.3f; host issue median %.3f ms\n", kinds[kind],
             ns, med(w), total / (med(w) * 1e6), *std::min_element(w.begin(), w.end()),
             *std::max_element(w.begin(), w.end()), med(is));
    }
    if (kind == 1) { CU(cudaHostUnregister(h)); }
    free_buffer(hb);
  }
  return 0;
}
