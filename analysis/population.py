"""Population row of the one-time costs, from the transient cells (src/route/transient.h)

usage: python3 -m analysis.population results/<campaign>
Writes summary/population.csv and population.md
"""
import csv
import glob
import math
import os
import sys

from analysis.load import knobs_of, write_csv
from analysis.stats import NAN, diff_summary, median_ci

REFERENCE = "cpu-all"
SETUP_STEPS = ("register", "fill", "malloc", "copyin")
FINISH_STEPS = ("copyout",)
TEARDOWN_STEPS = ("unregister", "unmap", "free")
GPU_NODE = 1


def census(text):
    """{'n0': a, 'n1': b, 'absent': c, 'other': d} from 'n0=a;n1=b;absent=c;other=d', else {}"""
    try:
        return {k: int(v) for k, v in (part.split("=") for part in text.split(";"))}
    except ValueError:
        return {}


def read_rounds(results_dir):
    """{(kernel, MiB): {level: {(process, round): record}}}, WARMUP rows left out"""
    data = {}
    for path in sorted(glob.glob(os.path.join(results_dir, "raw", "transient", "*.csv"))):
        with open(path, newline="") as f:
            for row in csv.DictReader(f):
                if row["status"] not in ("OK", "VOID_CHECKSUM"):
                    continue
                knobs = knobs_of(row["cell_id"])
                setting = (row["kernel"], int(
                    row["footprint_bytes"]) / 2 ** 20)
                level = data.setdefault(
                    setting, {}).setdefault(row["member"], {})
                rec = level.setdefault((knobs.get("process", "1"), int(row["rep"])), dict(
                    setup=0.0, runs={}, finish=0.0, teardown=0.0, void=False, fill=row["fill"], node=int(row["node"]),
                    thp=int(row["thp"]), pre=census(row["residency_pre"]), post=census(row["residency_post"]),
                    ahp_kb=NAN, quiet_ms=float(row["quiet_ms"])))
                ns, step = float(row["interval_ns"]), row["step"]
                if step in SETUP_STEPS:
                    rec["setup"] += ns
                    if step == "fill" and row["ahp_kb"] != "NA":
                        rec["ahp_kb"] = float(row["ahp_kb"])
                elif step in ("run", "call"):
                    rec["runs"][int(row["run"])] = ns
                elif step in FINISH_STEPS:
                    rec["finish"] += ns
                elif step in TEARDOWN_STEPS:
                    rec["teardown"] += ns
                rec["void"] = rec["void"] or row["status"] == "VOID_CHECKSUM"
    return data


def cumulative(rec, j):
    """Set-up through run j, plus copy-out and teardown"""
    return rec["setup"] + sum(rec["runs"][i] for i in range(1, j + 1)) + rec["finish"] + rec["teardown"]


def guard_ok(rec):
    """Every sampled page on the level's node after population, and none populated before a GPU population"""
    if rec["fill"] == "gpu-device":
        return True
    node = rec["node"] if rec["node"] >= 0 else GPU_NODE
    if rec["fill"] in ("copy", "copy-calls"):
        node = 0
    post = rec["post"]
    total = sum(post.values())
    if not total or post.get("n%d" % node, 0) != total:
        return False
    if rec["fill"] == "gpu":
        pre = rec["pre"]
        return sum(pre.values()) > 0 and pre.get("absent", 0) == sum(pre.values())
    return True


