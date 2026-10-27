// perf counters read around every timed interval
// uncore PMUs count the whole node (the job is exclusive), core events are summed per role
#pragma once
#include <linux/perf_event.h>
#include <sys/ioctl.h>
#include <sys/syscall.h>
#include <unistd.h>

#include <cerrno>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

namespace suite {

struct CounterRole {
  std::string name;
  std::vector<int> cores;
};

// SMMU PMU name per cluster, from harness/site.env via the Makefile
#ifndef SUITE_SMMU_PMU
#error \
    "SUITE_SMMU_PMU is not defined: build with the Makefile, which takes it from harness/site.env"
#endif
struct EventSet {
  const char* name;
  const char* events;
};
static const EventSet EVENT_SETS[] = {
    // C2C reads and writes in requests and bytes, and translation requests at the GPU's SMMU
    {"route",
     "nvidia_nvlink_c2c0_pmu_0/rd_req_loc/,nvidia_nvlink_c2c0_pmu_0/rd_bytes_loc/,"
     "nvidia_nvlink_c2c0_pmu_0/wr_req_loc/,nvidia_nvlink_c2c0_pmu_0/wr_bytes_loc/," SUITE_SMMU_PMU
     "/pcie_ats_trans_rq/"},
    // the route set plus the writer cores' L2 refill and write-back events (r57, r58)
    // and their TLB refills (r05), per core role
    {"writes",
     "nvidia_nvlink_c2c0_pmu_0/rd_req_loc/,nvidia_nvlink_c2c0_pmu_0/rd_bytes_loc/,"
     "nvidia_nvlink_c2c0_pmu_0/wr_req_loc/,nvidia_nvlink_c2c0_pmu_0/wr_bytes_loc/," SUITE_SMMU_PMU
     "/pcie_ats_trans_rq/,r57,r58,r05"},
    // SCF reads and writes of GPU and CPU memory and its cache refills and write-backs,
    // with core event r17 (L2 cache write-back) on the issuing cores
    {"cpu_atomics",
     "nvidia_scf_pmu_0/gmem_rd_access/,nvidia_scf_pmu_0/gmem_wr_access/,nvidia_scf_pmu_0/cmem_rd_access/,"
     "nvidia_scf_pmu_0/cmem_wr_access/,nvidia_scf_pmu_0/scf_cache_refill/,nvidia_scf_pmu_0/scf_cache_wb/,r17"},
};

static inline std::string expand_event_sets(const std::string& spec) {
  std::string out;
  std::stringstream ss(spec);
  std::string tok;
  while (std::getline(ss, tok, ',')) {
    if (tok.empty()) { continue; }
    const char* piece = tok.c_str();
    for (const EventSet& s : EVENT_SETS) {
      if (tok == s.name) { piece = s.events; }
    }
    if (!out.empty()) { out += ","; }
    out += piece;
  }
  return out;
}

class Counters {
  // PERF_EVENT_IOC_RESET clears the count but not the enabled and running times, so each fd
  // keeps the times of its last read and an interval's share is the difference
  struct Fd {
    int fd;
    unsigned long long enabled = 0, running = 0;
  };
  struct Ev {
    std::string column;
    std::vector<Fd> fds;
    unsigned long long value = 0;
    bool multiplexed = false;  // sets ctr_multiplexed, which voids the row in the analysis
  };
  std::vector<Ev> evs;

  static std::string sysfs(const std::string& path) {
    std::ifstream f(path);
    std::string s;
    std::getline(f, s);
    return s;
  }
  static std::string short_pmu(const std::string& pmu) {
    if (pmu.rfind("nvidia_nvlink_", 0) == 0) {
      return pmu.substr(14, pmu.find("_pmu") - 14);  // c2c0, c2c1
    }
    if (pmu.rfind("nvidia_", 0) == 0) {
      return pmu.substr(7, pmu.find("_pmu") - 7);  // scf, pcie, cnvlink
    }
    if (pmu.rfind("smmuv3_pmcg_", 0) == 0) { return "smmu" + pmu.substr(12); }
    return pmu;
  }
  // puts v at the bits a sysfs format names, e.g. config:0-32
  static void place(perf_event_attr& a, const std::string& fmt, unsigned long long v) {
    size_t c = fmt.find(':');
    if (c == std::string::npos) {
      fprintf(stderr, "counters: bad format %s\n", fmt.c_str());
      exit(1);
    }
    std::string field = fmt.substr(0, c);
    int lo = atoi(fmt.c_str() + c + 1);
    unsigned long long shifted = v << lo;
    if (field == "config") {
      a.config |= shifted;
    } else if (field == "config1") {
      a.config1 |= shifted;
    } else if (field == "config2") {
      a.config2 |= shifted;
    } else {
      fprintf(stderr, "counters: unknown format field %s\n", field.c_str());
      exit(1);
    }
  }
  // A failed ioctl would leave a zero count that reads as a measurement
  static void control(int fd, unsigned long request, const char* what) {
    if (ioctl(fd, request, 0) != 0) {
      fprintf(stderr, "counters: %s failed: %s\n", what, strerror(errno));
      exit(1);
    }
  }
  static int open_one(const perf_event_attr& a, int cpu, const std::string& what) {
    int fd = (int)syscall(SYS_perf_event_open, &a, -1, cpu, -1, 0);
    if (fd < 0) {
      fprintf(stderr, "counters: cannot open %s on cpu %d: %s\n", what.c_str(), cpu,
              strerror(errno));
      exit(1);
    }
    return fd;
  }

