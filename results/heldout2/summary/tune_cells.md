# Tuning cells: one route in every configuration of its space, recomputed from raw rows

Times are per repetition in ms. Each round runs every configuration once in the order the seed drew. Per cell the five fastest configurations and, for a copy space, the simplest one (copy engine, pageable memory, one stream, whole transfer); the slowdown against the fastest is paired within rounds, as median with 95 % rank interval. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

## route/copies=ce-registered-1-256m-pipe-whole-kernel+ce-registered-2-256m-pipe-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=4096,generator=uniform,kernel=k4,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-256m-pipe-whole-kernel | 12.6182 | [12.6152, 12.6231] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-256m-pipe-whole-kernel | 12.6216 | [12.6168, 12.6243] | 0.0014 [-0.0017, 0.0063] |
| 3 | ce-pageable-1-whole-none-whole | 18.5799 | [18.5701, 18.5823] | 5.9608 [5.9518, 5.9651] |

## route/copies=ce-registered-1-256m-pipe-whole-kernel+ce-registered-4-256m-pipe-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=16384,generator=uniform,kernel=k4,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-1-256m-pipe-whole-kernel | 46.9345 | [46.9288, 46.9519] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-4-256m-pipe-whole-kernel | 46.9374 | [46.9290, 46.9484] | -0.0005 [-0.0121, 0.0107] |
| 3 | ce-pageable-1-whole-none-whole | 75.9664 | [75.9528, 75.9740] | 29.0276 [28.9987, 29.0412] |

## route/copies=ce-registered-1-256m-pipe-whole-kernel+ce-registered-4-256m-pipe-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=24576,generator=uniform,kernel=k4,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-4-256m-pipe-whole-kernel | 73.7469 | [73.6376, 73.9446] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-256m-pipe-whole-kernel | 73.7620 | [73.6982, 73.8011] | -0.0035 [-0.1743, 0.1334] |
| 3 | ce-pageable-1-whole-none-whole | 113.9540 | [113.9392, 114.0365] | 40.2728 [40.1120, 40.3838] |

## route/copies=ce-registered-1-4m-none-touched+ce-registered-1-16m-none-touched+ce-pageable-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=cpu,tune=copy,type=tune,working-set-mib=1024

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-pageable-1-whole-none-touched | 8.0963 | [8.0900, 8.1003] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-16m-none-touched | 8.2058 | [8.1968, 8.2100] | 0.1069 [0.1026, 0.1139] |
| 3 | ce-registered-1-4m-none-touched | 8.2088 | [8.1997, 8.2138] | 0.1092 [0.1064, 0.1227] |

## route/copies=ce-registered-1-64m-pipe-whole-kernel+ce-registered-2-64m-pipe-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=512,kernel=k5,placement=cpu,sweeps=2,tiling=tiles,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-64m-pipe-whole-kernel | 3.4780 | [3.4756, 3.4830] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-64m-pipe-whole-kernel | 3.4784 | [3.4757, 3.4818] | 0.0002 [-0.0047, 0.0053] |
| 3 | ce-pageable-1-whole-none-whole | 4.0594 | [4.0583, 4.0598] | 0.5813 [0.5753, 0.5842] |

## route/copies=ce-registered-2-64m-pipe-whole-kernel+ce-registered-1-64m-pipe-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-64m-pipe-whole-kernel | 3.4260 | [3.4248, 3.4302] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-64m-pipe-whole-kernel | 3.4261 | [3.4249, 3.4274] | -0.0004 [-0.0035, 0.0022] |
| 3 | ce-pageable-1-whole-none-whole | 4.1592 | [4.1573, 4.1622] | 0.7334 [0.7271, 0.7362] |

## route/copies=ce-registered-2-64m-pipe-whole-kernel+ce-registered-1-64m-pipe-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=512,kernel=k5,placement=cpu,sweeps=1,tiling=tiles,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-1-64m-pipe-whole-kernel | 3.0735 | [3.0728, 3.0768] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-2-64m-pipe-whole-kernel | 3.0747 | [3.0731, 3.0762] | 0.0000 [-0.0024, 0.0035] |
| 3 | ce-pageable-1-whole-none-whole | 3.6645 | [3.6640, 3.6670] | 0.5903 [0.5889, 0.5924] |

