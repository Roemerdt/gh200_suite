# Four-variant cells: direct and copy route at home and at a level of one factor, recomputed from raw rows

Times are per repetition in ms (one pass for the direct route, one complete call for the copy route). Each round runs the four variants once in the order the seed drew; the route difference at home (A - B) and at the level (C - D) and the change of the route difference, (C - D) - (A - B), are formed within each round and given as median with 95 % rank interval. A negative route difference means direct access is faster; a negative change means the level moved the comparison towards direct access. The relative change is the change over the route difference at home, given only where that difference excludes zero. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | level | direct home ms | copy home ms | direct level ms | copy level ms | route difference home ms [interval] | route difference level ms [interval] | change ms [interval] | relative change | rounds | change excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| at=none,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=tiling | tiling | none | 26.8783 | 6.4670 | 47.5869 | 6.4676 | 20.4113 [20.3744, 20.4284] | 41.1188 [40.9504, 41.1619] | 20.7028 [20.5376, 20.8002] | +101.4 % | 10 | yes | pass |
| at=plain,footprint-mib=1024,kernel=k6,placement=cpu,type=four,update=atomic,vary=update | update | plain | 6.1848 | 7.3750 | 5.9230 | 7.1018 | -1.1916 [-1.1948, -1.1839] | -1.1807 [-1.1862, -1.1715] | 0.0111 [-0.0033, 0.0252] | -0.9 % | 10 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 0.1929 | 0.2429 | 0.3807 | 0.4119 | -0.0501 [-0.0505, -0.0496] | -0.0319 [-0.0360, -0.0290] | 0.0180 [0.0142, 0.0215] | -35.9 % | 10 | yes | pass |

## Host phases

The CPU phase before every pass, timed on the CPU clock (ms per pass), and the state check's median load latency on the preparing core after the phase (ns per sampled load), per variant.

| cell | direct home CPU ms | direct home state ns | copy home CPU ms | copy home state ns | direct level CPU ms | direct level state ns | copy level CPU ms | copy level state ns |
|---|---|---|---|---|---|---|---|---|
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 2.7015 | 90.0 | 2.7144 | 106.1 | 2.7082 | 121.4 | 2.7691 | 114.4 |

## Per cell

### route/at=none,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=tiling

- seed 7; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x584ac0000000, copy home 0x584bc0000000, direct level 0x584c80000000, copy level 0x584d80000000
- factor effect within the cell: on the direct route 20.7058 [20.5373, 20.7976] ms, on the copy route 0.0017 [-0.0026, 0.0111] ms; change relative to the copy call at home: +320.1 %
- per repetition: direct home 6.422e+09 link read bytes and 3.633e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 1.352e+10 link read bytes and 2.697e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=1024,kernel=k6,placement=cpu,type=four,update=atomic,vary=update

- seed 7; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x4919c0000000, copy home 0x491a80000000, direct level 0x491b40000000, copy level 0x491c00000000
- factor effect within the cell: on the direct route -0.2601 [-0.2710, -0.2514] ms, on the copy route -0.2720 [-0.2772, -0.2678] ms; change relative to the copy call at home: +0.2 %
- per repetition: direct home 0 link read bytes and 4646 SMMU translation requests; copy home 1.074e+09 link read bytes and 3.278e+04 SMMU translation requests; direct level 1.074e+09 link read bytes and 4578 SMMU translation requests; copy level 1.074e+09 link read bytes and 3.278e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 7; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x43d780000000, copy home 0x43d800000000, direct level 0x43d880000000, copy level 0x43d900000000
- factor effect within the cell: on the direct route 0.1879 [0.1835, 0.1888] ms, on the copy route 0.1688 [0.1649, 0.1702] ms; change relative to the copy call at home: +7.4 %
- per repetition: direct home 6.711e+07 link read bytes and 2066 SMMU translation requests; copy home 6.711e+07 link read bytes and 1043 SMMU translation requests; direct level 6.711e+07 link read bytes and 1343 SMMU translation requests; copy level 6.711e+07 link read bytes and 1056 SMMU translation requests; multiplexed rows voided: 0

