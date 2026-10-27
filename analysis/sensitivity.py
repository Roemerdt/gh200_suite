"""Sensitivity phase, route verdicts with the frozen and the fastest copy under the absolute and relative floor

usage: python3 -m analysis.sensitivity results/<campaign> results/<replicate>
                [--reference results/c1 results/c2] [--floors harness/floors.json]
Writes summary/sensitivity.csv and sensitivity.md in the campaign's directory
"""
import argparse
import csv
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "..", "harness"))
from analysis.crossovers import resolvable  # noqa: E402
from analysis.floors import percentile  # noqa: E402
from analysis.load import knobs_of, write_csv  # noqa: E402
from analysis.route import ms, summarize_route  # noqa: E402
from analysis.stats import NAN  # noqa: E402
import grids  # noqa: E402

SUITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
VERDICT = {1: "copy", -1: "direct", 0: "-"}


def read_route_csv(results_dir):
    """{cell id: row} from a campaign's summary/route_cells.csv"""
    rows = {}
    with open(os.path.join(results_dir, "summary", "route_cells.csv")) as f:
        for r in csv.DictReader(f):
            for column in ("route_diff_ns", "route_diff_lo_ns", "route_diff_hi_ns", "copy_ns", "direct_ns"):
                r[column] = float(r[column]) if r.get(
                    column) not in (None, "") else NAN
            r["excludes_zero"] = r.get("excludes_zero") == "True"
            rows[r["cell"]] = r
    return rows


def relative_floor(reference1, reference2):
    """(90th percentile, n) of |rel1 - rel2| over the route-axis cells of both reference campaigns
    rel is the route difference over the copy route's time"""
    changes = []
    for cell_id, r1 in reference1.items():
        r2 = reference2.get(cell_id)
        if r2 is None or grids.family_group(knobs_of(cell_id)) != ("route", "route_axes"):
            continue
        rel1, rel2 = r1["route_diff_ns"] / \
            r1["copy_ns"], r2["route_diff_ns"] / r2["copy_ns"]
        if rel1 == rel1 and rel2 == rel2:
            changes.append(abs(rel1 - rel2))
    return percentile(changes, 0.9), len(changes)


def route_floor(floors, cell_id):
    """Absolute floor of the cell's group, else the route-axis floor (K6)"""
    _, group = grids.family_group(knobs_of(cell_id))
    route = floors.get("route", {})
    entry = route.get(group) or route.get("route_axes")
    return entry["floor_ns"]


def verdicts(c, rep, floor_abs, floor_rel, floor_aa):
    """(absolute, relative) verdict of a route cell with its replicate"""
    if c is None:
        return "?", "?"
    v_abs = resolvable(c, floor_abs, rep)
    v_rel = resolvable(c, max(floor_rel * c["copy_ns"], floor_aa), rep)
    return VERDICT[v_abs], VERDICT[v_rel]


def analyse(campaign, replicate, reference, floors):
    rows1 = {c["cell"]: c for c in summarize_route(campaign)["route"]}
    rows2 = {c["cell"]: c for c in summarize_route(replicate)["route"]}
    ref1, ref2 = read_route_csv(reference[0]), read_route_csv(reference[1])
    floor_rel, n_rel = relative_floor(ref1, ref2)
    floor_aa = floors.get("aa", {}).get("route_axes", {}).get("floor_ns", 0.0)
    out = []
    for s in grids.sensitivity_settings():
        knobs, entry, frozen_id, fastest_id = s["knobs"], s["entry"], s["frozen_id"], s["fastest_id"]
        floor_abs = route_floor(floors, frozen_id)
        row = dict(kernel=knobs["kernel"], placement=knobs["placement"], setting=s["key"],
                   frozen_copy=entry["copy"], fastest_copy=entry["fastest"], floor_abs_ns=floor_abs,
                   floor_rel=floor_rel, floor_aa_ns=floor_aa)
        for name, cell_id in (("frozen", frozen_id), ("fastest", fastest_id)):
            c, rep = rows1.get(cell_id), rows2.get(cell_id)
            row.update({
                name + "_direct_ns": c["direct_ns"] if c else NAN,
                name + "_copy_ns": c["copy_ns"] if c else NAN,
                name + "_route_diff_ns": c["route_diff_ns"] if c else NAN,
                name + "_route_diff_lo_ns": c["route_diff_lo_ns"] if c else NAN,
                name + "_route_diff_hi_ns": c["route_diff_hi_ns"] if c else NAN,
                name + "_rel_copy": c["route_diff_rel_copy"] if c else NAN,
                name + "_replicate_diff_ns": rep["route_diff_ns"] if rep else NAN,
                name + "_checks_ok": bool(c and c["checks_ok"] and rep and rep["checks_ok"]),
            })
            row[name + "_abs"], row[name +
                                    "_rel"] = verdicts(c, rep, floor_abs, floor_rel, floor_aa)
        campaign_cell, campaign_rep = ref1.get(frozen_id), ref2.get(frozen_id)
        row["campaign_abs"] = VERDICT[resolvable(
            campaign_cell, floor_abs, campaign_rep)] if campaign_cell else "?"
        row["survives_abs"] = row["frozen_abs"] == row["fastest_abs"]
        row["survives_rel"] = row["frozen_rel"] == row["fastest_rel"]
        out.append(row)
    return out, floor_rel, n_rel, floor_aa


