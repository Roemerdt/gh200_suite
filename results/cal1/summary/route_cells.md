# Route cells: direct route against copy route, recomputed from raw rows

Times are per repetition in ms: one pass for the direct route, one complete call (copy-in, kernel, copy-out) for the copy route. The route difference is direct minus copy within a repeat, as median with its 95 % rank interval; a negative value means direct access is faster. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | direct ms | copy ms | route difference ms [interval] | relative to copy | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|
| alignment=off512m,footprint-mib=8192,kernel=k3,placement=cpu | 48.2083 | 21.5825 | 26.6250 [26.5316, 26.6742] | +123.4 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 2.9296 | 4.5056 | -1.5764 [-1.5855, -1.5701] | -35.0 % | 50 | yes | pass |
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | 0.5093 | 3.0556 | -2.5463 [-2.5486, -2.5452] | -83.3 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=cpu | 44.8352 | 50.1545 | -5.3266 [-5.3683, -5.2974] | -10.6 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=hbm | 12.6336 | 49.0179 | -36.3814 [-36.4083, -36.3591] | -74.2 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=cpu | 66.4601 | 75.2181 | -8.7542 [-8.7865, -8.7321] | -11.6 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=hbm | 18.9708 | 73.5649 | -54.5864 [-54.6311, -54.5613] | -74.2 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu | 0.7363 | 1.0491 | -0.3130 [-0.3160, -0.2861] | -29.8 % | 100 | yes | pass |
| f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm | 0.1310 | 0.7867 | -0.6558 [-0.6564, -0.6542] | -83.4 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=cpu | 88.1026 | 100.2461 | -12.1358 [-12.1757, -12.1066] | -12.1 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu | 11.7139 | 12.6009 | -0.8874 [-0.8923, -0.8842] | -7.0 % | 40 | yes | pass |
| f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=hbm | 2.0223 | 12.1306 | -10.1079 [-10.1102, -10.1057] | -83.3 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=cpu | 23.0291 | 25.1029 | -2.0800 [-2.0919, -2.0675] | -8.3 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=hbm | 4.1020 | 24.4360 | -20.3323 [-20.3380, -20.3250] | -83.2 % | 10 | yes | pass |
| f-den=10,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 0.3013 | 3.0178 | -2.7166 [-2.7173, -2.7160] | -90.0 % | 30 | yes | pass |
| f-den=10,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | 0.0594 | 2.6066 | -2.5473 [-2.5482, -2.5464] | -97.7 % | 10 | yes | pass |
| f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=cpu | 2.6631 | 5.0466 | -2.3829 [-2.3855, -1.9845] | -47.2 % | 100 | yes | pass |
| f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=hbm | 0.4733 | 3.0228 | -2.5499 [-2.5511, -2.5485] | -84.4 % | 10 | yes | pass |
| f-den=100,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 0.0344 | 2.9270 | -2.8925 [-2.8939, -2.8914] | -98.8 % | 10 | yes | pass |
| f-den=100,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | 0.0097 | 2.5605 | -2.5508 [-2.5511, -2.5494] | -99.6 % | 10 | yes | pass |
| f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 0.0076 | 3.2606 | -3.2530 [-3.2535, -3.2505] | -99.8 % | 60 | yes | pass |
| f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | 0.0041 | 2.5598 | -2.5557 [-2.5561, -2.5554] | -99.8 % | 10 | yes | pass |
| f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 1.4828 | 3.1792 | -1.6970 [-1.6975, -1.6955] | -53.4 % | 10 | yes | pass |
| f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | 0.2596 | 2.8055 | -2.5459 [-2.5469, -2.5450] | -90.7 % | 10 | yes | pass |
| f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=cpu | 2.2315 | 3.6833 | -1.4522 [-1.4581, -1.4476] | -39.4 % | 90 | yes | pass |
| f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=hbm | 0.3920 | 2.9345 | -2.5424 [-2.5440, -2.5406] | -86.6 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k3,placement=cpu | 5.3740 | 4.2142 | 1.1592 [1.1548, 1.1670] | +27.5 % | 50 | yes | pass |
| footprint-mib=1024,kernel=k3,placement=hbm | 0.4733 | 3.0214 | -2.5484 [-2.5492, -2.5471] | -84.3 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,page-order=2m,placement=cpu | 5.3715 | 42.6087 | -37.2369 [-37.2421, -37.2342] | -87.4 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,page-order=2m,placement=hbm | 2.4566 | 41.4774 | -39.0208 [-39.0286, -39.0129] | -94.1 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,page-order=64k,placement=cpu | 5.1695 | 42.6020 | -37.4345 [-37.4446, -37.4256] | -87.9 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,page-order=64k,placement=hbm | 1.2512 | 41.4602 | -40.2091 [-40.2235, -40.2026] | -97.0 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu | 5.3828 | 42.6282 | -37.2454 [-37.2513, -37.2423] | -87.4 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,page-size=512m,placement=hbm | 0.4832 | 41.3922 | -40.9092 [-40.9214, -40.8983] | -98.8 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,partition=2g,placement=cpu | 5.6819 | 42.8082 | -37.1243 [-37.1354, -37.1077] | -86.7 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,placement=cpu | 432.6112 | 42.6423 | 389.9693 [389.9182, 390.0602] | +914.5 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,placement=hbm | 427.2758 | 41.4989 | 385.7750 [385.4554, 386.0049] | +929.6 % | 10 | yes | pass |
| footprint-mib=24576,kernel=k3,placement=cpu | 598.1637 | 63.6972 | 534.4671 [534.2727, 534.5441] | +839.1 % | 10 | yes | pass |
| footprint-mib=24576,kernel=k3,placement=hbm | 591.4253 | 62.0527 | 529.3634 [529.2630, 529.5434] | +853.1 % | 10 | yes | pass |
| footprint-mib=256,kernel=k3,placement=cpu | 5.3670 | 1.6714 | 3.6957 [3.6924, 3.7294] | +221.1 % | 100 | yes | pass |
| footprint-mib=256,kernel=k3,placement=hbm | 0.4417 | 1.0827 | -0.6407 [-0.6419, -0.6403] | -59.2 % | 10 | yes | pass |
| footprint-mib=32768,kernel=k3,placement=cpu | 684.8273 | 84.7508 | 600.0745 [599.9847, 600.2344] | +708.0 % | 10 | yes | pass |
| footprint-mib=4096,kernel=k3,placement=cpu | 5.5544 | 11.0599 | -5.5048 [-5.5238, -5.4908] | -49.8 % | 10 | yes | pass |
| footprint-mib=4096,kernel=k3,placement=hbm | 5.1668 | 10.6220 | -5.4551 [-5.4574, -5.4540] | -51.4 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu | 7.7473 | 21.5871 | -13.8395 [-13.8429, -13.8361] | -64.1 % | 20 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=hbm | 7.7522 | 20.9194 | -13.1658 [-13.1696, -13.1627] | -62.9 % | 10 | yes | pass |

