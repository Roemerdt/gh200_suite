"""The cells of every phase, and the seeded draws of src/common/draw.h so the analysis can recompute them"""
import hashlib
import json
import os
import shlex

MASK64 = (1 << 64) - 1


def _cid(instr, **k):
    return "%s/%s" % (instr, ",".join("%s=%s" % (a, _fmt(v)) for a, v in sorted(k.items())))


def cell_knobs(cell_id):
    return dict(pair.split("=", 1) for pair in cell_id.split("/", 1)[1].split(",") if "=" in pair)


def _fmt(v):
    if isinstance(v, float):
        return ("%.4f" % v).rstrip("0").rstrip(".")
    return str(v)


def _args(**k):
    out = []
    for a, v in k.items():
        out += ["--" + a, _fmt(v)]
    return out


def read_site_env(path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "site.env")):
    """KEY=VALUE pairs of site.env, quotes and comments removed"""
    site = {}
    for line in open(path):
        for token in shlex.split(line, comments=True):
            key, sep, value = token.partition("=")
            if sep:
                site[key] = value
    return site


SITE = read_site_env()
SMMU_PMU = SITE["SITE_SMMU_PMU"]
TUNED_COPY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tuned_copy.json")
BISECTION_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bisection.json")


def load_json(path):
    """{} when the file does not exist"""
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def counter_column(event):
    """Raw-row column of an uncore perf event, ctr_<short pmu>_<event> as in counters.h"""
    pmu, _, name = event.rstrip("/").partition("/")
    if pmu.startswith("nvidia_nvlink_"):
        short = pmu[len("nvidia_nvlink_"):pmu.find("_pmu")]
    elif pmu.startswith("nvidia_"):
        short = pmu[len("nvidia_"):pmu.find("_pmu")]
    elif pmu.startswith("smmuv3_pmcg_"):
        short = "smmu" + pmu[len("smmuv3_pmcg_"):]
    else:
        short = pmu
    return "ctr_%s_%s" % (short, name)


# translation requests at the GPU's SMMU (the analysis derives its column name from this)
SMMU_ATS = SMMU_PMU + "/pcie_ats_trans_rq/"
# the named counter sets of src/common/counters.h: route is link reads and writes in requests and bytes, and
# SMMU_ATS; writes adds the writer cores' L2 refills, write-backs and TLB refills; cpu_atomics is the SCF's
# accesses and cache traffic with the issuing cores' L2 write-backs
EV_ROUTE = "route"
EV_WRITES = "writes"
EV_CPU_ATOMICS = "cpu_atomics"


def first_variant(seed, cell_id):
    """A or B, whichever runs first in every repeat of a two-variant cell"""
    return "AB"[hashlib.sha256(("%d:%s:first" % (seed, cell_id)).encode()).digest()[0] & 1]


def cell_order(seed, cells):
    """Cells in seeded order, so a resumed job runs them in the same order"""
    return sorted(cells, key=lambda c: hashlib.sha256(("%d:%s:order" % (seed, c["id"])).encode()).digest())


def fnv1a64(text):
    h = 1469598103934665603
    for byte in text.encode():
        h = ((h ^ byte) * 1099511628211) & MASK64
    return h


def splitmix64(state):
    """(next state, draw)"""
    state = (state + 0x9E3779B97F4A7C15) & MASK64
    z = state
    z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & MASK64
    z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & MASK64
    return state, z ^ (z >> 31)


def variant_name(v):
    """A letter for the first 26 variants, v<index> beyond (tuning cells)"""
    return chr(ord("A") + v) if v < 26 else "v%d" % v


def round_order(seed, cell_id, rnd, k):
    """Order of the k variants in round rnd, as the binary draws it"""
    state = fnv1a64("%s:%d:%d" % (cell_id, seed, rnd))
    order = list(range(k))
    for i in range(k - 1, 0, -1):
        state, draw = splitmix64(state)
        j = draw % (i + 1)
        order[i], order[j] = order[j], order[i]
    return order


# mechanism group of each factor, for the floors (one per cell type and group)
FACTOR_GROUPS = {"f": "route_axes", "footprint": "route_axes", "placement": "route_axes", "k": "route_axes",
                 "sweeps": "route_axes",
                 "working-set": "caching", "rotated": "caching", "tiling": "caching", "generator": "workload",
                 "page-size": "translation", "page-order": "translation", "partition": "translation",
                 "index-order": "translation", "alignment": "translation",
                 "sharing": "coherence",
                 "scope": "scope",
                 "update": "atomics", "keys": "atomics", "strategy": "atomics", "layout": "atomics", "repeat": "atomics",
                 "issuer": "atomics"}


def family_group(knobs):
    """(cell type, mechanism group) from a cell's knobs, route and A/A' cells in route_axes"""
    family = knobs.get("type", "route")
    group = FACTOR_GROUPS.get(knobs.get("vary", ""), "route_axes")
    if knobs.get("kernel") == "k6":
        group = "atomics"
    elif knobs.get("host") and group == "route_axes":
        group = "coherence"
    return family, group


def _cell(knobs, note, est, events=None):
    if events is None:
        events = EV_CPU_ATOMICS if knobs.get("issuer") == "cpu" else (EV_WRITES if knobs.get("host") in ("writes", "state") else EV_ROUTE)
    return dict(instr="route", binary="route", id=_cid("route", **knobs), sub="run", args=_args(**knobs),
                est=est, note=note, events=events, seeded=True)


# knobs of each kernel's home route cell
# campaign.py falls back to these where a setting was not tuned itself
HOME_SETTING = {
    "k1": {"footprint-mib": "1024", "f-num": "1", "f-den": "1"},
    "k3": {"footprint-mib": "1024"},
    "k3p": {"footprint-mib": "16384"},
    "k2": {"footprint-mib": "1024", "working-set-mib": "32", "k": "16"},
    "k4": {"footprint-mib": "1024", "generator": "uniform"},
    "k5": {"footprint-mib": "512", "sweeps": "8", "tiling": "tiles"},
    "k6": {"footprint-mib": "1024", "update": "atomic"},
}
# knob a factor sets, where it differs from the factor's name
KNOB_OF_FACTOR = {"working-set": "working-set-mib"}


K1_HOME = {"kernel": "k1", "placement": "cpu", "footprint-mib": 1024, "f-num": 1, "f-den": 1}


def route_slice_cells():
    """K1 at home, f = 1 and 1/2, with the untuned copy-engine copy"""
    cells = []
    for g, G in ((1, 1), (1, 2)):
        k = {"kernel": "k1", "placement": "cpu",
             "footprint-mib": 1024, "f-num": g, "f-den": G}
        cells.append(_cell(k, "K1 route cell, f = %d/%d" % (g, G), 60))
    return cells


def cell_types_cells():
    """K1 at home in four-variant, factor and k-variant cells, plus the cursor and HBM placement"""
    return [
        _cell(dict(K1_HOME, type="four", vary="f", at="1of100"), "four-variant cell: route x f, 1/100 against 1", 150),
        _cell(dict(K1_HOME, type="factor", vary="f", at="1of100"), "factor cell: direct at f = 1/100 against 1", 90),
        _cell(dict(K1_HOME, type="kvar", vary="f", at="1of2+1of10"), "k-variant cell: direct at f = 1, 1/2 and 1/10", 150),
        _cell(dict(K1_HOME, **{"f-den": 1000}), "route cell with the cursor, f = 1/1000", 90),
        _cell(dict(K1_HOME, placement="hbm"), "route cell at HBM placement", 90),
        _cell(dict(K1_HOME, type="four", vary="placement", at="hbm"), "four-variant cell: route x placement", 150),
    ]


K3_HOME = {"kernel": "k3", "placement": "cpu", "footprint-mib": 1024}
K3_16G = dict(K3_HOME, **{"footprint-mib": 16384})
K3_8G = dict(K3_HOME, **{"footprint-mib": 8192})


