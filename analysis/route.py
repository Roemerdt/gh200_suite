"""Per-cell summaries of the route experiments, recomputed from raw rows

usage: python3 -m analysis.route results/<campaign>
Writes summary/<type>_cells.csv and .md for each cell type the campaign has (route, factor, four_variant,
kvariant, cross, aa, carry_over, tune)
"""
import grids
from analysis.stats import NAN
from analysis.load import load_rows, group_cells, load_done_summary, write_csv, is_good
from analysis import stats
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "..", "harness"))

ROUTE_OF_VARIANT = {"A": "direct", "B": "copy"}
GPU_LINE_BYTES = 128
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
COUNTERS_PER_REP = (("c2c_rd_bytes", "ctr_c2c0_rd_bytes_loc"),
                    ("c2c_wr_bytes", "ctr_c2c0_wr_bytes_loc"),
                    ("smmu_ats_rq", grids.counter_column(grids.SMMU_ATS)))


def ran_in_drawn_order(cell, first):
    """By timestamp, every repeat ran first then the other variant, without interleaving"""
    second = "B" if first == "A" else "A"
    by_time = sorted((r["ts_epoch"], r["rep"], r["member"])
                     for r in cell.rows if r["member"] in ("A", "B"))
    reps = sorted({rep for _, rep, _ in by_time})
    return [(rep, m) for _, rep, m in by_time] == [(rep, m) for rep in reps for m in (first, second)]


def member_index(member):
    """A..Z, then v26, v27, ..."""
    return ord(member) - ord("A") if len(member) == 1 and member in LETTERS else int(member[1:])


def is_variant(member):
    return (len(member) == 1 and member in LETTERS) or (member.startswith("v") and member[1:].isdigit())


def ran_in_round_order(cell, seed, k):
    """Every round ran its k variants in the seed's order, by timestamp and by the pos column"""
    by_round = {}
    for r in cell.rows:
        if is_variant(r["member"]):
            by_round.setdefault(r["rep"], []).append(
                (r["ts_epoch"], r["member"], r.get("pos")))
    for rep, entries in by_round.items():
        entries.sort()
        drawn = [grids.variant_name(v)
                 for v in grids.round_order(seed, cell.id, rep, k)]
        if [m for _, m, _ in entries] != drawn or [p for _, _, p in entries] != list(range(k)):
            return False
    return bool(by_round)


def single_value(rows, column):
    values = {r.get(column) for r in rows}
    return values.pop() if len(values) == 1 else None


def rows_checksum_ok(rows):
    """Every row delivered the checksum its last pass had to deliver"""
    return bool(rows) and all(r["checksum"] == r["expected"] for r in rows)


def variant_summary(cell, member):
    """One variant's ns per repetition with interval, its buffer facts and counters"""
    rows = cell.member_rows(member)
    n, med, lo, hi = stats.median_ci([r["ns_per_op"] for r in rows])
    summary = dict(n=n, median_ns=med, lo_ns=lo, hi_ns=hi,
                   passes=single_value(rows, "passes"), addr=single_value(rows, "addr"),
                   off_1g=single_value(rows, "off_1g"), off_16g=single_value(rows, "off_16g"),
                   anon_huge_kb=single_value(rows, "anon_huge_kb"),
                   route=single_value(rows, "route"), placement=single_value(rows, "placement"),
                   level=single_value(rows, "level"), cursor=single_value(rows, "cursor"),
                   passes_frozen=single_value(rows, "passes_frozen"), page_size=single_value(rows, "page_size"),
                   alignment=single_value(rows, "alignment"), footprint_bytes=single_value(rows, "footprint_bytes"),
                   touched_lines=single_value(rows, "touched_lines"), gathers=single_value(rows, "gathers"),
                   copy_label=single_value(rows, "copy"),
                   shape="%sx%sx%s" % (single_value(rows, "blocks"), single_value(rows, "threads"), single_value(rows, "load")))
    # a coherence cell's host phase, CPU time per pass and the state check's load latency
    cpu = [r["cpu_ns"] / r["passes"]
           for r in rows if isinstance(r.get("cpu_ns"), (int, float)) and r.get("passes")]
    summary["cpu_ns"] = stats.median(cpu) if cpu else NAN
    state_check = single_value(rows, "state_check_ns")
    summary["state_check_ns"] = state_check if isinstance(
        state_check, (int, float)) and state_check >= 0 else NAN
    summary["host"] = single_value(rows, "host")
    summary["sharing"] = single_value(rows, "sharing")
    counted = cell.counted_rows(member)
    # accesses per repetition, gathers for a gather kernel, else touched lines
    accesses = summary["gathers"] if isinstance(
        summary["gathers"], int) else summary["touched_lines"]
    for name, column in COUNTERS_PER_REP:
        per_rep = [r[column] / r["batch"]
                   for r in counted if isinstance(r.get(column), (int, float)) and r["batch"]]
        summary[name + "_per_rep"] = stats.median(per_rep) if per_rep else NAN
        summary[name + "_per_access"] = ratio(
            summary[name + "_per_rep"], accesses) if isinstance(accesses, int) else NAN
    return summary


def expected_off_1g(variant):
    return 512 << 20 if variant.get("alignment") == "off512m" else 0


def huge_pages_ok(variant):
    """Whole input on 512 MB pages if asked for, else none"""
    kb, footprint = variant.get("anon_huge_kb"), variant.get("footprint_bytes")
    if variant.get("page_size") == "512m":
        return isinstance(kb, int) and isinstance(footprint, int) and kb * 1024 >= footprint
    return kb in (None, 0, "")


def median_of(rows, column):
    return stats.median([r[column] for r in rows]) if rows else NAN


def ratio(numerator, denominator):
    return numerator / denominator if numerator == numerator and denominator else NAN


def cell_type(cell):
    return cell.knobs.get("type", "route")


def members_of(cell):
    return sorted({r["member"] for r in cell.rows if is_variant(r["member"])}, key=member_index)


def rounds_of(cell):
    """{rep: {variant: good row}}"""
    rounds = {}
    for r in cell.rows:
        if is_good(r) and is_variant(r["member"]):
            rounds.setdefault(r["rep"], {})[r["member"]] = r
    return rounds


def contrast(rounds, terms):
    """Signed sum of variant times per round, over the rounds where every variant involved has a good row"""
    values = [sum(coefficient * rounds[rep][m]["ns_per_op"] for m, coefficient in terms)
              for rep in sorted(rounds) if all(m in rounds[rep] for m, _ in terms)]
    return stats.diff_summary(values)


