#!/usr/bin/env python3
"""Freezes a campaign's repetitions per interval into harness/calibrated_passes.json, for campaign.py's --passes

usage: python3 harness/freeze_passes.py results/<campaign> [--target-ms 20] [--overwrite]
"""
import argparse
import json
import math
import os
import sys

SUITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, SUITE)
from analysis.load import load_rows, group_cells  # noqa: E402

PASSES_FILE = os.path.join(SUITE, "harness", "calibrated_passes.json")
MAX_PASSES = 100000
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def fastest_repetition_ns(rows):
    """Smallest repetition time, counting a copy row's first call as one"""
    candidates = [r["ns_per_op"] for r in rows]
    for r in rows:
        parts = [r.get(column) for column in ("copyin_ns", "kernel_ns", "copyout_ns")]
        if all(isinstance(p, (int, float)) and p == p for p in parts):
            candidates.append(sum(parts))
    return min(candidates)


def frozen_counts(cell, target_ns):
    """{letter: count} for the cell, and {letter: counts the rows used}"""
    counts, used = {}, {}
    for member in sorted({r["member"] for r in cell.rows if r["member"] in LETTERS}):
        rows = [r for r in cell.rows if r["member"] == member and r["status"] in ("OK", "WARMUP") and r["cold"] == 0]
        if not rows:
            continue
        used[member] = sorted({r["passes"] for r in rows if r["status"] == "OK"})
        recomputed = max(1, min(MAX_PASSES, math.ceil(target_ns / fastest_repetition_ns(rows))))
        counts[member] = used[member][-1] if used[member] else recomputed
    return counts, used


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("results")
    parser.add_argument("--target-ms", type=float, default=20.0, help="the campaign's --target-ms")
    parser.add_argument("--overwrite", action="store_true", help="replace entries already in the file")
    parser.add_argument("--out", default=PASSES_FILE)
    args = parser.parse_args()

    frozen = {}
    if os.path.exists(args.out):
        with open(args.out) as f:
            frozen = json.load(f)
    cells = {cell_id: cell for cell_id, cell in group_cells(load_rows(args.results)).items() if cell.instr == "route"}
    added = kept = 0
    for cell_id in sorted(cells):
        counts, used = frozen_counts(cells[cell_id], args.target_ms * 1e6)
        if not counts:
            continue
        for member, count in counts.items():
            if len(used[member]) > 1:
                print("note: %s variant %s: the counted rows used %s, frozen at %d" % (cell_id, member, used[member], count))
        if cell_id in frozen and not args.overwrite:
            kept += 1
            if frozen[cell_id] != counts:
                print("kept %s: file has %s, this campaign gives %s" % (cell_id, frozen[cell_id], counts))
            continue
        frozen[cell_id] = counts
        added += 1
    with open(args.out, "w") as f:
        json.dump(dict(sorted(frozen.items())), f, indent=1, sort_keys=True)
        f.write("\n")
    print("%s: %d cells frozen, %d kept, %d in the file" % (os.path.relpath(args.out, SUITE), added, kept, len(frozen)))


if __name__ == "__main__":
    main()
