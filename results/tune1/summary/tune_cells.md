# Tuning cells: one route in every configuration of its space, recomputed from raw rows

Times are per repetition in ms. Each round runs every configuration once in the order the seed drew. Per cell the five fastest configurations and, for a copy space, the simplest one (copy engine, pageable memory, one stream, whole transfer); the slowdown against the fastest is paired within rounds, as median with 95 % rank interval. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

## route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-64m-pipe-whole | 2.9866 | [2.9840, 2.9896] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-64m-pipe-whole | 2.9867 | [2.9845, 2.9884] | 0.0006 [-0.0033, 0.0031] |
| 3 | ce-registered-4-64m-pipe-whole | 2.9867 | [2.9846, 2.9881] | 0.0009 [-0.0052, 0.0023] |
| 4 | ce-registered-1-256m-pipe-whole | 3.0053 | [3.0042, 3.0071] | 0.0188 [0.0156, 0.0219] |
| 5 | ce-registered-2-256m-pipe-whole | 3.0065 | [3.0049, 3.0092] | 0.0216 [0.0156, 0.0230] |
| 51 | ce-pageable-1-whole-none-whole | 3.3322 | [3.3297, 3.3351] | 0.3455 [0.3428, 0.3504] |

## route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,tune=copy-kernel,type=tune

- 104 configurations, 30 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 2112x256x16 | 3.3070 | [3.3065, 3.3074] | 0.0000 [0.0000, 0.0000] |
| 2 | 16896x128x16 | 3.3070 | [3.3066, 3.3075] | 0.0000 [-0.0008, 0.0004] |
| 3 | 8448x128x16 | 3.3073 | [3.3068, 3.3080] | 0.0004 [-0.0008, 0.0014] |
| 4 | 2112x256x16 | 3.3075 | [3.3065, 3.3082] | 0.0005 [-0.0001, 0.0012] |
| 5 | 2112x256x16 | 3.3076 | [3.3068, 3.3083] | 0.0010 [-0.0006, 0.0014] |

## route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,tune=direct,type=tune

- 104 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 4224x512x8 | 2.9178 | [2.9171, 2.9190] | 0.0000 [0.0000, 0.0000] |
| 2 | 2112x1024x8 | 2.9191 | [2.9185, 2.9196] | 0.0014 [-0.0005, 0.0023] |
| 3 | 8448x256x8 | 2.9248 | [2.9235, 2.9261] | 0.0071 [0.0055, 0.0084] |
| 4 | 1056x512x8 | 2.9257 | [2.9245, 2.9265] | 0.0080 [0.0059, 0.0086] |
| 5 | 1056x512x8 | 2.9257 | [2.9255, 2.9265] | 0.0081 [0.0068, 0.0087] |

## route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,tune=copy,type=tune

- 108 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-64m-pipe-whole | 0.9434 | [0.9430, 0.9445] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-64m-pipe-whole | 0.9443 | [0.9435, 0.9449] | 0.0002 [-0.0002, 0.0016] |
| 3 | kernel-registered-1-whole-none-whole | 0.9460 | [0.9456, 0.9468] | 0.0018 [0.0012, 0.0032] |
| 4 | kernel-pageable-1-whole-none-whole | 0.9465 | [0.9464, 0.9476] | 0.0032 [0.0019, 0.0038] |
| 5 | kernel-registered-1-whole-none-touched | 0.9489 | [0.9484, 0.9495] | 0.0055 [0.0039, 0.0062] |
| 51 | ce-pageable-1-whole-none-whole | 2.8508 | [2.8499, 2.8510] | 1.9072 [1.9053, 1.9077] |

## route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,tune=direct,type=tune

- 104 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 8448x128x16 | 0.2983 | [0.2982, 0.2984] | 0.0000 [0.0000, 0.0000] |
| 2 | 8448x128x16 | 0.2983 | [0.2982, 0.2984] | 0.0000 [-0.0001, 0.0001] |
| 3 | 16896x128x16 | 0.2984 | [0.2984, 0.2985] | 0.0001 [-0.0000, 0.0002] |
| 4 | 4224x128x16 | 0.2986 | [0.2986, 0.2989] | 0.0003 [0.0002, 0.0006] |
| 5 | 4224x128x16 | 0.2987 | [0.2985, 0.2989] | 0.0004 [0.0002, 0.0006] |

## route/f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=cpu,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-256m-pipe-whole | 42.4712 | [42.4565, 42.4749] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-4-256m-pipe-whole | 42.4732 | [42.4496, 42.4802] | 0.0055 [-0.0250, 0.0149] |
| 3 | ce-registered-1-256m-pipe-whole | 42.4799 | [42.4691, 42.4857] | 0.0064 [-0.0058, 0.0293] |
| 4 | ce-registered-1-64m-pipe-whole | 43.0892 | [43.0851, 43.0940] | 0.6182 [0.6126, 0.6375] |
| 5 | ce-registered-2-64m-pipe-whole | 43.0898 | [43.0864, 43.0996] | 0.6218 [0.6127, 0.6315] |
| 27 | ce-pageable-1-whole-none-whole | 47.7826 | [47.7743, 47.7873] | 5.3118 [5.3056, 5.3342] |

## route/f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=hbm,tune=copy,type=tune

- 108 configurations, 40 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-256m-pipe-touched | 14.6576 | [14.6530, 14.6603] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-256m-pipe-touched | 14.6642 | [14.6612, 14.6675] | 0.0095 [-0.0015, 0.0160] |
| 3 | kernel-registered-1-256m-pipe-whole | 14.6646 | [14.6601, 14.6696] | 0.0074 [0.0028, 0.0163] |
| 4 | kernel-pageable-1-256m-pipe-whole | 14.6700 | [14.6644, 14.6745] | 0.0127 [0.0032, 0.0177] |
| 5 | kernel-registered-1-whole-none-whole | 14.7945 | [14.7883, 14.8053] | 0.1360 [0.1290, 0.1476] |
| 51 | ce-pageable-1-whole-none-whole | 45.6629 | [45.6508, 45.6680] | 31.0033 [30.9763, 31.0138] |

