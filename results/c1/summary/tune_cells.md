# Tuning cells: one route in every configuration of its space, recomputed from raw rows

Times are per repetition in ms. Each round runs every configuration once in the order the seed drew. Per cell the five fastest configurations and, for a copy space, the simplest one (copy engine, pageable memory, one stream, whole transfer); the slowdown against the fastest is paired within rounds, as median with 95 % rank interval. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

## route/f-den=1,f-num=1,footprint-mib=19456,kernel=k1,placement=cpu,tune=copy,type=tune

- 108 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-256m-pipe-whole | 54.1143 | [54.1039, 54.1227] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-4-256m-pipe-whole | 54.1151 | [54.1089, 54.1245] | 0.0049 [-0.0086, 0.0169] |
| 3 | ce-registered-1-256m-pipe-whole | 54.1154 | [54.1058, 54.1278] | 0.0032 [-0.0067, 0.0167] |
| 4 | kernel-registered-1-256m-pipe-whole | 54.5805 | [54.5571, 54.7076] | 0.4677 [0.4235, 0.5808] |
| 5 | kernel-registered-1-256m-pipe-touched | 54.6660 | [54.5982, 54.7822] | 0.5536 [0.4829, 0.7074] |
| 48 | ce-pageable-1-whole-none-whole | 60.6462 | [60.6415, 60.6622] | 6.5410 [6.5268, 6.5585] |

## route/f-den=1,f-num=1,footprint-mib=23296,kernel=k1,placement=cpu,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-1-256m-pipe-whole | 62.2017 | [62.1908, 62.2118] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-2-256m-pipe-whole | 62.2026 | [62.1894, 62.2130] | 0.0018 [-0.0226, 0.0325] |
| 3 | ce-registered-4-256m-pipe-whole | 62.2055 | [62.1869, 62.2224] | -0.0007 [-0.0296, 0.0459] |
| 4 | ce-registered-4-64m-pipe-whole | 63.1289 | [63.1203, 63.1593] | 0.9290 [0.9130, 0.9901] |
| 5 | ce-registered-1-64m-pipe-whole | 63.1315 | [63.1212, 63.1547] | 0.9336 [0.9076, 0.9718] |
| 43 | ce-pageable-1-whole-none-whole | 71.9610 | [71.9466, 72.0004] | 9.7538 [9.7426, 9.8096] |

## route/footprint-mib=11520,kernel=k3,placement=cpu,tune=copy,type=tune

- 30 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole | 32.3026 | [32.2905, 32.3118] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-256m-none-whole | 32.4840 | [32.4468, 32.4971] | 0.1788 [0.1565, 0.1961] |
| 3 | ce-registered-2-whole-none-whole | 32.6856 | [32.6807, 32.6969] | 0.3814 [0.3768, 0.4026] |
| 4 | ce-registered-4-whole-none-whole | 32.6877 | [32.6795, 32.7002] | 0.3875 [0.3719, 0.3961] |
| 5 | ce-registered-1-whole-none-whole | 32.6888 | [32.6823, 32.6961] | 0.3830 [0.3772, 0.4009] |
| 9 | ce-pageable-1-whole-none-whole | 33.0279 | [33.0127, 33.0358] | 0.7291 [0.7037, 0.7452] |

## route/footprint-mib=1536,kernel=k3,placement=cpu,tune=copy,type=tune

- 30 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-whole-none-whole | 4.8574 | [4.8560, 4.8595] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-4-whole-none-whole | 4.8583 | [4.8566, 4.8617] | 0.0013 [-0.0011, 0.0047] |
| 3 | ce-registered-1-whole-none-whole | 4.8584 | [4.8573, 4.8618] | 0.0010 [-0.0015, 0.0044] |
| 4 | ce-registered-1-256m-none-whole | 4.8740 | [4.8705, 4.8751] | 0.0162 [0.0114, 0.0190] |
| 5 | ce-registered-4-256m-none-whole | 4.8785 | [4.8762, 4.8807] | 0.0216 [0.0170, 0.0225] |
| 14 | ce-pageable-1-whole-none-whole | 5.0061 | [5.0029, 5.0079] | 0.1500 [0.1433, 0.1512] |

## route/footprint-mib=2048,kernel=k3,placement=cpu,tune=copy,type=tune

- 30 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-whole-none-whole | 6.2124 | [6.2117, 6.2144] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-4-whole-none-whole | 6.2124 | [6.2095, 6.2149] | -0.0006 [-0.0040, 0.0033] |
| 3 | ce-registered-1-whole-none-whole | 6.2137 | [6.2116, 6.2163] | 0.0004 [-0.0024, 0.0038] |
| 4 | ce-registered-1-256m-none-whole | 6.2304 | [6.2244, 6.2320] | 0.0170 [0.0123, 0.0206] |
| 5 | ce-registered-2-256m-none-whole | 6.2358 | [6.2338, 6.2409] | 0.0227 [0.0201, 0.0289] |
| 13 | ce-pageable-1-whole-none-whole | 6.4599 | [6.4589, 6.4623] | 0.2477 [0.2465, 0.2495] |

## route/footprint-mib=9728,kernel=k3,placement=cpu,tune=copy,type=tune

- 30 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole | 27.3431 | [27.3243, 27.3518] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-256m-none-whole | 27.4376 | [27.4273, 27.4576] | 0.0946 [0.0706, 0.1296] |
| 3 | ce-registered-4-whole-none-whole | 27.9305 | [27.9190, 27.9449] | 0.5873 [0.5724, 0.6204] |
| 4 | ce-registered-1-whole-none-whole | 27.9316 | [27.9261, 27.9422] | 0.5901 [0.5841, 0.6046] |
| 5 | ce-registered-2-whole-none-whole | 27.9403 | [27.9352, 27.9519] | 0.5969 [0.5904, 0.6081] |
| 10 | ce-pageable-1-whole-none-whole | 28.1345 | [28.1241, 28.1450] | 0.7902 [0.7812, 0.8015] |

