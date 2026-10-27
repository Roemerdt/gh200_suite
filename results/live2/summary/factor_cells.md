# Factor cells: the direct route at a level of one factor against its home level, recomputed from raw rows

Times are per pass in ms. The factor effect on direct access is level minus home within a repeat, as median with its 95 % rank interval; a positive value means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | level | home ms | level ms | effect ms [interval] | relative to home | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|
| at=plain,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | plain | 164.4382 | 17.1452 | -147.2655 [-147.4882, -147.0251] | -89.6 % | 10 | yes | pass |
| at=plain,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | plain | 34.7516 | 13.5007 | -21.2365 [-25.2144, -14.5804] | -61.1 % | 10 | yes | pass |
| at=returned,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | returned | 164.9521 | 293.1138 | 128.2314 [127.4508, 129.1229] | +77.7 % | 10 | yes | pass |
| at=returned,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | returned | 34.9361 | 74.8560 | 39.2825 [29.6570, 47.2054] | +112.4 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=factor,vary=sharing | sharing | shared | 45.1775 | 44.8525 | -0.3224 [-0.3660, -0.3087] | -0.7 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0742 | 0.0749 | 0.0007 [0.0002, 0.0011] | +1.0 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 2.6658 | 2.7457 | 0.0802 [0.0745, 0.0855] | +3.0 % | 10 | yes | pass |
| at=stadd,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | stadd | 164.5392 | 5.4526 | -159.0639 [-159.1275, -158.9184] | -96.7 % | 10 | yes | pass |
| at=stadd,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | stadd | 31.1116 | 13.1079 | -17.4428 [-41.8425, -14.3556] | -56.1 % | 10 | yes | pass |
| at=tiles,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=tiling,working-set-mib=8 | tiling | tiles | 0.0679 | 0.0650 | -0.0030 [-0.0030, -0.0029] | -4.4 % | 10 | yes | pass |

## Host phases

The CPU phase before every pass, timed on the CPU clock (ms per pass), and the state check's median load latency on the preparing core after the phase (ns per sampled load), per variant.

| cell | home CPU ms | home state ns | level CPU ms | level state ns |
|---|---|---|---|---|
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=factor,vary=sharing | 1.3303 | - | 1.6580 | - |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8 | 0.6200 | 196.8 | 0.6148 | 196.2 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32 | 3.5752 | 110.2 | 3.5807 | 151.6 |

## Per cell

### route/at=plain,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 7; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x583780000000; level: placement cpu, 2 passes per interval, cursor 0, buffer at 0x583800000000
- no hardware counters in this cell

### route/at=plain,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 7; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x51ef40000000; level: placement cpu, 2 passes per interval, cursor 0, buffer at 0x51f000000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 7; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x439780000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x439800000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 7; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x518fc0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x519080000000
- no hardware counters in this cell

### route/at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=factor,vary=sharing

- first variant B, seed 7; repeats alternated as drawn: yes
- home: placement cpu, 10 passes per interval, cursor 0, buffer at 0x53c880000000; level: placement cpu, 10 passes per interval, cursor 0, buffer at 0x53c980000000
- per repetition: home 4.638e+09 link read bytes and 0 SMMU translation requests; level 4.636e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8

- first variant B, seed 7; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x42c9c0000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x42cac0000000
- per repetition: home 8.382e+06 link read bytes and 335.2 SMMU translation requests; level 8.382e+06 link read bytes and 336.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32

- first variant B, seed 7; repeats alternated as drawn: yes
- home: placement cpu, 10 passes per interval, cursor 0, buffer at 0x596600000000; level: placement cpu, 10 passes per interval, cursor 0, buffer at 0x596700000000
- per repetition: home 5.366e+08 link read bytes and 867.2 SMMU translation requests; level 5.366e+08 link read bytes and 748.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=stadd,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 7; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x447500000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4475c0000000
- no hardware counters in this cell

### route/at=stadd,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 7; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x46ecc0000000; level: placement cpu, 2 passes per interval, cursor 0, buffer at 0x46ed80000000
- no hardware counters in this cell

### route/at=tiles,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=tiling,working-set-mib=8

- first variant B, seed 7; repeats alternated as drawn: yes
- home: placement cpu, 295 passes per interval, cursor 1, buffer at 0x5fe640000000; level: placement cpu, 308 passes per interval, cursor 1, buffer at 0x5fe740000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 8.38e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

