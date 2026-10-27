# k-variant cells: the direct route at several levels of one factor, recomputed from raw rows

Times are per pass in ms. Each round runs every variant once in the order the seed drew; each level minus home is formed within a round and given as median with 95 % rank interval; a positive value means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | variant | level | home ms | level ms | effect ms [interval] | relative to home | rounds | excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|
| at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0303 | 0.0302 | -0.0001 [-0.0001, -0.0000] | -0.2 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0303 | 0.0304 | 0.0001 [0.0001, 0.0001] | +0.3 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0303 | 0.0308 | 0.0005 [0.0005, 0.0005] | +1.8 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0089 | 0.0089 | 0.0000 [-0.0000, 0.0000] | +0.2 % | 10 | no | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0089 | 0.0090 | 0.0001 [0.0001, 0.0002] | +1.6 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0089 | 0.0096 | 0.0007 [0.0007, 0.0007] | +8.2 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0377 | 0.0379 | 0.0003 [0.0002, 0.0003] | +0.7 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0377 | 0.3745 | 0.3368 [0.3365, 0.3374] | +894.7 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0377 | 0.3995 | 0.3619 [0.3606, 0.3626] | +961.1 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0160 | 0.0162 | 0.0002 [0.0002, 0.0002] | +1.4 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0160 | 0.0314 | 0.0154 [0.0154, 0.0155] | +96.7 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0160 | 0.0382 | 0.0222 [0.0222, 0.0223] | +138.9 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0309 | 0.0309 | -0.0000 [-0.0000, 0.0000] | -0.0 % | 10 | no | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0309 | 0.0540 | 0.0231 [0.0231, 0.0231] | +74.7 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0309 | 0.0554 | 0.0245 [0.0245, 0.0245] | +79.4 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0094 | 0.0095 | 0.0000 [-0.0000, 0.0000] | +0.1 % | 10 | no | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0094 | 0.0105 | 0.0011 [0.0011, 0.0011] | +11.3 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0094 | 0.0117 | 0.0022 [0.0022, 0.0022] | +23.6 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0319 | 0.0319 | 0.0000 [-0.0000, 0.0000] | +0.1 % | 10 | no | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0319 | 0.0999 | 0.0681 [0.0680, 0.0681] | +213.5 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0319 | 0.1054 | 0.0735 [0.0734, 0.0735] | +230.5 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0104 | 0.0105 | 0.0000 [0.0000, 0.0000] | +0.4 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0104 | 0.0135 | 0.0031 [0.0030, 0.0031] | +29.5 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0104 | 0.0155 | 0.0051 [0.0051, 0.0051] | +48.8 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0610 | 0.0619 | 0.0009 [0.0009, 0.0010] | +1.5 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0610 | 1.4809 | 1.4200 [1.4152, 1.4250] | +2329.1 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0610 | 1.5686 | 1.5076 [1.5002, 1.5156] | +2472.9 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0387 | 0.0396 | 0.0010 [0.0010, 0.0010] | +2.5 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0387 | 0.1049 | 0.0663 [0.0662, 0.0664] | +171.4 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0387 | 0.1279 | 0.0892 [0.0891, 0.0895] | +230.8 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=kvar,vary=strategy | strategy | B | warp | 191.3084 | 5.9796 | -185.3288 [-185.3324, -185.3268] | -96.9 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=kvar,vary=strategy | strategy | C | private | 191.3084 | 4.1233 | -187.1847 [-187.1863, -187.1833] | -97.8 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=kvar,vary=strategy | strategy | B | warp | 12.2938 | 0.4145 | -11.8793 [-11.8801, -11.8788] | -96.6 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=kvar,vary=strategy | strategy | C | private | 12.2938 | 4.1232 | -8.1707 [-8.1720, -8.1689] | -66.5 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy | strategy | B | warp | 12.4949 | 12.3186 | -0.1756 [-0.1853, -0.1723] | -1.4 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy | strategy | C | private | 12.4949 | 0.0970 | -12.3978 [-12.4053, -12.3937] | -99.2 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=hbm,type=kvar,vary=strategy | strategy | B | warp | 0.7662 | 0.7560 | -0.0103 [-0.0107, -0.0098] | -1.3 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=hbm,type=kvar,vary=strategy | strategy | C | private | 0.7662 | 0.0920 | -0.6741 [-0.6744, -0.6740] | -88.0 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=16,placement=cpu,type=kvar,vary=strategy | strategy | B | warp | 82.2362 | 20.4541 | -61.7830 [-61.7972, -61.7715] | -75.1 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=16,placement=cpu,type=kvar,vary=strategy | strategy | C | private | 82.2362 | 0.3253 | -81.9109 [-81.9149, -81.9080] | -99.6 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=16,placement=hbm,type=kvar,vary=strategy | strategy | B | warp | 5.0378 | 1.4777 | -3.5602 [-3.5611, -3.5590] | -70.7 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=16,placement=hbm,type=kvar,vary=strategy | strategy | C | private | 5.0378 | 0.3249 | -4.7129 [-4.7135, -4.7119] | -93.6 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=256,placement=cpu,type=kvar,vary=strategy | strategy | B | warp | 48.2059 | 45.2922 | -2.9144 [-2.9272, -2.9085] | -6.0 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=256,placement=cpu,type=kvar,vary=strategy | strategy | C | private | 48.2059 | 0.1095 | -48.0963 [-48.1044, -48.0923] | -99.8 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=256,placement=hbm,type=kvar,vary=strategy | strategy | B | warp | 2.6878 | 2.5099 | -0.1781 [-0.1799, -0.1772] | -6.6 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=256,placement=hbm,type=kvar,vary=strategy | strategy | C | private | 2.6878 | 0.1086 | -2.5791 [-2.5813, -2.5784] | -96.0 % | 10 | yes | pass |

