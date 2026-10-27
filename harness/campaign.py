#!/usr/bin/env python3
"""Runs the cells of one phase, skipping those marked .done, .gap or .failed (remove .failed to retry). Exits 1 if
any cell failed"""
import argparse
import glob
import gzip
import os
import shutil
import subprocess
import sys
import time

import grids

SEED_FILE = "seed.txt"
GAP_EXIT_CODE = 5  # cell does not fit in GPU-node memory
PASSES_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "calibrated_passes.json")
FLOORS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "floors.json")
TUNED_DIRECT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tuned_direct.json")
TUNED_COPY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tuned_copy.json")
NOT_SETTING = ("kernel", "placement", "type", "tune", "vary", "at", "vary2", "at2", "replicate", "sequence", "copies",
               "process", "copy")
TRANSLATION_KNOBS = ("page-size", "page-order", "alignment", "partition", "index-order")


def setting_key(knobs):
    return ",".join("%s=%s" % (k, v) for k, v in sorted(knobs.items()) if k not in NOT_SETTING)


def level_knobs(knobs):
    """Knobs of the variant at the --at level. Placement and sharing change no copy setting"""
    moved = {k: v for k, v in knobs.items()}
    vary, at = knobs.get("vary"), knobs.get("at")
    if not vary or not at or vary in ("placement", "sharing"):
        return moved
    if vary == "f":
        g, G = at.split("of")
        moved["f-num"], moved["f-den"] = g, G
    elif vary == "footprint":
        moved["footprint-mib"] = at
    else:
        moved[grids.KNOB_OF_FACTOR.get(vary, vary)] = at
    return moved


HOST_KNOBS = ("host", "w", "pattern", "writers", "state", "sharing", "recopy")


def tuned_copy_label(tuned, kernel, placement, knobs):
    """Frozen copy of the setting, else of the nearest tuned one, None without any"""
    settings = tuned.get(kernel, {}).get(placement, {})
    if not settings:
        return None
    home = dict(grids.HOME_SETTING[kernel])
    same_size = dict(home, **{"footprint-mib": knobs.get("footprint-mib", home["footprint-mib"])})
    for candidate in (knobs, {k: v for k, v in knobs.items() if k not in TRANSLATION_KNOBS + HOST_KNOBS}, same_size, home):
        entry = settings.get(setting_key(candidate))
        if entry:
            return entry["copy"]
    return None


def tuned_shape(tuned, kernel, placement, route, knobs):
    """The setting's re-frozen shape, else the home shape"""
    slot = tuned.get(kernel, {}).get(placement, {}).get(route, {})
    if not slot:
        return None
    at = slot.get("at", {}).get(setting_key(knobs))
    if at and at.get("refrozen"):
        return at["shape"]
    return slot.get("home", {}).get("shape")


def tuned_flags(cell, tuned_direct, tuned_copy):
    """Shape and copy flags from the frozen tuning files. Tuning cells get only the shapes, and a sensitivity cell
    keeps the copy in its id"""
    knobs = grids.cell_knobs(cell["id"])
    kernel, home = knobs["kernel"], knobs.get("placement", "cpu")
    flags = []
    for flag, placement, route in (("--shape", "cpu", "direct"), ("--shape-hbm", "hbm", "direct"),
                                   ("--copy-shape", "cpu", "copy"), ("--copy-shape-hbm", "hbm", "copy")):
        shape = tuned_shape(tuned_direct, kernel, placement, route, knobs)
        if shape:
            flags += [flag, shape]
    if knobs.get("type") == "tune":
        return flags
    other = "hbm" if home == "cpu" else "cpu"
    for flag, placement, setting in (("--copy", home, knobs), ("--copy-hbm", "hbm", knobs), ("--copy-at", home, level_knobs(knobs))):
        if flag == "--copy-hbm" and home == "hbm":
            continue
        if flag == "--copy-at" and knobs.get("vary") in (None, "placement"):
            continue
        if flag == "--copy" and "copy" in knobs:
            continue
        label = tuned_copy_label(tuned_copy, kernel, placement, setting)
        if label:
            flags += [flag, label]
    return flags


