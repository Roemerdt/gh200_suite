# Route experiments

`route` runs one kernel in one cell. A cell is a list of variants. The direct route runs the kernel on a pointer to system memory; the copy route runs one complete call per repetition, copy-in to a `cudaMalloc` buffer, the same kernel on that buffer, copy-out of the output. Every variant has its own host buffers; the copy variants of a cell share one device buffer.

## Cell types

A route cell alternates the direct route (A) and the copy route (B) at the home setting. A factor cell alternates the direct route at home (A) and at one level of a factor (B). A four-variant cell runs direct and copy at home (A, B) and at the level (C, D) in rounds, each round in an order drawn from the campaign seed, and forms its contrasts within a round: the route difference at home, at the level, and the change between them. A k-variant cell runs the direct route at home (A) and at every level (B, C, ...) in rounds and forms each level minus home within a round. A cross cell runs the direct route at home (A), at a level of one factor (B), at a level of a second factor (C) and at both (D), in rounds, and forms the first factor's effect at each level of the second and the change between them. An A/A' cell alternates two identically prepared direct variants; its difference is the noise between identical buffers.

A transient cell (`route transient`, `transient.h`) times the one-time costs of populating the input: every round runs every population level once on a fresh mapping and times the population, the first runs one by one and the teardown.

## Factors

The factors are `placement` (cpu, hbm), `footprint` (MiB), `page-size` (64k, 512m), `alignment` (1g, off512m: 512 MiB past a 16 GiB boundary), `sharing` (control, shared: whether a cell's host phase works on the variant's own input or on a disjoint control buffer) and the kernel's own (K1: `f`, a level written `<g>of<G>`, for example `1of100`; K2: `k`, `working-set`, `rotated`, `scope`, `tiling`; K3: `page-order`, `partition`, `index-order`; K4: `generator`; K5: `sweeps`, `tiling`; K6: `update`, `keys`, `strategy`, `layout`, `repeat`, `issuer`).

## Host phases

A cell with a host phase (`--host writes|state|reads`) runs that phase before every pass of every variant: the CPU writing a fraction w of the input's lines (one 8-byte store per 64 B line, or whole lines), the CPU preparing the lines the next pass reads into a cache state (dirty, clean, evicted), or the CPU reading the output; the matched control does the same work on the control buffer. Each pass is then timed between its own event pair and the phase on the CPU clock; a verification pass times sampled loads of the prepared lines (the state check).

A copy variant under CPU writes either copies the whole input in every call (the basic copy) or keeps its own device copy and re-copies only the written runs (`--recopy runs|pitched|gather`), validated by changed first words written, re-copied and read back.

## Kernels

- K1 stream reads g of every G lines in address order.
- K2 reuse is a persistent kernel, one block per SM (a dynamic shared-memory request of 116 KiB with the carveout at the 132 KiB configuration), whose blocks each reread their slice of a window of W bytes k times per pass with an acquire fence of a chosen scope between rereads. Its levels are k, the working set W, a rotation that moves each block to the next slice on every reread, shared-memory tiles that stage the slice once, and the fence scope. Its launch check records every block's SM and counts the reads per slice.
- K3 gather reads 16M random 8-byte words through an index array in device memory, drawn from a fixed seed per footprint so every variant of a cell reads the same words. Its page-order level groups the indices by 64 KB page or 2 MB block at set-up (a layout chosen at design time, not timed), its partition level buckets them by 2 GiB window on the GPU inside every pass (a radix sort on the window bits, so the bucketing is part of the timed call), and its sorted level sorts them once on the GPU at set-up, timed and recorded in the `setup_ns` column.
- K3P page-sparse reads one line of every 64 KB page at a seeded offset inside the page, in a seeded random page order, with its cursor advancing the offset by one line per pass.
- K4 graph is a sparse matrix-vector product y = A x in CSR form (8-byte row pointers, column indices, values and x in the input, integer arithmetic) over a synthetic graph of degree 16 drawn from a fixed seed per generator and footprint, uniform or R-MAT; y is its output.
- K5 stencil is a two-dimensional five-point stencil over the largest square grid of doubles the footprint holds, one launch per sweep, the sweeps alternating between two grids that follow the input so that the final grid comes first; with tiles each sweep stages its block's tile and halo in shared memory.
- K6 update adds to the entries of a table that is its own input and output. At zero contention it updates every slot once per sweep (an atomic add whose result is unused, a plain relaxed load, add and store, or an atomic add whose returned value is consumed; consecutive slots per warp, or one line per thread; k repeated updates per slot as the dependent level), with max(1, 256 MiB / table) sweeps per pass. At the contended levels it adds 16M random keys from device memory into a table of 1, 1K or 1M entries, in place, warp-aggregated, or privatised in shared memory and merged at the end of the pass. In CPU-issued passes (`--issuer cpu`) pinned CPU threads update their contiguous shares of the table with `ldadd`, `stadd`, plain `ldr`/`add`/`str` or `ldadd` with the result consumed, timed on the CPU clock.

