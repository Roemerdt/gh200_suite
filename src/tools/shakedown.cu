// Measuring-equipment checks and job-level guards:
//   shakedown timers            timer resolution / overhead table (CPU clock, CUDA events, %globaltimer)
//   shakedown warmup <seconds>  sustained load so the SM clock reaches its maximum before measuring
//   shakedown bw <node>         GPU read bandwidth from node's memory, for the placement gate
#include "common/common.h"

using namespace suite;

__global__ void gtimer_res(unsigned long long* out, int n) {
  unsigned long long prev, t, mind = ~0ull;
  asm volatile("mov.u64 %0, %%globaltimer;" : "=l"(prev));
  unsigned long long first = prev;
  for (int i = 1; i < n; i++) {
    asm volatile("mov.u64 %0, %%globaltimer;" : "=l"(t));
    unsigned long long d = t - prev;
    if (d > 0 && d < mind) { mind = d; }
    prev = t;
  }
  out[0] = mind;
  out[1] = first;
  out[2] = prev;
}
__global__ void busy_kernel(float* sink, long iters) {
  float a = threadIdx.x * 0.001f + 1.0001f, b = 1.0000001f;
  for (long i = 0; i < iters; i++) { a = fmaf(a, b, 1e-7f); }
  if (a == 12345.678f) { sink[blockIdx.x * blockDim.x + threadIdx.x] = a; }
}
__global__ void bw_read(const float4* buf, size_t n4, float* out) {
  float acc = 0;
  size_t stride = (size_t)gridDim.x * blockDim.x;
  for (size_t i = (size_t)blockIdx.x * blockDim.x + threadIdx.x; i < n4; i += stride) {
    float4 v = buf[i];
    acc += v.x + v.y + v.z + v.w;
  }
  out[(size_t)blockIdx.x * blockDim.x + threadIdx.x] = acc;
}

