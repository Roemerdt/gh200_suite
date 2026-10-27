# Tuning cells: one route in every configuration of its space, recomputed from raw rows

Times are per repetition in ms. Each round runs every configuration once in the order the seed drew. Per cell the five fastest configurations and, for a copy space, the simplest one (copy engine, pageable memory, one stream, whole transfer); the slowdown against the fastest is paired within rounds, as median with 95 % rank interval. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

## route/footprint-mib=1024,generator=rmat,kernel=k4,placement=cpu,tune=copy,type=tune

- 108 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole-kernel | 67.3483 | [67.3197, 68.2384] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-4-whole-none-whole | 67.4068 | [67.3804, 68.3290] | 0.0607 [0.0322, 0.1482] |
| 3 | kernel-pageable-1-256m-none-whole-kernel | 67.4124 | [67.3202, 68.2877] | 0.0019 [-0.0831, 0.8631] |
| 4 | ce-registered-1-whole-none-whole-kernel | 67.4156 | [67.3515, 68.2869] | -0.0056 [-0.0948, 0.1510] |
| 5 | kernel-registered-1-256m-none-whole | 67.4220 | [67.3592, 68.3013] | 0.0226 [-0.0030, 0.1821] |
| 39 | ce-pageable-1-whole-none-whole | 68.3405 | [67.4531, 68.3691] | 0.1176 [0.0733, 0.8837] |

## route/footprint-mib=1024,generator=rmat,kernel=k4,placement=cpu,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 2112x1024x8 | 122.8727 | [122.7267, 123.3504] | 0.0000 [0.0000, 0.0000] |
| 2 | 4224x512x8 | 123.3003 | [122.9941, 123.5804] | 0.2387 [-0.2333, 0.7829] |
| 3 | 8448x256x8 | 123.9357 | [123.5932, 124.2498] | 0.8399 [0.7834, 1.3783] |
| 4 | 16896x128x8 | 124.0149 | [123.6113, 124.2872] | 0.8801 [0.6799, 1.4962] |
| 5 | 1056x1024x8 | 131.0297 | [130.9307, 131.7713] | 8.2413 [7.6349, 8.8663] |

## route/footprint-mib=1024,generator=rmat,kernel=k4,placement=hbm,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-whole-kernel | 64.9967 | [64.9404, 65.9868] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-64m-none-whole-kernel | 65.0648 | [65.0505, 65.9814] | 0.0733 [-0.1115, 0.1319] |
| 3 | kernel-registered-1-256m-none-whole | 65.0862 | [65.0522, 65.1143] | 0.0798 [-0.8299, 0.1506] |
| 4 | kernel-registered-1-16m-none-whole-kernel | 65.2260 | [65.1545, 66.1564] | 0.2112 [0.0247, 1.1352] |
| 5 | kernel-registered-1-16m-none-whole | 65.3047 | [65.2208, 66.2732] | 0.3133 [-0.7123, 1.2926] |
| 47 | ce-pageable-1-whole-none-whole | 67.9217 | [67.0525, 67.9445] | 2.5173 [1.7846, 2.9781] |

## route/footprint-mib=1024,generator=rmat,kernel=k4,placement=hbm,tune=direct,type=tune

- 52 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 4224x512x8 | 34.3437 | [34.2835, 34.7684] | 0.0000 [0.0000, 0.0000] |
| 2 | 2112x1024x8 | 34.6133 | [34.5298, 34.9212] | 0.1963 [-0.1063, 0.5626] |
| 3 | 16896x128x8 | 34.6477 | [34.2318, 34.6757] | -0.0724 [-0.1406, 0.3160] |
| 4 | 8448x256x8 | 34.6894 | [34.2653, 34.7327] | 0.0220 [-0.1286, 0.4031] |
| 5 | 4224x256x8 | 37.9463 | [37.8137, 38.3243] | 3.5155 [3.4511, 3.8808] |

## route/footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,tune=copy,type=tune

- 108 configurations, 100 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-64m-pipe-whole-kernel | 3.3734 | [3.3730, 3.3741] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-64m-pipe-whole-kernel | 3.3734 | [3.3731, 3.3738] | -0.0001 [-0.0012, 0.0005] |
| 3 | ce-registered-4-64m-pipe-whole-kernel | 3.3737 | [3.3734, 3.3743] | 0.0005 [-0.0003, 0.0011] |
| 4 | ce-registered-1-64m-pipe-whole | 3.4045 | [3.4041, 3.4048] | 0.0311 [0.0301, 0.0316] |
| 5 | ce-registered-2-64m-pipe-whole | 3.4045 | [3.4037, 3.4051] | 0.0310 [0.0303, 0.0321] |
| 49 | ce-pageable-1-whole-none-whole | 4.2310 | [4.2304, 4.2318] | 0.8571 [0.8564, 0.8586] |

## route/footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,tune=copy-kernel,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 264x128x8 | 4.2380 | [4.2374, 4.2399] | 0.0000 [0.0000, 0.0000] |
| 2 | 132x256x8 | 4.2381 | [4.2352, 4.2394] | -0.0003 [-0.0031, 0.0017] |
| 3 | 132x512x8 | 4.4129 | [4.4047, 4.4185] | 0.1750 [0.1670, 0.1833] |
| 4 | 528x128x8 | 4.4189 | [4.4124, 4.4218] | 0.1813 [0.1726, 0.1843] |
| 5 | 528x128x8 | 4.4203 | [4.4165, 4.4248] | 0.1826 [0.1771, 0.1875] |

## route/footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x256x8 | 30.8080 | [30.7913, 30.8455] | 0.0000 [0.0000, 0.0000] |
| 2 | 264x128x8 | 31.0038 | [30.9766, 31.0182] | 0.1866 [0.1453, 0.2162] |
| 3 | 132x512x8 | 35.2436 | [35.1918, 35.2593] | 4.4134 [4.3675, 4.4680] |
| 4 | 264x256x8 | 36.4364 | [36.4230, 36.4889] | 5.6277 [5.6102, 5.6976] |
| 5 | 264x256x8 | 36.4655 | [36.4368, 36.5292] | 5.6729 [5.5956, 5.7082] |

## route/footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,tune=copy,type=tune

- 108 configurations, 60 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole-kernel | 1.7645 | [1.7639, 1.7650] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-whole-kernel | 1.7651 | [1.7638, 1.7669] | 0.0003 [-0.0004, 0.0016] |
| 3 | kernel-registered-1-256m-none-whole-kernel | 1.7802 | [1.7796, 1.7806] | 0.0157 [0.0151, 0.0165] |
| 4 | kernel-pageable-1-256m-none-whole-kernel | 1.7804 | [1.7793, 1.7810] | 0.0159 [0.0147, 0.0173] |
| 5 | kernel-pageable-1-64m-none-whole-kernel | 1.8234 | [1.8227, 1.8238] | 0.0585 [0.0578, 0.0594] |
| 69 | ce-pageable-1-whole-none-whole | 3.7551 | [3.7542, 3.7558] | 1.9904 [1.9895, 1.9918] |

## route/footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,tune=direct,type=tune

- 52 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x256x8 | 1.2722 | [1.2712, 1.2735] | 0.0000 [0.0000, 0.0000] |
| 2 | 264x128x8 | 1.2723 | [1.2719, 1.2730] | 0.0004 [-0.0012, 0.0017] |
| 3 | 132x512x8 | 1.3201 | [1.3068, 1.3267] | 0.0489 [0.0295, 0.0565] |
| 4 | 264x256x8 | 1.3651 | [1.3537, 1.3738] | 0.0931 [0.0801, 0.1006] |
| 5 | 264x256x8 | 1.3671 | [1.3578, 1.3725] | 0.0928 [0.0856, 0.1003] |

## route/footprint-mib=1024,k=1,kernel=k2,placement=cpu,tune=copy,type=tune,working-set-mib=32

- 30 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-touched | 0.1203 | [0.1202, 0.1207] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-16m-none-touched | 0.1203 | [0.1202, 0.1205] | 0.0001 [-0.0005, 0.0001] |
| 3 | kernel-registered-1-256m-none-touched | 0.1204 | [0.1202, 0.1205] | -0.0000 [-0.0003, 0.0003] |
| 4 | kernel-registered-1-4m-none-touched | 0.1204 | [0.1201, 0.1205] | 0.0000 [-0.0003, 0.0001] |
| 5 | kernel-registered-1-64m-none-touched | 0.1205 | [0.1203, 0.1207] | 0.0002 [-0.0002, 0.0004] |

## route/footprint-mib=1024,k=1,kernel=k2,placement=cpu,tune=direct,type=tune,working-set-mib=32

- 12 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x512x16 | 0.0993 | [0.0993, 0.0994] | 0.0000 [0.0000, 0.0000] |
| 2 | 132x1024x16 | 0.1006 | [0.1006, 0.1006] | 0.0013 [0.0012, 0.0013] |
| 3 | 132x1024x8 | 0.1007 | [0.1007, 0.1008] | 0.0014 [0.0014, 0.0014] |
| 4 | 132x512x8 | 0.1231 | [0.1231, 0.1232] | 0.0238 [0.0237, 0.0238] |
| 5 | 132x256x16 | 0.1258 | [0.1258, 0.1259] | 0.0265 [0.0264, 0.0265] |

## route/footprint-mib=1024,k=1,kernel=k2,placement=hbm,tune=copy,type=tune,working-set-mib=32

- 30 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-64m-none-touched | 0.0499 | [0.0498, 0.0500] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-touched | 0.0499 | [0.0498, 0.0499] | -0.0000 [-0.0001, 0.0000] |
| 3 | kernel-registered-1-16m-none-touched | 0.0499 | [0.0498, 0.0500] | 0.0000 [-0.0001, 0.0001] |
| 4 | kernel-registered-1-64m-none-touched | 0.0499 | [0.0498, 0.0500] | 0.0001 [-0.0001, 0.0002] |
| 5 | kernel-pageable-1-256m-none-touched | 0.0499 | [0.0498, 0.0500] | 0.0000 [-0.0002, 0.0002] |

## route/footprint-mib=1024,k=1,kernel=k2,placement=hbm,tune=direct,type=tune,working-set-mib=32

- 12 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x1024x16 | 0.0174 | [0.0174, 0.0174] | 0.0000 [0.0000, 0.0000] |
| 2 | 132x512x16 | 0.0202 | [0.0202, 0.0202] | 0.0028 [0.0028, 0.0028] |
| 3 | 132x1024x8 | 0.0214 | [0.0214, 0.0214] | 0.0039 [0.0039, 0.0039] |
| 4 | 132x512x8 | 0.0314 | [0.0314, 0.0314] | 0.0140 [0.0140, 0.0140] |
| 5 | 132x256x16 | 0.0316 | [0.0316, 0.0316] | 0.0142 [0.0142, 0.0142] |

## route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,rotated=1,tune=copy,type=tune,working-set-mib=8

- 30 configurations, 100 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-16m-none-touched | 0.0680 | [0.0680, 0.0680] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-64m-none-touched | 0.0680 | [0.0680, 0.0681] | 0.0000 [-0.0001, 0.0001] |
| 3 | kernel-registered-1-whole-none-touched | 0.0680 | [0.0680, 0.0681] | 0.0000 [-0.0000, 0.0001] |
| 4 | kernel-registered-1-4m-none-touched | 0.0681 | [0.0680, 0.0681] | 0.0000 [-0.0001, 0.0001] |
| 5 | kernel-registered-1-256m-none-touched | 0.0681 | [0.0680, 0.0681] | 0.0001 [-0.0000, 0.0001] |

## route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,rotated=1,tune=direct,type=tune,working-set-mib=8