## route/copies=ce-registered-2-64m-pipe-whole-kernel+ce-registered-4-64m-pipe-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=512,kernel=k5,placement=cpu,sweeps=16,tiling=tiles,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-4-64m-pipe-whole-kernel | 9.1001 | [9.0858, 9.1089] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-2-64m-pipe-whole-kernel | 9.1051 | [9.0919, 9.1110] | 0.0014 [-0.0096, 0.0110] |
| 3 | ce-pageable-1-whole-none-whole | 9.7038 | [9.6936, 9.7107] | 0.6037 [0.5963, 0.6115] |

## route/copies=ce-registered-2-64m-pipe-whole-kernel+ce-registered-4-64m-pipe-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=none,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-64m-pipe-whole-kernel | 5.4530 | [5.4476, 5.4571] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-4-64m-pipe-whole-kernel | 5.4557 | [5.4512, 5.4619] | 0.0013 [-0.0017, 0.0154] |
| 3 | ce-pageable-1-whole-none-whole | 5.9897 | [5.9865, 5.9947] | 0.5378 [0.5321, 0.5428] |

## route/copies=ce-registered-2-whole-none-whole-kernel+ce-registered-1-whole-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=1024,kernel=k6,placement=cpu,tune=copy,type=tune,update=atomic

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-whole-none-whole-kernel | 6.7143 | [6.7093, 6.7169] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-whole-none-whole-kernel | 6.7183 | [6.7145, 6.7227] | 0.0060 [-0.0024, 0.0122] |
| 3 | ce-pageable-1-whole-none-whole | 7.3444 | [7.3383, 7.3479] | 0.6302 [0.6230, 0.6377] |

## route/copies=ce-registered-2-whole-none-whole-kernel+ce-registered-1-whole-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=4096,kernel=k6,placement=cpu,tune=copy,type=tune,update=atomic

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-whole-none-whole-kernel | 26.3248 | [26.3114, 26.3362] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-whole-none-whole-kernel | 26.3288 | [26.3059, 26.3390] | -0.0031 [-0.0170, 0.0242] |
| 3 | ce-pageable-1-whole-none-whole | 28.8760 | [28.8617, 28.8821] | 2.5520 [2.5380, 2.5726] |

## route/copies=ce-registered-2-whole-none-whole-kernel+ce-registered-2-256m-none-whole+ce-pageable-1-whole-none-whole,footprint-mib=8192,generator=rmat,kernel=k4,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-whole-none-whole-kernel | 412.6115 | [412.5711, 417.6190] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-pageable-1-whole-none-whole | 414.8657 | [412.2539, 417.4389] | -0.2133 [-0.3436, 4.8121] |
| 3 | ce-registered-2-256m-none-whole | 415.3461 | [412.7457, 417.9804] | 0.2063 [-4.8347, 5.3829] |

## route/copies=ce-registered-4-256m-pipe-whole-kernel+ce-registered-1-256m-pipe-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=32768,generator=uniform,kernel=k4,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-4-256m-pipe-whole-kernel | 91.7154 | [91.6732, 91.7325] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-256m-pipe-whole-kernel | 91.7197 | [91.6863, 91.7585] | 0.0137 [-0.0292, 0.0525] |
| 3 | ce-pageable-1-whole-none-whole | 152.5050 | [152.4676, 152.5105] | 60.7812 [60.7550, 60.8193] |

## route/copies=ce-registered-4-256m-pipe-whole-kernel+ce-registered-1-256m-pipe-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=8192,generator=uniform,kernel=k4,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-1-256m-pipe-whole-kernel | 24.8103 | [24.7999, 24.8277] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-4-256m-pipe-whole-kernel | 24.8174 | [24.8063, 24.8452] | 0.0061 [-0.0190, 0.0302] |
| 3 | ce-pageable-1-whole-none-whole | 37.5532 | [37.5322, 37.5755] | 12.7352 [12.7203, 12.7668] |

