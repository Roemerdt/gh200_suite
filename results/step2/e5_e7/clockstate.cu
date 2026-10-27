// clockstate.cu - step 2 node check E-5 (PILOT_FINDINGS section E): the state of the SM clock.
// Pilot probe, not suite code. Question: is the SM clock held at its maximum, or does it fall when
// the GPU idles, and at what clock does the first kernel after an idle gap run?
// A spin kernel runs for a fixed number of SM clock cycles (clock64), so its event-timed duration
// is that number over the effective clock: 2e6 cycles take 1.010 ms at 1980 MHz and 5.8 ms at
// 345 MHz. Each trial: 20 back-to-back kernels, an idle gap, then two timed kernels.
// usage: clockstate            (stdout: one CSV row per trial, then a summary per gap)
#include <map>

#include "common/common.h"

using namespace suite;

__global__ void spin(long long cyc, long long* out) {
  long long t0 = clock64(), t;
  do { t = clock64(); } while (t - t0 < cyc);
  if (threadIdx.x == 0 && blockIdx.x == 0) { *out = t - t0; }
}

int main() {
  CU(cudaSetDevice(0));
  CU(cudaFree(0));
  cudaStream_t st;
  CU(cudaStreamCreateWithFlags(&st, cudaStreamNonBlocking));
  cudaEvent_t e0, e1;
  CU(cudaEventCreate(&e0));
  CU(cudaEventCreate(&e1));
  long long* d_out;
  CU(cudaMalloc(&d_out, 8));
  pin_self(TIMED_CORE);
  ClockReader clk;
  clk.init(TIMED_CORE);
  const long long CYC = 2000000;
  struct Shape {
    const char* name;
    int blocks, threads;
  };
  const Shape shapes[] = {{"one_block", 1, 32}, {"all_sms", 4224, 64}};
  const double gaps_ms[] = {0, 0.1, 1, 10, 100, 1000, 3000};
  printf("shape,gap_ms,trial,idle_clock_read,mhz_idle,first_ms,mhz_after_first,second_ms,mhz_from_first\n");
  std::map<std::string, std::vector<double>> firsts, seconds, idle;
  for (const Shape& s : shapes) {
    auto timed_ms = [&]() {
      return gpu_timed_ns(e0, e1, st, [&]() { spin<<<s.blocks, s.threads, 0, st>>>(CYC, d_out); }) /
             1e6;
    };
    for (double gap : gaps_ms) {
      int trials = gap >= 1000 ? 6 : 12;
      for (int t = 0; t < trials; t++) {
        for (int i = 0; i < 20; i++) { spin<<<s.blocks, s.threads, 0, st>>>(CYC, d_out); }
        CU(cudaStreamSynchronize(st));
        uint64_t g0 = now_ns();
        if (gap >= 10) {
          usleep((useconds_t)(gap * 1000));
        } else {
          while ((double)(now_ns() - g0) < gap * 1e6) {}
        }
        // every second trial reads the idle clock through NVML before the kernel, the others do not,
        // so that the read itself can be ruled out as a cause
        int pre = t % 2, mhz_idle = pre ? clk.sm_mhz() : -1;
        double first = timed_ms();
        int mhz_after = clk.sm_mhz();
        double second = timed_ms();
        printf("%s,%g,%d,%d,%d,%.4f,%d,%.4f,%.0f\n", s.name, gap, t, pre, mhz_idle, first, mhz_after,
               second, CYC / first / 1e3);
        char key[64];
        snprintf(key, sizeof key, "%-9s gap %6g ms", s.name, gap);
        firsts[key].push_back(first);
        seconds[key].push_back(second);
        if (pre) { idle[key].push_back(mhz_idle); }
      }
    }
  }
  printf("\nsummary: duration of 2e6 cycles (1.010 ms at 1980 MHz)\n");
  for (auto& kv : firsts) {
    Summary f = summarize(kv.second), g = summarize(seconds[kv.first]), c = summarize(idle[kv.first]);
    std::vector<double> v = kv.second;
    printf("%s | first kernel after the gap: median %.4f ms (min %.4f, max %.4f) = %.0f MHz | second: median %.4f ms | NVML clock at the end of the gap: median %.0f MHz\n",
           kv.first.c_str(), f.median, *std::min_element(v.begin(), v.end()),
           *std::max_element(v.begin(), v.end()), CYC / f.median / 1e3, g.median, c.median);
  }
  return 0;
}
