// SM clock through NVML (dlopen, so no link-time dependency) and the timed core's cpufreq
#pragma once
#include <dlfcn.h>

#include <cstdio>

namespace suite {

struct ClockReader {
  static constexpr int NVML_CLOCK_SM = 1;  // nvmlClockType_t value, nvml.h is not included
  void* lib = nullptr;
  void* dev = nullptr;
  int (*getclock)(void*, int, unsigned*) = nullptr;
  int core = 0;

  void init(int timed_core) {
    core = timed_core;
    lib = dlopen("libnvidia-ml.so.1", RTLD_NOW);
    if (lib) {
      auto init_ = (int (*)())dlsym(lib, "nvmlInit_v2");
      auto by_index = (int (*)(unsigned, void**))dlsym(lib, "nvmlDeviceGetHandleByIndex_v2");
      getclock = (int (*)(void*, int, unsigned*))dlsym(lib, "nvmlDeviceGetClockInfo");
      if (!init_ || !by_index || !getclock || init_() != 0 || by_index(0, &dev) != 0) {
        getclock = nullptr;
      }
    }
    if (!getclock) {
      fprintf(stderr, "warning: NVML unavailable, sm_clock_mhz will be -1 in every row\n");
    }
  }

  int sm_mhz() {
    unsigned mhz = 0;
    if (!getclock || getclock(dev, NVML_CLOCK_SM, &mhz) != 0) { return -1; }
    return (int)mhz;
  }

  long cpu_khz() {
    char path[128];
    snprintf(path, sizeof path, "/sys/devices/system/cpu/cpu%d/cpufreq/scaling_cur_freq", core);
    FILE* f = fopen(path, "r");
    if (!f) { return -1; }
    long khz = -1;
    if (fscanf(f, "%ld", &khz) != 1) { khz = -1; }
    fclose(f);
    return khz;
  }
};

}  // namespace suite
