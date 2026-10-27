# Factor cells: the direct route at a level of one factor against its home level, recomputed from raw rows

Times are per pass in ms. The factor effect on direct access is level minus home within a repeat, as median with its 95 % rank interval; a positive value means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | level | home ms | level ms | effect ms [interval] | relative to home | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|
| at=2m,footprint-mib=1024,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 5.3801 | 5.3569 | -0.0232 [-0.0242, -0.0229] | -0.4 % | 10 | yes | pass |
| at=2m,footprint-mib=1024,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 0.4655 | 0.3117 | -0.1537 [-0.1541, -0.1534] | -33.0 % | 10 | yes | pass |
| at=2m,footprint-mib=11520,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 240.1253 | 5.3707 | -234.7553 [-234.7878, -234.6536] | -97.8 % | 10 | yes | pass |
| at=2m,footprint-mib=12288,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 279.8513 | 5.3732 | -274.4780 [-274.5507, -274.3188] | -98.1 % | 10 | yes | pass |
| at=2m,footprint-mib=12288,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 276.0183 | 1.9631 | -274.0568 [-274.1996, -273.9836] | -99.3 % | 10 | yes | pass |
| at=2m,footprint-mib=1536,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 5.3813 | 5.3563 | -0.0251 [-0.0263, -0.0243] | -0.5 % | 10 | yes | pass |
| at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 433.6959 | 5.3776 | -428.3185 [-428.4103, -428.2255] | -98.8 % | 10 | yes | pass |
| at=2m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 425.1699 | 2.5127 | -422.6567 [-422.7035, -422.5662] | -99.4 % | 10 | yes | pass |
| at=2m,footprint-mib=2048,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 5.3833 | 5.3538 | -0.0295 [-0.0301, -0.0288] | -0.5 % | 10 | yes | pass |
| at=2m,footprint-mib=24576,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 598.4359 | 5.3867 | -593.0499 [-593.1818, -592.9537] | -99.1 % | 10 | yes | pass |
| at=2m,footprint-mib=256,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 5.3745 | 5.2856 | -0.0892 [-0.0904, -0.0858] | -1.7 % | 10 | yes | pass |
| at=2m,footprint-mib=256,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 0.4254 | 0.1676 | -0.2578 [-0.2580, -0.2577] | -60.6 % | 10 | yes | pass |
| at=2m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 685.1383 | 5.4263 | -679.7116 [-679.8548, -679.6535] | -99.2 % | 10 | yes | pass |
| at=2m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 5.4508 | 5.3546 | -0.0959 [-0.1052, -0.0867] | -1.8 % | 80 | yes | pass |
| at=2m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 5.1261 | 0.4273 | -4.6987 [-4.7019, -4.6961] | -91.7 % | 10 | yes | pass |
| at=2m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 7.8886 | 5.3587 | -2.5296 [-2.5318, -2.5288] | -32.1 % | 10 | yes | pass |
| at=2m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 7.8080 | 0.4750 | -7.3330 [-7.3398, -7.3255] | -93.9 % | 10 | yes | pass |
| at=2m,footprint-mib=9728,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 128.5156 | 5.3685 | -123.1475 [-123.2462, -123.0580] | -95.8 % | 10 | yes | pass |
| at=64k,footprint-mib=1024,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 5.3799 | 5.1209 | -0.2585 [-0.2616, -0.2562] | -4.8 % | 10 | yes | pass |
| at=64k,footprint-mib=1024,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 0.4655 | 0.2937 | -0.1718 [-0.1720, -0.1716] | -36.9 % | 10 | yes | pass |
| at=64k,footprint-mib=11520,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 240.0753 | 5.1886 | -234.8864 [-235.0073, -234.7861] | -97.8 % | 10 | yes | pass |
| at=64k,footprint-mib=12288,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 279.8150 | 5.1957 | -274.6174 [-274.6582, -274.4098] | -98.1 % | 10 | yes | pass |
| at=64k,footprint-mib=12288,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 283.1055 | 1.1807 | -281.9254 [-282.0085, -281.7877] | -99.6 % | 10 | yes | pass |
| at=64k,footprint-mib=1536,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 5.3812 | 5.1341 | -0.2472 [-0.2500, -0.2428] | -4.6 % | 10 | yes | pass |
| at=64k,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 433.5883 | 5.2116 | -428.3772 [-428.5305, -428.3196] | -98.8 % | 10 | yes | pass |
| at=64k,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 426.0132 | 1.6189 | -424.3941 [-424.4391, -424.3183] | -99.6 % | 10 | yes | pass |
| at=64k,footprint-mib=2048,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 5.3828 | 5.1133 | -0.2688 [-0.2701, -0.2661] | -5.0 % | 10 | yes | pass |
| at=64k,footprint-mib=24576,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 597.5031 | 5.2391 | -592.2648 [-592.3422, -592.1116] | -99.1 % | 10 | yes | pass |
| at=64k,footprint-mib=256,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 5.3747 | 5.0337 | -0.3408 [-0.3435, -0.3360] | -6.3 % | 10 | yes | pass |
| at=64k,footprint-mib=256,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 0.4262 | 0.1477 | -0.2784 [-0.2786, -0.2784] | -65.3 % | 10 | yes | pass |
| at=64k,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 685.1690 | 5.2529 | -679.9142 [-679.9865, -679.8652] | -99.2 % | 10 | yes | pass |
| at=64k,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 5.6020 | 5.1479 | -0.4553 [-0.4695, -0.4321] | -8.1 % | 10 | yes | pass |
| at=64k,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 5.1075 | 0.4105 | -4.6971 [-4.6999, -4.6914] | -92.0 % | 10 | yes | pass |
| at=64k,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 7.8886 | 5.1636 | -2.7247 [-2.7269, -2.7217] | -34.5 % | 10 | yes | pass |
| at=64k,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 7.8149 | 0.4450 | -7.3699 [-7.3766, -7.3656] | -94.3 % | 10 | yes | pass |
| at=64k,footprint-mib=9728,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 128.4912 | 5.1812 | -123.3106 [-123.4752, -123.2473] | -96.0 % | 10 | yes | pass |