## route/copies=ce-registered-4-64m-pipe-whole-kernel+ce-registered-1-64m-pipe-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=256,generator=uniform,kernel=k4,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-4-64m-pipe-whole-kernel | 0.9124 | [0.9118, 0.9132] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-64m-pipe-whole-kernel | 0.9128 | [0.9120, 0.9134] | 0.0003 [-0.0008, 0.0013] |
| 3 | ce-pageable-1-whole-none-whole | 1.0094 | [1.0087, 1.0098] | 0.0968 [0.0960, 0.0978] |

## route/copies=ce-registered-4-64m-pipe-whole-kernel+ce-registered-1-64m-pipe-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=512,kernel=k5,placement=cpu,sweeps=4,tiling=tiles,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-4-64m-pipe-whole-kernel | 4.2748 | [4.2731, 4.2777] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-64m-pipe-whole-kernel | 4.2750 | [4.2738, 4.2796] | -0.0005 [-0.0033, 0.0065] |
| 3 | ce-pageable-1-whole-none-whole | 4.8706 | [4.8657, 4.8742] | 0.5943 [0.5896, 0.5999] |

## route/copies=ce-registered-4-64m-pipe-whole-kernel+ce-registered-2-64m-pipe-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=512,kernel=k5,placement=cpu,sweeps=64,tiling=tiles,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-64m-pipe-whole-kernel | 28.3566 | [28.3187, 28.4040] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-4-64m-pipe-whole-kernel | 28.3856 | [28.3454, 28.4011] | 0.0033 [-0.0063, 0.0420] |
| 3 | ce-pageable-1-whole-none-whole | 28.9577 | [28.9232, 28.9833] | 0.5896 [0.5370, 0.6410] |

## route/copies=ce-registered-4-64m-pipe-whole-kernel+ce-registered-2-64m-pipe-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-4-64m-pipe-whole-kernel | 5.8766 | [5.8727, 5.8792] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-2-64m-pipe-whole-kernel | 5.8769 | [5.8726, 5.8798] | 0.0023 [-0.0066, 0.0052] |
| 3 | ce-pageable-1-whole-none-whole | 6.4677 | [6.4660, 6.4708] | 0.5921 [0.5890, 0.5948] |

## route/copies=kernel-pageable-1-16m-none-touched+kernel-pageable-1-whole-none-touched+ce-pageable-1-whole-none-touched,footprint-mib=1024,k=64,kernel=k2,placement=cpu,tune=copy,type=tune,working-set-mib=32

- 3 configurations, 100 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-16m-none-touched | 0.3758 | [0.3757, 0.3758] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-touched | 0.3758 | [0.3757, 0.3759] | 0.0000 [-0.0001, 0.0001] |
| 3 | ce-pageable-1-whole-none-touched | 1.2521 | [1.2040, 1.2974] | 0.8760 [0.8279, 0.9214] |

## route/copies=kernel-pageable-1-256m-none-whole-kernel+kernel-pageable-1-whole-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=256,kernel=k6,placement=hbm,tune=copy,type=tune,update=atomic

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-256m-none-whole-kernel | 0.5347 | [0.5342, 0.5356] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-whole-kernel | 0.5348 | [0.5339, 0.5353] | -0.0000 [-0.0008, 0.0005] |
| 3 | ce-pageable-1-whole-none-whole | 1.6610 | [1.6607, 1.6616] | 1.1262 [1.1254, 1.1287] |

## route/copies=kernel-pageable-1-256m-none-whole-kernel+kernel-pageable-1-whole-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=512,kernel=k5,placement=hbm,sweeps=64,tiling=tiles,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-256m-none-whole-kernel | 26.3852 | [26.3584, 26.4565] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-whole-kernel | 26.4048 | [26.3773, 26.4403] | -0.0026 [-0.0471, 0.0643] |
| 3 | ce-pageable-1-whole-none-whole | 28.6451 | [28.6186, 28.6996] | 2.2477 [2.2244, 2.2808] |