def common_checks(cell, members, variants):
    rows = [r for r in cell.rows if r["member"] in members]
    good = [r for m in members for r in cell.member_rows(m)]
    return dict(checksum_ok=rows_checksum_ok(good),
                void_checksum_rows=sum(
                    1 for r in rows if r["status"] == "VOID_CHECKSUM"),
                discarded_migration_rows=sum(
                    1 for r in rows if r["status"] == "DISCARDED_MIGRATION"),
                aligned_ok=all(variants[m]["off_1g"] == expected_off_1g(
                    variants[m]) for m in members),
                huge_pages_ok=all(huge_pages_ok(variants[m]) for m in members),
                multiplexed_rows=sum(1 for r in good if r.get("ctr_multiplexed") == 1))


def checks_pass(out):
    return bool(out["checksum_ok"] and out["void_checksum_rows"] == 0 and out["order_ok"]
                and out["aligned_ok"] and out["huge_pages_ok"] and out["discarded_migration_rows"] == 0)


def stop_flags(done):
    return dict(cap_hit=done.get("cap_hit", "") == "1", stopped_on_target=done.get("stopped_on_target", "") == "1")


def counters_of(prefix, variant):
    return {prefix + "_c2c_rd_bytes_per_rep": variant["c2c_rd_bytes_per_rep"],
            prefix + "_smmu_ats_rq_per_rep": variant["smmu_ats_rq_per_rep"],
            prefix + "_c2c_rd_bytes_per_access": variant["c2c_rd_bytes_per_access"],
            prefix + "_smmu_ats_rq_per_access": variant["smmu_ats_rq_per_access"]}


def spread_of(prefix, variant):
    return {prefix + "_n": variant["n"], prefix + "_ns": variant["median_ns"],
            prefix + "_lo_ns": variant["lo_ns"], prefix + "_hi_ns": variant["hi_ns"],
            prefix + "_cpu_ns": variant["cpu_ns"], prefix + "_state_check_ns": variant["state_check_ns"]}


def has_host_phase(c):
    return c.get("host") not in (None, "", "none", "-")


def host_phase_lines(summaries, prefixes):
    """Host-phase table, CPU time per pass and state-check latency per variant"""
    with_host = [c for c in summaries if has_host_phase(c)]
    if not with_host:
        return []
    lines = ["", "## Host phases\n",
             "The CPU phase before every pass, timed on the CPU clock (ms per pass), and the state check's median load "
             "latency on the preparing core after the phase (ns per sampled load), per variant.\n",
             "| cell | " + " | ".join("%s CPU ms | %s state ns" % (
                 p.replace("_", " "), p.replace("_", " ")) for p in prefixes) + " |",
             "|---|" + "---|" * (2 * len(prefixes))]
    for c in with_host:
        cells = []
        for p in prefixes:
            v = c.get(p + "_state_check_ns", NAN)
            cells += [ms(c.get(p + "_cpu_ns", NAN)),
                      ("%.1f" % v) if v == v else "-"]
        lines.append("| %s | %s |" %
                     (c["cell"].split("/", 1)[1], " | ".join(cells)))
    return lines


def route_cell(cell):
    route_rows = [r for r in cell.rows if r["member"] in ("A", "B")]
    for member, route in ROUTE_OF_VARIANT.items():
        if {r.get("route") for r in route_rows if r["member"] == member} != {route}:
            raise ValueError("%s: variant %s is not the %s route" %
                             (cell.id, member, route))

    direct = variant_summary(cell, "A")
    copy = variant_summary(cell, "B")
    copy_rows = cell.member_rows("B")
    good_rows = cell.member_rows("A") + copy_rows
    pairs = cell.matched_pairs()
    diff = stats.paired_delta([a["ns_per_op"] for _, a, _ in pairs], [
                              b["ns_per_op"] for _, _, b in pairs])

    first = single_value(route_rows, "first")
    seed = single_value(route_rows, "seed")
    touched_lines = single_value(route_rows, "touched_lines")
    has_touched = isinstance(touched_lines, int) and touched_lines > 0
    done = load_done_summary(cell.file)

    out = dict(cell.knobs)
    out.update(
        cell=cell.id, kernel=single_value(route_rows, "kernel"), placement=single_value(route_rows, "placement"),
        footprint_bytes=single_value(route_rows, "footprint_bytes"), f_num=single_value(route_rows, "f_num"),
        f_den=single_value(route_rows, "f_den"), touched_lines=touched_lines,
        # the two variants, ns per repetition
        direct_n=direct["n"], direct_ns=direct["median_ns"], direct_lo_ns=direct["lo_ns"], direct_hi_ns=direct["hi_ns"],
        direct_passes=direct["passes"],
        copy_n=copy["n"], copy_ns=copy["median_ns"], copy_lo_ns=copy["lo_ns"], copy_hi_ns=copy["hi_ns"],
        copy_passes=copy["passes"], passes_frozen=direct["passes_frozen"],
        # route difference, direct minus copy within a repeat
        n_pairs=diff["n"], route_diff_ns=diff["median"], route_diff_lo_ns=diff["lo"], route_diff_hi_ns=diff["hi"],
        route_diff_rel_copy=(
            diff["median"] / copy["median_ns"]) if diff["n"] and copy["median_ns"] else NAN,
        excludes_zero=diff["excludes_zero"], npos=diff["npos"], nneg=diff["nneg"], sign_p=diff["sign_p"],
        # direct read rate over the touched lines (bytes per ns = GB/s)
        direct_GBps=(touched_lines * GPU_LINE_BYTES /
                     direct["median_ns"]) if has_touched and direct["n"] and direct["median_ns"] else NAN,
        # breakdown of the first copy call per interval, not summed
        copyin_ns=median_of(copy_rows, "copyin_ns"), copy_kernel_ns=median_of(copy_rows, "kernel_ns"),
        copyout_ns=median_of(copy_rows, "copyout_ns"),
        # checks
        checksum_ok=rows_checksum_ok(good_rows),
        void_checksum_rows=sum(
            1 for r in route_rows if r["status"] == "VOID_CHECKSUM"),
        discarded_migration_rows=sum(
            1 for r in route_rows if r["status"] == "DISCARDED_MIGRATION"),
        first=first, seed=seed,
        first_matches_seed=(isinstance(seed, int) and first ==
                            grids.first_variant(seed, cell.id)),
        order_ok=first in ("A", "B") and ran_in_drawn_order(cell, first),
        aligned_ok=direct["off_1g"] == expected_off_1g(
            direct) and copy["off_1g"] == expected_off_1g(copy),
        huge_pages_ok=huge_pages_ok(direct) and huge_pages_ok(copy),
        direct_addr=direct["addr"], direct_off_16g=direct["off_16g"], copy_addr=copy["addr"], copy_off_16g=copy["off_16g"],
        direct_anon_huge_kb=direct["anon_huge_kb"], copy_anon_huge_kb=copy["anon_huge_kb"],
        direct_anon_huge_kb_end=done.get("ahp_kb_end_A", ""), copy_anon_huge_kb_end=done.get("ahp_kb_end_B", ""),
        **stop_flags(done),
        # link traffic per repetition, where counters were recorded
        copy_label=copy["copy_label"], direct_shape=direct["shape"],
        direct_c2c_rd_bytes_per_rep=direct["c2c_rd_bytes_per_rep"], copy_c2c_rd_bytes_per_rep=copy["c2c_rd_bytes_per_rep"],
        direct_c2c_wr_bytes_per_rep=direct["c2c_wr_bytes_per_rep"], copy_c2c_wr_bytes_per_rep=copy["c2c_wr_bytes_per_rep"],
        direct_c2c_rd_bytes_per_touched_line=(
            direct["c2c_rd_bytes_per_rep"] / touched_lines) if has_touched else NAN,
        direct_smmu_ats_rq_per_rep=direct["smmu_ats_rq_per_rep"], copy_smmu_ats_rq_per_rep=copy["smmu_ats_rq_per_rep"],
        multiplexed_rows=sum(
            1 for r in good_rows if r.get("ctr_multiplexed") == 1),
        direct_c2c_rd_bytes_per_access=direct["c2c_rd_bytes_per_access"], direct_smmu_ats_rq_per_access=direct["smmu_ats_rq_per_access"],
        copy_smmu_ats_rq_per_access=copy["smmu_ats_rq_per_access"])
    out["checks_ok"] = checks_pass(out) and out["first_matches_seed"]
    return out


