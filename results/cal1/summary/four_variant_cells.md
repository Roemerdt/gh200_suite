# Four-variant cells: direct and copy route at home and at a level of one factor, recomputed from raw rows

Times are per repetition in ms (one pass for the direct route, one complete call for the copy route). Each round runs the four variants once in the order the seed drew; the route difference at home (A - B) and at the level (C - D) and the change of the route difference, (C - D) - (A - B), are formed within each round and given as median with 95 % rank interval. A negative route difference means direct access is faster; a negative change means the level moved the comparison towards direct access. The relative change is the change over the route difference at home, given only where that difference excludes zero. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | level | direct home ms | copy home ms | direct level ms | copy level ms | route difference home ms [interval] | route difference level ms [interval] | change ms [interval] | relative change | rounds | change excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| at=16384,footprint-mib=1024,kernel=k3,placement=cpu,type=four,vary=footprint | footprint | 16384 | 5.3882 | 3.4099 | 433.3428 | 42.6416 | 1.9776 [1.9653, 1.9795] | 390.7082 [390.5477, 390.8451] | 388.7377 [388.5708, 388.8669] | +19657.3 % | 10 | yes | pass |
| at=16384,footprint-mib=1024,kernel=k3,placement=hbm,type=four,vary=footprint | footprint | 16384 | 0.4754 | 3.0244 | 427.5682 | 41.5311 | -2.5490 [-2.5510, -2.5478] | 386.0234 [385.8484, 386.1097] | 388.5741 [388.4015, 388.6575] | -15244.1 % | 10 | yes | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=f | f | 1of100 | 2.9298 | 4.5183 | 0.0352 | 2.7655 | -1.5889 [-1.6029, -1.5836] | -2.7303 [-2.7307, -2.7297] | -1.1413 [-1.1523, -1.1356] | +71.8 % | 30 | yes | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=four,vary=f | f | 1of100 | 0.5097 | 3.0581 | 0.0096 | 2.5597 | -2.5483 [-2.5486, -2.5481] | -2.5501 [-2.5504, -2.5498] | -0.0018 [-0.0022, -0.0016] | +0.1 % | 100 | yes | pass |
| at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=partition | partition | 2g | 433.4181 | 42.6403 | 5.6861 | 42.7996 | 390.7782 [390.6605, 390.9219] | -37.1171 [-37.1220, -37.1047] | -427.8989 [-428.0380, -427.7727] | -109.5 % | 10 | yes | pass |
| at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-order | page-order | 2m | 433.4140 | 42.6417 | 5.3660 | 42.6128 | 390.7603 [390.5341, 390.8873] | -37.2473 [-37.2529, -37.2404] | -428.0011 [-428.1306, -427.7870] | -109.5 % | 10 | yes | pass |
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 433.2457 | 42.6282 | 5.3871 | 42.6336 | 390.6139 [390.5405, 390.8140] | -37.2494 [-37.2606, -37.2385] | -427.8886 [-428.0646, -427.7908] | -109.5 % | 10 | yes | pass |
| at=hbm,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=placement | placement | hbm | 2.9286 | 3.4417 | 0.5114 | 3.0557 | -0.5130 [-0.5154, -0.5122] | -2.5443 [-2.5457, -2.5434] | -2.0312 [-2.0322, -2.0299] | +395.9 % | 20 | yes | pass |
| at=off512m,footprint-mib=8192,kernel=k3,placement=cpu,type=four,vary=alignment | alignment | off512m | 7.8889 | 21.5801 | 48.5667 | 21.5856 | -13.6907 [-13.7029, -13.6873] | 26.9795 [26.5927, 27.0369] | 40.6758 [40.2949, 40.7549] | -297.1 % | 10 | yes | pass |

## Per cell

### route/at=16384,footprint-mib=1024,kernel=k3,placement=cpu,type=four,vary=footprint

- seed 31; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x445c00000000, copy home 0x445cc0000000, direct level 0x445d80000000, copy level 0x446280000000
- factor effect within the cell: on the direct route 427.9629 [427.8013, 428.1016] ms, on the copy route 39.2299 [39.2156, 39.2355] ms; change relative to the copy call at home: +11400.1 %
- per repetition: direct home 5.369e+08 link read bytes and 4372 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.64e+04 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy level 1.723e+10 link read bytes and 2.621e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=16384,footprint-mib=1024,kernel=k3,placement=hbm,type=four,vary=footprint

