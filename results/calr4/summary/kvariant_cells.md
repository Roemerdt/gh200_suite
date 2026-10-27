# k-variant cells: the direct route at several levels of one factor, recomputed from raw rows

Times are per pass in ms. Each round runs every variant once in the order the seed drew; each level minus home is formed within a round and given as median with 95 % rank interval; a positive value means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | variant | level | home ms | level ms | effect ms [interval] | relative to home | rounds | excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0393 | 0.0394 | 0.0001 [0.0000, 0.0001] | +0.1 % | 100 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0393 | 0.3727 | 0.3334 [0.3332, 0.3336] | +848.2 % | 100 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0393 | 0.3968 | 0.3575 [0.3573, 0.3576] | +909.5 % | 100 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0162 | 0.0164 | 0.0002 [0.0002, 0.0002] | +1.5 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0162 | 0.0316 | 0.0154 [0.0154, 0.0154] | +95.3 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0162 | 0.0385 | 0.0223 [0.0223, 0.0223] | +137.9 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=kvar,vary=strategy | strategy | B | warp | 191.3091 | 5.9797 | -185.3291 [-185.3393, -185.3264] | -96.9 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=kvar,vary=strategy | strategy | C | private | 191.3091 | 4.1236 | -187.1850 [-187.1936, -187.1833] | -97.8 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=kvar,vary=strategy | strategy | B | warp | 12.2957 | 0.4112 | -11.8846 [-11.8939, -11.8834] | -96.7 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=kvar,vary=strategy | strategy | C | private | 12.2957 | 4.1229 | -8.1728 [-8.1828, -8.1717] | -66.5 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy | strategy | B | warp | 12.4723 | 12.2992 | -0.1709 [-0.1784, -0.1686] | -1.4 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy | strategy | C | private | 12.4723 | 0.0970 | -12.3753 [-12.3850, -12.3731] | -99.2 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=hbm,type=kvar,vary=strategy | strategy | B | warp | 0.7658 | 0.7558 | -0.0100 [-0.0101, -0.0098] | -1.3 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=hbm,type=kvar,vary=strategy | strategy | C | private | 0.7658 | 0.0921 | -0.6737 [-0.6737, -0.6736] | -88.0 % | 10 | yes | pass |

## Per cell and level

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 67; every round ran in the drawn order: yes; 4 variants; stopped on target: no, cap hit: yes
- home: placement cpu, cursor 1, buffer at 0x4d5280000000; level: placement cpu, cursor 1, buffer at 0x4d5340000000
- per repetition: home 8.429e+06 link read bytes and 0 SMMU translation requests; level 8.429e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 67; every round ran in the drawn order: yes; 4 variants; stopped on target: no, cap hit: yes
- home: placement cpu, cursor 1, buffer at 0x4d5280000000; level: placement cpu, cursor 1, buffer at 0x4d5400000000
- per repetition: home 8.429e+06 link read bytes and 0 SMMU translation requests; level 1.341e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 67; every round ran in the drawn order: yes; 4 variants; stopped on target: no, cap hit: yes
- home: placement cpu, cursor 1, buffer at 0x4d5280000000; level: placement cpu, cursor 1, buffer at 0x4d54c0000000
- per repetition: home 8.429e+06 link read bytes and 0 SMMU translation requests; level 1.341e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 67; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x43d940000000; level: placement hbm, cursor 1, buffer at 0x43da40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 67; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x43d940000000; level: placement hbm, cursor 1, buffer at 0x43db00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 67; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x43d940000000; level: placement hbm, cursor 1, buffer at 0x43dbc0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=kvar,vary=strategy, variant B

- seed 67; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x4decc0000000; level: placement cpu, cursor 0, buffer at 0x4ded80000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=kvar,vary=strategy, variant C

- seed 67; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x4decc0000000; level: placement cpu, cursor 0, buffer at 0x4dee00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=kvar,vary=strategy, variant B

- seed 67; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x5c96c0000000; level: placement hbm, cursor 0, buffer at 0x5c9740000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=kvar,vary=strategy, variant C

- seed 67; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x5c96c0000000; level: placement hbm, cursor 0, buffer at 0x5c97c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy, variant B

- seed 67; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x5af500000000; level: placement cpu, cursor 0, buffer at 0x5af580000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy, variant C

- seed 67; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x5af500000000; level: placement cpu, cursor 0, buffer at 0x5af600000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=hbm,type=kvar,vary=strategy, variant B

- seed 67; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x472240000000; level: placement hbm, cursor 0, buffer at 0x472300000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=hbm,type=kvar,vary=strategy, variant C

- seed 67; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x472240000000; level: placement hbm, cursor 0, buffer at 0x472380000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

