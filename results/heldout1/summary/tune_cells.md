# Tuning cells: one route in every configuration of its space, recomputed from raw rows

Times are per repetition in ms. Each round runs every configuration once in the order the seed drew. Per cell the five fastest configurations and, for a copy space, the simplest one (copy engine, pageable memory, one stream, whole transfer); the slowdown against the fastest is paired within rounds, as median with 95 % rank interval. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

## route/copies=ce-pageable-1-256m-none-whole+ce-pageable-1-whole-none-whole,footprint-mib=256,kernel=k3,placement=cpu,tune=copy,type=tune

- 2 configurations, 30 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-pageable-1-whole-none-whole | 1.2113 | [1.2111, 1.2116] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-pageable-1-256m-none-whole | 1.2114 | [1.2111, 1.2119] | 0.0001 [-0.0004, 0.0005] |

## route/copies=ce-registered-1-64m-pipe-touched+ce-registered-2-64m-pipe-touched+ce-pageable-1-whole-none-whole,f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-1-64m-pipe-touched | 2.8449 | [2.8437, 2.8465] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-2-64m-pipe-touched | 2.8467 | [2.8448, 2.8477] | 0.0014 [-0.0008, 0.0040] |
| 3 | ce-pageable-1-whole-none-whole | 3.2091 | [3.2066, 3.2103] | 0.3636 [0.3615, 0.3666] |

## route/copies=ce-registered-1-whole-none-whole+ce-registered-2-whole-none-whole+ce-pageable-1-whole-none-whole,footprint-mib=16384,kernel=k3,placement=cpu,tune=copy,type=tune

- 3 configurations, 30 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-pageable-1-whole-none-whole | 42.6472 | [42.6298, 42.6870] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-2-whole-none-whole | 43.5975 | [43.5925, 43.6012] | 0.9549 [0.9404, 0.9662] |
| 3 | ce-registered-1-whole-none-whole | 43.6003 | [43.5916, 43.6068] | 0.9595 [0.9194, 0.9689] |

## route/copies=ce-registered-1-whole-none-whole+ce-registered-2-whole-none-whole+ce-pageable-1-whole-none-whole,footprint-mib=8192,kernel=k3,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-pageable-1-whole-none-whole | 21.5821 | [21.5791, 21.5856] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-whole-none-whole | 22.5358 | [22.5233, 22.5430] | 0.9559 [0.9410, 0.9640] |
| 3 | ce-registered-2-whole-none-whole | 22.5400 | [22.5290, 22.5423] | 0.9565 [0.9445, 0.9630] |

## route/copies=ce-registered-1-whole-none-whole+ce-registered-4-whole-none-whole+ce-pageable-1-whole-none-whole,footprint-mib=4096,kernel=k3,placement=cpu,tune=copy,type=tune

- 3 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-pageable-1-whole-none-whole | 11.0599 | [11.0579, 11.0623] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-whole-none-whole | 11.9199 | [11.9174, 11.9239] | 0.8601 [0.8564, 0.8644] |
| 3 | ce-registered-4-whole-none-whole | 11.9218 | [11.9183, 11.9235] | 0.8603 [0.8580, 0.8626] |

## route/copies=ce-registered-2-256m-pipe-whole+ce-registered-1-256m-pipe-whole+ce-pageable-1-whole-none-whole,f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-1-256m-pipe-whole | 85.7577 | [85.7155, 85.7684] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-2-256m-pipe-whole | 85.7603 | [85.7494, 85.7622] | 0.0020 [-0.0104, 0.0436] |
| 3 | ce-pageable-1-whole-none-whole | 93.5601 | [93.5500, 93.5824] | 7.8074 [7.7840, 7.8458] |

## route/copies=ce-registered-2-256m-pipe-whole+ce-registered-1-256m-pipe-whole+ce-pageable-1-whole-none-whole,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu,tune=copy,type=tune