def floor_ns(cell, floors):
    """Floor of the cell's family and group, None without one"""
    family, group = grids.family_group(grids.cell_knobs(cell["id"]))
    entry = floors.get(family, {}).get(group)
    return entry["floor_ns"] if entry else None


def log(message):
    print("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), message), flush=True)


def campaign_seed(results_dir, given_seed, store=True):
    """The first job stores the seed in <results>/seed.txt, so a resumed job draws what the interrupted one drew"""
    path = os.path.join(results_dir, SEED_FILE)
    if os.path.exists(path):
        stored_seed = int(open(path).read().split()[0])
        if given_seed is not None and given_seed != stored_seed:
            sys.exit("--seed %d differs from the seed %d stored in %s" %
                     (given_seed, stored_seed, path))
        return stored_seed
    if given_seed is None:
        sys.exit(
            "this phase has seeded cells and %s does not exist: pass --seed" % path)
    if store:
        os.makedirs(results_dir, exist_ok=True)
        with open(path, "w") as f:
            f.write("%d\n" % given_seed)
    return given_seed


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", required=True, choices=sorted(grids.PHASES))
    parser.add_argument("--results", required=True,
                        help="results/<campaign> directory")
    parser.add_argument("--bindir", default="bin")
    parser.add_argument("--campaign", default=None,
                        help="campaign name recorded in every row (default: the results directory's name)")
    parser.add_argument("--only", default=None,
                        help="substring filter on cell ids")
    parser.add_argument("--warmup", type=int, default=10,
                        help="repeats per variant recorded as WARMUP and not counted")
    parser.add_argument("--n0", type=int, default=10)
    parser.add_argument("--step", type=int, default=10)
    parser.add_argument("--cap", type=int, default=100)
    parser.add_argument("--target-ms", type=float, default=20.0)
    parser.add_argument("--margin-s", type=float, default=300.0,
                        help="keep this much job time free")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--seed", type=int, default=None,
                        help="campaign seed for the seeded cells, stored on first use")
    parser.add_argument("--no-events", action="store_true",
                        help="run every cell without its hardware counters (trial runs on a node without counter access; not measurement data)")
    return parser.parse_args()


class Job:
    """Slurm's view of this job, with defaults outside Slurm"""

    def __init__(self, args):
        self.id = os.environ.get("SLURM_JOB_ID", "local")
        self.attempt = int(os.environ.get("SLURM_RESTART_COUNT", "0"))
        self.end_time = float(os.environ.get("SLURM_JOB_END_TIME", "0") or 0)
        self.campaign = args.campaign or os.path.basename(
            os.path.normpath(args.results))

    def seconds_left(self):
        """None when no end time is known"""
        return self.end_time - time.time() if self.end_time else None


class CellFiles:
    """Files of one cell under <results>/raw, per attempt"""

    def __init__(self, results_dir, cell_id, attempt):
        self.base = os.path.join(results_dir, "raw", cell_id)
        self.output = "%s.a%d.csv" % (self.base, attempt)
        self.log = self.output + ".log"
        self.done_marker = self.output + ".done"
        self.failed_marker = "%s.a%d.failed" % (self.base, attempt)
        self.gap_marker = "%s.a%d.gap" % (self.base, attempt)

    def prepare_dir(self):
        os.makedirs(os.path.dirname(self.base), exist_ok=True)

    def done_in_any_attempt(self):
        return bool(glob.glob(self.base + ".a*.csv.done"))

    def failed_in_any_attempt(self):
        return bool(glob.glob(self.base + ".a*.failed"))

    def gap_in_any_attempt(self):
        return bool(glob.glob(self.base + ".a*.gap"))

    def write_gap_marker(self):
        """The binary's last log line says what the cell needed and what was free"""
        with open(self.log) as f:
            lines = f.read().strip().splitlines()
        with open(self.gap_marker, "w") as f:
            f.write((lines[-1] if lines else "declared gap") + "\n")

    def rename_partial_files(self):
        """A raw file without a marker is a partial attempt, moved aside so the analysis ignores it"""
        for partial in glob.glob(self.base + ".a*.csv"):
            os.rename(partial, partial + ".partial.%d" % int(time.time()))
            log("    renamed partial file %s" % os.path.basename(partial))

    def write_failed_marker(self, return_code, elapsed_s):
        signal = -return_code if return_code < 0 else ""
        with open(self.failed_marker, "w") as f:
            f.write("rc=%d signal=%s elapsed=%.0f\n" %
                    (return_code, signal, elapsed_s))


