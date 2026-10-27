# Factor cells: the direct route at a level of one factor against its home level, recomputed from raw rows

Times are per pass in ms. The factor effect on direct access is level minus home within a repeat, as median with its 95 % rank interval; a positive value means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | level | home ms | level ms | effect ms [interval] | relative to home | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|
| at=2m,footprint-mib=1024,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 5.3812 | 5.3567 | -0.0245 [-0.0250, -0.0237] | -0.5 % | 10 | yes | pass |
| at=2m,footprint-mib=1024,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 0.4652 | 0.3113 | -0.1540 [-0.1541, -0.1539] | -33.1 % | 10 | yes | pass |
| at=2m,footprint-mib=11520,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 240.0954 | 5.3708 | -234.7238 [-234.8314, -234.5995] | -97.8 % | 10 | yes | pass |
| at=2m,footprint-mib=12288,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 279.4028 | 5.3736 | -274.0293 [-274.1115, -273.9070] | -98.1 % | 10 | yes | pass |
| at=2m,footprint-mib=12288,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 283.7918 | 1.9590 | -281.8362 [-281.9790, -281.7125] | -99.3 % | 10 | yes | pass |
| at=2m,footprint-mib=1536,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 5.3817 | 5.3570 | -0.0246 [-0.0248, -0.0243] | -0.5 % | 10 | yes | pass |
| at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 433.0652 | 5.3780 | -427.6869 [-427.7450, -427.5671] | -98.8 % | 10 | yes | pass |
| at=2m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 425.1595 | 2.5266 | -422.6287 [-422.7807, -422.5189] | -99.4 % | 10 | yes | pass |
| at=2m,footprint-mib=2048,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 5.3822 | 5.3540 | -0.0282 [-0.0286, -0.0277] | -0.5 % | 10 | yes | pass |
| at=2m,footprint-mib=24576,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 597.5457 | 5.3875 | -592.1596 [-592.2243, -592.1135] | -99.1 % | 10 | yes | pass |
| at=2m,footprint-mib=256,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 5.3743 | 5.2902 | -0.0843 [-0.0866, -0.0816] | -1.6 % | 10 | yes | pass |
| at=2m,footprint-mib=256,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 0.4262 | 0.1663 | -0.2599 [-0.2600, -0.2596] | -61.0 % | 10 | yes | pass |
| at=2m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 684.0475 | 5.4367 | -678.6113 [-678.8000, -678.4759] | -99.2 % | 10 | yes | pass |
| at=2m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 5.5192 | 5.3533 | -0.1664 [-0.1762, -0.1485] | -3.0 % | 20 | yes | pass |
| at=2m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 5.1245 | 0.4277 | -4.6968 [-4.7002, -4.6935] | -91.7 % | 10 | yes | pass |
| at=2m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 7.8873 | 5.3601 | -2.5272 [-2.5285, -2.5254] | -32.0 % | 10 | yes | pass |
| at=2m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 7.8178 | 0.4762 | -7.3413 [-7.3456, -7.3382] | -93.9 % | 10 | yes | pass |
| at=2m,footprint-mib=9728,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 128.3379 | 5.3659 | -122.9726 [-123.1007, -122.9498] | -95.8 % | 10 | yes | pass |
| at=64k,footprint-mib=1024,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 5.3797 | 5.1231 | -0.2568 [-0.2605, -0.2528] | -4.8 % | 10 | yes | pass |
| at=64k,footprint-mib=1024,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 0.4653 | 0.2943 | -0.1708 [-0.1712, -0.1705] | -36.7 % | 10 | yes | pass |
| at=64k,footprint-mib=11520,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 240.1148 | 5.1828 | -234.9333 [-235.0613, -234.8329] | -97.8 % | 10 | yes | pass |
| at=64k,footprint-mib=12288,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 279.4403 | 5.1902 | -274.2508 [-274.3403, -274.1570] | -98.1 % | 10 | yes | pass |
| at=64k,footprint-mib=12288,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 282.8204 | 1.1826 | -281.6376 [-281.7781, -280.4718] | -99.6 % | 10 | yes | pass |
| at=64k,footprint-mib=1536,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 5.3808 | 5.1320 | -0.2493 [-0.2517, -0.2466] | -4.6 % | 10 | yes | pass |
| at=64k,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 433.0565 | 5.2131 | -427.8424 [-427.9268, -427.6258] | -98.8 % | 10 | yes | pass |
| at=64k,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 425.1389 | 1.6135 | -423.5243 [-423.6055, -423.4340] | -99.6 % | 10 | yes | pass |
| at=64k,footprint-mib=2048,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 5.3823 | 5.1280 | -0.2542 [-0.2556, -0.2527] | -4.7 % | 10 | yes | pass |
| at=64k,footprint-mib=24576,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 597.6299 | 5.2399 | -592.3908 [-592.4440, -592.3182] | -99.1 % | 10 | yes | pass |
| at=64k,footprint-mib=256,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 5.3749 | 5.0406 | -0.3340 [-0.3390, -0.3279] | -6.2 % | 10 | yes | pass |
| at=64k,footprint-mib=256,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 0.4272 | 0.1483 | -0.2790 [-0.2792, -0.2788] | -65.3 % | 10 | yes | pass |
| at=64k,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 684.0958 | 5.2610 | -678.8352 [-678.9614, -678.6938] | -99.2 % | 10 | yes | pass |
| at=64k,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 5.4671 | 5.1460 | -0.3231 [-0.3325, -0.3005] | -5.9 % | 10 | yes | pass |
| at=64k,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 5.1118 | 0.4112 | -4.7005 [-4.7031, -4.6975] | -92.0 % | 10 | yes | pass |
| at=64k,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 7.8881 | 5.1707 | -2.7171 [-2.7184, -2.7145] | -34.4 % | 10 | yes | pass |
| at=64k,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 7.8267 | 0.4441 | -7.3825 [-7.3866, -7.3779] | -94.3 % | 10 | yes | pass |
| at=64k,footprint-mib=9728,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 128.2910 | 5.1833 | -123.1089 [-123.1834, -123.0329] | -96.0 % | 10 | yes | pass |