def factor_cell(cell):
    """Factor effect on direct access, level B minus home A"""
    rows = [r for r in cell.rows if r["member"] in ("A", "B")]
    variants = {m: variant_summary(cell, m) for m in "AB"}
    home, level = variants["A"], variants["B"]
    pairs = cell.matched_pairs()
    effect = stats.paired_delta([b["ns_per_op"] for _, _, b in pairs], [
                                a["ns_per_op"] for _, a, _ in pairs])
    first = single_value(rows, "first")
    seed = single_value(rows, "seed")
    done = load_done_summary(cell.file)

    out = dict(cell.knobs)
    out.update(cell=cell.id, kernel=single_value(rows, "kernel"), vary=cell.knobs.get("vary"), level=level["level"],
               home_placement=home["placement"], level_placement=level["placement"],
               footprint_bytes=single_value(rows, "footprint_bytes"))
    out.update(spread_of("home", home),
               home_passes=home["passes"], home_cursor=home["cursor"])
    out.update(spread_of("level", level), level_passes=level["passes"], level_cursor=level["cursor"],
               passes_frozen=home["passes_frozen"])
    out.update(n_pairs=effect["n"], effect_ns=effect["median"], effect_lo_ns=effect["lo"], effect_hi_ns=effect["hi"],
               effect_rel_home=ratio(
                   effect["median"], home["median_ns"]) if effect["n"] else NAN,
               excludes_zero=effect["excludes_zero"], npos=effect["npos"], nneg=effect["nneg"], sign_p=effect["sign_p"],
               first=first, seed=seed,
               first_matches_seed=(isinstance(
                   seed, int) and first == grids.first_variant(seed, cell.id)),
               order_ok=first in (
                   "A", "B") and ran_in_drawn_order(cell, first),
               home_addr=home["addr"], level_addr=level["addr"], **stop_flags(done))
    out.update(counters_of("home", home), **counters_of("level", level))
    out.update(common_checks(cell, ("A", "B"), variants))
    out["checks_ok"] = checks_pass(out) and out["first_matches_seed"]
    return out


FOUR_NAMES = {"A": "direct_home", "B": "copy_home",
              "C": "direct_level", "D": "copy_level"}


def four_variant_cell(cell):
    """Route difference at home and at the level, and its change"""
    members = tuple("ABCD")
    rows = [r for r in cell.rows if r["member"] in members]
    variants = {m: variant_summary(cell, m) for m in members}
    for m, route in (("A", "direct"), ("B", "copy"), ("C", "direct"), ("D", "copy")):
        if variants[m]["route"] != route:
            raise ValueError("%s: variant %s is not the %s route" %
                             (cell.id, m, route))
    rounds = rounds_of(cell)
    rd_home = contrast(rounds, [("A", 1), ("B", -1)])
    rd_level = contrast(rounds, [("C", 1), ("D", -1)])
    change = contrast(rounds, [("C", 1), ("D", -1), ("A", -1), ("B", 1)])
    direct_effect = contrast(rounds, [("C", 1), ("A", -1)])
    copy_effect = contrast(rounds, [("D", 1), ("B", -1)])
    seed = single_value(rows, "seed")
    done = load_done_summary(cell.file)

    out = dict(cell.knobs)
    out.update(cell=cell.id, kernel=single_value(rows, "kernel"), vary=cell.knobs.get("vary"), level=variants["C"]["level"],
               home_placement=variants["A"]["placement"], level_placement=variants["C"]["placement"],
               footprint_bytes=single_value(rows, "footprint_bytes"))
    for m in members:
        out.update(spread_of(FOUR_NAMES[m], variants[m]))
    out.update(n_rounds=change["n"],
               rd_home_ns=rd_home["median"], rd_home_lo_ns=rd_home["lo"], rd_home_hi_ns=rd_home["hi"],
               rd_home_excludes_zero=rd_home["excludes_zero"],
               rd_level_ns=rd_level["median"], rd_level_lo_ns=rd_level["lo"], rd_level_hi_ns=rd_level["hi"],
               rd_level_excludes_zero=rd_level["excludes_zero"],
               change_ns=change["median"], change_lo_ns=change["lo"], change_hi_ns=change["hi"],
               change_excludes_zero=change["excludes_zero"], change_npos=change["npos"], change_nneg=change["nneg"],
               change_sign_p=change["sign_p"],
               # relative change only where the home route difference excludes zero
               change_rel_rd_home=ratio(
                   change["median"], rd_home["median"]) if rd_home["excludes_zero"] else NAN,
               change_rel_copy_home=ratio(
                   change["median"], variants["B"]["median_ns"]),
               direct_effect_ns=direct_effect["median"], direct_effect_lo_ns=direct_effect[
                   "lo"], direct_effect_hi_ns=direct_effect["hi"],
               copy_effect_ns=copy_effect["median"], copy_effect_lo_ns=copy_effect["lo"], copy_effect_hi_ns=copy_effect["hi"],
               seed=seed, order_ok=isinstance(
                   seed, int) and ran_in_round_order(cell, seed, len(members)),
               floor_ns=single_value(rows, "floor_ns"), passes_frozen=single_value(rows, "passes_frozen"),
               **stop_flags(done))
    for m in members:
        out[FOUR_NAMES[m] + "_addr"] = variants[m]["addr"]
        out[FOUR_NAMES[m] + "_passes"] = variants[m]["passes"]
        out[FOUR_NAMES[m] + "_cursor"] = variants[m]["cursor"]
        out.update(counters_of(FOUR_NAMES[m], variants[m]))
    out.update(common_checks(cell, members, variants))
    out["checks_ok"] = checks_pass(out)
    return out


