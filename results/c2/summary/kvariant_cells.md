# k-variant cells: the direct route at several levels of one factor, recomputed from raw rows

Times are per pass in ms. Each round runs every variant once in the order the seed drew; each level minus home is formed within a round and given as median with 95 % rank interval; a positive value means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | variant | level | home ms | level ms | effect ms [interval] | relative to home | rounds | excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|
| at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0301 | 0.0301 | -0.0000 [-0.0000, -0.0000] | -0.0 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0301 | 0.0303 | 0.0001 [0.0001, 0.0001] | +0.4 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0301 | 0.0305 | 0.0004 [0.0003, 0.0004] | +1.2 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0088 | 0.0088 | -0.0000 [-0.0000, -0.0000] | -0.2 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0088 | 0.0090 | 0.0001 [0.0001, 0.0002] | +1.6 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0088 | 0.0096 | 0.0007 [0.0007, 0.0007] | +8.3 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0379 | 0.0381 | 0.0002 [0.0002, 0.0002] | +0.6 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0379 | 0.3754 | 0.3375 [0.3366, 0.3382] | +890.8 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0379 | 0.3987 | 0.3608 [0.3595, 0.3619] | +952.3 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0160 | 0.0162 | 0.0002 [0.0002, 0.0002] | +1.3 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0160 | 0.0315 | 0.0155 [0.0154, 0.0155] | +96.6 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0160 | 0.0382 | 0.0222 [0.0222, 0.0222] | +138.6 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0309 | 0.0309 | -0.0000 [-0.0001, -0.0000] | -0.1 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0309 | 0.0539 | 0.0230 [0.0229, 0.0230] | +74.2 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0309 | 0.0554 | 0.0245 [0.0245, 0.0245] | +79.3 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0093 | 0.0093 | 0.0000 [-0.0000, 0.0000] | +0.0 % | 10 | no | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0093 | 0.0104 | 0.0011 [0.0011, 0.0011] | +11.8 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0093 | 0.0115 | 0.0022 [0.0022, 0.0022] | +23.3 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0321 | 0.0321 | 0.0000 [-0.0000, 0.0000] | +0.0 % | 10 | no | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0321 | 0.0998 | 0.0677 [0.0677, 0.0677] | +211.0 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0321 | 0.1052 | 0.0731 [0.0731, 0.0732] | +227.9 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0103 | 0.0103 | 0.0001 [0.0000, 0.0001] | +0.7 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0103 | 0.0134 | 0.0031 [0.0031, 0.0031] | +30.0 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0103 | 0.0154 | 0.0051 [0.0051, 0.0051] | +49.6 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0607 | 0.0617 | 0.0009 [0.0009, 0.0010] | +1.5 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0607 | 1.4736 | 1.4129 [1.4067, 1.4191] | +2325.8 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0607 | 1.5706 | 1.5099 [1.4955, 1.5142] | +2485.4 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0388 | 0.0398 | 0.0010 [0.0009, 0.0010] | +2.5 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0388 | 0.1046 | 0.0658 [0.0657, 0.0658] | +169.5 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0388 | 0.1279 | 0.0891 [0.0889, 0.0893] | +229.6 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=kvar,vary=strategy | strategy | B | warp | 191.3084 | 5.9798 | -185.3285 [-185.3307, -185.3260] | -96.9 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=kvar,vary=strategy | strategy | C | private | 191.3084 | 4.1237 | -187.1844 [-187.1868, -187.1820] | -97.8 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=kvar,vary=strategy | strategy | B | warp | 12.3183 | 0.4146 | -11.9036 [-11.9065, -11.8976] | -96.6 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=kvar,vary=strategy | strategy | C | private | 12.3183 | 4.1222 | -8.1956 [-8.1998, -8.1897] | -66.5 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy | strategy | B | warp | 12.4834 | 12.3127 | -0.1690 [-0.1740, -0.1610] | -1.4 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy | strategy | C | private | 12.4834 | 0.0972 | -12.3862 [-12.3916, -12.3772] | -99.2 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=hbm,type=kvar,vary=strategy | strategy | B | warp | 0.7658 | 0.7561 | -0.0096 [-0.0100, -0.0094] | -1.3 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=hbm,type=kvar,vary=strategy | strategy | C | private | 0.7658 | 0.0921 | -0.6737 [-0.6738, -0.6736] | -88.0 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=16,placement=cpu,type=kvar,vary=strategy | strategy | B | warp | 82.2128 | 19.4509 | -62.7623 [-62.7656, -62.7564] | -76.3 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=16,placement=cpu,type=kvar,vary=strategy | strategy | C | private | 82.2128 | 0.3252 | -81.8876 [-81.8905, -81.8822] | -99.6 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=16,placement=hbm,type=kvar,vary=strategy | strategy | B | warp | 5.0314 | 1.4766 | -3.5546 [-3.5550, -3.5546] | -70.6 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=16,placement=hbm,type=kvar,vary=strategy | strategy | C | private | 5.0314 | 0.3251 | -4.7062 [-4.7066, -4.7061] | -93.5 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=256,placement=cpu,type=kvar,vary=strategy | strategy | B | warp | 48.2062 | 45.2929 | -2.9124 [-2.9213, -2.9040] | -6.0 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=256,placement=cpu,type=kvar,vary=strategy | strategy | C | private | 48.2062 | 0.1097 | -48.0964 [-48.1009, -48.0907] | -99.8 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=256,placement=hbm,type=kvar,vary=strategy | strategy | B | warp | 2.6879 | 2.5098 | -0.1777 [-0.1783, -0.1775] | -6.6 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=256,placement=hbm,type=kvar,vary=strategy | strategy | C | private | 2.6879 | 0.1085 | -2.5794 [-2.5796, -2.5789] | -96.0 % | 10 | yes | pass |

