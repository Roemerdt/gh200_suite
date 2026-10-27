# Tuning cells: one route in every configuration of its space, recomputed from raw rows

Times are per repetition in ms. Each round runs every configuration once in the order the seed drew. Per cell the five fastest configurations and, for a copy space, the simplest one (copy engine, pageable memory, one stream, whole transfer); the slowdown against the fastest is paired within rounds, as median with 95 % rank interval. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

## route/footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-1-64m-pipe-whole-kernel | 3.4095 | [3.4085, 3.4115] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-4-64m-pipe-whole-kernel | 3.4096 | [3.4070, 3.4133] | 0.0002 [-0.0045, 0.0058] |
| 3 | ce-registered-2-64m-pipe-whole-kernel | 3.4117 | [3.4097, 3.4134] | 0.0027 [-0.0000, 0.0039] |
| 4 | ce-registered-4-64m-pipe-whole | 3.4425 | [3.4413, 3.4434] | 0.0329 [0.0299, 0.0343] |
| 5 | ce-registered-2-64m-pipe-whole | 3.4426 | [3.4400, 3.4443] | 0.0322 [0.0296, 0.0352] |
| 73 | ce-pageable-1-whole-none-whole | 5.2014 | [5.1955, 5.2115] | 1.7921 [1.7864, 1.8008] |

## route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,tune=copy,type=tune,working-set-mib=32

- 60 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-256m-none-touched | 0.4725 | [0.4722, 0.4727] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-16m-none-touched | 0.4727 | [0.4720, 0.4732] | 0.0003 [-0.0007, 0.0009] |
| 3 | kernel-registered-1-64m-none-touched | 0.4727 | [0.4722, 0.4731] | 0.0002 [-0.0005, 0.0007] |
| 4 | kernel-registered-1-whole-none-touched | 0.4727 | [0.4721, 0.4731] | 0.0004 [-0.0006, 0.0010] |
| 5 | kernel-registered-1-4m-none-touched | 0.4727 | [0.4714, 0.4733] | 0.0005 [-0.0011, 0.0007] |
| 44 | ce-pageable-1-whole-none-whole | 3.4249 | [3.4235, 3.4258] | 2.9523 [2.9512, 2.9532] |

## route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,tune=direct,type=tune,working-set-mib=32

- 12 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x512x16 | 1.5028 | [1.5023, 1.5036] | 0.0000 [0.0000, 0.0000] |
| 2 | 132x1024x16 | 1.5050 | [1.5042, 1.5060] | 0.0020 [0.0011, 0.0038] |
| 3 | 132x1024x8 | 1.5069 | [1.5056, 1.5077] | 0.0044 [0.0021, 0.0049] |
| 4 | 132x512x8 | 1.9104 | [1.9098, 1.9120] | 0.4078 [0.4067, 0.4092] |
| 5 | 132x256x16 | 1.9404 | [1.9385, 1.9416] | 0.4374 [0.4357, 0.4386] |

## route/footprint-mib=1024,kernel=k6,placement=cpu,tune=copy,type=tune,update=atomic

- 60 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-4-whole-none-whole-kernel | 6.3241 | [6.3211, 6.3282] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-2-whole-none-whole-kernel | 6.3245 | [6.3237, 6.3319] | 0.0016 [-0.0046, 0.0052] |
| 3 | ce-registered-1-whole-none-whole-kernel | 6.3311 | [6.3279, 6.3360] | 0.0060 [0.0039, 0.0117] |
| 4 | ce-registered-1-256m-none-whole-kernel | 6.3380 | [6.3337, 6.3402] | 0.0137 [0.0079, 0.0181] |
| 5 | ce-registered-2-256m-none-whole-kernel | 6.3398 | [6.3383, 6.3441] | 0.0146 [0.0112, 0.0229] |
| 52 | ce-pageable-1-whole-none-whole | 7.4409 | [7.4377, 7.4462] | 1.1163 [1.1105, 1.1252] |

## route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-4-64m-pipe-whole-kernel | 5.8100 | [5.8070, 5.8156] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-2-64m-pipe-whole-kernel | 5.8101 | [5.8058, 5.8184] | 0.0027 [-0.0098, 0.0087] |
| 3 | ce-registered-1-64m-pipe-whole-kernel | 5.8130 | [5.8104, 5.8178] | 0.0033 [-0.0009, 0.0043] |
| 4 | ce-registered-2-16m-pipe-whole-kernel | 5.8548 | [5.8505, 5.8613] | 0.0464 [0.0368, 0.0489] |
| 5 | ce-registered-1-16m-pipe-whole-kernel | 5.8584 | [5.8549, 5.8656] | 0.0474 [0.0403, 0.0558] |
| 80 | ce-pageable-1-whole-none-whole | 6.5601 | [6.5547, 6.5660] | 0.7477 [0.7423, 0.7563] |