## Files

- `route.cu` is `main`: parse, set up, calibrate, run the paired loop or the round loop, write the marker; `route transient` runs `transient.h`, the transient cell.
- `config.h` reads the flags into a `Config`, builds the variant list of the cell type, builds one kernel instance per variant and holds the constants of the experiments.
- `cell.h` is `RouteCell`, which checks the cell's demand on GPU-node memory, owns each variant's host buffers and pass count, the shared device copy, the stream and events, and times an interval of any variant.
- `gpu_read.cu` is the GPU read pass over every buffer at HBM placement before the first interval.
- `calibration.h` sets the repetitions per interval.
- `rows.h` formats the binary's own row columns.
- `measurement.h` runs one timed interval of a variant for either loop, with residency, counters and the checksum check, and writes the summary line.
- `kernel.h` is the interface a kernel implements (`RouteKernel`: its knobs as row columns, the lines one pass touches, the words one pass writes and delivers, `populate`, the cursor, `launch`, `expected_checksum`, its parts for a pipelined copy, its touched window, the lines a pass reads for a host phase, whether it updates in place or its passes are CPU-issued) and the `KernelEntry` the driver builds it from (its flags, its factors, how a level sets its flags).
- `copy.cu` holds the copy configurations and the copies they issue; `host_phase.h` the host phases, the cache-state maintenance and the state check.
- `kernels.cu` lists the kernels; `kernels/` holds one file per kernel with its header.

## Adding a kernel

Write `kernels/kN_name.cu` with the `__global__` kernel, a class that implements `RouteKernel`, a `make_kN` that reads the kernel's own flags from `Args`, a `set_level` that rewrites those flags for a level of one of its factors, and a `KernelEntry` naming the kernel, its flags and its factors; declare the entry in `kernels/kN_name.h`; include the header in `kernels.cu` and add the entry to the list. The Makefile compiles every `.cu` under `src/route` and `src/route/kernels` into the binary.

The driver supplies the input buffer, the output buffer and a per-variant pass counter; the kernel's `populate` fills the input and prepares its reference checksums, its `launch` runs one pass with the pass's tag added to block 0's output, and its `expected_checksum` says what the output must hold after a given pass. A kernel with a cursor advances its position with the pass counter and answers `enable_cursor` with true.

## Status

K1, K2, K3, K3P, K4, K5 and K6 at both placements in route, factor, four-variant, k-variant, cross, A/A' and tuning cells; 512 MB pages and the start offset as factors; the cursor for K1, K2 and K3P; the copy route in every configuration of its space (`copy.h`: copy engine or GPU copy kernel, pageable or registered memory, one to four streams, chunks, pipelining with the parts of K1, K4 and K5, the whole input or the touched lines only, and the copy-out by copy engine or copy kernel where the delivered output is large); the host phases and the stateful re-copy; kernels that update in place (K6) and passes issued by CPU threads; transient cells. Not implemented: copy-out pipelining in row chunks.

## Tuning

A tuning cell runs one route in every configuration of a space as its variants, in seeded rounds on shared buffers (the first variant populates, the others attach to its prepared state). The direct space is threads per block (128 to 1024), resident warps per SM (8 to 64, through the blocks per SM), waves (1 to 8) and the load width (8 or 16 bytes where the kernel offers it). The copy space is the configurations above; each is validated with the device copy set to a sentinel before it is timed. `harness/freeze_tuning.py` freezes the fastest shapes and, per setting, the copy configuration the held-out rule chooses.