CROSS_NAMES = {"A": "home", "B": "level1", "C": "level2", "D": "both"}


def cross_cell(cell):
    """First factor's effect at each level of the second, and its change"""
    members = tuple("ABCD")
    rows = [r for r in cell.rows if r["member"] in members]
    variants = {m: variant_summary(cell, m) for m in members}
    rounds = rounds_of(cell)
    effect1_home = contrast(rounds, [("B", 1), ("A", -1)])
    effect1_level2 = contrast(rounds, [("D", 1), ("C", -1)])
    change = contrast(rounds, [("D", 1), ("C", -1), ("B", -1), ("A", 1)])
    effect2_home = contrast(rounds, [("C", 1), ("A", -1)])
    seed = single_value(rows, "seed")
    done = load_done_summary(cell.file)

    out = dict(cell.knobs)
    out.update(cell=cell.id, kernel=single_value(rows, "kernel"), vary=cell.knobs.get("vary"), vary2=cell.knobs.get("vary2"),
               level1=cell.knobs.get("at"), level2=cell.knobs.get("at2"), placement=variants["A"]["placement"],
               footprint_bytes=single_value(rows, "footprint_bytes"))
    for m in members:
        out.update(spread_of(CROSS_NAMES[m], variants[m]))
    out.update(n_rounds=change["n"],
               effect1_home_ns=effect1_home["median"], effect1_home_lo_ns=effect1_home[
                   "lo"], effect1_home_hi_ns=effect1_home["hi"],
               effect1_home_excludes_zero=effect1_home["excludes_zero"],
               effect1_level2_ns=effect1_level2["median"], effect1_level2_lo_ns=effect1_level2["lo"],
               effect1_level2_hi_ns=effect1_level2["hi"], effect1_level2_excludes_zero=effect1_level2["excludes_zero"],
               change_ns=change["median"], change_lo_ns=change["lo"], change_hi_ns=change["hi"],
               change_excludes_zero=change["excludes_zero"], change_npos=change["npos"], change_nneg=change["nneg"],
               change_sign_p=change["sign_p"],
               effect2_home_ns=effect2_home["median"], effect2_home_lo_ns=effect2_home[
                   "lo"], effect2_home_hi_ns=effect2_home["hi"],
               effect1_home_rel=ratio(
                   effect1_home["median"], variants["A"]["median_ns"]),
               seed=seed, order_ok=isinstance(
                   seed, int) and ran_in_round_order(cell, seed, len(members)),
               floor_ns=single_value(rows, "floor_ns"), passes_frozen=single_value(rows, "passes_frozen"),
               **stop_flags(done))
    for m in members:
        out[CROSS_NAMES[m] + "_addr"] = variants[m]["addr"]
        out[CROSS_NAMES[m] + "_passes"] = variants[m]["passes"]
        out[CROSS_NAMES[m] + "_anon_huge_kb"] = variants[m]["anon_huge_kb"]
        out.update(counters_of(CROSS_NAMES[m], variants[m]))
    out.update(common_checks(cell, members, variants))
    out["checks_ok"] = checks_pass(out)
    return out


def sequence_cell(cell):
    """One row per variant of a fixed-sequence cell, with its time after each predecessor
    in a pattern like AABB also the paired carry-over per repeat"""
    members = members_of(cell)
    variants = {m: variant_summary(cell, m) for m in members}
    pattern = cell.knobs.get("sequence", "")
    ordered = sorted((r["ts_epoch"], r)
                     for r in cell.rows if r["member"] in members)
    rows = [r for _, r in ordered]
    checks = common_checks(cell, members, variants)
    outs = []
    for m in members:
        after = {}
        for i in range(1, len(rows)):
            if rows[i]["member"] == m and is_good(rows[i]):
                after.setdefault(rows[i - 1]["member"], []
                                 ).append(rows[i]["ns_per_op"])
        paired = []
        if len(set(pattern)) == 2:
            other = [x for x in members if x != m][0]
            by_rep = {}
            for i in range(1, len(rows)):
                r = rows[i]
                if r["member"] == m and is_good(r):
                    by_rep.setdefault(r["rep"], {})[
                        rows[i - 1]["member"]] = r["ns_per_op"]
            paired = [d[other] - d[m]
                      for d in by_rep.values() if m in d and other in d]
        carry = stats.diff_summary(paired)
        out = dict(cell.knobs)
        out.update(cell=cell.id, kernel=single_value(rows, "kernel"), sequence=pattern, variant=m, route=variants[m]["route"],
                   level=variants[m]["level"], placement=variants[m]["placement"], footprint_bytes=variants[m]["footprint_bytes"],
                   n=variants[m]["n"], ns=variants[m]["median_ns"], lo_ns=variants[m]["lo_ns"], hi_ns=variants[m]["hi_ns"],
                   passes=variants[m]["passes"], seed=single_value(rows, "seed"), order_ok=True)
        for predecessor in ("A", "B"):
            values = after.get(predecessor, [])
            n, med, lo, hi = stats.median_ci(values)
            out.update({"after_%s_n" % predecessor: n, "after_%s_ns" % predecessor: med,
                        "after_%s_lo_ns" % predecessor: lo, "after_%s_hi_ns" % predecessor: hi})
        out.update(carry_n=carry["n"], carry_ns=carry["median"], carry_lo_ns=carry["lo"], carry_hi_ns=carry["hi"],
                   carry_excludes_zero=carry["excludes_zero"], carry_rel=ratio(carry["median"], variants[m]["median_ns"]))
        out.update(counters_of("variant", variants[m]))
        out.update(checks)
        out["checks_ok"] = checks_pass(out)
        outs.append(out)
    return outs