def write_md(path, rows, floor_rel, n_rel, floor_aa):
    changed_abs = sum(1 for r in rows if not r["survives_abs"])
    changed_rel = sum(1 for r in rows if not r["survives_rel"])
    with open(path, "w") as md:
        md.write("# Route verdicts against the frozen and the fastest copy\n\n"
                 "Per setting whose simplest copy was frozen within the floor: the route difference (direct minus copy, ms, "
                 "median with its 95 %% rank interval; negative means direct access is faster) with the frozen copy and with "
                 "the fastest copy, and the verdict (the faster route, or '-' when not resolvable) under the absolute route "
                 "floor and under the relative floor (%.1f %% of the copy route, the 90th percentile over %d route-axis "
                 "contrasts of c1 against c2, at least the A/A' floor of %s ms). 'campaign' is the verdict of the frozen cell "
                 "in c1 with c2 as replicate, absolute floor.\n\n"
                 "Verdicts that change with the fastest copy: %d of %d under the absolute floor, %d of %d under the "
                 "relative floor.\n\n" % (100 * floor_rel, n_rel, ms(floor_aa), changed_abs, len(rows), changed_rel, len(rows)))
        md.write("| kernel | plac. | setting | frozen copy | route diff, frozen | fastest copy | route diff, fastest | "
                 "abs: campaign / frozen / fastest | rel: frozen / fastest |\n|---|---|---|---|---|---|---|---|---|\n")
        for r in rows:
            md.write("| %s | %s | %s | %s | %s [%s, %s] | %s | %s [%s, %s] | %s / %s / %s | %s / %s |\n" % (
                r["kernel"], r["placement"], r["setting"], r["frozen_copy"],
                ms(r["frozen_route_diff_ns"]), ms(
                    r["frozen_route_diff_lo_ns"]), ms(r["frozen_route_diff_hi_ns"]),
                r["fastest_copy"],
                ms(r["fastest_route_diff_ns"]), ms(
                    r["fastest_route_diff_lo_ns"]), ms(r["fastest_route_diff_hi_ns"]),
                r["campaign_abs"], r["frozen_abs"], r["fastest_abs"], r["frozen_rel"], r["fastest_rel"]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("campaign")
    parser.add_argument("replicate")
    parser.add_argument("--reference", nargs=2, default=[os.path.join(
        SUITE, "results", "c1"), os.path.join(SUITE, "results", "c2")])
    parser.add_argument(
        "--floors", default=os.path.join(SUITE, "harness", "floors.json"))
    args = parser.parse_args()
    floors = json.load(open(args.floors))
    rows, floor_rel, n_rel, floor_aa = analyse(
        args.campaign, args.replicate, args.reference, floors)
    summary_dir = os.path.join(args.campaign, "summary")
    os.makedirs(summary_dir, exist_ok=True)
    write_csv(os.path.join(summary_dir, "sensitivity.csv"), rows)
    write_md(os.path.join(summary_dir, "sensitivity.md"),
             rows, floor_rel, n_rel, floor_aa)
    print("relative floor %.1f %% over %d contrasts; A/A' floor %s ms" %
          (100 * floor_rel, n_rel, ms(floor_aa)))
    for r in rows:
        print("%-3s %-3s %-48s abs %s/%s/%s  rel %s/%s" % (r["kernel"], r["placement"], r["setting"], r["campaign_abs"],
                                                           r["frozen_abs"], r["fastest_abs"], r["frozen_rel"], r["fastest_rel"]))


if __name__ == "__main__":
    main()