## Per cell

### route/alignment=off512m,footprint-mib=8192,kernel=k3,placement=cpu

- first variant A, seed 31; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 39.4 GB/s over the touched lines; buffer at 0x4eb020000000 (offset in its 16 GiB window: 536870912 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 21.0661 ms, kernel 0.5019 ms, copy-out 0.0134 ms; source buffer at 0x4eb820000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (36.2 per touched line), copy 8.607e+09; SMMU translation requests per repetition: direct 1.358e+07, copy 1.311e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 8 passes per interval, 366.5 GB/s over the touched lines; buffer at 0x525e00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9371 ms, kernel 0.5135 ms, copy-out 0.0146 ms; source buffer at 0x525f00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+09 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 40 passes per interval, 2108.4 GB/s over the touched lines; buffer at 0x4ef500000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.5414 ms, kernel 0.5117 ms, copy-out 0.0109 ms; source buffer at 0x4ef640000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=cpu

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 383.2 GB/s over the touched lines; buffer at 0x519480000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 42.1132 ms, kernel 8.0223 ms, copy-out 0.0136 ms; source buffer at 0x519940000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.718e+10 (128.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 5.895e+05, copy 2.621e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=hbm

- first variant A, seed 31; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 1359.9 GB/s over the touched lines; buffer at 0x43e5c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 40.9717 ms, kernel 8.0313 ms, copy-out 0.0140 ms; source buffer at 0x43ea40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 8.314e+05, copy 2.647e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=cpu

- first variant A, seed 31; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 387.7 GB/s over the touched lines; buffer at 0x5af280000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 63.1647 ms, kernel 12.0358 ms, copy-out 0.0160 ms; source buffer at 0x5af900000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.577e+10 (128.0 per touched line), copy 2.585e+10; SMMU translation requests per repetition: direct 8.618e+05, copy 3.932e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=hbm

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 1358.4 GB/s over the touched lines; buffer at 0x46f080000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 61.4972 ms, kernel 12.0535 ms, copy-out 0.0138 ms; source buffer at 0x46f700000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.245e+06, copy 3.969e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 28 passes per interval, 364.6 GB/s over the touched lines; buffer at 0x4caa40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 22 calls per interval; first call of an interval: copy-in 0.7667 ms, kernel 0.1361 ms, copy-out 0.0128 ms; source buffer at 0x4cab40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.684e+08 (128.0 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 0, copy 4106; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm

- first variant A, seed 31; repeats alternated as drawn: yes
- direct route: 153 passes per interval, 2048.5 GB/s over the touched lines; buffer at 0x4e0500000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 26 calls per interval; first call of an interval: copy-in 0.6462 ms, kernel 0.1368 ms, copy-out 0.0158 ms; source buffer at 0x4e05c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 4106; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=cpu

- first variant A, seed 31; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 390.0 GB/s over the touched lines; buffer at 0x5430c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 84.2034 ms, kernel 16.0287 ms, copy-out 0.0125 ms; source buffer at 0x543980000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.436e+10 (128.0 per touched line), copy 3.448e+10; SMMU translation requests per repetition: direct 1.133e+06, copy 5.243e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu

- first variant A, seed 31; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 366.7 GB/s over the touched lines; buffer at 0x4f20c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 10.5771 ms, kernel 2.0140 ms, copy-out 0.0125 ms; source buffer at 0x4f2240000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 4.295e+09 (128.0 per touched line), copy 4.295e+09; SMMU translation requests per repetition: direct 0, copy 6.555e+04; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=hbm

- first variant A, seed 31; repeats alternated as drawn: yes
- direct route: 10 passes per interval, 2123.8 GB/s over the touched lines; buffer at 0x59a200000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 10.1116 ms, kernel 2.0083 ms, copy-out 0.0142 ms; source buffer at 0x59a380000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 6.555e+04; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=cpu

- first variant A, seed 31; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 373.0 GB/s over the touched lines; buffer at 0x5fbd00000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 21.0727 ms, kernel 4.0152 ms, copy-out 0.0149 ms; source buffer at 0x5fbfc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.59e+09 (128.0 per touched line), copy 8.607e+09; SMMU translation requests per repetition: direct 5.512e+04, copy 1.311e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=hbm

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 5 passes per interval, 2094.1 GB/s over the touched lines; buffer at 0x409500000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 20.3918 ms, kernel 4.0289 ms, copy-out 0.0131 ms; source buffer at 0x4097c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 2.563e+04, copy 1.317e+05; multiplexed rows voided: 0

### route/f-den=10,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 67 passes per interval, 356.4 GB/s over the touched lines; buffer at 0x5172c0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9473 ms, kernel 0.0636 ms, copy-out 0.0148 ms; source buffer at 0x5173c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+08 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=10,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 338 passes per interval, 1809.1 GB/s over the touched lines; buffer at 0x544400000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 8 calls per interval; first call of an interval: copy-in 2.5432 ms, kernel 0.0636 ms, copy-out 0.0107 ms; source buffer at 0x544500000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 8 passes per interval, 362.9 GB/s over the touched lines; buffer at 0x4e2900000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 2.9350 ms, kernel 0.4741 ms, copy-out 0.0133 ms; source buffer at 0x4e2a00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 9.664e+08 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=hbm

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 43 passes per interval, 2041.7 GB/s over the touched lines; buffer at 0x5e3cc0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.5439 ms, kernel 0.4747 ms, copy-out 0.0138 ms; source buffer at 0x5e3d80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.641e+04; multiplexed rows voided: 0

### route/f-den=100,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 31; repeats alternated as drawn: yes
- direct route: 581 passes per interval, 311.9 GB/s over the touched lines; buffer at 0x40ff40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9117 ms, kernel 0.0135 ms, copy-out 0.0105 ms; source buffer at 0x410080000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+07 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=100,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 2058 passes per interval, 1103.7 GB/s over the touched lines; buffer at 0x450d00000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 8 calls per interval; first call of an interval: copy-in 2.5445 ms, kernel 0.0151 ms, copy-out 0.0111 ms; source buffer at 0x450e00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 31; repeats alternated as drawn: yes
- direct route: 2653 passes per interval, 142.0 GB/s over the touched lines; buffer at 0x55d980000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 8 calls per interval; first call of an interval: copy-in 2.9400 ms, kernel 0.0079 ms, copy-out 0.0153 ms; source buffer at 0x55dac0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+06 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm

- first variant A, seed 31; repeats alternated as drawn: yes
- direct route: 4834 passes per interval, 259.4 GB/s over the touched lines; buffer at 0x4d3b40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 8 calls per interval; first call of an interval: copy-in 2.5544 ms, kernel 0.0092 ms, copy-out 0.0164 ms; source buffer at 0x4d3c40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.641e+04; multiplexed rows voided: 0

### route/f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 31; repeats alternated as drawn: yes
- direct route: 15 passes per interval, 362.1 GB/s over the touched lines; buffer at 0x583580000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9110 ms, kernel 0.2638 ms, copy-out 0.0161 ms; source buffer at 0x583680000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 78 passes per interval, 2068.0 GB/s over the touched lines; buffer at 0x4ee840000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 8 calls per interval; first call of an interval: copy-in 2.5396 ms, kernel 0.2628 ms, copy-out 0.0117 ms; source buffer at 0x4ee900000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 31; repeats alternated as drawn: yes
- direct route: 9 passes per interval, 360.9 GB/s over the touched lines; buffer at 0x5dc640000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9350 ms, kernel 0.3916 ms, copy-out 0.0123 ms; source buffer at 0x5dc700000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.053e+08 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=hbm

- first variant A, seed 31; repeats alternated as drawn: yes
- direct route: 52 passes per interval, 2054.1 GB/s over the touched lines; buffer at 0x4dd700000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.5404 ms, kernel 0.3920 ms, copy-out 0.0105 ms; source buffer at 0x4dd7c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k3,placement=cpu

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 172.7 GB/s over the touched lines; buffer at 0x5dbd80000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 2.9132 ms, kernel 0.4737 ms, copy-out 0.0121 ms; source buffer at 0x5dbe80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k3,placement=hbm

- first variant A, seed 31; repeats alternated as drawn: yes
- direct route: 43 passes per interval, 1961.6 GB/s over the touched lines; buffer at 0x538e00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.5416 ms, kernel 0.4760 ms, copy-out 0.0132 ms; source buffer at 0x538f00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-order=2m,placement=cpu

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 375.8 GB/s over the touched lines; buffer at 0x549340000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 42.1141 ms, kernel 0.4800 ms, copy-out 0.0126 ms; source buffer at 0x5497c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.366e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 6.065e+05, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-order=2m,placement=hbm

- first variant A, seed 31; repeats alternated as drawn: yes
- direct route: 9 passes per interval, 821.8 GB/s over the touched lines; buffer at 0x4c0600000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 40.9787 ms, kernel 0.4820 ms, copy-out 0.0145 ms; source buffer at 0x4c0a80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 5.595e+05, copy 2.647e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-order=64k,placement=cpu

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 390.5 GB/s over the touched lines; buffer at 0x410400000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 42.1171 ms, kernel 0.4689 ms, copy-out 0.0160 ms; source buffer at 0x4108c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.383e+08 (34.1 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 2.281e+05, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-order=64k,placement=hbm

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 17 passes per interval, 1613.5 GB/s over the touched lines; buffer at 0x472d80000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 40.9773 ms, kernel 0.4683 ms, copy-out 0.0137 ms; source buffer at 0x473200000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 3.161e+05, copy 2.648e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 375.1 GB/s over the touched lines; buffer at 0x4d1740000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 42.1156 ms, kernel 0.4981 ms, copy-out 0.0128 ms; source buffer at 0x4d1c00000000
- AnonHugePages after population (kB): direct 16777216, copy 16777216; after the series: direct 16777216, copy 16777216
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 0, copy 531; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-size=512m,placement=hbm

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 42 passes per interval, 4178.2 GB/s over the touched lines; buffer at 0x4c3600000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 40.8784 ms, kernel 0.5005 ms, copy-out 0.0143 ms; source buffer at 0x4c3a80000000
- AnonHugePages after population (kB): direct 16777216, copy 16777216; after the series: direct 16777216, copy 16777216
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 532; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,partition=2g,placement=cpu

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 355.3 GB/s over the touched lines; buffer at 0x49a9c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 42.1137 ms, kernel 0.6785 ms, copy-out 0.0132 ms; source buffer at 0x49ae80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 2.752e+05, copy 2.621e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x561a40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 42.1141 ms, kernel 0.5119 ms, copy-out 0.0146 ms; source buffer at 0x561ec0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 1.211e+08, copy 2.621e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=hbm

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x57a840000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 40.9732 ms, kernel 0.5116 ms, copy-out 0.0121 ms; source buffer at 0x57ad00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.211e+08, copy 2.642e+05; multiplexed rows voided: 0

### route/footprint-mib=24576,kernel=k3,placement=cpu

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 3.4 GB/s over the touched lines; buffer at 0x48d2c0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 63.1639 ms, kernel 0.5178 ms, copy-out 0.0149 ms; source buffer at 0x48d940000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (33.4 per touched line), copy 2.585e+10; SMMU translation requests per repetition: direct 1.671e+08, copy 3.932e+05; multiplexed rows voided: 0

### route/footprint-mib=24576,kernel=k3,placement=hbm

- first variant A, seed 31; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 3.5 GB/s over the touched lines; buffer at 0x4d3e00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 61.5195 ms, kernel 0.5185 ms, copy-out 0.0133 ms; source buffer at 0x4d44c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.67e+08, copy 3.969e+05; multiplexed rows voided: 0

### route/footprint-mib=256,kernel=k3,placement=cpu

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 50.0 GB/s over the touched lines; buffer at 0x4ca4c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 17 calls per interval; first call of an interval: copy-in 0.7705 ms, kernel 0.4334 ms, copy-out 0.0131 ms; source buffer at 0x4ca580000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.368e+08 (256.0 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 0, copy 4106; multiplexed rows voided: 0

### route/footprint-mib=256,kernel=k3,placement=hbm

- first variant A, seed 31; repeats alternated as drawn: yes
- direct route: 46 passes per interval, 607.6 GB/s over the touched lines; buffer at 0x53ad00000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 19 calls per interval; first call of an interval: copy-in 0.6459 ms, kernel 0.4348 ms, copy-out 0.0120 ms; source buffer at 0x53ad80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 4105; multiplexed rows voided: 0

### route/footprint-mib=32768,kernel=k3,placement=cpu

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 3.0 GB/s over the touched lines; buffer at 0x5e17c0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 84.2123 ms, kernel 0.5248 ms, copy-out 0.0124 ms; source buffer at 0x5e2040000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (33.0 per touched line), copy 3.448e+10; SMMU translation requests per repetition: direct 1.912e+08, copy 5.243e+05; multiplexed rows voided: 0

### route/footprint-mib=4096,kernel=k3,placement=cpu

- first variant A, seed 31; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 304.3 GB/s over the touched lines; buffer at 0x5fdd80000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 10.5653 ms, kernel 0.4846 ms, copy-out 0.0130 ms; source buffer at 0x5fdf40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (40.7 per touched line), copy 4.295e+09; SMMU translation requests per repetition: direct 0, copy 6.555e+04; multiplexed rows voided: 0

### route/footprint-mib=4096,kernel=k3,placement=hbm

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 327.1 GB/s over the touched lines; buffer at 0x5a1940000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 10.1288 ms, kernel 0.4876 ms, copy-out 0.0122 ms; source buffer at 0x5a1b00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 6.555e+04; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu

- first variant A, seed 31; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 245.3 GB/s over the touched lines; buffer at 0x449200000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 21.0672 ms, kernel 0.5042 ms, copy-out 0.0135 ms; source buffer at 0x4494c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (36.2 per touched line), copy 8.607e+09; SMMU translation requests per repetition: direct 4082, copy 1.311e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=hbm

- first variant B, seed 31; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 245.1 GB/s over the touched lines; buffer at 0x5b5440000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 20.3987 ms, kernel 0.5041 ms, copy-out 0.0152 ms; source buffer at 0x5b56c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4240, copy 1.316e+05; multiplexed rows voided: 0