def tune_cell(cell):
    """One row per configuration by rank, with its paired slowdown against the fastest
    the held-out rule reads the slowdown's upper bound"""
    members = members_of(cell)
    variants = {m: variant_summary(cell, m) for m in members}
    rounds = rounds_of(cell)
    rows = [r for r in cell.rows if is_variant(r["member"])]
    seed = single_value(rows, "seed")
    done = load_done_summary(cell.file)
    ranked = sorted(members, key=lambda m: variants[m]["median_ns"] if variants[m]
                    ["median_ns"] == variants[m]["median_ns"] else float("inf"))
    fastest = ranked[0]
    tune = cell.knobs.get("tune", "direct")
    copies = {m: single_value(cell.member_rows(m), "copy")
              for m in members} if tune == "copy" else {}
    simplest = next((m for m in members if copies.get(
        m) == "ce-pageable-1-whole-none-whole"), None)
    checks = common_checks(cell, members, variants)
    order_ok = isinstance(seed, int) and ran_in_round_order(
        cell, seed, len(members))
    outs = []
    for rank, m in enumerate(ranked, 1):
        v = variants[m]
        slow = contrast(rounds, [(m, 1), (fastest, -1)])
        out = dict(cell.knobs)
        out.update(cell=cell.id, kernel=single_value(rows, "kernel"), tune=tune, variant=m, config=v["level"],
                   route=v["route"], placement=v["placement"], footprint_bytes=v["footprint_bytes"], rank=rank,
                   n=v["n"], ns=v["median_ns"], lo_ns=v["lo_ns"], hi_ns=v["hi_ns"], passes=v["passes"],
                   fastest=variants[fastest]["level"], runner_up=variants[ranked[1]]["level"] if len(
                       ranked) > 1 else "",
                   simplest=(variants[simplest]["level"] if simplest else ""),
                   vs_fastest_ns=slow["median"], vs_fastest_lo_ns=slow["lo"], vs_fastest_hi_ns=slow["hi"], n_rounds=slow["n"],
                   seed=seed, order_ok=order_ok, floor_ns=single_value(rows, "floor_ns"), **stop_flags(done))
        out.update(counters_of("variant", v))
        out.update(checks)
        out["checks_ok"] = checks_pass(out)
        outs.append(out)
    return outs


def kvariant_cell(cell):
    """One row per level, level minus home A within each round"""
    members = members_of(cell)
    rows = [r for r in cell.rows if r["member"] in members]
    variants = {m: variant_summary(cell, m) for m in members}
    rounds = rounds_of(cell)
    seed = single_value(rows, "seed")
    done = load_done_summary(cell.file)
    checks = common_checks(cell, members, variants)
    order_ok = isinstance(seed, int) and ran_in_round_order(
        cell, seed, len(members))
    home = variants["A"]

    outs = []
    for m in members[1:]:
        level = variants[m]
        effect = contrast(rounds, [(m, 1), ("A", -1)])
        out = dict(cell.knobs)
        out.update(cell=cell.id, kernel=single_value(rows, "kernel"), vary=cell.knobs.get("vary"), k=len(members),
                   variant=m, level=level["level"], home_placement=home["placement"], level_placement=level["placement"],
                   footprint_bytes=single_value(rows, "footprint_bytes"))
        out.update(spread_of("home", home), **spread_of("level", level))
        out.update(n_rounds=effect["n"], effect_ns=effect["median"], effect_lo_ns=effect["lo"], effect_hi_ns=effect["hi"],
                   effect_rel_home=ratio(
                       effect["median"], home["median_ns"]) if effect["n"] else NAN,
                   excludes_zero=effect["excludes_zero"], npos=effect["npos"], nneg=effect["nneg"], sign_p=effect["sign_p"],
                   seed=seed, order_ok=order_ok, floor_ns=single_value(
                       rows, "floor_ns"),
                   passes_frozen=single_value(rows, "passes_frozen"), home_passes=home["passes"], level_passes=level["passes"],
                   home_addr=home["addr"], level_addr=level["addr"], home_cursor=home["cursor"], level_cursor=level["cursor"],
                   **stop_flags(done))
        out.update(counters_of("home", home), **counters_of("level", level))
        out.update(checks)
        out["checks_ok"] = checks_pass(out)
        outs.append(out)
    return outs


# factors that change what the GPU translates
# under any other factor both direct variants should show the same translation rate
TRANSLATION_FACTORS = ("page-size", "page-order", "partition",
                       "index-order", "alignment", "footprint", "placement")


def flag_smmu_rates(tables):
    """Sets smmu_rate_flag on a non-translation factor cell whose direct variants differ in SMMU requests per access
    by more than the A/A' range at that footprint, the largest |B - A| there or else the smallest nonzero range"""
    ranges = {}
    for c in tables["aa"]:
        a, b = c["home_smmu_ats_rq_per_access"], c["level_smmu_ats_rq_per_access"]
        if a == a and b == b:
            ranges[c["footprint_bytes"]] = max(
                ranges.get(c["footprint_bytes"], 0.0), abs(b - a))
    fallback = min((r for r in ranges.values() if r > 0), default=NAN)
    for c in tables["factor"]:
        a, b = c["home_smmu_ats_rq_per_access"], c["level_smmu_ats_rq_per_access"]
        same_setting = c.get("vary") not in TRANSLATION_FACTORS
        c["smmu_rate_diff_per_access"] = (b - a) if a == a and b == b else NAN
        allowed = ranges.get(c["footprint_bytes"], fallback)
        c["smmu_rate_flag"] = bool(same_setting and c["smmu_rate_diff_per_access"] == c["smmu_rate_diff_per_access"]
                                   and allowed == allowed and abs(c["smmu_rate_diff_per_access"]) > allowed)


def summarize_route(results_dir):
    cells = {cell_id: cell for cell_id, cell in group_cells(
        load_rows(results_dir)).items() if cell.instr == "route"}
    by_type = {"route": [], "factor": [], "four": [], "kvar": [],
               "cross": [], "aa": [], "sequence": [], "tune": []}
    for cell_id in sorted(cells):
        kind = "sequence" if cells[cell_id].knobs.get(
            "sequence") else cell_type(cells[cell_id])
        if kind not in by_type:
            raise ValueError("%s: unknown cell type %s" % (cell_id, kind))
        by_type[kind].append(cells[cell_id])
    summary_dir = os.path.join(results_dir, "summary")
    os.makedirs(summary_dir, exist_ok=True)

    tables = dict(route=[route_cell(c) for c in by_type["route"]],
                  factor=[factor_cell(c) for c in by_type["factor"]],
                  four=[four_variant_cell(c) for c in by_type["four"]],
                  kvar=[row for c in by_type["kvar"]
                        for row in kvariant_cell(c)],
                  cross=[cross_cell(c) for c in by_type["cross"]],
                  aa=[factor_cell(c) for c in by_type["aa"]],
                  sequence=[row for c in by_type["sequence"]
                            for row in sequence_cell(c)],
                  tune=[row for c in by_type["tune"] for row in tune_cell(c)])
    flag_smmu_rates(tables)
    write_csv(os.path.join(summary_dir, "route_cells.csv"), tables["route"])
    write_md(os.path.join(summary_dir, "route_cells.md"), tables["route"])
    for kind, name, writer in (("factor", "factor_cells", write_factor_md), ("four", "four_variant_cells", write_four_md),
                               ("kvar", "kvariant_cells", write_kvar_md), ("cross",
                                                                           "cross_cells", write_cross_md),
                               ("aa", "aa_cells", write_aa_md), ("sequence",
                                                                 "carry_over_cells", write_sequence_md),
                               ("tune", "tune_cells", write_tune_md)):
        if tables[kind]:
            write_csv(os.path.join(summary_dir, name + ".csv"), tables[kind])
            writer(os.path.join(summary_dir, name + ".md"), tables[kind])
    return tables