- 3 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-256m-pipe-whole | 11.6124 | [11.6104, 11.6150] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-256m-pipe-whole | 11.6129 | [11.6087, 11.6151] | -0.0000 [-0.0046, 0.0036] |
| 3 | ce-pageable-1-whole-none-whole | 11.7382 | [11.7354, 11.7397] | 0.1248 [0.1234, 0.1300] |

## route/copies=ce-registered-2-256m-pipe-whole+ce-registered-4-256m-pipe-whole+ce-pageable-1-whole-none-whole,f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-256m-pipe-whole | 43.3857 | [43.3708, 43.4019] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-4-256m-pipe-whole | 43.4013 | [43.3970, 43.4117] | 0.0130 [-0.0050, 0.0380] |
| 3 | ce-pageable-1-whole-none-whole | 46.7999 | [46.7967, 46.8099] | 3.4144 [3.3997, 3.4270] |

## route/copies=ce-registered-2-64m-pipe-whole+ce-registered-1-64m-pipe-whole+ce-pageable-1-whole-none-whole,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-1-64m-pipe-whole | 3.1012 | [3.0989, 3.1022] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-2-64m-pipe-whole | 3.1014 | [3.1001, 3.1038] | 0.0004 [-0.0021, 0.0037] |
| 3 | ce-pageable-1-whole-none-whole | 3.2433 | [3.2429, 3.2443] | 0.1423 [0.1411, 0.1454] |

## route/copies=ce-registered-2-64m-pipe-whole+ce-registered-4-64m-pipe-whole+ce-pageable-1-whole-none-whole,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-64m-pipe-whole | 0.8144 | [0.8135, 0.8151] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-4-64m-pipe-whole | 0.8151 | [0.8143, 0.8160] | 0.0005 [0.0001, 0.0019] |
| 3 | ce-pageable-1-whole-none-whole | 0.8558 | [0.8547, 0.8562] | 0.0413 [0.0402, 0.0422] |

## route/copies=ce-registered-2-whole-none-whole+ce-registered-1-whole-none-whole+ce-pageable-1-whole-none-whole,footprint-mib=1024,kernel=k3,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-pageable-1-whole-none-whole | 3.4067 | [3.4052, 3.4070] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-2-whole-none-whole | 3.4947 | [3.4933, 3.4979] | 0.0887 [0.0872, 0.0924] |
| 3 | ce-registered-1-whole-none-whole | 3.4950 | [3.4927, 3.4967] | 0.0883 [0.0868, 0.0908] |

## route/copies=ce-registered-4-256m-pipe-whole+ce-registered-1-256m-pipe-whole+ce-pageable-1-whole-none-whole,f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-1-256m-pipe-whole | 64.5655 | [64.5335, 64.5773] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-4-256m-pipe-whole | 64.5743 | [64.5344, 64.5799] | 0.0123 [-0.0330, 0.0449] |
| 3 | ce-pageable-1-whole-none-whole | 70.1783 | [70.1673, 70.1881] | 5.6191 [5.5984, 5.6502] |

## route/copies=ce-registered-4-256m-pipe-whole+ce-registered-1-256m-pipe-whole+ce-pageable-1-whole-none-whole,f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-1-256m-pipe-whole | 22.2011 | [22.1864, 22.2127] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-4-256m-pipe-whole | 22.2036 | [22.1942, 22.2051] | -0.0019 [-0.0118, 0.0173] |
| 3 | ce-pageable-1-whole-none-whole | 23.4167 | [23.4124, 23.4237] | 1.2151 [1.2074, 1.2233] |

## route/copies=ce-registered-4-64m-pipe-touched+ce-registered-1-64m-pipe-touched+ce-pageable-1-whole-none-whole,f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-1-64m-pipe-touched | 2.3619 | [2.3615, 2.3637] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-4-64m-pipe-touched | 2.3626 | [2.3605, 2.3643] | -0.0002 [-0.0015, 0.0024] |
| 3 | ce-pageable-1-whole-none-whole | 3.1424 | [3.1421, 3.1436] | 0.7807 [0.7789, 0.7818] |

