"""Crossovers of the route difference along each axis, and the bisection cells still to run

usage: python3 -m analysis.crossovers results/<campaign> [--replicate results/<replicate>]
                [--floors harness/floors.json] [--bisection harness/bisection.json]
Writes summary/crossovers.csv and crossovers.md
"""
import argparse
import json
import math
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "..", "harness"))
from analysis.load import write_csv  # noqa: E402
from analysis.route import summarize_route  # noqa: E402
from analysis.stats import NAN  # noqa: E402
import grids  # noqa: E402

SUITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
NARROW = 1.25
# (axis, kernel, level knobs, home-setting knobs held fixed)
AXES = [
    ("f", "k1", ("f-num", "f-den"), {"footprint-mib": "1024"}),
    ("footprint", "k1", ("footprint-mib",), {"f-num": "1", "f-den": "1"}),
    ("footprint", "k3", ("footprint-mib",), {}),
    ("footprint", "k4", ("footprint-mib",), {"generator": "uniform"}),
    ("k", "k2", ("k",), {"footprint-mib": "1024", "working-set-mib": "32"}),
    ("sweeps", "k5", ("sweeps",), {"footprint-mib": "512", "tiling": "tiles"}),
]
NOT_AXIS_KNOBS = ("kernel", "placement", "type", "vary", "at",
                  "vary2", "at2", "replicate", "sequence", "tune", "copies")


def level_of(axis, knobs):
    if axis == "f":
        return Fraction(int(knobs["f-num"]), int(knobs["f-den"]))
    return float(knobs[{"footprint": "footprint-mib", "k": "k", "sweeps": "sweeps"}[axis]])


def level_text(axis, x):
    if axis == "f":
        return "%dof%d" % (x.numerator, x.denominator)
    return "%g" % x


def level_knobs(axis, x):
    if axis == "f":
        return {"f-num": str(x.numerator), "f-den": str(x.denominator)}
    knob = {"footprint": "footprint-mib", "k": "k", "sweeps": "sweeps"}[axis]
    return {knob: "%g" % x}


def midpoint(axis, a, b):
    m = math.sqrt(float(a) * float(b))
    if axis == "f":
        return Fraction(m).limit_denominator(1000)
    if axis == "footprint":
        return float(max(256, round(m / 256) * 256))
    return float(max(1, round(m)))


def axis_cells(table, axis, kernel, level_knob_names, fixed, placement):
    """{level: route cell}"""
    cells = {}
    for c in table:
        if c.get("kernel") != kernel or c.get("placement", "cpu") != placement:
            continue
        knobs = {k: v for k, v in c.items(
        ) if k in grids.HOME_SETTING[kernel] or k in level_knob_names}
        knobs = {k: str(v) for k, v in knobs.items() if v not in ("", None)}
        if any(c.get(k) not in ("", None, "none", "-") for k in ("host", "type", "vary", "page-size", "page-order", "partition",
                                                                 "index-order", "alignment", "rotated", "scope", "update", "keys",
                                                                 "issuer", "layout", "repeat")):
            if not (c.get("type") in ("", None, "route")):
                continue
            if any(c.get(k) not in ("", None, "none", "-", "random", "1g", "64k", "0") for k in ("host", "page-size", "page-order", "partition", "index-order", "alignment", "rotated", "scope")):
                continue
        if any(knobs.get(k, grids.HOME_SETTING[kernel].get(k)) != v for k, v in fixed.items()):
            continue
        try:
            x = level_of(axis, knobs)
        except (KeyError, ValueError):
            continue
        cells[x] = c
    return cells


def resolvable(c, floor_ns, replicate_cell):
    d = c.get("route_diff_ns", NAN)
    if d != d or not c.get("excludes_zero"):
        return 0
    if floor_ns == floor_ns and abs(d) <= floor_ns:
        return 0
    if replicate_cell is not None:
        r = replicate_cell.get("route_diff_ns", NAN)
        if r != r or (r > 0) != (d > 0) or not replicate_cell.get("excludes_zero"):
            return 0
    return 1 if d > 0 else -1


