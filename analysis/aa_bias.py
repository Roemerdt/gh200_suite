"""Allocation-order check, B - A of the A/A' cells per setting and placement

usage: python3 -m analysis.aa_bias results/<campaign> results/<replicate> [--extra results/c1 results/c2]
Writes summary/aa_bias.csv and aa_bias.md in the campaign's directory
"""
import argparse
import os
import statistics

from analysis.load import write_csv
from analysis.route import summarize_route
from analysis.stats import NAN


def setting_of(cell_id):
    """Cell id without its replicate"""
    instr, rest = cell_id.split("/", 1)
    return "%s/%s" % (instr, ",".join(p for p in rest.split(",") if not p.startswith("replicate=")))


def analyse(dirs):
    cells, groups = [], {}
    for d in dirs:
        for c in summarize_route(d)["aa"]:
            row = dict(campaign=os.path.basename(os.path.normpath(d)), cell=c["cell"], setting=setting_of(c["cell"]),
                       a_ms=c["home_ns"] / 1e6, b_ms=c["level_ns"] / 1e6, diff_ms=c["effect_ns"] / 1e6,
                       diff_lo_ms=c["effect_lo_ns"] / 1e6, diff_hi_ms=c["effect_hi_ns"] / 1e6,
                       rel=c["effect_rel_home"], excludes_zero=bool(c["excludes_zero"]), n_pairs=c["n_pairs"],
                       first=c.get("first", ""))
            cells.append(row)
            groups.setdefault(row["setting"], []).append(row)
    summary = []
    for setting, rows in sorted(groups.items()):
        rels = [r["rel"] for r in rows if r["rel"] == r["rel"]]
        summary.append(dict(setting=setting, cells=len(rows),
                            median_rel=statistics.median(
                                rels) if rels else NAN,
                            min_rel=min(rels) if rels else NAN, max_rel=max(rels) if rels else NAN,
                            b_faster=sum(
                                1 for r in rows if r["excludes_zero"] and r["diff_ms"] < 0),
                            b_slower=sum(1 for r in rows if r["excludes_zero"] and r["diff_ms"] > 0)))
    return cells, summary


def pct(x):
    return "--" if x != x else "%+.1f %%" % (100 * x)


def write_md(path, cells, summary):
    lines = ["# A/A' cells: what the allocation order alone does to a contrast\n",
             "B - A between two identically prepared direct variants, B allocated after A as the level variant of a "
             "factor cell is allocated after its control. Per setting over all its cells (processes and campaigns): "
             "the median of B - A relative to A, its range, and the cells whose interval excludes zero with B faster "
             "or slower.\n",
             "| setting | cells | median B - A | range | B faster | B slower |", "|---|---|---|---|---|---|"]
    for s in summary:
        lines.append("| %s | %d | %s | %s to %s | %d | %d |" % (s["setting"].split("/", 1)[1], s["cells"], pct(s["median_rel"]),
                                                                pct(s["min_rel"]), pct(s["max_rel"]), s["b_faster"], s["b_slower"]))
    lines += ["", "## Per cell\n", "| campaign | cell | A ms | B ms | B - A ms [interval] | relative | pairs | first |",
              "|---|---|---|---|---|---|---|---|"]
    for c in cells:
        lines.append("| %s | %s | %.4f | %.4f | %.4f [%.4f, %.4f] | %s | %d | %s |" % (
            c["campaign"], c["cell"].split(
                "/", 1)[1], c["a_ms"], c["b_ms"], c["diff_ms"], c["diff_lo_ms"], c["diff_hi_ms"],
            pct(c["rel"]), c["n_pairs"], c["first"]))
    open(path, "w").write("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("campaign")
    parser.add_argument("replicate")
    parser.add_argument("--extra", nargs="*", default=[],
                        help="further results directories with A/A' cells")
    args = parser.parse_args()
    cells, summary = analyse([args.campaign, args.replicate] + args.extra)
    out = os.path.join(args.campaign, "summary")
    os.makedirs(out, exist_ok=True)
    write_csv(os.path.join(out, "aa_bias.csv"), cells)
    write_md(os.path.join(out, "aa_bias.md"), cells, summary)
    for s in summary:
        print("%-100s %2d cells  median %s  range %s to %s  B faster %d, slower %d" % (
            s["setting"].split("/", 1)[1], s["cells"], pct(s["median_rel"]
                                                           ), pct(s["min_rel"]), pct(s["max_rel"]),
            s["b_faster"], s["b_slower"]))


if __name__ == "__main__":
    main()
