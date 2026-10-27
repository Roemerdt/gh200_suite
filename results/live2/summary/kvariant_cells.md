# k-variant cells: the direct route at several levels of one factor, recomputed from raw rows

Times are per pass in ms. Each round runs every variant once in the order the seed drew; each level minus home is formed within a round and given as median with 95 % rank interval; a positive value means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | variant | level | home ms | level ms | effect ms [interval] | relative to home | rounds | excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | B | cta | 0.0679 | 0.0684 | 0.0005 [0.0004, 0.0006] | +0.7 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | C | gpu | 0.0679 | 0.6881 | 0.6203 [0.6138, 0.6237] | +913.7 % | 10 | yes | pass |
| at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8 | scope | D | sys | 0.0679 | 0.6734 | 0.6056 [0.5869, 0.6177] | +892.0 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy | strategy | B | warp | 12.4822 | 12.3224 | -0.1618 [-0.1646, -0.1519] | -1.3 % | 10 | yes | pass |
| at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy | strategy | C | private | 12.4822 | 0.1263 | -12.3558 [-12.3617, -12.3523] | -99.0 % | 10 | yes | pass |

## Per cell and level

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant B

- seed 7; every round ran in the drawn order: yes; 4 variants; stopped on target: no, cap hit: yes
- home: placement cpu, cursor 1, buffer at 0x5a8180000000; level: placement cpu, cursor 1, buffer at 0x5a8280000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 8.382e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant C

- seed 7; every round ran in the drawn order: yes; 4 variants; stopped on target: no, cap hit: yes
- home: placement cpu, cursor 1, buffer at 0x5a8180000000; level: placement cpu, cursor 1, buffer at 0x5a8340000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 1.341e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=cta+gpu+sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=kvar,vary=scope,working-set-mib=8, variant D

- seed 7; every round ran in the drawn order: yes; 4 variants; stopped on target: no, cap hit: yes
- home: placement cpu, cursor 1, buffer at 0x5a8180000000; level: placement cpu, cursor 1, buffer at 0x5a8400000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 1.341e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy, variant B

- seed 7; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x53f7c0000000; level: placement cpu, cursor 0, buffer at 0x53f840000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp+private,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=kvar,vary=strategy, variant C

- seed 7; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x53f7c0000000; level: placement cpu, cursor 0, buffer at 0x53f8c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

