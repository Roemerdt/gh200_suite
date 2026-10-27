"""Medians with rank intervals (Hoefler and Belli 2015, section 4.2.2) and the exact sign test
src/common/stats.h uses the same rank rule"""
import math

NAN = float("nan")


def median_ci_ranks(n, alpha=0.05):
    """1-based ranks (lo, hi) of the ~95 % interval of the median of n sorted values
    lo is the largest l with P(Bin(n, 1/2) <= l-1) <= alpha/2, hi = n + 1 - lo"""
    cumulative = 0.0
    lo = 0
    for k in range(n):
        cumulative += math.comb(n, k) / 2.0 ** n
        if cumulative > alpha / 2:
            break
        lo = k + 1
    lo = max(lo, 1)
    return lo, max(n + 1 - lo, lo)


def median(values):
    ordered = sorted(values)
    n = len(ordered)
    if n == 0:
        return NAN
    return ordered[n // 2] if n % 2 else 0.5 * (ordered[n // 2 - 1] + ordered[n // 2])


def median_ci(values):
    """(n, median, lo, hi)"""
    ordered = sorted(values)
    n = len(ordered)
    if n == 0:
        return 0, NAN, NAN, NAN
    lo_rank, hi_rank = median_ci_ranks(n)
    return n, median(ordered), ordered[lo_rank - 1], ordered[hi_rank - 1]


def sign_test_p(n_positive, n_negative):
    """Two-sided exact sign test, ties dropped by the caller"""
    m = n_positive + n_negative
    if m == 0:
        return 1.0
    lower_tail = sum(math.comb(m, k)
                     for k in range(0, n_positive + 1)) / 2.0 ** m
    upper_tail = sum(math.comb(m, k)
                     for k in range(n_positive, m + 1)) / 2.0 ** m
    return min(1.0, 2.0 * min(lower_tail, upper_tail))


def diff_summary(diffs):
    """Median of paired differences or within-round contrasts, with rank interval and sign test"""
    n, med, lo, hi = median_ci(diffs)
    n_positive = sum(1 for d in diffs if d > 0)
    n_negative = sum(1 for d in diffs if d < 0)
    return dict(n=n, median=med, lo=lo, hi=hi, npos=n_positive, nneg=n_negative,
                sign_p=sign_test_p(n_positive, n_negative),
                excludes_zero=(n > 0 and (lo > 0 or hi < 0)), diffs=diffs)


def paired_delta(a_values, b_values):
    """A - B over lists already matched by repeat"""
    return diff_summary([a - b for a, b in zip(a_values, b_values)])