- 12 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x1024x16 | 0.3763 | [0.3762, 0.3765] | 0.0000 [0.0000, 0.0000] |
| 2 | 132x512x16 | 0.3792 | [0.3790, 0.3794] | 0.0028 [0.0026, 0.0032] |
| 3 | 132x1024x8 | 0.3818 | [0.3817, 0.3820] | 0.0054 [0.0052, 0.0058] |
| 4 | 132x256x16 | 0.4918 | [0.4912, 0.4930] | 0.1156 [0.1151, 0.1162] |
| 5 | 132x512x8 | 0.4921 | [0.4916, 0.4926] | 0.1157 [0.1152, 0.1162] |

## route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,tune=copy,type=tune,working-set-mib=1024

- 30 configurations, 50 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-1-4m-none-touched | 8.1006 | [8.0991, 8.1030] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-16m-none-touched | 8.1014 | [8.1001, 8.1037] | 0.0016 [-0.0017, 0.0035] |
| 3 | ce-registered-1-whole-none-touched | 8.1016 | [8.0989, 8.1047] | 0.0013 [-0.0020, 0.0033] |
| 4 | ce-registered-2-256m-none-touched | 8.1022 | [8.1013, 8.1044] | 0.0023 [-0.0004, 0.0042] |
| 5 | ce-registered-4-64m-none-touched | 8.1024 | [8.1010, 8.1059] | 0.0022 [-0.0007, 0.0048] |

## route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,tune=copy,type=tune,working-set-mib=32

- 30 configurations, 100 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-touched | 0.1825 | [0.1824, 0.1827] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-4m-none-touched | 0.1826 | [0.1825, 0.1826] | 0.0000 [-0.0001, 0.0002] |
| 3 | kernel-registered-1-whole-none-touched | 0.1826 | [0.1824, 0.1827] | 0.0000 [-0.0001, 0.0002] |
| 4 | kernel-registered-1-256m-none-touched | 0.1826 | [0.1825, 0.1827] | 0.0001 [-0.0001, 0.0003] |
| 5 | kernel-registered-1-16m-none-touched | 0.1826 | [0.1825, 0.1827] | 0.0001 [-0.0001, 0.0002] |

## route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,tune=copy,type=tune,working-set-mib=8

- 30 configurations, 100 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-touched | 0.0542 | [0.0541, 0.0542] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-touched | 0.0542 | [0.0541, 0.0542] | 0.0000 [-0.0001, 0.0001] |
| 3 | kernel-registered-1-16m-none-touched | 0.0542 | [0.0541, 0.0542] | 0.0000 [-0.0001, 0.0001] |
| 4 | kernel-registered-1-4m-none-touched | 0.0542 | [0.0542, 0.0542] | 0.0001 [0.0000, 0.0001] |
| 5 | kernel-registered-1-64m-none-touched | 0.0542 | [0.0541, 0.0542] | -0.0000 [-0.0001, 0.0001] |

## route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,tune=copy-kernel,type=tune,working-set-mib=32

- 12 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x1024x16 | 0.1905 | [0.1903, 0.1906] | 0.0000 [0.0000, 0.0000] |
| 2 | 132x512x16 | 0.2231 | [0.2230, 0.2232] | 0.0326 [0.0324, 0.0328] |
| 3 | 132x1024x8 | 0.2233 | [0.2231, 0.2237] | 0.0328 [0.0327, 0.0333] |
| 4 | 132x512x8 | 0.3052 | [0.3049, 0.3053] | 0.1147 [0.1145, 0.1148] |
| 5 | 132x256x16 | 0.3135 | [0.3132, 0.3135] | 0.1230 [0.1226, 0.1231] |

## route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,tune=direct,type=tune,working-set-mib=1024

- 12 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x1024x8 | 46.7042 | [46.6972, 46.7280] | 0.0000 [0.0000, 0.0000] |
| 2 | 132x1024x16 | 46.9364 | [46.9066, 46.9555] | 0.2322 [0.1930, 0.2526] |
| 3 | 132x512x16 | 47.2304 | [47.2174, 47.2350] | 0.5241 [0.4943, 0.5515] |
| 4 | 132x512x8 | 57.8294 | [57.8232, 57.8401] | 11.1260 [11.0959, 11.1504] |
| 5 | 132x256x16 | 61.0813 | [61.0471, 61.0923] | 14.3696 [14.3391, 14.3946] |

## route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,tune=direct,type=tune,working-set-mib=32

- 12 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x1024x16 | 1.4965 | [1.4963, 1.4969] | 0.0000 [0.0000, 0.0000] |
| 2 | 132x512x16 | 1.5024 | [1.5018, 1.5032] | 0.0058 [0.0050, 0.0068] |
| 3 | 132x1024x8 | 1.5078 | [1.5076, 1.5088] | 0.0114 [0.0111, 0.0120] |
| 4 | 132x512x8 | 1.8985 | [1.8953, 1.8989] | 0.4015 [0.3990, 0.4024] |
| 5 | 132x256x16 | 1.9325 | [1.9316, 1.9334] | 0.4359 [0.4344, 0.4370] |

## route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,tune=direct,type=tune,working-set-mib=8

- 12 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x512x16 | 0.0370 | [0.0370, 0.0371] | 0.0000 [0.0000, 0.0000] |
| 2 | 132x1024x16 | 0.0378 | [0.0378, 0.0378] | 0.0008 [0.0007, 0.0008] |
| 3 | 132x1024x8 | 0.0408 | [0.0408, 0.0409] | 0.0038 [0.0038, 0.0039] |
| 4 | 132x256x16 | 0.0469 | [0.0468, 0.0469] | 0.0098 [0.0098, 0.0099] |
| 5 | 132x512x8 | 0.0479 | [0.0479, 0.0480] | 0.0109 [0.0108, 0.0110] |

## route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,rotated=1,tune=copy,type=tune,working-set-mib=8

- 30 configurations, 30 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-256m-none-touched | 0.0484 | [0.0484, 0.0485] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-touched | 0.0484 | [0.0484, 0.0485] | -0.0000 [-0.0000, 0.0001] |
| 3 | kernel-registered-1-16m-none-touched | 0.0484 | [0.0484, 0.0485] | 0.0000 [-0.0001, 0.0001] |
| 4 | kernel-registered-1-4m-none-touched | 0.0485 | [0.0484, 0.0485] | 0.0000 [-0.0000, 0.0001] |
| 5 | kernel-registered-1-64m-none-touched | 0.0485 | [0.0484, 0.0485] | 0.0000 [-0.0000, 0.0001] |

## route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,rotated=1,tune=direct,type=tune,working-set-mib=8

- 12 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x1024x16 | 0.0301 | [0.0301, 0.0301] | 0.0000 [0.0000, 0.0000] |
| 2 | 132x512x16 | 0.0390 | [0.0390, 0.0391] | 0.0089 [0.0089, 0.0090] |
| 3 | 132x1024x8 | 0.0416 | [0.0416, 0.0416] | 0.0115 [0.0115, 0.0115] |
| 4 | 132x512x8 | 0.0653 | [0.0653, 0.0653] | 0.0352 [0.0352, 0.0352] |
| 5 | 132x256x16 | 0.0659 | [0.0659, 0.0659] | 0.0358 [0.0358, 0.0358] |

## route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,tune=copy,type=tune,working-set-mib=1024

- 30 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-4m-none-touched | 5.8063 | [5.8010, 5.8092] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-16m-none-touched | 5.8095 | [5.8037, 5.8155] | 0.0027 [0.0005, 0.0063] |
| 3 | kernel-pageable-1-16m-none-touched | 5.8097 | [5.8017, 5.8147] | 0.0045 [-0.0065, 0.0118] |
| 4 | kernel-pageable-1-4m-none-touched | 5.8104 | [5.8070, 5.8130] | 0.0069 [-0.0004, 0.0103] |
| 5 | kernel-pageable-1-64m-none-touched | 5.8107 | [5.8039, 5.8143] | 0.0029 [-0.0002, 0.0132] |

## route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,tune=copy,type=tune,working-set-mib=32

- 30 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-touched | 0.1086 | [0.1085, 0.1087] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-touched | 0.1087 | [0.1085, 0.1088] | 0.0001 [-0.0002, 0.0001] |
| 3 | kernel-registered-1-16m-none-touched | 0.1087 | [0.1086, 0.1087] | 0.0000 [-0.0001, 0.0002] |
| 4 | kernel-registered-1-4m-none-touched | 0.1087 | [0.1085, 0.1088] | 0.0001 [-0.0001, 0.0002] |
| 5 | kernel-registered-1-256m-none-touched | 0.1087 | [0.1085, 0.1088] | 0.0000 [-0.0001, 0.0002] |

## route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,tune=copy,type=tune,working-set-mib=8

- 30 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-touched | 0.0334 | [0.0333, 0.0335] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-4m-none-touched | 0.0334 | [0.0334, 0.0335] | 0.0000 [-0.0001, 0.0001] |
| 3 | kernel-pageable-1-256m-none-touched | 0.0335 | [0.0334, 0.0335] | 0.0001 [0.0000, 0.0001] |
| 4 | kernel-pageable-1-16m-none-touched | 0.0335 | [0.0334, 0.0335] | 0.0001 [-0.0001, 0.0002] |
| 5 | kernel-pageable-1-64m-none-touched | 0.0335 | [0.0334, 0.0336] | 0.0001 [-0.0000, 0.0002] |

## route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,tune=direct,type=tune,working-set-mib=1024

- 12 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x1024x16 | 5.1632 | [5.1597, 5.1651] | 0.0000 [0.0000, 0.0000] |
| 2 | 132x1024x8 | 6.9649 | [6.9606, 6.9667] | 1.8020 [1.8001, 1.8044] |
| 3 | 132x512x16 | 7.6773 | [7.6722, 7.6830] | 2.5140 [2.5087, 2.5214] |
| 4 | 132x512x8 | 12.6426 | [12.6383, 12.6452] | 7.4782 [7.4742, 7.4855] |
| 5 | 132x256x16 | 13.9632 | [13.9596, 13.9668] | 8.8007 [8.7955, 8.8052] |

## route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,tune=direct,type=tune,working-set-mib=32

- 12 configurations, 100 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x1024x16 | 0.0975 | [0.0975, 0.0975] | 0.0000 [0.0000, 0.0000] |
| 2 | 132x1024x8 | 0.1561 | [0.1561, 0.1562] | 0.0586 [0.0586, 0.0587] |
| 3 | 132x512x16 | 0.1603 | [0.1602, 0.1604] | 0.0628 [0.0628, 0.0629] |
| 4 | 132x512x8 | 0.2883 | [0.2878, 0.2885] | 0.1908 [0.1903, 0.1910] |
| 5 | 132x256x16 | 0.3008 | [0.3005, 0.3010] | 0.2033 [0.2031, 0.2035] |

## route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,tune=direct,type=tune,working-set-mib=8

- 12 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x512x16 | 0.0160 | [0.0160, 0.0160] | 0.0000 [0.0000, 0.0000] |
| 2 | 132x1024x16 | 0.0161 | [0.0161, 0.0161] | 0.0001 [0.0001, 0.0001] |
| 3 | 132x1024x8 | 0.0196 | [0.0196, 0.0196] | 0.0036 [0.0036, 0.0036] |
| 4 | 132x256x16 | 0.0217 | [0.0217, 0.0217] | 0.0057 [0.0057, 0.0057] |
| 5 | 132x512x8 | 0.0227 | [0.0226, 0.0227] | 0.0066 [0.0066, 0.0067] |

## route/footprint-mib=1024,k=2,kernel=k2,placement=cpu,tune=copy,type=tune,working-set-mib=32

