#!/usr/bin/env python3
"""Freezes a campaign's tuned launch shapes and copies into harness/tuned_direct.json and tuned_copy.json

usage: python3 harness/freeze_tuning.py results/<campaign> [--held-out] [--floor-ns F]
"""
import argparse
import json
import os
import sys

SUITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, SUITE)
from analysis.route import summarize_route  # noqa: E402
sys.path.insert(0, os.path.join(SUITE, "harness"))
import grids  # noqa: E402

DIRECT_FILE = os.path.join(SUITE, "harness", "tuned_direct.json")
COPY_FILE = os.path.join(SUITE, "harness", "tuned_copy.json")
NOT_SETTING = ("kernel", "placement", "type", "tune", "vary", "at", "vary2", "at2", "replicate", "sequence", "copies")
SIMPLEST = "ce-pageable-1-whole-none-whole"


def setting_key(knobs):
    """Sorted key of the knobs that describe the setting"""
    return ",".join("%s=%s" % (k, v) for k, v in sorted(knobs.items()) if k not in NOT_SETTING)


def save(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=1, sort_keys=True)
        f.write("\n")


def by_cell(rows):
    cells = {}
    for r in rows:
        cells.setdefault(r["cell"], []).append(r)
    return cells


def freeze_direct(cells, tuned, floor_ns, home_floor_notes):
    for cell_id, rows in cells.items():
        head = rows[0]
        knobs = grids.cell_knobs(cell_id)
        route = "direct" if head["tune"] == "direct" else "copy"
        ranked = sorted(rows, key=lambda r: r["rank"])
        entry = dict(shape=ranked[0]["config"], median_ns=ranked[0]["ns"], runner_up=ranked[1]["config"] if len(ranked) > 1 else "",
                     runner_up_ns=ranked[1]["ns"] if len(ranked) > 1 else float("nan"), cell=cell_id, n_rounds=ranked[0]["n_rounds"])
        slot = tuned.setdefault(knobs["kernel"], {}).setdefault(knobs["placement"], {}).setdefault(route, {})
        key = setting_key(knobs)
        slot.setdefault("at", {})[key] = entry
    # home entry of each slot, else the first setting tuned
    # K5's untiled shape stands in for its tiled home, whose shape is fixed
    for kernel, placements in tuned.items():
        for placement, routes in placements.items():
            for route, slot in routes.items():
                at = slot.get("at", {})
                if not at:
                    continue
                home_setting = dict(grids.HOME_SETTING.get(kernel, {}))
                candidates = [setting_key(home_setting), setting_key(dict(home_setting, tiling="none"))]
                home_key = next((k for k in candidates if k in at), sorted(at)[0])
                slot["home"], slot["home_key"] = at[home_key], home_key
    # re-freeze where the home shape is slower than the best by more than the floor
    for kernel, placements in tuned.items():
        for placement, routes in placements.items():
            for route, slot in routes.items():
                home = slot.get("home")
                if not home:
                    continue
                for key, entry in slot.get("at", {}).items():
                    if key == slot.get("home_key") or entry["shape"] == home["shape"] or entry["cell"] not in cells:
                        continue
                    cell_rows = cells.get(entry["cell"], [])
                    home_shape_row = next((r for r in cell_rows if r["config"] == home["shape"]), None)
                    gap = (home_shape_row["ns"] - entry["median_ns"]) if home_shape_row else float("nan")
                    entry["home_shape_slower_by_ns"] = gap
                    entry["refrozen"] = bool(gap == gap and gap > floor_ns)
                    home_floor_notes.append("%s %s %s at %s: best %s, home shape %s slower by %.4f ms%s" % (
                        kernel, placement, route, key, entry["shape"], home["shape"], gap / 1e6,
                        " (re-frozen for this setting)" if entry["refrozen"] else ""))


