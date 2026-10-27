# k-variant cells: the direct route at several levels of one factor, recomputed from raw rows

Times are per pass in ms. Each round runs every variant once in the order the seed drew; each level minus home is formed within a round and given as median with 95 % rank interval; a positive value means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | variant | level | home ms | level ms | effect ms [interval] | relative to home | rounds | excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0378 | 0.0379 | 0.0001 [0.0001, 0.0001] | +0.3 % | 40 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0378 | 0.3732 | 0.3354 [0.3350, 0.3356] | +887.7 % | 40 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0378 | 0.3935 | 0.3557 [0.3554, 0.3560] | +941.5 % | 40 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0160 | 0.0162 | 0.0002 [0.0002, 0.0002] | +1.2 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0160 | 0.0316 | 0.0156 [0.0156, 0.0156] | +97.7 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0160 | 0.0382 | 0.0222 [0.0222, 0.0223] | +139.1 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=kvar,vary=strategy | strategy | B | warp | 191.3092 | 5.9797 | -185.3288 [-185.3325, -185.3272] | -96.9 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=kvar,vary=strategy | strategy | C | private | 191.3092 | 4.1234 | -187.1860 [-187.1896, -187.1833] | -97.8 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=kvar,vary=strategy | strategy | B | warp | 12.2927 | 0.4125 | -11.8803 [-11.8830, -11.8793] | -96.6 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=kvar,vary=strategy | strategy | C | private | 12.2927 | 4.1230 | -8.1703 [-8.1723, -8.1683] | -66.5 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy | strategy | B | warp | 12.4813 | 12.3205 | -0.1570 [-0.1612, -0.1543] | -1.3 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy | strategy | C | private | 12.4813 | 0.0971 | -12.3842 [-12.3862, -12.3792] | -99.2 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=hbm,type=kvar,vary=strategy | strategy | B | warp | 0.7662 | 0.7566 | -0.0093 [-0.0099, -0.0089] | -1.2 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=hbm,type=kvar,vary=strategy | strategy | C | private | 0.7662 | 0.0921 | -0.6741 [-0.6744, -0.6737] | -88.0 % | 10 | yes | pass |

## Per cell and level

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 61; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x4b46c0000000; level: placement cpu, cursor 1, buffer at 0x4b47c0000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 8.382e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 61; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x4b46c0000000; level: placement cpu, cursor 1, buffer at 0x4b4880000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 1.341e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 61; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x4b46c0000000; level: placement cpu, cursor 1, buffer at 0x4b4940000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 1.341e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 61; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x4af340000000; level: placement hbm, cursor 1, buffer at 0x4af440000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 61; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x4af340000000; level: placement hbm, cursor 1, buffer at 0x4af500000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 61; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x4af340000000; level: placement hbm, cursor 1, buffer at 0x4af5c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=kvar,vary=strategy, variant B

- seed 61; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x59fa40000000; level: placement cpu, cursor 0, buffer at 0x59fb00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=kvar,vary=strategy, variant C

- seed 61; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x59fa40000000; level: placement cpu, cursor 0, buffer at 0x59fb80000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=kvar,vary=strategy, variant B

- seed 61; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x4d3ec0000000; level: placement hbm, cursor 0, buffer at 0x4d3f80000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=kvar,vary=strategy, variant C

- seed 61; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x4d3ec0000000; level: placement hbm, cursor 0, buffer at 0x4d4000000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy, variant B

- seed 61; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x5b1cc0000000; level: placement cpu, cursor 0, buffer at 0x5b1d80000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy, variant C

- seed 61; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x5b1cc0000000; level: placement cpu, cursor 0, buffer at 0x5b1e00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=hbm,type=kvar,vary=strategy, variant B

- seed 61; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x403380000000; level: placement hbm, cursor 0, buffer at 0x403440000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=hbm,type=kvar,vary=strategy, variant C

- seed 61; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x403380000000; level: placement hbm, cursor 0, buffer at 0x4034c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