def k3_cells():
    """K3 and K3P with each translation factor once"""
    return [
        _cell(K3_HOME, "K3 route cell at home (1 GiB, CPU)", 90),
        _cell(dict(K3_HOME, placement="hbm"), "K3 route cell at HBM placement", 90),
        _cell(dict(K3_16G, type="factor", vary="page-size", at="512m"), "K3 page size at 16 GiB", 150),
        _cell(dict(K3_16G, type="factor", vary="page-order", at="2m"), "K3 page order, 2 MB blocks against random, 16 GiB", 150),
        _cell(dict(K3_16G, type="factor", vary="partition", at="2g"), "K3 partitioning by 2 GiB window, 16 GiB", 150),
        _cell(dict(K3_16G, type="factor", vary="index-order", at="sorted"), "K3 sorted indices against random, 16 GiB", 150),
        _cell(dict(K3_8G, type="factor", vary="alignment", at="off512m"), "K3 start offset by 512 MiB against 1 GiB-aligned, 8 GiB", 150),
        _cell(dict(K3_16G, type="cross", vary="page-order", at="2m", vary2="page-size", at2="512m"),
              "K3 page order x page size, 16 GiB", 240),
        _cell(dict(K3_16G, type="four", vary="page-size", at="512m"), "K3 four-variant cell: route x page size, 16 GiB", 300),
        _cell(dict(K3_8G, type="aa", replicate=1), "K3 A/A' cell at 8 GiB, replicate 1", 120),
        _cell(dict(K3_8G, type="aa", replicate=2), "K3 A/A' cell at 8 GiB, replicate 2", 120),
        _cell({"kernel": "k3p", "placement": "cpu", "footprint-mib": 16384}, "K3P route cell at 16 GiB", 150),
        _cell({"kernel": "k3p", "placement": "cpu", "footprint-mib": 16384, "type": "factor", "vary": "page-size", "at": "512m"},
              "K3P page size at 16 GiB", 150),
    ]


def carry_over_cells():
    """Carry-over check on K1 and K3 cells"""
    pairs = [
        (dict(K3_16G, type="factor", vary="page-size", at="512m"), "K3 page size at 16 GiB"),
        (K3_16G, "K3 route cell at 16 GiB"),
        (dict(K3_HOME, **{"footprint-mib": 4096}), "K3 route cell at 4 GiB"),
        (K3_8G, "K3 route cell at 8 GiB"),
        (dict(K3_HOME, **{"footprint-mib": 4096}, type="factor", vary="page-size", at="512m"), "K3 page size at 4 GiB"),
        (dict(K3_8G, type="factor", vary="page-size", at="512m"), "K3 page size at 8 GiB"),
        (dict(K3_8G, **{"page-size": "512m"}), "K3 route cell at 8 GiB with 512 MB pages"),
        (dict(K1_HOME, **{"footprint-mib": 256}, placement="hbm"), "K1 route cell at HBM placement, 256 MiB"),
    ]
    cells = []
    for knobs, note in pairs:
        for sequence in ("AAAA", "AABB", "ABAB"):
            cells.append(_cell(dict(knobs, sequence=sequence), "%s, sequence %s" % (note, sequence), 150))
    return cells


FOOTPRINTS_MIB = (256, 1024, 4096, 8192, 16384, 24576, 32768)
F_LEVELS = ("1of1000", "1of100", "1of10", "1of2", "3of4", "9of10")  # besides f = 1, the home level


def _est(mib, variants=2):
    """Estimated seconds for population and about 20 repeats"""
    return int(45 + 4 * mib / 1024) * (1 if variants == 2 else 2)


def grid_k1k3_cells():
    """K1 and K3 part of the grid, also the calibration subset run twice with different seeds for the floors. HBM cells
    that do not fit the node are left to the capacity check as declared gaps"""
    grid = _Grid()
    add = grid.add
    for placement in ("cpu", "hbm"):
        k1 = dict(K1_HOME, placement=placement)
        add(k1, "K1 route cell at home, %s" % placement, _est(1024))
        for level in F_LEVELS:
            g, G = level.split("of")
            add(dict(k1, **{"f-num": int(g), "f-den": int(G)}), "K1 route cell, f = %s/%s, %s" % (g, G, placement), _est(1024))
            add(dict(k1, type="factor", vary="f", at=level), "K1 factor cell, f = %s/%s against 1, %s" % (g, G, placement), _est(1024))
        add(dict(k1, type="four", vary="f", at="1of100"), "K1 four-variant cell, route x f (1/100 against 1), %s" % placement, _est(1024, 4))
        k3 = dict(K3_HOME, placement=placement)
        for home, name in ((k1, "K1"), (k3, "K3")):
            for mib in FOOTPRINTS_MIB:
                add(dict(home, **{"footprint-mib": mib}), "%s route cell at %d MiB, %s" % (name, mib, placement), _est(mib))
                if mib != 1024:
                    add(dict(home, **{"footprint-mib": mib}, type="factor", vary="footprint", at="1024"),
                        "%s factor cell, footprint %d MiB against 1 GiB, %s" % (name, mib, placement), _est(mib))
        add(dict(k3, type="four", vary="footprint", at="16384"), "K3 four-variant cell, route x footprint (16 GiB against 1), %s" % placement, _est(16384, 4))
        for mib in (1024, 4096, 8192, 16384, 32768):
            add(dict(k3, **{"footprint-mib": mib}, type="factor", vary="page-size", at="512m"),
                "K3 page size, 512 MB against 64 KB, %d MiB, %s" % (mib, placement), _est(mib))
        for mib in (4096, 8192, 16384, 32768):
            for order in ("64k", "2m"):
                add(dict(k3, **{"footprint-mib": mib}, type="factor", vary="page-order", at=order),
                    "K3 page order, %s blocks against random, %d MiB, %s" % (order, mib, placement), _est(mib))
        for mib in (4096, 8192, 12288, 16384):
            for page_size in ("64k", "512m"):
                add(dict(k3, **{"footprint-mib": mib, "page-size": page_size}, type="factor", vary="alignment", at="off512m"),
                    "K3 alignment, offset against aligned, %d MiB, %s pages, %s" % (mib, page_size, placement), _est(mib))
        k3_16g = dict(k3, **{"footprint-mib": 16384})
        add(dict(k3_16g, **{"page-size": "512m"}), "K3 route cell at 16 GiB with 512 MB pages, %s" % placement, _est(16384))
        for order in ("64k", "2m"):
            add(dict(k3_16g, **{"page-order": order}), "K3 route cell at 16 GiB, page order %s, %s" % (order, placement), _est(16384))
        add(dict(k3_16g, type="four", vary="page-size", at="512m"), "K3 four-variant cell, route x page size, 16 GiB, %s" % placement, _est(16384, 4))
    add(dict(K1_HOME, type="four", vary="placement", at="hbm"), "K1 four-variant cell, route x placement, 1 GiB", _est(1024, 4))
    k3_16g = dict(K3_HOME, **{"footprint-mib": 16384})
    add(dict(k3_16g, **{"partition": "2g"}), "K3 route cell at 16 GiB, partitioned by 2 GiB window", _est(16384))
    add(dict(k3_16g, type="factor", vary="partition", at="2g"), "K3 partitioning by 2 GiB window against none, 16 GiB", _est(16384))
    add(dict(k3_16g, type="factor", vary="index-order", at="sorted"), "K3 sorted indices against random, 16 GiB", _est(16384))
    for order in ("64k", "2m"):
        add(dict(k3_16g, **{"page-size": "512m"}, type="factor", vary="page-order", at=order),
            "K3 page order, %s blocks against random, 16 GiB, 512 MB pages" % order, _est(16384))
    add(dict(K3_8G, alignment="off512m"), "K3 route cell at 8 GiB, start offset by 512 MiB", _est(8192))
    add(dict(k3_16g, type="four", vary="page-order", at="2m"), "K3 four-variant cell, route x page order (2 MB blocks), 16 GiB", _est(16384, 4))
    add(dict(k3_16g, type="four", vary="partition", at="2g"), "K3 four-variant cell, route x partitioning, 16 GiB", _est(16384, 4))
    add(dict(K3_8G, type="four", vary="alignment", at="off512m"), "K3 four-variant cell, route x alignment, 8 GiB", _est(8192, 4))
    add(dict(k3_16g, type="cross", vary="page-order", at="2m", vary2="page-size", at2="512m"), "K3 page order x page size, 16 GiB", _est(16384, 4))
    for mib in (8192, 16384):
        for replicate in range(1, 11):
            add(dict(K3_HOME, **{"footprint-mib": mib}, type="aa", replicate=replicate),
                "K3 A/A' cell at %d MiB, replicate %d" % (mib, replicate), _est(mib))
    return grid.list()


def k3_pageorder_all_cells():
    """K3 page order at every input size of the page-size figure, HBM up to 16 GiB (two host buffers per cell). Repeats
    the grid's sizes so every point of a line comes from one job"""
    cells = []
    for placement, sizes in (("cpu", (256, 1024, 1536, 2048, 4096, 8192, 9728, 11520, 12288, 16384, 24576, 32768)),
                             ("hbm", (256, 1024, 4096, 8192, 12288, 16384))):
        k3 = dict(K3_HOME, placement=placement)
        for mib in sizes:
            for order in ("64k", "2m"):
                cells.append(_cell(dict(k3, **{"footprint-mib": mib}, type="factor", vary="page-order", at=order),
                                   "K3 page order, %s blocks against random, %d MiB, %s" % (order, mib, placement), _est(mib)))
    return cells