- 30 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-64m-none-touched | 0.1259 | [0.1256, 0.1263] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-4m-none-touched | 0.1261 | [0.1259, 0.1263] | 0.0001 [-0.0003, 0.0006] |
| 3 | kernel-registered-1-whole-none-touched | 0.1261 | [0.1259, 0.1265] | 0.0002 [-0.0002, 0.0004] |
| 4 | kernel-registered-1-256m-none-touched | 0.1261 | [0.1258, 0.1265] | 0.0001 [-0.0002, 0.0008] |
| 5 | kernel-registered-1-16m-none-touched | 0.1261 | [0.1257, 0.1262] | -0.0001 [-0.0003, 0.0006] |

## route/footprint-mib=1024,k=2,kernel=k2,placement=hbm,tune=copy,type=tune,working-set-mib=32

- 30 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-touched | 0.0523 | [0.0522, 0.0524] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-256m-none-touched | 0.0523 | [0.0522, 0.0524] | -0.0000 [-0.0001, 0.0002] |
| 3 | kernel-registered-1-4m-none-touched | 0.0523 | [0.0523, 0.0524] | 0.0001 [0.0000, 0.0002] |
| 4 | kernel-registered-1-16m-none-touched | 0.0523 | [0.0522, 0.0524] | 0.0001 [-0.0001, 0.0001] |
| 5 | kernel-pageable-1-64m-none-touched | 0.0524 | [0.0523, 0.0524] | 0.0001 [-0.0000, 0.0003] |

## route/footprint-mib=1024,k=4,kernel=k2,placement=cpu,tune=copy,type=tune,working-set-mib=32

- 30 configurations, 100 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-touched | 0.1343 | [0.1342, 0.1344] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-16m-none-touched | 0.1343 | [0.1342, 0.1344] | 0.0000 [-0.0001, 0.0001] |
| 3 | kernel-registered-1-4m-none-touched | 0.1343 | [0.1343, 0.1344] | 0.0001 [-0.0001, 0.0001] |
| 4 | kernel-registered-1-64m-none-touched | 0.1343 | [0.1342, 0.1344] | -0.0000 [-0.0001, 0.0001] |
| 5 | kernel-registered-1-256m-none-touched | 0.1343 | [0.1343, 0.1344] | 0.0000 [-0.0001, 0.0001] |

## route/footprint-mib=1024,k=4,kernel=k2,placement=hbm,tune=copy,type=tune,working-set-mib=32

- 30 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-touched | 0.0604 | [0.0602, 0.0605] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-64m-none-touched | 0.0604 | [0.0603, 0.0605] | 0.0000 [-0.0002, 0.0002] |
| 3 | kernel-pageable-1-16m-none-touched | 0.0604 | [0.0604, 0.0606] | 0.0000 [-0.0001, 0.0003] |
| 4 | kernel-pageable-1-4m-none-touched | 0.0604 | [0.0603, 0.0607] | 0.0001 [-0.0001, 0.0004] |
| 5 | kernel-pageable-1-256m-none-touched | 0.0605 | [0.0603, 0.0606] | 0.0001 [-0.0002, 0.0004] |

## route/footprint-mib=1024,k=64,kernel=k2,placement=cpu,tune=copy,type=tune,working-set-mib=32

- 30 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-16m-none-touched | 0.3746 | [0.3742, 0.3750] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-touched | 0.3746 | [0.3743, 0.3749] | -0.0000 [-0.0005, 0.0001] |
| 3 | kernel-pageable-1-64m-none-touched | 0.3746 | [0.3740, 0.3750] | 0.0001 [-0.0008, 0.0006] |
| 4 | kernel-pageable-1-4m-none-touched | 0.3747 | [0.3743, 0.3750] | 0.0000 [-0.0005, 0.0006] |
| 5 | kernel-pageable-1-256m-none-touched | 0.3747 | [0.3745, 0.3752] | 0.0002 [-0.0003, 0.0007] |

## route/footprint-mib=1024,k=64,kernel=k2,placement=cpu,tune=direct,type=tune,working-set-mib=32

- 12 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x1024x16 | 5.9127 | [5.9091, 5.9145] | 0.0000 [0.0000, 0.0000] |
| 2 | 132x512x16 | 5.9758 | [5.9737, 5.9809] | 0.0637 [0.0600, 0.0709] |
| 3 | 132x1024x8 | 6.0047 | [6.0010, 6.0103] | 0.0920 [0.0876, 0.0964] |
| 4 | 132x512x8 | 7.6316 | [7.6258, 7.6423] | 1.7224 [1.7135, 1.7286] |
| 5 | 132x256x16 | 7.7344 | [7.7298, 7.7477] | 1.8215 [1.8168, 1.8374] |

## route/footprint-mib=1024,k=64,kernel=k2,placement=hbm,tune=copy,type=tune,working-set-mib=32

- 30 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-4m-none-touched | 0.3010 | [0.3004, 0.3017] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-touched | 0.3012 | [0.3010, 0.3016] | 0.0004 [-0.0006, 0.0012] |
| 3 | kernel-registered-1-16m-none-touched | 0.3012 | [0.3006, 0.3017] | 0.0002 [-0.0007, 0.0008] |
| 4 | kernel-pageable-1-16m-none-touched | 0.3012 | [0.3009, 0.3020] | 0.0005 [-0.0001, 0.0010] |
| 5 | kernel-registered-1-64m-none-touched | 0.3014 | [0.3011, 0.3016] | 0.0003 [-0.0004, 0.0011] |

## route/footprint-mib=1024,k=64,kernel=k2,placement=hbm,tune=direct,type=tune,working-set-mib=32

- 12 configurations, 100 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x1024x16 | 0.3419 | [0.3418, 0.3421] | 0.0000 [0.0000, 0.0000] |
| 2 | 132x1024x8 | 0.5630 | [0.5625, 0.5633] | 0.2209 [0.2206, 0.2213] |
| 3 | 132x512x16 | 0.5820 | [0.5817, 0.5824] | 0.2400 [0.2396, 0.2406] |
| 4 | 132x512x8 | 1.0628 | [1.0614, 1.0643] | 0.7205 [0.7194, 0.7221] |
| 5 | 132x256x16 | 1.1111 | [1.1097, 1.1122] | 0.7687 [0.7681, 0.7702] |

## route/footprint-mib=1024,kernel=k6,layout=line,placement=cpu,tune=direct,type=tune,update=atomic

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 2112x256x8 | 3.3467 | [3.3346, 3.3632] | 0.0000 [0.0000, 0.0000] |
| 2 | 264x256x8 | 3.3769 | [3.3651, 3.3929] | 0.0308 [0.0200, 0.0408] |
| 3 | 264x256x8 | 3.3798 | [3.3533, 3.3881] | 0.0291 [0.0057, 0.0497] |
| 4 | 1056x128x8 | 3.3811 | [3.3588, 3.4122] | 0.0344 [0.0136, 0.0539] |
| 5 | 132x256x8 | 3.3812 | [3.3680, 3.3925] | 0.0308 [0.0163, 0.0416] |

## route/footprint-mib=1024,kernel=k6,layout=line,placement=hbm,tune=direct,type=tune,update=atomic

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 528x256x8 | 0.3375 | [0.3367, 0.3376] | 0.0000 [0.0000, 0.0000] |
| 2 | 132x512x8 | 0.3386 | [0.3384, 0.3393] | 0.0014 [0.0009, 0.0018] |
| 3 | 1056x128x8 | 0.3389 | [0.3387, 0.3395] | 0.0015 [0.0012, 0.0024] |
| 4 | 264x128x8 | 0.3390 | [0.3388, 0.3394] | 0.0015 [0.0011, 0.0024] |
| 5 | 528x256x8 | 0.3390 | [0.3387, 0.3396] | 0.0017 [0.0014, 0.0023] |

## route/footprint-mib=1024,kernel=k6,placement=cpu,tune=copy,type=tune,update=atomic

- 60 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-whole-none-whole-kernel | 6.5727 | [6.5681, 6.5768] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-whole-none-whole-kernel | 6.5728 | [6.5676, 6.5765] | 0.0005 [-0.0093, 0.0073] |
| 3 | ce-registered-4-whole-none-whole-kernel | 6.5731 | [6.5674, 6.5760] | 0.0012 [-0.0046, 0.0044] |
| 4 | ce-registered-1-256m-none-whole-kernel | 6.5820 | [6.5789, 6.5852] | 0.0101 [0.0021, 0.0165] |
| 5 | ce-registered-4-256m-none-whole-kernel | 6.5831 | [6.5812, 6.5861] | 0.0111 [0.0053, 0.0159] |
| 35 | ce-pageable-1-whole-none-whole | 7.3975 | [7.3943, 7.3987] | 0.8249 [0.8175, 0.8306] |

## route/footprint-mib=1024,kernel=k6,placement=cpu,tune=copy-kernel,type=tune,update=atomic

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x1024x8 | 7.0702 | [7.0658, 7.0750] | 0.0000 [0.0000, 0.0000] |
| 2 | 264x1024x8 | 7.0714 | [7.0692, 7.0767] | 0.0018 [-0.0018, 0.0062] |
| 3 | 132x512x8 | 7.0714 | [7.0696, 7.0738] | 0.0022 [-0.0038, 0.0061] |
| 4 | 264x512x8 | 7.0741 | [7.0697, 7.0773] | 0.0030 [-0.0024, 0.0091] |
| 5 | 264x512x8 | 7.0758 | [7.0727, 7.0794] | 0.0048 [0.0026, 0.0104] |

## route/footprint-mib=1024,kernel=k6,placement=cpu,tune=direct,type=tune,update=atomic

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x1024x8 | 5.5807 | [5.5770, 5.5837] | 0.0000 [0.0000, 0.0000] |
| 2 | 2112x1024x8 | 5.6025 | [5.5998, 5.6042] | 0.0210 [0.0163, 0.0243] |
| 3 | 1056x1024x8 | 5.6088 | [5.6051, 5.6105] | 0.0271 [0.0247, 0.0308] |
| 4 | 1056x1024x8 | 5.6111 | [5.6080, 5.6136] | 0.0302 [0.0276, 0.0349] |
| 5 | 528x1024x8 | 5.6149 | [5.6121, 5.6171] | 0.0343 [0.0317, 0.0362] |

## route/footprint-mib=1024,kernel=k6,placement=cpu,tune=direct,type=tune,update=plain

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 2112x1024x8 | 5.5552 | [5.5522, 5.5572] | 0.0000 [0.0000, 0.0000] |
| 2 | 132x512x8 | 5.5633 | [5.5520, 5.6076] | 0.0070 [-0.0021, 0.0504] |
| 3 | 1056x1024x8 | 5.5679 | [5.5658, 5.5702] | 0.0136 [0.0084, 0.0177] |
| 4 | 1056x1024x8 | 5.5691 | [5.5673, 5.5728] | 0.0146 [0.0106, 0.0190] |
| 5 | 4224x512x8 | 5.5692 | [5.5660, 5.5710] | 0.0156 [0.0101, 0.0177] |

## route/footprint-mib=1024,kernel=k6,placement=cpu,tune=direct,type=tune,update=returned

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x512x8 | 5.5794 | [5.5774, 5.5838] | 0.0000 [0.0000, 0.0000] |
| 2 | 264x256x8 | 5.5840 | [5.5818, 5.5863] | 0.0040 [0.0003, 0.0070] |
| 3 | 264x256x8 | 5.5859 | [5.5829, 5.5910] | 0.0062 [0.0010, 0.0136] |
| 4 | 2112x1024x8 | 5.6111 | [5.6099, 5.6145] | 0.0317 [0.0280, 0.0343] |
| 5 | 4224x512x8 | 5.6276 | [5.6234, 5.6287] | 0.0477 [0.0426, 0.0506] |