def spearman(xs, ys):
    """Spearman's rho with average ranks for ties, nan below three points"""
    def ranks(values):
        order = sorted(range(len(values)), key=lambda i: values[i])
        r = [0.0] * len(values)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and values[order[j + 1]] == values[order[i]]:
                j += 1
            for k in range(i, j + 1):
                r[order[k]] = (i + j) / 2.0 + 1
            i = j + 1
        return r
    if len(xs) < 3:
        return NAN
    rx, ry = ranks(xs), ranks(ys)
    mx, my = sum(rx) / len(rx), sum(ry) / len(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = math.sqrt(sum((a - mx) ** 2 for a in rx)
                    * sum((b - my) ** 2 for b in ry))
    return num / den if den else NAN


def break_even(net_m, run_diff_m, m):
    """Runs until the net effect against the reference reaches zero, extrapolated past m at the run-m difference, else nan"""
    if run_diff_m == 0 or net_m == 0 or (net_m > 0) == (run_diff_m > 0):
        return NAN
    return m - net_m / run_diff_m


def summarize_population(results_dir):
    out = []
    for setting in sorted(read_rounds(results_dir).items()):
        (kernel, mib), levels = setting
        ref = levels.get(REFERENCE, {})
        for name in sorted(levels, key=lambda n: (n != REFERENCE, n)):
            rounds = {k: r for k, r in levels[name].items(
            ) if not r["void"] and r["runs"]}
            good = {k: r for k, r in rounds.items() if guard_ok(r)}
            m = min(len(r["runs"]) for r in rounds.values()) if rounds else 0
            paired = [k for k in good if k in ref and guard_ok(
                ref[k]) and not ref[k]["void"]]
            setup, run1, run2, runm = (median_ci([r["setup"] for r in good.values()]),
                                       median_ci([r["runs"][1]
                                                 for r in good.values()]),
                                       median_ci(
                                           [r["runs"][2] for r in good.values() if 2 in r["runs"]]),
                                       median_ci([r["runs"][m] for r in good.values() if m in r["runs"]]))
            excess = diff_summary([r["runs"][1] - r["runs"][m]
                                  for r in good.values()])
            teardown = median_ci([r["teardown"] for r in good.values()])
            d_setup = diff_summary(
                [good[k]["setup"] - ref[k]["setup"] for k in paired])
            d_runm = diff_summary(
                [good[k]["runs"][m] - ref[k]["runs"][m] for k in paired])
            net1 = diff_summary(
                [cumulative(good[k], 1) - cumulative(ref[k], 1) for k in paired])
            netm = diff_summary(
                [cumulative(good[k], m) - cumulative(ref[k], m) for k in paired])
            rhos = []
            for process in sorted({k[0] for k in good}):
                keys = sorted(k for k in good if k[0] == process)
                rhos.append(spearman([k[1] for k in keys], [
                            good[k]["setup"] for k in keys]))
            ahp = median_ci([r["ahp_kb"]
                            for r in good.values() if r["ahp_kb"] == r["ahp_kb"]])
            quiet = median_ci([r["quiet_ms"] for r in rounds.values()])
            out.append(dict(kernel=kernel, footprint_mib=mib, level=name, rounds=len(rounds), guard_failures=len(rounds) - len(good),
                            runs=m, setup_ms=setup[1] / 1e6, setup_lo_ms=setup[2] / 1e6, setup_hi_ms=setup[3] / 1e6,
                            run1_ms=run1[1] / 1e6, run2_ms=run2[1] / 1e6, runm_ms=runm[1] / 1e6,
                            first_excess_ms=excess["median"] / 1e6, teardown_ms=teardown[1] / 1e6,
                            d_setup_ms=d_setup["median"] / 1e6, d_setup_lo_ms=d_setup["lo"] / 1e6, d_setup_hi_ms=d_setup["hi"] / 1e6,
                            d_runm_ms=d_runm["median"] / 1e6, d_runm_lo_ms=d_runm["lo"] / 1e6, d_runm_hi_ms=d_runm["hi"] / 1e6,
                            net1_ms=net1["median"] / 1e6, netm_ms=netm["median"] / 1e6, netm_lo_ms=netm["lo"] / 1e6,
                            netm_hi_ms=netm["hi"] / 1e6, break_even_runs=break_even(netm["median"], d_runm["median"], m),
                            ahp_mib=ahp[1] / 1024, quiet_ms=quiet[1], setup_trend_rho=max(rhos, key=lambda r: abs(r) if r == r else -1) if rhos else NAN))
    summary_dir = os.path.join(results_dir, "summary")
    os.makedirs(summary_dir, exist_ok=True)
    write_csv(os.path.join(summary_dir, "population.csv"), out)
    write_md(os.path.join(summary_dir, "population.md"), out)
    return out


def write_md(path, entries):
    def f(v, digits=2):
        return "%.*f" % (digits, v) if v == v else "-"
    with open(path, "w") as md:
        md.write("# population row\n\nPer setting and level over the counted rounds: medians in ms (set-up with its 95 %% "
                 "interval); differences against %s in the same round; net effect = set-up, runs, copy-out and teardown; "
                 "break-even in runs (beyond m extrapolated); the largest |rho| of the set-up over the rounds of a "
                 "process.\n\n" % REFERENCE)
        md.write("| kernel | MiB | level | rounds | guard fail | set-up | run 1 | run 2 | run m | run 1 - run m | teardown | "
                 "d set-up | d run m | net after 1 | net after m | break-even | AnonHuge MiB | quiet ms | rho |\n"
                 "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
        for e in entries:
            md.write("| %s | %d | %s | %d | %d | %s [%s, %s] | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n" % (
                e["kernel"], e["footprint_mib"], e["level"], e["rounds"], e["guard_failures"], f(
                    e["setup_ms"]),
                f(e["setup_lo_ms"]), f(e["setup_hi_ms"]), f(
                    e["run1_ms"]), f(e["run2_ms"]), f(e["runm_ms"]),
                f(e["first_excess_ms"]), f(e["teardown_ms"]), f(
                    e["d_setup_ms"]), f(e["d_runm_ms"]), f(e["net1_ms"]),
                f(e["netm_ms"]), f(e["break_even_runs"], 1), f(e["ahp_mib"], 0), f(e["quiet_ms"], 0), f(e["setup_trend_rho"])))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    entries = summarize_population(sys.argv[1])
    print("%d population entries" % len(entries))
