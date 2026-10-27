# Route cells: direct route against copy route, recomputed from raw rows

Times are per repetition in ms: one pass for the direct route, one complete call (copy-in, kernel, copy-out) for the copy route. The route difference is direct minus copy within a repeat, as median with its 95 % rank interval; a negative value means direct access is faster. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | direct ms | copy ms | route difference ms [interval] | relative to copy | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|
| footprint-mib=1024,kernel=k3,placement=cpu | 5.3733 | 3.4065 | 1.9666 [1.9643, 1.9702] | +57.7 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k3,placement=hbm | 0.4726 | 3.0223 | -2.5494 [-2.5512, -2.5482] | -84.4 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3p,placement=cpu | 7.0502 | 42.1755 | -35.1269 [-35.1347, -35.1226] | -83.3 % | 20 | yes | pass |

## Per cell

### route/footprint-mib=1024,kernel=k3,placement=cpu

- first variant B, seed 29; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 172.8 GB/s over the touched lines; buffer at 0x5a2bc0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 2.9276 ms, kernel 0.4721 ms, copy-out 0.0140 ms; source buffer at 0x5a2d00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.368e+08 (74.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k3,placement=hbm

- first variant A, seed 29; repeats alternated as drawn: yes
- direct route: 43 passes per interval, 1964.3 GB/s over the touched lines; buffer at 0x483880000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.5419 ms, kernel 0.4766 ms, copy-out 0.0126 ms; source buffer at 0x483940000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3p,placement=cpu

- first variant B, seed 29; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 4.8 GB/s over the touched lines; buffer at 0x4e8980000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 42.1120 ms, kernel 0.0464 ms, copy-out 0.0157 ms; source buffer at 0x4e8e00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.355e+07 (128.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 1.971e+06, copy 2.622e+05; multiplexed rows voided: 0