## Per cell

### route/at=2m,footprint-mib=1024,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x596280000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x596340000000
- per repetition: home 5.368e+08 link read bytes and 0 SMMU translation requests; level 5.366e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=1024,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 44 passes per interval, cursor 0, buffer at 0x4e60c0000000; level: placement hbm, 65 passes per interval, cursor 0, buffer at 0x4e62c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=11520,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x599800000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x599b80000000
- per repetition: home 5.369e+08 link read bytes and 6.722e+07 SMMU translation requests; level 5.368e+08 link read bytes and 3.953e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=12288,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x592d00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5930c0000000
- per repetition: home 5.369e+08 link read bytes and 7.82e+07 SMMU translation requests; level 5.368e+08 link read bytes and 4.316e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=12288,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5f24c0000000; level: placement hbm, 11 passes per interval, cursor 0, buffer at 0x5f2840000000
- per repetition: home 0 link read bytes and 7.777e+07 SMMU translation requests; level 0 link read bytes and 4.452e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=1536,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x572500000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x572600000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.367e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x409d80000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x40a200000000
- per repetition: home 5.369e+08 link read bytes and 1.212e+08 SMMU translation requests; level 5.368e+08 link read bytes and 6.272e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x418580000000; level: placement hbm, 9 passes per interval, cursor 0, buffer at 0x418a40000000
- per repetition: home 0 link read bytes and 1.207e+08 SMMU translation requests; level 0 link read bytes and 5.695e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=2048,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x535d80000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x535ec0000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.368e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=24576,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x59ce80000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x59d540000000
- per repetition: home 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; level 5.368e+08 link read bytes and 1.138e+06 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=256,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x55d600000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x55d6c0000000
- per repetition: home 5.368e+08 link read bytes and 0 SMMU translation requests; level 5.355e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=256,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 47 passes per interval, cursor 0, buffer at 0x5949c0000000; level: placement hbm, 121 passes per interval, cursor 0, buffer at 0x594a80000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4d1340000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4d1c00000000
- per repetition: home 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; level 5.368e+08 link read bytes and 1.318e+06 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x497280000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x497400000000
- per repetition: home 5.369e+08 link read bytes and 72 SMMU translation requests; level 5.368e+08 link read bytes and 317.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x512840000000; level: placement hbm, 47 passes per interval, cursor 0, buffer at 0x512a00000000
- per repetition: home 0 link read bytes and 74 SMMU translation requests; level 0 link read bytes and 29.69 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x583f00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5841c0000000
- per repetition: home 5.369e+08 link read bytes and 4.422e+04 SMMU translation requests; level 5.368e+08 link read bytes and 6.634e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x41d940000000; level: placement hbm, 45 passes per interval, cursor 0, buffer at 0x41dc00000000
- per repetition: home 0 link read bytes and 4.423e+04 SMMU translation requests; level 0 link read bytes and 6851 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=9728,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4c0140000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4c0440000000
- per repetition: home 5.369e+08 link read bytes and 3.597e+07 SMMU translation requests; level 5.368e+08 link read bytes and 2.988e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=1024,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x49f540000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x49f640000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.355e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=1024,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 43 passes per interval, cursor 0, buffer at 0x57f740000000; level: placement hbm, 69 passes per interval, cursor 0, buffer at 0x57f840000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=11520,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x55b180000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x55b4c0000000
- per repetition: home 5.369e+08 link read bytes and 6.723e+07 SMMU translation requests; level 5.379e+08 link read bytes and 1.516e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=12288,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5ca980000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5cad40000000
- per repetition: home 5.369e+08 link read bytes and 7.821e+07 SMMU translation requests; level 5.381e+08 link read bytes and 1.866e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=12288,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x4bd0c0000000; level: placement hbm, 17 passes per interval, cursor 0, buffer at 0x4bd480000000
- per repetition: home 0 link read bytes and 7.777e+07 SMMU translation requests; level 0 link read bytes and 2.882e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=1536,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4d6fc0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4d70c0000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.356e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x57ccc0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x57d140000000
- per repetition: home 5.369e+08 link read bytes and 1.212e+08 SMMU translation requests; level 5.386e+08 link read bytes and 2.777e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x4be600000000; level: placement hbm, 13 passes per interval, cursor 0, buffer at 0x4beac0000000
- per repetition: home 0 link read bytes and 1.207e+08 SMMU translation requests; level 0 link read bytes and 3.955e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=2048,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5022c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x502400000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.357e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=24576,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x582640000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x582cc0000000
- per repetition: home 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; level 5.389e+08 link read bytes and 4.871e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=256,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x48c180000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x48c280000000
- per repetition: home 5.368e+08 link read bytes and 0 SMMU translation requests; level 5.354e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=256,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 47 passes per interval, cursor 0, buffer at 0x44d0c0000000; level: placement hbm, 135 passes per interval, cursor 0, buffer at 0x44d180000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5cfe40000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5d06c0000000
- per repetition: home 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; level 5.39e+08 link read bytes and 8.268e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x528580000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x528740000000
- per repetition: home 5.369e+08 link read bytes and 42.12 SMMU translation requests; level 5.363e+08 link read bytes and 92.75 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x45ec80000000; level: placement hbm, 49 passes per interval, cursor 0, buffer at 0x45ee40000000
- per repetition: home 0 link read bytes and 68 SMMU translation requests; level 0 link read bytes and 17.11 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x598280000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x598500000000
- per repetition: home 5.369e+08 link read bytes and 4.423e+04 SMMU translation requests; level 5.372e+08 link read bytes and 3.438e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x47d580000000; level: placement hbm, 46 passes per interval, cursor 0, buffer at 0x47d840000000
- per repetition: home 0 link read bytes and 4.423e+04 SMMU translation requests; level 0 link read bytes and 4363 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=9728,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x55e2c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x55e5c0000000
- per repetition: home 5.369e+08 link read bytes and 3.596e+07 SMMU translation requests; level 5.376e+08 link read bytes and 7.659e+04 SMMU translation requests; multiplexed rows voided: 0

