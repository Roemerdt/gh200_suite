"""Calibration floors from two runs of the same cells with different seeds

usage: python3 -m analysis.floors results/<campaign 1> results/<campaign 2> [--out harness/floors.json] [--merge]
"""
import argparse
import json
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "..", "harness"))
from analysis.load import knobs_of  # noqa: E402
from analysis.route import summarize_route  # noqa: E402
from analysis.stats import NAN  # noqa: E402
import grids  # noqa: E402

SUITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
CONTRASTS = {"route": ["route_diff_ns"],
             "factor": ["effect_ns"],
             "four": ["rd_home_ns", "rd_level_ns", "change_ns"],
             "kvar": ["effect_ns"],
             "cross": ["effect1_home_ns", "effect1_level2_ns", "change_ns", "effect2_home_ns"],
             "aa": ["effect_ns"]}
MIN_CONTRASTS = 20


def percentile(values, q):
    ordered = sorted(values)
    if not ordered:
        return NAN
    rank = max(0, min(len(ordered) - 1, int(math.ceil(q * len(ordered))) - 1))
    return ordered[rank]


def contrast_key(row, family):
    return (row["cell"], row.get("variant", "")) if family == "kvar" else (row["cell"], "")


def changes(tables1, tables2):
    """{(family, group): [(cell, contrast, change in ns)]} over the cells complete in both campaigns"""
    out = {}
    for family, columns in CONTRASTS.items():
        rows2 = {contrast_key(r, family): r for r in tables2[family]}
        for r1 in tables1[family]:
            r2 = rows2.get(contrast_key(r1, family))
            if r2 is None:
                continue
            _, group = grids.family_group(knobs_of(r1["cell"]))
            for column in columns:
                a, b = r1.get(column), r2.get(column)
                if isinstance(a, float) and isinstance(b, float) and a == a and b == b:
                    out.setdefault((family, group), []).append(
                        (r1["cell"], column, b - a))
    return out


def floors_from(change_lists):
    floors = {}
    for family in CONTRASTS:
        family_changes = [abs(c) for (
            f, _), items in change_lists.items() if f == family for _, _, c in items]
        family_floor = percentile(
            family_changes, 0.9) if family_changes else NAN
        for (f, group), items in change_lists.items():
            if f != family:
                continue
            own = [abs(c) for _, _, c in items]
            if len(own) >= MIN_CONTRASTS:
                floor, rule = percentile(
                    own, 0.9), "90th percentile of %d contrasts" % len(own)
            else:
                floor = max(family_floor, max(
                    own)) if family_changes else max(own)
                rule = "fewer than %d contrasts (%d): the larger of the family floor over %d and the group's largest change" % (
                    MIN_CONTRASTS, len(own), len(family_changes))
            floors.setdefault(family, {})[group] = dict(
                floor_ns=floor, n=len(own), rule=rule)
    return floors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("campaign1")
    parser.add_argument("campaign2")
    parser.add_argument(
        "--out", default=os.path.join(SUITE, "harness", "floors.json"))
    parser.add_argument("--merge", action="store_true",
                        help="keep the entries of --out whose family and group these campaigns do not cover")
    args = parser.parse_args()
    tables1, tables2 = summarize_route(
        args.campaign1), summarize_route(args.campaign2)
    change_lists = changes(tables1, tables2)
    floors = floors_from(change_lists)
    if args.merge and os.path.exists(args.out):
        kept = json.load(open(args.out))
        for family, groups in kept.items():
            for group, entry in groups.items():
                floors.setdefault(family, {}).setdefault(group, entry)
    print("%-8s %-12s %5s %14s  %s" %
          ("family", "group", "n", "floor ms", "rule"))
    for family in sorted(floors):
        for group in sorted(floors[family]):
            e = floors[family][group]
            print("%-8s %-12s %5d %14.4f  %s" %
                  (family, group, e["n"], e["floor_ns"] / 1e6, e["rule"]))
    for (family, group), items in sorted(change_lists.items()):
        worst = max(items, key=lambda t: abs(t[2]))
        print("  largest change in %s/%s: %.4f ms (%s, %s)" %
              (family, group, worst[2] / 1e6, worst[1], worst[0]))
    with open(args.out, "w") as f:
        json.dump(floors, f, indent=1, sort_keys=True)
        f.write("\n")
    print("written %s" % os.path.relpath(args.out, SUITE))


if __name__ == "__main__":
    main()