## Per cell

### route/at=2m,footprint-mib=1024,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4519c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x451ac0000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.366e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=1024,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 43 passes per interval, cursor 0, buffer at 0x54e840000000; level: placement hbm, 65 passes per interval, cursor 0, buffer at 0x54e900000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=11520,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4b2640000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4b29c0000000
- per repetition: home 5.369e+08 link read bytes and 6.723e+07 SMMU translation requests; level 5.368e+08 link read bytes and 3.959e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=12288,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x418180000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x418500000000
- per repetition: home 5.369e+08 link read bytes and 7.821e+07 SMMU translation requests; level 5.368e+08 link read bytes and 4.303e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=12288,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x590bc0000000; level: placement hbm, 11 passes per interval, cursor 0, buffer at 0x590f40000000
- per repetition: home 0 link read bytes and 7.776e+07 SMMU translation requests; level 0 link read bytes and 4.437e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=1536,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x53e140000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x53e240000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.367e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x45da00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x45de80000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.368e+08 link read bytes and 6.328e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x562580000000; level: placement hbm, 9 passes per interval, cursor 0, buffer at 0x562a00000000
- per repetition: home 0 link read bytes and 1.207e+08 SMMU translation requests; level 0 link read bytes and 5.689e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=2048,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x535740000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x535880000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.368e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=24576,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x580580000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x580c40000000
- per repetition: home 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; level 5.368e+08 link read bytes and 1.123e+06 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=256,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x413440000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x413500000000
- per repetition: home 5.368e+08 link read bytes and 0 SMMU translation requests; level 5.355e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=256,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 48 passes per interval, cursor 0, buffer at 0x56c540000000; level: placement hbm, 120 passes per interval, cursor 0, buffer at 0x56c600000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x564440000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x564cc0000000
- per repetition: home 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; level 5.368e+08 link read bytes and 1.309e+06 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x581b40000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x581d00000000
- per repetition: home 5.369e+08 link read bytes and 68.25 SMMU translation requests; level 5.368e+08 link read bytes and 308 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x5d6780000000; level: placement hbm, 47 passes per interval, cursor 0, buffer at 0x5d6940000000
- per repetition: home 0 link read bytes and 74.12 SMMU translation requests; level 0 link read bytes and 38.49 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x4da000000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4da280000000
- per repetition: home 5.369e+08 link read bytes and 4.422e+04 SMMU translation requests; level 5.368e+08 link read bytes and 6.606e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x50eb40000000; level: placement hbm, 45 passes per interval, cursor 0, buffer at 0x50edc0000000
- per repetition: home 0 link read bytes and 4.431e+04 SMMU translation requests; level 0 link read bytes and 7268 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=9728,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x53d2c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x53d5c0000000
- per repetition: home 5.369e+08 link read bytes and 3.597e+07 SMMU translation requests; level 5.368e+08 link read bytes and 2.951e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=1024,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4c6800000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4c68c0000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.354e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=1024,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 43 passes per interval, cursor 0, buffer at 0x42bf00000000; level: placement hbm, 69 passes per interval, cursor 0, buffer at 0x42bfc0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=11520,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x457ac0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x457e00000000
- per repetition: home 5.369e+08 link read bytes and 6.721e+07 SMMU translation requests; level 5.378e+08 link read bytes and 1.427e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=12288,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x572900000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x572c80000000
- per repetition: home 5.369e+08 link read bytes and 7.82e+07 SMMU translation requests; level 5.382e+08 link read bytes and 1.846e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=12288,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x56e2c0000000; level: placement hbm, 18 passes per interval, cursor 0, buffer at 0x56e680000000
- per repetition: home 0 link read bytes and 7.777e+07 SMMU translation requests; level 0 link read bytes and 2.891e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=1536,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5b43c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5b44c0000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.355e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4fa600000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4faa80000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.386e+08 link read bytes and 2.787e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5acbc0000000; level: placement hbm, 13 passes per interval, cursor 0, buffer at 0x5ad080000000
- per repetition: home 0 link read bytes and 1.207e+08 SMMU translation requests; level 0 link read bytes and 3.98e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=2048,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x432f40000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x433040000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.356e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=24576,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x479280000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x479940000000
- per repetition: home 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; level 5.39e+08 link read bytes and 4.935e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=256,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x51db00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x51dc00000000
- per repetition: home 5.368e+08 link read bytes and 0 SMMU translation requests; level 5.35e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=256,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 47 passes per interval, cursor 0, buffer at 0x44c980000000; level: placement hbm, 136 passes per interval, cursor 0, buffer at 0x44ca40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5668c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x567140000000
- per repetition: home 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; level 5.39e+08 link read bytes and 8.245e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x55aa00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x55ab80000000
- per repetition: home 5.369e+08 link read bytes and 58.12 SMMU translation requests; level 5.364e+08 link read bytes and 137 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x5bcd00000000; level: placement hbm, 49 passes per interval, cursor 0, buffer at 0x5bce80000000
- per repetition: home 0 link read bytes and 56 SMMU translation requests; level 0 link read bytes and 17.61 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x590880000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x590b00000000
- per repetition: home 5.369e+08 link read bytes and 4.423e+04 SMMU translation requests; level 5.372e+08 link read bytes and 3.446e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x53a340000000; level: placement hbm, 46 passes per interval, cursor 0, buffer at 0x53a5c0000000
- per repetition: home 0 link read bytes and 4.425e+04 SMMU translation requests; level 0 link read bytes and 4363 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=9728,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4d13c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4d16c0000000
- per repetition: home 5.369e+08 link read bytes and 3.597e+07 SMMU translation requests; level 5.376e+08 link read bytes and 7.465e+04 SMMU translation requests; multiplexed rows voided: 0

