# Four-variant cells: direct and copy route at home and at a level of one factor, recomputed from raw rows

Times are per repetition in ms (one pass for the direct route, one complete call for the copy route). Each round runs the four variants once in the order the seed drew; the route difference at home (A - B) and at the level (C - D) and the change of the route difference, (C - D) - (A - B), are formed within each round and given as median with 95 % rank interval. A negative route difference means direct access is faster; a negative change means the level moved the comparison towards direct access. The relative change is the change over the route difference at home, given only where that difference excludes zero. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | level | direct home ms | copy home ms | direct level ms | copy level ms | route difference home ms [interval] | route difference level ms [interval] | change ms [interval] | relative change | rounds | change excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 432.5230 | 42.6248 | 5.3887 | 42.6321 | 389.8924 [389.8077, 390.0249] | -37.2471 [-37.2559, -37.2331] | -427.1351 [-427.2807, -427.0467] | -109.6 % | 10 | yes | pass |

## Per cell

### route/at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 29; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x44b380000000, copy home 0x44b800000000, direct level 0x44bc80000000, copy level 0x44c140000000
- factor effect within the cell: on the direct route -427.1342 [-427.2601, -427.0560] ms, on the copy route 0.0091 [-0.0151, 0.0178] ms; change relative to the copy call at home: -1002.1 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.621e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 151.5 SMMU translation requests; copy level 1.723e+10 link read bytes and 531 SMMU translation requests; multiplexed rows voided: 0

