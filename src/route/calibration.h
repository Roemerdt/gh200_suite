// repetitions per interval, calibrated to the target or frozen with --passes
#pragma once
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>

#include "config.h"

namespace suite {

class Calibration {
  const Config& cfg_;
  double target_ns_;
  std::vector<double> fastest_ns_;
  std::vector<long> passes_;
  std::vector<long> frozen_;  // 0 when calibrated by this process

  // A=8,B=7,... with a count for every variant
  void parse_frozen(const std::string& spec) {
    if (spec.empty()) { return; }
    const char* reason = "must list <letter>=<count> for every variant of the cell";
    for (const std::string& item : split(spec, ',')) {
      const size_t eq = item.find('=');
      if (eq == std::string::npos || eq == 0) { bad_flag_value("passes", spec, reason); }
      int v = -1;
      for (int i = 0; i < (int)passes_.size(); i++) {
        if (variant_letter(i) == item.substr(0, eq)) { v = i; }
      }
      char* end;
      const long n = strtol(item.c_str() + eq + 1, &end, 10);
      if (v < 0 || *end != '\0' || n < 1 || n > MAX_PASSES_PER_INTERVAL) {
        bad_flag_value("passes", spec, reason);
      }
      frozen_[v] = n;
    }
    for (long n : frozen_) {
      if (n == 0) { bad_flag_value("passes", spec, reason); }
    }
  }

 public:
  Calibration(const Config& cfg, double target_ns, const std::string& frozen_spec)
      : cfg_(cfg),
        target_ns_(target_ns),
        fastest_ns_(cfg.variants.size(), 0),
        passes_(cfg.variants.size(), 1),
        frozen_(cfg.variants.size(), 0) {
    parse_frozen(frozen_spec);
  }

  long passes(int v) const { return passes_[v]; }
  bool frozen() const { return frozen_[0] != 0; }

  // A cell with host phases holds passes until the summed GPU time reaches the target, at least
  // 10 and at most 50 per interval; any other cell as many repetitions as the target needs
  long count_for(double repetition_ns) const {
    const long needed = (long)ceil(target_ns_ / repetition_ns);
    if (cfg_.host.kind == "state") {
      return STATE_PHASE_PASSES;
    }  // fixed, so every pass meets a freshly prepared state
    if (cfg_.host.kind != "none") { return std::clamp(needed, 1L, HOST_PHASE_MAX_PASSES); }
    return std::clamp(needed, 1L, MAX_PASSES_PER_INTERVAL);
  }

  void start(int v, double repetition_ns) {
    fastest_ns_[v] = repetition_ns;
    passes_[v] = frozen_[v] ? frozen_[v] : count_for(repetition_ns);
    fprintf(stderr, "calib variant=%s route=%s level=%s one repetition=%.3f ms -> passes=%ld%s\n",
            variant_letter(v).c_str(), route_name(cfg_.variants[v].route),
            cfg_.variants[v].level.c_str(), repetition_ns / 1e6, passes_[v],
            frozen_[v] ? " (frozen)" : "");
    if (frozen_[v] && repetition_ns * (double)frozen_[v] < 0.8 * target_ns_) {
      fprintf(stderr,
              "note: variant %s: the frozen count gives an interval of %.1f ms, below %.1f ms\n",
              variant_letter(v).c_str(), repetition_ns * (double)frozen_[v] / 1e6,
              target_ns_ / 1e6);
    }
  }

  // a copy variant's first call counts too, it follows another variant and is rarely slow
  void observe(int v, double interval_ns, long passes, const double* first_call_ns) {
    fastest_ns_[v] = std::min(fastest_ns_[v], interval_ns / (double)passes);
    if (cfg_.variants[v].route == COPY) {
      fastest_ns_[v] =
          std::min(fastest_ns_[v], first_call_ns[0] + first_call_ns[1] + first_call_ns[2]);
    }
  }

  // recount from the fastest warm-up repetition
  void refine(int v) {
    if (frozen_[v]) { return; }
    const long refined = count_for(fastest_ns_[v]);
    if (refined == passes_[v]) { return; }
    fprintf(stderr, "calib variant=%s fastest repetition in warm-up=%.3f ms -> passes=%ld\n",
            variant_letter(v).c_str(), fastest_ns_[v] / 1e6, refined);
    passes_[v] = refined;
  }
};

}  // namespace suite
