# GH200 route experiments

Microbenchmark suite for an NVIDIA GH200 node. A GPU kernel runs by two routes from one binary: the direct route reads its input in CPU memory over NVLink-C2C, the copy route copies the input into HBM, runs the same kernel there and copies the output back.

Both variants alternate inside one measurement cell. The reported quantity is the difference between the data routes (direct minus copy) with hardware counters (C2C and SMMU PMUs) read around every timed interval.

Other cell types move one factor (the touched fraction, the placement of the data, the footprint) away from its reference settings.

## Layout

- `src/` CUDA sources: the benchmark binary that runs a kernel by both routes; the shared header (allocation, timing, run loop, counters); a check tool that measures the GPU's read bandwidth from CPU memory and from GPU memory before a run and loads the GPU until its clock is at its maximum
- `harness/` cell definitions, the campaign runner, Slurm scripts
- `analysis/` tools that make summaries of a campaign's raw rows
- `results/` one folder per campaign: raw rows, environment captures, guards, summary

## Requirements

- A GH200 node in NUMA memory mode (CPU memory as node 0, GPU memory as node 1) running Linux on aarch64.
- CUDA 13.0 toolkit (`nvcc`, target `sm_90`) and GCC 12; the host code is compiled for `armv9-a`. `nvc++` only for the optional `make nvcpp`.
- Python 3, standard library only.
- To read the hardware counters, `perf_event_paranoid` 0 (or `CAP_PERFMON`) and the C2C (`nvidia_nvlink_c2c0_pmu_0`) and SMMU (`smmuv3_pmcg_*`, the instance named in `harness/site.env`) PMUs exposed by the kernel. Without them, omit `--events` when running the binary, or pass `--no-events` to the campaign runner, which then drops the counters from every cell; such runs are not measurement data.

## Build

```bash
make         # bin/route, bin/shakedown, build_flags.txt (compiler versions and flags)
make nvcpp   # optional: bin/shakedown through nvc++
make clean
```

The cluster-specific settings are in `harness/site.env`: Slurm node, partition, resource flags and time limits, the modules to load, the Slurm path, the bandwidth gate factor and the name of the GPU's SMMU PMU, which the build compiles into the binary. Node topology (NUMA node ids, the timed core, the huge-page size) is a set of `SUITE_*` macros in `src/common/topology.h`, overridable with `make SITE_DEFS="-DSUITE_...=..."`. The GPU generation is `make ARCH=sm_90`.

## Run one cell

```bash
./bin/shakedown bw 0 && ./bin/shakedown bw 1    # GPU read bandwidth from CPU memory (node 0) and GPU memory (node 1); the Slurm jobs abort unless node 1 is at least twice node 0
./bin/shakedown warmup 30                       # 30 s of sustained load so the SM clock is at its maximum
./bin/route run --kernel k1 --placement cpu --footprint-mib 1024 --f-num 1 --f-den 1 \
    --warmup 10 --n0 10 --step 10 --cap 100 --target-ms 20 --first A --seed 1 \
    --events route --out k1_f1.csv
```

Kernel and home options:

