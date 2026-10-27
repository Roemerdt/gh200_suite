# Route cells: direct route against copy route, recomputed from raw rows

Times are per repetition in ms: one pass for the direct route, one complete call (copy-in, kernel, copy-out) for the copy route. The route difference is direct minus copy within a repeat, as median with its 95 % rank interval; a negative value means direct access is faster. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | direct ms | copy ms | route difference ms [interval] | relative to copy | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 3.0050 | 3.3404 | -0.3353 [-0.3374, -0.3342] | -10.0 % | 10 | yes | pass |
| f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 1.5223 | 3.1091 | -1.5866 [-1.5885, -1.5845] | -51.0 % | 10 | yes | pass |

## Per cell

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 20261008; repeats alternated as drawn: yes
- direct route: 7 passes per interval, 357.3 GB/s over the touched lines; buffer at 0x5eff00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 2.8477 ms, kernel 0.4888 ms, copy-out 0.0116 ms; source buffer at 0x5effc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+09 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 20261008; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 352.7 GB/s over the touched lines; buffer at 0x598e00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.8529 ms, kernel 0.2527 ms, copy-out 0.0128 ms; source buffer at 0x598ec0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.639e+04; multiplexed rows voided: 0

