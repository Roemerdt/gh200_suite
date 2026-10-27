# Cross cells: the direct route at home, at a level of one factor, at a level of a second factor and at both, recomputed from raw rows

Times are per pass in ms. Each round runs the four variants once in the order the seed drew. The first factor's effect is given at the second factor's home (B - A) and at its level (D - C), with the change between them, (D - C) - (B - A), all formed within each round as median with 95 % rank interval; a positive effect means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor 1 | level 1 | factor 2 | level 2 | home ms | level 1 ms | level 2 ms | both ms | effect 1 at home [interval] | effect 1 at level 2 [interval] | change [interval] | effect 2 at home [interval] | rounds | change excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| at=2m,at2=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=cross,vary=page-order,vary2=page-size | page-order | 2m | page-size | 512m | 433.5251 | 5.3783 | 5.3844 | 5.3038 | -428.1472 [-428.3446, -428.0862] | -0.0808 [-0.0822, -0.0786] | 428.0705 [428.0045, 428.2647] | -428.1424 [-428.3377, -428.0811] | 10 | yes | pass |
| at=shared,at2=512m,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=cross,vary=sharing,vary2=page-size | sharing | shared | page-size | 512m | 7.2658 | 7.2320 | 0.1220 | 0.2002 | -0.0287 [-0.0423, -0.0106] | 0.0781 [0.0771, 0.0796] | 0.1065 [0.0901, 0.1205] | -7.1437 [-7.1463, -7.1382] | 10 | yes | pass |

## Per cell

### route/at=2m,at2=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=cross,vary=page-order,vary2=page-size

- seed 73; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no
- buffers: home 0x484400000000, level 1 0x484880000000, level 2 0x484d00000000, both 0x4851c0000000; AnonHugePages (kB): 0, 0, 16777216, 16777216
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level1 5.368e+08 link read bytes and 6.317e+05 SMMU translation requests; level2 5.369e+08 link read bytes and 149 SMMU translation requests; both 5.368e+08 link read bytes and 1576 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,at2=512m,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=cross,vary=sharing,vary2=page-size

- seed 73; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no
- buffers: home 0x580240000000, level 1 0x5806c0000000, level 2 0x580b40000000, both 0x580fc0000000; AnonHugePages (kB): 0, 0, 16777216, 16777216
- per repetition: home 3.355e+07 link read bytes and 2.026e+06 SMMU translation requests; level1 3.355e+07 link read bytes and 2.016e+06 SMMU translation requests; level2 3.355e+07 link read bytes and 599.9 SMMU translation requests; both 3.355e+07 link read bytes and 450.1 SMMU translation requests; multiplexed rows voided: 0

