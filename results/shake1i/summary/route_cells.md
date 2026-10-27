# Route cells: direct route against copy route, recomputed from raw rows

Times are per repetition in ms: one pass for the direct route, one complete call (copy-in, kernel, copy-out) for the copy route. The route difference is direct minus copy within a repeat, as median with its 95 % rank interval; a negative value means direct access is faster. 'excludes zero' is the interval rule only: resolvability also needs the floor from a replicate campaign (P10.1).

| cell | direct ms | copy ms | route difference ms [interval] | relative to copy | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 3.0014 | 4.2941 | -1.2916 [-1.3026, -1.2847] | -30.1 % | 1000 | yes | pass |
| f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 1.5221 | 3.0881 | -1.5661 [-1.5661, -1.5660] | -50.7 % | 1000 | yes | pass |

## Per cell

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 20261006; repeats alternated as drawn: yes
- direct route: 7 passes per interval, 357.7 GB/s over the touched lines; buffer at 0x4efc80000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.8287 ms, kernel 0.4858 ms, copy-out 0.0132 ms; source buffer at 0x4efd80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- no hardware counters in this cell

### route/f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 20261006; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 352.7 GB/s over the touched lines; buffer at 0x40afc0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.8333 ms, kernel 0.2520 ms, copy-out 0.0113 ms; source buffer at 0x40b0c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- no hardware counters in this cell

