# Route cells: direct route against copy route, recomputed from raw rows

Times are per repetition in ms: one pass for the direct route, one complete call (copy-in, kernel, copy-out) for the copy route. The route difference is direct minus copy within a repeat, as median with its 95 % rank interval; a negative value means direct access is faster. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | direct ms | copy ms | route difference ms [interval] | relative to copy | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|
| alignment=off512m,footprint-mib=8192,kernel=k3,placement=cpu | 48.2172 | 21.5950 | 26.6045 [26.5644, 26.6321] | +123.2 % | 20 | yes | pass |
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 2.9278 | 5.1945 | -2.2676 [-2.2749, -2.2644] | -43.7 % | 30 | yes | pass |
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | 0.5099 | 3.0544 | -2.5443 [-2.5457, -2.5435] | -83.3 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=cpu | 44.8148 | 50.1357 | -5.3215 [-5.3341, -5.2968] | -10.6 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=hbm | 12.6703 | 49.0214 | -36.3547 [-36.3975, -36.3363] | -74.2 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=cpu | 66.4727 | 75.1958 | -8.7139 [-8.7376, -8.6992] | -11.6 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=hbm | 18.9957 | 73.5357 | -54.5507 [-54.5917, -54.5185] | -74.2 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu | 0.7378 | 0.9079 | -0.1701 [-0.1713, -0.1694] | -18.7 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm | 0.1316 | 0.7852 | -0.6535 [-0.6543, -0.6531] | -83.2 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=cpu | 88.1244 | 100.2715 | -12.1551 [-12.1707, -12.1323] | -12.1 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu | 11.7184 | 17.4285 | -5.7080 [-5.7462, -5.6972] | -32.8 % | 40 | yes | pass |
| f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=hbm | 2.0221 | 12.1537 | -10.1308 [-10.1341, -10.1261] | -83.4 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=cpu | 23.0328 | 25.0978 | -2.0692 [-2.0728, -2.0630] | -8.2 % | 20 | yes | pass |
| f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=hbm | 4.0937 | 24.4199 | -20.3250 [-20.3297, -20.3190] | -83.2 % | 10 | yes | pass |
| f-den=10,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 0.3016 | 3.0054 | -2.7038 [-2.7054, -2.7023] | -90.0 % | 10 | yes | pass |
| f-den=10,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | 0.0595 | 2.6109 | -2.5514 [-2.5523, -2.5508] | -97.7 % | 10 | yes | pass |
| f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=cpu | 2.6666 | 3.4170 | -0.7511 [-0.7527, -0.7476] | -22.0 % | 10 | yes | pass |
| f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=hbm | 0.4733 | 3.0185 | -2.5450 [-2.5460, -2.5432] | -84.3 % | 10 | yes | pass |
| f-den=100,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 0.0348 | 2.9586 | -2.9239 [-2.9256, -2.9212] | -98.8 % | 10 | yes | pass |
| f-den=100,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | 0.0096 | 2.5612 | -2.5516 [-2.5522, -2.5509] | -99.6 % | 10 | yes | pass |
| f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 0.0077 | 2.9590 | -2.9513 [-3.2551, -2.9505] | -99.7 % | 100 | yes | pass |
| f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | 0.0040 | 2.5604 | -2.5564 [-2.5575, -2.5559] | -99.8 % | 10 | yes | pass |
| f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 1.4830 | 3.1931 | -1.7102 [-1.7106, -1.7091] | -53.6 % | 10 | yes | pass |
| f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | 0.2597 | 2.8083 | -2.5487 [-2.5498, -2.5484] | -90.8 % | 10 | yes | pass |
| f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=cpu | 2.2328 | 3.3338 | -1.1010 [-1.1039, -1.0985] | -33.0 % | 10 | yes | pass |
| f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=hbm | 0.3926 | 2.9373 | -2.5448 [-2.5467, -2.5433] | -86.6 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k3,placement=cpu | 5.3727 | 3.4137 | 1.9588 [1.9563, 1.9620] | +57.4 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k3,placement=hbm | 0.4730 | 3.0197 | -2.5467 [-2.5482, -2.5457] | -84.3 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,page-order=2m,placement=cpu | 5.3708 | 42.6089 | -37.2388 [-37.2403, -37.2354] | -87.4 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,page-order=2m,placement=hbm | 2.4480 | 41.4473 | -39.0014 [-39.0087, -38.9961] | -94.1 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,page-order=64k,placement=cpu | 5.1884 | 42.5963 | -37.4063 [-37.4115, -37.4040] | -87.8 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,page-order=64k,placement=hbm | 1.2660 | 41.4827 | -40.2157 [-40.2201, -40.2034] | -96.9 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu | 5.3829 | 42.6331 | -37.2503 [-37.2647, -37.2449] | -87.4 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,page-size=512m,placement=hbm | 0.4831 | 41.4050 | -40.9220 [-40.9270, -40.9150] | -98.8 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,partition=2g,placement=cpu | 5.7112 | 42.8032 | -37.0963 [-37.1073, -37.0886] | -86.7 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,placement=cpu | 433.2711 | 42.6391 | 390.6282 [390.4556, 390.7453] | +916.1 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,placement=hbm | 427.5577 | 41.5243 | 386.0334 [385.9260, 386.1903] | +929.7 % | 10 | yes | pass |
| footprint-mib=24576,kernel=k3,placement=cpu | 598.0959 | 63.6917 | 534.4067 [534.2379, 534.4909] | +839.1 % | 10 | yes | pass |
| footprint-mib=24576,kernel=k3,placement=hbm | 592.4112 | 62.0915 | 530.3163 [530.2746, 530.3810] | +854.1 % | 10 | yes | pass |
| footprint-mib=256,kernel=k3,placement=cpu | 5.3644 | 1.2038 | 4.1606 [4.1595, 4.1618] | +345.6 % | 10 | yes | pass |
| footprint-mib=256,kernel=k3,placement=hbm | 0.4400 | 1.0820 | -0.6421 [-0.6432, -0.6406] | -59.3 % | 10 | yes | pass |
| footprint-mib=32768,kernel=k3,placement=cpu | 684.8393 | 84.7462 | 600.0939 [600.0179, 600.2317] | +708.1 % | 10 | yes | pass |
| footprint-mib=4096,kernel=k3,placement=cpu | 5.5041 | 15.9133 | -10.4152 [-10.4334, -10.3866] | -65.4 % | 20 | yes | pass |
| footprint-mib=4096,kernel=k3,placement=hbm | 5.1485 | 10.6070 | -5.4585 [-5.4606, -5.4565] | -51.5 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu | 7.7477 | 21.5865 | -13.8392 [-13.8446, -13.8370] | -64.1 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=hbm | 7.7407 | 20.9130 | -13.1716 [-13.1745, -13.1619] | -63.0 % | 10 | yes | pass |