def ms(ns):
    return "%.4f" % (ns / 1e6) if ns == ns else "-"


def percent(fraction):
    return ("%+.1f %%" % (100 * fraction)) if fraction == fraction else "-"


def interval(c, prefix):
    return "%s [%s, %s]" % (ms(c[prefix + "_ns"]), ms(c[prefix + "_lo_ns"]), ms(c[prefix + "_hi_ns"]))


def check_text(c, names=("checksum_ok", "order_ok", "first_matches_seed", "aligned_ok", "huge_pages_ok")):
    failed = [check for check in names if not c[check]]
    failed += ["%s=%d" % (count, c[count])
               for count in ("void_checksum_rows", "discarded_migration_rows") if c[count]]
    return "pass" if c["checks_ok"] else "FAILED: " + ", ".join(failed)


ROUND_CHECKS = ("checksum_ok", "order_ok", "aligned_ok", "huge_pages_ok")
FLOOR_NOTE = ("'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a "
              "repeat campaign.")


def counter_line(c, prefixes):
    """Link reads and translation requests per repetition of the named variants"""
    if c[prefixes[0] + "_c2c_rd_bytes_per_rep"] != c[prefixes[0] + "_c2c_rd_bytes_per_rep"]:
        return "- no hardware counters in this cell"
    parts = ["%s %.4g link read bytes and %.4g SMMU translation requests" % (
        p.replace("_", " "), c[p + "_c2c_rd_bytes_per_rep"], c[p + "_smmu_ats_rq_per_rep"]) for p in prefixes]
    return "- per repetition: %s; multiplexed rows voided: %d" % ("; ".join(parts), c["multiplexed_rows"])


def write_md(path, summaries):
    lines = ["# Route cells: direct route against copy route, recomputed from raw rows\n",
             "Times are per repetition in ms: one pass for the direct route, one complete call (copy-in, kernel, copy-out) "
             "for the copy route. The route difference is direct minus copy within a repeat, as median with its 95 %% rank "
             "interval; a negative value means direct access is faster. %s\n" % FLOOR_NOTE,
             "| cell | direct ms | copy ms | route difference ms [interval] | relative to copy | pairs | excludes zero | checks |",
             "|---|---|---|---|---|---|---|---|"]
    for c in summaries:
        lines.append("| %s | %s | %s | %s [%s, %s] | %s | %d | %s | %s |" % (
            c["cell"].split("/", 1)[1], ms(c["direct_ns"]
                                           ), ms(c["copy_ns"]), ms(c["route_diff_ns"]),
            ms(c["route_diff_lo_ns"]), ms(c["route_diff_hi_ns"]), percent(
                c["route_diff_rel_copy"]), c["n_pairs"],
            "yes" if c["excludes_zero"] else "no", check_text(c)))
    lines += host_phase_lines(summaries, ("direct", "copy"))
    lines += ["", "## Per cell\n"]
    for c in summaries:
        lines += ["### %s\n" % c["cell"],
                  "- first variant %s, seed %s; repeats alternated as drawn: %s" % (
                      c["first"], c["seed"], "yes" if c["order_ok"] else "NO"),
                  "- direct route: %d passes per interval, %.1f GB/s over the touched lines; buffer at %s (offset in its 16 GiB window: %s bytes)" % (
                      c["direct_passes"] or 0, c["direct_GBps"], c["direct_addr"], c["direct_off_16g"]),
                  "- copy route: %d calls per interval; first call of an interval: copy-in %s ms, kernel %s ms, copy-out %s ms; source buffer at %s" % (
                      c["copy_passes"] or 0, ms(c["copyin_ns"]), ms(c["copy_kernel_ns"]), ms(c["copyout_ns"]), c["copy_addr"]),
                  "- AnonHugePages after population (kB): direct %s, copy %s; after the series: direct %s, copy %s" % (
                      c["direct_anon_huge_kb"], c["copy_anon_huge_kb"], c["direct_anon_huge_kb_end"], c["copy_anon_huge_kb_end"])]
        if c["direct_c2c_rd_bytes_per_rep"] == c["direct_c2c_rd_bytes_per_rep"]:
            lines.append("- link read bytes per repetition: direct %.4g (%.1f per touched line), copy %.4g; "
                         "SMMU translation requests per repetition: direct %.4g, copy %.4g; multiplexed rows voided: %d" % (
                             c["direct_c2c_rd_bytes_per_rep"], c["direct_c2c_rd_bytes_per_touched_line"], c["copy_c2c_rd_bytes_per_rep"],
                             c["direct_smmu_ats_rq_per_rep"], c["copy_smmu_ats_rq_per_rep"], c["multiplexed_rows"]))
        else:
            lines.append("- no hardware counters in this cell")
        lines.append("")
    open(path, "w").write("\n".join(lines) + "\n")


