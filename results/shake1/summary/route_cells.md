# Route cells: direct route against copy route, recomputed from raw rows

Times are per repetition in ms: one pass for the direct route, one complete call (copy-in, kernel, copy-out) for the copy route. The route difference is direct minus copy within a repeat, as median with its 95 % rank interval; a negative value means direct access is faster. 'excludes zero' is the interval rule only: resolvability also needs the floor from a replicate campaign (P10.1).

| cell | direct ms | copy ms | route difference ms [interval] | relative to copy | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 2.9930 | 3.3139 | -0.3207 [-0.3216, -0.3194] | -9.7 % | 10 | yes | pass |
| f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 1.5149 | 4.1619 | -2.6475 [-2.6682, -2.3983] | -63.6 % | 100 | yes | pass |

## Per cell

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 20261005; repeats alternated as drawn: yes
- direct route: 7 passes per interval, 358.8 GB/s over the touched lines; buffer at 0x462d40000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.8244 ms, kernel 0.4837 ms, copy-out 0.0116 ms; source buffer at 0x462e40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- no hardware counters in this cell

### route/f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 20261005; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 354.4 GB/s over the touched lines; buffer at 0x401780000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.8250 ms, kernel 0.2501 ms, copy-out 0.0142 ms; source buffer at 0x401880000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- no hardware counters in this cell

