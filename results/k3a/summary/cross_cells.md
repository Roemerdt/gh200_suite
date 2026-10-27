# Cross cells: the direct route at home, at a level of one factor, at a level of a second factor and at both, recomputed from raw rows

Times are per pass in ms. Each round runs the four variants once in the order the seed drew. The first factor's effect is given at the second factor's home (B - A) and at its level (D - C), with the change between them, (D - C) - (B - A), all formed within each round as median with 95 % rank interval; a positive effect means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor 1 | level 1 | factor 2 | level 2 | home ms | level 1 ms | level 2 ms | both ms | effect 1 at home [interval] | effect 1 at level 2 [interval] | change [interval] | effect 2 at home [interval] | rounds | change excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| at=2m,at2=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=cross,vary=page-order,vary2=page-size | page-order | 2m | page-size | 512m | 432.8039 | 5.3690 | 5.3885 | 5.2648 | -427.4360 [-427.5166, -427.2955] | -0.1212 [-0.1271, -0.1131] | 427.3149 [427.1687, 427.4036] | -427.4176 [-427.4984, -427.2757] | 10 | yes | pass |

## Per cell

### route/at=2m,at2=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=cross,vary=page-order,vary2=page-size

- seed 29; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no
- buffers: home 0x483b40000000, level 1 0x484000000000, level 2 0x484480000000, both 0x484940000000; AnonHugePages (kB): 0, 0, 16777216, 16777216
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level1 5.366e+08 link read bytes and 6.107e+05 SMMU translation requests; level2 5.369e+08 link read bytes and 148.4 SMMU translation requests; both 5.366e+08 link read bytes and 1598 SMMU translation requests; multiplexed rows voided: 0