def freeze_copy(cells, tuned, floor_ns, held_out):
    for cell_id, rows in cells.items():
        knobs = grids.cell_knobs(cell_id)
        ranked = sorted(rows, key=lambda r: r["rank"])
        fastest = ranked[0]
        # touched lines where the kernel's space has no whole-input form (K2 copies its window)
        simplest_label = SIMPLEST if any(r["config"] == SIMPLEST for r in rows) else SIMPLEST.rsplit("-", 1)[0] + "-touched"
        simplest = next((r for r in rows if r["config"] == simplest_label), None)
        slot = tuned.setdefault(knobs["kernel"], {}).setdefault(knobs["placement"], {})
        key = setting_key(knobs)
        previous = slot.get(key, {})
        if held_out and not previous:
            print("held-out cell without a tuning entry: %s" % cell_id)
            continue
        entry = dict(previous)
        entry.update(cell=cell_id, n_rounds=fastest["n_rounds"])
        if not held_out:
            entry.update(fastest=fastest["config"], fastest_ns=fastest["ns"],
                         runner_up=ranked[1]["config"] if len(ranked) > 1 else "", runner_up_ns=ranked[1]["ns"] if len(ranked) > 1 else float("nan"),
                         simplest=simplest_label, held_out=False)
        else:
            entry.update(held_out=True, held_out_cell=cell_id, held_out_fastest=fastest["config"])
        slowdown_hi = simplest["vs_fastest_hi_ns"] if simplest else float("nan")
        entry.update(simplest_ns=simplest["ns"] if simplest else float("nan"), simplest_slowdown_hi_ns=slowdown_hi)
        simplest_within_floor = bool(slowdown_hi == slowdown_hi and slowdown_hi < floor_ns)
        entry.update(copy=simplest_label if simplest_within_floor else fastest["config"],
                     sensitivity=fastest["config"] if simplest_within_floor else "",
                     rule="simplest within the floor of %.4f ms" % (floor_ns / 1e6) if simplest_within_floor else "fastest")
        slot[key] = entry


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("results")
    parser.add_argument("--held-out", action="store_true", help="the campaign holds the held-out block")
    parser.add_argument("--floor-ns", type=float, default=None,
                        help="the route family's calibration floor (default: from harness/floors.json)")
    args = parser.parse_args()
    floor_ns = args.floor_ns
    if floor_ns is None:
        floor_ns = grids.load_json(os.path.join(SUITE, "harness", "floors.json")).get("route", {}).get("route_axes", {}).get("floor_ns", 0.0)
    tables = summarize_route(args.results)
    cells = by_cell(tables["tune"])
    direct_cells = {c: rows for c, rows in cells.items() if rows[0]["tune"] in ("direct", "copy-kernel")}
    copy_cells = {c: rows for c, rows in cells.items() if rows[0]["tune"] == "copy"}
    notes = []
    if direct_cells:
        tuned = grids.load_json(DIRECT_FILE)
        freeze_direct(direct_cells, tuned, floor_ns, notes)
        save(DIRECT_FILE, tuned)
        for kernel, placements in sorted(tuned.items()):
            for placement, routes in sorted(placements.items()):
                for route, slot in sorted(routes.items()):
                    h = slot.get("home", {})
                    print("%-4s %-4s %-7s home shape %-14s %.4f ms, runner-up %-14s %.4f ms" % (
                        kernel, placement, route, h.get("shape"), h.get("median_ns", float("nan")) / 1e6, h.get("runner_up"),
                        h.get("runner_up_ns", float("nan")) / 1e6))
        for note in notes:
            print("  " + note)
        print("written %s" % os.path.relpath(DIRECT_FILE, SUITE))
    if copy_cells:
        tuned = grids.load_json(COPY_FILE)
        freeze_copy(copy_cells, tuned, floor_ns, args.held_out)
        save(COPY_FILE, tuned)
        for kernel, placements in sorted(tuned.items()):
            for placement, settings in sorted(placements.items()):
                for key, e in sorted(settings.items()):
                    print("%-4s %-4s %-44s frozen %-38s (%s); fastest %s %.4f ms, simplest %.4f ms, slowdown hi %.4f ms%s" % (
                        kernel, placement, key, e["copy"], e["rule"], e["fastest"], e["fastest_ns"] / 1e6,
                        e.get("simplest_ns", float("nan")) / 1e6, e.get("simplest_slowdown_hi_ns", float("nan")) / 1e6,
                        "; held out" if e.get("held_out") else ""))
        print("written %s" % os.path.relpath(COPY_FILE, SUITE))
    if not cells:
        print("no tuning cells in %s" % args.results)


if __name__ == "__main__":
    main()
