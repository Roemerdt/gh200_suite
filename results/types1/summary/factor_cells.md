# Factor cells: the direct route at a level of one factor against its home level, recomputed from raw rows

Times are per pass in ms. The factor effect on direct access is level minus home within a repeat, as median with its 95 % rank interval; a positive value means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | level | home ms | level ms | effect ms [interval] | relative to home | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 1of100 | 2.7022 | 0.0317 | -2.6705 [-2.6720, -2.6698] | -98.8 % | 10 | yes | pass |

## Per cell

### route/at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant B, seed 23; repeats alternated as drawn: yes
- home: placement cpu, 8 passes per interval, cursor 0, buffer at 0x468e40000000; level: placement cpu, 632 passes per interval, cursor 0, buffer at 0x468f00000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 1.074e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