## route/copies=kernel-pageable-1-256m-none-whole-kernel+kernel-registered-1-whole-none-whole+ce-pageable-1-whole-none-whole,footprint-mib=8192,generator=rmat,kernel=k4,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-256m-none-whole-kernel | 394.7755 | [394.6872, 399.7328] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole | 397.7091 | [395.0257, 400.1942] | 0.4996 [-4.4463, 5.4445] |
| 3 | ce-pageable-1-whole-none-whole | 412.9144 | [410.3895, 415.5605] | 15.7268 [10.6833, 20.8220] |

## route/copies=kernel-pageable-1-256m-none-whole-kernel+kernel-registered-1-whole-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=8,kernel=k6,keys=1,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-256m-none-whole-kernel | 12.3119 | [12.3114, 12.3132] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole-kernel | 12.3144 | [12.3122, 12.3151] | 0.0019 [-0.0009, 0.0035] |
| 3 | ce-pageable-1-whole-none-whole | 12.3647 | [12.3636, 12.3679] | 0.0524 [0.0504, 0.0560] |

## route/copies=kernel-pageable-1-64m-none-touched+kernel-registered-1-whole-none-touched+ce-pageable-1-whole-none-touched,footprint-mib=1024,k=1,kernel=k2,placement=hbm,tune=copy,type=tune,working-set-mib=32

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-touched | 0.0523 | [0.0522, 0.0523] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-64m-none-touched | 0.0523 | [0.0523, 0.0524] | 0.0000 [-0.0000, 0.0003] |
| 3 | ce-pageable-1-whole-none-touched | 0.1190 | [0.1188, 0.1192] | 0.0667 [0.0666, 0.0671] |

## route/copies=kernel-pageable-1-whole-none-touched+kernel-pageable-1-4m-none-touched+ce-pageable-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=hbm,tune=copy,type=tune,working-set-mib=8

- 3 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-touched | 0.0333 | [0.0333, 0.0335] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-4m-none-touched | 0.0333 | [0.0333, 0.0334] | 0.0000 [-0.0000, 0.0001] |
| 3 | ce-pageable-1-whole-none-touched | 0.0589 | [0.0589, 0.0592] | 0.0256 [0.0254, 0.0259] |

## route/copies=kernel-pageable-1-whole-none-touched+kernel-pageable-1-64m-none-touched+ce-pageable-1-whole-none-touched,footprint-mib=1024,k=4,kernel=k2,placement=hbm,tune=copy,type=tune,working-set-mib=32

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-touched | 0.0605 | [0.0605, 0.0607] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-64m-none-touched | 0.0606 | [0.0605, 0.0607] | 0.0001 [-0.0001, 0.0002] |
| 3 | ce-pageable-1-whole-none-touched | 0.1319 | [0.1315, 0.1322] | 0.0715 [0.0708, 0.0717] |

## route/copies=kernel-pageable-1-whole-none-touched+kernel-registered-1-4m-none-touched+ce-pageable-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=cpu,tune=copy,type=tune,working-set-mib=32

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-touched | 0.1830 | [0.1828, 0.1832] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-4m-none-touched | 0.1831 | [0.1827, 0.1833] | 0.0001 [-0.0004, 0.0003] |
| 3 | ce-pageable-1-whole-none-touched | 0.1910 | [0.1907, 0.1914] | 0.0080 [0.0076, 0.0088] |

## route/copies=kernel-pageable-1-whole-none-touched+kernel-registered-1-whole-none-touched+ce-pageable-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=cpu,tune=copy,type=tune,working-set-mib=8

- 3 configurations, 100 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-touched | 0.0539 | [0.0538, 0.0539] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-touched | 0.0542 | [0.0541, 0.0542] | 0.0003 [0.0002, 0.0004] |
| 3 | ce-pageable-1-whole-none-touched | 0.1216 | [0.1138, 0.1299] | 0.0678 [0.0599, 0.0758] |

## route/copies=kernel-pageable-1-whole-none-whole-kernel+kernel-pageable-1-256m-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=256,generator=uniform,kernel=k4,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-whole-kernel | 0.3785 | [0.3781, 0.3787] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-256m-none-whole-kernel | 0.3785 | [0.3783, 0.3789] | 0.0001 [-0.0004, 0.0005] |
| 3 | ce-pageable-1-whole-none-whole | 0.8875 | [0.8868, 0.8882] | 0.5093 [0.5083, 0.5098] |

