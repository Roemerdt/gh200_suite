// strict --key value parsing and the run-control flags every binary accepts
#pragma once
#include <errno.h>

#include <cstdio>
#include <cstdlib>
#include <initializer_list>
#include <string>
#include <utility>
#include <vector>

namespace suite {

// flags every binary accepts, passed by harness/campaign.py
static const char* const RUN_FLAGS[] = {"out",    "cell",  "campaign", "jobid",     "attempt",
                                        "n0",     "step",  "cap",      "target-ms", "warmup",
                                        "events", "first", "seed",     "floor-ns",  "passes"};

[[noreturn]] static inline void bad_flag_value(const std::string& key, const std::string& value,
                                               const char* reason) {
  fprintf(stderr, "--%s=%s %s\n", key.c_str(), value.c_str(), reason);
  exit(2);
}

struct Args {
  std::vector<std::pair<std::string, std::string>> flags;
  std::vector<std::string>
      stray;  // tokens after the subcommand that are neither a flag nor its value

  Args(int argc, char** argv) {
    for (int i = 1; i < argc; i++) {
      std::string token = argv[i];
      if (token.rfind("--", 0) == 0) {
        std::string value = "1";
        if (i + 1 < argc && std::string(argv[i + 1]).rfind("--", 0) != 0) { value = argv[++i]; }
        flags.push_back({token.substr(2), value});
      } else if (i > 1) {
        stray.push_back(token);
      }
    }
  }

  bool has(const std::string& key) const {
    for (const auto& f : flags) {
      if (f.first == key) { return true; }
    }
    return false;
  }

  std::string get(const std::string& key, const std::string& fallback = "") const {
    for (const auto& f : flags) {
      if (f.first == key) { return f.second; }
    }
    return fallback;
  }

  // how a cell's variants get the knob values of their level
  void set(const std::string& key, const std::string& value) {
    for (auto& f : flags) {
      if (f.first == key) {
        f.second = value;
        return;
      }
    }
    flags.push_back({key, value});
  }

  // 131O72 is an error, not 131
  long geti(const std::string& key, long fallback) const {
    if (!has(key)) { return fallback; }
    const std::string value = get(key);
    char* end;
    errno = 0;
    const long x = strtol(value.c_str(), &end, 10);
    if (end == value.c_str() || *end != '\0' || errno == ERANGE) {
      bad_flag_value(key, value, "is not a number");
    }
    return x;
  }

  double getf(const std::string& key, double fallback) const {
    if (!has(key)) { return fallback; }
    const std::string value = get(key);
    char* end;
    errno = 0;
    const double x = strtod(value.c_str(), &end);
    if (end == value.c_str() || *end != '\0' || errno == ERANGE) {
      bad_flag_value(key, value, "is not a number");
    }
    return x;
  }

  std::string enum_arg(const std::string& key, const std::string& fallback,
                       std::initializer_list<const char*> allowed) const {
    const std::string value = get(key, fallback);
    for (const char* a : allowed) {
      if (value == a) { return value; }
    }
    std::string list;
    for (const char* a : allowed) { list += std::string(" ") + a; }
    bad_flag_value(key, value, ("is not one of {" + list + " }").c_str());
  }

  // stray tokens are errors, or a flag with a single dash would be dropped and its default measured
  void check_known(const std::vector<const char*>& allowed) const {
    if (!stray.empty()) {
      fprintf(stderr, "unexpected argument '%s' (flags are --key value)\n", stray[0].c_str());
      exit(2);
    }
    for (const auto& f : flags) {
      bool known = false;
      for (const char* a : allowed) { known = known || f.first == a; }
      for (const char* a : RUN_FLAGS) { known = known || f.first == a; }
      if (!known) {
        fprintf(stderr, "unknown flag --%s\n", f.first.c_str());
        exit(2);
      }
    }
  }
};

struct RunCtl {
  std::string out;  // raw CSV path, one writer per file
  std::string campaign, jobid, cell_id;
  int attempt = 0;
  int warmup = 10;                    // repeats per variant recorded as WARMUP and not counted
  int n0 = 10, step = 10, cap = 100;  // sequential stopping, first check / step / cap
  double target_ns = 20e6;            // minimum length of a timed interval
  std::string events;  // hardware counters read around every timed interval, empty = none
  std::string instrument;
  bool first_b = false;     // run variant B before A in every repeat
  std::string seed = "na";  // campaign seed the first variant was drawn from, recorded only
  double floor_ns = 0;      // the calibration floor a contrast's half-width may stay within
  std::string passes;       // frozen repetitions per interval as A=8,B=7,..., empty to calibrate

  static RunCtl from(const Args& a, const std::string& instrument) {
    RunCtl r;
    r.instrument = instrument;
    r.out = a.get("out", "");
    r.campaign = a.get("campaign", "dev");
    r.jobid = a.get("jobid", "0");
    r.cell_id = a.get("cell", "");
    r.attempt = (int)a.geti("attempt", r.attempt);
    r.warmup = (int)a.geti("warmup", r.warmup);
    r.n0 = (int)a.geti("n0", r.n0);
    r.step = (int)a.geti("step", r.step);
    r.cap = (int)a.geti("cap", r.cap);
    r.target_ns = a.getf("target-ms", r.target_ns / 1e6) * 1e6;
    r.events = a.get("events", "");
    r.first_b = a.enum_arg("first", "A", {"A", "B"}) == "B";
    r.seed = a.get("seed", r.seed);
    r.floor_ns = a.getf("floor-ns", r.floor_ns);
    r.passes = a.get("passes", "");
    if (r.out.empty()) {
      fprintf(stderr, "--out is required\n");
      exit(2);
    }
    if (r.step < 1) {
      fprintf(stderr, "--step must be at least 1\n");
      exit(2);
    }
    return r;
  }
};

}  // namespace suite
