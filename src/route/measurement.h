#pragma once
#include <cstdio>
#include <string>
#include <vector>

#include "calibration.h"
#include "cell.h"
#include "common/common.h"
#include "rows.h"

namespace suite {

// two unrecorded single-repetition intervals per variant, the second sets the first count
inline bool calibrate(RouteCell& cell, Calibration& calib) {
  for (int v = 0; v < cell.variants(); v++) {
    if (!cell.verify_launch(v)) {
      fprintf(stderr, "variant %d: the launch check failed: cell refused\n", v);
      return false;
    }
    cell.interval_ns(v, 1);
    const double repetition_ns = cell.interval_ns(v, 1);
    if (cell.delivered_checksum(v) != cell.expected_checksum(v)) {
      fprintf(stderr, "variant %d: checksum 0x%016llx, expected 0x%016llx: cell refused\n", v,
              cell.delivered_checksum(v), cell.expected_checksum(v));
      return false;
    }
    if (cell.spec(v).route == COPY && !cell.sentinel_check(v)) {
      fprintf(
          stderr,
          "variant %d: the copy %s does not deliver the checksum from a sentinel: cell refused\n",
          v, cell.spec(v).copy.label().c_str());
      return false;
    }
    calib.start(v, repetition_ns);
    cell.state_check(v);
    if (cell.state_check_ns(v) >= 0) {
      const VariantSpec& s = cell.spec(v);
      const double threshold = s.node == GPU_NODE ? STATE_CHECK_GPU_NODE_NS : STATE_CHECK_CPU_NS;
      if (s.host.kind ==
          "writes") {  // several cores wrote the lines, so the latency is only recorded
        fprintf(stderr, "state check variant=%d %s: %.1f ns per sampled load (recorded)\n", v,
                s.host.label().c_str(), cell.state_check_ns(v));
      } else {
        const bool expect_cached = s.host.state != "evicted";
        fprintf(stderr,
                "state check variant=%d %s: %.1f ns per sampled load, threshold %.0f ns: %s\n", v,
                s.host.label().c_str(), cell.state_check_ns(v), threshold,
                (cell.state_check_ns(v) < threshold) == expect_cached ? "as prepared"
                                                                      : "NOT as prepared");
      }
    }
  }
  return true;
}

// one timed interval of a variant
class Measurement {
  const Config& cfg_;
  const RunCtl& rc_;
  RouteCell& cell_;
  Calibration& calib_;
  Counters& counters_;
  std::vector<int> intervals_done_;  // the first rc.warmup of each variant are the warm-up block

 public:
  Measurement(const Config& cfg, const RunCtl& rc, RouteCell& cell, Calibration& calib,
              Counters& counters)
      : cfg_(cfg),
        rc_(rc),
        cell_(cell),
        calib_(calib),
        counters_(counters),
        intervals_done_(cfg.variants.size(), 0) {}

  Interval operator()(int v, int pos) {
    if (intervals_done_[v] == rc_.warmup) { calib_.refine(v); }
    const long passes = calib_.passes(v);
    const Residency before = cell_.residency(v);
    counters_.start();
    const uint64_t wall_begin = now_ns();  // the wall clock brackets the event interval
    const double t = cell_.interval_ns(v, passes);
    const uint64_t wall_end = now_ns();
    counters_.stop();
    const Residency after = cell_.residency(v);

    Interval iv;
    iv.set_timed(t, passes, before, after);
    const u64 checksum = cell_.delivered_checksum(v);
    if (checksum != cell_.expected_checksum(v)) { iv.status = "VOID_CHECKSUM"; }
    if (intervals_done_[v] < rc_.warmup && good_status(iv.status)) {
      calib_.observe(v, t, passes, cell_.first_call_ns());
    }
    intervals_done_[v]++;
    iv.extra = row_values(cfg_, cell_, rc_, v, pos, passes, calib_.frozen(), checksum,
                          (double)(wall_end - wall_begin));
    return iv;
  }
};

// the loop's summary plus each variant's AnonHugePages, read again after the series
inline std::string cell_summary(const RouteCell& cell, const std::string& loop_line) {
  std::string line = loop_line;
  char tail[64];
  for (int v = 0; v < cell.variants(); v++) {
    snprintf(tail, sizeof tail, " ahp_kb_end_%s=%ld", variant_letter(v).c_str(),
             smaps_anon_huge_kb(cell.host(v).input.p));
    line += tail;
  }
  return line;
}

}  // namespace suite