## What is measured

ns per repetition: one pass for the direct route, one complete call for the copy route. Intervals are calibrated to at least 20 ms by repetitions: one timed repetition sets the count for the warm-up block, and the fastest repetition seen in that block sets it for the counted repeats, because a single copy call can be a slow one. The count can only rise, so warm-up rows may carry fewer `passes` than counted rows. Once a cell has been measured, `harness/freeze_passes.py` freezes its counts into `harness/calibrated_passes.json` by the same rule over all its rows, and every later run gets them as `--passes` (rows then carry `passes_frozen` 1 and the same count throughout). The copy route also records the copy-in, kernel and copy-out times of the first call of each interval, as a breakdown that is not summed.

Two-variant cells stop on the paired loop's targets; cells with rounds stop when every variant meets its point target and every contrast's half-width is within the larger of 10 % of its median and `--floor-ns`; a cell run in a `--sequence` has no stopping rule and runs `--warmup` plus `--cap` repeats of its pattern.

## Reference settings

Each variant has its own host buffers: system allocator, bound to the CPU node, 64 KB pages, start aligned to 1 GiB, populated by the CPU on all cores (one pinned thread per core; the `pop` column says `cpuall`, earlier rows say `cpu1`). The copy route's source is read only by the copy. A variant at the `512m` page-size level maps whole 512 MB huge pages with `madvise`; the pages obtained are read from `AnonHugePages` after population, and a variant whose input is not fully backed refuses the cell with exit code 4. The `off512m` alignment level starts the buffer 512 MiB past a 16 GiB boundary. At HBM placement the same allocation is bound to the GPU's node, populated by the CPU and read once by the GPU before the first interval; the residency guard then checks for that node. Before allocating, the cell adds up what it needs on the GPU's node (host buffers bound there and the device buffers) and exits with code 5, a declared gap, if that exceeds the free memory minus 2 GiB.

## Cursor

A touched set below 8 MiB at CPU placement, or below twice the GPU's L2 at HBM placement, would meet state left by the previous pass. K1 then advances a line phase per pass: pass p reads lines (p x g) mod G onwards of every group of G lines, so consecutive passes read disjoint lines over the same pages. The expected checksum follows the phase. A kernel without a cursor for its setting refuses the cell.

## Output and checksum

A checksum kernel stores one partial sum per block. The direct route's kernel stores them in system memory. The copy route's kernel stores them in device memory and the call copies them out. Both routes therefore deliver the output to host memory. The checksum is the wrap-around sum of the output words and must equal what the kernel computed while populating for that pass. Every pass adds its own tag to the output, so an output left over from an earlier pass cannot pass the check. An interval that fails is recorded as `VOID_CHECKSUM`; a failure during calibration refuses the cell.

## Flags