def brackets_of(levels, signs):
    """[(lower, upper)] per sign change between resolvable levels, unresolved levels in between fall inside"""
    out = []
    last_resolved = None
    for x in levels:
        s = signs[x]
        if s == 0:
            continue
        if last_resolved is not None and signs[last_resolved] != s:
            out.append((last_resolved, x))
        last_resolved = x
    return out


def model_crossovers(axis, cells, levels):
    """Bytes-and-bandwidth model, the home cell's parts scaled along the axis, with sign changes interpolated in log(level)"""
    home_level = {"f": Fraction(1), "footprint": 1024.0, "k": 16.0, "sweeps": 8.0}[
        axis]
    home = cells.get(home_level)
    if home is None:
        return [], {}
    direct_ns = home.get("direct_ns", NAN)
    copyin, kernel, copyout = home.get("copyin_ns", NAN), home.get(
        "copy_kernel_ns", NAN), home.get("copyout_ns", NAN)
    if any(v != v for v in (direct_ns, copyin, kernel, copyout)):
        return [], {}

    def parts(x):
        r = float(x) / float(home_level)
        if axis == "footprint":
            return direct_ns * r, copyin * r, kernel * r, copyout * r
        # the other axes scale the direct pass and the kernel
        # the buffer moves once
        return direct_ns * r, copyin, kernel * r, copyout

    modelled = {x: parts(x)[0] - sum(parts(x)[1:]) for x in levels}
    crossings = []
    ordered = sorted(levels)
    for a, b in zip(ordered, ordered[1:]):
        da, db = modelled[a], modelled[b]
        if (da > 0) != (db > 0) and da != db:
            la, lb = math.log(float(a)), math.log(float(b))
            t = da / (da - db)
            crossings.append(math.exp(la + t * (lb - la)))
    return crossings, modelled


def analyse(campaign, replicate, floors, sign_of=None, swap=None):
    """sign_of(cell, replicate cell) replaces the absolute rule where given
    swap maps a cell id to (cell, replicate cell) with the fastest copy, which then stands in for it"""
    tables = summarize_route(campaign)["route"]
    rep = {c["cell"]: c for c in summarize_route(
        replicate)["route"]} if replicate else {}
    floor_ns = floors.get("route", {}).get(
        "route_axes", {}).get("floor_ns", NAN)
    out, bisection = [], []
    for axis, kernel, knob_names, fixed in AXES:
        for placement in ("cpu", "hbm"):
            cells = axis_cells(tables, axis, kernel,
                               knob_names, fixed, placement)
            if len(cells) < 2:
                continue
            reps = {x: rep.get(
                c["cell"]) if replicate else None for x, c in cells.items()}
            for x, c in list(cells.items()):
                if swap and c["cell"] in swap:
                    cells[x], reps[x] = swap[c["cell"]]
            levels = sorted(cells)
            if sign_of is None:
                signs = {x: resolvable(
                    cells[x], floor_ns, reps[x]) for x in levels}
            else:
                signs = {x: sign_of(cells[x], reps[x]) for x in levels}
            brackets = brackets_of(levels, signs)
            crossings, modelled = model_crossovers(axis, cells, levels)
            row = dict(axis=axis, kernel=kernel, placement=placement, n_levels=len(levels),
                       levels=" ".join(level_text(axis, x) for x in levels),
                       route_diff_ms=" ".join(
                           "%.3f" % (cells[x]["route_diff_ns"] / 1e6) for x in levels),
                       resolvable_signs=" ".join(
                           {1: "+", -1: "-", 0: "?"}[signs[x]] for x in levels),
                       floor_ns=floor_ns, replicate_used=bool(replicate),
                       model_crossovers=" ".join(
                           "%.4g" % c for c in crossings),
                       model_diff_ms=" ".join("%.3f" % (modelled[x] / 1e6) for x in levels) if modelled else "")
            if not brackets:
                row.update(outcome="no sign change on the grid" if any(
                    signs.values()) else "not resolvable", brackets="")
            else:
                texts = []
                for lo, hi in brackets:
                    width = float(hi) / float(lo)
                    copies = {cells[lo].get(
                        "copy_label"), cells[hi].get("copy_label")}
                    shapes = {cells[lo].get(
                        "direct_shape"), cells[hi].get("direct_shape")}
                    flag = " (tuning changes inside: %s)" % ", ".join(sorted(
                        str(v) for v in copies | shapes)) if len(copies) > 1 or len(shapes) > 1 else ""
                    mid = math.sqrt(float(lo) * float(hi))
                    distance = (" model crossover at %s" % " and ".join("%.4g (x%.2f from the middle)" % (c, c / mid if c > mid else mid / c) for c in crossings)
                                if crossings else " model: no crossover")
                    texts.append("[%s, %s] width x%.2f%s;%s" % (level_text(
                        axis, lo), level_text(axis, hi), width, flag, distance))
                    if width > NARROW:
                        m = midpoint(axis, lo, hi)
                        if m not in cells and float(lo) < float(m) < float(hi):
                            bisection.append(dict(axis=axis, kernel=kernel, placement=placement, level=level_text(axis, m),
                                                  knobs=level_knobs(axis, m), bracket=[level_text(axis, lo), level_text(axis, hi)]))
                row.update(outcome="%d sign change(s)" %
                           len(brackets), brackets="; ".join(texts))
            out.append(row)
    return out, bisection


