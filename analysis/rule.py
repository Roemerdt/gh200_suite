"""Revised resolvability rule, with floors relative to a contrast's reference time and the allocation order
corrected from the A/A' cells

Verdict letters R resolvable, z the interval includes zero, f below the floor, d the replicate disagrees or is
missing, n no estimate
"""
import math
import os
import statistics
import sys

sys.path.insert(0, os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "..", "harness"))
from analysis.floors import CONTRASTS, contrast_key, floors_from  # noqa: E402
from analysis.load import knobs_of  # noqa: E402
from analysis.route import summarize_route  # noqa: E402
from analysis.stats import NAN  # noqa: E402
import grids  # noqa: E402

# the times a contrast compares, per family and contrast
COMPARED = {"factor": {"effect": ("home_ns", "level_ns")}, "kvar": {"effect": ("home_ns", "level_ns")},
            "aa": {"effect": ("home_ns", "level_ns")},
            "four": {"rd_home": ("direct_home_ns", "copy_home_ns"), "rd_level": ("direct_level_ns", "copy_level_ns"),
                     "change": ("direct_home_ns", "copy_home_ns", "direct_level_ns", "copy_level_ns")},
            "cross": {"effect1_home": ("home_ns", "level1_ns"), "effect2_home": ("home_ns", "level2_ns"),
                      "effect1_level2": ("level2_ns", "both_ns"), "change": ("home_ns", "level1_ns", "level2_ns", "both_ns")}}


def reference(family, row, prefix):
    """Copy call for a route cell, else the longest time the contrast compares
    so a short against a long variant (32 MiB against 1 GiB window, an empty re-copy control against a 16 GiB gather)
    is not scaled by the short one"""
    if family == "route":
        return row.get("copy_ns", NAN)
    times = [row.get(c, NAN) for c in COMPARED.get(family, {}).get(prefix, ())]
    times = [t for t in times if isinstance(t, float) and t == t]
    return max(times) if times else NAN


def finite(*values):
    return all(isinstance(v, float) and v == v for v in values)


def relative_changes(tables1, tables2):
    """{(family, group): [(cell, contrast, change of contrast / reference)]} over the cells complete in both campaigns"""
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
                ref1, ref2 = reference(
                    family, r1, column[:-3]), reference(family, r2, column[:-3])
                if finite(a, b, ref1, ref2) and ref1 and ref2:
                    out.setdefault((family, group), []).append(
                        (r1["cell"], column, b / ref2 - a / ref1))
    return out


def relative_floors(tables1, tables2):
    """{family: {group: {floor, n, rule}}} with the floor as a fraction, built like the absolute floors"""
    floors = floors_from(relative_changes(tables1, tables2))
    return {family: {group: dict(floor=e["floor_ns"], n=e["n"], rule=e["rule"]) for group, e in groups.items()}
            for family, groups in floors.items()}


class AllocationBias:
    """Median relative B - A of the A/A' cells per kernel, placement and setting"""

    def __init__(self, dirs):
        groups = {}
        for d in dirs:
            for c in summarize_route(d)["aa"]:
                rel = c.get("effect_rel_home", NAN)
                if not finite(rel):
                    continue
                knobs = {k: v for k, v in knobs_of(
                    c["cell"]).items() if k not in ("replicate", "type")}
                key = tuple(sorted(knobs.items()))
                groups.setdefault(key, []).append(rel)
        self.settings = [dict(knobs=dict(key), bias=statistics.median(
            rels), n=len(rels)) for key, rels in sorted(groups.items())]

    def lookup(self, kernel, placement, knobs):
        """Nearest A/A' bias for a setting, returned with the setting it came from. K3P falls back to K3"""
        for k in (kernel, "k3") if kernel == "k3p" else (kernel,):
            candidates = [s for s in self.settings if s["knobs"].get(
                "kernel") == k and s["knobs"].get("placement", "cpu") == placement]
            if candidates:
                break
        else:
            return 0.0, "none"
        footprint = float(knobs.get(
            "footprint-mib", grids.HOME_SETTING.get(kernel, {}).get("footprint-mib", 1024)))

        def score(s):
            same_host = (s["knobs"].get("host") is not None) == (
                knobs.get("host") is not None)
            same_ws = s["knobs"].get(
                "working-set-mib") == knobs.get("working-set-mib")
            distance = abs(
                math.log(float(s["knobs"].get("footprint-mib", 1024)) / footprint))
            return (not same_host, not same_ws, distance)
        best = min(candidates, key=score)
        return best["bias"], ",".join("%s=%s" % kv for kv in sorted(best["knobs"].items()))