## route/copies=kernel-pageable-1-whole-none-whole-kernel+kernel-registered-1-256m-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=512,kernel=k5,placement=hbm,sweeps=16,tiling=tiles,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-whole-kernel | 7.1120 | [7.1051, 7.1170] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-256m-none-whole-kernel | 7.1144 | [7.1087, 7.1265] | 0.0030 [-0.0072, 0.0164] |
| 3 | ce-pageable-1-whole-none-whole | 9.3674 | [9.3581, 9.3770] | 2.2565 [2.2458, 2.2662] |

## route/copies=kernel-pageable-1-whole-none-whole-kernel+kernel-registered-1-64m-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=1024,generator=rmat,kernel=k4,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-whole-kernel | 65.8690 | [64.8821, 65.8891] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-64m-none-whole-kernel | 65.9570 | [64.9468, 65.9731] | 0.0673 [-0.9240, 1.0791] |
| 3 | ce-pageable-1-whole-none-whole | 67.8617 | [66.8859, 67.9211] | 1.9946 [1.9597, 2.0404] |

## route/copies=kernel-pageable-1-whole-none-whole-kernel+kernel-registered-1-whole-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=16384,generator=uniform,kernel=k4,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole-kernel | 42.4068 | [42.3749, 42.4169] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-whole-kernel | 42.4160 | [42.3827, 42.4751] | 0.0133 [-0.0342, 0.0496] |
| 3 | ce-pageable-1-whole-none-whole | 74.6026 | [74.5854, 74.6211] | 32.2047 [32.1434, 32.2344] |

## route/copies=kernel-pageable-1-whole-none-whole-kernel+kernel-registered-1-whole-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=4096,generator=uniform,kernel=k4,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-whole-kernel | 9.5849 | [9.5832, 9.5903] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole-kernel | 9.5928 | [9.5875, 9.6041] | 0.0082 [-0.0008, 0.0205] |
| 3 | ce-pageable-1-whole-none-whole | 17.5055 | [17.5003, 17.5142] | 7.9215 [7.9059, 7.9294] |

## route/copies=kernel-pageable-1-whole-none-whole-kernel+kernel-registered-1-whole-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=none,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-whole-kernel | 3.3888 | [3.3874, 3.3926] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole-kernel | 3.3894 | [3.3846, 3.3918] | -0.0000 [-0.0043, 0.0036] |
| 3 | ce-pageable-1-whole-none-whole | 5.6684 | [5.6648, 5.6734] | 2.2783 [2.2753, 2.2859] |

## route/copies=kernel-pageable-1-whole-none-whole-kernel+kernel-registered-1-whole-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=8192,generator=uniform,kernel=k4,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-whole-kernel | 20.2269 | [20.2092, 20.2605] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole-kernel | 20.2315 | [20.1939, 20.2412] | 0.0037 [-0.0437, 0.0243] |
| 3 | ce-pageable-1-whole-none-whole | 36.2912 | [36.2819, 36.3758] | 16.0732 [16.0622, 16.1323] |

## route/copies=kernel-registered-1-16m-none-touched+kernel-registered-1-64m-none-touched+ce-pageable-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=cpu,rotated=1,tune=copy,type=tune,working-set-mib=8

- 3 configurations, 100 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-16m-none-touched | 0.0683 | [0.0683, 0.0684] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-64m-none-touched | 0.0683 | [0.0683, 0.0684] | 0.0000 [-0.0000, 0.0001] |
| 3 | ce-pageable-1-whole-none-touched | 0.1660 | [0.1608, 0.1812] | 0.0977 [0.0924, 0.1131] |

## route/copies=kernel-registered-1-16m-none-whole-kernel+kernel-registered-1-256m-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=16,kernel=k6,placement=hbm,tune=copy,type=tune,update=atomic

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-16m-none-whole-kernel | 0.0948 | [0.0947, 0.0948] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-256m-none-whole-kernel | 0.0948 | [0.0947, 0.0948] | 0.0000 [-0.0001, 0.0001] |
| 3 | ce-pageable-1-whole-none-whole | 0.1937 | [0.1929, 0.1939] | 0.0989 [0.0982, 0.0992] |

