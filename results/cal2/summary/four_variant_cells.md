# Four-variant cells: direct and copy route at home and at a level of one factor, recomputed from raw rows

Times are per repetition in ms (one pass for the direct route, one complete call for the copy route). Each round runs the four variants once in the order the seed drew; the route difference at home (A - B) and at the level (C - D) and the change of the route difference, (C - D) - (A - B), are formed within each round and given as median with 95 % rank interval. A negative route difference means direct access is faster; a negative change means the level moved the comparison towards direct access. The relative change is the change over the route difference at home, given only where that difference excludes zero. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | level | direct home ms | copy home ms | direct level ms | copy level ms | route difference home ms [interval] | route difference level ms [interval] | change ms [interval] | relative change | rounds | change excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| at=16384,footprint-mib=1024,kernel=k3,placement=cpu,type=four,vary=footprint | footprint | 16384 | 5.3888 | 3.4139 | 433.3709 | 42.6430 | 1.9730 [1.9610, 1.9759] | 390.7155 [390.6330, 390.7399] | 388.7547 [388.7133, 388.8490] | +19703.8 % | 20 | yes | pass |
| at=16384,footprint-mib=1024,kernel=k3,placement=hbm,type=four,vary=footprint | footprint | 16384 | 0.4739 | 3.0252 | 427.4673 | 41.5040 | -2.5515 [-2.5529, -2.5506] | 385.9508 [385.7865, 386.0742] | 388.5027 [388.3393, 388.6249] | -15226.4 % | 10 | yes | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=f | f | 1of100 | 2.9301 | 3.4618 | 0.0348 | 2.7612 | -0.5321 [-0.5334, -0.5301] | -2.7265 [-2.7271, -2.7255] | -2.1943 [-2.1964, -2.1928] | +412.4 % | 10 | yes | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=four,vary=f | f | 1of100 | 0.5096 | 3.0648 | 0.0096 | 2.5596 | -2.5550 [-2.5555, -2.5546] | -2.5500 [-2.5501, -2.5497] | 0.0050 [0.0047, 0.0058] | -0.2 % | 100 | yes | pass |
| at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=partition | partition | 2g | 433.4327 | 42.6304 | 5.7113 | 42.8033 | 390.7995 [390.7356, 390.8795] | -37.0910 [-37.1054, -37.0766] | -427.8900 [-427.9933, -427.8123] | -109.5 % | 10 | yes | pass |
| at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-order | page-order | 2m | 433.4814 | 42.6379 | 5.3686 | 42.6130 | 390.8438 [390.7192, 390.9637] | -37.2449 [-37.2482, -37.2388] | -428.0886 [-428.1992, -427.9646] | -109.5 % | 10 | yes | pass |
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 433.2029 | 42.6380 | 5.3878 | 42.6344 | 390.5759 [390.4404, 390.7449] | -37.2488 [-37.2588, -37.2421] | -427.8199 [-427.9990, -427.6776] | -109.5 % | 10 | yes | pass |
| at=hbm,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=placement | placement | hbm | 2.9283 | 3.4495 | 0.5091 | 3.0569 | -0.5212 [-0.5234, -0.5197] | -2.5479 [-2.5489, -2.5459] | -2.0264 [-2.0286, -2.0247] | +388.8 % | 10 | yes | pass |
| at=off512m,footprint-mib=8192,kernel=k3,placement=cpu,type=four,vary=alignment | alignment | off512m | 7.8889 | 21.5845 | 48.4725 | 21.5888 | -13.6969 [-13.8296, -13.6953] | 26.6030 [26.4385, 26.8856] | 40.5269 [40.1411, 40.6478] | -295.9 % | 40 | yes | pass |

## Per cell

### route/at=16384,footprint-mib=1024,kernel=k3,placement=cpu,type=four,vary=footprint

- seed 37; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x504dc0000000, copy home 0x504f00000000, direct level 0x504fc0000000, copy level 0x505480000000
- factor effect within the cell: on the direct route 427.9831 [427.9468, 428.0819] ms, on the copy route 39.2303 [39.2197, 39.2340] ms; change relative to the copy call at home: +11387.5 %
- per repetition: direct home 5.369e+08 link read bytes and 4341 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.639e+04 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy level 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=16384,footprint-mib=1024,kernel=k3,placement=hbm,type=four,vary=footprint