## route/f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=hbm,tune=direct,type=tune

- 104 configurations, 30 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 1056x1024x16 | 4.9541 | [4.9463, 4.9692] | 0.0000 [0.0000, 0.0000] |
| 2 | 1056x1024x16 | 4.9695 | [4.9543, 4.9739] | 0.0041 [-0.0054, 0.0248] |
| 3 | 2112x512x16 | 5.1645 | [5.1596, 5.1760] | 0.2060 [0.1836, 0.2274] |
| 4 | 2112x512x16 | 5.1664 | [5.1566, 5.1798] | 0.2124 [0.1951, 0.2251] |
| 5 | 4224x256x16 | 5.4718 | [5.4607, 5.4819] | 0.5157 [0.4988, 0.5309] |

## route/f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=cpu,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-4-256m-pipe-whole | 63.6539 | [63.6200, 63.6859] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-256m-pipe-whole | 63.6540 | [63.6459, 63.6630] | -0.0014 [-0.0359, 0.0403] |
| 3 | ce-registered-2-256m-pipe-whole | 63.6661 | [63.6395, 63.6778] | 0.0145 [-0.0458, 0.0414] |
| 4 | ce-registered-2-64m-pipe-whole | 64.6029 | [64.5995, 64.6122] | 0.9485 [0.9202, 0.9930] |
| 5 | ce-registered-4-64m-pipe-whole | 64.6062 | [64.5965, 64.6094] | 0.9475 [0.9086, 0.9854] |
| 26 | ce-pageable-1-whole-none-whole | 71.1552 | [71.1393, 71.1700] | 7.5066 [7.4501, 7.5560] |

## route/f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-64m-pipe-whole | 0.8063 | [0.8050, 0.8071] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-4-64m-pipe-whole | 0.8066 | [0.8057, 0.8073] | 0.0000 [-0.0007, 0.0015] |
| 3 | ce-registered-1-64m-pipe-whole | 0.8066 | [0.8057, 0.8071] | 0.0002 [-0.0009, 0.0011] |
| 4 | ce-pageable-1-64m-pipe-whole | 0.8249 | [0.8241, 0.8255] | 0.0185 [0.0180, 0.0196] |
| 5 | ce-registered-2-16m-pipe-whole | 0.8277 | [0.8271, 0.8294] | 0.0212 [0.0205, 0.0231] |
| 21 | ce-pageable-1-whole-none-whole | 0.8465 | [0.8459, 0.8475] | 0.0404 [0.0392, 0.0413] |

## route/f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu,tune=direct,type=tune

- 104 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 4224x512x8 | 0.7340 | [0.7339, 0.7341] | 0.0000 [0.0000, 0.0000] |
| 2 | 4224x256x8 | 0.7340 | [0.7338, 0.7341] | 0.0000 [-0.0002, 0.0001] |
| 3 | 4224x256x8 | 0.7340 | [0.7340, 0.7341] | -0.0000 [-0.0001, 0.0001] |
| 4 | 2112x512x8 | 0.7349 | [0.7348, 0.7351] | 0.0009 [0.0007, 0.0012] |
| 5 | 2112x512x8 | 0.7350 | [0.7349, 0.7351] | 0.0009 [0.0007, 0.0012] |

## route/f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm,tune=copy,type=tune

- 108 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole | 0.2545 | [0.2543, 0.2547] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-whole | 0.2547 | [0.2544, 0.2549] | 0.0002 [-0.0000, 0.0004] |
| 3 | kernel-registered-1-256m-none-whole | 0.2547 | [0.2546, 0.2550] | 0.0004 [-0.0002, 0.0007] |
| 4 | kernel-pageable-1-256m-none-whole | 0.2548 | [0.2546, 0.2552] | 0.0003 [-0.0001, 0.0007] |
| 5 | kernel-pageable-1-256m-pipe-whole | 0.2558 | [0.2556, 0.2561] | 0.0013 [0.0010, 0.0018] |
| 54 | ce-pageable-1-whole-none-whole | 0.7364 | [0.7358, 0.7370] | 0.4821 [0.4814, 0.4824] |

## route/f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm,tune=direct,type=tune

- 104 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 4224x128x16 | 0.0782 | [0.0781, 0.0782] | 0.0000 [0.0000, 0.0000] |
| 2 | 4224x128x16 | 0.0782 | [0.0781, 0.0782] | -0.0000 [-0.0000, 0.0000] |
| 3 | 4224x128x16 | 0.0782 | [0.0782, 0.0782] | 0.0000 [-0.0000, 0.0000] |
| 4 | 8448x128x16 | 0.0783 | [0.0783, 0.0783] | 0.0001 [0.0001, 0.0002] |
| 5 | 8448x128x16 | 0.0783 | [0.0783, 0.0784] | 0.0002 [0.0001, 0.0002] |

## route/f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=cpu,tune=copy,type=tune

- 108 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-256m-pipe-whole | 84.8297 | [84.8222, 84.8488] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-256m-pipe-whole | 84.8322 | [84.8204, 84.8530] | -0.0039 [-0.0185, 0.0510] |
| 3 | ce-registered-4-256m-pipe-whole | 84.8359 | [84.8301, 84.8392] | 0.0033 [-0.0096, 0.0257] |
| 4 | ce-registered-1-64m-pipe-whole | 86.1152 | [86.1094, 86.1198] | 1.2834 [1.2658, 1.2988] |
| 5 | ce-registered-4-64m-pipe-whole | 86.1184 | [86.1143, 86.1209] | 1.2839 [1.2700, 1.3123] |
| 26 | ce-pageable-1-whole-none-whole | 94.5833 | [94.5755, 94.5919] | 9.7587 [9.7373, 9.7731] |

## route/f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=cpu,tune=direct,type=tune

