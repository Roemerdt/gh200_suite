"""ncu cells, one variant's pass under Nsight Compute summed over its launches

usage: python3 -m analysis.ncu results/<ncu campaign>
Writes summary/ncu_cells.csv and ncu_cells.md
"""
import csv
import os
import sys

from analysis.load import load_rows, group_cells, write_csv
from analysis.stats import NAN

K6_KEYS_PER_PASS = 1 << 24


def read_ncu_csv(path):
    """{metric: sum over the profiled launches}, {metric: unit}, launch count"""
    sums, units, launches = {}, {}, set()
    with open(path, newline="") as f:
        lines = [line for line in f if line.startswith('"')]
    reader = csv.reader(lines)
    header = next(reader, None)
    if not header:
        return sums, units, 0
    col = {name: i for i, name in enumerate(header)}
    for record in reader:
        if len(record) != len(header):
            continue
        name, unit, value = record[col["Metric Name"]
                                   ], record[col["Metric Unit"]], record[col["Metric Value"]]
        launches.add(record[col["ID"]])
        try:
            v = float(value.replace(",", ""))
        except ValueError:
            continue
        units[name] = unit
        if name.endswith(".pct") or name == "launch__shared_mem_config_size":
            sums.setdefault(name, []).append(v)
        else:
            sums[name] = sums.get(name, 0.0) + v
    for name, v in list(sums.items()):
        if isinstance(v, list):
            # rates and configurations take the mean over the launches
            sums[name] = sum(v) / len(v)
    return sums, units, len(launches)