## route/copies=kernel-registered-1-16m-none-whole-kernel+kernel-registered-1-256m-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=8,kernel=k6,keys=1024,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-256m-none-whole-kernel | 0.8224 | [0.8223, 0.8225] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-16m-none-whole-kernel | 0.8226 | [0.8223, 0.8227] | 0.0001 [-0.0001, 0.0003] |
| 3 | ce-pageable-1-whole-none-whole | 0.8431 | [0.8425, 0.8433] | 0.0207 [0.0202, 0.0212] |

## route/copies=kernel-registered-1-16m-none-whole-kernel+kernel-registered-1-256m-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-16m-none-whole-kernel | 0.2315 | [0.2314, 0.2316] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-256m-none-whole-kernel | 0.2315 | [0.2313, 0.2321] | 0.0001 [-0.0002, 0.0004] |
| 3 | ce-pageable-1-whole-none-whole | 0.2499 | [0.2495, 0.2502] | 0.0184 [0.0181, 0.0187] |

## route/copies=kernel-registered-1-256m-none-touched+kernel-registered-1-whole-none-touched+ce-pageable-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=hbm,rotated=1,tune=copy,type=tune,working-set-mib=8

- 3 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-touched | 0.0477 | [0.0476, 0.0477] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-256m-none-touched | 0.0477 | [0.0477, 0.0478] | -0.0000 [-0.0001, 0.0001] |
| 3 | ce-pageable-1-whole-none-touched | 0.0749 | [0.0748, 0.0751] | 0.0272 [0.0271, 0.0273] |

## route/copies=kernel-registered-1-256m-none-whole-kernel+kernel-registered-1-whole-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=256,kernel=k6,placement=cpu,tune=copy,type=tune,update=atomic

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-256m-none-whole-kernel | 1.6735 | [1.6729, 1.6743] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole-kernel | 1.6740 | [1.6729, 1.6749] | 0.0003 [-0.0003, 0.0013] |
| 3 | ce-pageable-1-whole-none-whole | 1.8707 | [1.8694, 1.8721] | 0.1967 [0.1959, 0.1989] |

## route/copies=kernel-registered-1-4m-none-touched+kernel-registered-1-16m-none-touched+ce-pageable-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=hbm,tune=copy,type=tune,working-set-mib=1024

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-4m-none-touched | 5.8118 | [5.8071, 5.8163] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-16m-none-touched | 5.8120 | [5.8070, 5.8199] | 0.0003 [-0.0058, 0.0074] |
| 3 | ce-pageable-1-whole-none-touched | 7.7084 | [7.7031, 7.7139] | 1.8942 [1.8929, 1.8987] |

## route/copies=kernel-registered-1-4m-none-touched+kernel-registered-1-whole-none-touched+ce-pageable-1-whole-none-touched,footprint-mib=1024,k=64,kernel=k2,placement=hbm,tune=copy,type=tune,working-set-mib=32

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-touched | 0.3059 | [0.3057, 0.3066] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-4m-none-touched | 0.3061 | [0.3057, 0.3062] | 0.0000 [-0.0005, 0.0004] |
| 3 | ce-pageable-1-whole-none-touched | 0.3736 | [0.3730, 0.3742] | 0.0675 [0.0670, 0.0683] |

## route/copies=kernel-registered-1-64m-none-touched+kernel-registered-1-4m-none-touched+ce-pageable-1-whole-none-touched,footprint-mib=1024,k=2,kernel=k2,placement=cpu,tune=copy,type=tune,working-set-mib=32

- 3 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-4m-none-touched | 0.1265 | [0.1264, 0.1267] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-64m-none-touched | 0.1266 | [0.1265, 0.1268] | 0.0002 [-0.0001, 0.0004] |
| 3 | ce-pageable-1-whole-none-touched | 0.1325 | [0.1324, 0.1326] | 0.0059 [0.0058, 0.0062] |

