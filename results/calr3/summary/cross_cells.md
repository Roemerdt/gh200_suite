# Cross cells: the direct route at home, at a level of one factor, at a level of a second factor and at both, recomputed from raw rows

Times are per pass in ms. Each round runs the four variants once in the order the seed drew. The first factor's effect is given at the second factor's home (B - A) and at its level (D - C), with the change between them, (D - C) - (B - A), all formed within each round as median with 95 % rank interval; a positive effect means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor 1 | level 1 | factor 2 | level 2 | home ms | level 1 ms | level 2 ms | both ms | effect 1 at home [interval] | effect 1 at level 2 [interval] | change [interval] | effect 2 at home [interval] | rounds | change excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| at=shared,at2=512m,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=cross,vary=sharing,vary2=page-size | sharing | shared | page-size | 512m | 7.2627 | 7.2203 | 0.1216 | 0.1959 | -0.0426 [-0.0474, -0.0368] | 0.0744 [0.0738, 0.0747] | 0.1165 [0.1107, 0.1219] | -7.1411 [-7.1414, -7.1407] | 100 | yes | pass |

## Per cell

### route/at=shared,at2=512m,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=cross,vary=sharing,vary2=page-size

- seed 61; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes
- buffers: home 0x544280000000, level 1 0x544740000000, level 2 0x544bc0000000, both 0x545040000000; AnonHugePages (kB): 0, 0, 16777216, 16777216
- per repetition: home 3.355e+07 link read bytes and 2.026e+06 SMMU translation requests; level1 3.355e+07 link read bytes and 2.014e+06 SMMU translation requests; level2 3.355e+07 link read bytes and 600.3 SMMU translation requests; both 3.355e+07 link read bytes and 396.6 SMMU translation requests; multiplexed rows voided: 0

