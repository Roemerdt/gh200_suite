// median, rank-based 95 % interval, sign test and stopping targets, as in analysis/stats.py
#pragma once
#include <algorithm>
#include <cmath>
#include <vector>

namespace suite {

struct Summary {
  int n = 0;
  double median = 0, lo = 0, hi = 0;
};

static inline double log_binom_pmf(int n, int k) {
  return lgamma(n + 1.0) - lgamma(k + 1.0) - lgamma(n - k + 1.0) - n * log(2.0);
}

// 1-based ranks of the median's 95 % interval over n sorted values, after Hoefler and Belli
// 2015 section 4.2.2. lo is the largest l with P(Bin(n, 1/2) <= l-1) <= 0.025, hi = n + 1 - lo
// needs n >= 6 for 95 % coverage
static inline void median_ci_ranks(int n, int* lo, int* hi) {
  double cumulative = 0;
  int l = 0;
  for (int k = 0; k < n; k++) {
    cumulative += exp(log_binom_pmf(n, k));
    if (cumulative > 0.025) { break; }
    l = k + 1;
  }
  if (l < 1) { l = 1; }
  int u = n + 1 - l;
  if (u < l) { u = l; }
  *lo = l;
  *hi = u;
}

static inline Summary summarize(std::vector<double> values) {
  Summary s;
  s.n = (int)values.size();
  if (s.n == 0) { return s; }
  std::sort(values.begin(), values.end());
  s.median = (s.n % 2) ? values[s.n / 2] : 0.5 * (values[s.n / 2 - 1] + values[s.n / 2]);
  int lo, hi;
  median_ci_ranks(s.n, &lo, &hi);
  s.lo = values[lo - 1];
  s.hi = values[hi - 1];
  return s;
}

// two-sided exact sign test, the caller leaves out ties
static inline double sign_test_p(int n_positive, int n_negative) {
  const int m = n_positive + n_negative;
  if (m == 0) { return 1.0; }
  double lower_tail = 0, upper_tail = 0;
  for (int k = 0; k <= n_positive; k++) { lower_tail += exp(log_binom_pmf(m, k)); }
  for (int k = n_positive; k <= m; k++) { upper_tail += exp(log_binom_pmf(m, k)); }
  return std::min(1.0, 2.0 * std::min(lower_tail, upper_tail));
}

// full interval width within 2 % of the median
static inline bool point_target_met(const Summary& s) {
  return s.n >= 6 && s.median != 0 && (s.hi - s.lo) <= 0.02 * fabs(s.median);
}

// interval excludes zero, half-width within 10 % of the median
static inline bool pair_target_met(const Summary& d) {
  if (d.n < 6) { return false; }
  const bool excludes_zero = (d.lo > 0) || (d.hi < 0);
  return excludes_zero && 0.5 * (d.hi - d.lo) <= 0.10 * fabs(d.median);
}

}  // namespace suite