- `--kernel k1|k2|k3|k3p|k4|k5|k6`: the kernel. `k1` streams a fraction of the lines; `k2` is a persistent kernel whose blocks reread their slice of a window k times; `k3` gathers random words through an index array in device memory; `k3p` reads one line of every 64 KB page in random page order; `k4` is a sparse matrix-vector product over a synthetic graph; `k5` a five-point stencil over a square grid, several sweeps per pass; `k6` adds to the entries of a table in place (atomics).
- `--placement cpu|hbm`: where the direct route's data live: system memory bound to the CPU's NUMA node, or the same allocation bound to the GPU's node (populated by the CPU and read once by the GPU before the first interval).
- `--footprint-mib F`: input size in MiB. Default 1024.
- `--page-size 64k|512m`: the pages of the input buffer; `512m` asks for transparent huge pages and the cell is refused (exit code 4) if the whole input is not backed by them. Default `64k`.
- `--alignment 1g|off512m`: the input buffer starts on a 1 GiB boundary, or 512 MiB past a 16 GiB boundary. Default `1g`.
- `--f-num g`, `--f-den G` (K1): touched fraction f = g/G; g of every G 128 B lines are read. Default 1/1. A touched set below 8 MiB at CPU placement, or below twice the GPU's L2 at HBM placement, uses the kernel's cursor: every pass reads the next g lines of each group of G, so consecutive passes read disjoint lines over the same pages.
- `--working-set-mib W`, `--k K`, `--rotated 0|1`, `--scope none|cta|gpu|sys`, `--tiling none|tiles` (K2): the window, the rereads per pass, whether each reread moves to the next slice, the acquire fence between rereads, whether the slice is staged in shared memory.
- `--generator uniform|rmat`, `--degree D` (K4): the graph generator and the nonzeros per row.
- `--sweeps S`, `--tiling none|tiles` (K5): the sweeps per pass, whether each sweep stages its tile in shared memory.
- `--update atomic|plain|returned|stadd`, `--keys N`, `--strategy atomic|warp|private`, `--layout warp|line`, `--repeat k`, `--issuer gpu|cpu` (K6): the update kind, the contended table size (0 for one update per slot), the coordination strategy, the slot layout, dependent repeats, and whether CPU threads issue the passes.
- `--host writes|state|reads`, `--w`, `--pattern word|line`, `--writers N`, `--state dirty|clean|evicted`: a host phase before every pass, in which the CPU writes a fraction w of the lines, prepares the lines the next pass reads into a cache state, or reads the output.
- `--sharing control|shared`: whether the host phase works on a disjoint control buffer or on the variant's own input.
- `--recopy runs|pitched|gather`: the copy route's stateful re-copy of the written runs.
- `--gathers N`, `--page-order random|64k|2m`, `--partition none|2g`, `--index-order random|sorted` (K3): the number of random 8-byte gathers (default 16,777,216); whether the indices are grouped by 64 KB page or 2 MB block (random within, the same words read); whether every pass first buckets the indices by 2 GiB window on the GPU; whether the indices are sorted once at set-up (the sort time is recorded as `setup_ns`).
- `--shape BxTxL`: the direct route's launch shape at CPU placement (blocks, threads per block, load width 8 or 16 bytes), default 528x256x8; `--shape-hbm` the same at HBM placement; `--copy-shape` and `--copy-shape-hbm` the copy route's kernel shape at either placement. The runner fills them from `harness/tuned_direct.json` once the direct tuning has run.
- `--copy LABEL`: the copy route's configuration, written `<ce|kernel>-<pageable|registered>-<1|2|4>-<whole|4m|16m|64m|256m>-<none|pipe>-<whole|touched>[-kernel]` (copy mechanism, host memory, streams, chunk size, pipelining with the kernel's parts, whole input or touched lines only, and a copy-kernel copy-out where the output is large); default `ce-pageable-1-whole-none-whole`, the simplest. `--copy-hbm` for the copy variant at HBM placement and `--copy-at` for the one at the level, where they differ. The runner fills them from `harness/tuned_copy.json`.

Cell options:

- `--type route|factor|four|kvar|cross|aa|tune`: the cell type, default `route`. Variants beyond the 26th are named `v26`, `v27`, ...
  - `route`: the direct route (A) and the copy route (B) at the home setting.
  - `factor`: the direct route at home (A) and at one level of a factor (B).
  - `four`: direct and copy at home (A, B) and at the level (C, D), in rounds.
  - `kvar`: the direct route at home (A) and at every level (B, C, ...), in rounds.
  - `cross`: the direct route at home (A), at a level of one factor (B), at a level of a second factor (C) and at both (D), in rounds.
  - `aa`: two identically prepared direct variants (A, B).
  - `tune`: one route at home in every configuration of a tuning space, in rounds, all on shared buffers. `--tune direct` the direct route's launch shapes, `--tune copy-kernel` the copy route's kernel shapes, `--tune copy` the copy configurations (`--copies L+L+L` restricts them, for the held-out block).
