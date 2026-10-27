# k-variant cells: the direct route at several levels of one factor, recomputed from raw rows

Times are per pass in ms. Each round runs every variant once in the order the seed drew; each level minus home is formed within a round and given as median with 95 % rank interval; a positive value means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | variant | level | home ms | level ms | effect ms [interval] | relative to home | rounds | excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|
| at=1of2+1of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=kvar,vary=f | f | B | 1of2 | 2.7269 | 1.3621 | -1.3638 [-1.3783, -1.3432] | -50.0 % | 20 | yes | pass |
| at=1of2+1of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=kvar,vary=f | f | C | 1of10 | 2.7269 | 0.2743 | -2.4526 [-2.4663, -2.4352] | -89.9 % | 20 | yes | pass |

## Per cell and level

### route/at=1of2+1of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=kvar,vary=f, variant B

- seed 23; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x438b40000000; level: placement cpu, cursor 0, buffer at 0x438c00000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of2+1of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=kvar,vary=f, variant C

- seed 23; every round ran in the drawn order: yes; 3 variants; stopped on target: yes, cap hit: no
- home: placement cpu, cursor 0, buffer at 0x438b40000000; level: placement cpu, cursor 0, buffer at 0x438cc0000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 1.074e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