- 104 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 1056x128x8 | 88.0686 | [88.0522, 88.1067] | 0.0000 [0.0000, 0.0000] |
| 2 | 1056x128x8 | 88.0737 | [88.0379, 88.1152] | -0.0052 [-0.0578, 0.0390] |
| 3 | 264x512x8 | 88.0752 | [88.0428, 88.1002] | -0.0020 [-0.0308, 0.0351] |
| 4 | 264x512x8 | 88.0779 | [88.0350, 88.1111] | 0.0038 [-0.0865, 0.0424] |
| 5 | 528x256x8 | 88.0805 | [88.0638, 88.1028] | 0.0088 [-0.0310, 0.0678] |

## route/f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu,tune=copy,type=tune

- 108 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-256m-pipe-whole | 10.7239 | [10.7226, 10.7248] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-256m-pipe-whole | 10.7247 | [10.7227, 10.7261] | 0.0011 [-0.0015, 0.0027] |
| 3 | ce-registered-4-256m-pipe-whole | 10.7252 | [10.7240, 10.7266] | 0.0023 [-0.0002, 0.0036] |
| 4 | ce-registered-1-64m-pipe-whole | 10.8392 | [10.8367, 10.8412] | 0.1141 [0.1116, 0.1189] |
| 5 | ce-registered-2-64m-pipe-whole | 10.8397 | [10.8382, 10.8412] | 0.1164 [0.1150, 0.1171] |
| 47 | ce-pageable-1-whole-none-whole | 12.6315 | [12.6282, 12.6325] | 1.9069 [1.9046, 1.9099] |

## route/f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=hbm,tune=copy,type=tune

- 108 configurations, 50 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-64m-pipe-whole | 3.6657 | [3.6646, 3.6665] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-64m-pipe-whole | 3.6664 | [3.6654, 3.6672] | 0.0006 [-0.0006, 0.0019] |
| 3 | kernel-pageable-1-256m-pipe-whole | 3.6907 | [3.6898, 3.6923] | 0.0253 [0.0235, 0.0269] |
| 4 | kernel-pageable-1-256m-pipe-touched | 3.6910 | [3.6891, 3.6931] | 0.0251 [0.0230, 0.0278] |
| 5 | kernel-registered-1-256m-pipe-touched | 3.6914 | [3.6897, 3.6936] | 0.0255 [0.0246, 0.0278] |
| 51 | ce-pageable-1-whole-none-whole | 11.3230 | [11.3144, 11.3284] | 7.6573 [7.6494, 7.6643] |

## route/f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=cpu,tune=copy,type=tune

- 108 configurations, 100 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-4-256m-pipe-whole | 21.2898 | [21.2886, 21.2912] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-256m-pipe-whole | 21.2899 | [21.2889, 21.2915] | 0.0005 [-0.0021, 0.0028] |
| 3 | ce-registered-2-256m-pipe-whole | 21.2907 | [21.2893, 21.2924] | 0.0004 [-0.0015, 0.0024] |
| 4 | ce-registered-4-64m-pipe-whole | 21.5741 | [21.5722, 21.5759] | 0.2854 [0.2827, 0.2879] |
| 5 | ce-registered-1-64m-pipe-whole | 21.5744 | [21.5728, 21.5756] | 0.2865 [0.2836, 0.2876] |
| 41 | ce-pageable-1-whole-none-whole | 24.3985 | [24.3956, 24.4004] | 3.1103 [3.1068, 3.1125] |

## route/f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=hbm,tune=copy,type=tune

- 108 configurations, 100 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-64m-pipe-whole | 7.3248 | [7.3168, 7.3819] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-64m-pipe-whole | 7.3259 | [7.3174, 7.3352] | -0.0019 [-0.0064, 0.0015] |
| 3 | kernel-pageable-1-256m-pipe-touched | 7.3358 | [7.3334, 7.3386] | 0.0103 [-0.0337, 0.0176] |
| 4 | kernel-registered-1-256m-pipe-touched | 7.3374 | [7.3348, 7.3392] | 0.0120 [-0.0404, 0.0180] |
| 5 | kernel-registered-1-256m-pipe-whole | 7.3396 | [7.3384, 7.3425] | 0.0146 [-0.0383, 0.0222] |
| 54 | ce-pageable-1-whole-none-whole | 22.7918 | [22.7878, 22.7953] | 15.4518 [15.4149, 15.4651] |

## route/f-den=10,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-256m-pipe-touched | 0.3548 | [0.3537, 0.3566] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-256m-pipe-touched | 0.3555 | [0.3538, 0.3568] | 0.0006 [-0.0017, 0.0018] |
| 3 | kernel-pageable-1-whole-none-touched | 0.3597 | [0.3596, 0.3601] | 0.0048 [0.0030, 0.0062] |
| 4 | kernel-registered-1-whole-none-touched | 0.3602 | [0.3601, 0.3606] | 0.0057 [0.0039, 0.0065] |
| 5 | kernel-registered-1-256m-none-touched | 0.3766 | [0.3761, 0.3768] | 0.0216 [0.0198, 0.0226] |
| 71 | ce-pageable-1-whole-none-whole | 3.0189 | [3.0165, 3.0211] | 2.6639 [2.6624, 2.6654] |

## route/f-den=10,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,tune=copy,type=tune

- 108 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-touched | 0.1231 | [0.1230, 0.1232] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-touched | 0.1234 | [0.1233, 0.1235] | 0.0003 [0.0000, 0.0004] |
| 3 | kernel-registered-1-256m-pipe-touched | 0.1294 | [0.1293, 0.1295] | 0.0063 [0.0061, 0.0064] |
| 4 | kernel-pageable-1-256m-pipe-touched | 0.1295 | [0.1293, 0.1295] | 0.0063 [0.0062, 0.0063] |
| 5 | kernel-registered-1-256m-none-touched | 0.1380 | [0.1379, 0.1381] | 0.0148 [0.0148, 0.0150] |
| 78 | ce-pageable-1-whole-none-whole | 2.5923 | [2.5919, 2.5934] | 2.4692 [2.4689, 2.4702] |

