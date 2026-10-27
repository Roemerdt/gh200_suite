# Factor cells: the direct route at a level of one factor against its home level, recomputed from raw rows

Times are per pass in ms. The factor effect on direct access is level minus home within a repeat, as median with its 95 % rank interval; a positive value means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | level | home ms | level ms | effect ms [interval] | relative to home | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|
| at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=partition | partition | 2g | 432.8294 | 5.6968 | -427.1391 [-427.2328, -427.0152] | -98.7 % | 10 | yes | pass |
| at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 432.9721 | 5.3818 | -427.5912 [-427.6492, -427.4089] | -98.8 % | 10 | yes | pass |
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-size | page-size | 512m | 432.7096 | 5.4032 | -427.3067 [-427.4021, -427.2721] | -98.8 % | 10 | yes | pass |
| at=512m,footprint-mib=16384,kernel=k3p,placement=cpu,type=factor,vary=page-size | page-size | 512m | 7.0498 | 0.0911 | -6.9587 [-6.9619, -6.9554] | -98.7 % | 10 | yes | pass |
| at=off512m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=alignment | alignment | off512m | 7.9053 | 48.4920 | 40.5862 [40.5261, 40.6863] | +513.4 % | 10 | yes | pass |
| at=sorted,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=index-order | index-order | sorted | 432.8817 | 5.0200 | -427.8586 [-427.9316, -427.6504] | -98.8 % | 10 | yes | pass |

## Per cell

### route/at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=partition

- first variant B, seed 29; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x537c40000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x538100000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 2.7e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 29; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4d4300000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4d4780000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.366e+08 link read bytes and 6.105e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-size

- first variant B, seed 29; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4367c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x436c40000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 151.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=16384,kernel=k3p,placement=cpu,type=factor,vary=page-size

- first variant A, seed 29; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x50a600000000; level: placement cpu, 220 passes per interval, cursor 0, buffer at 0x50aac0000000
- per repetition: home 3.355e+07 link read bytes and 1.971e+06 SMMU translation requests; level 3.355e+07 link read bytes and 2.745 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=alignment

- first variant A, seed 29; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x568540000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x568820000000
- per repetition: home 5.369e+08 link read bytes and 4.394e+04 SMMU translation requests; level 5.369e+08 link read bytes and 1.368e+07 SMMU translation requests; multiplexed rows voided: 0

### route/at=sorted,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=index-order

- first variant A, seed 29; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5e0240000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5e06c0000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.438e+08 link read bytes and 2.305e+05 SMMU translation requests; multiplexed rows voided: 0

