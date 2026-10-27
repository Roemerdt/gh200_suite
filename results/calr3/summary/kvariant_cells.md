# k-variant cells: the direct route at several levels of one factor, recomputed from raw rows

Times are per pass in ms. Each round runs every variant once in the order the seed drew; each level minus home is formed within a round and given as median with 95 % rank interval; a positive value means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | variant | level | home ms | level ms | effect ms [interval] | relative to home | rounds | excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0393 | 0.0395 | 0.0002 [0.0002, 0.0002] | +0.4 % | 40 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0393 | 0.3751 | 0.3358 [0.3356, 0.3361] | +854.7 % | 40 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0393 | 0.3982 | 0.3589 [0.3587, 0.3592] | +913.3 % | 40 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0160 | 0.0163 | 0.0002 [0.0002, 0.0003] | +1.5 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0160 | 0.0315 | 0.0155 [0.0155, 0.0155] | +96.7 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0160 | 0.0383 | 0.0223 [0.0222, 0.0223] | +138.8 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=kvar,vary=strategy | strategy | B | warp | 191.3084 | 5.9798 | -185.3288 [-185.3336, -185.3272] | -96.9 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=kvar,vary=strategy | strategy | C | private | 191.3084 | 4.1236 | -187.1851 [-187.1903, -187.1830] | -97.8 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=kvar,vary=strategy | strategy | B | warp | 12.2932 | 0.4121 | -11.8812 [-11.8816, -11.8804] | -96.6 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=kvar,vary=strategy | strategy | C | private | 12.2932 | 4.1234 | -8.1699 [-8.1714, -8.1682] | -66.5 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy | strategy | B | warp | 12.4808 | 12.3282 | -0.1523 [-0.1575, -0.1435] | -1.2 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy | strategy | C | private | 12.4808 | 0.0971 | -12.3836 [-12.3917, -12.3762] | -99.2 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=hbm,type=kvar,vary=strategy | strategy | B | warp | 0.7662 | 0.7562 | -0.0100 [-0.0102, -0.0098] | -1.3 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=hbm,type=kvar,vary=strategy | strategy | C | private | 0.7662 | 0.0922 | -0.6740 [-0.6740, -0.6739] | -88.0 % | 10 | yes | pass |

## Per cell and level

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 61; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x439300000000; level: placement cpu, cursor 1, buffer at 0x439400000000
- per repetition: home 8.429e+06 link read bytes and 0 SMMU translation requests; level 8.429e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 61; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x439300000000; level: placement cpu, cursor 1, buffer at 0x4394c0000000
- per repetition: home 8.429e+06 link read bytes and 0 SMMU translation requests; level 1.341e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 61; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x439300000000; level: placement cpu, cursor 1, buffer at 0x439580000000
- per repetition: home 8.429e+06 link read bytes and 0 SMMU translation requests; level 1.341e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 61; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x570000000000; level: placement hbm, cursor 1, buffer at 0x570100000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 61; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x570000000000; level: placement hbm, cursor 1, buffer at 0x5701c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 61; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x570000000000; level: placement hbm, cursor 1, buffer at 0x570280000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=kvar,vary=strategy, variant B

- seed 61; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x549100000000; level: placement cpu, cursor 0, buffer at 0x5491c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=kvar,vary=strategy, variant C

- seed 61; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x549100000000; level: placement cpu, cursor 0, buffer at 0x549240000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=kvar,vary=strategy, variant B

- seed 61; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x583280000000; level: placement hbm, cursor 0, buffer at 0x583300000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=kvar,vary=strategy, variant C

- seed 61; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x583280000000; level: placement hbm, cursor 0, buffer at 0x583380000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy, variant B

- seed 61; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x5c8880000000; level: placement cpu, cursor 0, buffer at 0x5c8900000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy, variant C

- seed 61; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x5c8880000000; level: placement cpu, cursor 0, buffer at 0x5c8980000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=hbm,type=kvar,vary=strategy, variant B

- seed 61; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x4e2a80000000; level: placement hbm, cursor 0, buffer at 0x4e2b40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=hbm,type=kvar,vary=strategy, variant C

- seed 61; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x4e2a80000000; level: placement hbm, cursor 0, buffer at 0x4e2bc0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