def build_command(cell, files, args, job, seed, frozen, floors, tuned_direct, tuned_copy):
    command = [os.path.join(args.bindir, cell["binary"]),
               cell["sub"]] + cell["args"]
    record = ["--out", files.output, "--cell", cell["id"], "--campaign", job.campaign, "--jobid", job.id,
              "--attempt", str(job.attempt)]
    if cell["sub"] == "transient":
        # a transient cell runs its own rounds (transient.h)
        command += tuned_flags(cell, tuned_direct, tuned_copy) + record + ["--seed", str(seed)]
        if cell.get("events") and not args.no_events:
            command += ["--events", cell["events"]]
        return command
    if cell["sub"] != "run":
        return command + ["--out", files.output]
    if cell.get("ncu"):
        # application replay, since kernel replay restores only device memory and K6's direct route, which updates
        # host memory in place, would accumulate the replays and fail its checksum
        n = cell["ncu"]
        command = [grids.SITE.get("SITE_NCU", "ncu"), "--cache-control", "none", "--replay-mode", "application",
                   "--kernel-name-base", "function", "-k", "regex:" + n["regex"], "--launch-skip", str(n["skip"]),
                   "--launch-count", str(n["count"]), "--metrics", grids.NCU_METRICS, "--csv", "--log-file",
                   files.output + ".ncu.txt"] + command
        command += tuned_flags(cell, tuned_direct, tuned_copy) + record
        command += ["--warmup", "0", "--n0", "1", "--step", "1", "--cap", "1", "--target-ms", "1", "--passes", "A=1,B=1",
                    "--first", "A", "--seed", str(seed)]
        return command
    if cell.get("spe"):
        # under perf record with SPE, few repeats to keep the trace small
        command = [grids.SITE.get("SITE_PERF", "perf"), "record", "-e", grids.SPE_EVENT, "-c", str(grids.SPE_PERIOD),
                   "-o", files.output + ".spe.data", "--"] + command
        command += tuned_flags(cell, tuned_direct, tuned_copy) + record
        command += ["--warmup", "2", "--n0", "10", "--step", "10", "--cap", "30", "--target-ms", str(args.target_ms),
                    "--first", grids.first_variant(seed, cell["id"]), "--seed", str(seed)]
        return command
    command += tuned_flags(cell, tuned_direct, tuned_copy) + record
    command += ["--warmup", str(args.warmup), "--n0", str(args.n0), "--step", str(args.step),
                "--cap", str(args.cap), "--target-ms", str(args.target_ms)]
    if cell.get("events") and not args.no_events:
        command += ["--events", cell["events"]]
    if cell.get("seeded"):
        command += ["--first",
                    grids.first_variant(seed, cell["id"]), "--seed", str(seed)]
    if cell["id"] in frozen:
        command += ["--passes", ",".join("%s=%d" % (member, count)
                                         for member, count in sorted(frozen[cell["id"]].items()))]
    floor = floor_ns(cell, floors)
    if floor is not None:
        command += ["--floor-ns", "%.0f" % floor]
    return command


def run_cell(command, files):
    """Output appended to the cell's log. Returns (succeeded, return code, seconds)"""
    started = time.time()
    with open(files.log, "a") as log_file:
        return_code = subprocess.call(
            command, stdout=log_file, stderr=subprocess.STDOUT)
    elapsed_s = time.time() - started
    succeeded = return_code == 0 and os.path.exists(files.done_marker)
    return succeeded, return_code, elapsed_s