## route/f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=cpu,tune=copy,type=tune

- 108 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-1-64m-pipe-touched | 2.6817 | [2.6808, 2.6824] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-2-64m-pipe-touched | 2.6820 | [2.6809, 2.6826] | -0.0001 [-0.0009, 0.0012] |
| 3 | ce-registered-4-64m-pipe-touched | 2.6821 | [2.6810, 2.6830] | 0.0004 [-0.0007, 0.0008] |
| 4 | ce-registered-1-256m-pipe-touched | 2.6947 | [2.6941, 2.6958] | 0.0136 [0.0119, 0.0143] |
| 5 | ce-registered-2-256m-pipe-touched | 2.6957 | [2.6943, 2.6963] | 0.0140 [0.0129, 0.0147] |
| 67 | ce-pageable-1-whole-none-whole | 3.2727 | [3.2712, 3.2734] | 0.5906 [0.5896, 0.5919] |

## route/f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=hbm,tune=copy,type=tune

- 108 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-64m-pipe-touched | 0.8740 | [0.8735, 0.8745] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-64m-pipe-touched | 0.8744 | [0.8740, 0.8749] | 0.0002 [-0.0004, 0.0020] |
| 3 | kernel-pageable-1-256m-pipe-touched | 0.8861 | [0.8850, 0.8871] | 0.0120 [0.0105, 0.0132] |
| 4 | kernel-pageable-1-whole-none-touched | 0.8864 | [0.8859, 0.8870] | 0.0121 [0.0118, 0.0133] |
| 5 | kernel-registered-1-whole-none-touched | 0.8866 | [0.8860, 0.8870] | 0.0124 [0.0119, 0.0134] |
| 75 | ce-pageable-1-whole-none-whole | 2.8281 | [2.8268, 2.8292] | 1.9536 [1.9529, 1.9554] |

## route/f-den=100,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,tune=copy,type=tune

- 108 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-touched | 0.0516 | [0.0515, 0.0517] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-touched | 0.0518 | [0.0517, 0.0518] | 0.0002 [0.0001, 0.0003] |
| 3 | kernel-registered-1-256m-none-touched | 0.0696 | [0.0695, 0.0696] | 0.0180 [0.0179, 0.0181] |
| 4 | kernel-pageable-1-256m-none-touched | 0.0697 | [0.0696, 0.0697] | 0.0181 [0.0181, 0.0182] |
| 5 | kernel-pageable-1-256m-pipe-touched | 0.0698 | [0.0697, 0.0701] | 0.0183 [0.0180, 0.0186] |
| 76 | ce-pageable-1-whole-none-whole | 3.0237 | [3.0225, 3.0251] | 2.9715 [2.9711, 2.9731] |

## route/f-den=100,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,tune=copy,type=tune

- 108 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-touched | 0.0312 | [0.0312, 0.0313] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-touched | 0.0314 | [0.0314, 0.0315] | 0.0002 [0.0002, 0.0003] |
| 3 | kernel-registered-1-256m-none-touched | 0.0439 | [0.0439, 0.0440] | 0.0127 [0.0126, 0.0128] |
| 4 | kernel-pageable-1-256m-none-touched | 0.0440 | [0.0439, 0.0440] | 0.0127 [0.0127, 0.0128] |
| 5 | kernel-pageable-1-256m-pipe-touched | 0.0472 | [0.0470, 0.0474] | 0.0160 [0.0159, 0.0162] |
| 75 | ce-pageable-1-whole-none-whole | 2.5649 | [2.5637, 2.5659] | 2.5337 [2.5325, 2.5347] |

## route/f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,tune=copy,type=tune

- 216 configurations, 40 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-touched-kernel | 0.0183 | [0.0182, 0.0183] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-touched-kernel | 0.0183 | [0.0183, 0.0183] | 0.0000 [0.0000, 0.0000] |
| 3 | kernel-registered-1-whole-none-touched | 0.0241 | [0.0240, 0.0241] | 0.0058 [0.0057, 0.0058] |
| 4 | kernel-pageable-1-whole-none-touched | 0.0241 | [0.0241, 0.0241] | 0.0058 [0.0057, 0.0058] |
| 5 | kernel-pageable-1-256m-none-touched-kernel | 0.0311 | [0.0311, 0.0312] | 0.0129 [0.0128, 0.0129] |
| 152 | ce-pageable-1-whole-none-whole | 3.0216 | [3.0210, 3.0220] | 3.0033 [3.0027, 3.0037] |

## route/f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,tune=direct,type=tune

- 104 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 528x128x16 | 0.0073 | [0.0073, 0.0074] | 0.0000 [0.0000, 0.0000] |
| 2 | 528x128x16 | 0.0073 | [0.0073, 0.0074] | 0.0000 [-0.0000, 0.0000] |
| 3 | 1056x128x8 | 0.0074 | [0.0074, 0.0074] | 0.0000 [0.0000, 0.0000] |
| 4 | 1056x128x8 | 0.0074 | [0.0074, 0.0074] | 0.0000 [0.0000, 0.0000] |
| 5 | 1056x128x8 | 0.0074 | [0.0074, 0.0074] | 0.0000 [0.0000, 0.0000] |

## route/f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,tune=copy,type=tune

- 216 configurations, 40 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-touched-kernel | 0.0144 | [0.0143, 0.0144] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-touched-kernel | 0.0144 | [0.0143, 0.0144] | 0.0000 [0.0000, 0.0000] |
| 3 | kernel-pageable-1-whole-none-touched | 0.0210 | [0.0209, 0.0210] | 0.0066 [0.0066, 0.0067] |
| 4 | kernel-registered-1-whole-none-touched | 0.0210 | [0.0209, 0.0210] | 0.0066 [0.0065, 0.0067] |
| 5 | kernel-registered-1-256m-none-touched-kernel | 0.0245 | [0.0244, 0.0245] | 0.0101 [0.0101, 0.0101] |
| 156 | ce-pageable-1-whole-none-whole | 2.5629 | [2.5625, 2.5635] | 2.5485 [2.5481, 2.5491] |

