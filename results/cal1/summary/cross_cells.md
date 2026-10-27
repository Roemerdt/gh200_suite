# Cross cells: the direct route at home, at a level of one factor, at a level of a second factor and at both, recomputed from raw rows

Times are per pass in ms. Each round runs the four variants once in the order the seed drew. The first factor's effect is given at the second factor's home (B - A) and at its level (D - C), with the change between them, (D - C) - (B - A), all formed within each round as median with 95 % rank interval; a positive effect means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor 1 | level 1 | factor 2 | level 2 | home ms | level 1 ms | level 2 ms | both ms | effect 1 at home [interval] | effect 1 at level 2 [interval] | change [interval] | effect 2 at home [interval] | rounds | change excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| at=2m,at2=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=cross,vary=page-order,vary2=page-size | page-order | 2m | page-size | 512m | 433.3798 | 5.3675 | 5.3880 | 5.2772 | -428.0132 [-428.1289, -427.9168] | -0.1111 [-0.1189, -0.1034] | 427.8965 [427.8126, 428.0257] | -427.9910 [-428.1133, -427.8965] | 10 | yes | pass |

## Per cell

### route/at=2m,at2=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=cross,vary=page-order,vary2=page-size

- seed 31; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no
- buffers: home 0x52ff80000000, level 1 0x530440000000, level 2 0x5308c0000000, both 0x530d80000000; AnonHugePages (kB): 0, 0, 16777216, 16777216
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level1 5.366e+08 link read bytes and 6.124e+05 SMMU translation requests; level2 5.369e+08 link read bytes and 148.1 SMMU translation requests; both 5.366e+08 link read bytes and 1605 SMMU translation requests; multiplexed rows voided: 0

