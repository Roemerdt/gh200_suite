"""Campaign report, every contrast against its floor and replicate, plus per-unit costs from the counters

usage: python3 -m analysis.report results/<campaign> [--replicate results/<replicate>]
                [--floors harness/floors.json] [--out results/<campaign>/summary/REPORT.md]
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "..", "harness"))
from analysis import stats  # noqa: E402
from analysis.floors import changes, floors_from  # noqa: E402
from analysis.load import knobs_of, load_rows, group_cells  # noqa: E402
from analysis.route import summarize_route  # noqa: E402
from analysis.stats import NAN  # noqa: E402
import grids  # noqa: E402

SUITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
# (column prefix, name in the report) per family
CONTRASTS = {"route": [("route_diff", "route difference (direct - copy)")],
             "factor": [("effect", "factor effect on direct access (level - home)")],
             "four": [("rd_home", "route difference at home"), ("rd_level", "route difference at the level"),
                      ("change", "change of the route difference")],
             "kvar": [("effect", "level - home")],
             "cross": [("effect1_home", "first factor's effect at the second's home"),
                       ("effect1_level2", "first factor's effect at the second's level"),
                       ("change", "change of the first factor's effect"), ("effect2_home", "second factor's effect at home")],
             "aa": [("effect", "A' - A")]}
GROUP_ORDER = ("route_axes", "caching", "translation",
               "coherence", "scope", "workload", "atomics")


def ms(v):
    return "%.4f" % (v / 1e6) if isinstance(v, float) and v == v else "-"


def pct(v):
    return "%+.1f %%" % (100 * v) if isinstance(v, float) and v == v else "-"


def contrast_fields(row, prefix):
    med, lo, hi = row.get(prefix + "_ns", NAN), row.get(prefix +
                                                        "_lo_ns", NAN), row.get(prefix + "_hi_ns", NAN)
    ez = row.get(prefix + "_excludes_zero", row.get("excludes_zero", False))
    if prefix == "route_diff":
        ez = row.get("excludes_zero", False)
    return med, lo, hi, bool(ez)


def normaliser(row, family):
    if family == "route":
        return row.get("copy_ns", NAN)
    if family == "four":
        return row.get("copy_home_ns", NAN)
    return row.get("home_ns", NAN)


def route_diff_at_setting(row, family):
    if family == "route":
        return row.get("route_diff_ns", NAN)
    if family == "four":
        return row.get("rd_home_ns", NAN)
    return NAN


class Report:
    def __init__(self, campaign, replicate, calibration_floors):
        self.campaign, self.replicate = campaign, replicate
        self.tables = summarize_route(campaign)
        self.rep_tables = summarize_route(replicate) if replicate else None
        self.cal_floors = calibration_floors
        self.rep_floors = floors_from(
            changes(self.tables, self.rep_tables)) if replicate else {}
        self.flagged = []  # resolvable under the calibration floor but not the replicate floor

    def floor(self, floors, family, group):
        entry = floors.get(family, {}).get(group)
        return entry["floor_ns"] if entry else NAN

    def rep_row(self, family, row):
        if not self.rep_tables:
            return None
        key = (row["cell"], row.get("variant", ""))
        for r in self.rep_tables[family]:
            if (r["cell"], r.get("variant", "")) == key:
                return r
        return None

    def resolvable(self, family, group, row, prefix):
        """(verdict text, resolvable under the calibration floor, under the replicate floor)"""
        med, lo, hi, ez = contrast_fields(row, prefix)
        if med != med:
            return "no estimate", False, False
        if not ez:
            return "interval includes zero", False, False
        cal, rep = self.floor(self.cal_floors, family, group), self.floor(
            self.rep_floors, family, group)
        under_cal = cal != cal or abs(med) > cal
        under_rep = rep != rep or abs(med) > rep
        agree = True
        rr = self.rep_row(family, row)
        if self.replicate:
            if rr is None:
                agree = False
                text = "no replicate cell"
            else:
                rmed, _, _, _ = contrast_fields(rr, prefix)
                agree = rmed == rmed and (rmed > 0) == (med > 0)
                text = "replicate agrees" if agree else "replicate disagrees (%s ms)" % ms(
                    rmed)
        else:
            text = "no replicate yet"
        if not under_cal:
            return "below the floor (%s ms); %s" % (ms(cal), text), False, False
        if self.replicate and not under_rep:
            return "above the calibration floor (%s ms) but below the replicate floor (%s ms); %s" % (ms(cal), ms(rep), text), agree, False
        if not agree:
            return text, False, False
        return "resolvable", True, under_rep

    def family_lines(self, family):
        rows = self.tables[family]
        if not rows:
            return []
        lines = []
        by_group = {}
        for r in rows:
            _, group = grids.family_group(knobs_of(r["cell"]))
            by_group.setdefault(group, []).append(r)
        for group in sorted(by_group, key=lambda g: GROUP_ORDER.index(g) if g in GROUP_ORDER else 99):
            lines += ["", "### %s, %s (calibration floor %s ms%s)" % (
                family, group, ms(self.floor(self.cal_floors, family, group)),
                (", replicate floor %s ms" % ms(self.floor(self.rep_floors, family, group))) if self.replicate else ""), "",
                "| cell | contrast | ms [interval] | route difference at the setting ms | relative to normaliser | verdict | checks |",
                "|---|---|---|---|---|---|---|"]
            for r in by_group[group]:
                label = r["cell"].split(
                    "/", 1)[1] + ((" " + r["variant"]) if r.get("variant") else "")
                for prefix, name in CONTRASTS[family]:
                    med, lo, hi, _ = contrast_fields(r, prefix)
                    if med != med:
                        continue
                    verdict, under_cal, under_rep = self.resolvable(
                        family, group, r, prefix)
                    if under_cal and not under_rep and self.replicate:
                        self.flagged.append((family, group, r["cell"], prefix))
                    rel = med / normaliser(r, family) if normaliser(r, family) == normaliser(
                        r, family) and normaliser(r, family) else NAN
                    rd = route_diff_at_setting(r, family)
                    if prefix == "change" and family == "four":
                        rel_text = pct(r.get("change_rel_rd_home", NAN)) + " of the route difference at home" if r.get(
                            "change_rel_rd_home", NAN) == r.get("change_rel_rd_home", NAN) else "- (route difference at home not resolvable)"
                    else:
                        rel_text = pct(rel)
                    lines.append("| %s | %s | %s [%s, %s] | %s | %s | %s | %s |" % (
                        label, name, ms(med), ms(lo), ms(hi), ms(rd) if prefix not in (
                            "route_diff", "rd_home") else "same", rel_text,
                        verdict, "pass" if r.get("checks_ok") else "FAIL"))
        return lines

    def per_unit_lines(self):
        """Per-unit costs from the raw rows of the factor cells of the translation group and of the route cells"""
        cells = group_cells(load_rows(self.campaign))
        lines = ["", "## Per-unit costs (P11.4)", "",
                 "Per pair: the time difference over the counter difference, median with rank interval; given only where the "
                 "counter difference excludes zero. Translation costs are per counted SMMU request, including uncounted "
                 "GPU-internal translation, within one footprint and page-order level.", "",
                 "| cell | counter | counter difference per pass [interval] | ns per unit [interval] | pairs |", "|---|---|---|---|---|"]
        found = False
        for cell_id in sorted(cells):
            cell = cells[cell_id]
            knobs = cell.knobs
            if knobs.get("type") not in ("factor",) or cell.instr != "route":
                continue
            family, group = grids.family_group(knobs)
            if group != "translation":
                continue
            pairs = cell.matched_pairs()
            for column, name in ((grids.counter_column(grids.SMMU_ATS), "SMMU translation requests"),
                                 ("ctr_c2c0_rd_bytes_loc", "link read bytes")):
                diffs, costs = [], []
                for _, a, b in pairs:
                    if not all(isinstance(r.get(column), (int, float)) and r.get("batch") for r in (a, b)):
                        continue
                    dc = b[column] / b["batch"] - a[column] / a["batch"]
                    dt = b["ns_per_op"] - a["ns_per_op"]
                    diffs.append(dc)
                    if dc:
                        costs.append(dt / dc)
                if len(diffs) < 3:
                    continue
                d = stats.diff_summary(diffs)
                if not d["excludes_zero"]:
                    lines.append("| %s | %s | %.3g [%.3g, %.3g] | - (counter difference includes zero) | %d |" % (
                        cell_id.split("/", 1)[1], name, d["median"], d["lo"], d["hi"], d["n"]))
                    found = True
                    continue
                c = stats.diff_summary(costs)
                lines.append("| %s | %s | %.3g [%.3g, %.3g] | %.1f [%.1f, %.1f] | %d |" % (
                    cell_id.split("/", 1)[1], name, d["median"], d["lo"], d["hi"], c["median"], c["lo"], c["hi"], c["n"]))
                found = True
        return lines if found else []

    def comparison_points(self):
        """K3P at 16 GiB for translation against coherence, K2 at 8 MiB for coherence against caching and scope"""
        lines = ["", "## Comparison points (P5.4)", ""]
        picks = [("K3P at 16 GiB, CPU placement: translation against coherence", lambda k: k.get("kernel") == "k3p"),
                 ("K2 at 8 MiB, CPU placement: coherence against caching and scope",
                  lambda k: k.get("kernel") == "k2" and k.get("working-set-mib") == "8" and k.get("placement", "cpu") == "cpu")]
        for title, pick in picks:
            lines += ["### %s" % title, "",
                      "| cell | family | contrast | ms [interval] | verdict |", "|---|---|---|---|---|"]
            for family in ("factor", "four", "kvar", "cross"):
                for r in self.tables[family]:
                    knobs = knobs_of(r["cell"])
                    if not pick(knobs) or knobs.get("type") != family:
                        continue
                    _, group = grids.family_group(knobs)
                    for prefix, name in CONTRASTS[family]:
                        med, lo, hi, _ = contrast_fields(r, prefix)
                        if med != med:
                            continue
                        verdict, _, _ = self.resolvable(
                            family, group, r, prefix)
                        lines.append("| %s | %s | %s | %s [%s, %s] | %s |" % (
                            r["cell"].split(
                                "/", 1)[1] + ((" " + r["variant"]) if r.get("variant") else ""), family, name,
                            ms(med), ms(lo), ms(hi), verdict))
            lines.append("")
        return lines

    def write(self, path):
        lines = ["# Route experiments: results", "",
                 "Campaign `%s`%s. Every contrast in absolute ms with its 95 %% rank interval; a contrast is resolvable when "
                 "its interval excludes zero, its size exceeds the floor of its family and mechanism group, and the replicate "
                 "agrees on the sign. Relative values are given against the cell's normaliser (the copy route's call at home "
                 "where the cell has one, else the home variant) and are never summed." % (
                     self.campaign, (", replicate `%s`" % self.replicate) if self.replicate else ", no replicate yet"), ""]
        lines += ["## Floors", "", "| family | group | calibration floor ms | n | replicate floor ms | n |",
                  "|---|---|---|---|---|---|"]
        families = sorted(set(self.cal_floors) | set(self.rep_floors))
        for family in families:
            for group in sorted(set(self.cal_floors.get(family, {})) | set(self.rep_floors.get(family, {}))):
                c, r = self.cal_floors.get(family, {}).get(
                    group, {}), self.rep_floors.get(family, {}).get(group, {})
                lines.append("| %s | %s | %s | %s | %s | %s |" % (family, group, ms(c.get("floor_ns", NAN)), c.get("n", "-"),
                                                                  ms(r.get("floor_ns", NAN)), r.get("n", "-")))
        for family in ("route", "factor", "four", "kvar", "cross", "aa"):
            body = self.family_lines(family)
            if body:
                lines += ["", "## %s cells" % family] + body
        lines += self.comparison_points()
        crossovers = os.path.join(self.campaign, "summary", "crossovers.md")
        if os.path.exists(crossovers):
            lines += ["", "## Crossovers", "",
                      "See `summary/crossovers.md`:", ""]
            lines += [l for l in open(crossovers).read().splitlines()
                      if l.startswith("|")]
        lines += self.per_unit_lines()
        if self.flagged:
            lines += ["", "## Re-examined under the replicate floor", "",
                      "Contrasts resolvable under the calibration floor but not under the larger replicate floor:", ""]
            lines += ["- %s / %s: %s (%s)" % f for f in self.flagged]
        with open(path, "w") as f:
            f.write("\n".join(lines) + "\n")
        return path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("campaign")
    parser.add_argument("--replicate", default=None)
    parser.add_argument(
        "--floors", default=os.path.join(SUITE, "harness", "floors.json"))
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    try:
        floors = json.load(open(args.floors))
    except FileNotFoundError:
        floors = {}
    report = Report(args.campaign, args.replicate, floors)
    out = args.out or os.path.join(args.campaign, "summary", "REPORT.md")
    report.write(out)
    print("written %s" % os.path.relpath(out, SUITE))


if __name__ == "__main__":
    main()