## route/f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,tune=direct,type=tune

- 104 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 528x128x16 | 0.0038 | [0.0038, 0.0038] | 0.0000 [0.0000, 0.0000] |
| 2 | 528x128x16 | 0.0038 | [0.0038, 0.0038] | 0.0000 [-0.0000, 0.0000] |
| 3 | 1056x128x16 | 0.0038 | [0.0038, 0.0038] | 0.0000 [-0.0000, 0.0000] |
| 4 | 1056x128x16 | 0.0038 | [0.0038, 0.0038] | 0.0000 [-0.0000, 0.0000] |
| 5 | 1056x128x16 | 0.0038 | [0.0038, 0.0038] | 0.0000 [0.0000, 0.0000] |

## route/f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,tune=copy,type=tune

- 108 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-64m-pipe-touched | 1.6114 | [1.6107, 1.6136] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-256m-pipe-touched | 1.6146 | [1.6107, 1.6281] | 0.0036 [-0.0006, 0.0169] |
| 3 | kernel-pageable-1-64m-pipe-touched | 1.6171 | [1.6151, 1.6187] | 0.0048 [0.0036, 0.0067] |
| 4 | kernel-pageable-1-256m-pipe-touched | 1.6192 | [1.6097, 1.6249] | 0.0060 [-0.0015, 0.0112] |
| 5 | ce-registered-1-256m-pipe-touched | 1.6483 | [1.6475, 1.6488] | 0.0364 [0.0353, 0.0377] |
| 80 | ce-pageable-1-whole-none-whole | 3.1961 | [3.1956, 3.1981] | 1.5851 [1.5829, 1.5856] |

## route/f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,tune=copy,type=tune

- 108 configurations, 100 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-64m-pipe-touched | 0.5109 | [0.5108, 0.5111] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-64m-pipe-touched | 0.5111 | [0.5111, 0.5113] | 0.0002 [0.0001, 0.0004] |
| 3 | kernel-registered-1-whole-none-touched | 0.5122 | [0.5120, 0.5124] | 0.0013 [0.0011, 0.0015] |
| 4 | kernel-pageable-1-whole-none-touched | 0.5124 | [0.5122, 0.5125] | 0.0013 [0.0011, 0.0015] |
| 5 | kernel-pageable-1-256m-pipe-touched | 0.5184 | [0.5182, 0.5186] | 0.0074 [0.0070, 0.0077] |
| 81 | ce-pageable-1-whole-none-whole | 2.7104 | [2.7099, 2.7111] | 2.1994 [2.1990, 2.1998] |

## route/f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=cpu,tune=copy,type=tune

- 108 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-4-64m-pipe-touched | 2.3195 | [2.3185, 2.3211] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-64m-pipe-touched | 2.3196 | [2.3185, 2.3200] | -0.0005 [-0.0016, 0.0012] |
| 3 | ce-registered-2-64m-pipe-touched | 2.3198 | [2.3186, 2.3207] | -0.0003 [-0.0009, 0.0013] |
| 4 | ce-registered-4-256m-pipe-touched | 2.3238 | [2.3231, 2.3262] | 0.0046 [0.0024, 0.0062] |
| 5 | ce-registered-2-256m-pipe-touched | 2.3245 | [2.3228, 2.3261] | 0.0045 [0.0037, 0.0070] |
| 75 | ce-pageable-1-whole-none-whole | 3.2635 | [3.2626, 3.2650] | 0.9435 [0.9423, 0.9464] |

## route/f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=hbm,tune=copy,type=tune

- 108 configurations, 20 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-64m-pipe-touched | 0.7437 | [0.7433, 0.7447] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-64m-pipe-touched | 0.7446 | [0.7444, 0.7450] | 0.0010 [-0.0001, 0.0017] |
| 3 | kernel-pageable-1-whole-none-touched | 0.7524 | [0.7520, 0.7528] | 0.0086 [0.0079, 0.0094] |
| 4 | kernel-registered-1-whole-none-touched | 0.7527 | [0.7523, 0.7531] | 0.0089 [0.0085, 0.0094] |
| 5 | kernel-registered-1-256m-pipe-touched | 0.7535 | [0.7526, 0.7540] | 0.0095 [0.0086, 0.0108] |
| 81 | ce-pageable-1-whole-none-whole | 2.7855 | [2.7851, 2.7868] | 2.0420 [2.0412, 2.0432] |

## route/footprint-mib=1024,kernel=k3,placement=cpu,tune=copy,type=tune

- 30 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-2-whole-none-whole | 3.3930 | [3.3919, 3.3957] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-whole-none-whole | 3.3933 | [3.3909, 3.3966] | 0.0013 [-0.0022, 0.0035] |
| 3 | ce-registered-4-whole-none-whole | 3.3934 | [3.3923, 3.3949] | -0.0002 [-0.0021, 0.0018] |
| 4 | ce-registered-2-256m-none-whole | 3.4038 | [3.4016, 3.4054] | 0.0101 [0.0071, 0.0140] |
| 5 | ce-registered-4-256m-none-whole | 3.4041 | [3.4019, 3.4073] | 0.0108 [0.0082, 0.0149] |
| 14 | ce-pageable-1-whole-none-whole | 3.5112 | [3.5110, 3.5122] | 0.1183 [0.1142, 0.1204] |

## route/footprint-mib=1024,kernel=k3,placement=cpu,tune=copy-kernel,type=tune