## route/footprint-mib=1024,kernel=k6,placement=hbm,tune=copy,type=tune,update=atomic

- 60 configurations, 100 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole-kernel | 2.1031 | [2.1026, 2.1037] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-whole-kernel | 2.1041 | [2.1037, 2.1048] | 0.0011 [0.0006, 0.0017] |
| 3 | kernel-registered-1-256m-none-whole-kernel | 2.1235 | [2.1232, 2.1242] | 0.0205 [0.0198, 0.0215] |
| 4 | kernel-pageable-1-256m-none-whole-kernel | 2.1261 | [2.1258, 2.1269] | 0.0228 [0.0220, 0.0237] |
| 5 | kernel-registered-1-64m-none-whole-kernel | 2.1684 | [2.1676, 2.1692] | 0.0653 [0.0645, 0.0659] |
| 45 | ce-pageable-1-whole-none-whole | 6.6024 | [6.6018, 6.6030] | 4.4989 [4.4984, 4.4998] |

## route/footprint-mib=1024,kernel=k6,placement=hbm,tune=direct,type=tune,update=atomic

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x1024x8 | 0.8172 | [0.8166, 0.8186] | 0.0000 [0.0000, 0.0000] |
| 2 | 264x1024x8 | 0.8181 | [0.8173, 0.8200] | 0.0009 [-0.0004, 0.0015] |
| 3 | 528x1024x8 | 0.8193 | [0.8187, 0.8198] | 0.0016 [0.0003, 0.0033] |
| 4 | 264x1024x8 | 0.8193 | [0.8188, 0.8203] | 0.0020 [0.0005, 0.0035] |
| 5 | 2112x1024x8 | 0.8199 | [0.8193, 0.8204] | 0.0026 [0.0009, 0.0033] |

## route/footprint-mib=1024,kernel=k6,placement=hbm,tune=direct,type=tune,update=plain

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 1056x256x8 | 0.6505 | [0.6504, 0.6507] | 0.0000 [0.0000, 0.0000] |
| 2 | 8448x128x8 | 0.6509 | [0.6505, 0.6511] | 0.0004 [0.0001, 0.0007] |
| 3 | 1056x512x8 | 0.6509 | [0.6505, 0.6511] | 0.0004 [0.0000, 0.0006] |
| 4 | 2112x512x8 | 0.6511 | [0.6510, 0.6515] | 0.0006 [0.0003, 0.0012] |
| 5 | 2112x256x8 | 0.6512 | [0.6508, 0.6515] | 0.0006 [0.0003, 0.0014] |

## route/footprint-mib=1024,kernel=k6,placement=hbm,tune=direct,type=tune,update=returned

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 4224x512x8 | 0.8070 | [0.8057, 0.8079] | 0.0000 [0.0000, 0.0000] |
| 2 | 2112x1024x8 | 0.8082 | [0.8077, 0.8092] | 0.0015 [0.0007, 0.0026] |
| 3 | 16896x128x8 | 0.8120 | [0.8116, 0.8130] | 0.0048 [0.0043, 0.0072] |
| 4 | 8448x256x8 | 0.8121 | [0.8114, 0.8125] | 0.0052 [0.0044, 0.0064] |
| 5 | 1056x1024x8 | 0.8155 | [0.8145, 0.8161] | 0.0088 [0.0073, 0.0100] |

## route/footprint-mib=16,kernel=k6,placement=hbm,tune=copy,type=tune,update=atomic

- 60 configurations, 40 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-16m-none-whole-kernel | 0.0957 | [0.0956, 0.0957] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-256m-none-whole-kernel | 0.0957 | [0.0956, 0.0957] | -0.0000 [-0.0000, 0.0000] |
| 3 | kernel-registered-1-whole-none-whole-kernel | 0.0957 | [0.0956, 0.0957] | -0.0000 [-0.0000, 0.0000] |
| 4 | kernel-registered-1-64m-none-whole-kernel | 0.0957 | [0.0956, 0.0957] | -0.0000 [-0.0000, 0.0000] |
| 5 | kernel-pageable-1-64m-none-whole-kernel | 0.0958 | [0.0958, 0.0958] | 0.0001 [0.0001, 0.0001] |
| 59 | ce-pageable-1-whole-none-whole | 0.1946 | [0.1944, 0.1948] | 0.0989 [0.0987, 0.0991] |

## route/footprint-mib=16,kernel=k6,placement=hbm,tune=direct,type=tune,update=atomic

- 52 configurations, 100 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x512x8 | 0.0737 | [0.0736, 0.0751] | 0.0000 [0.0000, 0.0000] |
| 2 | 264x1024x8 | 0.0740 | [0.0737, 0.0744] | -0.0001 [-0.0007, 0.0003] |
| 3 | 264x512x8 | 0.0745 | [0.0731, 0.0757] | -0.0003 [-0.0005, 0.0005] |
| 4 | 528x256x8 | 0.0746 | [0.0745, 0.0747] | 0.0008 [-0.0005, 0.0010] |
| 5 | 1056x1024x8 | 0.0751 | [0.0751, 0.0751] | 0.0014 [-0.0000, 0.0015] |

## route/footprint-mib=16384,generator=uniform,kernel=k4,placement=cpu,tune=copy,type=tune

- 108 configurations, 80 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-1-256m-pipe-whole-kernel | 45.2014 | [45.1971, 45.2053] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-4-256m-pipe-whole-kernel | 45.2034 | [45.1991, 45.2062] | -0.0021 [-0.0066, 0.0072] |
| 3 | ce-registered-2-256m-pipe-whole-kernel | 45.2041 | [45.1992, 45.2096] | 0.0035 [-0.0019, 0.0071] |
| 4 | ce-registered-4-256m-pipe-whole | 45.5846 | [45.5827, 45.5878] | 0.3842 [0.3743, 0.3891] |
| 5 | ce-registered-1-256m-pipe-whole | 45.5860 | [45.5809, 45.5886] | 0.3824 [0.3786, 0.3910] |
| 62 | ce-pageable-1-whole-none-whole | 77.9395 | [77.9346, 77.9455] | 32.7415 [32.7323, 32.7463] |

## route/footprint-mib=16384,generator=uniform,kernel=k4,placement=hbm,tune=copy,type=tune

- 108 configurations, 50 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-whole-kernel | 42.3711 | [42.3625, 42.3763] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole-kernel | 42.3733 | [42.3674, 42.3830] | 0.0063 [-0.0068, 0.0166] |
| 3 | kernel-registered-1-256m-none-whole-kernel | 42.8484 | [42.8406, 42.8561] | 0.4700 [0.4628, 0.4952] |
| 4 | kernel-pageable-1-256m-none-whole-kernel | 42.8640 | [42.8524, 42.8782] | 0.4980 [0.4783, 0.5078] |
| 5 | kernel-registered-1-64m-none-whole-kernel | 43.5923 | [43.5756, 43.6050] | 1.2237 [1.2093, 1.2346] |
| 75 | ce-pageable-1-whole-none-whole | 74.6159 | [74.6021, 74.6204] | 32.2402 [32.2237, 32.2567] |

## route/footprint-mib=16384,generator=uniform,kernel=k4,placement=hbm,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 264x128x8 | 32.2423 | [32.2268, 32.2672] | 0.0000 [0.0000, 0.0000] |
| 2 | 132x256x8 | 32.2505 | [32.2396, 32.2703] | 0.0149 [-0.0261, 0.0419] |
| 3 | 132x512x8 | 35.2718 | [35.2032, 35.3286] | 3.0295 [2.9374, 3.0774] |
| 4 | 264x256x8 | 35.3577 | [35.3348, 35.3757] | 3.1145 [3.0677, 3.1513] |
| 5 | 528x128x8 | 35.3979 | [35.3598, 35.4478] | 3.1414 [3.1148, 3.2324] |

## route/footprint-mib=24576,generator=uniform,kernel=k4,placement=cpu,tune=copy,type=tune

- 108 configurations, 50 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-1-256m-pipe-whole-kernel | 72.8928 | [72.8690, 72.9409] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-4-256m-pipe-whole-kernel | 72.8987 | [72.8603, 72.9519] | 0.0315 [-0.0246, 0.0696] |
| 3 | ce-registered-2-256m-pipe-whole-kernel | 72.9209 | [72.8888, 72.9578] | 0.0316 [-0.0166, 0.0796] |
| 4 | ce-registered-4-256m-pipe-whole | 73.5346 | [73.5191, 73.5794] | 0.6698 [0.5942, 0.7113] |
| 5 | ce-registered-1-256m-pipe-whole | 73.5373 | [73.5020, 73.5878] | 0.6558 [0.5884, 0.7148] |
| 50 | ce-pageable-1-whole-none-whole | 115.6093 | [115.6049, 115.6214] | 42.7220 [42.6832, 42.7584] |

## route/footprint-mib=256,generator=uniform,kernel=k4,placement=cpu,tune=copy,type=tune

- 108 configurations, 50 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-4-64m-pipe-whole-kernel | 0.9054 | [0.9052, 0.9058] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-64m-pipe-whole-kernel | 0.9057 | [0.9054, 0.9060] | 0.0003 [-0.0001, 0.0006] |
| 3 | ce-registered-2-64m-pipe-whole-kernel | 0.9058 | [0.9054, 0.9060] | 0.0004 [0.0001, 0.0006] |
| 4 | ce-registered-1-64m-pipe-whole | 0.9157 | [0.9154, 0.9159] | 0.0104 [0.0099, 0.0106] |
| 5 | ce-registered-2-64m-pipe-whole | 0.9161 | [0.9159, 0.9164] | 0.0106 [0.0104, 0.0110] |
| 52 | ce-pageable-1-whole-none-whole | 1.0170 | [1.0166, 1.0174] | 0.1115 [0.1111, 0.1122] |

## route/footprint-mib=256,generator=uniform,kernel=k4,placement=cpu,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x256x8 | 7.3916 | [7.3881, 7.3988] | 0.0000 [0.0000, 0.0000] |
| 2 | 264x128x8 | 7.4356 | [7.4308, 7.4409] | 0.0460 [0.0367, 0.0466] |
| 3 | 132x512x8 | 7.7147 | [7.7053, 7.7358] | 0.3257 [0.3135, 0.3357] |
| 4 | 264x256x8 | 7.8907 | [7.8841, 7.8982] | 0.4969 [0.4833, 0.5096] |
| 5 | 264x256x8 | 7.8926 | [7.8757, 7.9067] | 0.5002 [0.4871, 0.5110] |

## route/footprint-mib=256,generator=uniform,kernel=k4,placement=hbm,tune=copy,type=tune

- 108 configurations, 80 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-whole-kernel | 0.3782 | [0.3780, 0.3783] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-256m-none-whole-kernel | 0.3782 | [0.3781, 0.3784] | 0.0000 [-0.0001, 0.0003] |
| 3 | kernel-registered-1-256m-none-whole-kernel | 0.3788 | [0.3786, 0.3790] | 0.0007 [0.0005, 0.0010] |
| 4 | kernel-registered-1-whole-none-whole-kernel | 0.3789 | [0.3788, 0.3790] | 0.0007 [0.0005, 0.0009] |
| 5 | kernel-pageable-1-64m-none-whole-kernel | 0.3875 | [0.3873, 0.3877] | 0.0094 [0.0092, 0.0097] |
| 67 | ce-pageable-1-whole-none-whole | 0.8874 | [0.8873, 0.8877] | 0.5093 [0.5090, 0.5096] |

## route/footprint-mib=256,generator=uniform,kernel=k4,placement=hbm,tune=direct,type=tune

