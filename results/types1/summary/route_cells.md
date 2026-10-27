# Route cells: direct route against copy route, recomputed from raw rows

Times are per repetition in ms: one pass for the direct route, one complete call (copy-in, kernel, copy-out) for the copy route. The route difference is direct minus copy within a repeat, as median with its 95 % rank interval; a negative value means direct access is faster. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | direct ms | copy ms | route difference ms [interval] | relative to copy | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | 0.5127 | 3.0543 | -2.5418 [-2.5429, -2.5407] | -83.2 % | 10 | yes | pass |
| f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 0.0075 | 2.6638 | -2.6563 [-2.6565, -2.6558] | -99.7 % | 10 | yes | pass |

## Per cell

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm

- first variant A, seed 23; repeats alternated as drawn: yes
- direct route: 40 passes per interval, 2094.5 GB/s over the touched lines; buffer at 0x4ecec0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.5386 ms, kernel 0.5115 ms, copy-out 0.0117 ms; source buffer at 0x4ecfc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 23; repeats alternated as drawn: yes
- direct route: 2650 passes per interval, 142.3 GB/s over the touched lines; buffer at 0x472700000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 8 calls per interval; first call of an interval: copy-in 2.6486 ms, kernel 0.0091 ms, copy-out 0.0156 ms; source buffer at 0x472800000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+06 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.639e+04; multiplexed rows voided: 0