- 52 configurations, 30 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 16896x128x8 | 3.4860 | [3.4852, 3.4867] | 0.0000 [0.0000, 0.0000] |
| 2 | 2112x128x8 | 3.4864 | [3.4859, 3.4876] | 0.0009 [-0.0002, 0.0018] |
| 3 | 2112x256x8 | 3.4864 | [3.4860, 3.4869] | 0.0001 [-0.0002, 0.0015] |
| 4 | 2112x128x8 | 3.4864 | [3.4856, 3.4871] | -0.0001 [-0.0009, 0.0013] |
| 5 | 2112x128x8 | 3.4864 | [3.4852, 3.4868] | 0.0003 [-0.0008, 0.0013] |

## route/footprint-mib=1024,kernel=k3,placement=cpu,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 2112x128x8 | 5.3699 | [5.3696, 5.3702] | 0.0000 [0.0000, 0.0000] |
| 2 | 1056x256x8 | 5.3700 | [5.3696, 5.3703] | 0.0001 [-0.0004, 0.0005] |
| 3 | 2112x128x8 | 5.3700 | [5.3698, 5.3706] | 0.0003 [-0.0008, 0.0007] |
| 4 | 1056x256x8 | 5.3702 | [5.3698, 5.3705] | 0.0002 [-0.0001, 0.0006] |
| 5 | 2112x128x8 | 5.3702 | [5.3694, 5.3706] | 0.0002 [-0.0005, 0.0009] |

## route/footprint-mib=1024,kernel=k3,placement=hbm,tune=copy,type=tune

- 30 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-whole | 1.1172 | [1.1168, 1.1177] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole | 1.1173 | [1.1157, 1.1178] | -0.0003 [-0.0021, 0.0011] |
| 3 | kernel-pageable-1-256m-none-whole | 1.1340 | [1.1325, 1.1352] | 0.0171 [0.0153, 0.0176] |
| 4 | kernel-registered-1-256m-none-whole | 1.1355 | [1.1349, 1.1363] | 0.0182 [0.0174, 0.0195] |
| 5 | kernel-pageable-1-64m-none-whole | 1.1782 | [1.1772, 1.1798] | 0.0611 [0.0601, 0.0621] |
| 14 | ce-pageable-1-whole-none-whole | 3.0223 | [3.0201, 3.0232] | 1.9050 [1.9025, 1.9063] |

## route/footprint-mib=1024,kernel=k3,placement=hbm,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 16896x128x8 | 0.4651 | [0.4650, 0.4652] | 0.0000 [0.0000, 0.0000] |
| 2 | 8448x256x8 | 0.4668 | [0.4664, 0.4671] | 0.0017 [0.0013, 0.0020] |
| 3 | 2112x128x8 | 0.4708 | [0.4707, 0.4711] | 0.0056 [0.0054, 0.0061] |
| 4 | 4224x128x8 | 0.4708 | [0.4706, 0.4711] | 0.0057 [0.0054, 0.0061] |
| 5 | 2112x128x8 | 0.4708 | [0.4707, 0.4712] | 0.0057 [0.0055, 0.0062] |

## route/footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 1056x256x8 | 5.3804 | [5.3802, 5.3809] | 0.0000 [0.0000, 0.0000] |
| 2 | 2112x128x8 | 5.3805 | [5.3804, 5.3810] | 0.0002 [-0.0005, 0.0007] |
| 3 | 2112x128x8 | 5.3805 | [5.3801, 5.3817] | 0.0002 [-0.0002, 0.0008] |
| 4 | 2112x256x8 | 5.3806 | [5.3801, 5.3812] | 0.0002 [-0.0005, 0.0008] |
| 5 | 2112x256x8 | 5.3806 | [5.3801, 5.3810] | 0.0002 [-0.0006, 0.0008] |

## route/footprint-mib=16384,kernel=k3,page-size=512m,placement=hbm,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 16896x128x8 | 0.4777 | [0.4776, 0.4778] | 0.0000 [0.0000, 0.0000] |
| 2 | 8448x256x8 | 0.4789 | [0.4788, 0.4793] | 0.0012 [0.0011, 0.0016] |
| 3 | 4224x128x8 | 0.4800 | [0.4799, 0.4803] | 0.0024 [0.0020, 0.0025] |
| 4 | 4224x128x8 | 0.4800 | [0.4799, 0.4804] | 0.0024 [0.0021, 0.0027] |
| 5 | 2112x256x8 | 0.4800 | [0.4799, 0.4802] | 0.0024 [0.0022, 0.0026] |

## route/footprint-mib=16384,kernel=k3,placement=cpu,tune=copy,type=tune

- 30 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-1-whole-none-whole | 42.6175 | [42.6103, 42.6231] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-2-whole-none-whole | 42.6197 | [42.6174, 42.6228] | 0.0030 [-0.0041, 0.0072] |
| 3 | ce-registered-4-whole-none-whole | 42.6204 | [42.6146, 42.6265] | 0.0016 [-0.0013, 0.0087] |
| 4 | ce-registered-1-256m-none-whole | 42.8570 | [42.8501, 42.8662] | 0.2389 [0.2281, 0.2559] |
| 5 | ce-registered-2-256m-none-whole | 42.9048 | [42.9006, 42.9173] | 0.2863 [0.2776, 0.3062] |
| 8 | ce-pageable-1-whole-none-whole | 43.5979 | [43.5922, 43.6090] | 0.9780 [0.9730, 0.9930] |

## route/footprint-mib=16384,kernel=k3,placement=hbm,tune=copy,type=tune

- 30 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-registered-1-whole-none-whole | 10.6305 | [10.6138, 10.6477] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-pageable-1-whole-none-whole | 10.6563 | [10.6381, 10.7041] | 0.0225 [-0.0049, 0.0895] |
| 3 | kernel-pageable-1-256m-none-whole | 11.0986 | [11.0771, 11.1016] | 0.4554 [0.4475, 0.4846] |
| 4 | kernel-registered-1-256m-none-whole | 11.1095 | [11.1025, 11.1245] | 0.4843 [0.4548, 0.4933] |
| 5 | kernel-pageable-1-64m-none-whole | 11.8204 | [11.8124, 11.8261] | 1.1927 [1.1724, 1.2049] |
| 17 | ce-pageable-1-whole-none-whole | 41.4687 | [41.4566, 41.4796] | 30.8442 [30.7695, 30.8613] |