## route/copies=ce-registered-4-whole-none-whole+ce-registered-1-whole-none-whole+ce-pageable-1-whole-none-whole,footprint-mib=32768,kernel=k3,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-pageable-1-whole-none-whole | 84.7124 | [84.7082, 84.7154] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-4-whole-none-whole | 85.6792 | [85.6704, 85.6852] | 0.9668 [0.9565, 0.9776] |
| 3 | ce-registered-1-whole-none-whole | 85.6812 | [85.6773, 85.6894] | 0.9677 [0.9634, 0.9770] |

## route/copies=ce-registered-4-whole-none-whole+ce-registered-2-whole-none-whole+ce-pageable-1-whole-none-whole,footprint-mib=24576,kernel=k3,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-pageable-1-whole-none-whole | 63.6639 | [63.6615, 63.6731] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-4-whole-none-whole | 64.6367 | [64.6295, 64.6480] | 0.9723 [0.9535, 0.9851] |
| 3 | ce-registered-2-whole-none-whole | 64.6384 | [64.6291, 64.6457] | 0.9707 [0.9589, 0.9816] |

## route/copies=kernel-pageable-1-256m-pipe-touched+kernel-registered-1-256m-pipe-touched+ce-pageable-1-whole-none-whole,f-den=10,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-256m-pipe-touched | 0.3547 | [0.3544, 0.3552] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-256m-pipe-touched | 0.3564 | [0.3562, 0.3573] | 0.0019 [0.0011, 0.0025] |
| 3 | ce-pageable-1-whole-none-whole | 3.0690 | [3.0682, 3.0700] | 2.7142 [2.7134, 2.7152] |

## route/copies=kernel-pageable-1-64m-pipe-touched+kernel-registered-1-64m-pipe-touched+ce-pageable-1-whole-none-whole,f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-64m-pipe-touched | 0.5157 | [0.5148, 0.5171] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-64m-pipe-touched | 0.5163 | [0.5160, 0.5166] | 0.0004 [-0.0006, 0.0020] |
| 3 | ce-pageable-1-whole-none-whole | 2.7114 | [2.7103, 2.7126] | 2.1958 [2.1942, 2.1973] |

## route/copies=kernel-pageable-1-64m-pipe-touched+kernel-registered-1-64m-pipe-touched+ce-pageable-1-whole-none-whole,f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-64m-pipe-touched | 0.7471 | [0.7466, 0.7480] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-64m-pipe-touched | 0.7476 | [0.7468, 0.7483] | 0.0002 [-0.0005, 0.0009] |
| 3 | ce-pageable-1-whole-none-whole | 2.7852 | [2.7844, 2.7861] | 2.0380 [2.0371, 2.0390] |

## route/copies=kernel-pageable-1-64m-pipe-whole+kernel-registered-1-64m-pipe-whole+ce-pageable-1-whole-none-whole,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-64m-pipe-whole | 0.9460 | [0.9453, 0.9474] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-64m-pipe-whole | 0.9467 | [0.9459, 0.9477] | 0.0007 [-0.0005, 0.0022] |
| 3 | ce-pageable-1-whole-none-whole | 2.8486 | [2.8470, 2.8506] | 1.9021 [1.9014, 1.9040] |

## route/copies=kernel-pageable-1-64m-pipe-whole+kernel-registered-1-64m-pipe-whole+ce-pageable-1-whole-none-whole,f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-64m-pipe-whole | 7.3329 | [7.3292, 7.3982] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-64m-pipe-whole | 7.3974 | [7.3927, 7.4041] | 0.0623 [-0.0047, 0.0732] |
| 3 | ce-pageable-1-whole-none-whole | 22.7828 | [22.7787, 22.7877] | 15.4490 [15.3836, 15.4565] |