## route/copies=kernel-registered-1-64m-none-whole-kernel+kernel-pageable-1-256m-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=8,kernel=k6,keys=1024,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-64m-none-whole-kernel | 0.7817 | [0.7814, 0.7820] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-256m-none-whole-kernel | 0.7820 | [0.7818, 0.7822] | 0.0005 [-0.0001, 0.0007] |
| 3 | ce-pageable-1-whole-none-whole | 0.8389 | [0.8381, 0.8393] | 0.0571 [0.0564, 0.0578] |

## route/copies=kernel-registered-1-whole-none-touched+kernel-pageable-1-whole-none-touched+ce-pageable-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=hbm,tune=copy,type=tune,working-set-mib=32

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-touched | 0.1096 | [0.1094, 0.1098] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-touched | 0.1096 | [0.1095, 0.1097] | 0.0000 [-0.0003, 0.0002] |
| 3 | ce-pageable-1-whole-none-touched | 0.1781 | [0.1777, 0.1785] | 0.0685 [0.0679, 0.0690] |

## route/copies=kernel-registered-1-whole-none-touched+kernel-registered-1-16m-none-touched+ce-pageable-1-whole-none-touched,footprint-mib=1024,k=1,kernel=k2,placement=cpu,tune=copy,type=tune,working-set-mib=32

- 3 configurations, 100 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-touched | 0.1224 | [0.1224, 0.1225] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-16m-none-touched | 0.1225 | [0.1224, 0.1226] | 0.0001 [-0.0000, 0.0002] |
| 3 | ce-pageable-1-whole-none-touched | 0.3835 | [0.3509, 0.4002] | 0.2610 [0.2284, 0.2777] |

## route/copies=kernel-registered-1-whole-none-touched+kernel-registered-1-16m-none-touched+ce-pageable-1-whole-none-touched,footprint-mib=1024,k=4,kernel=k2,placement=cpu,tune=copy,type=tune,working-set-mib=32

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-touched | 0.1347 | [0.1344, 0.1349] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-16m-none-touched | 0.1348 | [0.1345, 0.1350] | -0.0000 [-0.0001, 0.0004] |
| 3 | ce-pageable-1-whole-none-touched | 0.1404 | [0.1403, 0.1405] | 0.0057 [0.0055, 0.0059] |

## route/copies=kernel-registered-1-whole-none-touched+kernel-registered-1-256m-none-touched+ce-pageable-1-whole-none-touched,footprint-mib=1024,k=2,kernel=k2,placement=hbm,tune=copy,type=tune,working-set-mib=32

- 3 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-256m-none-touched | 0.0522 | [0.0521, 0.0523] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-touched | 0.0523 | [0.0522, 0.0523] | 0.0000 [-0.0001, 0.0001] |
| 3 | ce-pageable-1-whole-none-touched | 0.1248 | [0.1246, 0.1252] | 0.0725 [0.0724, 0.0730] |

## route/copies=kernel-registered-1-whole-none-whole-kernel+ce-registered-4-whole-none-whole+ce-pageable-1-whole-none-whole,footprint-mib=1024,generator=rmat,kernel=k4,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-4-whole-none-whole | 67.4656 | [67.4110, 68.4346] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole-kernel | 67.8404 | [67.3228, 68.3733] | -0.0758 [-1.0796, 0.8907] |
| 3 | ce-pageable-1-whole-none-whole | 68.3642 | [67.3960, 68.4137] | 0.4593 [-1.0318, 0.9762] |

## route/copies=kernel-registered-1-whole-none-whole-kernel+kernel-pageable-1-whole-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-whole-kernel | 1.7627 | [1.7616, 1.7635] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole-kernel | 1.7638 | [1.7631, 1.7647] | 0.0008 [-0.0007, 0.0034] |
| 3 | ce-pageable-1-whole-none-whole | 3.7555 | [3.7547, 3.7573] | 1.9923 [1.9914, 1.9957] |