## route/footprint-mib=16384,kernel=k3,placement=hbm,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 16896x128x8 | 426.0331 | [425.8871, 426.0827] | 0.0000 [0.0000, 0.0000] |
| 2 | 2112x1024x8 | 426.0573 | [425.7229, 426.1441] | -0.0343 [-0.1827, 0.2424] |
| 3 | 8448x256x8 | 426.0614 | [426.0092, 426.1898] | 0.1153 [-0.0246, 0.1704] |
| 4 | 4224x512x8 | 426.0714 | [425.9512, 426.1550] | -0.0054 [-0.0539, 0.1367] |
| 5 | 2112x512x8 | 426.4822 | [426.3715, 426.6778] | 0.4618 [0.4025, 0.5949] |

## route/footprint-mib=16384,kernel=k3p,placement=cpu,tune=direct,type=tune

- 104 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 2112x1024x8 | 7.0024 | [7.0001, 7.0070] | 0.0000 [0.0000, 0.0000] |
| 2 | 1056x1024x16 | 7.0047 | [6.9989, 7.0087] | 0.0036 [-0.0093, 0.0083] |
| 3 | 8448x256x8 | 7.0053 | [7.0018, 7.0143] | 0.0016 [-0.0005, 0.0112] |
| 4 | 1056x1024x16 | 7.0055 | [6.9971, 7.0103] | -0.0009 [-0.0048, 0.0151] |
| 5 | 16896x128x8 | 7.0087 | [7.0053, 7.0185] | 0.0047 [-0.0017, 0.0184] |

## route/footprint-mib=24576,kernel=k3,placement=cpu,tune=copy,type=tune

- 30 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-4-whole-none-whole | 63.6703 | [63.6675, 63.6790] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-2-whole-none-whole | 63.6724 | [63.6691, 63.6783] | 0.0035 [-0.0065, 0.0100] |
| 3 | ce-registered-1-whole-none-whole | 63.6737 | [63.6712, 63.6766] | 0.0027 [-0.0052, 0.0062] |
| 4 | ce-registered-1-256m-none-whole | 64.0429 | [64.0216, 64.0494] | 0.3699 [0.3540, 0.3793] |
| 5 | ce-registered-2-256m-none-whole | 64.1153 | [64.0952, 64.1279] | 0.4447 [0.4180, 0.4647] |
| 7 | ce-pageable-1-whole-none-whole | 64.6688 | [64.6580, 64.6715] | 0.9959 [0.9798, 1.0008] |

## route/footprint-mib=256,kernel=k3,placement=cpu,tune=copy,type=tune

- 30 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-pageable-1-256m-none-whole | 1.1880 | [1.1872, 1.1890] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-pageable-1-whole-none-whole | 1.1882 | [1.1878, 1.1888] | 0.0002 [-0.0010, 0.0013] |
| 3 | kernel-registered-1-256m-none-whole | 1.1954 | [1.1950, 1.1958] | 0.0074 [0.0068, 0.0082] |
| 4 | kernel-registered-1-whole-none-whole | 1.1957 | [1.1953, 1.1963] | 0.0081 [0.0075, 0.0084] |
| 5 | kernel-pageable-1-256m-none-whole | 1.1962 | [1.1950, 1.1972] | 0.0087 [0.0059, 0.0094] |

## route/footprint-mib=256,kernel=k3,placement=cpu,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 2112x256x8 | 5.3102 | [5.3097, 5.3107] | 0.0000 [0.0000, 0.0000] |
| 2 | 2112x256x8 | 5.3103 | [5.3097, 5.3106] | 0.0001 [-0.0006, 0.0008] |
| 3 | 1056x512x8 | 5.3105 | [5.3099, 5.3111] | 0.0002 [-0.0004, 0.0010] |
| 4 | 2112x256x8 | 5.3105 | [5.3101, 5.3107] | 0.0003 [-0.0005, 0.0008] |
| 5 | 1056x512x8 | 5.3107 | [5.3106, 5.3112] | 0.0007 [0.0002, 0.0011] |

## route/footprint-mib=256,kernel=k3,placement=hbm,tune=copy,type=tune

- 30 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-whole | 0.6020 | [0.6014, 0.6025] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole | 0.6020 | [0.6016, 0.6025] | 0.0003 [-0.0009, 0.0007] |
| 3 | kernel-registered-1-256m-none-whole | 0.6022 | [0.6017, 0.6024] | 0.0001 [-0.0008, 0.0005] |
| 4 | kernel-pageable-1-256m-none-whole | 0.6024 | [0.6016, 0.6029] | 0.0003 [-0.0008, 0.0010] |
| 5 | kernel-pageable-1-64m-none-whole | 0.6113 | [0.6111, 0.6116] | 0.0093 [0.0088, 0.0099] |
| 17 | ce-pageable-1-whole-none-whole | 1.0814 | [1.0802, 1.0818] | 0.4790 [0.4781, 0.4802] |

## route/footprint-mib=256,kernel=k3,placement=hbm,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 16896x128x8 | 0.4255 | [0.4254, 0.4257] | 0.0000 [0.0000, 0.0000] |
| 2 | 8448x256x8 | 0.4274 | [0.4272, 0.4275] | 0.0019 [0.0016, 0.0021] |
| 3 | 4224x512x8 | 0.4323 | [0.4321, 0.4329] | 0.0068 [0.0064, 0.0073] |
| 4 | 8448x128x8 | 0.4356 | [0.4354, 0.4361] | 0.0101 [0.0098, 0.0106] |
| 5 | 8448x128x8 | 0.4359 | [0.4356, 0.4362] | 0.0104 [0.0100, 0.0107] |

