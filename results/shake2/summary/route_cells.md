# Route cells: direct route against copy route, recomputed from raw rows

Times are per repetition in ms: one pass for the direct route, one complete call (copy-in, kernel, copy-out) for the copy route. The route difference is direct minus copy within a repeat, as median with its 95 % rank interval; a negative value means direct access is faster. 'excludes zero' is the interval rule only: resolvability also needs the floor from a replicate campaign (P10.1).

| cell | direct ms | copy ms | route difference ms [interval] | relative to copy | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 2.9748 | 4.4824 | -1.5081 [-1.5671, -1.2934] | -33.6 % | 100 | yes | pass |
| f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 1.5091 | 3.6220 | -2.1125 [-2.1204, -2.1077] | -58.3 % | 40 | yes | pass |

## Per cell

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 20261007; repeats alternated as drawn: yes
- direct route: 7 passes per interval, 360.9 GB/s over the touched lines; buffer at 0x51c8c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.8248 ms, kernel 0.4854 ms, copy-out 0.0137 ms; source buffer at 0x51c980000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+09 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 20261007; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 355.8 GB/s over the touched lines; buffer at 0x43b700000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.8244 ms, kernel 0.2491 ms, copy-out 0.0127 ms; source buffer at 0x43b800000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.639e+04; multiplexed rows voided: 0