- seed 37; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x564e40000000, copy home 0x564f40000000, direct level 0x565000000000, copy level 0x5654c0000000
- factor effect within the cell: on the direct route 426.9941 [426.8229, 427.0933] ms, on the copy route 38.4789 [38.4684, 38.4946] ms; change relative to the copy call at home: +12842.1 %
- per repetition: direct home 0 link read bytes and 404.7 SMMU translation requests; copy home 0 link read bytes and 1.641e+04 SMMU translation requests; direct level 0 link read bytes and 1.211e+08 SMMU translation requests; copy level 0 link read bytes and 2.646e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=f

- seed 37; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x54ebc0000000, copy home 0x54ecc0000000, direct level 0x54ed80000000, copy level 0x54ee40000000
- factor effect within the cell: on the direct route -2.8953 [-2.8955, -2.8946] ms, on the copy route -0.7005 [-0.7016, -0.6991] ms; change relative to the copy call at home: -63.4 %
- per repetition: direct home 1.074e+09 link read bytes and 0 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.639e+04 SMMU translation requests; direct level 1.074e+07 link read bytes and 0 SMMU translation requests; copy level 1.074e+09 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=four,vary=f

- seed 37; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x4bbac0000000, copy home 0x4bbbc0000000, direct level 0x4bbc80000000, copy level 0x4bbd40000000
- factor effect within the cell: on the direct route -0.5001 [-0.5002, -0.4999] ms, on the copy route -0.5052 [-0.5058, -0.5047] ms; change relative to the copy call at home: +0.2 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 1.643e+04 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=partition

- seed 37; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4c9100000000, copy home 0x4c9580000000, direct level 0x4c9a00000000, copy level 0x4c9ec0000000
- factor effect within the cell: on the direct route -427.7201 [-427.8063, -427.6347] ms, on the copy route 0.1745 [0.1577, 0.1864] ms; change relative to the copy call at home: -1003.7 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 2.817e+05 SMMU translation requests; copy level 1.723e+10 link read bytes and 2.621e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-order

- seed 37; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x41e940000000, copy home 0x41edc0000000, direct level 0x41f240000000, copy level 0x41f700000000
- factor effect within the cell: on the direct route -428.1137 [-428.2393, -427.9765] ms, on the copy route -0.0216 [-0.0362, -0.0120] ms; change relative to the copy call at home: -1004.0 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.621e+05 SMMU translation requests; direct level 5.366e+08 link read bytes and 6.129e+05 SMMU translation requests; copy level 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 37; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x54ac00000000, copy home 0x54b0c0000000, direct level 0x54b540000000, copy level 0x54ba00000000
- factor effect within the cell: on the direct route -427.8172 [-427.9859, -427.6951] ms, on the copy route 0.0001 [-0.0151, 0.0192] ms; change relative to the copy call at home: -1003.4 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.621e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 149.1 SMMU translation requests; copy level 1.723e+10 link read bytes and 524.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=hbm,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=placement

- seed 37; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement hbm; buffers: direct home 0x4e3c40000000, copy home 0x4e3d40000000, direct level 0x4e3e00000000, copy level 0x4e3ec0000000
- factor effect within the cell: on the direct route -2.4192 [-2.4204, -2.4184] ms, on the copy route -0.3926 [-0.3943, -0.3919] ms; change relative to the copy call at home: -58.7 %
- per repetition: direct home 1.074e+09 link read bytes and 0 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.64e+04 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=8192,kernel=k3,placement=cpu,type=four,vary=alignment

- seed 37; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4a3240000000, copy home 0x4a34c0000000, direct level 0x4a3820000000, copy level 0x4a4020000000
- factor effect within the cell: on the direct route 40.6023 [40.5616, 40.6700] ms, on the copy route 0.0044 [-0.0011, 0.0134] ms; change relative to the copy call at home: +187.8 %
- per repetition: direct home 5.369e+08 link read bytes and 4.399e+04 SMMU translation requests; copy home 8.607e+09 link read bytes and 1.311e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.368e+07 SMMU translation requests; copy level 8.607e+09 link read bytes and 1.311e+05 SMMU translation requests; multiplexed rows voided: 0