- 52 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x512x8 | 0.1932 | [0.1931, 0.1934] | 0.0000 [0.0000, 0.0000] |
| 2 | 264x256x8 | 0.1991 | [0.1987, 0.1999] | 0.0060 [0.0056, 0.0065] |
| 3 | 264x256x8 | 0.1991 | [0.1986, 0.1996] | 0.0058 [0.0056, 0.0064] |
| 4 | 528x128x8 | 0.2039 | [0.2028, 0.2044] | 0.0110 [0.0095, 0.0111] |
| 5 | 528x128x8 | 0.2044 | [0.2036, 0.2046] | 0.0112 [0.0102, 0.0115] |

## route/footprint-mib=256,kernel=k6,placement=cpu,tune=copy,type=tune,update=atomic

- 60 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-256m-none-whole-kernel | 1.6719 | [1.6712, 1.6735] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole-kernel | 1.6722 | [1.6716, 1.6738] | 0.0004 [-0.0010, 0.0017] |
| 3 | kernel-pageable-1-256m-none-whole-kernel | 1.6754 | [1.6747, 1.6769] | 0.0031 [0.0020, 0.0053] |
| 4 | kernel-pageable-1-whole-none-whole-kernel | 1.6758 | [1.6749, 1.6766] | 0.0038 [0.0023, 0.0045] |
| 5 | ce-registered-1-whole-none-whole-kernel | 1.6844 | [1.6836, 1.6871] | 0.0121 [0.0110, 0.0145] |
| 36 | ce-pageable-1-whole-none-whole | 1.8760 | [1.8756, 1.8765] | 0.2039 [0.2021, 0.2049] |

## route/footprint-mib=256,kernel=k6,placement=cpu,tune=direct,type=tune,update=atomic

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x1024x8 | 1.3875 | [1.3870, 1.3892] | 0.0000 [0.0000, 0.0000] |
| 2 | 264x1024x8 | 1.3925 | [1.3914, 1.3938] | 0.0050 [0.0036, 0.0062] |
| 3 | 264x1024x8 | 1.3930 | [1.3919, 1.3942] | 0.0051 [0.0040, 0.0066] |
| 4 | 528x1024x8 | 1.3952 | [1.3940, 1.3960] | 0.0076 [0.0057, 0.0087] |
| 5 | 528x1024x8 | 1.3953 | [1.3946, 1.3960] | 0.0078 [0.0068, 0.0086] |

## route/footprint-mib=256,kernel=k6,placement=hbm,tune=copy,type=tune,update=atomic

- 60 configurations, 30 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-256m-none-whole-kernel | 0.5331 | [0.5327, 0.5338] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-whole-kernel | 0.5333 | [0.5326, 0.5340] | 0.0004 [-0.0004, 0.0007] |
| 3 | kernel-registered-1-whole-none-whole-kernel | 0.5342 | [0.5336, 0.5348] | 0.0005 [0.0001, 0.0014] |
| 4 | kernel-registered-1-256m-none-whole-kernel | 0.5345 | [0.5341, 0.5350] | 0.0013 [0.0002, 0.0019] |
| 5 | kernel-pageable-1-64m-none-whole-kernel | 0.5434 | [0.5431, 0.5440] | 0.0106 [0.0097, 0.0111] |
| 48 | ce-pageable-1-whole-none-whole | 1.6595 | [1.6587, 1.6599] | 1.1263 [1.1249, 1.1270] |

## route/footprint-mib=256,kernel=k6,placement=hbm,tune=direct,type=tune,update=atomic

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 2112x1024x8 | 0.2036 | [0.2035, 0.2037] | 0.0000 [0.0000, 0.0000] |
| 2 | 16896x128x8 | 0.2039 | [0.2037, 0.2040] | 0.0003 [0.0002, 0.0004] |
| 3 | 8448x256x8 | 0.2039 | [0.2038, 0.2040] | 0.0003 [0.0002, 0.0005] |
| 4 | 1056x1024x8 | 0.2045 | [0.2043, 0.2046] | 0.0009 [0.0007, 0.0011] |
| 5 | 528x1024x8 | 0.2045 | [0.2044, 0.2047] | 0.0009 [0.0007, 0.0011] |

## route/footprint-mib=32768,generator=uniform,kernel=k4,placement=cpu,tune=copy,type=tune

- 108 configurations, 60 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-4-256m-pipe-whole-kernel | 89.5632 | [89.5525, 89.5743] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-256m-pipe-whole-kernel | 89.5651 | [89.5513, 89.5743] | -0.0079 [-0.0193, 0.0121] |
| 3 | ce-registered-2-256m-pipe-whole-kernel | 89.5710 | [89.5583, 89.5756] | 0.0035 [-0.0132, 0.0179] |
| 4 | ce-registered-2-256m-pipe-whole | 90.7433 | [90.7352, 90.7573] | 1.1757 [1.1641, 1.1986] |
| 5 | ce-registered-4-256m-pipe-whole | 90.7505 | [90.7370, 90.7599] | 1.1847 [1.1727, 1.1983] |
| 50 | ce-pageable-1-whole-none-whole | 153.6104 | [153.6053, 153.6204] | 64.0487 [64.0285, 64.0622] |

## route/footprint-mib=32768,generator=uniform,kernel=k4,placement=cpu,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 264x128x8 | 970.6692 | [970.4021, 970.8442] | 0.0000 [0.0000, 0.0000] |
| 2 | 132x256x8 | 970.7042 | [970.5820, 970.7913] | 0.0486 [-0.3069, 0.2985] |
| 3 | 132x512x8 | 1040.0365 | [1039.9188, 1040.1204] | 69.4428 [69.0642, 69.6179] |
| 4 | 528x128x8 | 1053.8332 | [1053.7592, 1053.9458] | 83.2392 [82.8679, 83.4192] |
| 5 | 528x128x8 | 1053.9090 | [1053.5852, 1054.0349] | 83.2748 [82.8892, 83.5014] |

## route/footprint-mib=4096,generator=uniform,kernel=k4,placement=cpu,tune=copy,type=tune

- 108 configurations, 90 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-1-256m-pipe-whole-kernel | 12.2692 | [12.2677, 12.2705] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-2-256m-pipe-whole-kernel | 12.2699 | [12.2686, 12.2715] | 0.0020 [0.0006, 0.0032] |
| 3 | ce-registered-4-256m-pipe-whole-kernel | 12.2701 | [12.2684, 12.2717] | 0.0016 [-0.0012, 0.0032] |
| 4 | ce-registered-1-256m-pipe-whole | 12.3683 | [12.3666, 12.3702] | 0.0986 [0.0974, 0.1011] |
| 5 | ce-registered-2-256m-pipe-whole | 12.3686 | [12.3675, 12.3700] | 0.1009 [0.0992, 0.1018] |
| 57 | ce-pageable-1-whole-none-whole | 19.0917 | [19.0905, 19.0933] | 6.8234 [6.8198, 6.8260] |

## route/footprint-mib=4096,generator=uniform,kernel=k4,placement=hbm,tune=copy,type=tune

- 108 configurations, 90 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-whole-kernel | 9.5798 | [9.5786, 9.5810] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole-kernel | 9.5822 | [9.5801, 9.5837] | 0.0024 [0.0006, 0.0042] |
| 3 | kernel-registered-1-256m-none-whole-kernel | 9.6916 | [9.6901, 9.6935] | 0.1114 [0.1094, 0.1146] |
| 4 | kernel-pageable-1-256m-none-whole-kernel | 9.6943 | [9.6929, 9.6951] | 0.1147 [0.1119, 0.1161] |
| 5 | kernel-registered-1-64m-none-whole-kernel | 9.8704 | [9.8693, 9.8722] | 0.2907 [0.2875, 0.2930] |
| 69 | ce-pageable-1-whole-none-whole | 17.5145 | [17.5126, 17.5167] | 7.9347 [7.9307, 7.9370] |

## route/footprint-mib=4096,kernel=k6,placement=cpu,tune=copy,type=tune,update=atomic

- 60 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-whole-none-whole-kernel | 26.0263 | [26.0133, 26.0576] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-whole-none-whole-kernel | 26.0331 | [26.0276, 26.0449] | 0.0065 [-0.0043, 0.0285] |
| 3 | ce-registered-4-whole-none-whole-kernel | 26.0425 | [26.0267, 26.0458] | 0.0160 [-0.0119, 0.0271] |
| 4 | ce-registered-1-256m-none-whole-kernel | 26.0838 | [26.0772, 26.1024] | 0.0556 [0.0340, 0.0718] |
| 5 | ce-registered-2-256m-none-whole-kernel | 26.0912 | [26.0788, 26.1086] | 0.0718 [0.0265, 0.0869] |
| 37 | ce-pageable-1-whole-none-whole | 29.3902 | [29.3751, 29.4049] | 3.3616 [3.3452, 3.3886] |

## route/footprint-mib=4096,kernel=k6,placement=cpu,tune=direct,type=tune,update=atomic

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x1024x8 | 22.5093 | [22.4826, 22.5434] | 0.0000 [0.0000, 0.0000] |
| 2 | 2112x1024x8 | 22.6140 | [22.5974, 22.6224] | 0.1042 [0.0789, 0.1283] |
| 3 | 1056x1024x8 | 22.6885 | [22.6849, 22.7031] | 0.1772 [0.1437, 0.2233] |
| 4 | 1056x1024x8 | 22.6903 | [22.6704, 22.7046] | 0.1700 [0.1502, 0.2149] |
| 5 | 264x512x8 | 22.6990 | [22.6763, 22.7251] | 0.1994 [0.1363, 0.2237] |

## route/footprint-mib=4096,kernel=k6,placement=hbm,tune=copy,type=tune,update=atomic

- 60 configurations, 100 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole-kernel | 8.3712 | [8.3652, 8.3745] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-whole-kernel | 8.3888 | [8.3854, 8.3905] | 0.0153 [0.0130, 0.0234] |
| 3 | kernel-pageable-1-256m-none-whole-kernel | 8.4826 | [8.4808, 8.4852] | 0.1116 [0.1078, 0.1161] |
| 4 | kernel-registered-1-256m-none-whole-kernel | 8.4832 | [8.4802, 8.4850] | 0.1124 [0.1078, 0.1151] |
| 5 | kernel-registered-1-64m-none-whole-kernel | 8.6582 | [8.6557, 8.6604] | 0.2904 [0.2850, 0.2936] |
| 44 | ce-pageable-1-whole-none-whole | 26.3928 | [26.3780, 26.4018] | 18.0212 [18.0124, 18.0337] |

## route/footprint-mib=4096,kernel=k6,placement=hbm,tune=direct,type=tune,update=atomic

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x1024x8 | 3.2734 | [3.2716, 3.2766] | 0.0000 [0.0000, 0.0000] |
| 2 | 264x1024x8 | 3.2833 | [3.2791, 3.2884] | 0.0110 [0.0045, 0.0155] |
| 3 | 264x1024x8 | 3.2842 | [3.2791, 3.2865] | 0.0101 [0.0052, 0.0149] |
| 4 | 528x1024x8 | 3.2926 | [3.2888, 3.2987] | 0.0184 [0.0130, 0.0255] |
| 5 | 528x1024x8 | 3.2935 | [3.2892, 3.2944] | 0.0197 [0.0139, 0.0225] |

## route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=1,tiling=none,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x256x8 | 5.7147 | [5.7076, 5.7213] | 0.0000 [0.0000, 0.0000] |
| 2 | 264x128x8 | 5.8580 | [5.8551, 5.8674] | 0.1444 [0.1393, 0.1550] |
| 3 | 2112x1024x8 | 5.9505 | [5.9474, 5.9529] | 0.2343 [0.2282, 0.2454] |
| 4 | 4224x512x8 | 5.9842 | [5.9817, 5.9853] | 0.2694 [0.2628, 0.2775] |
| 5 | 8448x256x8 | 6.0217 | [6.0196, 6.0244] | 0.3086 [0.3032, 0.3120] |