  static perf_event_attr base_attr() {
    perf_event_attr a;
    memset(&a, 0, sizeof a);
    a.size = sizeof a;
    a.disabled = 1;
    a.read_format = PERF_FORMAT_TOTAL_TIME_ENABLED | PERF_FORMAT_TOTAL_TIME_RUNNING;
    return a;
  }

  static unsigned pmu_type(const std::string& sysfs_dir, const std::string& pmu) {
    std::string type = sysfs(sysfs_dir + "/type");
    if (type.empty()) {
      fprintf(stderr, "counters: no PMU %s\n", pmu.c_str());
      exit(1);
    }
    return (unsigned)atoi(type.c_str());
  }

  // a sysfs event definition such as event=0x6,..., each field placed by the PMU's format files
  static void apply_event_definition(perf_event_attr& a, const std::string& sysfs_dir,
                                     const std::string& pmu, const std::string& event) {
    std::string definition = sysfs(sysfs_dir + "/events/" + event);
    if (definition.empty()) {
      fprintf(stderr, "counters: no event %s in %s\n", event.c_str(), pmu.c_str());
      exit(1);
    }
    std::stringstream fields(definition);
    std::string field;
    while (std::getline(fields, field, ',')) {
      size_t eq = field.find('=');
      std::string key = field.substr(0, eq);
      unsigned long long value =
          (eq == std::string::npos) ? 1 : strtoull(field.substr(eq + 1).c_str(), nullptr, 0);
      std::string fmt = sysfs(sysfs_dir + "/format/" + key);
      if (fmt.empty()) {
        fprintf(stderr, "counters: no format %s for %s\n", key.c_str(), pmu.c_str());
        exit(1);
      }
      place(a, fmt, value);
    }
  }

  // opened on every core of every role, one column per role
  void open_core_event(const std::string& token, const std::vector<CounterRole>& roles) {
    perf_event_attr a = base_attr();
    a.type = PERF_TYPE_RAW;
    a.config = strtoull(token.c_str() + 1, nullptr, 16);
    for (const CounterRole& role : roles) {
      Ev e;
      e.column = "ctr_" + token + "_" + role.name;
      for (int core : role.cores) { e.fds.push_back({open_one(a, core, token)}); }
      evs.push_back(e);
    }
  }

  // <pmu>/<event>/, opened once on the PMU's own CPU
  void open_uncore_event(const std::string& token) {
    size_t slash = token.find('/');
    std::string pmu = token.substr(0, slash), event = token.substr(slash + 1);
    if (!event.empty() && event.back() == '/') { event.pop_back(); }
    std::string sysfs_dir = "/sys/bus/event_source/devices/" + pmu;
    perf_event_attr a = base_attr();
    a.type = pmu_type(sysfs_dir, pmu);
    apply_event_definition(a, sysfs_dir, pmu, event);
    std::string cpumask = sysfs(sysfs_dir + "/cpumask");
    int cpu = cpumask.empty() ? 0 : atoi(cpumask.c_str());
    Ev e;
    e.column = "ctr_" + short_pmu(pmu) + "_" + event;
    e.fds.push_back({open_one(a, cpu, token)});
    evs.push_back(e);
  }

 public:
  bool empty() const { return evs.empty(); }

  // comma-separated spec, set names expanded first
  void open(const std::string& spec, const std::vector<CounterRole>& roles) {
    std::stringstream ss(expand_event_sets(spec));
    std::string token;
    while (std::getline(ss, token, ',')) {
      if (token.empty()) { continue; }
      const bool core_event = token[0] == 'r' && token.find('/') == std::string::npos;
      if (core_event) {
        open_core_event(token, roles);
      } else {
        open_uncore_event(token);
      }
    }
  }
  std::string header() const {
    std::string h;
    for (const Ev& e : evs) { h += e.column + ","; }
    return h + "ctr_multiplexed";
  }
  void start() {
    for (Ev& e : evs) {
      for (const Fd& f : e.fds) {
        control(f.fd, PERF_EVENT_IOC_RESET, "reset");
        control(f.fd, PERF_EVENT_IOC_ENABLE, "enable");
      }
    }
  }
  void stop() {
    for (Ev& e : evs) {
      e.value = 0;
      e.multiplexed = false;
      for (Fd& f : e.fds) {
        control(f.fd, PERF_EVENT_IOC_DISABLE, "disable");
        unsigned long long r[3] = {0, 0, 0};  // value, time enabled, time running
        if (read(f.fd, r, sizeof r) != (ssize_t)sizeof r) {
          fprintf(stderr, "counters: read failed\n");
          exit(1);
        }
        e.value += r[0];
        // multiplexed if it ran for less of this interval than it was enabled
        if (r[2] - f.running < r[1] - f.enabled) { e.multiplexed = true; }
        f.enabled = r[1];
        f.running = r[2];
      }
    }
  }
  std::string values() const {
    std::string v;
    bool mux = false;
    for (const Ev& e : evs) {
      v += std::to_string(e.value) + ",";
      mux = mux || e.multiplexed;
    }
    return v + (mux ? "1" : "0");
  }
};

}  // namespace suite