## route/copies=kernel-pageable-1-whole-none-touched+kernel-registered-1-whole-none-touched+ce-pageable-1-whole-none-whole,f-den=10,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-touched | 0.1262 | [0.1259, 0.1264] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-touched | 0.1263 | [0.1261, 0.1264] | 0.0001 [-0.0002, 0.0002] |
| 3 | ce-pageable-1-whole-none-whole | 2.5929 | [2.5907, 2.5942] | 2.4667 [2.4648, 2.4682] |

## route/copies=kernel-pageable-1-whole-none-touched+kernel-registered-1-whole-none-touched+ce-pageable-1-whole-none-whole,f-den=100,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-touched | 0.0517 | [0.0517, 0.0518] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-touched | 0.0526 | [0.0525, 0.0527] | 0.0009 [0.0006, 0.0010] |
| 3 | ce-pageable-1-whole-none-whole | 3.0342 | [3.0329, 3.0350] | 2.9826 [2.9810, 2.9833] |

## route/copies=kernel-pageable-1-whole-none-touched-kernel+kernel-registered-1-whole-none-touched-kernel+ce-pageable-1-whole-none-whole,f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-touched-kernel | 0.0183 | [0.0182, 0.0183] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-touched-kernel | 0.0183 | [0.0182, 0.0183] | 0.0000 [0.0000, 0.0001] |
| 3 | ce-pageable-1-whole-none-whole | 3.0487 | [3.0478, 3.0510] | 3.0304 [3.0295, 3.0327] |

## route/copies=kernel-pageable-1-whole-none-whole+kernel-registered-1-whole-none-whole+ce-pageable-1-whole-none-whole,footprint-mib=1024,kernel=k3,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole | 1.1182 | [1.1168, 1.1191] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-whole | 1.1190 | [1.1181, 1.1199] | 0.0008 [-0.0012, 0.0030] |
| 3 | ce-pageable-1-whole-none-whole | 3.0198 | [3.0185, 3.0206] | 1.9016 [1.8998, 1.9033] |

## route/copies=kernel-pageable-1-whole-none-whole+kernel-registered-1-whole-none-whole+ce-pageable-1-whole-none-whole,footprint-mib=256,kernel=k3,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole | 0.6016 | [0.6012, 0.6026] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-whole | 0.6018 | [0.6014, 0.6021] | 0.0002 [-0.0009, 0.0012] |
| 3 | ce-pageable-1-whole-none-whole | 1.0806 | [1.0799, 1.0812] | 0.4789 [0.4773, 0.4798] |

## route/copies=kernel-pageable-1-whole-none-whole+kernel-registered-1-whole-none-whole+ce-pageable-1-whole-none-whole,footprint-mib=4096,kernel=k3,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole | 3.0273 | [3.0265, 3.0294] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-whole | 3.0294 | [3.0244, 3.0356] | 0.0027 [-0.0038, 0.0087] |
| 3 | ce-pageable-1-whole-none-whole | 10.6185 | [10.6135, 10.6217] | 7.5915 [7.5867, 7.5946] |

## route/copies=kernel-pageable-1-whole-none-whole+kernel-registered-1-whole-none-whole+ce-pageable-1-whole-none-whole,footprint-mib=8192,kernel=k3,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-whole | 5.5668 | [5.5612, 5.5867] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole | 5.5911 | [5.5805, 5.6046] | 0.0161 [-0.0005, 0.0414] |
| 3 | ce-pageable-1-whole-none-whole | 20.9043 | [20.8805, 20.9374] | 15.3277 [15.3168, 15.3641] |

## route/copies=kernel-registered-1-256m-pipe-touched+kernel-pageable-1-256m-pipe-touched+ce-pageable-1-whole-none-whole,f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-256m-pipe-touched | 14.6674 | [14.6581, 14.6721] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-256m-pipe-touched | 14.6709 | [14.6574, 14.6857] | 0.0003 [-0.0109, 0.0167] |
| 3 | ce-pageable-1-whole-none-whole | 45.6726 | [45.6522, 45.6831] | 31.0077 [30.9820, 31.0219] |