def units_of_work(cell, row):
    """(name, count) of the kernel's work unit in one pass"""
    kernel = cell.knobs["kernel"]
    if kernel in ("k3", "k3p"):
        return "gather", float(row.get("gathers", 0) or row.get("touched_lines", 0))
    if kernel == "k6":
        keys = int(cell.knobs.get("keys", 0))
        if keys > 0:
            return "update", float(K6_KEYS_PER_PASS)
        slots, repeat, sweeps = float(row.get("slots", 0)), float(
            row.get("repeat", 1)), float(row.get("sweeps", 1))
        stride = 16 if row.get("layout") == "line" else 1
        return "update", ((slots + stride - 1) // stride) * repeat * sweeps
    return "line", float(row.get("touched_lines", 0))


def summarize_ncu(results_dir):
    cells = group_cells(load_rows(results_dir))
    out = []
    for cell_id in sorted(cells):
        cell = cells[cell_id]
        if cell.instr != "ncu":
            continue
        variant = cell.knobs.get("variant", "A")
        rows = cell.member_rows(variant, good_only=False) or cell.rows
        row = rows[-1]
        path = cell.file + ".ncu.txt"
        if not os.path.exists(path):
            print("warning: %s: no profiler file" % cell_id, file=sys.stderr)
            continue
        sums, units, launches = read_ncu_csv(path)
        unit, count = units_of_work(cell, row)
        # a pipelined copy launches the kernel once per chunk and the cell profiled one launch per sweep,
        # so that launch did the pass's units over the number of parts
        label = str(row.get("copy", "-"))
        if row.get("route") == "copy" and "-pipe-" in label:
            chunk_mib = int(label.split("-")[3].rstrip("m"))
            parts = max(
                1, -(-int(row.get("footprint_bytes", 0)) // (chunk_mib << 20)))
            count = count / parts
            entry_parts = parts
        else:
            entry_parts = 1
        entry = dict(cell=cell_id, kernel=cell.knobs["kernel"], placement=cell.knobs.get("placement", "cpu"),
                     variant=variant, route=row.get("route", ""), launches=launches, parts=entry_parts, unit=unit,
                     units_per_pass=count, copy=label,
                     l1_hit_pct=sums.get("l1tex__t_sector_hit_rate.pct", NAN),
                     shared_mem_config_bytes=sums.get(
                         "launch__shared_mem_config_size", NAN),
                     gpu_ns=sums.get("gpu__time_duration.sum", NAN))
        for metric, short in (("l1tex__t_requests_pipe_lsu_mem_global_op_ld.sum", "ld_requests"),
                              ("l1tex__t_sectors_pipe_lsu_mem_global_op_ld.sum",
                               "ld_sectors"),
                              ("lts__t_sectors_srcunit_tex_op_read.sum",
                               "l2_read_sectors"),
                              ("lts__t_sectors_srcunit_tex_op_read_lookup_hit.sum",
                               "l2_read_hits"),
                              ("dram__sectors_read.sum", "dram_read_sectors"),
                              ("dram__sectors_write.sum", "dram_write_sectors"),
                              ("lts__t_sectors_op_red.sum", "red_sectors"),
                              ("lts__t_sectors_op_atom.sum", "atom_sectors"),
                              ("lts__t_sectors_aperture_sysmem_op_red.sum",
                               "red_sectors_sysmem"),
                              ("lts__t_sectors_aperture_device_op_red.sum",
                               "red_sectors_device"),
                              ("lts__t_sectors_aperture_sysmem_op_atom.sum",
                               "atom_sectors_sysmem"),
                              ("lts__t_sectors_aperture_device_op_atom.sum",
                               "atom_sectors_device"),
                              ("lts__t_sectors_aperture_sysmem_op_read.sum",
                               "read_sectors_sysmem"),
                              ("lts__t_sectors_aperture_sysmem_op_write.sum", "write_sectors_sysmem")):
            v = sums.get(metric, NAN)
            entry[short] = v
            entry[short + "_per_unit"] = v / count if count else NAN
        for knob in ("working-set-mib", "k", "rotated", "tiling", "scope", "sweeps", "generator", "update", "keys",
                     "strategy", "layout", "page-order", "page-size", "f-num", "f-den", "footprint-mib"):
            if knob in cell.knobs:
                entry[knob] = cell.knobs[knob]
        out.append(entry)
    summary_dir = os.path.join(results_dir, "summary")
    os.makedirs(summary_dir, exist_ok=True)
    write_csv(os.path.join(summary_dir, "ncu_cells.csv"), out)
    write_md(os.path.join(summary_dir, "ncu_cells.md"), out)
    return out


def write_md(path, entries):
    def f(v, digits=3):
        return ("%.*f" % (digits, v)) if isinstance(v, float) and v == v else str(v)
    with open(path, "w") as md:
        md.write("# ncu cells\n\nOne variant's pass under Nsight Compute, summed over its launches; per-unit values per "
                 "touched line, gather or update.\n\n")
        md.write("| cell | variant | launches | unit | units/pass | L1 hit % | shmem config | ld req/unit | ld sect/unit | "
                 "L2 read sect/unit | L2 hit/unit | DRAM read/unit | RED/unit (sysmem, device) | ATOM/unit (sysmem, device) | "
                 "sysmem read/unit |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
        for e in entries:
            md.write("| %s | %s | %d | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s (%s, %s) | %s (%s, %s) | %s |\n" % (
                e["cell"].split(
                    "/", 1)[1], e["variant"], e["launches"], e["unit"], f(e["units_per_pass"], 0),
                f(e["l1_hit_pct"], 1), f(e["shared_mem_config_bytes"], 0), f(
                    e["ld_requests_per_unit"]),
                f(e["ld_sectors_per_unit"]), f(e["l2_read_sectors_per_unit"]), f(
                    e["l2_read_hits_per_unit"]),
                f(e["dram_read_sectors_per_unit"]), f(
                    e["red_sectors_per_unit"]), f(e["red_sectors_sysmem_per_unit"]),
                f(e["red_sectors_device_per_unit"]), f(
                    e["atom_sectors_per_unit"]), f(e["atom_sectors_sysmem_per_unit"]),
                f(e["atom_sectors_device_per_unit"]), f(e["read_sectors_sysmem_per_unit"])))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    entries = summarize_ncu(sys.argv[1])
    print("%d ncu cells summarised" % len(entries))