| flag | meaning |
|---|---|
| `--kernel k1`, `k2`, `k3`, `k3p`, `k4`, `k5`, `k6` | the kernel (see Kernels) |
| `--f-num g`, `--f-den G` | K1's touched fraction f = g/G at home |
| `--gathers`, `--page-order`, `--partition`, `--index-order` | K3's gathers per pass (16,777,216), page order (random, 64k, 2m), partitioning by 2 GiB window (none, 2g), index order (random, sorted) |
| `--footprint-mib` | size of the input buffer at home |
| `--placement cpu`, `hbm` | where the direct route's data live at home |
| `--page-size 64k`, `512m` | the pages of the input buffer at home |
| `--alignment 1g`, `off512m` | where the input buffer starts at home |
| `--type route`, `factor`, `four`, `kvar`, `cross`, `aa` | the cell type (default route) |
| `--vary`, `--at`; `--vary2`, `--at2` | the factor a cell varies and its level(s), `+`-separated for a k-variant cell; the second factor and level of a cross cell |
| `--replicate` | a label that tells otherwise identical cells apart |
| `--sequence` | a fixed pattern over A and B (for example `AABB`) a two-variant cell runs in, for the carry-over check |
| `--shape`, `--shape-hbm`, `--copy-shape`, `--copy-shape-hbm` | launch shapes `<blocks>x<threads>x<load bytes>` of the direct route at either placement and of the copy route's kernel at either placement (default 528x256x8) |
| `--copy`, `--copy-hbm`, `--copy-at` | the copy route's configuration (`copy.h`), at home, at HBM placement and at the level |
| `--tune direct`, `copy-kernel`, `copy`; `--copies` | the space a tuning cell runs; a list of copy configurations that restricts it |
| `--host writes`, `state`, `reads`; `--w`; `--pattern word`, `line`; `--writers`; `--state dirty`, `clean`, `evicted`; `--sharing control`, `shared`; `--recopy runs`, `pitched`, `gather` | the host phase before every pass and its parameters (`host_phase.h`); whether it works on the variant's input or the control buffer; a copy variant's stateful re-copy form |
| `--working-set-mib`, `--k`, `--rotated`, `--scope`, `--tiling` | K2's window, rereads, rotation, fence scope (none, cta, gpu, sys) and tiles |
| `--generator uniform`, `rmat`; `--degree` | K4's graph |
| `--sweeps`; `--tiling none`, `tiles` | K5's sweeps per pass and tiles |
| `--update atomic`, `plain`, `returned`, `stadd`; `--keys`; `--strategy atomic`, `warp`, `private`; `--layout warp`, `line`; `--repeat`; `--issuer gpu`, `cpu` | K6's update kind, contended table size (0: zero contention), coordination strategy, slot layout, dependent repeats and issuer |
| `--levels`, `--runs`, `--rounds`, `--process` | `route transient`: the population levels (`+`-separated, listed in `transient.h`), the runs timed one by one (default 10), the counted rounds (default 15), a label for the process |
| `--first A`, `B`; `--seed` | set by `harness/campaign.py`: the variant that runs first in every repeat of a two-variant cell, drawn from the campaign's stored seed, and that seed, from which a cell with rounds draws the order of every round |
| `--floor-ns` | the calibration floor in the stopping rule of a cell with rounds |
| `--passes` | frozen repetitions per interval per variant (`A=8,B=7`), set by `harness/campaign.py` from `harness/calibrated_passes.json` |
| `--events` | comma-separated perf events, or a named set (`route`, `writes`, `cpu_atomics`) expanded by `counters.h` |

## Recorded per row

The kernel and its knobs, the variant's route, placement, footprint and level, its position in its repeat or round, whether its cursor is on, each buffer's address with its offsets in a 1 GiB and a 16 GiB window, AnonHugePages of the input mapping after population (the `.done` line has the value after the series for every variant), the checksum and its reference for the last pass, the first variant and the seed, the floor, the copy call's breakdown, the host wall time of the interval.

## Counters

The `route` set: C2C0 read and write requests and bytes, SMMU `pcie_ats_trans_rq`. At CPU placement K1's direct route should show 128 B of link reads per touched line, K3's 32 B per gather (one sector), K3P's 128 B per page. The `writes` set adds the writer cores' L2 refills, write-backs and TLB refills (r57, r58, r05) under the `writers` role, for the cells with a host phase; the `cpu_atomics` set is the SCF's memory accesses by side and its cache refills and write-backs with the issuing cores' L2 write-backs (r17), for K6's CPU-issued passes.

## Run

Phases in `harness/grids.py`: `route_slice`, `cell_types`, `k3_cells`, `carry_over` and `grid_k1k3` (K1 and K3), `live_rest` (a short check of the other kernels), `tune_direct`, `tune_copy`, `tune_heldout`, `tune_direct2` and `tune_copy2` (tuning), `calib_rest` (the calibration subset of the remaining grid, run twice with different seeds for the floors), `grid_rest` (K2, K3P, K4, K5, K6 and the coherence cells), `bisect_tune` and `bisect` (the levels `analysis/crossovers.py` asks for), `population` (the transient cells) and `ncu` (one variant's pass under Nsight Compute, in a campaign of its own); the first job of a campaign needs `CAMPAIGN_ARGS="--seed <n>"`.

Summarise with `python3 -m analysis.route results/<campaign>`; draw the floors from two campaigns with `python3 -m analysis.floors`; find the crossovers with `python3 -m analysis.crossovers`; write the report with `python3 -m analysis.report results/<campaign> --replicate results/<replicate>`; `python3 -m analysis.ncu results/<ncu campaign>` for the ncu cells; `python3 -m analysis.population results/<campaign>` for the transient cells.
