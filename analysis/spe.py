"""spe cells, the CPU's loads and stores of one setting sampled by the Arm statistical profiling extension

usage: python3 -m analysis.spe results/<spe campaign>
Writes summary/spe_cells.csv and spe_cells.md
"""
import csv
import glob
import gzip
import os
import re
import sys

from analysis.load import write_csv

# comm, pid/tid, data address, raw and decoded data source, total latency, instruction address, dso
SAMPLE = re.compile(r"^\s*(?P<comm>.+?)\s+(?P<pid>\d+)/(?P<tid>\d+)\s+(?P<addr>[0-9a-f]+)\s+[0-9a-f]+\s+"
                    r"(?P<source>\|.*?)\s+(?P<latency>\d+)\s+(?P<ip>[0-9a-f]+)\s+\((?P<dso>[^)]*)\)\s*$")
TRACE_SUFFIX = re.compile(r"\.a\d+\.csv\.spe\.txt\.gz$")
SHOWN_SHARE = 0.01  # smallest share of a cell's samples the markdown lists
# measured-loop instructions of the spe2 binary by address modulo 64 KB,
# the same in every process since the load base is 64 KB aligned
# ldadd serves both the atomic and the returned kind
# the only buffer-touching instructions of the 64 KB-table cells and the reads cells' main thread,
# besides the serial and parallel checksums (0x2398, 0xc850) and the fill at 0x2978
# a rebuilt binary needs them found again
LOOP_RESIDUES = {0x3f30: "ldadd", 0x3f70: "plain load",
                 0x3f7c: "plain store", 0x3fc0: "stadd", 0x2630: "read"}


def source_fields(decoded):
    """{'OP': 'LOAD', 'LVL': 'L1 hit', ...} from perf's '|OP LOAD|LVL L1 hit|SNP N/A|...'"""
    fields = {}
    for part in decoded.split("|"):
        name, _, value = part.strip().partition(" ")
        if name:
            fields[name] = value.strip()
    return fields


def buffers(rows_path):
    """[(name, first address, end address)] of the cell's input and output from its last row"""
    with open(rows_path, newline="") as f:
        row = list(csv.DictReader(f))[-1]
    size = int(row["footprint_bytes"])
    return [("input", int(row["addr"], 16), int(row["addr"], 16) + size),
            ("output", int(row["out_addr"], 16), int(row["out_addr"], 16) + size)]


def sample_class(buffer, fields):
    """Buffer, operation and serving level, plus the snoop where perf decoded one"""
    label = "%s %s %s" % (buffer, fields.get(
        "OP", "?"), fields.get("LVL", "?"))
    if fields.get("SNP", "N/A") != "N/A":
        label += ", snoop " + fields["SNP"]
    return label


def percentile(ordered, q):
    """The nearest-rank percentile q (0..1) of a sorted list"""
    return ordered[min(len(ordered) - 1, int(q * len(ordered)))]


def read_trace(path, spans):
    """({class: [latencies]}, TLB misses, samples kept) over the measured loops' samples inside the spans"""
    classes, tlb_misses, total = {}, 0, 0
    with gzip.open(path, "rt") as f:
        for line in f:
            m = SAMPLE.match(line)
            if not m or m.group("comm") != "route" or not m.group("dso").endswith("/route"):
                continue
            addr = int(m.group("addr"), 16)
            buffer = next(
                (name for name, first, end in spans if first <= addr < end), None)
            if buffer is None or int(m.group("ip"), 16) & 0xFFFF not in LOOP_RESIDUES:
                continue
            fields = source_fields(m.group("source"))
            classes.setdefault(sample_class(buffer, fields),
                               []).append(int(m.group("latency")))
            tlb_misses += "miss" in fields.get("TLB", "")
            total += 1
    return classes, tlb_misses, total


def summarize_spe(results_dir):
    out = []
    for path in sorted(glob.glob(os.path.join(results_dir, "raw", "spe", "*.spe.txt.gz"))):
        knobs = dict(pair.split("=", 1) for pair in TRACE_SUFFIX.sub(
            "", os.path.basename(path)).split(","))
        classes, tlb_misses, total = read_trace(
            path, buffers(path[:-len(".spe.txt.gz")]))
        if not total:
            print("warning: %s: no samples of the measured loop" %
                  os.path.basename(path), file=sys.stderr)
            continue
        everything = sorted(v for latencies in classes.values()
                            for v in latencies)
        ranked = [("all", everything)] + sorted(((c, sorted(v))
                                                 for c, v in classes.items()), key=lambda cv: -len(cv[1]))
        for label, latencies in ranked:
            entry = dict(cell="spe/" + TRACE_SUFFIX.sub("", os.path.basename(path)), kernel=knobs["kernel"],
                         placement=knobs.get("placement", "cpu"), footprint_mib=knobs.get("footprint-mib", ""),
                         update=knobs.get("update", ""), host=knobs.get("host", ""), samples=total,
                         tlb_miss_share=tlb_misses / total, source=label, count=len(latencies),
                         share=len(latencies) / total, p50_cycles=percentile(latencies, 0.5),
                         p90_cycles=percentile(latencies, 0.9), p99_cycles=percentile(latencies, 0.99))
            out.append(entry)
    summary_dir = os.path.join(results_dir, "summary")
    os.makedirs(summary_dir, exist_ok=True)
    write_csv(os.path.join(summary_dir, "spe_cells.csv"), out)
    write_md(os.path.join(summary_dir, "spe_cells.md"), out)
    return out


def write_md(path, entries):
    with open(path, "w") as md:
        md.write("# spe cells\n\nThe samples of the measured loop in the cell's input and output: the classes with at "
                 "least %d %% of a cell's samples, and the total latency of their operations in core cycles.\n\n"
                 % (SHOWN_SHARE * 100))
        md.write(
            "| cell | samples | TLB miss | source | share | p50 | p90 | p99 |\n|---|---|---|---|---|---|---|---|\n")
        for e in entries:
            if e["share"] < SHOWN_SHARE:
                continue
            md.write("| %s | %d | %.3f | %s | %.3f | %d | %d | %d |\n" % (
                e["cell"].split(
                    "/", 1)[1], e["samples"], e["tlb_miss_share"], e["source"], e["share"],
                e["p50_cycles"], e["p90_cycles"], e["p99_cycles"]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    entries = summarize_spe(sys.argv[1])
    print("%d spe cells summarised" % len({e["cell"] for e in entries}))
