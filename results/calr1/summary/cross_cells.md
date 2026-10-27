# Cross cells: the direct route at home, at a level of one factor, at a level of a second factor and at both, recomputed from raw rows

Times are per pass in ms. Each round runs the four variants once in the order the seed drew. The first factor's effect is given at the second factor's home (B - A) and at its level (D - C), with the change between them, (D - C) - (B - A), all formed within each round as median with 95 % rank interval; a positive effect means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor 1 | level 1 | factor 2 | level 2 | home ms | level 1 ms | level 2 ms | both ms | effect 1 at home [interval] | effect 1 at level 2 [interval] | change [interval] | effect 2 at home [interval] | rounds | change excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| at=shared,at2=512m,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=cross,vary=sharing,vary2=page-size | sharing | shared | page-size | 512m | 7.2558 | 7.2426 | 0.1215 | 0.2010 | -0.0099 [-0.0164, 0.0057] | 0.0795 [0.0792, 0.0800] | 0.0896 [0.0732, 0.0963] | -7.1343 [-7.1359, -7.1333] | 100 | yes | pass |

## Per cell

### route/at=shared,at2=512m,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=cross,vary=sharing,vary2=page-size

- seed 61; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes
- buffers: home 0x42d400000000, level 1 0x42d8c0000000, level 2 0x42dd40000000, both 0x42e1c0000000; AnonHugePages (kB): 0, 0, 16777216, 16777216
- per repetition: home 3.355e+07 link read bytes and 2.024e+06 SMMU translation requests; level1 3.355e+07 link read bytes and 2.02e+06 SMMU translation requests; level2 3.355e+07 link read bytes and 600.8 SMMU translation requests; both 3.355e+07 link read bytes and 444.8 SMMU translation requests; multiplexed rows voided: 0