- `--vary F`, `--at L[+L...]`: the factor and its level(s). `factor`, `four` and `cross` take one level, `kvar` at least two, joined by `+`. `cross` names its second factor and level with `--vary2` and `--at2`. Factors:
  - `placement` (levels `cpu`, `hbm`), `footprint` (a size in MiB), `page-size` (`64k`, `512m`), `alignment` (`1g`, `off512m`), and `sharing` (`control`, `shared`) for cells with a host phase.
  - the kernel's own, each with the knob's values as levels: K1's `f` with a level written `<g>of<G>` (for example `1of100`); K2's `k`, `working-set`, `rotated`, `scope` and `tiling`; K3's `page-order`, `partition` and `index-order`; K4's `generator`; K5's `sweeps` and `tiling`; K6's `update`, `keys`, `strategy`, `layout`, `repeat` and `issuer`.
- `--replicate N`: a label that tells otherwise identical cells apart (the A/A' cells). Default 1.
- `--sequence AABB`: runs a two-variant cell in a fixed pattern over A and B instead of the paired loop, `--warmup` repeats of the pattern recorded as warm-up and then `--cap` repeats, for the carry-over check (does a variant's time depend on which variant ran before it).

Run options:

- `--warmup N`: repeats (or rounds) per variant recorded with status `WARMUP` and excluded from the statistics. Default 10.
- `--n0 N`, `--step N`, `--cap N`: sequential stopping. Counted repeats per variant start at `n0` and grow by `step` until every target is met (relative half-width of the rank interval within 2 % per variant and within 10 % for the paired difference, which must exclude zero) or `cap` is reached. Cells with rounds count rounds and require, for every contrast they report, a half-width within the larger of 10 % of its median and `--floor-ns`. Defaults 10, 10, 100.
- `--target-ms T`: minimum length of a timed interval. Repetitions per interval (kernel passes for the direct route, complete calls for the copy route) are calibrated to reach it. Default 20.
- `--passes A=8,B=7,...`: frozen repetitions per interval, one per variant; the binary then uses them instead of calibrating and marks every row `passes_frozen`. The runner passes them from `harness/calibrated_passes.json`, which `python3 harness/freeze_passes.py results/<campaign>` writes from a campaign's rows, so every later run of a cell times its intervals the same way.
- `--floor-ns F`: the calibration floor the stopping rule of a cell with rounds uses, recorded in every row. Default 0.
- `--first A|B`: the variant that runs first in every repeat of a two-variant cell. Default A.
- `--seed N`: the campaign seed, recorded in every row; a two-variant cell's first variant was drawn from it by the runner, a cell with rounds draws the order of every round from it itself. Default `na`, refused by cells with rounds.
- `--events LIST`: comma-separated perf events (`<pmu>/<event>/` or raw core codes `rNN`) or a named set. `route` is C2C0 read and write requests and bytes plus the SMMU's ATS translation requests; `writes` adds the writer cores' L2 refills, write-backs and TLB refills; `cpu_atomics` is the SCF's accesses and cache traffic with the issuing cores' L2 write-backs. Empty: no counters.
- `--out FILE`: output CSV, one row per interval, with a `.done` marker file written on completion. Required.
- `--cell`, `--campaign`, `--jobid`, `--attempt`: labels copied into every row; set by the campaign runner.

Unknown flags and invalid values are rejected. A row carries the status, the checksum and its expected value, the time per repetition, the copy call's breakdown, the variant's level and position in its repeat or round, and the counter values. A cell whose host buffers at HBM placement and device buffers would not fit in the GPU node's free memory (minus 2 GiB) exits with code 5 before allocating; the runner records it as a declared gap.

## Run a phase

```bash
python3 harness/campaign.py --phase route_slice --results results/<campaign> --seed <n>   # first job of a campaign
python3 harness/campaign.py --phase route_slice --results results/<campaign>              # resume: reads seed.txt, skips cells with .done
python3 harness/campaign.py --phase route_slice --results results/<campaign> --dry-run    # print the commands only
python3 -m analysis.route results/<campaign>                                              # summary/route_cells.csv and .md, plus factor_cells, four_variant_cells and kvariant_cells where present
```

`campaign.py` runs from the suite directory and expects the binaries in `bin/`. It runs a phase's cells in the order drawn from the stored seed and writes `raw/<cell>.a<attempt>.csv` plus a `.done` marker per cell. A file left without a marker is renamed before its cell is rerun. A cell the binary declines for lack of GPU-node memory is recorded as a `.gap` marker. The runner stops early when the remaining job time (from `SLURM_JOB_END_TIME`, if set) is too short for the next cell.

The summary gives, per cell, the medians of every variant, the cell's contrasts (route difference; factor effect; route difference at each level and its change; each level minus home; a factor's effect at each level of a second factor; the difference between two identical variants) with their rank intervals and sign tests, the checks (checksum, run order against the seed, alignment, page size obtained, residency) and the counter values per repetition and per access. A factor cell whose factor does not touch translation but whose two direct variants differ in translation requests per access by more than the A/A' range of that footprint is flagged (`smmu_rate_flag`).

`python3 harness/grids.py [<phase> ...]` lists the cells and estimated duration of every phase (the `PHASES` table at the end of that file). The first ones: `route_slice` (K1 at f = 1 and 1/2), `cell_types` (K1 at 1 GiB: a four-variant, a factor and a k-variant cell on f, a four-variant cell on placement, the cursor at f = 1/1000, HBM placement), `k3_cells` (K3 and K3P: each translation factor once, the page sizes, both placements, two A/A' cells), `carry_over` (eight K1 and K3 cells in the sequences AAAA, AABB and ABAB) and `grid_k1k3` (the K1 and K3 part of the grid, 161 cells, also the calibration subset).

Tuning: `tune_direct` (the launch-shape space of K1, K3 and K3P at home and at the extremes of their axes, both placements, and the copy route's kernel shapes) and `tune_copy` (the copy space of K1 and K3 at every level of the route axes and footprint, both placements). `python3 harness/freeze_tuning.py results/<campaign>` writes the fastest shapes to `harness/tuned_direct.json` and the frozen copy per setting to `harness/tuned_copy.json` (the simplest configuration when its paired slowdown against the fastest stays below the route floor, else the fastest); with `--held-out` it remakes that choice from a held-out block. Every configuration is validated before it is timed: the device copy is set to a sentinel and one call must still deliver the checksum.

Calibration floors: run `grid_k1k3` as two campaigns with different seeds, then `python3 -m analysis.floors results/<campaign 1> results/<campaign 2>`, which writes `harness/floors.json` with, per cell family and mechanism group, the 90th percentile of the change of every contrast between the runs; the runner passes it to every cell of that family and group as `--floor-ns`. Freeze the first campaign's repetition counts before the second (`harness/freeze_passes.py`), so both time their intervals the same way.

## Running under Slurm

`harness/submit.sh <campaign> build` and `harness/submit.sh <campaign> phase route_slice` submit `harness/jobs/build.sbatch` and `phase.sbatch` with the node, partition, resource flags and time limits from `harness/site.env`. That file holds what changes for another cluster, except the `nvc++` CPU target (`-tp=neoverse-v2` in the Makefile) and the Nsight Compute path in `harness/carveout_probe.sh`. Before the runner, `prologue.sh` captures the environment, runs the placement gate, logs GPU clocks at 1 Hz and warms up. Extra runner arguments go through `CAMPAIGN_ARGS`, for example `CAMPAIGN_ARGS="--seed 7"`. `harness/sync.sh <host>:<dir>` copies the committed tree to the cluster.
