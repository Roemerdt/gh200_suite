// capacity.cpp: how much node-1 (GPU) memory a process can bind and touch, with 64 KB and with
// 512 MB pages; what the node's free memory, the process's cgroup and CUDA report along the way;
// and how fast the memory comes back after it is freed. Run inside an exclusive job.
// usage: capacity <step GiB> <max GiB> <thp 0|1>
#include <linux/mempolicy.h>
#include <sys/mman.h>
#include <sys/syscall.h>
#include <unistd.h>

#include <chrono>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <thread>
#include <vector>

#include <cuda_runtime.h>

static const size_t HP = 512ull << 20;

static long meminfo_kb(const char* path, const char* key) {
  FILE* f = fopen(path, "r");
  char line[256];
  long v = -1;
  while (f && fgets(line, sizeof line, f)) {
    const char* k = strstr(line, key);
    if (k) { sscanf(k + strlen(key), "%ld", &v); }
  }
  if (f) { fclose(f); }
  return v;
}
static std::string cgroup_dir() {
  FILE* f = fopen("/proc/self/cgroup", "r");
  char line[512] = "";
  if (f) { fgets(line, sizeof line, f); fclose(f); }
  std::string s(line);
  size_t p = s.rfind(':');
  if (p == std::string::npos) { return ""; }
  s = s.substr(p + 1);
  while (!s.empty() && (s.back() == '\n')) { s.pop_back(); }
  return "/sys/fs/cgroup" + s;
}
static std::string read_file(const std::string& path) {
  FILE* f = fopen(path.c_str(), "r");
  if (!f) { return "(absent)"; }
  char buf[256] = "";
  fgets(buf, sizeof buf, f);
  fclose(f);
  std::string s(buf);
  while (!s.empty() && s.back() == '\n') { s.pop_back(); }
  return s;
}
static void report(const char* when, const std::string& cg) {
  size_t free_dev = 0, total = 0;
  cudaMemGetInfo(&free_dev, &total);
  printf("%-28s node1 MemFree %6ld MiB | cuda free %6zu MiB | cgroup current %s max %s | VmRSS %ld MiB\n", when,
         meminfo_kb("/sys/devices/system/node/node1/meminfo", "MemFree:") >> 10, free_dev >> 20,
         read_file(cg + "/memory.current").c_str(), read_file(cg + "/memory.max").c_str(),
         meminfo_kb("/proc/self/status", "VmRSS:") >> 10);
  fflush(stdout);
}

int main(int argc, char** argv) {
  const size_t step = (size_t)atoi(argv[1]) << 30, max = (size_t)atoi(argv[2]) << 30;
  const int thp = atoi(argv[3]);
  const std::string cg = cgroup_dir();
  printf("cgroup %s; node1 total %ld MiB\n", cg.c_str(), meminfo_kb("/sys/devices/system/node/node1/meminfo", "MemTotal:") >> 10);
  cudaFree(0);
  report("start", cg);
  std::vector<std::pair<void*, size_t>> maps;
  for (size_t used = 0; used + step <= max; used += step) {
    const size_t mapsz = step + HP;
    void* raw = mmap(nullptr, mapsz, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS | MAP_NORESERVE, -1, 0);
    char* p = (char*)(((uintptr_t)raw + HP - 1) & ~(uintptr_t)(HP - 1));
    if (thp) { madvise(p, step, MADV_HUGEPAGE); }
    unsigned long mask = 1ul << 1;
    if (syscall(SYS_mbind, p, step, MPOL_BIND, &mask, 64, 0)) { perror("mbind"); }
    auto t0 = std::chrono::steady_clock::now();
    std::vector<std::thread> threads;
    const size_t per = step / 16;
    for (int w = 0; w < 16; w++) { threads.emplace_back([=]() { memset(p + (size_t)w * per, 1, per); }); }
    for (auto& t : threads) { t.join(); }
    const double s = std::chrono::duration<double>(std::chrono::steady_clock::now() - t0).count();
    maps.push_back({raw, mapsz});
    char when[64];
    snprintf(when, sizeof when, "bound+touched %3zu GiB (%.2f s)", (used + step) >> 30, s);
    report(when, cg);
  }
  size_t dev_bytes = 8ull << 30;
  void* d = nullptr;
  if (cudaMalloc(&d, dev_bytes) == cudaSuccess) { report("plus cudaMalloc 8 GiB", cg); cudaFree(d); } else { printf("cudaMalloc 8 GiB failed\n"); }
  for (auto& m : maps) { munmap(m.first, m.second); }
  for (int i = 0; i < 20; i++) {
    char when[64];
    snprintf(when, sizeof when, "freed, +%d ms", i * 100);
    report(when, cg);
    std::this_thread::sleep_for(std::chrono::milliseconds(100));
  }
  return 0;
}