def decode_spe(files):
    """SPE trace to gzipped perf script text beside the rows. A failed decode takes back the done marker"""
    trace = files.output + ".spe.data"
    with open(files.log, "a") as log_file, gzip.open(files.output + ".spe.txt.gz", "wb") as out:
        script = subprocess.Popen([grids.SITE.get("SITE_PERF", "perf"), "script", "-i", trace, "--itrace=M",
                                   "-F", grids.SPE_FIELDS], stdout=subprocess.PIPE, stderr=log_file)
        shutil.copyfileobj(script.stdout, out)
        return_code = script.wait()
    if return_code:
        os.remove(files.done_marker)
        return False, return_code
    os.remove(trace)
    return True, 0


def main():
    args = parse_args()
    job = Job(args)

    cells = grids.PHASES[args.phase]()
    needs_seed = any(cell.get("seeded") for cell in cells)
    seed = campaign_seed(args.results, args.seed,
                         store=not args.dry_run) if needs_seed else None
    if seed is not None:
        cells = grids.cell_order(seed, cells)
    if args.only:
        cells = [cell for cell in cells if args.only in cell["id"]]

    frozen = grids.load_json(PASSES_FILE)
    floors = grids.load_json(FLOORS_FILE)
    tuned_direct, tuned_copy = grids.load_json(TUNED_DIRECT_FILE), grids.load_json(TUNED_COPY_FILE)
    log("phase=%s cells=%d jobid=%s attempt=%d campaign=%s warmup=%d frozen_passes=%d with_floor=%d tuned=%d"
        % (args.phase, len(cells), job.id, job.attempt, job.campaign, args.warmup,
           sum(1 for cell in cells if cell["id"] in frozen),
           sum(1 for cell in cells if floor_ns(cell, floors) is not None),
           sum(1 for cell in cells if tuned_flags(cell, tuned_direct, tuned_copy))))
    if args.no_events:
        log("--no-events: cells run without their hardware counters")

    done = skipped = failed = gaps = 0
    for cell in cells:
        files = CellFiles(args.results, cell["id"], job.attempt)
        files.prepare_dir()
        if files.done_in_any_attempt() or files.gap_in_any_attempt():
            skipped += 1
            continue
        if files.failed_in_any_attempt():
            log("SKIP (previously failed, remove .failed to retry): %s" %
                cell["id"])
            skipped += 1
            continue
        seconds_left = job.seconds_left()
        if seconds_left is not None and seconds_left < cell["est"] * 1.5 + args.margin_s:
            log("STOP: %.0f s left, cell %s needs ~%.0f s; resume in the next job" % (
                seconds_left, cell["id"], cell["est"]))
            break

        command = build_command(cell, files, args, job, seed, frozen, floors, tuned_direct, tuned_copy)
        log("RUN %s  (%s)" % (cell["id"], cell["note"]))
        log("    " + " ".join(command))
        if args.dry_run:
            continue

        files.rename_partial_files()
        succeeded, return_code, elapsed_s = run_cell(command, files)
        if succeeded and cell.get("spe"):
            succeeded, return_code = decode_spe(files)
        if succeeded:
            done += 1
            log("OK  %s in %.0f s (est %.0f)" %
                (cell["id"], elapsed_s, cell["est"]))
        elif return_code == GAP_EXIT_CODE:
            gaps += 1
            files.write_gap_marker()
            log("GAP %s (does not fit in GPU-node memory; declared gap)" % cell["id"])
        else:
            failed += 1
            files.write_failed_marker(return_code, elapsed_s)
            log("FAIL %s rc=%d after %.0f s" %
                (cell["id"], return_code, elapsed_s))

    log("phase %s finished: done=%d skipped=%d gaps=%d failed=%d" %
        (args.phase, done, skipped, gaps, failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