## route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=1,tiling=tiles,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-64m-pipe-whole-kernel | 3.0416 | [3.0388, 3.0451] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-64m-pipe-whole-kernel | 3.0446 | [3.0430, 3.0467] | 0.0024 [-0.0005, 0.0064] |
| 3 | ce-registered-4-64m-pipe-whole-kernel | 3.0449 | [3.0413, 3.0454] | 0.0020 [-0.0037, 0.0064] |
| 4 | ce-registered-2-16m-pipe-whole-kernel | 3.0786 | [3.0768, 3.0802] | 0.0370 [0.0330, 0.0395] |
| 5 | ce-registered-4-16m-pipe-whole-kernel | 3.0802 | [3.0779, 3.0841] | 0.0391 [0.0331, 0.0453] |
| 74 | ce-pageable-1-whole-none-whole | 3.7382 | [3.7369, 3.7407] | 0.6969 [0.6928, 0.6993] |

## route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=16,tiling=tiles,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-64m-pipe-whole-kernel | 9.0505 | [9.0294, 9.0591] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-4-64m-pipe-whole-kernel | 9.0524 | [9.0336, 9.0608] | -0.0047 [-0.0138, 0.0314] |
| 3 | ce-registered-1-64m-pipe-whole-kernel | 9.0534 | [9.0481, 9.0615] | 0.0074 [-0.0113, 0.0223] |
| 4 | ce-registered-2-16m-pipe-whole-kernel | 9.0943 | [9.0745, 9.1074] | 0.0470 [0.0337, 0.0617] |
| 5 | ce-registered-1-16m-pipe-whole-kernel | 9.0957 | [9.0907, 9.1029] | 0.0448 [0.0384, 0.0623] |
| 78 | ce-pageable-1-whole-none-whole | 9.7827 | [9.7642, 9.7845] | 0.7269 [0.7139, 0.7533] |

## route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=2,tiling=tiles,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-1-64m-pipe-whole-kernel | 3.4392 | [3.4373, 3.4432] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-2-64m-pipe-whole-kernel | 3.4410 | [3.4387, 3.4433] | 0.0017 [-0.0034, 0.0083] |
| 3 | ce-registered-4-64m-pipe-whole-kernel | 3.4424 | [3.4391, 3.4433] | 0.0034 [-0.0049, 0.0051] |
| 4 | ce-registered-2-16m-pipe-whole-kernel | 3.4760 | [3.4746, 3.4827] | 0.0371 [0.0328, 0.0421] |
| 5 | ce-registered-1-16m-pipe-whole-kernel | 3.4775 | [3.4760, 3.4810] | 0.0380 [0.0340, 0.0415] |
| 75 | ce-pageable-1-whole-none-whole | 4.1449 | [4.1433, 4.1467] | 0.7043 [0.7015, 0.7089] |

## route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=4,tiling=tiles,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-4-64m-pipe-whole-kernel | 4.2248 | [4.2230, 4.2275] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-64m-pipe-whole-kernel | 4.2249 | [4.2219, 4.2263] | -0.0009 [-0.0039, 0.0025] |
| 3 | ce-registered-2-64m-pipe-whole-kernel | 4.2269 | [4.2233, 4.2309] | 0.0026 [-0.0030, 0.0061] |
| 4 | ce-registered-4-16m-pipe-whole-kernel | 4.2658 | [4.2631, 4.2679] | 0.0411 [0.0360, 0.0433] |
| 5 | ce-registered-1-16m-pipe-whole-kernel | 4.2670 | [4.2629, 4.2713] | 0.0417 [0.0377, 0.0471] |
| 76 | ce-pageable-1-whole-none-whole | 4.9443 | [4.9401, 4.9473] | 0.7183 [0.7170, 0.7232] |

## route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=64,tiling=none,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x256x8 | 335.7249 | [335.4618, 336.0716] | 0.0000 [0.0000, 0.0000] |
| 2 | 264x128x8 | 342.7105 | [342.5680, 342.9762] | 6.9172 [6.6159, 7.5071] |
| 3 | 2112x1024x8 | 373.0284 | [372.9414, 373.0526] | 37.2290 [36.9715, 37.6338] |
| 4 | 4224x512x8 | 375.0929 | [375.0269, 375.1728] | 39.3760 [38.9554, 39.6898] |
| 5 | 8448x256x8 | 377.6231 | [377.5555, 377.6535] | 41.8250 [41.5819, 42.1592] |

## route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=64,tiling=tiles,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-4-64m-pipe-whole-kernel | 28.2928 | [28.2742, 28.3120] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-2-64m-pipe-whole-kernel | 28.3045 | [28.2840, 28.3367] | 0.0065 [-0.0188, 0.0411] |
| 3 | ce-registered-1-64m-pipe-whole-kernel | 28.3055 | [28.2886, 28.3286] | 0.0155 [-0.0101, 0.0637] |
| 4 | ce-registered-2-16m-pipe-whole-kernel | 28.3468 | [28.3320, 28.3703] | 0.0575 [0.0315, 0.1060] |
| 5 | ce-registered-4-16m-pipe-whole-kernel | 28.3529 | [28.3330, 28.3743] | 0.0686 [0.0210, 0.0988] |
| 75 | ce-pageable-1-whole-none-whole | 29.0204 | [28.9985, 29.0383] | 0.7312 [0.6865, 0.7641] |

## route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=none,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-64m-pipe-whole-kernel | 5.3880 | [5.3827, 5.3972] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-4-64m-pipe-whole-kernel | 5.3891 | [5.3845, 5.3928] | 0.0013 [-0.0127, 0.0099] |
| 3 | ce-registered-1-64m-pipe-whole-kernel | 5.3900 | [5.3853, 5.3939] | 0.0005 [-0.0053, 0.0062] |
| 4 | ce-registered-1-16m-pipe-whole-kernel | 5.4341 | [5.4307, 5.4364] | 0.0465 [0.0335, 0.0528] |
| 5 | ce-registered-4-16m-pipe-whole-kernel | 5.4343 | [5.4295, 5.4383] | 0.0457 [0.0342, 0.0536] |
| 73 | ce-pageable-1-whole-none-whole | 6.0715 | [6.0688, 6.0800] | 0.6845 [0.6756, 0.6924] |

## route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=none,tune=copy-kernel,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 264x1024x8 | 6.0762 | [6.0736, 6.0832] | 0.0000 [0.0000, 0.0000] |
| 2 | 264x1024x8 | 6.0791 | [6.0747, 6.0850] | 0.0039 [-0.0085, 0.0096] |
| 3 | 1056x256x8 | 6.0798 | [6.0774, 6.0858] | 0.0032 [0.0010, 0.0054] |
| 4 | 528x512x8 | 6.0809 | [6.0785, 6.0871] | 0.0051 [-0.0037, 0.0087] |
| 5 | 528x512x8 | 6.0815 | [6.0780, 6.0856] | 0.0068 [-0.0021, 0.0086] |

## route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=none,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 132x256x8 | 42.2496 | [42.1661, 42.2734] | 0.0000 [0.0000, 0.0000] |
| 2 | 264x128x8 | 43.1019 | [43.0250, 43.1542] | 0.8405 [0.7684, 0.9959] |
| 3 | 2112x1024x8 | 46.6732 | [46.6600, 46.6846] | 4.4241 [4.4087, 4.5009] |
| 4 | 4224x512x8 | 46.9543 | [46.9401, 46.9832] | 4.7224 [4.6667, 4.7707] |
| 5 | 8448x256x8 | 47.2508 | [47.2367, 47.2707] | 5.0131 [4.9827, 5.0888] |

## route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-4-64m-pipe-whole-kernel | 5.8452 | [5.8426, 5.8556] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-2-64m-pipe-whole-kernel | 5.8468 | [5.8416, 5.8501] | -0.0005 [-0.0078, 0.0035] |
| 3 | ce-registered-1-64m-pipe-whole-kernel | 5.8478 | [5.8427, 5.8503] | 0.0017 [-0.0129, 0.0085] |
| 4 | ce-registered-2-16m-pipe-whole-kernel | 5.8904 | [5.8841, 5.8962] | 0.0450 [0.0279, 0.0484] |
| 5 | ce-registered-4-16m-pipe-whole-kernel | 5.8910 | [5.8855, 5.8957] | 0.0401 [0.0354, 0.0510] |
| 76 | ce-pageable-1-whole-none-whole | 6.5551 | [6.5511, 6.5597] | 0.7071 [0.6986, 0.7151] |

## route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=1,tiling=none,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 264x1024x8 | 0.3433 | [0.3429, 0.3437] | 0.0000 [0.0000, 0.0000] |
| 2 | 264x1024x8 | 0.3437 | [0.3433, 0.3439] | 0.0002 [-0.0001, 0.0009] |
| 3 | 528x512x8 | 0.3454 | [0.3451, 0.3459] | 0.0022 [0.0015, 0.0030] |
| 4 | 528x512x8 | 0.3456 | [0.3452, 0.3460] | 0.0023 [0.0014, 0.0030] |
| 5 | 528x512x8 | 0.3457 | [0.3449, 0.3459] | 0.0024 [0.0016, 0.0026] |

## route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=1,tiling=tiles,tune=copy,type=tune

- 108 configurations, 70 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole-kernel | 1.0429 | [1.0427, 1.0432] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-whole-kernel | 1.0450 | [1.0447, 1.0452] | 0.0021 [0.0013, 0.0025] |
| 3 | kernel-registered-1-256m-none-whole-kernel | 1.0492 | [1.0490, 1.0497] | 0.0064 [0.0058, 0.0066] |
| 4 | kernel-pageable-1-256m-none-whole-kernel | 1.0514 | [1.0508, 1.0518] | 0.0083 [0.0080, 0.0087] |
| 5 | kernel-registered-1-64m-none-whole-kernel | 1.0721 | [1.0718, 1.0724] | 0.0294 [0.0287, 0.0296] |
| 85 | ce-pageable-1-whole-none-whole | 3.3202 | [3.3191, 3.3239] | 2.2775 [2.2765, 2.2812] |

## route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=16,tiling=tiles,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-whole-kernel | 7.0894 | [7.0847, 7.0955] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-256m-none-whole-kernel | 7.0922 | [7.0798, 7.1028] | 0.0019 [-0.0108, 0.0156] |
| 3 | kernel-registered-1-whole-none-whole-kernel | 7.0952 | [7.0842, 7.0981] | 0.0021 [-0.0072, 0.0128] |
| 4 | kernel-pageable-1-256m-none-whole-kernel | 7.0959 | [7.0894, 7.1051] | 0.0057 [-0.0061, 0.0161] |
| 5 | kernel-registered-1-64m-none-whole-kernel | 7.1184 | [7.1078, 7.1265] | 0.0271 [0.0145, 0.0374] |
| 81 | ce-pageable-1-whole-none-whole | 9.3521 | [9.3482, 9.3596] | 2.2617 [2.2570, 2.2686] |

## route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=2,tiling=tiles,tune=copy,type=tune

- 108 configurations, 90 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole-kernel | 1.4506 | [1.4501, 1.4509] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-whole-kernel | 1.4515 | [1.4511, 1.4518] | 0.0012 [0.0005, 0.0017] |
| 3 | kernel-registered-1-256m-none-whole-kernel | 1.4571 | [1.4566, 1.4577] | 0.0067 [0.0063, 0.0071] |
| 4 | kernel-pageable-1-256m-none-whole-kernel | 1.4581 | [1.4576, 1.4586] | 0.0078 [0.0068, 0.0083] |
| 5 | kernel-registered-1-64m-none-whole-kernel | 1.4802 | [1.4799, 1.4804] | 0.0297 [0.0292, 0.0302] |
| 82 | ce-pageable-1-whole-none-whole | 3.7251 | [3.7246, 3.7254] | 2.2747 [2.2741, 2.2755] |