- seed 31; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x505680000000, copy home 0x505780000000, direct level 0x505840000000, copy level 0x505d00000000
- factor effect within the cell: on the direct route 427.0935 [426.8999, 427.1798] ms, on the copy route 38.5065 [38.4968, 38.5223] ms; change relative to the copy call at home: +12848.1 %
- per repetition: direct home 0 link read bytes and 405.8 SMMU translation requests; copy home 0 link read bytes and 1.642e+04 SMMU translation requests; direct level 0 link read bytes and 1.211e+08 SMMU translation requests; copy level 0 link read bytes and 2.655e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=f

- seed 31; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x50b040000000, copy home 0x50b140000000, direct level 0x50b200000000, copy level 0x50b2c0000000
- factor effect within the cell: on the direct route -2.8945 [-2.8955, -2.8939] ms, on the copy route -1.7520 [-1.7591, -1.7443] ms; change relative to the copy call at home: -25.3 %
- per repetition: direct home 1.074e+09 link read bytes and 0 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.64e+04 SMMU translation requests; direct level 1.074e+07 link read bytes and 0 SMMU translation requests; copy level 1.074e+09 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=four,vary=f

- seed 31; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x53eec0000000, copy home 0x53efc0000000, direct level 0x53f080000000, copy level 0x53f140000000
- factor effect within the cell: on the direct route -0.5000 [-0.5002, -0.5000] ms, on the copy route -0.4982 [-0.4985, -0.4980] ms; change relative to the copy call at home: -0.1 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 1.64e+04 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 1.641e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=partition

- seed 31; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5b5140000000, copy home 0x5b5600000000, direct level 0x5b5a80000000, copy level 0x5b5f40000000
- factor effect within the cell: on the direct route -427.7334 [-427.8808, -427.5990] ms, on the copy route 0.1594 [0.1562, 0.1737] ms; change relative to the copy call at home: -1003.5 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 2.713e+05 SMMU translation requests; copy level 1.723e+10 link read bytes and 2.621e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-order

- seed 31; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4635c0000000, copy home 0x463a80000000, direct level 0x463f00000000, copy level 0x4643c0000000
- factor effect within the cell: on the direct route -428.0484 [-428.1694, -427.8915] ms, on the copy route -0.0308 [-0.0422, -0.0088] ms; change relative to the copy call at home: -1003.7 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; direct level 5.366e+08 link read bytes and 6.101e+05 SMMU translation requests; copy level 1.723e+10 link read bytes and 2.621e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 31; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4217c0000000, copy home 0x421c80000000, direct level 0x422100000000, copy level 0x4225c0000000
- factor effect within the cell: on the direct route -427.8610 [-428.0620, -427.7888] ms, on the copy route 0.0050 [-0.0130, 0.0189] ms; change relative to the copy call at home: -1003.8 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.621e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 148.5 SMMU translation requests; copy level 1.723e+10 link read bytes and 515.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=hbm,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=placement

- seed 31; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement hbm; buffers: direct home 0x4dc600000000, copy home 0x4dc6c0000000, direct level 0x4dc780000000, copy level 0x4dc840000000
- factor effect within the cell: on the direct route -2.4173 [-2.4177, -2.4164] ms, on the copy route -0.3863 [-0.3876, -0.3848] ms; change relative to the copy call at home: -59.0 %
- per repetition: direct home 1.074e+09 link read bytes and 0 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.64e+04 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 1.641e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=8192,kernel=k3,placement=cpu,type=four,vary=alignment

- seed 31; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4a2480000000, copy home 0x4a2740000000, direct level 0x4a2c20000000, copy level 0x4a3420000000
- factor effect within the cell: on the direct route 40.6781 [40.2846, 40.7607] ms, on the copy route 0.0051 [-0.0103, 0.0119] ms; change relative to the copy call at home: +188.5 %
- per repetition: direct home 5.369e+08 link read bytes and 4.401e+04 SMMU translation requests; copy home 8.607e+09 link read bytes and 1.311e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.368e+07 SMMU translation requests; copy level 8.607e+09 link read bytes and 1.311e+05 SMMU translation requests; multiplexed rows voided: 0

