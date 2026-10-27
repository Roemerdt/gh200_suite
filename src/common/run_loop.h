// The paired loop (A B A B ...) and the round loop of cells with more than two variants
#pragma once
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <functional>
#include <string>
#include <utility>
#include <vector>

#include "args.h"
#include "records.h"
#include "stats.h"

namespace suite {

struct LoopResult {
  Summary A, B, D;  // per variant and for the paired difference A-B
  int attempts = 0, warmups = 0, discards = 0;
  bool cap_hit = false, stopped_on_target = false;
  int npos = 0, nneg = 0;  // sign counts of the paired differences
  double sign_p = 1.0;
};

static inline bool good_status(const std::string& s) {
  return s == "OK" || s == "RECORDED";
}

static inline bool targets_met(const LoopResult& r, bool paired) {
  return point_target_met(r.A) && (!paired || (point_target_met(r.B) && pair_target_met(r.D)));
}

struct Samples {
  bool paired;
  std::vector<double> a, b, diff;

  explicit Samples(bool paired_) : paired(paired_) {}

  // true when the repeat is discarded for a bad status
  // a cold repetition is left out but is not a discard
  bool add(const Interval& A, const Interval& B) {
    const bool a_ok = good_status(A.status) && !A.cold;
    const bool b_ok = !paired || (good_status(B.status) && !B.cold);
    if (a_ok) { a.push_back(A.per_op()); }
    if (paired && b_ok) { b.push_back(B.per_op()); }
    if (paired && a_ok && b_ok) { diff.push_back(A.per_op() - B.per_op()); }
    return !(a_ok && b_ok) && !(A.cold || B.cold);
  }

  int count() const { return paired ? (int)diff.size() : (int)a.size(); }

  void summarize_into(LoopResult& r) const {
    r.A = summarize(a);
    if (paired) {
      r.B = summarize(b);
      r.D = summarize(diff);
    }
  }
};

// run(0) times one interval of A, run(1) one of B
// every interval is written as a row as soon as it is measured
static inline LoopResult run_loop(Recorder& rec, const RunCtl& rc, bool paired,
                                  const std::string& allocA, const std::string& allocB,
                                  const std::function<Interval(int)>& run) {
  const std::string pair_id = paired ? rc.cell_id + "#pair" : "";
  const int give_up_at = 3 * rc.cap + 5 + rc.warmup;  // repeats, counting discarded ones
  LoopResult result;
  Samples samples(paired);

  for (int rep = 0;; rep++) {
    const bool warm = rep < rc.warmup;
    auto measure = [&](int variant, const char* member, const std::string& alloc_id) {
      Interval iv = run(variant);
      if (warm && good_status(iv.status)) { iv.status = "WARMUP"; }
      rec.row(pair_id, alloc_id, member, rep, iv);
      return iv;
    };
    Interval a, b;
    if (paired && rc.first_b) { b = measure(1, "B", allocB); }
    a = measure(0, paired ? "A" : "-", allocA);
    if (paired && !rc.first_b) { b = measure(1, "B", allocB); }
    result.attempts = rep + 1;
    if (warm) {
      result.warmups++;
      continue;
    }
    if (samples.add(a, b)) { result.discards++; }

    const int n = samples.count();
    if (n >= rc.n0 && (n - rc.n0) % rc.step == 0) {
      samples.summarize_into(result);
      if (targets_met(result, paired)) {
        result.stopped_on_target = true;
        break;
      }
    }
    if (n >= rc.cap) {
      result.cap_hit = true;
      break;
    }
    if (rep + 1 >= give_up_at) {
      fprintf(stderr, "too many discarded intervals, giving up on cell\n");
      break;
    }
  }

  samples.summarize_into(result);  // the cap and give-up exits leave the loop between checks
  if (paired) {
    for (double d : samples.diff) {
      if (d > 0) { result.npos++; }
      if (d < 0) { result.nneg++; }
    }
    result.sign_p = sign_test_p(result.npos, result.nneg);
  }
  return result;
}

// .done marker line, the analysis recomputes it from the rows
static inline std::string loop_summary_line(const RunCtl& rc, const LoopResult& r, bool paired) {
  char buf[1024];
  snprintf(
      buf, sizeof buf,
      "cell=%s attempts=%d warmups=%d discards=%d nA=%d medA=%.6g loA=%.6g hiA=%.6g targetA=%d "
      "nB=%d medB=%.6g loB=%.6g hiB=%.6g targetB=%d nD=%d medD=%.6g loD=%.6g hiD=%.6g targetD=%d "
      "npos=%d nneg=%d sign_p=%.3g cap_hit=%d stopped_on_target=%d paired=%d",
      rc.cell_id.c_str(), r.attempts, r.warmups, r.discards, r.A.n, r.A.median, r.A.lo, r.A.hi,
      (int)point_target_met(r.A), r.B.n, r.B.median, r.B.lo, r.B.hi, (int)point_target_met(r.B),
      r.D.n, r.D.median, r.D.lo, r.D.hi, (int)pair_target_met(r.D), r.npos, r.nneg, r.sign_p,
      (int)r.cap_hit, (int)r.stopped_on_target, (int)paired);
  return buf;
}

// v<index> beyond 26 variants (tuning cells)
static inline std::string variant_letter(int variant) {
  return variant < 26 ? std::string(1, (char)('A' + variant)) : "v" + std::to_string(variant);
}

// signed sum of a round's per-variant times, e.g. 2 - 0 or (2 - 3) - (0 - 1)
struct Contrast {
  std::string name;
  std::vector<std::pair<int, int>> terms;  // (variant, coefficient)