## Per cell

### route/alignment=off512m,footprint-mib=8192,kernel=k3,placement=cpu

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 39.4 GB/s over the touched lines; buffer at 0x44ec20000000 (offset in its 16 GiB window: 536870912 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 21.0765 ms, kernel 0.5029 ms, copy-out 0.0144 ms; source buffer at 0x44f020000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (36.2 per touched line), copy 8.607e+09; SMMU translation requests per repetition: direct 1.358e+07, copy 1.311e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 37; repeats alternated as drawn: yes
- direct route: 8 passes per interval, 366.7 GB/s over the touched lines; buffer at 0x47ad00000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9299 ms, kernel 0.5116 ms, copy-out 0.0149 ms; source buffer at 0x47adc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+09 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 40 passes per interval, 2105.7 GB/s over the touched lines; buffer at 0x480000000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.5393 ms, kernel 0.5117 ms, copy-out 0.0127 ms; source buffer at 0x480100000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=cpu

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 383.4 GB/s over the touched lines; buffer at 0x46ed00000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 42.1111 ms, kernel 8.0102 ms, copy-out 0.0132 ms; source buffer at 0x46f180000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.718e+10 (128.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 5.915e+05, copy 2.621e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=hbm

- first variant B, seed 37; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 1355.9 GB/s over the touched lines; buffer at 0x54c100000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 40.9778 ms, kernel 8.0299 ms, copy-out 0.0167 ms; source buffer at 0x54c5c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 8.3e+05, copy 2.645e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=cpu

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 387.7 GB/s over the touched lines; buffer at 0x43fc80000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 63.1587 ms, kernel 12.0224 ms, copy-out 0.0128 ms; source buffer at 0x440340000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.577e+10 (128.0 per touched line), copy 2.585e+10; SMMU translation requests per repetition: direct 8.625e+05, copy 3.932e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=hbm

- first variant B, seed 37; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 1356.6 GB/s over the touched lines; buffer at 0x44c200000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 61.4822 ms, kernel 12.0389 ms, copy-out 0.0134 ms; source buffer at 0x44c8c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.247e+06, copy 3.966e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu

- first variant B, seed 37; repeats alternated as drawn: yes
- direct route: 28 passes per interval, 363.8 GB/s over the touched lines; buffer at 0x5c8dc0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 23 calls per interval; first call of an interval: copy-in 0.7687 ms, kernel 0.1357 ms, copy-out 0.0132 ms; source buffer at 0x5c8ec0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.684e+08 (128.0 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 0, copy 4106; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm

- first variant B, seed 37; repeats alternated as drawn: yes
- direct route: 153 passes per interval, 2039.7 GB/s over the touched lines; buffer at 0x5f2740000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 26 calls per interval; first call of an interval: copy-in 0.6454 ms, kernel 0.1367 ms, copy-out 0.0155 ms; source buffer at 0x5f2800000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 4105; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=cpu

- first variant B, seed 37; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 389.9 GB/s over the touched lines; buffer at 0x464740000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 84.2092 ms, kernel 16.0390 ms, copy-out 0.0144 ms; source buffer at 0x465000000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.436e+10 (128.0 per touched line), copy 3.448e+10; SMMU translation requests per repetition: direct 1.133e+06, copy 5.243e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 366.5 GB/s over the touched lines; buffer at 0x595240000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 10.5574 ms, kernel 2.0096 ms, copy-out 0.0140 ms; source buffer at 0x5953c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 4.295e+09 (128.0 per touched line), copy 4.295e+09; SMMU translation requests per repetition: direct 0, copy 6.555e+04; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=hbm

- first variant B, seed 37; repeats alternated as drawn: yes
- direct route: 10 passes per interval, 2124.1 GB/s over the touched lines; buffer at 0x57ebc0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 10.1229 ms, kernel 2.0207 ms, copy-out 0.0120 ms; source buffer at 0x57ed40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 6.555e+04; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=cpu

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 372.9 GB/s over the touched lines; buffer at 0x4a80c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 21.0675 ms, kernel 4.0141 ms, copy-out 0.0134 ms; source buffer at 0x4a8340000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.59e+09 (128.0 per touched line), copy 8.607e+09; SMMU translation requests per repetition: direct 5.384e+04, copy 1.311e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=hbm

- first variant B, seed 37; repeats alternated as drawn: yes
- direct route: 5 passes per interval, 2098.3 GB/s over the touched lines; buffer at 0x41b7c0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 20.3817 ms, kernel 4.0214 ms, copy-out 0.0147 ms; source buffer at 0x41ba40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 2.658e+04, copy 1.314e+05; multiplexed rows voided: 0

### route/f-den=10,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 37; repeats alternated as drawn: yes
- direct route: 67 passes per interval, 356.0 GB/s over the touched lines; buffer at 0x59ac80000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9395 ms, kernel 0.0643 ms, copy-out 0.0117 ms; source buffer at 0x59ad80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+08 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=10,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm

- first variant B, seed 37; repeats alternated as drawn: yes
- direct route: 338 passes per interval, 1804.3 GB/s over the touched lines; buffer at 0x41bcc0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 8 calls per interval; first call of an interval: copy-in 2.5455 ms, kernel 0.0646 ms, copy-out 0.0163 ms; source buffer at 0x41be00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.641e+04; multiplexed rows voided: 0

### route/f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 8 passes per interval, 362.4 GB/s over the touched lines; buffer at 0x532e40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 2.9388 ms, kernel 0.4740 ms, copy-out 0.0129 ms; source buffer at 0x532f40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 9.664e+08 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=hbm

- first variant B, seed 37; repeats alternated as drawn: yes
- direct route: 43 passes per interval, 2041.7 GB/s over the touched lines; buffer at 0x4940c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.5398 ms, kernel 0.4746 ms, copy-out 0.0133 ms; source buffer at 0x4941c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=100,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 582 passes per interval, 308.9 GB/s over the touched lines; buffer at 0x580c80000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9432 ms, kernel 0.0153 ms, copy-out 0.0108 ms; source buffer at 0x580d80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+07 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=100,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm

- first variant B, seed 37; repeats alternated as drawn: yes
- direct route: 2058 passes per interval, 1119.2 GB/s over the touched lines; buffer at 0x5cd400000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 8 calls per interval; first call of an interval: copy-in 2.5564 ms, kernel 0.0146 ms, copy-out 0.0109 ms; source buffer at 0x5cd540000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.641e+04; multiplexed rows voided: 0

### route/f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 37; repeats alternated as drawn: yes
- direct route: 2653 passes per interval, 140.1 GB/s over the touched lines; buffer at 0x459480000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 8 calls per interval; first call of an interval: copy-in 2.9433 ms, kernel 0.0088 ms, copy-out 0.0152 ms; source buffer at 0x459540000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+06 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 4834 passes per interval, 270.8 GB/s over the touched lines; buffer at 0x42e0c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 8 calls per interval; first call of an interval: copy-in 2.5549 ms, kernel 0.0090 ms, copy-out 0.0162 ms; source buffer at 0x42e200000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.642e+04; multiplexed rows voided: 0

### route/f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 15 passes per interval, 362.0 GB/s over the touched lines; buffer at 0x4adb00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9280 ms, kernel 0.2618 ms, copy-out 0.0146 ms; source buffer at 0x4adc00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 78 passes per interval, 2067.4 GB/s over the touched lines; buffer at 0x596e00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 8 calls per interval; first call of an interval: copy-in 2.5421 ms, kernel 0.2627 ms, copy-out 0.0145 ms; source buffer at 0x596f00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 37; repeats alternated as drawn: yes
- direct route: 9 passes per interval, 360.7 GB/s over the touched lines; buffer at 0x5bafc0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9337 ms, kernel 0.3935 ms, copy-out 0.0147 ms; source buffer at 0x5bb080000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.053e+08 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=hbm

- first variant B, seed 37; repeats alternated as drawn: yes
- direct route: 52 passes per interval, 2051.2 GB/s over the touched lines; buffer at 0x4bc140000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.5406 ms, kernel 0.3936 ms, copy-out 0.0149 ms; source buffer at 0x4bc200000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k3,placement=cpu

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 172.8 GB/s over the touched lines; buffer at 0x433cc0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 2.9359 ms, kernel 0.4736 ms, copy-out 0.0118 ms; source buffer at 0x433dc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.368e+08 (74.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k3,placement=hbm

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 43 passes per interval, 1962.7 GB/s over the touched lines; buffer at 0x4dc1c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.5406 ms, kernel 0.4735 ms, copy-out 0.0114 ms; source buffer at 0x4dc2c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-order=2m,placement=cpu

- first variant B, seed 37; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 375.9 GB/s over the touched lines; buffer at 0x54d500000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 42.1116 ms, kernel 0.4815 ms, copy-out 0.0137 ms; source buffer at 0x54d980000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.366e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 6.104e+05, copy 2.621e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-order=2m,placement=hbm

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 9 passes per interval, 824.7 GB/s over the touched lines; buffer at 0x4a4300000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 40.9517 ms, kernel 0.4825 ms, copy-out 0.0125 ms; source buffer at 0x4a4780000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 5.568e+05, copy 2.639e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-order=64k,placement=cpu

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 389.1 GB/s over the touched lines; buffer at 0x472300000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 42.1144 ms, kernel 0.4683 ms, copy-out 0.0111 ms; source buffer at 0x472780000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.382e+08 (34.1 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 2.292e+05, copy 2.621e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-order=64k,placement=hbm

- first variant B, seed 37; repeats alternated as drawn: yes
- direct route: 17 passes per interval, 1594.7 GB/s over the touched lines; buffer at 0x5f09c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 40.9958 ms, kernel 0.4674 ms, copy-out 0.0138 ms; source buffer at 0x5f0e40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 3.213e+05, copy 2.648e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 375.0 GB/s over the touched lines; buffer at 0x54d700000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 42.1163 ms, kernel 0.5004 ms, copy-out 0.0150 ms; source buffer at 0x54dbc0000000
- AnonHugePages after population (kB): direct 16777216, copy 16777216; after the series: direct 16777216, copy 16777216
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 0, copy 516; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-size=512m,placement=hbm

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 42 passes per interval, 4178.7 GB/s over the touched lines; buffer at 0x455500000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 40.8909 ms, kernel 0.4996 ms, copy-out 0.0123 ms; source buffer at 0x4559c0000000
- AnonHugePages after population (kB): direct 16777216, copy 16777216; after the series: direct 16777216, copy 16777216
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 519; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,partition=2g,placement=cpu

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 353.5 GB/s over the touched lines; buffer at 0x44e080000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 42.1130 ms, kernel 0.6763 ms, copy-out 0.0129 ms; source buffer at 0x44e500000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 2.712e+05, copy 2.621e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu

- first variant B, seed 37; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x574540000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 42.1132 ms, kernel 0.5108 ms, copy-out 0.0145 ms; source buffer at 0x5749c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 1.211e+08, copy 2.621e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=hbm

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x52c300000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 40.9951 ms, kernel 0.5128 ms, copy-out 0.0132 ms; source buffer at 0x52c7c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.211e+08, copy 2.647e+05; multiplexed rows voided: 0

### route/footprint-mib=24576,kernel=k3,placement=cpu

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 3.4 GB/s over the touched lines; buffer at 0x4c3b00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 63.1600 ms, kernel 0.5166 ms, copy-out 0.0138 ms; source buffer at 0x4c4180000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (33.4 per touched line), copy 2.585e+10; SMMU translation requests per repetition: direct 1.671e+08, copy 3.932e+05; multiplexed rows voided: 0

### route/footprint-mib=24576,kernel=k3,placement=hbm

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 3.5 GB/s over the touched lines; buffer at 0x5bbf00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 61.5548 ms, kernel 0.5175 ms, copy-out 0.0155 ms; source buffer at 0x5bc5c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.671e+08, copy 3.974e+05; multiplexed rows voided: 0

### route/footprint-mib=256,kernel=k3,placement=cpu

- first variant B, seed 37; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 50.0 GB/s over the touched lines; buffer at 0x59ee40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 17 calls per interval; first call of an interval: copy-in 0.7679 ms, kernel 0.4329 ms, copy-out 0.0147 ms; source buffer at 0x59ef00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.368e+08 (256.0 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 0, copy 4106; multiplexed rows voided: 0

### route/footprint-mib=256,kernel=k3,placement=hbm

- first variant B, seed 37; repeats alternated as drawn: yes
- direct route: 46 passes per interval, 609.9 GB/s over the touched lines; buffer at 0x45f680000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 19 calls per interval; first call of an interval: copy-in 0.6459 ms, kernel 0.4351 ms, copy-out 0.0125 ms; source buffer at 0x45f740000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 4106; multiplexed rows voided: 0

### route/footprint-mib=32768,kernel=k3,placement=cpu

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 3.0 GB/s over the touched lines; buffer at 0x51db00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 84.2077 ms, kernel 0.5220 ms, copy-out 0.0144 ms; source buffer at 0x51e380000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (33.0 per touched line), copy 3.448e+10; SMMU translation requests per repetition: direct 1.912e+08, copy 5.243e+05; multiplexed rows voided: 0

### route/footprint-mib=4096,kernel=k3,placement=cpu

- first variant B, seed 37; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 307.1 GB/s over the touched lines; buffer at 0x56c8c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 10.5655 ms, kernel 0.4860 ms, copy-out 0.0147 ms; source buffer at 0x56ca40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (40.7 per touched line), copy 4.295e+09; SMMU translation requests per repetition: direct 0, copy 6.555e+04; multiplexed rows voided: 0

### route/footprint-mib=4096,kernel=k3,placement=hbm

- first variant B, seed 37; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 328.3 GB/s over the touched lines; buffer at 0x52c880000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 10.1130 ms, kernel 0.4857 ms, copy-out 0.0140 ms; source buffer at 0x52ca40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 6.555e+04; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 245.2 GB/s over the touched lines; buffer at 0x582400000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 21.0665 ms, kernel 0.5042 ms, copy-out 0.0137 ms; source buffer at 0x5826c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (36.2 per touched line), copy 8.607e+09; SMMU translation requests per repetition: direct 4165, copy 1.311e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=hbm

- first variant A, seed 37; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 245.5 GB/s over the touched lines; buffer at 0x5f4c40000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 20.3910 ms, kernel 0.5035 ms, copy-out 0.0156 ms; source buffer at 0x5f4ec0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4131, copy 1.314e+05; multiplexed rows voided: 0