## Per cell and level

### route/at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x48ac80000000; level: placement cpu, cursor 1, buffer at 0x48ad40000000
- per repetition: home 8.38e+06 link read bytes and 0 SMMU translation requests; level 8.38e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x48ac80000000; level: placement cpu, cursor 1, buffer at 0x48ae00000000
- per repetition: home 8.38e+06 link read bytes and 0 SMMU translation requests; level 8.38e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x48ac80000000; level: placement cpu, cursor 1, buffer at 0x48aec0000000
- per repetition: home 8.38e+06 link read bytes and 0 SMMU translation requests; level 8.38e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x588080000000; level: placement hbm, cursor 1, buffer at 0x588180000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x588080000000; level: placement hbm, cursor 1, buffer at 0x588240000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x588080000000; level: placement hbm, cursor 1, buffer at 0x588300000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x5fd300000000; level: placement cpu, cursor 1, buffer at 0x5fd400000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 8.382e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x5fd300000000; level: placement cpu, cursor 1, buffer at 0x5fd4c0000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 1.341e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x5fd300000000; level: placement cpu, cursor 1, buffer at 0x5fd580000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 1.341e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x561340000000; level: placement hbm, cursor 1, buffer at 0x561440000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x561340000000; level: placement hbm, cursor 1, buffer at 0x561500000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x561340000000; level: placement hbm, cursor 1, buffer at 0x5615c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x501200000000; level: placement cpu, cursor 1, buffer at 0x501300000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 8.382e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x501200000000; level: placement cpu, cursor 1, buffer at 0x5013c0000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 1.676e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x501200000000; level: placement cpu, cursor 1, buffer at 0x501480000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 1.676e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x4a4400000000; level: placement hbm, cursor 1, buffer at 0x4a44c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x4a4400000000; level: placement hbm, cursor 1, buffer at 0x4a4580000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x4a4400000000; level: placement hbm, cursor 1, buffer at 0x4a4640000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x411dc0000000; level: placement cpu, cursor 1, buffer at 0x411ec0000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 8.382e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x411dc0000000; level: placement cpu, cursor 1, buffer at 0x411f80000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 3.352e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x411dc0000000; level: placement cpu, cursor 1, buffer at 0x412040000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 3.352e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x5e9e40000000; level: placement hbm, cursor 1, buffer at 0x5e9f40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x5e9e40000000; level: placement hbm, cursor 1, buffer at 0x5ea000000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x5e9e40000000; level: placement hbm, cursor 1, buffer at 0x5ea0c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x5f6dc0000000; level: placement cpu, cursor 1, buffer at 0x5f6ec0000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 8.382e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x5f6dc0000000; level: placement cpu, cursor 1, buffer at 0x5f6f80000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 5.363e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 1, buffer at 0x5f6dc0000000; level: placement cpu, cursor 1, buffer at 0x5f7040000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 5.363e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x4c3f00000000; level: placement hbm, cursor 1, buffer at 0x4c3fc0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x4c3f00000000; level: placement hbm, cursor 1, buffer at 0x4c4080000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 73; every round ran in the drawn order: yes; 4 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 1, buffer at 0x4c3f00000000; level: placement hbm, cursor 1, buffer at 0x4c4140000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=kvar,vary=strategy, variant B

- seed 73; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x4bba40000000; level: placement cpu, cursor 0, buffer at 0x4bbac0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=kvar,vary=strategy, variant C

- seed 73; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x4bba40000000; level: placement cpu, cursor 0, buffer at 0x4bbb40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=kvar,vary=strategy, variant B

- seed 73; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x5fc940000000; level: placement hbm, cursor 0, buffer at 0x5fc9c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=kvar,vary=strategy, variant C

- seed 73; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x5fc940000000; level: placement hbm, cursor 0, buffer at 0x5fca40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy, variant B

- seed 73; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x4c8480000000; level: placement cpu, cursor 0, buffer at 0x4c8540000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy, variant C

- seed 73; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x4c8480000000; level: placement cpu, cursor 0, buffer at 0x4c85c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=hbm,type=kvar,vary=strategy, variant B

- seed 73; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x4cac00000000; level: placement hbm, cursor 0, buffer at 0x4cac80000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=hbm,type=kvar,vary=strategy, variant C

- seed 73; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x4cac00000000; level: placement hbm, cursor 0, buffer at 0x4cad00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=16,placement=cpu,type=kvar,vary=strategy, variant B

- seed 73; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x482140000000; level: placement cpu, cursor 0, buffer at 0x482200000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=16,placement=cpu,type=kvar,vary=strategy, variant C

- seed 73; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x482140000000; level: placement cpu, cursor 0, buffer at 0x482280000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=16,placement=hbm,type=kvar,vary=strategy, variant B

- seed 73; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x5468c0000000; level: placement hbm, cursor 0, buffer at 0x546980000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=16,placement=hbm,type=kvar,vary=strategy, variant C

- seed 73; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x5468c0000000; level: placement hbm, cursor 0, buffer at 0x546a00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=256,placement=cpu,type=kvar,vary=strategy, variant B

- seed 73; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x482e80000000; level: placement cpu, cursor 0, buffer at 0x482f00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=256,placement=cpu,type=kvar,vary=strategy, variant C

- seed 73; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x482e80000000; level: placement cpu, cursor 0, buffer at 0x482f80000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=256,placement=hbm,type=kvar,vary=strategy, variant B

- seed 73; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x5196c0000000; level: placement hbm, cursor 0, buffer at 0x519780000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=256,placement=hbm,type=kvar,vary=strategy, variant C

- seed 73; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement hbm, cursor 0, buffer at 0x5196c0000000; level: placement hbm, cursor 0, buffer at 0x519800000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