  double value(const std::vector<double>& per_op) const {
    double v = 0;
    for (const auto& t : terms) { v += t.second * per_op[t.first]; }
    return v;
  }
};

struct RoundsResult {
  std::vector<Summary> variants, contrasts;
  int rounds = 0, warmups = 0, discards = 0;
  bool cap_hit = false, stopped_on_target = false;
};

// half-width within 10 % of the median or within the floor, whichever is larger
static inline bool contrast_target_met(const Summary& d, double floor_ns) {
  return d.n >= 6 && 0.5 * (d.hi - d.lo) <= std::max(0.10 * fabs(d.median), floor_ns);
}

static inline bool round_targets_met(const RoundsResult& r, double floor_ns) {
  for (const Summary& s : r.variants) {
    if (!point_target_met(s)) { return false; }
  }
  for (const Summary& d : r.contrasts) {
    if (!contrast_target_met(d, floor_ns)) { return false; }
  }
  return true;
}

static inline void summarize_rounds(RoundsResult& r, const std::vector<std::vector<double>>& variants,
                                    const std::vector<std::vector<double>>& contrasts) {
  r.variants.clear();
  r.contrasts.clear();
  for (const auto& values : variants) { r.variants.push_back(summarize(values)); }
  for (const auto& values : contrasts) { r.contrasts.push_back(summarize(values)); }
}

// a round counts only when all its intervals are good, so every contrast comes from a whole round
static inline RoundsResult run_rounds(Recorder& rec, const RunCtl& rc, int k,
                                      const std::vector<Contrast>& contrasts,
                                      const std::function<std::vector<int>(int)>& order_of,
                                      const std::function<Interval(int, int)>& run) {
  const std::string round_id = rc.cell_id + "#round";
  const int give_up_at = 3 * rc.cap + 5 + rc.warmup;  // rounds, counting discarded ones
  RoundsResult result;
  std::vector<std::vector<double>> per_variant(k), per_contrast(contrasts.size());

  for (int round = 0;; round++) {
    const bool warm = round < rc.warmup;
    const std::vector<int> order = order_of(round);
    std::vector<double> per_op(k, 0);
    bool all_good = true;
    for (int position = 0; position < k; position++) {
      const int v = order[position];
      Interval iv = run(v, position);
      if (warm && good_status(iv.status)) { iv.status = "WARMUP"; }
      rec.row(round_id, rc.cell_id + "#" + variant_letter(v), variant_letter(v), round, iv);
      all_good = all_good && good_status(iv.status) && !iv.cold;
      per_op[v] = iv.per_op();
    }
    result.rounds = round + 1;
    if (warm) {
      result.warmups++;
      continue;
    }
    if (!all_good) {
      result.discards++;
    } else {
      for (int v = 0; v < k; v++) { per_variant[v].push_back(per_op[v]); }
      for (size_t c = 0; c < contrasts.size(); c++) {
        per_contrast[c].push_back(contrasts[c].value(per_op));
      }
    }

    const int n = (int)per_variant[0].size();
    if (n >= rc.n0 && (n - rc.n0) % rc.step == 0) {
      summarize_rounds(result, per_variant, per_contrast);
      if (round_targets_met(result, rc.floor_ns)) {
        result.stopped_on_target = true;
        break;
      }
    }
    if (n >= rc.cap) {
      result.cap_hit = true;
      break;
    }
    if (round + 1 >= give_up_at) {
      fprintf(stderr, "too many discarded rounds, giving up on cell\n");
      break;
    }
  }

  summarize_rounds(result, per_variant, per_contrast);
  return result;
}

// carry-over check, a pattern such as AABB repeated warmup + cap times, no stopping rule
// the analysis groups a variant's intervals by the variant that ran before them
static inline RoundsResult run_sequence(Recorder& rec, const RunCtl& rc, const std::string& pattern,
                                        const std::function<Interval(int, int)>& run) {
  const std::string sequence_id = rc.cell_id + "#sequence";
  RoundsResult result;
  std::vector<std::vector<double>> per_variant(2);
  for (int repeat = 0; repeat < rc.warmup + rc.cap; repeat++) {
    const bool warm = repeat < rc.warmup;
    for (int position = 0; position < (int)pattern.size(); position++) {
      const int v = pattern[position] - 'A';
      Interval iv = run(v, position);
      if (warm && good_status(iv.status)) { iv.status = "WARMUP"; }
      rec.row(sequence_id, rc.cell_id + "#" + variant_letter(v), variant_letter(v), repeat, iv);
      if (!warm && good_status(iv.status) && !iv.cold) { per_variant[v].push_back(iv.per_op()); }
    }
    result.rounds = repeat + 1;
    if (warm) { result.warmups++; }
  }
  summarize_rounds(result, per_variant, {});
  return result;
}

// .done marker line of a round cell, per variant and per contrast c<i>
static inline std::string rounds_summary_line(const RunCtl& rc, const RoundsResult& r,
                                              const std::vector<Contrast>& contrasts) {
  char buf[256];
  snprintf(buf, sizeof buf, "cell=%s rounds=%d warmups=%d discards=%d k=%d floor_ns=%.6g",
           rc.cell_id.c_str(), r.rounds, r.warmups, r.discards, (int)r.variants.size(),
           rc.floor_ns);
  std::string line = buf;
  for (size_t v = 0; v < r.variants.size(); v++) {
    const Summary& s = r.variants[v];
    const std::string m = variant_letter((int)v);
    snprintf(buf, sizeof buf, " n%s=%d med%s=%.6g lo%s=%.6g hi%s=%.6g target%s=%d", m.c_str(), s.n,
             m.c_str(), s.median, m.c_str(), s.lo, m.c_str(), s.hi, m.c_str(), (int)point_target_met(s));
    line += buf;
  }
  for (size_t c = 0; c < r.contrasts.size(); c++) {
    const Summary& d = r.contrasts[c];
    const size_t i = c + 1;
    snprintf(buf, sizeof buf, " c%zu=%s n%zu=%d med%zu=%.6g lo%zu=%.6g hi%zu=%.6g target%zu=%d", i,
             contrasts[c].name.c_str(), i, d.n, i, d.median, i, d.lo, i, d.hi, i,
             (int)contrast_target_met(d, rc.floor_ns));
    line += buf;
  }
  snprintf(buf, sizeof buf, " cap_hit=%d stopped_on_target=%d", (int)r.cap_hit,
           (int)r.stopped_on_target);
  return line + buf;
}

}  // namespace suite
