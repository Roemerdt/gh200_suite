# Route cells: direct route against copy route, recomputed from raw rows

Times are per repetition in ms: one pass for the direct route, one complete call (copy-in, kernel, copy-out) for the copy route. The route difference is direct minus copy within a repeat, as median with its 95 % rank interval; a negative value means direct access is faster. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | direct ms | copy ms | route difference ms [interval] | relative to copy | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|
| footprint-mib=1024,generator=rmat,kernel=k4,placement=cpu | 160.9870 | 52.8136 | 108.1670 [108.1070, 108.2184] | +204.8 % | 10 | yes | pass |
| footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu | 45.1447 | 5.1018 | 40.0444 [40.0194, 40.1551] | +784.9 % | 10 | yes | pass |
| footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm | 2.1008 | 4.6879 | -2.5872 [-2.5905, -2.5825] | -55.2 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.1,working-set-mib=32 | 2.6558 | 1.0427 | 1.6136 [1.6121, 1.6159] | +154.8 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=32 | 2.7037 | 3.3277 | -0.6239 [-0.6259, -0.6187] | -18.7 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=32 | 0.5469 | 2.9406 | -2.3930 [-2.3963, -2.3894] | -81.4 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=cpu,update=atomic | 6.1687 | 7.3608 | -1.1932 [-1.1965, -1.1861] | -16.2 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=hbm,update=atomic | 0.8237 | 6.6072 | -5.7836 [-5.7855, -5.7803] | -87.5 % | 10 | yes | pass |
| footprint-mib=16,kernel=k6,placement=hbm,update=atomic | 0.0765 | 0.1871 | -0.1106 [-0.1109, -0.1101] | -59.1 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=1 | 27.1086 | - | - [-, -] | - | 0 | no | FAILED: aligned_ok, void_checksum_rows=37 |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles | 27.0290 | 6.4874 | 20.5495 [20.5323, 20.5695] | +316.8 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles | 3.2746 | 6.1396 | -2.8673 [-2.8717, -2.8619] | -46.7 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1048576,placement=cpu | 7.8891 | 0.2489 | 7.6404 [7.6375, 7.6411] | +3070.1 % | 10 | yes | pass |

## Host phases

The CPU phase before every pass, timed on the CPU clock (ms per pass), and the state check's median load latency on the preparing core after the phase (ns per sampled load), per variant.

| cell | direct CPU ms | direct state ns | copy CPU ms | copy state ns |
|---|---|---|---|---|
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.1,working-set-mib=32 | - | - | - | - |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=1 | - | - | - | - |

## Per cell

### route/footprint-mib=1024,generator=rmat,kernel=k4,placement=cpu

- first variant B, seed 7; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 6.7 GB/s over the touched lines; buffer at 0x4e3300000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 2.9930 ms, kernel 49.6992 ms, copy-out 0.1203 ms; source buffer at 0x4e3440000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.97e+09 (354.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.689e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu

- first variant A, seed 7; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 23.8 GB/s over the touched lines; buffer at 0x580000000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 2.9438 ms, kernel 2.0535 ms, copy-out 0.1203 ms; source buffer at 0x580100000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 4.636e+09 (552.6 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.689e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm

- first variant A, seed 7; repeats alternated as drawn: yes
- direct route: 10 passes per interval, 511.1 GB/s over the touched lines; buffer at 0x46e880000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 2.5464 ms, kernel 2.0384 ms, copy-out 0.1116 ms; source buffer at 0x46e980000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.689e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.1,working-set-mib=32

- first variant B, seed 7; repeats alternated as drawn: yes
- direct route: 10 passes per interval, 12.6 GB/s over the touched lines; buffer at 0x598740000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 20 calls per interval; first call of an interval: copy-in 0.6764 ms, kernel 0.3712 ms, copy-out 0.0147 ms; source buffer at 0x598840000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.366e+08 (2047.9 per touched line), copy 1.074e+08; SMMU translation requests per repetition: direct 816.2, copy 5.056e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=32

- first variant B, seed 7; repeats alternated as drawn: yes
- direct route: 8 passes per interval, 12.4 GB/s over the touched lines; buffer at 0x48d0c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9348 ms, kernel 0.3870 ms, copy-out 0.0148 ms; source buffer at 0x48d1c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.366e+08 (2047.9 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=32

- first variant B, seed 7; repeats alternated as drawn: yes
- direct route: 38 passes per interval, 61.3 GB/s over the touched lines; buffer at 0x48f840000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.5480 ms, kernel 0.3896 ms, copy-out 0.0128 ms; source buffer at 0x48f940000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=cpu,update=atomic

- first variant B, seed 7; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 174.1 GB/s over the touched lines; buffer at 0x507bc0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 2.9382 ms, kernel 0.8178 ms, copy-out 3.6170 ms; source buffer at 0x507cc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 4645, copy 3.278e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=hbm,update=atomic

- first variant B, seed 7; repeats alternated as drawn: yes
- direct route: 25 passes per interval, 1303.5 GB/s over the touched lines; buffer at 0x518800000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 2.5463 ms, kernel 0.8163 ms, copy-out 3.2563 ms; source buffer at 0x518900000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 2146, copy 3.278e+04; multiplexed rows voided: 0

### route/footprint-mib=16,kernel=k6,placement=hbm,update=atomic

- first variant B, seed 7; repeats alternated as drawn: yes
- direct route: 264 passes per interval, 219.4 GB/s over the touched lines; buffer at 0x540540000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 108 calls per interval; first call of an interval: copy-in 0.0562 ms, kernel 0.0806 ms, copy-out 0.0619 ms; source buffer at 0x540600000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 48.48; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=1

- first variant B, seed 7; repeats alternated as drawn: yes
- direct route: 10 passes per interval, 19.8 GB/s over the touched lines; buffer at 0x5480c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 0 calls per interval; first call of an interval: copy-in - ms, kernel - ms, copy-out - ms; source buffer at None
- AnonHugePages after population (kB): direct 0, copy None; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy nan; SMMU translation requests per repetition: direct 2.169e+04, copy nan; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles

- first variant B, seed 7; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 19.9 GB/s over the touched lines; buffer at 0x465480000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.4557 ms, kernel 3.2344 ms, copy-out 1.8152 ms; source buffer at 0x4655c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.613e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles

- first variant B, seed 7; repeats alternated as drawn: yes
- direct route: 7 passes per interval, 163.9 GB/s over the touched lines; buffer at 0x454d40000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.2863 ms, kernel 3.2612 ms, copy-out 1.6352 ms; source buffer at 0x454e40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 5582, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1048576,placement=cpu

- first variant B, seed 7; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 1.1 GB/s over the touched lines; buffer at 0x55b380000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 81 calls per interval; first call of an interval: copy-in 0.0407 ms, kernel 0.1816 ms, copy-out 0.0376 ms; source buffer at 0x55b440000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