## route/footprint-mib=32768,kernel=k3,placement=cpu,tune=copy,type=tune

- 30 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-4-whole-none-whole | 84.7124 | [84.7060, 84.7316] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-1-whole-none-whole | 84.7159 | [84.7083, 84.7191] | 0.0010 [-0.0155, 0.0112] |
| 3 | ce-registered-2-whole-none-whole | 84.7172 | [84.7039, 84.7788] | 0.0011 [-0.0189, 0.0630] |
| 4 | ce-registered-1-256m-none-whole | 85.1987 | [85.1701, 85.2164] | 0.4850 [0.4516, 0.5119] |
| 5 | ce-registered-4-256m-none-whole | 85.2790 | [85.2750, 85.3162] | 0.5665 [0.5429, 0.6009] |
| 7 | ce-pageable-1-whole-none-whole | 85.7180 | [85.7137, 85.7267] | 1.0086 [0.9961, 1.0214] |

## route/footprint-mib=32768,kernel=k3,placement=cpu,tune=direct,type=tune

- 52 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | 2112x1024x8 | 682.7763 | [682.6769, 682.9382] | 0.0000 [0.0000, 0.0000] |
| 2 | 16896x128x8 | 682.8064 | [682.7234, 682.9796] | 0.0494 [-0.1291, 0.2979] |
| 3 | 8448x256x8 | 682.8446 | [682.7289, 682.9887] | 0.0923 [-0.0040, 0.1630] |
| 4 | 4224x512x8 | 682.9030 | [682.5944, 683.0343] | 0.1389 [-0.0883, 0.2454] |
| 5 | 8448x128x8 | 683.2002 | [683.1540, 683.3270] | 0.4828 [0.2434, 0.5842] |

## route/footprint-mib=4096,kernel=k3,placement=cpu,tune=copy,type=tune

- 30 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-1-whole-none-whole | 11.0474 | [11.0449, 11.0507] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-4-whole-none-whole | 11.0482 | [11.0456, 11.0498] | 0.0010 [-0.0050, 0.0040] |
| 3 | ce-registered-2-whole-none-whole | 11.0492 | [11.0462, 11.0504] | 0.0010 [-0.0043, 0.0045] |
| 4 | ce-registered-1-256m-none-whole | 11.1045 | [11.1018, 11.1088] | 0.0574 [0.0536, 0.0626] |
| 5 | ce-registered-2-256m-none-whole | 11.1171 | [11.1150, 11.1204] | 0.0694 [0.0651, 0.0755] |
| 14 | ce-pageable-1-whole-none-whole | 11.9754 | [11.9701, 11.9775] | 0.9280 [0.9203, 0.9308] |

## route/footprint-mib=4096,kernel=k3,placement=hbm,tune=copy,type=tune

- 30 configurations, 10 rounds; every round ran in the drawn order: yes; stopped on target: yes, cap hit: no; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-whole | 3.0311 | [3.0273, 3.0379] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole | 3.0431 | [3.0334, 3.0460] | 0.0101 [0.0048, 0.0145] |
| 3 | kernel-pageable-1-256m-none-whole | 3.1333 | [3.1317, 3.1351] | 0.1032 [0.0928, 0.1065] |
| 4 | kernel-registered-1-256m-none-whole | 3.1360 | [3.1333, 3.1394] | 0.1058 [0.0990, 0.1091] |
| 5 | kernel-registered-1-64m-none-whole | 3.3071 | [3.3058, 3.3098] | 0.2767 [0.2675, 0.2827] |
| 14 | ce-pageable-1-whole-none-whole | 10.6458 | [10.6051, 10.6546] | 7.6103 [7.5747, 7.6252] |

## route/footprint-mib=8192,kernel=k3,placement=cpu,tune=copy,type=tune

- 30 configurations, 100 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | ce-registered-1-whole-none-whole | 21.5699 | [21.5688, 21.5705] | 0.0000 [0.0000, 0.0000] |
| 2 | ce-registered-2-whole-none-whole | 21.5699 | [21.5679, 21.5716] | 0.0010 [-0.0026, 0.0031] |
| 3 | ce-registered-4-whole-none-whole | 21.5718 | [21.5705, 21.5730] | 0.0014 [-0.0012, 0.0037] |
| 4 | ce-registered-1-256m-none-whole | 21.6842 | [21.6822, 21.6860] | 0.1145 [0.1124, 0.1158] |
| 5 | ce-registered-2-256m-none-whole | 21.7095 | [21.7082, 21.7111] | 0.1401 [0.1380, 0.1420] |
| 12 | ce-pageable-1-whole-none-whole | 22.5817 | [22.5802, 22.5824] | 1.0117 [1.0096, 1.0132] |

## route/footprint-mib=8192,kernel=k3,placement=hbm,tune=copy,type=tune

- 30 configurations, 100 rounds; every round ran in the drawn order: yes; stopped on target: no, cap hit: yes; checks pass

| rank | configuration | ms | interval | slowdown against the fastest ms [interval] |
|---|---|---|---|---|
| 1 | kernel-pageable-1-whole-none-whole | 5.5609 | [5.5598, 5.5631] | 0.0000 [0.0000, 0.0000] |
| 2 | kernel-registered-1-whole-none-whole | 5.5745 | [5.5705, 5.5770] | 0.0084 [0.0065, 0.0138] |
| 3 | kernel-registered-1-256m-none-whole | 5.7884 | [5.7868, 5.7891] | 0.2277 [0.2233, 0.2290] |
| 4 | kernel-pageable-1-256m-none-whole | 5.7889 | [5.7877, 5.7900] | 0.2266 [0.2242, 0.2284] |
| 5 | kernel-registered-1-64m-none-whole | 6.1405 | [6.1388, 6.1415] | 0.5766 [0.5742, 0.5789] |
| 17 | ce-pageable-1-whole-none-whole | 20.9673 | [20.9654, 20.9705] | 15.4043 [15.4003, 15.4082] |

