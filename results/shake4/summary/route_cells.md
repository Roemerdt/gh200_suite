# Route cells: direct route against copy route, recomputed from raw rows

Times are per repetition in ms: one pass for the direct route, one complete call (copy-in, kernel, copy-out) for the copy route. The route difference is direct minus copy within a repeat, as median with its 95 % rank interval; a negative value means direct access is faster. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | direct ms | copy ms | route difference ms [interval] | relative to copy | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 2.6737 | 3.1392 | -0.4658 [-0.4677, -0.4453] | -14.8 % | 10 | yes | pass |
| f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 1.3810 | 3.9265 | -2.4646 [-2.4777, -2.2576] | -62.8 % | 100 | yes | pass |

## Per cell

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 11; repeats alternated as drawn: yes
- direct route: 8 passes per interval, 401.6 GB/s over the touched lines; buffer at 0x5c3000000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.6478 ms, kernel 0.4875 ms, copy-out 0.0132 ms; source buffer at 0x5c3100000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+09 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.639e+04; multiplexed rows voided: 0

### route/f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 11; repeats alternated as drawn: yes
- direct route: 15 passes per interval, 388.8 GB/s over the touched lines; buffer at 0x421c00000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.6491 ms, kernel 0.2539 ms, copy-out 0.0134 ms; source buffer at 0x421d00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.639e+04; multiplexed rows voided: 0