def write_md(path, rows, bisection):
    with open(path, "w") as md:
        md.write("# Crossovers along the axes\n\nRoute difference (direct minus copy, ms) per level; signs are given only for "
                 "resolvable levels (interval excludes zero, above the route floor, replicate agreeing where given). A bracket "
                 "is reported for every sign change, with its width as a factor, a flag where the frozen tuning differs between "
                 "its ends, and the factor between the bytes-and-bandwidth model's crossover and the bracket's middle.\n\n"
                 "| axis | kernel | placement | levels | route difference ms | signs | outcome | brackets | model crossover(s) |\n"
                 "|---|---|---|---|---|---|---|---|---|\n")
        for r in rows:
            md.write("| %s | %s | %s | %s | %s | %s | %s | %s | %s |\n" % (
                r["axis"], r["kernel"], r["placement"], r["levels"], r["route_diff_ms"], r["resolvable_signs"], r["outcome"],
                r["brackets"], r["model_crossovers"]))
        if bisection:
            md.write("\n## Bisection cells to run\n\n")
            for b in bisection:
                md.write("- %s %s at %s placement: level %s inside [%s, %s]\n" % (b["kernel"], b["axis"], b["placement"], b["level"],
                                                                                  b["bracket"][0], b["bracket"][1]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("campaign")
    parser.add_argument("--replicate", default=None)
    parser.add_argument(
        "--floors", default=os.path.join(SUITE, "harness", "floors.json"))
    parser.add_argument(
        "--bisection", default=os.path.join(SUITE, "harness", "bisection.json"))
    args = parser.parse_args()
    try:
        floors = json.load(open(args.floors))
    except FileNotFoundError:
        floors = {}
    rows, bisection = analyse(args.campaign, args.replicate, floors)
    summary_dir = os.path.join(args.campaign, "summary")
    os.makedirs(summary_dir, exist_ok=True)
    write_csv(os.path.join(summary_dir, "crossovers.csv"), rows)
    write_md(os.path.join(summary_dir, "crossovers.md"), rows, bisection)
    # the bisection file accumulates the levels of every round, so the replicate runs them all
    try:
        previous = json.load(open(args.bisection))
    except (FileNotFoundError, ValueError):
        previous = []
    known = {(b["kernel"], b["axis"], b["placement"], b["level"])
             for b in previous}
    merged = previous + \
        [b for b in bisection if (
            b["kernel"], b["axis"], b["placement"], b["level"]) not in known]
    with open(args.bisection, "w") as f:
        json.dump(merged, f, indent=1)
        f.write("\n")
    for r in rows:
        print("%-9s %-3s %-3s %s: %s %s" %
              (r["axis"], r["kernel"], r["placement"], r["resolvable_signs"], r["outcome"], r["brackets"]))
    print("%d new bisection cell(s); %d in %s" %
          (len(bisection), len(merged), os.path.relpath(args.bisection, SUITE)))


if __name__ == "__main__":
    main()