## route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=4,tiling=tiles,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole-kernel | 2.2591 | [2.2558, 2.2638] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-whole-kernel | 2.2629 | [2.2604, 2.2660] | 0.0045 [-0.0016, 0.0057] |
| 3 | kernel-registered-1-256m-none-whole-kernel | 2.2665 | [2.2645, 2.2693] | 0.0062 [0.0038, 0.0099] |
| 4 | kernel-pageable-1-256m-none-whole-kernel | 2.2681 | [2.2663, 2.2702] | 0.0084 [0.0046, 0.0145] |
| 5 | kernel-registered-1-64m-none-whole-kernel | 2.2861 | [2.2829, 2.2892] | 0.0264 [0.0211, 0.0302] |
| 85 | ce-pageable-1-whole-none-whole | 4.5316 | [4.5264, 4.5338] | 2.2712 [2.2640, 2.2776] |

## route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=64,tiling=none,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 264x1024x8 | 21.9977 | [21.9816, 22.0356] | 0.0000 [0.0000, 0.0000] |
| 2 | 264x1024x8 | 22.0024 | [21.9798, 22.0303] | 0.0062 [-0.0518, 0.0461] |
| 3 | 528x512x8 | 22.0138 | [21.9944, 22.0307] | 0.0047 [-0.0271, 0.0457] |
| 4 | 528x512x8 | 22.0139 | [21.9937, 22.0343] | 0.0188 [-0.0292, 0.0521] |
| 5 | 528x512x8 | 22.0217 | [21.9917, 22.0473] | 0.0030 [-0.0242, 0.0787] |

## route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=64,tiling=tiles,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-256m-none-whole-kernel | 26.3624 | [26.3529, 26.4325] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-whole-kernel | 26.3796 | [26.3489, 26.4380] | 0.0186 [-0.0332, 0.0504] |
| 3 | kernel-registered-1-whole-none-whole-kernel | 26.3808 | [26.3512, 26.4551] | 0.0024 [-0.0222, 0.0487] |
| 4 | kernel-registered-1-256m-none-whole-kernel | 26.3889 | [26.3553, 26.4235] | 0.0107 [-0.0309, 0.0337] |
| 5 | kernel-registered-1-64m-none-whole-kernel | 26.4012 | [26.3601, 26.4594] | 0.0275 [-0.0138, 0.0517] |
| 87 | ce-pageable-1-whole-none-whole | 28.6302 | [28.5814, 28.6599] | 2.2509 [2.1944, 2.2931] |

## route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=none,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-whole-kernel | 3.3852 | [3.3826, 3.3900] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole-kernel | 3.3878 | [3.3814, 3.3910] | 0.0040 [-0.0034, 0.0060] |
| 3 | kernel-pageable-1-256m-none-whole-kernel | 3.3899 | [3.3849, 3.3918] | 0.0039 [-0.0012, 0.0086] |
| 4 | kernel-registered-1-256m-none-whole-kernel | 3.3969 | [3.3931, 3.4007] | 0.0122 [0.0075, 0.0150] |
| 5 | kernel-pageable-1-64m-none-whole-kernel | 3.4120 | [3.4070, 3.4154] | 0.0261 [0.0189, 0.0304] |
| 77 | ce-pageable-1-whole-none-whole | 5.6561 | [5.6518, 5.6699] | 2.2716 [2.2654, 2.2780] |

## route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=none,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 264x1024x8 | 2.7499 | [2.7482, 2.7561] | 0.0000 [0.0000, 0.0000] |
| 2 | 264x1024x8 | 2.7506 | [2.7462, 2.7572] | -0.0009 [-0.0080, 0.0079] |
| 3 | 528x512x8 | 2.7564 | [2.7548, 2.7596] | 0.0059 [0.0001, 0.0103] |
| 4 | 528x512x8 | 2.7569 | [2.7548, 2.7599] | 0.0078 [-0.0012, 0.0101] |
| 5 | 528x512x8 | 2.7576 | [2.7545, 2.7598] | 0.0065 [0.0017, 0.0103] |

## route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole-kernel | 3.8699 | [3.8647, 3.8765] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-whole-kernel | 3.8718 | [3.8634, 3.8753] | -0.0006 [-0.0080, 0.0096] |
| 3 | kernel-pageable-1-256m-none-whole-kernel | 3.8749 | [3.8696, 3.8785] | 0.0039 [-0.0007, 0.0090] |
| 4 | kernel-registered-1-256m-none-whole-kernel | 3.8777 | [3.8751, 3.8826] | 0.0081 [0.0021, 0.0127] |
| 5 | kernel-registered-1-64m-none-whole-kernel | 3.8960 | [3.8897, 3.9029] | 0.0273 [0.0132, 0.0362] |
| 85 | ce-pageable-1-whole-none-whole | 6.1452 | [6.1421, 6.1479] | 2.2722 [2.2681, 2.2834] |

## route/footprint-mib=8,kernel=k6,keys=1,placement=cpu,strategy=warp,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 1056x512x8 | 5.9799 | [5.9797, 5.9804] | 0.0000 [0.0000, 0.0000] |
| 2 | 2112x512x8 | 5.9799 | [5.9797, 5.9802] | 0.0002 [-0.0006, 0.0003] |
| 3 | 8448x256x8 | 5.9799 | [5.9797, 5.9801] | 0.0001 [-0.0004, 0.0003] |
| 4 | 528x256x8 | 5.9799 | [5.9798, 5.9804] | 0.0001 [-0.0007, 0.0004] |
| 5 | 4224x128x8 | 5.9799 | [5.9799, 5.9801] | 0.0001 [-0.0006, 0.0004] |

## route/footprint-mib=8,kernel=k6,keys=1,placement=cpu,tune=copy,type=tune

- 60 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole-kernel | 12.3676 | [12.3652, 12.3710] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-16m-none-whole-kernel | 12.3683 | [12.3654, 12.3711] | -0.0011 [-0.0051, 0.0068] |
| 3 | kernel-registered-1-256m-none-whole-kernel | 12.3683 | [12.3663, 12.3705] | 0.0008 [-0.0035, 0.0030] |
| 4 | kernel-pageable-1-256m-none-whole-kernel | 12.3685 | [12.3669, 12.3722] | 0.0013 [-0.0029, 0.0052] |
| 5 | kernel-pageable-1-whole-none-whole-kernel | 12.3687 | [12.3663, 12.3702] | -0.0013 [-0.0032, 0.0045] |
| 56 | ce-pageable-1-whole-none-whole | 12.3891 | [12.3847, 12.3918] | 0.0200 [0.0136, 0.0259] |

## route/footprint-mib=8,kernel=k6,keys=1,placement=cpu,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 2112x1024x8 | 191.3084 | [191.3073, 191.3099] | 0.0000 [0.0000, 0.0000] |
| 2 | 528x512x8 | 191.3089 | [191.3074, 191.3108] | 0.0003 [-0.0018, 0.0026] |
| 3 | 264x1024x8 | 191.3091 | [191.3058, 191.3113] | 0.0004 [-0.0025, 0.0030] |
| 4 | 1056x1024x8 | 191.3091 | [191.3082, 191.3121] | 0.0013 [-0.0018, 0.0041] |
| 5 | 1056x128x8 | 191.3091 | [191.3077, 191.3104] | 0.0010 [-0.0015, 0.0022] |

## route/footprint-mib=8,kernel=k6,keys=1,placement=hbm,strategy=warp,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 16896x128x8 | 0.4093 | [0.4093, 0.4094] | 0.0000 [0.0000, 0.0000] |
| 2 | 2112x1024x8 | 0.4097 | [0.4096, 0.4098] | 0.0004 [0.0003, 0.0005] |
| 3 | 4224x256x8 | 0.4098 | [0.4097, 0.4098] | 0.0004 [0.0003, 0.0005] |
| 4 | 1056x256x8 | 0.4098 | [0.4096, 0.4104] | 0.0006 [0.0003, 0.0010] |
| 5 | 1056x1024x8 | 0.4101 | [0.4100, 0.4102] | 0.0008 [0.0005, 0.0010] |

## route/footprint-mib=8,kernel=k6,keys=1,placement=hbm,tune=copy,type=tune

- 60 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-256m-none-whole-kernel | 12.3226 | [12.3209, 12.3251] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole-kernel | 12.3230 | [12.3210, 12.3269] | 0.0014 [-0.0020, 0.0035] |
| 3 | kernel-pageable-1-16m-none-whole-kernel | 12.3232 | [12.3214, 12.3259] | -0.0011 [-0.0034, 0.0050] |
| 4 | kernel-registered-1-256m-none-whole-kernel | 12.3232 | [12.3210, 12.3269] | 0.0001 [-0.0028, 0.0060] |
| 5 | kernel-registered-1-64m-none-whole-kernel | 12.3241 | [12.3227, 12.3254] | 0.0011 [-0.0024, 0.0049] |
| 58 | ce-pageable-1-whole-none-whole | 12.3768 | [12.3739, 12.3797] | 0.0545 [0.0496, 0.0569] |

## route/footprint-mib=8,kernel=k6,keys=1,placement=hbm,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 1056x1024x8 | 12.3036 | [12.3010, 12.3128] | 0.0000 [0.0000, 0.0000] |
| 2 | 8448x128x8 | 12.3039 | [12.3019, 12.3120] | 0.0010 [-0.0092, 0.0088] |
| 3 | 264x512x8 | 12.3051 | [12.3044, 12.3076] | 0.0013 [-0.0079, 0.0050] |
| 4 | 4224x512x8 | 12.3051 | [12.3035, 12.3099] | 0.0024 [-0.0093, 0.0073] |
| 5 | 1056x512x8 | 12.3053 | [12.3043, 12.3070] | 0.0018 [-0.0085, 0.0060] |

## route/footprint-mib=8,kernel=k6,keys=1024,placement=cpu,strategy=warp,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 528x512x8 | 12.2937 | [12.2860, 12.2971] | 0.0000 [0.0000, 0.0000] |
| 2 | 16896x128x8 | 12.2949 | [12.2863, 12.3027] | 0.0009 [-0.0063, 0.0112] |
| 3 | 1056x128x8 | 12.2960 | [12.2925, 12.2988] | 0.0032 [-0.0039, 0.0090] |
| 4 | 2112x128x8 | 12.2966 | [12.2957, 12.3017] | 0.0055 [-0.0028, 0.0110] |
| 5 | 1056x512x8 | 12.2966 | [12.2940, 12.3018] | 0.0040 [-0.0032, 0.0126] |

## route/footprint-mib=8,kernel=k6,keys=1024,placement=cpu,tune=copy,type=tune

- 60 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-16m-none-whole-kernel | 0.8219 | [0.8215, 0.8223] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-256m-none-whole-kernel | 0.8221 | [0.8220, 0.8223] | 0.0001 [-0.0001, 0.0005] |
| 3 | kernel-registered-1-whole-none-whole-kernel | 0.8221 | [0.8215, 0.8224] | -0.0000 [-0.0002, 0.0005] |
| 4 | kernel-registered-1-64m-none-whole-kernel | 0.8222 | [0.8220, 0.8223] | 0.0002 [-0.0001, 0.0008] |
| 5 | kernel-pageable-1-64m-none-whole-kernel | 0.8228 | [0.8226, 0.8230] | 0.0008 [0.0005, 0.0012] |
| 54 | ce-pageable-1-whole-none-whole | 0.8402 | [0.8397, 0.8412] | 0.0186 [0.0178, 0.0192] |