def write_factor_md(path, summaries):
    lines = ["# Factor cells: the direct route at a level of one factor against its home level, recomputed from raw rows\n",
             "Times are per pass in ms. The factor effect on direct access is level minus home within a repeat, as median "
             "with its 95 %% rank interval; a positive value means the level is slower. %s\n" % FLOOR_NOTE,
             "| cell | factor | level | home ms | level ms | effect ms [interval] | relative to home | pairs | excludes zero | checks |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for c in summaries:
        lines.append("| %s | %s | %s | %s | %s | %s | %s | %d | %s | %s |" % (
            c["cell"].split("/", 1)[1], c["vary"], c["level"], ms(c["home_ns"]
                                                                  ), ms(c["level_ns"]), interval(c, "effect"),
            percent(c["effect_rel_home"]), c["n_pairs"], "yes" if c["excludes_zero"] else "no", check_text(c)))
    lines += host_phase_lines(summaries, ("home", "level"))
    lines += ["", "## Per cell\n"]
    for c in summaries:
        lines += ["### %s\n" % c["cell"],
                  "- first variant %s, seed %s; repeats alternated as drawn: %s" % (
                      c["first"], c["seed"], "yes" if c["order_ok"] else "NO"),
                  "- home: placement %s, %d passes per interval, cursor %s, buffer at %s; level: placement %s, %d passes per interval, cursor %s, buffer at %s" % (
                      c["home_placement"], c["home_passes"] or 0, c["home_cursor"], c["home_addr"],
                      c["level_placement"], c["level_passes"] or 0, c["level_cursor"], c["level_addr"]),
                  counter_line(c, ("home", "level")), ""]
    open(path, "w").write("\n".join(lines) + "\n")


def write_four_md(path, summaries):
    lines = ["# Four-variant cells: direct and copy route at home and at a level of one factor, recomputed from raw rows\n",
             "Times are per repetition in ms (one pass for the direct route, one complete call for the copy route). Each "
             "round runs the four variants once in the order the seed drew; the route difference at home (A - B) and at "
             "the level (C - D) and the change of the route difference, (C - D) - (A - B), are formed within each round "
             "and given as median with 95 %% rank interval. A negative route difference means direct access is faster; a "
             "negative change means the level moved the comparison towards direct access. The relative change is the "
             "change over the route difference at home, given only where that difference excludes zero. %s\n" % FLOOR_NOTE,
             "| cell | factor | level | direct home ms | copy home ms | direct level ms | copy level ms | route difference home ms [interval] | route difference level ms [interval] | change ms [interval] | relative change | rounds | change excludes zero | checks |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for c in summaries:
        lines.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %d | %s | %s |" % (
            c["cell"].split(
                "/", 1)[1], c["vary"], c["level"], ms(c["direct_home_ns"]), ms(c["copy_home_ns"]),
            ms(c["direct_level_ns"]), ms(c["copy_level_ns"]), interval(
                c, "rd_home"), interval(c, "rd_level"),
            interval(c, "change"), percent(
                c["change_rel_rd_home"]), c["n_rounds"],
            "yes" if c["change_excludes_zero"] else "no", check_text(c, ROUND_CHECKS)))
    lines += host_phase_lines(summaries, ("direct_home",
                              "copy_home", "direct_level", "copy_level"))
    lines += ["", "## Per cell\n"]
    for c in summaries:
        lines += ["### %s\n" % c["cell"],
                  "- seed %s; every round ran in the drawn order: %s; floor %s ms; stopped on target: %s, cap hit: %s" % (
                      c["seed"], "yes" if c["order_ok"] else "NO", ms(
                          c["floor_ns"]) if isinstance(c["floor_ns"], (int, float)) else "-",
                      "yes" if c["stopped_on_target"] else "no", "yes" if c["cap_hit"] else "no"),
                  "- home at placement %s, level at placement %s; buffers: direct home %s, copy home %s, direct level %s, copy level %s" % (
                      c["home_placement"], c["level_placement"], c["direct_home_addr"], c["copy_home_addr"],
                      c["direct_level_addr"], c["copy_level_addr"]),
                  "- factor effect within the cell: on the direct route %s ms, on the copy route %s ms; change relative to the copy call at home: %s" % (
                      interval(c, "direct_effect"), interval(c, "copy_effect"), percent(c["change_rel_copy_home"])),
                  counter_line(c, ("direct_home", "copy_home", "direct_level", "copy_level")), ""]
    open(path, "w").write("\n".join(lines) + "\n")


def write_cross_md(path, summaries):
    lines = ["# Cross cells: the direct route at home, at a level of one factor, at a level of a second factor and at both, recomputed from raw rows\n",
             "Times are per pass in ms. Each round runs the four variants once in the order the seed drew. The first factor's "
             "effect is given at the second factor's home (B - A) and at its level (D - C), with the change between them, "
             "(D - C) - (B - A), all formed within each round as median with 95 %% rank interval; a positive effect means the "
             "level is slower. %s\n" % FLOOR_NOTE,
             "| cell | factor 1 | level 1 | factor 2 | level 2 | home ms | level 1 ms | level 2 ms | both ms | effect 1 at home [interval] | effect 1 at level 2 [interval] | change [interval] | effect 2 at home [interval] | rounds | change excludes zero | checks |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for c in summaries:
        lines.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %d | %s | %s |" % (
            c["cell"].split("/", 1)[1], c["vary"], c["level1"], c["vary2"], c["level2"], ms(
                c["home_ns"]), ms(c["level1_ns"]),
            ms(c["level2_ns"]), ms(c["both_ns"]), interval(c, "effect1_home"), interval(
                c, "effect1_level2"), interval(c, "change"),
            interval(c, "effect2_home"), c["n_rounds"], "yes" if c["change_excludes_zero"] else "no", check_text(c, ROUND_CHECKS)))
    lines += ["", "## Per cell\n"]
    for c in summaries:
        lines += ["### %s\n" % c["cell"],
                  "- seed %s; every round ran in the drawn order: %s; stopped on target: %s, cap hit: %s" % (
                      c["seed"], "yes" if c["order_ok"] else "NO", "yes" if c["stopped_on_target"] else "no", "yes" if c["cap_hit"] else "no"),
                  "- buffers: home %s, level 1 %s, level 2 %s, both %s; AnonHugePages (kB): %s, %s, %s, %s" % (
                      c["home_addr"], c["level1_addr"], c["level2_addr"], c["both_addr"], c["home_anon_huge_kb"],
                      c["level1_anon_huge_kb"], c["level2_anon_huge_kb"], c["both_anon_huge_kb"]),
                  counter_line(c, ("home", "level1", "level2", "both")), ""]
    open(path, "w").write("\n".join(lines) + "\n")


def write_aa_md(path, summaries):
    lines = ["# A/A' cells: two identically prepared direct variants, recomputed from raw rows\n",
             "Times are per pass in ms. The difference B - A within a repeat is the noise between identically prepared "
             "buffers, as median with its 95 %% rank interval; its spread over the A/A' cells of a footprint is the floor "
             "for translation contrasts there. %s\n" % FLOOR_NOTE,
             "| cell | A ms | B ms | B - A ms [interval] | relative to A | pairs | excludes zero | checks |",
             "|---|---|---|---|---|---|---|---|"]
    for c in summaries:
        lines.append("| %s | %s | %s | %s | %s | %d | %s | %s |" % (
            c["cell"].split("/", 1)[1], ms(c["home_ns"]), ms(c["level_ns"]
                                                             ), interval(c, "effect"), percent(c["effect_rel_home"]),
            c["n_pairs"], "yes" if c["excludes_zero"] else "no", check_text(c)))
    lines += ["", "## Per cell\n"]
    for c in summaries:
        lines += ["### %s\n" % c["cell"],
                  "- first variant %s, seed %s; repeats alternated as drawn: %s" % (
                      c["first"], c["seed"], "yes" if c["order_ok"] else "NO"),
                  "- buffers: A at %s, B at %s" % (
                      c["home_addr"], c["level_addr"]),
                  counter_line(c, ("home", "level")), ""]
    open(path, "w").write("\n".join(lines) + "\n")


