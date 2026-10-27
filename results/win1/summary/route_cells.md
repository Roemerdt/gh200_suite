# Route cells: direct route against copy route, recomputed from raw rows

Times are per repetition in ms: one pass for the direct route, one complete call (copy-in, kernel, copy-out) for the copy route. The route difference is direct minus copy within a repeat, as median with its 95 % rank interval; a negative value means direct access is faster. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | direct ms | copy ms | route difference ms [interval] | relative to copy | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|
| footprint-mib=1024,k=1,kernel=k2,placement=cpu,working-set-mib=128 | 0.3574 | 0.4196 | -0.0621 [-0.0626, -0.0617] | -14.8 % | 10 | yes | pass |
| footprint-mib=1024,k=1,kernel=k2,placement=cpu,working-set-mib=64 | 0.1821 | 0.2236 | -0.0415 [-0.0417, -0.0412] | -18.6 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=128 | 5.6076 | 1.0474 | 4.5604 [4.5571, 4.5623] | +435.4 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=64 | 2.8187 | 0.5343 | 2.2851 [2.2839, 2.2872] | +427.7 % | 10 | yes | pass |
| footprint-mib=1024,k=2,kernel=k2,placement=cpu,working-set-mib=128 | 0.7055 | 0.4593 | 0.2462 [0.2457, 0.2474] | +53.6 % | 10 | yes | pass |
| footprint-mib=1024,k=2,kernel=k2,placement=cpu,working-set-mib=64 | 0.3525 | 0.2425 | 0.1100 [0.1097, 0.1107] | +45.4 % | 10 | yes | pass |
| footprint-mib=1024,k=4,kernel=k2,placement=cpu,working-set-mib=128 | 1.4037 | 0.5409 | 0.8627 [0.8623, 0.8634] | +159.5 % | 10 | yes | pass |
| footprint-mib=1024,k=4,kernel=k2,placement=cpu,working-set-mib=64 | 0.7053 | 0.2875 | 0.4178 [0.4171, 0.4183] | +145.4 % | 10 | yes | pass |
| footprint-mib=1024,k=64,kernel=k2,placement=cpu,working-set-mib=128 | 22.4313 | 3.0784 | 19.3508 [19.3213, 19.3757] | +628.6 % | 10 | yes | pass |
| footprint-mib=1024,k=64,kernel=k2,placement=cpu,working-set-mib=64 | 11.2381 | 1.5157 | 9.7229 [9.7182, 9.7269] | +641.5 % | 10 | yes | pass |

## Per cell

### route/footprint-mib=1024,k=1,kernel=k2,placement=cpu,working-set-mib=128

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 56 passes per interval, 375.5 GB/s over the touched lines; buffer at 0x536500000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 48 calls per interval; first call of an interval: copy-in 0.3684 ms, kernel 0.0476 ms, copy-out 0.0133 ms; source buffer at 0x5365c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.342e+08 (128.0 per touched line), copy 1.342e+08; SMMU translation requests per repetition: direct 0, copy 2069; multiplexed rows voided: 0

### route/footprint-mib=1024,k=1,kernel=k2,placement=cpu,working-set-mib=64

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 110 passes per interval, 368.5 GB/s over the touched lines; buffer at 0x4c0f00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 91 calls per interval; first call of an interval: copy-in 0.1922 ms, kernel 0.0257 ms, copy-out 0.0148 ms; source buffer at 0x4c0fc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.709e+07 (128.0 per touched line), copy 6.709e+07; SMMU translation requests per repetition: direct 0, copy 1045; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=128

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 23.9 GB/s over the touched lines; buffer at 0x539040000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 20 calls per interval; first call of an interval: copy-in 0.3661 ms, kernel 0.6780 ms, copy-out 0.0124 ms; source buffer at 0x539140000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.147e+09 (2048.0 per touched line), copy 1.342e+08; SMMU translation requests per repetition: direct 0, copy 2068; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=64

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 8 passes per interval, 23.8 GB/s over the touched lines; buffer at 0x485800000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 38 calls per interval; first call of an interval: copy-in 0.1918 ms, kernel 0.3372 ms, copy-out 0.0124 ms; source buffer at 0x485900000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+09 (2048.0 per touched line), copy 6.709e+07; SMMU translation requests per repetition: direct 0, copy 1045; multiplexed rows voided: 0

### route/footprint-mib=1024,k=2,kernel=k2,placement=cpu,working-set-mib=128

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 29 passes per interval, 190.2 GB/s over the touched lines; buffer at 0x41ce40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 44 calls per interval; first call of an interval: copy-in 0.3656 ms, kernel 0.0895 ms, copy-out 0.0156 ms; source buffer at 0x41cf40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.684e+08 (256.0 per touched line), copy 1.342e+08; SMMU translation requests per repetition: direct 0, copy 2069; multiplexed rows voided: 0

### route/footprint-mib=1024,k=2,kernel=k2,placement=cpu,working-set-mib=64

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 57 passes per interval, 190.3 GB/s over the touched lines; buffer at 0x47b100000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 83 calls per interval; first call of an interval: copy-in 0.1898 ms, kernel 0.0467 ms, copy-out 0.0148 ms; source buffer at 0x47b1c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.342e+08 (256.0 per touched line), copy 6.709e+07; SMMU translation requests per repetition: direct 0, copy 1045; multiplexed rows voided: 0

### route/footprint-mib=1024,k=4,kernel=k2,placement=cpu,working-set-mib=128

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 15 passes per interval, 95.6 GB/s over the touched lines; buffer at 0x4e2fc0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 38 calls per interval; first call of an interval: copy-in 0.3649 ms, kernel 0.1728 ms, copy-out 0.0132 ms; source buffer at 0x4e3080000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.368e+08 (512.0 per touched line), copy 1.342e+08; SMMU translation requests per repetition: direct 0, copy 2069; multiplexed rows voided: 0

### route/footprint-mib=1024,k=4,kernel=k2,placement=cpu,working-set-mib=64

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 29 passes per interval, 95.1 GB/s over the touched lines; buffer at 0x4452c0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 70 calls per interval; first call of an interval: copy-in 0.1938 ms, kernel 0.0891 ms, copy-out 0.0154 ms; source buffer at 0x445380000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.684e+08 (512.0 per touched line), copy 6.709e+07; SMMU translation requests per repetition: direct 0, copy 1045; multiplexed rows voided: 0

### route/footprint-mib=1024,k=64,kernel=k2,placement=cpu,working-set-mib=128

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 6.0 GB/s over the touched lines; buffer at 0x49ca40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 0.3646 ms, kernel 2.7096 ms, copy-out 0.0144 ms; source buffer at 0x49cb00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.589e+09 (8192.0 per touched line), copy 1.342e+08; SMMU translation requests per repetition: direct 0, copy 2069; multiplexed rows voided: 0

### route/footprint-mib=1024,k=64,kernel=k2,placement=cpu,working-set-mib=64

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 6.0 GB/s over the touched lines; buffer at 0x5cd580000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 14 calls per interval; first call of an interval: copy-in 0.1914 ms, kernel 1.3197 ms, copy-out 0.0141 ms; source buffer at 0x5cd640000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 4.294e+09 (8192.0 per touched line), copy 6.709e+07; SMMU translation requests per repetition: direct 0, copy 1045; multiplexed rows voided: 0