def k2_window_over_l2_cells():
    """K2 with the window just over the GPU's L2 (60 MiB) and twice that"""
    g = _Grid()
    for k in (1, 2, 4, 16, 64):
        for mib in (64, 128):
            g.add(dict(K2_HOME, k=k, **{"working-set-mib": mib}), "K2 route cell, %d MiB window, k = %d, cpu" % (mib, k))
    return g.list()


def ncu_window_cells():
    """ncu on K2's direct route at every reread count, for the L2 hit rate per point"""
    cells = []
    for mib in (32, 64, 128):
        for k in (1, 2, 4, 16, 64):
            cells.append(_ncu_cell(dict(K2_HOME, k=k, **{"working-set-mib": mib}), "A", "K2 at W = %d MiB, k = %d, cpu" % (mib, k), 120))
    return cells


def k3_copy512_cells():
    """The copy route with 512 MB pages at the other input sizes. In HBM four host buffers and two device copies exceed
    the node from 12 GiB on, the two with 512 MB pages counting twice while they fill"""
    cells = []
    for placement, sizes in (("cpu", (256, 1024, 1536, 2048, 4096, 8192, 9728, 11520, 12288, 24576, 32768)),
                             ("hbm", (256, 1024, 4096, 8192))):
        k3 = dict(K3_HOME, placement=placement)
        for mib in sizes:
            cells.append(_cell(dict(k3, **{"footprint-mib": mib}, type="four", vary="page-size", at="512m"),
                               "K3 four-variant cell, route x page size, %d MiB, %s" % (mib, placement), _est(mib, 4)))
    return cells


def k3_copy512_hbm16_cells():
    """Alone, so it runs first in a fresh job. Two huge-page buffers counted twice and one device copy need 80 GiB,
    which fits a free node but not one still holding the previous cell's memory (66 GiB free)"""
    k3_16g = dict(K3_HOME, **{"footprint-mib": 16384, "page-size": "512m"}, placement="hbm")
    return [_cell(k3_16g, "K3 route cell at 16 GiB with 512 MB pages, hbm", _est(16384))]


def k3_bucketing_cells():
    """K3 bucketing at every size above one 2 GiB window, which the kernel requires. In HBM the four-variant cells stop
    at 12 GiB, as four host buffers and two device copies exceed the node at 16 GiB, but the route cell fits"""
    cells = []
    for placement, sizes in (("cpu", (4096, 8192, 9728, 11520, 12288, 24576, 32768)), ("hbm", (4096, 8192, 12288))):
        k3 = dict(K3_HOME, placement=placement)
        for mib in sizes:
            cells.append(_cell(dict(k3, **{"footprint-mib": mib}, type="four", vary="partition", at="2g"),
                               "K3 four-variant cell, route x partitioning, %d MiB, %s" % (mib, placement), _est(mib, 4)))
    cells.append(_cell(dict(K3_HOME, **{"footprint-mib": 16384, "partition": "2g"}, placement="hbm"),
                       "K3 route cell at 16 GiB, partitioned by 2 GiB window, hbm", _est(16384)))
    return cells


def k3_alignment_cells():
    """K3 alignment at the sizes of the other translation series that the grid's alignment cells leave out"""
    cells = []
    for placement, sizes in (("cpu", (256, 1024, 1536, 2048, 9728, 11520, 24576, 32768)), ("hbm", (256, 1024))):
        k3 = dict(K3_HOME, placement=placement)
        for mib in sizes:
            for page_size in ("64k", "512m"):
                cells.append(_cell(dict(k3, **{"footprint-mib": mib, "page-size": page_size}, type="factor", vary="alignment", at="off512m"),
                                   "K3 alignment, offset against aligned, %d MiB, %s pages, %s" % (mib, page_size, placement), _est(mib)))
    return cells


def coherence_axes_cells():
    """Coherence factors along the full axis of each kernel, as four-variant cells. In HBM the sizes stop where four
    host buffers and two device copies no longer fit"""
    g = _Grid()
    gather_sizes = {"cpu": (256, 1024, 1536, 2048, 4096, 8192, 9728, 11520, 12288, 16384, 24576, 32768), "hbm": (256, 1024, 4096, 8192, 12288)}
    k4_sizes = {"cpu": FOOTPRINTS_MIB, "hbm": (256, 1024, 4096, 8192)}
    for placement in ("cpu", "hbm"):
        homes = [(dict(K3_HOME, placement=placement, **{"footprint-mib": mib}), "K3 %s MiB" % _fmt(mib)) for mib in gather_sizes[placement]]
        homes += [(dict(K2_HOME, placement=placement, k=k), "K2 32 MiB k = %d" % k) for k in (1, 2, 4, 16, 64)]
        if placement == "cpu":
            homes += [(dict(K2_8M, k=k), "K2 8 MiB k = %d" % k) for k in (1, 2, 4, 16, 64)]
        homes += [(dict(K5_HOME, placement=placement, sweeps=s), "K5 %d sweeps" % s) for s in (1, 2, 4, 8, 16, 64)]
        for home, name in homes:
            g.add(_writes(home, 1, type="four", vary="sharing", at="shared"),
                  "%s four-variant cell, route x CPU writes (w = 1, basic copy), %s" % (name, placement), variants=4)
            g.add(_writes(home, 0.1, recopy="gather", type="four", vary="sharing", at="shared"),
                  "%s four-variant cell, route x CPU writes (w = 0.1, stateful re-copy gather), %s" % (name, placement), variants=4)
        state_homes = [(dict(K1_HOME, placement=placement, **{"footprint-mib": mib}), "K1 %s MiB" % _fmt(mib))
                       for mib in (0.5, 2, 8, 32, 64, 96, 128, 256, 1024)]
        if placement == "cpu":
            state_homes += [(dict(K2_8M, k=k), "K2 8 MiB k = %d" % k) for k in (1, 2, 4, 16, 64)]
        for home, name in state_homes:
            for state in STATES:
                g.add(_state(home, state, type="four", vary="sharing", at="shared"),
                      "%s four-variant cell, route x cache state %s, %s" % (name, state, placement), variants=4)
        reads_homes = [(dict(K4_HOME, placement=placement, **{"footprint-mib": mib}), "K4 %s MiB" % _fmt(mib)) for mib in k4_sizes[placement]]
        reads_homes += [(dict(K5_HOME, placement=placement, sweeps=s), "K5 %d sweeps" % s) for s in (1, 2, 4, 8, 16, 64)]
        for home, name in reads_homes:
            g.add(dict(home, host="reads", type="four", vary="sharing", at="shared"), "%s four-variant cell, route x CPU reads, %s" % (name, placement), variants=4)
    return g.list()


def caching_axes_cells():
    """Caching and fence scope along K2's reread axis"""
    g = _Grid()
    for placement in ("cpu", "hbm"):
        for k in (1, 2, 4, 16, 64):
            k2 = dict(K2_HOME, placement=placement, k=k)
            k2_8m = dict(K2_8M, placement=placement, k=k)
            g.add(dict(k2, type="four", vary="working-set", at="8"), "K2 four-variant cell, route x W (8 against 32 MiB), k = %d, %s" % (k, placement), variants=4)
            g.add(dict(k2, **{"working-set-mib": 1024}), "K2 route cell, 1 GiB window, k = %d, %s" % (k, placement))
            g.add(dict(k2_8m, type="four", vary="rotated", at="1"), "K2 four-variant cell, route x rotation, 8 MiB, k = %d, %s" % (k, placement), variants=4)
            g.add(dict(k2_8m, type="kvar", vary="scope", at="cta+gpu+sys"), "K2 k-variant cell, fence scope at 8 MiB, k = %d, %s" % (k, placement), variants=4)
            g.add(dict(k2_8m, type="four", vary="scope", at="sys"), "K2 four-variant cell, route x scope (system against none), 8 MiB, k = %d, %s" % (k, placement), variants=4)
    return g.list()


def k2_copy_probe_cells():
    """Whether K2's pageable copy of its 32 MiB window depends on the allocation, three fresh ones per reread count"""
    copies = "ce-pageable-1-whole-none-touched+ce-registered-1-whole-none-touched+kernel-pageable-1-whole-none-touched"
    return [_cell(dict(K2_HOME, k=k, type="tune", tune="copy", copies=copies, replicate=rep), "K2 copy probe, k = %d, allocation %d" % (k, rep), 200)
            for k in (1, 2, 4, 16, 64) for rep in (1, 2, 3)]


