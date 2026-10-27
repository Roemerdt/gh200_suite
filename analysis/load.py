"""Raw rows of a campaign's completed attempts (with a .done marker), grouped into cells"""
import csv
import glob
import os
import re
import sys

STRING_COLUMNS = {"instrument", "campaign", "jobid", "cell_id", "pair_id", "alloc_id", "member",
                  "residency_pre", "residency_post", "status", "type", "vary", "at", "level"}
GOOD_STATUS = ("OK", "RECORDED")
MULTIPLEXED = "ctr_multiplexed"


def parse_cell_id(cell_id):
    """'route/f-den=1,f-num=1,...' -> ('route', {'f-den': '1', 'f-num': '1', ...})"""
    instrument, _, rest = cell_id.partition("/")
    knobs = {}
    for pair in rest.split(","):
        if "=" in pair:
            key, value = pair.split("=", 1)
            knobs[key] = value
    return instrument, knobs


def knobs_of(cell_id):
    return parse_cell_id(cell_id)[1]


def _typed(value):
    try:
        if value.lower() in ("nan", "inf", "-inf"):
            return float(value)
        if "." in value or "e" in value or "E" in value:
            return float(value)
        return int(value)
    except (ValueError, AttributeError):
        return value


def is_good(row):
    return row["status"] in GOOD_STATUS and row["cold"] == 0


def load_rows(results_dir):
    """Typed rows of every completed attempt, with _file set"""
    rows = []
    paths = [p for p in sorted(glob.glob(os.path.join(results_dir, "raw", "**", "*.csv"), recursive=True))
             if ".partial." not in p]
    attempts_by_cell = {}
    for path in paths:
        attempts_by_cell.setdefault(
            re.sub(r"\.a\d+\.csv$", "", path), []).append(path)
    for cell_base, attempt_files in sorted(attempts_by_cell.items()):
        completed = [p for p in attempt_files if os.path.exists(p + ".done")]
        if not completed:
            print("warning: %s: no attempt has a .done marker, cell skipped (%d partial attempt file(s))"
                  % (os.path.relpath(cell_base, results_dir), len(attempt_files)), file=sys.stderr)
        for path in completed:
            with open(path, newline="") as f:
                reader = csv.reader(f)
                header = next(reader, None)
                if not header or header[0] != "ts_epoch" or "cell_id" not in header:
                    continue
                for record in reader:
                    if len(record) != len(header):
                        continue
                    row = dict(zip(header, record))
                    for key in row:
                        if key not in STRING_COLUMNS:
                            row[key] = _typed(row[key])
                    row["_file"] = path
                    rows.append(row)
    return rows


def load_done_summary(path):
    try:
        line = open(path + ".done").read().strip()
    except (OSError, TypeError):
        return {}
    return dict(pair.split("=", 1) for pair in line.split() if "=" in pair)


def write_csv(path, dicts):
    if not dicts:
        return
    columns = []
    for d in dicts:
        for key in d:
            if key not in columns:
                columns.append(key)
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        for d in dicts:
            writer.writerow(d)


class Cell:
    """Rows of one cell, variants by the member column (A and B in a two-variant cell)"""

    def __init__(self, cell_id):
        self.id = cell_id
        self.instr, self.knobs = parse_cell_id(cell_id)
        self.rows = []

    def member_rows(self, member, good_only=True):
        """One variant's rows in file order, good_only drops warm-up, cold and discarded rows"""
        rows = [r for r in self.rows if r["member"] == member]
        return [r for r in rows if is_good(r)] if good_only else rows

    def counted_rows(self, member):
        """Good rows whose counters were read without multiplexing"""
        return [r for r in self.member_rows(member) if r.get(MULTIPLEXED) == 0]

    def matched_pairs(self):
        """(rep, A row, B row) where both variants have a good row"""
        a = {r["rep"]: r for r in self.member_rows("A")}
        b = {r["rep"]: r for r in self.member_rows("B")}
        return [(rep, a[rep], b[rep]) for rep in sorted(set(a) & set(b))]

    @property
    def file(self):
        """Raw file of the completed attempt"""
        return self.rows[0]["_file"] if self.rows else None


def group_cells(rows):
    cells = {}
    for row in rows:
        cells.setdefault(row["cell_id"], Cell(row["cell_id"])).rows.append(row)
    return cells