## route/footprint-mib=8,kernel=k6,keys=1024,placement=cpu,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 2112x128x8 | 12.4741 | [12.4693, 12.4782] | 0.0000 [0.0000, 0.0000] |
| 2 | 132x1024x8 | 12.4750 | [12.4705, 12.4807] | -0.0000 [-0.0031, 0.0070] |
| 3 | 2112x1024x8 | 12.4756 | [12.4736, 12.4770] | 0.0019 [-0.0022, 0.0071] |
| 4 | 1056x128x8 | 12.4758 | [12.4694, 12.4844] | 0.0012 [-0.0044, 0.0089] |
| 5 | 2112x256x8 | 12.4760 | [12.4714, 12.4792] | 0.0032 [-0.0066, 0.0088] |

## route/footprint-mib=8,kernel=k6,keys=1024,placement=hbm,strategy=warp,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 528x512x8 | 0.7560 | [0.7557, 0.7564] | 0.0000 [0.0000, 0.0000] |
| 2 | 1056x512x8 | 0.7561 | [0.7561, 0.7563] | 0.0001 [-0.0002, 0.0004] |
| 3 | 264x1024x8 | 0.7562 | [0.7560, 0.7563] | 0.0001 [-0.0002, 0.0006] |
| 4 | 264x1024x8 | 0.7562 | [0.7561, 0.7565] | 0.0002 [-0.0002, 0.0007] |
| 5 | 2112x256x8 | 0.7562 | [0.7561, 0.7564] | 0.0002 [-0.0001, 0.0006] |

## route/footprint-mib=8,kernel=k6,keys=1024,placement=hbm,tune=copy,type=tune

- 60 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-64m-none-whole-kernel | 0.7824 | [0.7819, 0.7827] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-256m-none-whole-kernel | 0.7824 | [0.7821, 0.7829] | 0.0001 [-0.0004, 0.0007] |
| 3 | kernel-pageable-1-64m-none-whole-kernel | 0.7825 | [0.7822, 0.7830] | 0.0000 [-0.0001, 0.0004] |
| 4 | kernel-registered-1-256m-none-whole-kernel | 0.7825 | [0.7822, 0.7830] | 0.0002 [-0.0004, 0.0006] |
| 5 | kernel-registered-1-16m-none-whole-kernel | 0.7826 | [0.7820, 0.7829] | 0.0001 [-0.0005, 0.0007] |
| 56 | ce-pageable-1-whole-none-whole | 0.8357 | [0.8354, 0.8361] | 0.0533 [0.0527, 0.0540] |

## route/footprint-mib=8,kernel=k6,keys=1024,placement=hbm,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 8448x256x8 | 0.7659 | [0.7658, 0.7661] | 0.0000 [0.0000, 0.0000] |
| 2 | 528x1024x8 | 0.7660 | [0.7657, 0.7661] | 0.0000 [-0.0002, 0.0002] |
| 3 | 264x512x8 | 0.7660 | [0.7659, 0.7664] | 0.0002 [-0.0000, 0.0003] |
| 4 | 1056x128x8 | 0.7661 | [0.7660, 0.7661] | 0.0002 [0.0000, 0.0002] |
| 5 | 528x256x8 | 0.7661 | [0.7660, 0.7664] | 0.0002 [0.0000, 0.0006] |

## route/footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,strategy=warp,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 528x512x8 | 7.8192 | [7.8156, 7.8225] | 0.0000 [0.0000, 0.0000] |
| 2 | 1056x512x8 | 7.8947 | [7.8900, 7.8983] | 0.0749 [0.0700, 0.0798] |
| 3 | 528x1024x8 | 7.9065 | [7.9040, 7.9110] | 0.0892 [0.0825, 0.0919] |
| 4 | 1056x1024x8 | 7.9116 | [7.9094, 7.9128] | 0.0927 [0.0885, 0.0973] |
| 5 | 8448x128x8 | 7.9194 | [7.9149, 7.9217] | 0.0993 [0.0959, 0.1052] |

## route/footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,tune=copy,type=tune

- 60 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-16m-none-whole-kernel | 0.2319 | [0.2317, 0.2324] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-256m-none-whole-kernel | 0.2319 | [0.2318, 0.2324] | -0.0000 [-0.0004, 0.0005] |
| 3 | kernel-registered-1-64m-none-whole-kernel | 0.2322 | [0.2317, 0.2323] | 0.0002 [-0.0002, 0.0004] |
| 4 | kernel-registered-1-whole-none-whole-kernel | 0.2323 | [0.2318, 0.2324] | 0.0002 [-0.0001, 0.0006] |
| 5 | kernel-pageable-1-64m-none-whole-kernel | 0.2332 | [0.2330, 0.2335] | 0.0013 [0.0011, 0.0015] |
| 59 | ce-pageable-1-whole-none-whole | 0.2515 | [0.2510, 0.2517] | 0.0197 [0.0190, 0.0200] |

## route/footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 264x256x8 | 7.6824 | [7.6798, 7.6872] | 0.0000 [0.0000, 0.0000] |
| 2 | 8448x128x8 | 7.7424 | [7.7390, 7.7448] | 0.0600 [0.0561, 0.0630] |
| 3 | 1056x128x8 | 7.7622 | [7.7592, 7.7635] | 0.0788 [0.0730, 0.0843] |
| 4 | 264x1024x8 | 7.9132 | [7.9111, 7.9147] | 0.2308 [0.2268, 0.2329] |
| 5 | 132x256x8 | 7.9162 | [7.9137, 7.9227] | 0.2340 [0.2280, 0.2419] |

## route/footprint-mib=8,kernel=k6,keys=1048576,placement=hbm,strategy=warp,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 528x128x8 | 0.2818 | [0.2817, 0.2818] | 0.0000 [0.0000, 0.0000] |
| 2 | 264x256x8 | 0.2818 | [0.2817, 0.2818] | 0.0000 [-0.0001, 0.0001] |
| 3 | 264x256x8 | 0.2818 | [0.2818, 0.2818] | 0.0001 [-0.0000, 0.0001] |
| 4 | 528x128x8 | 0.2820 | [0.2819, 0.2820] | 0.0002 [0.0002, 0.0002] |
| 5 | 132x512x8 | 0.2822 | [0.2821, 0.2822] | 0.0004 [0.0004, 0.0005] |

## route/footprint-mib=8,kernel=k6,keys=1048576,placement=hbm,tune=copy,type=tune

- 60 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole-kernel | 0.1905 | [0.1904, 0.1911] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-64m-none-whole-kernel | 0.1906 | [0.1905, 0.1911] | 0.0000 [-0.0001, 0.0002] |
| 3 | kernel-pageable-1-256m-none-whole-kernel | 0.1908 | [0.1907, 0.1913] | 0.0002 [-0.0003, 0.0007] |
| 4 | kernel-registered-1-16m-none-whole-kernel | 0.1908 | [0.1905, 0.1913] | 0.0001 [-0.0001, 0.0007] |
| 5 | kernel-pageable-1-whole-none-whole-kernel | 0.1909 | [0.1907, 0.1914] | 0.0003 [-0.0003, 0.0009] |
| 59 | ce-pageable-1-whole-none-whole | 0.2442 | [0.2440, 0.2444] | 0.0536 [0.0531, 0.0539] |

## route/footprint-mib=8,kernel=k6,keys=1048576,placement=hbm,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 2112x256x8 | 0.1770 | [0.1769, 0.1772] | 0.0000 [0.0000, 0.0000] |
| 2 | 2112x512x8 | 0.1785 | [0.1784, 0.1786] | 0.0015 [0.0013, 0.0017] |
| 3 | 2112x128x8 | 0.1786 | [0.1784, 0.1794] | 0.0016 [0.0013, 0.0024] |
| 4 | 1056x256x8 | 0.1786 | [0.1784, 0.1801] | 0.0016 [0.0014, 0.0031] |
| 5 | 528x1024x8 | 0.1798 | [0.1796, 0.1799] | 0.0028 [0.0025, 0.0029] |

## route/footprint-mib=8192,generator=rmat,kernel=k4,placement=cpu,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-whole-none-whole-kernel | 411.3104 | [410.5026, 411.6786] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-2-256m-none-whole | 411.6687 | [411.4068, 416.5059] | 0.4887 [-0.0380, 4.8274] |
| 3 | ce-registered-2-256m-none-whole-kernel | 411.9358 | [411.3765, 416.3697] | 0.5024 [-0.7593, 5.2308] |
| 4 | ce-registered-4-whole-none-whole | 411.9515 | [411.4172, 416.8680] | 1.3403 [-0.1527, 5.2694] |
| 5 | ce-registered-4-64m-none-whole-kernel | 412.1250 | [411.5636, 416.7685] | 1.0028 [-0.1231, 5.4783] |
| 7 | ce-pageable-1-whole-none-whole | 412.6912 | [412.5977, 417.5677] | 1.4070 [1.1657, 4.9783] |

## route/footprint-mib=8192,generator=rmat,kernel=k4,placement=hbm,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-256m-none-whole-kernel | 395.1279 | [394.6981, 399.9504] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole | 395.3029 | [394.5178, 399.5674] | 0.0529 [-4.5696, 4.8693] |
| 3 | kernel-registered-1-256m-none-whole-kernel | 395.4609 | [394.8865, 399.9650] | 0.1344 [-4.4463, 5.2073] |
| 4 | kernel-registered-1-256m-none-whole | 395.8211 | [394.6771, 400.5228] | -0.0466 [-3.1308, 5.8247] |
| 5 | kernel-pageable-1-64m-none-whole | 396.1846 | [395.8518, 401.0465] | 1.0255 [-3.5582, 6.2993] |
| 34 | ce-pageable-1-whole-none-whole | 412.7959 | [410.5786, 415.7139] | 15.7249 [10.6378, 20.5890] |

## route/footprint-mib=8192,generator=uniform,kernel=k4,placement=cpu,tune=copy,type=tune

- 108 configurations, 100 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-4-256m-pipe-whole-kernel | 24.2095 | [24.2018, 24.2200] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-256m-pipe-whole-kernel | 24.2178 | [24.2088, 24.2271] | 0.0011 [-0.0112, 0.0113] |
| 3 | ce-registered-2-256m-pipe-whole-kernel | 24.2205 | [24.2083, 24.2266] | 0.0097 [-0.0054, 0.0198] |
| 4 | ce-registered-1-256m-pipe-whole | 24.4091 | [24.3956, 24.4143] | 0.1926 [0.1859, 0.2130] |
| 5 | ce-registered-2-256m-pipe-whole | 24.4110 | [24.4028, 24.4222] | 0.1991 [0.1910, 0.2172] |
| 60 | ce-pageable-1-whole-none-whole | 38.7976 | [38.7950, 38.8013] | 14.5892 [14.5751, 14.5996] |

## route/footprint-mib=8192,generator=uniform,kernel=k4,placement=hbm,tune=copy,type=tune

- 108 configurations, 100 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-whole-kernel | 20.2177 | [20.2116, 20.2280] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole-kernel | 20.2247 | [20.2193, 20.2320] | 0.0034 [-0.0060, 0.0101] |
| 3 | kernel-pageable-1-256m-none-whole-kernel | 20.4578 | [20.4529, 20.4619] | 0.2354 [0.2284, 0.2404] |
| 4 | kernel-registered-1-256m-none-whole-kernel | 20.4674 | [20.4639, 20.4714] | 0.2508 [0.2401, 0.2582] |
| 5 | kernel-pageable-1-64m-none-whole-kernel | 20.8189 | [20.8157, 20.8221] | 0.5956 [0.5895, 0.6031] |
| 72 | ce-pageable-1-whole-none-whole | 36.3241 | [36.3166, 36.3292] | 16.0978 [16.0855, 16.1068] |