def atomics_axes_cells():
    """K6 along each of its axes"""
    g = _Grid()
    sizes = {"cpu": (16, 64, 256, 1024, 4096, 8192, 16384, 32768), "hbm": (16, 64, 256, 1024, 4096, 8192, 16384)}
    for placement in ("cpu", "hbm"):
        for mib in sizes[placement]:
            g.add(dict(K6_HOME, placement=placement, **{"footprint-mib": mib}), "K6 route cell, %s MiB table, %s" % (_fmt(mib), placement))
        for keys in (1, 16, 256, 1024, 4096, 65536, 1048576):
            base = dict(K6_CONTENDED, placement=placement, keys=keys)
            g.add(base, "K6 route cell, contended on %d entries, %s" % (keys, placement), 150)
            if keys <= 1024:  # private copies hold at most 1024 entries
                g.add(dict(base, type="kvar", vary="strategy", at="warp+private"), "K6 k-variant cell, strategies on %d entries, %s" % (keys, placement), 200)
            else:
                g.add(dict(base, type="factor", vary="strategy", at="warp"), "K6 warp aggregation against in place on %d entries, %s" % (keys, placement), 150)
        for mib in (0.0625, 1, 16, 256):
            base = dict(K6_CPU, placement=placement, **{"footprint-mib": mib})
            for update in ("plain", "stadd", "returned"):
                g.add(dict(base, type="factor", vary="update", at=update), "K6 CPU-issued %s against ldadd, %s MiB table, %s" % (update, _fmt(mib), placement), 120)
    return g.list()


def tune_direct_cells():
    """Launch shapes of K1, K3 and K3P at home and at the extremes of each axis, plus the copy route's kernel shape"""
    grid = _Grid()
    add = grid.add
    for placement in ("cpu", "hbm"):
        k1 = dict(K1_HOME, placement=placement, type="tune", tune="direct")
        k3 = dict(K3_HOME, placement=placement, type="tune", tune="direct")
        add(k1, "K1 direct shapes at home, %s" % placement, 300)
        add(dict(k1, **{"f-den": 1000}), "K1 direct shapes at f = 1/1000, %s" % placement, 300)
        add(dict(k1, **{"footprint-mib": 256}), "K1 direct shapes at 256 MiB, %s" % placement, 300)
        add(dict(k1, **{"footprint-mib": 32768 if placement == "cpu" else 16384}),
            "K1 direct shapes at the largest footprint, %s" % placement, 900)
        add(k3, "K3 direct shapes at home, %s" % placement, 300)
        add(dict(k3, **{"footprint-mib": 256}), "K3 direct shapes at 256 MiB, %s" % placement, 300)
        add(dict(k3, **{"footprint-mib": 32768 if placement == "cpu" else 16384}),
            "K3 direct shapes at the largest footprint, %s" % placement, 1500)
        add(dict(k3, **{"footprint-mib": 16384, "page-size": "512m"}), "K3 direct shapes at 16 GiB with 512 MB pages, %s" % placement, 300)
    add({"kernel": "k3p", "placement": "cpu", "footprint-mib": 16384, "type": "tune", "tune": "direct"}, "K3P direct shapes at 16 GiB", 600)
    for kernel_home, name in ((K1_HOME, "K1"), (K3_HOME, "K3")):
        add(dict(kernel_home, type="tune", tune="copy-kernel"), "%s: the copy route's kernel shapes at home" % name, 400)
    return grid.list()