## route/copies=kernel-registered-1-whole-none-whole-kernel+kernel-pageable-1-whole-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=1024,kernel=k6,placement=hbm,tune=copy,type=tune,update=atomic

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-whole-kernel | 2.0975 | [2.0963, 2.0989] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole-kernel | 2.0984 | [2.0947, 2.0990] | 0.0003 [-0.0020, 0.0021] |
| 3 | ce-pageable-1-whole-none-whole | 6.5985 | [6.5966, 6.6020] | 4.5014 [4.4991, 4.5034] |

## route/copies=kernel-registered-1-whole-none-whole-kernel+kernel-pageable-1-whole-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=4096,kernel=k6,placement=hbm,tune=copy,type=tune,update=atomic

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole-kernel | 8.3572 | [8.3491, 8.3662] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-whole-kernel | 8.3621 | [8.3493, 8.3704] | -0.0003 [-0.0078, 0.0141] |
| 3 | ce-pageable-1-whole-none-whole | 26.3686 | [26.3578, 26.3832] | 18.0122 [18.0022, 18.0206] |

## route/copies=kernel-registered-1-whole-none-whole-kernel+kernel-pageable-1-whole-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=512,kernel=k5,placement=hbm,sweeps=1,tiling=tiles,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-whole-kernel | 1.0485 | [1.0471, 1.0490] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole-kernel | 1.0487 | [1.0482, 1.0500] | 0.0004 [-0.0009, 0.0023] |
| 3 | ce-pageable-1-whole-none-whole | 3.3259 | [3.3251, 3.3293] | 2.2777 [2.2757, 2.2805] |

## route/copies=kernel-registered-1-whole-none-whole-kernel+kernel-pageable-1-whole-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=512,kernel=k5,placement=hbm,sweeps=2,tiling=tiles,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole-kernel | 1.4480 | [1.4465, 1.4489] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-whole-kernel | 1.4491 | [1.4479, 1.4509] | 0.0017 [-0.0002, 0.0033] |
| 3 | ce-pageable-1-whole-none-whole | 3.7254 | [3.7231, 3.7286] | 2.2773 [2.2755, 2.2800] |

## route/copies=kernel-registered-1-whole-none-whole-kernel+kernel-pageable-1-whole-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=512,kernel=k5,placement=hbm,sweeps=4,tiling=tiles,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-whole-kernel | 2.2569 | [2.2527, 2.2594] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole-kernel | 2.2578 | [2.2570, 2.2611] | 0.0018 [-0.0002, 0.0043] |
| 3 | ce-pageable-1-whole-none-whole | 4.5311 | [4.5244, 4.5340] | 2.2741 [2.2713, 2.2787] |

## route/copies=kernel-registered-1-whole-none-whole-kernel+kernel-pageable-1-whole-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole-kernel | 3.8740 | [3.8698, 3.8773] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-whole-kernel | 3.8755 | [3.8700, 3.8803] | -0.0001 [-0.0038, 0.0074] |
| 3 | ce-pageable-1-whole-none-whole | 6.1478 | [6.1462, 6.1526] | 2.2749 [2.2689, 2.2810] |

## route/copies=kernel-registered-1-whole-none-whole-kernel+kernel-registered-1-16m-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=8,kernel=k6,keys=1,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole-kernel | 12.3672 | [12.3662, 12.3722] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-16m-none-whole-kernel | 12.3684 | [12.3658, 12.3723] | 0.0008 [-0.0043, 0.0042] |
| 3 | ce-pageable-1-whole-none-whole | 12.3926 | [12.3873, 12.3940] | 0.0218 [0.0196, 0.0259] |

## route/copies=kernel-registered-1-whole-none-whole-kernel+kernel-registered-1-64m-none-whole-kernel+ce-pageable-1-whole-none-whole,footprint-mib=8,kernel=k6,keys=1048576,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole-kernel | 0.1910 | [0.1909, 0.1910] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-64m-none-whole-kernel | 0.1910 | [0.1909, 0.1910] | 0.0000 [-0.0001, 0.0001] |
| 3 | ce-pageable-1-whole-none-whole | 0.2449 | [0.2446, 0.2451] | 0.0539 [0.0536, 0.0541] |