## route/copies=kernel-registered-1-64m-pipe-touched+kernel-pageable-1-64m-pipe-touched+ce-pageable-1-whole-none-whole,f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-64m-pipe-touched | 0.8790 | [0.8782, 0.8801] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-64m-pipe-touched | 0.8800 | [0.8778, 0.8812] | 0.0016 [-0.0028, 0.0019] |
| 3 | ce-pageable-1-whole-none-whole | 2.8278 | [2.8274, 2.8320] | 1.9490 [1.9475, 1.9534] |

## route/copies=kernel-registered-1-64m-pipe-touched+kernel-registered-1-256m-pipe-touched+ce-pageable-1-whole-none-whole,f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-256m-pipe-touched | 1.6149 | [1.6022, 1.6246] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-64m-pipe-touched | 1.6167 | [1.6153, 1.6190] | 0.0017 [-0.0077, 0.0167] |
| 3 | ce-pageable-1-whole-none-whole | 3.0749 | [3.0732, 3.0756] | 1.4600 [1.4510, 1.4729] |

## route/copies=kernel-registered-1-64m-pipe-whole+kernel-pageable-1-64m-pipe-whole+ce-pageable-1-whole-none-whole,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-64m-pipe-whole | 3.6683 | [3.6672, 3.6709] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-64m-pipe-whole | 3.6686 | [3.6671, 3.6700] | -0.0002 [-0.0022, 0.0025] |
| 3 | ce-pageable-1-whole-none-whole | 11.3105 | [11.3057, 11.3176] | 7.6400 [7.6371, 7.6504] |

## route/copies=kernel-registered-1-whole-none-touched+kernel-pageable-1-whole-none-touched+ce-pageable-1-whole-none-whole,f-den=100,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-touched | 0.0326 | [0.0325, 0.0327] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-touched | 0.0326 | [0.0326, 0.0327] | 0.0000 [-0.0000, 0.0001] |
| 3 | ce-pageable-1-whole-none-whole | 2.5626 | [2.5616, 2.5631] | 2.5301 [2.5290, 2.5305] |

## route/copies=kernel-registered-1-whole-none-touched-kernel+kernel-pageable-1-whole-none-touched-kernel+ce-pageable-1-whole-none-whole,f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-touched-kernel | 0.0142 | [0.0142, 0.0142] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-touched-kernel | 0.0142 | [0.0142, 0.0142] | 0.0000 [-0.0000, 0.0000] |
| 3 | ce-pageable-1-whole-none-whole | 2.5637 | [2.5618, 2.5652] | 2.5495 [2.5476, 2.5510] |

## route/copies=kernel-registered-1-whole-none-whole+kernel-pageable-1-whole-none-whole+ce-pageable-1-whole-none-whole,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole | 0.2545 | [0.2545, 0.2547] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-whole | 0.2567 | [0.2564, 0.2574] | 0.0022 [0.0019, 0.0030] |
| 3 | ce-pageable-1-whole-none-whole | 0.7365 | [0.7362, 0.7366] | 0.4819 [0.4813, 0.4821] |

## route/copies=kernel-registered-1-whole-none-whole+kernel-pageable-1-whole-none-whole+ce-pageable-1-whole-none-whole,footprint-mib=16384,kernel=k3,placement=hbm,tune=copy,type=tune

- 3 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-whole | 10.6365 | [10.6299, 10.6548] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole | 10.6367 | [10.6256, 10.6795] | -0.0008 [-0.0152, 0.0247] |
| 3 | ce-pageable-1-whole-none-whole | 41.4590 | [41.4503, 41.4670] | 30.8168 [30.8071, 30.8287] |