def tune_copy_cells():
    """K1 and K3 copy space at every level of the route axes and footprint"""
    grid = _Grid()
    add = grid.add
    for placement in ("cpu", "hbm"):
        k1 = dict(K1_HOME, placement=placement, type="tune", tune="copy")
        add(k1, "K1 copy space at home, %s" % placement, 300)
        for level in F_LEVELS:
            g, G = level.split("of")
            add(dict(k1, **{"f-num": int(g), "f-den": int(G)}), "K1 copy space at f = %s/%s, %s" % (g, G, placement), 300)
        for mib in FOOTPRINTS_MIB:
            if mib == 1024:
                continue
            if placement == "hbm" and mib > 16384:
                continue
            add(dict(k1, **{"footprint-mib": mib}), "K1 copy space at %d MiB, %s" % (mib, placement), 300 + mib // 64)
            add(dict(K3_HOME, placement=placement, type="tune", tune="copy", **{"footprint-mib": mib}),
                "K3 copy space at %d MiB, %s" % (mib, placement), 300 + mib // 64)
        add(dict(K3_HOME, placement=placement, type="tune", tune="copy"), "K3 copy space at home, %s" % placement, 300)
    return grid.list()


def tune_heldout_cells():
    """Held-out block of the copy tuning, one cell per tuned setting not yet held out"""
    tuned = load_json(TUNED_COPY_FILE)
    cells = []
    for kernel, placements in sorted(tuned.items()):
        for placement, settings in sorted(placements.items()):
            for key, entry in sorted(settings.items()):
                if entry.get("held_out"):  # already re-measured in an earlier held-out campaign
                    continue
                knobs = dict(pair.split("=", 1) for pair in key.split(",") if "=" in pair)
                knobs.update(kernel=kernel, placement=placement, type="tune", tune="copy")
                labels = []
                for label in (entry["fastest"], entry.get("runner_up", ""), entry.get("simplest", "")):
                    if label and label not in labels:
                        labels.append(label)
                knobs["copies"] = "+".join(labels)
                cells.append(_cell(knobs, "%s held-out block at %s, %s" % (kernel.upper(), key, placement),
                                   120 + int(knobs.get("footprint-mib", 1024)) // 64))
    return cells


K2_HOME = {"kernel": "k2", "placement": "cpu", "footprint-mib": 1024, "working-set-mib": 32, "k": 16}
K2_8M = dict(K2_HOME, **{"working-set-mib": 8})
K4_HOME = {"kernel": "k4", "placement": "cpu", "footprint-mib": 1024, "generator": "uniform"}
K5_HOME = {"kernel": "k5", "placement": "cpu", "footprint-mib": 512, "sweeps": 8, "tiling": "tiles"}
K6_HOME = {"kernel": "k6", "placement": "cpu", "footprint-mib": 1024, "update": "atomic"}
K6_CONTENDED = {"kernel": "k6", "placement": "cpu", "footprint-mib": 8, "keys": 1024}  # the 8 MiB table holds 1M entries
K6_CPU = {"kernel": "k6", "placement": "cpu", "footprint-mib": 256, "update": "atomic", "issuer": "cpu"}
K3P_HOME = {"kernel": "k3p", "placement": "cpu", "footprint-mib": 16384}
W_LEVELS = (0.01, 0.1, 1)
RECOPY_FORMS = ("runs", "pitched", "gather")
STATES = ("dirty", "clean", "evicted")
PATTERNS = ("word", "line")
K_LEVELS = (1, 2, 4, 64)         # besides k = 16, the home level
SWEEP_LEVELS = (1, 2, 4, 16, 64)  # besides 8 sweeps, the home level
HBM_MAX_MIB = 16384


def _largest(placement):
    return 32768 if placement == "cpu" else HBM_MAX_MIB


class _Grid:
    """Collects cells by id, so a setting added twice is one cell"""

    def __init__(self):
        self.cells = {}

    def add(self, knobs, note, est=None, variants=2):
        if est is None:
            est = _est(float(knobs.get("footprint-mib", 1024)), variants)
        cell = _cell(knobs, note, est)
        self.cells.setdefault(cell["id"], cell)

    def list(self):
        return list(self.cells.values())


def _writes(knobs, w, pattern="word", **more):
    return dict(knobs, host="writes", w=w, pattern=pattern, **more)


def _state(knobs, state, pattern="word", **more):
    return dict(knobs, host="state", state=state, pattern=pattern, **more)


def _k6_cpu_cells(g, placement):
    """CPU-issued update kinds against the atomic add"""
    for mib in (256, 0.0625):
        base = dict(K6_CPU, placement=placement, **{"footprint-mib": mib})
        label = "256 MiB table" if mib == 256 else "64 KB page (cache resident)"
        for update in ("plain", "stadd", "returned"):
            g.add(dict(base, type="factor", vary="update", at=update),
                  "K6 CPU-issued %s against ldadd, %s, %s" % (update, label, placement), 120)
        if placement == "hbm":
            for update in ("atomic", "plain"):
                g.add(dict(base, placement="cpu", update=update, type="factor", vary="placement", at="hbm"),
                      "K6 CPU-issued %s, HBM against CPU placement, %s" % (update, label), 120)


def live_rest_cells():
    """A short check of K2, K4, K5 and K6 on the node"""
    g = _Grid()
    for placement in ("cpu", "hbm"):
        g.add(dict(K2_HOME, placement=placement), "K2 route cell at home, %s" % placement, 120)
        g.add(dict(K4_HOME, placement=placement), "K4 route cell at home, %s" % placement, 120)
        g.add(dict(K5_HOME, placement=placement), "K5 route cell at home, %s" % placement, 120)
        g.add(dict(K6_HOME, placement=placement), "K6 route cell at home, %s" % placement, 120)
    g.add(dict(K2_8M, type="kvar", vary="scope", at="cta+gpu+sys"), "K2 scope k-variant cell at 8 MiB", 200)
    g.add(dict(K2_8M, type="factor", vary="tiling", at="tiles"), "K2 tiles against none at 8 MiB", 120)
    g.add(_writes(K2_HOME, 0.1, type="factor", vary="sharing", at="shared"), "K2 CPU writes w = 0.1 against control", 200)
    g.add(_writes(K2_HOME, 0.1, sharing="shared", recopy="pitched"), "K2 CPU writes w = 0.1, stateful re-copy (pitched)", 200)
    g.add(_state(K2_8M, "evicted", type="factor", vary="sharing", at="shared"), "K2 cache state evicted at 8 MiB", 200)
    g.add(_state(dict(K1_HOME, **{"footprint-mib": 64}), "dirty", type="four", vary="sharing", at="shared"),
          "K1 cache state dirty at 64 MiB, four-variant", 300)
    g.add(dict(K4_HOME, host="reads", type="factor", vary="sharing", at="shared"), "K4 CPU reads the output", 150)
    g.add(dict(K4_HOME, generator="rmat"), "K4 route cell, R-MAT", 150)
    g.add(dict(K5_HOME, type="four", vary="tiling", at="none"), "K5 tiling x route", 300)
    g.add(_writes(K5_HOME, 1, sharing="shared", recopy="gather"), "K5 CPU writes w = 1, stateful re-copy (gather)", 200)
    g.add(dict(K6_HOME, type="four", vary="update", at="plain"), "K6 plain x route", 300)
    g.add(dict(K6_CONTENDED, type="kvar", vary="strategy", at="warp+private"), "K6 contended strategies, 1K entries", 300)
    g.add(dict(K6_CONTENDED, keys=1048576), "K6 contended route cell, 1M entries", 150)
    g.add(dict(K6_HOME, placement="hbm", **{"footprint-mib": 16}), "K6 L2-resident table at HBM", 120)
    _k6_cpu_cells(g, "cpu")
    for home, name in ((K2_HOME, "K2"), (K4_HOME, "K4"), (K5_HOME, "K5"), (K6_HOME, "K6")):
        g.add(dict(home, type="tune", tune="copy"), "%s copy space at home" % name, 400)
    g.add(dict(K2_HOME, type="tune", tune="direct"), "K2 direct shapes at home", 150)
    return g.list()


def tune_direct2_cells():
    """Launch shapes of K2, K4, K5 and K6 at home and at the extremes of each axis, plus the copy route's kernel shape"""
    g = _Grid()
    for placement in ("cpu", "hbm"):
        k2 = dict(K2_HOME, placement=placement, type="tune", tune="direct")
        g.add(k2, "K2 direct shapes at home, %s" % placement, 200)
        for k in (1, 64):
            g.add(dict(k2, k=k), "K2 direct shapes at k = %d, %s" % (k, placement), 200)
        for mib in (8, 1024):
            g.add(dict(k2, **{"working-set-mib": mib}), "K2 direct shapes at W = %d MiB, %s" % (mib, placement), 200)
        g.add(dict(k2, **{"working-set-mib": 8}, rotated=1), "K2 direct shapes, rotated 8 MiB, %s" % placement, 200)
        k4 = dict(K4_HOME, placement=placement, type="tune", tune="direct")
        g.add(k4, "K4 direct shapes at home, %s" % placement, 400)
        g.add(dict(k4, **{"footprint-mib": 256}), "K4 direct shapes at 256 MiB, %s" % placement, 300)
        g.add(dict(k4, **{"footprint-mib": _largest(placement)}), "K4 direct shapes at the largest footprint, %s" % placement, 1500)
        g.add(dict(k4, generator="rmat"), "K4 direct shapes, R-MAT, %s" % placement, 400)
        k5 = dict(K5_HOME, placement=placement, type="tune", tune="direct", tiling="none")
        g.add(k5, "K5 direct shapes, untiled, at home, %s" % placement, 400)
        for sweeps in (1, 64):
            g.add(dict(k5, sweeps=sweeps), "K5 direct shapes, untiled, %d sweeps, %s" % (sweeps, placement), 400 if sweeps == 1 else 1200)
        k6 = dict(K6_HOME, placement=placement, type="tune", tune="direct")
        g.add(k6, "K6 direct shapes at home, %s" % placement, 400)
        for update in ("plain", "returned"):
            g.add(dict(k6, update=update), "K6 direct shapes, %s update, %s" % (update, placement), 400)
        g.add(dict(k6, layout="line"), "K6 direct shapes, one line per thread, %s" % placement, 400)
        for mib in (256, 4096):
            g.add(dict(k6, **{"footprint-mib": mib}), "K6 direct shapes at %d MiB, %s" % (mib, placement), 400)
        if placement == "hbm":
            g.add(dict(k6, **{"footprint-mib": 16}), "K6 direct shapes, L2-resident table, hbm", 300)
        k6c = dict(K6_CONTENDED, placement=placement, type="tune", tune="direct")
        for keys in (1, 1024, 1048576):
            g.add(dict(k6c, keys=keys), "K6 direct shapes, %d entries, atomic in place, %s" % (keys, placement), 600)
            g.add(dict(k6c, keys=keys, strategy="warp"), "K6 direct shapes, %d entries, warp-aggregated, %s" % (keys, placement), 600)
    for home, name in ((K2_HOME, "K2"), (K4_HOME, "K4"), (K6_HOME, "K6")):
        g.add(dict(home, type="tune", tune="copy-kernel"), "%s: the copy route's kernel shapes at home" % name, 400)
    g.add(dict(K5_HOME, tiling="none", type="tune", tune="copy-kernel"), "K5: the copy route's kernel shapes, untiled, at home", 400)
    return g.list()


def tune_copy2_cells():
    """K2, K4, K5 and K6 copy space at every level of the route axes and footprint"""
    g = _Grid()
    for placement in ("cpu", "hbm"):
        k2 = dict(K2_HOME, placement=placement, type="tune", tune="copy")
        g.add(k2, "K2 copy space at home, %s" % placement, 300)
        for k in K_LEVELS:
            g.add(dict(k2, k=k), "K2 copy space at k = %d, %s" % (k, placement), 300)
        for mib in (8, 1024):
            g.add(dict(k2, **{"working-set-mib": mib}), "K2 copy space at W = %d MiB, %s" % (mib, placement), 300)
        g.add(dict(k2, **{"working-set-mib": 8}, rotated=1), "K2 copy space, rotated 8 MiB, %s" % placement, 300)
        k4 = dict(K4_HOME, placement=placement, type="tune", tune="copy")
        g.add(k4, "K4 copy space at home, %s" % placement, 400)
        for mib in FOOTPRINTS_MIB:
            if mib != 1024 and mib <= _largest(placement):
                g.add(dict(k4, **{"footprint-mib": mib}), "K4 copy space at %d MiB, %s" % (mib, placement), 400 + mib // 32)
        for mib in (1024, 8192):
            g.add(dict(k4, generator="rmat", **{"footprint-mib": mib}), "K4 copy space, R-MAT, %d MiB, %s" % (mib, placement), 400 + mib // 32)
        k5 = dict(K5_HOME, placement=placement, type="tune", tune="copy")
        g.add(k5, "K5 copy space at home, %s" % placement, 400)
        for sweeps in SWEEP_LEVELS:
            g.add(dict(k5, sweeps=sweeps), "K5 copy space at %d sweeps, %s" % (sweeps, placement), 400 + 10 * sweeps)
        g.add(dict(k5, tiling="none"), "K5 copy space, untiled, %s" % placement, 400)
        k6 = dict(K6_HOME, placement=placement, type="tune", tune="copy")
        g.add(k6, "K6 copy space at home, %s" % placement, 400)
        for mib in (256, 4096):
            g.add(dict(k6, **{"footprint-mib": mib}), "K6 copy space at %d MiB, %s" % (mib, placement), 400 + mib // 32)
        if placement == "hbm":
            g.add(dict(k6, **{"footprint-mib": 16}), "K6 copy space, L2-resident table, hbm", 300)
        for keys in (1, 1024, 1048576):
            g.add(dict(K6_CONTENDED, placement=placement, type="tune", tune="copy", keys=keys),
                  "K6 copy space, contended table, %d entries, %s" % (keys, placement), 400)
    return g.list()


def _rest_grid(calibration_only):
    """The grid besides the K1 and K3 rows. calibration_only keeps the contrast cells of the groups with no floor yet"""
    g = _Grid()
    for placement in ("cpu", "hbm"):
        cpu = placement == "cpu"
        # K2
        k2 = dict(K2_HOME, placement=placement)
        k2_8m = dict(K2_8M, placement=placement)
        g.add(k2, "K2 route cell at home, %s" % placement)
        for k in K_LEVELS:
            g.add(dict(k2, k=k), "K2 route cell at k = %d, %s" % (k, placement))
            g.add(dict(k2, type="factor", vary="k", at=k), "K2 factor cell, k = %d against 16, %s" % (k, placement))
        g.add(dict(k2, type="four", vary="k", at="1"), "K2 four-variant cell, route x k (1 against 16), %s" % placement, variants=4)
        for mib in (8, 1024):
            g.add(dict(k2, **{"working-set-mib": mib}), "K2 route cell at W = %d MiB, %s" % (mib, placement))
            g.add(dict(k2, type="factor", vary="working-set", at=mib), "K2 factor cell, W = %d MiB against 32, %s" % (mib, placement))
        g.add(dict(k2, type="four", vary="working-set", at="8"), "K2 four-variant cell, route x W (8 against 32 MiB), %s" % placement, variants=4)
        g.add(dict(k2_8m, rotated=1), "K2 route cell, rotated 8 MiB, %s" % placement)
        g.add(dict(k2_8m, type="factor", vary="rotated", at="1"), "K2 factor cell, rotated against fixed slices, 8 MiB, %s" % placement)
        if cpu:
            g.add(dict(k2_8m, type="four", vary="rotated", at="1"), "K2 four-variant cell, route x rotation, 8 MiB, cpu", variants=4)
        g.add(dict(k2_8m, tiling="tiles"), "K2 route cell, slices staged in shared memory, 8 MiB, %s" % placement)
        g.add(dict(k2_8m, type="factor", vary="tiling", at="tiles"), "K2 factor cell, shared-memory tiles against none, 8 MiB, %s" % placement)
        g.add(dict(k2_8m, type="kvar", vary="scope", at="cta+gpu+sys"), "K2 k-variant cell, fence scope at 8 MiB, %s" % placement, variants=4)
        g.add(dict(k2_8m, scope="sys"), "K2 route cell, system-scope fence, 8 MiB, %s" % placement)
        if cpu:
            g.add(dict(k2_8m, type="four", vary="scope", at="sys"), "K2 four-variant cell, route x scope (system against none), 8 MiB, cpu", variants=4)
        # CPU writes before each pass
        writes_homes = [(k2, "K2 32 MiB"), (dict(K5_HOME, placement=placement), "K5 home")]
        writes_homes.append((dict(K3_HOME, placement=placement, **{"footprint-mib": 16384 if cpu else 8192}), "K3 %s" % ("16 GiB" if cpu else "8 GiB")))
        if cpu:
            writes_homes += [(k2_8m, "K2 8 MiB"), (dict(K3_HOME, placement="cpu"), "K3 1 GiB")]
        for home, name in writes_homes:
            for w in W_LEVELS:
                for pattern in PATTERNS:
                    g.add(_writes(home, w, pattern, type="factor", vary="sharing", at="shared"),
                          "%s CPU writes w = %g (%s pattern) against matched control, %s" % (name, w, pattern, placement))
                g.add(_writes(home, w, sharing="shared"), "%s route cell under CPU writes w = %g, basic copy, %s" % (name, w, placement))
                # per-run copy-engine calls only where the written set is one run (w = 1)
                for form in (RECOPY_FORMS if w == 1 else RECOPY_FORMS[1:]):
                    g.add(_writes(home, w, sharing="shared", recopy=form), "%s route cell under CPU writes w = %g, stateful re-copy (%s), %s" % (name, w, form, placement))
            if "1 GiB" in name:
                continue
            g.add(_writes(home, 1, type="four", vary="sharing", at="shared"), "%s four-variant cell, route x CPU writes (w = 1, basic copy), %s" % (name, placement), variants=4)
            for form in ("pitched", "gather"):
                g.add(_writes(home, 0.1, recopy=form, type="four", vary="sharing", at="shared"),
                      "%s four-variant cell, route x CPU writes (w = 0.1, stateful re-copy %s), %s" % (name, form, placement), variants=4)
        # CPU cache state before each pass
        state_homes = [(dict(K1_HOME, placement=placement, **{"footprint-mib": mib}), "K1 %s MiB" % _fmt(mib))
                       for mib in ((0.5, 64) if cpu else (8, 64, 96))]
        if cpu:
            state_homes.append((k2_8m, "K2 8 MiB"))
        for home, name in state_homes:
            for state in STATES:
                for pattern in PATTERNS:
                    g.add(_state(home, state, pattern, type="factor", vary="sharing", at="shared"),
                          "%s cache state %s (%s pattern) against matched control, %s" % (name, state, pattern, placement))
            if "64" in name or "K2" in name:
                for state in STATES:
                    g.add(_state(home, state, sharing="shared"), "%s route cell, cache state %s, %s" % (name, state, placement))
                for state in (("dirty", "clean") if "64" in name else ("dirty",)):
                    g.add(_state(home, state, type="four", vary="sharing", at="shared"),
                          "%s four-variant cell, route x cache state %s, %s" % (name, state, placement), variants=4)
        # K4, then CPU reads of the K4 and K5 output
        k4 = dict(K4_HOME, placement=placement)
        for mib in FOOTPRINTS_MIB:
            if mib > _largest(placement):
                continue
            g.add(dict(k4, **{"footprint-mib": mib}), "K4 route cell at %d MiB, %s" % (mib, placement))
            if mib != 1024:
                g.add(dict(k4, **{"footprint-mib": mib}, type="factor", vary="footprint", at="1024"),
                      "K4 factor cell, footprint %d MiB against 1 GiB, %s" % (mib, placement))
        for mib in (1024, 8192):
            g.add(dict(k4, generator="rmat", **{"footprint-mib": mib}), "K4 route cell, R-MAT, %d MiB, %s" % (mib, placement))
            g.add(dict(k4, **{"footprint-mib": mib}, type="factor", vary="generator", at="rmat"), "K4 factor cell, R-MAT against uniform, %d MiB, %s" % (mib, placement))
        g.add(dict(k4, type="four", vary="generator", at="rmat"), "K4 four-variant cell, route x generator, 1 GiB, %s" % placement, variants=4)
        for home, name in ((k4, "K4"), (dict(K5_HOME, placement=placement), "K5")):
            g.add(dict(home, host="reads", type="factor", vary="sharing", at="shared"), "%s CPU reads the output against matched control, %s" % (name, placement))
            g.add(dict(home, host="reads", sharing="shared"), "%s route cell, the CPU reads the output after each pass, %s" % (name, placement))
            g.add(dict(home, host="reads", type="four", vary="sharing", at="shared"), "%s four-variant cell, route x CPU reads, %s" % (name, placement), variants=4)
        # K5
        k5 = dict(K5_HOME, placement=placement)
        g.add(k5, "K5 route cell at home, %s" % placement)
        for sweeps in SWEEP_LEVELS:
            g.add(dict(k5, sweeps=sweeps), "K5 route cell at %d sweeps, %s" % (sweeps, placement))
            g.add(dict(k5, type="factor", vary="sweeps", at=sweeps), "K5 factor cell, %d sweeps against 8, %s" % (sweeps, placement))
        g.add(dict(k5, type="four", vary="sweeps", at="1"), "K5 four-variant cell, route x sweeps (1 against 8), %s" % placement, variants=4)
        g.add(dict(k5, tiling="none"), "K5 route cell, untiled, %s" % placement)
        g.add(dict(k5, type="factor", vary="tiling", at="none"), "K5 factor cell, untiled against tiles, %s" % placement)
        g.add(dict(k5, type="four", vary="tiling", at="none"), "K5 four-variant cell, route x tiling, %s" % placement, variants=4)
        # K6
        k6 = dict(K6_HOME, placement=placement)
        g.add(k6, "K6 route cell at home (atomic add, 1 GiB table), %s" % placement)
        for update in ("plain", "returned"):
            g.add(dict(k6, update=update), "K6 route cell, %s update, %s" % (update, placement))
            g.add(dict(k6, type="factor", vary="update", at=update), "K6 factor cell, %s against atomic, %s" % (update, placement))
        g.add(dict(k6, layout="line"), "K6 route cell, one line per thread, %s" % placement)
        g.add(dict(k6, type="factor", vary="layout", at="line"), "K6 factor cell, one line per thread against consecutive slots, %s" % placement)
        g.add(dict(k6, type="factor", vary="repeat", at="4"), "K6 factor cell, 4 dependent updates per slot against 1, %s" % placement)
        for mib in (256, 4096):
            g.add(dict(k6, **{"footprint-mib": mib}), "K6 route cell, %d MiB table, %s" % (mib, placement))
            g.add(dict(k6, **{"footprint-mib": mib}, type="factor", vary="footprint", at="1024"), "K6 factor cell, %d MiB table against 1 GiB, %s" % (mib, placement))
        if not cpu:
            g.add(dict(k6, **{"footprint-mib": 16}), "K6 route cell, L2-resident 16 MiB table, hbm")
            g.add(dict(k6, **{"footprint-mib": 16}, type="factor", vary="footprint", at="1024"), "K6 factor cell, L2-resident table against 1 GiB, hbm")
            for update in ("plain", "returned"):
                g.add(dict(k6, **{"footprint-mib": 16}, type="factor", vary="update", at=update), "K6 factor cell, %s against atomic, L2-resident table, hbm" % update)
        if cpu:
            g.add(dict(k6, type="four", vary="update", at="plain"), "K6 four-variant cell, route x update (plain against atomic), cpu", variants=4)
        k6c = dict(K6_CONTENDED, placement=placement)
        for keys in (1, 1024, 1048576):
            g.add(dict(k6c, keys=keys), "K6 route cell, contended table of %d entries, atomic in place, %s" % (keys, placement), 150)
            if keys <= 1024:  # privatisation needs a table that fits in shared memory
                g.add(dict(k6c, keys=keys, type="kvar", vary="strategy", at="warp+private"),
                      "K6 k-variant cell, coordination strategies on %d entries, %s" % (keys, placement), 300, variants=4)
            else:
                g.add(dict(k6c, keys=keys, type="factor", vary="strategy", at="warp"),
                      "K6 factor cell, warp aggregation against atomics in place on %d entries, %s" % (keys, placement), 300)
            if keys != 1024:
                g.add(dict(k6c, keys=keys, type="factor", vary="keys", at="1024"), "K6 factor cell, %d entries against 1K, %s" % (keys, placement), 200)
        _k6_cpu_cells(g, placement)
    # K3P at 16 GiB, CPU placement only
    g.add(K3P_HOME, "K3P route cell at 16 GiB")
    g.add(dict(K3P_HOME, **{"page-size": "512m"}), "K3P route cell at 16 GiB with 512 MB pages")
    g.add(dict(K3P_HOME, type="factor", vary="page-size", at="512m"), "K3P page size, 512 MB against 64 KB, 16 GiB")
    g.add(dict(K3P_HOME, type="four", vary="page-size", at="512m"), "K3P four-variant cell, route x page size, 16 GiB", variants=4)
    for pattern in PATTERNS:
        g.add(_state(K3P_HOME, "dirty", pattern, type="factor", vary="sharing", at="shared"),
              "K3P cache state dirty on the target lines (%s pattern) against matched control, 16 GiB" % pattern)
    g.add(_state(K3P_HOME, "dirty", sharing="shared"), "K3P route cell, target lines dirty, 16 GiB")
    g.add(_state(K3P_HOME, "dirty", type="four", vary="sharing", at="shared"), "K3P four-variant cell, route x cache state dirty, 16 GiB", variants=4)
    g.add(_state(K3P_HOME, "dirty", type="cross", vary="sharing", at="shared", vary2="page-size", at2="512m"),
          "K3P cache state dirty x page size, 16 GiB", variants=4)
    cells = g.list()
    if calibration_only:
        cells = [c for c in cells if c["id"].split("/", 1)[1].find("type=route") < 0 and
                 family_group(cell_knobs(c["id"]))[0] != "route" and
                 family_group(cell_knobs(c["id"]))[1] in ("caching", "coherence", "scope", "workload", "atomics")]
    return cells


# ncu cells, one untimed pass of one variant under Nsight Compute
# their rows are not timings, so they get a campaign of their own (results/ncu*)

NCU_METRICS = ",".join([
    "gpu__time_duration.sum",
    "launch__shared_mem_config_size",
    "l1tex__t_requests_pipe_lsu_mem_global_op_ld.sum",
    "l1tex__t_sectors_pipe_lsu_mem_global_op_ld.sum",
    "l1tex__t_sector_hit_rate.pct",
    "lts__t_sectors_srcunit_tex_op_read.sum",
    "lts__t_sectors_srcunit_tex_op_read_lookup_hit.sum",
    "dram__sectors_read.sum",
    "dram__sectors_write.sum",
    "lts__t_sectors_op_red.sum",
    "lts__t_sectors_op_atom.sum",
    "lts__t_sectors_aperture_sysmem_op_red.sum",
    "lts__t_sectors_aperture_device_op_red.sum",
    "lts__t_sectors_aperture_sysmem_op_atom.sum",
    "lts__t_sectors_aperture_device_op_atom.sum",
    "lts__t_sectors_aperture_sysmem_op_read.sum",
    "lts__t_sectors_aperture_sysmem_op_write.sum",
])
# kernel of one pass as ncu's function name base, without template arguments
NCU_KERNEL_REGEX = {"k1": "k1_stream_kernel", "k2": "k2_reuse_kernel", "k3": "k3_gather_kernel",
                    "k3p": "k3p_kernel", "k4": "k4_spmv_kernel", "k5": "k5_sweep", "k6": "k6_(update|contended)_kernel"}


def _ncu_cell(knobs, variant, note, est):
    """Profiles the second pass of variant A or B, skipping one pass for A and three for B. K2's launch check adds
    one counting launch per variant, skipped too"""
    launches = int(knobs.get("sweeps", 8)) if knobs["kernel"] == "k5" else 1
    check_launches = 1 if knobs["kernel"] == "k2" else 0
    skip = launches + check_launches if variant == "A" else 3 * launches + 2 * check_launches
    cell = dict(instr="ncu", binary="route", id=_cid("ncu", variant=variant, **knobs), sub="run", args=_args(**knobs),
                est=est, note=note, events=None, seeded=True,
                ncu=dict(regex=NCU_KERNEL_REGEX[knobs["kernel"]], skip=skip, count=launches))
    return cell


def ncu_cells():
    """The direct variant everywhere, the copy variant only at the home settings"""
    cells = {}

    def add(knobs, variant, note, est=120):
        cell = _ncu_cell(knobs, variant, note, est)
        cells.setdefault(cell["id"], cell)

    for placement in ("cpu", "hbm"):
        k2 = dict(K2_HOME, placement=placement)
        k2_8m = dict(K2_8M, placement=placement)
        for variant in "AB":
            add(k2, variant, "K2 at home, %s, variant %s" % (placement, variant))
            add(dict(K1_HOME, placement=placement), variant, "K1 at home, %s, variant %s" % (placement, variant))
            add(dict(K5_HOME, placement=placement), variant, "K5 at home (tiles), %s, variant %s" % (placement, variant))
            add(dict(K5_HOME, placement=placement, tiling="none"), variant, "K5 untiled, %s, variant %s" % (placement, variant))
            for generator in ("uniform", "rmat"):
                add(dict(K4_HOME, placement=placement, generator=generator), variant, "K4 %s, %s, variant %s" % (generator, placement, variant))
            for update in ("atomic", "plain", "returned"):
                add(dict(K6_HOME, placement=placement, update=update), variant, "K6 %s update, 1 GiB, %s, variant %s" % (update, placement, variant))
            for strategy in ("atomic", "warp", "private"):
                add(dict(K6_CONTENDED, placement=placement, strategy=strategy), variant, "K6 1K entries, %s, %s, variant %s" % (strategy, placement, variant))
            add(dict(K6_CONTENDED, placement=placement, keys=1048576), variant, "K6 1M entries, atomic in place, %s, variant %s" % (placement, variant))
        for mib in (8, 1024):
            add(dict(k2, **{"working-set-mib": mib}), "A", "K2 at W = %d MiB, %s" % (mib, placement))
        add(dict(k2_8m, rotated=1), "A", "K2 rotated 8 MiB, %s" % placement)
        add(dict(k2_8m, tiling="tiles"), "A", "K2 tiles at 8 MiB, %s" % placement)
        for scope in ("cta", "gpu", "sys"):
            add(dict(k2_8m, scope=scope), "A", "K2 %s-scope fence at 8 MiB, %s" % (scope, placement))
        for k in (1, 64):
            add(dict(k2, k=k), "A", "K2 at k = %d, %s" % (k, placement))
        add(dict(K6_HOME, placement=placement, layout="line"), "A", "K6 one line per thread, %s" % placement)
    add(dict(K6_HOME, placement="hbm", **{"footprint-mib": 16}), "A", "K6 L2-resident table, hbm")
    k3 = dict(K3_HOME, placement="hbm", **{"footprint-mib": 16384})
    for order in ("random", "64k", "2m"):
        add(dict(k3, **{"page-order": order}), "A", "K3 page order %s at 16 GiB, hbm" % order, 300)
    add(dict(k3, **{"page-size": "512m"}), "A", "K3 512 MB pages at 16 GiB, hbm", 300)
    return list(cells.values())


# spe cells, the CPU's loads and stores of one setting under Arm SPE, in a campaign of their own (results/spe*)

# jittered, since a fixed power-of-two interval over a short loop hits the same instruction at the same line offset
# the kernel is included so perf can attribute the samples
SPE_EVENT = "arm_spe_0/jitter=1,load_filter=1,store_filter=1,min_latency=0/"
SPE_PERIOD = 262144
SPE_FIELDS = "comm,pid,tid,ip,dso,addr,data_src,weight"


def _spe_cell(knobs, note, est):
    """An A/A' cell under perf record, so all its samples belong to one setting"""
    knobs = dict(knobs, type="aa")
    return dict(instr="spe", binary="route", id=_cid("spe", **knobs), sub="run", args=_args(**knobs),
                est=est, note=note, events=None, seeded=True, spe=True)


def spe_cells():
    """CPU-issued K6 updates of each kind, and the CPU reading the K4 and K5 output after each run"""
    cells = []
    for placement in ("cpu", "hbm"):
        for mib in (0.0625, 1, 16, 256):
            for update in ("atomic", "plain", "stadd", "returned"):
                cells.append(_spe_cell(dict(K6_CPU, placement=placement, update=update, **{"footprint-mib": mib}),
                                       "K6 CPU-issued %s, %s MiB table, %s" % (update, _fmt(mib), placement), 180))
        for home, name in ((K4_HOME, "K4"), (K5_HOME, "K5")):
            cells.append(_spe_cell(dict(home, placement=placement, host="reads", sharing="shared"),
                                   "%s, the CPU reads the output after each run, %s" % (name, placement), 300))
    return cells


# transient cells, the population row of the one-time costs

# home recipe first. The -thp levels only for CPU and registration (a GPU population gets no huge pages at fault
# time), plus gpu-bound-thp for the page size a GPU population ends up with
POPULATION_LEVELS = ("cpu-all", "cpu-one", "cpu-node1", "gpu-bound", "gpu-unbound", "register", "cpu-all-thp",
                     "cpu-one-thp", "cpu-node1-thp", "register-thp", "gpu-bound-thp", "copy", "copy-calls", "gpu-device")


def population_cells():
    """Every population level once per round on a fresh mapping, in two processes per setting"""
    cells = []
    for home, name in ((K1_HOME, "K1"), (K3_HOME, "K3")):
        for mib in (1024, 8192):
            for process in (1, 2):
                knobs = dict(home, process=process, **{"footprint-mib": mib})
                cells.append(dict(instr="transient", binary="route", id=_cid("transient", **knobs), sub="transient",
                                  args=_args(**knobs) + ["--levels", "+".join(POPULATION_LEVELS), "--runs", "10", "--rounds", "15"],
                                  est=300 if mib == 1024 else 600, note="%s population row, %d MiB, process %d" % (name, mib, process),
                                  events=EV_ROUTE, seeded=True))
    return cells


# bisection, route cells at the levels analysis/crossovers.py asks for, tuned like grid cells

HOMES = {"k1": K1_HOME, "k2": K2_HOME, "k3": K3_HOME, "k4": K4_HOME, "k5": K5_HOME, "k6": K6_HOME}


def bisect_tune_cells():
    """Copy space at every bisection level (the direct shape stays the one frozen for the axis range)"""
    g = _Grid()
    for b in load_json(BISECTION_FILE):
        knobs = dict(HOMES[b["kernel"]], placement=b["placement"], type="tune", tune="copy", **b["knobs"])
        g.add(knobs, "%s copy space at the bisection level %s of %s, %s" % (b["kernel"].upper(), b["level"], b["axis"], b["placement"]),
              400 + int(float(knobs.get("footprint-mib", 1024))) // 32)
    return g.list()


def bisect_cells():
    g = _Grid()
    for b in load_json(BISECTION_FILE):
        knobs = dict(HOMES[b["kernel"]], placement=b["placement"], **b["knobs"])
        g.add(knobs, "%s route cell at the bisection level %s of %s, %s" % (b["kernel"].upper(), b["level"], b["axis"], b["placement"]))
    return g.list()


def calib_rest_cells():
    """grid_rest's groups without a floor, run in two jobs with different seeds for their floors"""
    return _rest_grid(True)


def grid_rest_cells():
    return _rest_grid(False)


def sensitivity_settings():
    """Tuned settings whose frozen copy is the simplest within the floor, with the cell ids for both copies"""
    tuned = load_json(TUNED_COPY_FILE)
    out = []
    for kernel, placements in sorted(tuned.items()):
        for placement, settings in sorted(placements.items()):
            for key, entry in sorted(settings.items()):
                if not entry["rule"].startswith("simplest") or entry["copy"] == entry["fastest"]:
                    continue
                knobs = dict(pair.split("=", 1) for pair in key.split(",") if "=" in pair)
                knobs.update(kernel=kernel, placement=placement)
                out.append(dict(knobs=knobs, key=key, entry=entry, frozen_id=_cid("route", **knobs),
                                fastest_id=_cid("route", **dict(knobs, copy=entry["fastest"]))))
    return out


def sensitivity_cells():
    """Each such setting with its frozen and its fastest copy, so a route verdict can be read against both"""
    g = _Grid()
    for s in sensitivity_settings():
        kernel, placement, entry = s["knobs"]["kernel"].upper(), s["knobs"]["placement"], s["entry"]
        g.add(s["knobs"], "%s route cell at %s, %s, frozen copy %s" % (kernel, s["key"], placement, entry["copy"]))
        g.add(dict(s["knobs"], copy=entry["fastest"]),
              "%s route cell at %s, %s, fastest copy %s" % (kernel, s["key"], placement, entry["fastest"]))
    return g.list()


AA_REPLICATES = 3


def aa_bias_cells():
    """Allocation-order check for the kernels without A/A' cells so far, at the settings their contrasts use most"""
    settings = [
        (dict(K1_HOME, **{"footprint-mib": 64}), "K1 64 MiB"),
        (K1_HOME, "K1 1 GiB"),
        (K2_HOME, "K2 32 MiB window, k = 16"),
        (K2_8M, "K2 8 MiB window, k = 16"),
        (K4_HOME, "K4 1 GiB"),
        (dict(K4_HOME, host="reads", sharing="shared"), "K4 1 GiB, the CPU reads the output"),
        (K5_HOME, "K5 512 MiB, 8 sweeps"),
        (dict(K5_HOME, host="reads", sharing="shared"), "K5 512 MiB, 8 sweeps, the CPU reads the output"),
        (K6_HOME, "K6 1 GiB table"),
        (dict(K6_CONTENDED), "K6 contended on 1024 entries"),
        (K6_CPU, "K6 CPU-issued, 256 MiB table"),
    ]
    g = _Grid()
    for placement in ("cpu", "hbm"):
        for knobs, name in settings:
            for replicate in range(1, AA_REPLICATES + 1):
                g.add(dict(knobs, placement=placement, type="aa", replicate=replicate),
                      "%s A/A' cell, %s, process %d" % (name, placement, replicate))
    return g.list()


PHASES = {
    "route_slice": route_slice_cells,
    "cell_types": cell_types_cells,
    "k3_cells": k3_cells,
    "carry_over": carry_over_cells,
    "grid_k1k3": grid_k1k3_cells,
    "tune_direct": tune_direct_cells,
    "tune_copy": tune_copy_cells,
    "tune_heldout": tune_heldout_cells,
    "live_rest": live_rest_cells,
    "tune_direct2": tune_direct2_cells,
    "tune_copy2": tune_copy2_cells,
    "calib_rest": calib_rest_cells,
    "grid_rest": grid_rest_cells,
    "ncu": ncu_cells,
    "bisect_tune": bisect_tune_cells,
    "bisect": bisect_cells,
    "k3_copy512": k3_copy512_cells,
    "k3_copy512_hbm16": k3_copy512_hbm16_cells,
    "k3_bucketing": k3_bucketing_cells,
    "k3_pageorder_all": k3_pageorder_all_cells,
    "k2_window_over_l2": k2_window_over_l2_cells,
    "ncu_window": ncu_window_cells,
    "k3_alignment": k3_alignment_cells,
    "coherence_axes": coherence_axes_cells,
    "caching_axes": caching_axes_cells,
    "k2_copy_probe": k2_copy_probe_cells,
    "atomics_axes": atomics_axes_cells,
    "spe": spe_cells,
    "population": population_cells,
    "sensitivity": sensitivity_cells,
    "aa_bias": aa_bias_cells,
}


if __name__ == "__main__":
    import sys
    for ph in (sys.argv[1:] or PHASES):
        cells = PHASES[ph]()
        print("%s: %d cells, est %.0f min" %
              (ph, len(cells), sum(c["est"] for c in cells) / 60))
        for c in cells:
            print("  ", c["id"], " ".join(c["args"]))