def write_sequence_md(path, summaries):
    lines = ["# Carry-over cells: two variants run in a fixed sequence, recomputed from raw rows\n",
             "Times are per repetition in ms. For each variant: its median over all its intervals, and by the variant "
             "that ran just before it. In a pattern that has a variant after itself and after the other (AABB), the "
             "carry-over is the paired difference per repeat, after the other minus after itself, as median with 95 %% "
             "rank interval; a positive value means the variant is slower after the other. %s\n" % FLOOR_NOTE,
             "| cell | sequence | variant | route | level | ms | after A ms | after B ms | carry-over ms [interval] | relative | repeats | excludes zero | checks |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for c in summaries:
        lines.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %d | %s | %s |" % (
            c["cell"].split("/", 1)[1].replace(",sequence=%s" %
                                               c["sequence"], ""), c["sequence"], c["variant"], c["route"],
            c["level"], ms(c["ns"]), ms(c["after_A_ns"]), ms(
                c["after_B_ns"]), interval(c, "carry"), percent(c["carry_rel"]),
            c["carry_n"], "yes" if c["carry_excludes_zero"] else "no", check_text(c, ("checksum_ok", "aligned_ok", "huge_pages_ok"))))
    open(path, "w").write("\n".join(lines) + "\n")


def write_tune_md(path, summaries):
    lines = ["# Tuning cells: one route in every configuration of its space, recomputed from raw rows\n",
             "Times are per repetition in ms. Each round runs every configuration once in the order the seed drew. "
             "Per cell the five fastest configurations and, for a copy space, the simplest one (copy engine, pageable "
             "memory, one stream, whole transfer); the slowdown against the fastest is paired within rounds, as median "
             "with 95 %% rank interval. %s\n" % FLOOR_NOTE]
    cells = []
    for c in summaries:
        if c["cell"] not in cells:
            cells.append(c["cell"])
    for cell in cells:
        rows = [c for c in summaries if c["cell"] == cell]
        head = rows[0]
        lines += ["## %s\n" % cell,
                  "- %d configurations, %d rounds; every round ran in the drawn order: %s; stopped on target: %s, cap hit: %s; checks %s" % (
                      len(rows), head["n_rounds"], "yes" if head["order_ok"] else "NO", "yes" if head["stopped_on_target"] else "no",
                      "yes" if head["cap_hit"] else "no", check_text(head, ROUND_CHECKS)),
                  "", "| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |", "|---|---|---|---|---|"]
        shown = [c for c in rows if c["rank"] <= 5] + \
            [c for c in rows if c["config"] == head["simplest"] and c["rank"] > 5]
        for c in shown:
            lines.append("| %d | %s | %s | [%s, %s] | %s |" % (c["rank"], c["config"], ms(c["ns"]), ms(c["lo_ns"]), ms(c["hi_ns"]),
                                                               interval(c, "vs_fastest")))
        lines.append("")
    open(path, "w").write("\n".join(lines) + "\n")


def write_kvar_md(path, summaries):
    lines = ["# k-variant cells: the direct route at several levels of one factor, recomputed from raw rows\n",
             "Times are per pass in ms. Each round runs every variant once in the order the seed drew; each level minus "
             "home is formed within a round and given as median with 95 %% rank interval; a positive value means the "
             "level is slower. %s\n" % FLOOR_NOTE,
             "| cell | factor | variant | level | home ms | level ms | effect ms [interval] | relative to home | rounds | excludes zero | checks |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    for c in summaries:
        lines.append("| %s | %s | %s | %s | %s | %s | %s | %s | %d | %s | %s |" % (
            c["cell"].split(
                "/", 1)[1], c["vary"], c["variant"], c["level"], ms(c["home_ns"]), ms(c["level_ns"]),
            interval(c, "effect"), percent(
                c["effect_rel_home"]), c["n_rounds"], "yes" if c["excludes_zero"] else "no",
            check_text(c, ROUND_CHECKS)))
    lines += ["", "## Per cell and level\n"]
    for c in summaries:
        lines += ["### %s, variant %s\n" % (c["cell"], c["variant"]),
                  "- seed %s; every round ran in the drawn order: %s; %d variants; stopped on target: %s, cap hit: %s" % (
                      c["seed"], "yes" if c["order_ok"] else "NO", c["k"], "yes" if c["stopped_on_target"] else "no",
                      "yes" if c["cap_hit"] else "no"),
                  "- home: placement %s, cursor %s, buffer at %s; level: placement %s, cursor %s, buffer at %s" % (
                      c["home_placement"], c["home_cursor"], c["home_addr"], c["level_placement"], c["level_cursor"], c["level_addr"]),
                  counter_line(c, ("home", "level")), ""]
    open(path, "w").write("\n".join(lines) + "\n")


if __name__ == "__main__":
    tables = summarize_route(sys.argv[1])
    for c in tables["route"]:
        print("%-80s direct %s ms  copy %s ms  route difference %s ms [%s, %s]  checks %s" % (
            c["cell"][:80], ms(c["direct_ns"]), ms(c["copy_ns"]), ms(
                c["route_diff_ns"]), ms(c["route_diff_lo_ns"]),
            ms(c["route_diff_hi_ns"]), "pass" if c["checks_ok"] else "FAILED"))
    for c in tables["factor"]:
        print("%-80s home %s ms  level %s ms  effect %s  checks %s" % (
            c["cell"][:80], ms(c["home_ns"]), ms(c["level_ns"]), interval(c, "effect"), "pass" if c["checks_ok"] else "FAILED"))
    for c in tables["four"]:
        print("%-80s route difference home %s  level %s  change %s  checks %s" % (
            c["cell"][:80], interval(c, "rd_home"), interval(c, "rd_level"), interval(c, "change"), "pass" if c["checks_ok"] else "FAILED"))
    for c in tables["kvar"]:
        print("%-80s %s (%s) minus home %s  checks %s" % (
            c["cell"][:80], c["variant"], c["level"], interval(c, "effect"), "pass" if c["checks_ok"] else "FAILED"))
    for c in tables["cross"]:
        print("%-80s effect 1 at home %s  at level 2 %s  change %s  checks %s" % (
            c["cell"][:80], interval(c, "effect1_home"), interval(
                c, "effect1_level2"), interval(c, "change"),
            "pass" if c["checks_ok"] else "FAILED"))
    for c in tables["aa"]:
        print("%-80s A %s ms  B %s ms  B - A %s  checks %s" % (
            c["cell"][:80], ms(c["home_ns"]), ms(c["level_ns"]), interval(c, "effect"), "pass" if c["checks_ok"] else "FAILED"))