def later_variant_knobs(row):
    """(kernel, placement, knobs) of a cell's level variant, where the factor moves footprint, working set or placement"""
    knobs = knobs_of(row["cell"])
    vary, at = knobs.get("vary"), knobs.get("at")
    if vary == "footprint" and at:
        knobs["footprint-mib"] = at
    if vary == "working-set" and at:
        knobs["working-set-mib"] = at
    placement = row.get("level_placement") or knobs.get("placement", "cpu")
    if vary == "placement" and at:
        placement = at
    return knobs.get("kernel", ""), placement, knobs


class Rule:
    """Revised-rule verdicts for a campaign with its replicate"""

    def __init__(self, tables, rep_tables, abs_min_ns, bias):
        self.tables, self.rep_tables = tables, rep_tables
        self.floors = relative_floors(tables, rep_tables)
        self.abs_min_ns = abs_min_ns
        self.bias = bias
        self.rep_index = {family: {contrast_key(
            r, family): r for r in rows} for family, rows in rep_tables.items()}

    def floor(self, family, group):
        entry = self.floors.get(family, {}).get(group)
        return entry["floor"] if entry else NAN

    def correction_ns(self, family, row, prefix):
        """Measured minus corrected contrast
        a direct variant allocated after the control is taken to run (1 + b) times its true time
        copy variants stay uncorrected, no A/A' cell measures them"""
        if family not in ("factor", "kvar", "four", "cross"):
            return 0.0
        kernel, placement, knobs = later_variant_knobs(row)
        b, _ = self.bias.lookup(kernel, placement, knobs)

        def shift(column):
            t = row.get(column, NAN)
            return t - t / (1.0 + b) if finite(t) else 0.0
        if family in ("factor", "kvar"):
            return shift("level_ns") if prefix == "effect" else 0.0
        if family == "four":
            return shift("direct_level_ns") if prefix in ("change", "rd_level") else 0.0
        # B, C and D of a cross cell are allocated after A
        # D - C is taken to carry no net shift
        return {"effect1_home": shift("level1_ns"), "effect2_home": shift("level2_ns"), "effect1_level2": 0.0,
                "change": -shift("level1_ns")}.get(prefix, 0.0)

    def corrected(self, family, row, prefix):
        """(median, lo, hi) of a contrast in ns after the correction"""
        med, lo, hi = row.get(prefix + "_ns", NAN), row.get(prefix +
                                                            "_lo_ns", NAN), row.get(prefix + "_hi_ns", NAN)
        d = self.correction_ns(family, row, prefix)
        return (med - d if finite(med) else NAN), (lo - d if finite(lo) else NAN), (hi - d if finite(hi) else NAN)

    def corrected_change(self, row):
        """Corrected effect of a factor cell relative to its home run, as the tables give the measured change"""
        med, _, _ = self.corrected("factor", row, "effect")
        home = row.get("home_ns", NAN)
        return med / home if finite(med, home) and home else NAN

    def verdict(self, family, row, prefix, rep_row=None):
        """R, z, f, d or n"""
        _, group = grids.family_group(knobs_of(row["cell"]))
        med, lo, hi = self.corrected(family, row, prefix)
        if not finite(med):
            return "n"
        if finite(lo, hi):
            excludes_zero = lo > 0 or hi < 0
        else:
            excludes_zero = bool(
                row.get(prefix + "_excludes_zero", row.get("excludes_zero", False)))
        if not excludes_zero:
            return "z"
        ref = reference(family, row, prefix)
        floor = self.floor(family, group)
        threshold = max(floor * ref if finite(floor, ref)
                        else 0.0, self.abs_min_ns)
        if abs(med) <= threshold:
            return "f"
        if rep_row is None:
            rep_row = self.rep_index.get(family, {}).get(
                contrast_key(row, family))
        if rep_row is None:
            return "d"
        rmed, _, _ = self.corrected(family, rep_row, prefix)
        if not finite(rmed) or (rmed > 0) != (med > 0):
            return "d"
        return "R"

    def route_sign(self, cell, rep_cell):
        """+1 copy resolvably faster, -1 direct, 0 otherwise, like crossovers.resolvable"""
        v = self.verdict("route", cell, "route_diff", rep_cell)
        if v != "R":
            return 0
        return 1 if cell["route_diff_ns"] > 0 else -1


def fastest_copy_swap(sens_campaign, sens_replicate):
    """{frozen route cell id: (row with the fastest copy, its replicate row)} from the sensitivity campaigns"""
    rows1 = {c["cell"]: c for c in summarize_route(sens_campaign)["route"]}
    rows2 = {c["cell"]: c for c in summarize_route(sens_replicate)["route"]}
    out = {}
    for s in grids.sensitivity_settings():
        c = rows1.get(s["fastest_id"])
        if c is not None:
            out[s["frozen_id"]] = (c, rows2.get(s["fastest_id"]))
    return out