static void do_timers() {
  printf("ts_epoch,timer,resolution_ns,overhead_ns,notes\n");
  {
    const int N = 1000000;
    uint64_t prev = now_ns(), start = prev, mind = UINT64_MAX;
    for (int i = 1; i < N; i++) {
      uint64_t t = now_ns();
      uint64_t d = t - prev;
      if (d && d < mind) { mind = d; }
      prev = t;
    }
    printf("%.3f,clock_gettime_monotonic_raw,%llu,%.2f,N=1e6\n", now_epoch_s(),
           (unsigned long long)mind, (double)(prev - start) / (N - 1));
  }
  {
    cudaEvent_t a, b;
    CU(cudaEventCreate(&a));
    CU(cudaEventCreate(&b));
    float minel = 1e30f;
    int M = 2000;
    for (int i = 0; i < M; i++) {
      CU(cudaEventRecord(a));
      CU(cudaEventRecord(b));
      CU(cudaEventSynchronize(b));
      float ms;
      CU(cudaEventElapsedTime(&ms, a, b));
      if (ms > 0 && ms < minel) { minel = ms; }
    }
    uint64_t t0 = now_ns();
    for (int i = 0; i < M; i++) { CU(cudaEventRecord(a)); }
    CU(cudaDeviceSynchronize());
    uint64_t t1 = now_ns();
    printf("%.3f,cuda_events,%.1f,%.2f,res=min_nonzero_elapsed;ovh=one_record;N=%d\n",
           now_epoch_s(), minel * 1e6, (double)(t1 - t0) / M, M);
    CU(cudaEventDestroy(a));
    CU(cudaEventDestroy(b));
  }
  {
    const int N = 1000000;
    unsigned long long *d, h[3];
    CU(cudaMalloc(&d, 3 * sizeof(unsigned long long)));
    gtimer_res<<<1, 1>>>(d, N);
    CU(cudaGetLastError());
    CU(cudaDeviceSynchronize());
    CU(cudaMemcpy(h, d, sizeof h, cudaMemcpyDeviceToHost));
    printf("%.3f,globaltimer,%llu,%.2f,N=1e6;single_thread\n", now_epoch_s(), h[0],
           (double)(h[2] - h[1]) / (N - 1));
    CU(cudaFree(d));
  }
}
static void do_warmup(double total_s) {
  float* sink;
  CU(cudaMalloc(&sink, 128 * 256 * sizeof(float)));
  cudaEvent_t a, b;
  CU(cudaEventCreate(&a));
  CU(cudaEventCreate(&b));
  long iters = 2000000;
  float ms = 0;
  while (true) {
    CU(cudaEventRecord(a));
    busy_kernel<<<128, 256>>>(sink, iters);
    CU(cudaEventRecord(b));
    CU(cudaGetLastError());
    CU(cudaEventSynchronize(b));
    CU(cudaEventElapsedTime(&ms, a, b));
    if (ms > 200.0f) { break; }
    iters *= 2;
  }
  fprintf(stderr, "warmup: calibrated iters=%ld (%.1f ms/launch), running %.0f s\n", iters, ms,
          total_s);
  double t_end = now_epoch_s() + total_s;
  long launches = 0;
  while (now_epoch_s() < t_end) {
    busy_kernel<<<128, 256>>>(sink, iters);
    CU(cudaGetLastError());
    CU(cudaDeviceSynchronize());
    launches++;
  }
  printf("%.3f,warmup_done,launches,%ld,ms_per_launch,%.1f\n", now_epoch_s(), launches, ms);
}
static void do_bw(int node) {
  size_t bytes = 1ull << 30;
  Buffer buf = sys_alloc(bytes, node, 0);
  memset(buf.p, 1, bytes);
  Residency r = residency_check(buf);
  const int blocks = 1024, tpb = 256;
  float* out;
  CU(cudaMalloc(&out, (size_t)blocks * tpb * sizeof(float)));
  cudaEvent_t a, b;
  CU(cudaEventCreate(&a));
  CU(cudaEventCreate(&b));
  size_t n4 = bytes / 16;
  printf("ts_epoch,exp,node,rep,bytes,ms,GBps,residency\n");
  bw_read<<<blocks, tpb>>>((const float4*)buf.p, n4, out);
  CU(cudaGetLastError());
  CU(cudaDeviceSynchronize());
  for (int rep = 0; rep < 5; rep++) {
    CU(cudaEventRecord(a));
    bw_read<<<blocks, tpb>>>((const float4*)buf.p, n4, out);
    CU(cudaEventRecord(b));
    CU(cudaGetLastError());
    CU(cudaEventSynchronize(b));
    float ms;
    CU(cudaEventElapsedTime(&ms, a, b));
    printf("%.3f,bw_read,%d,%d,%zu,%.3f,%.1f,%s\n", now_epoch_s(), node, rep, bytes, ms,
           (double)bytes / (ms * 1e6), r.detail.c_str());
  }
  Residency r2 = residency_check(buf);
  printf("%.3f,bw_post_residency,%d,-1,%zu,0,0,%s\n", now_epoch_s(), node, bytes,
         r2.detail.c_str());
  free_buffer(buf);
}
int main(int argc, char** argv) {
  if (argc < 2) {
    fprintf(stderr, "usage: shakedown timers|warmup <s>|bw <node>\n");
    return 2;
  }
  CU(cudaSetDevice(0));
  CU(cudaFree(0));
  if (!strcmp(argv[1], "timers")) {
    do_timers();
  } else if (!strcmp(argv[1], "warmup")) {
    do_warmup(argc > 2 ? atof(argv[2]) : 30.0);
  } else if (!strcmp(argv[1], "bw")) {
    do_bw(argc > 2 ? atoi(argv[2]) : 0);
  } else {
    fprintf(stderr, "unknown subcommand\n");
    return 2;
  }
  return 0;
}