## Per cell and level

### route/at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x408300000000; level: placement cpu, cursor 1, buffer at 0x408400000000
- per repetition: home 8.38e+06 link read bytes and 0 SMMU translation requests; level 8.38e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x408300000000; level: placement cpu, cursor 1, buffer at 0x4084c0000000
- per repetition: home 8.38e+06 link read bytes and 0 SMMU translation requests; level 8.38e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x408300000000; level: placement cpu, cursor 1, buffer at 0x408580000000
- per repetition: home 8.38e+06 link read bytes and 0 SMMU translation requests; level 8.38e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x4d3d40000000; level: placement hbm, cursor 1, buffer at 0x4d3e40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x4d3d40000000; level: placement hbm, cursor 1, buffer at 0x4d3f00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x4d3d40000000; level: placement hbm, cursor 1, buffer at 0x4d3fc0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x4ccf80000000; level: placement cpu, cursor 1, buffer at 0x4cd080000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 8.382e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x4ccf80000000; level: placement cpu, cursor 1, buffer at 0x4cd140000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 1.341e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x4ccf80000000; level: placement cpu, cursor 1, buffer at 0x4cd200000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 1.341e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x53c640000000; level: placement hbm, cursor 1, buffer at 0x53c740000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x53c640000000; level: placement hbm, cursor 1, buffer at 0x53c800000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x53c640000000; level: placement hbm, cursor 1, buffer at 0x53c8c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x478400000000; level: placement cpu, cursor 1, buffer at 0x478500000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 8.382e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x478400000000; level: placement cpu, cursor 1, buffer at 0x4785c0000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 1.676e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x478400000000; level: placement cpu, cursor 1, buffer at 0x478680000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 1.676e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x54cb40000000; level: placement hbm, cursor 1, buffer at 0x54cc40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x54cb40000000; level: placement hbm, cursor 1, buffer at 0x54cd00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x54cb40000000; level: placement hbm, cursor 1, buffer at 0x54cdc0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x414d40000000; level: placement cpu, cursor 1, buffer at 0x414e40000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 8.382e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x414d40000000; level: placement cpu, cursor 1, buffer at 0x414f00000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 3.352e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x414d40000000; level: placement cpu, cursor 1, buffer at 0x414fc0000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 3.352e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x423500000000; level: placement hbm, cursor 1, buffer at 0x423600000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x423500000000; level: placement hbm, cursor 1, buffer at 0x4236c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x423500000000; level: placement hbm, cursor 1, buffer at 0x423780000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x43ce40000000; level: placement cpu, cursor 1, buffer at 0x43cf40000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 8.382e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x43ce40000000; level: placement cpu, cursor 1, buffer at 0x43d000000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 5.363e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x43ce40000000; level: placement cpu, cursor 1, buffer at 0x43d0c0000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 5.363e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x5c9380000000; level: placement hbm, cursor 1, buffer at 0x5c9480000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x5c9380000000; level: placement hbm, cursor 1, buffer at 0x5c9540000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 71; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x5c9380000000; level: placement hbm, cursor 1, buffer at 0x5c9600000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=kvar,vary=strategy, variant B

- seed 71; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x4f9a40000000; level: placement cpu, cursor 0, buffer at 0x4f9ac0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=kvar,vary=strategy, variant C

- seed 71; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x4f9a40000000; level: placement cpu, cursor 0, buffer at 0x4f9b40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=kvar,vary=strategy, variant B

- seed 71; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x4a4780000000; level: placement hbm, cursor 0, buffer at 0x4a4840000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=kvar,vary=strategy, variant C

- seed 71; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x4a4780000000; level: placement hbm, cursor 0, buffer at 0x4a48c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy, variant B

- seed 71; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x416500000000; level: placement cpu, cursor 0, buffer at 0x416580000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy, variant C

- seed 71; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x416500000000; level: placement cpu, cursor 0, buffer at 0x416600000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=hbm,type=kvar,vary=strategy, variant B

- seed 71; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x40ee40000000; level: placement hbm, cursor 0, buffer at 0x40ef00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=hbm,type=kvar,vary=strategy, variant C

- seed 71; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x40ee40000000; level: placement hbm, cursor 0, buffer at 0x40ef80000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=16,placement=cpu,type=kvar,vary=strategy, variant B

- seed 71; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x441e00000000; level: placement cpu, cursor 0, buffer at 0x441ec0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=16,placement=cpu,type=kvar,vary=strategy, variant C

- seed 71; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x441e00000000; level: placement cpu, cursor 0, buffer at 0x441f40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=16,placement=hbm,type=kvar,vary=strategy, variant B

- seed 71; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x53a4c0000000; level: placement hbm, cursor 0, buffer at 0x53a580000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=16,placement=hbm,type=kvar,vary=strategy, variant C

- seed 71; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x53a4c0000000; level: placement hbm, cursor 0, buffer at 0x53a600000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=256,placement=cpu,type=kvar,vary=strategy, variant B

- seed 71; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x584700000000; level: placement cpu, cursor 0, buffer at 0x5847c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=256,placement=cpu,type=kvar,vary=strategy, variant C

- seed 71; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x584700000000; level: placement cpu, cursor 0, buffer at 0x584840000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=256,placement=hbm,type=kvar,vary=strategy, variant B

- seed 71; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x4d8140000000; level: placement hbm, cursor 0, buffer at 0x4d8200000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=256,placement=hbm,type=kvar,vary=strategy, variant C

- seed 71; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x4d8140000000; level: placement hbm, cursor 0, buffer at 0x4d8280000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

