# Four-variant cells: direct and copy route at home and at a level of one factor, recomputed from raw rows

Times are per repetition in ms (one pass for the direct route, one complete call for the copy route). Each round runs the four variants once in the order the seed drew; the route difference at home (A - B) and at the level (C - D) and the change of the route difference, (C - D) - (A - B), are formed within each round and given as median with 95 % rank interval. A negative route difference means direct access is faster; a negative change means the level moved the comparison towards direct access. The relative change is the change over the route difference at home, given only where that difference excludes zero. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | level | direct home ms | copy home ms | direct level ms | copy level ms | route difference home ms [interval] | route difference level ms [interval] | change ms [interval] | relative change | rounds | change excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=f | f | 1of100 | 2.6918 | 3.5055 | 0.0315 | 2.9636 | -0.7971 [-0.8130, -0.4783] | -2.9320 [-3.2287, -2.9305] | -2.4129 [-2.4570, -2.1562] | +302.7 % | 100 | yes | pass |
| at=hbm,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=placement | placement | hbm | 2.8742 | 3.1633 | 0.5123 | 3.0583 | -0.2898 [-0.3012, -0.2754] | -2.5459 [-2.5468, -2.5449] | -2.2552 [-2.2714, -2.2456] | +778.2 % | 20 | yes | pass |

## Per cell

### route/at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=f

- seed 23; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x56f940000000, copy home 0x56fa00000000, direct level 0x56fac0000000, copy level 0x56fb80000000
- factor effect within the cell: on the direct route -2.6603 [-2.6614, -2.6592] ms, on the copy route -0.2484 [-0.5039, -0.2036] ms; change relative to the copy call at home: -68.8 %
- per repetition: direct home 1.074e+09 link read bytes and 0 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.639e+04 SMMU translation requests; direct level 1.074e+07 link read bytes and 0 SMMU translation requests; copy level 1.074e+09 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=hbm,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=placement

- seed 23; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement hbm; buffers: direct home 0x4c93c0000000, copy home 0x4c9480000000, direct level 0x4c9540000000, copy level 0x4c9600000000
- factor effect within the cell: on the direct route -2.3623 [-2.3785, -2.3506] ms, on the copy route -0.1050 [-0.1064, -0.1047] ms; change relative to the copy call at home: -71.3 %
- per repetition: direct home 1.074e+09 link read bytes and 0 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.639e+04 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 1.644e+04 SMMU translation requests; multiplexed rows voided: 0

