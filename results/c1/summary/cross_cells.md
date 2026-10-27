# Cross cells: the direct route at home, at a level of one factor, at a level of a second factor and at both, recomputed from raw rows

Times are per pass in ms. Each round runs the four variants once in the order the seed drew. The first factor's effect is given at the second factor's home (B - A) and at its level (D - C), with the change between them, (D - C) - (B - A), all formed within each round as median with 95 % rank interval; a positive effect means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor 1 | level 1 | factor 2 | level 2 | home ms | level 1 ms | level 2 ms | both ms | effect 1 at home [interval] | effect 1 at level 2 [interval] | change [interval] | effect 2 at home [interval] | rounds | change excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| at=2m,at2=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=cross,vary=page-order,vary2=page-size | page-order | 2m | page-size | 512m | 432.7855 | 5.3779 | 5.3863 | 5.3107 | -427.4081 [-427.5648, -427.2696] | -0.0756 [-0.0777, -0.0741] | 427.3317 [427.1931, 427.4887] | -427.3988 [-427.5560, -427.2624] | 10 | yes | pass |
| at=shared,at2=512m,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=cross,vary=sharing,vary2=page-size | sharing | shared | page-size | 512m | 7.2651 | 7.2388 | 0.1212 | 0.1960 | -0.0269 [-0.0479, -0.0242] | 0.0748 [0.0740, 0.0771] | 0.1031 [0.0998, 0.1235] | -7.1440 [-7.1477, -7.1432] | 10 | yes | pass |

## Per cell

### route/at=2m,at2=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=cross,vary=page-order,vary2=page-size

- seed 71; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no
- buffers: home 0x4f30c0000000, level 1 0x4f3580000000, level 2 0x4f3a00000000, both 0x4f3ec0000000; AnonHugePages (kB): 0, 0, 16777216, 16777216
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level1 5.368e+08 link read bytes and 6.273e+05 SMMU translation requests; level2 5.369e+08 link read bytes and 151.1 SMMU translation requests; both 5.368e+08 link read bytes and 1566 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,at2=512m,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=cross,vary=sharing,vary2=page-size

- seed 71; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no
- buffers: home 0x418b00000000, level 1 0x418fc0000000, level 2 0x419440000000, both 0x4198c0000000; AnonHugePages (kB): 0, 0, 16777216, 16777216
- per repetition: home 3.355e+07 link read bytes and 2.026e+06 SMMU translation requests; level1 3.355e+07 link read bytes and 2.018e+06 SMMU translation requests; level2 3.355e+07 link read bytes and 601.6 SMMU translation requests; both 3.355e+07 link read bytes and 438.7 SMMU translation requests; multiplexed rows voided: 0

