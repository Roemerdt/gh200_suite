# Four-variant cells: direct and copy route at home and at a level of one factor, recomputed from raw rows

Times are per repetition in ms (one pass for the direct route, one complete call for the copy route). Each round runs the four variants once in the order the seed drew; the route difference at home (A - B) and at the level (C - D) and the change of the route difference, (C - D) - (A - B), are formed within each round and given as median with 95 % rank interval. A negative route difference means direct access is faster; a negative change means the level moved the comparison towards direct access. The relative change is the change over the route difference at home, given only where that difference excludes zero. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | level | direct home ms | copy home ms | direct level ms | copy level ms | route difference home ms [interval] | route difference level ms [interval] | change ms [interval] | relative change | rounds | change excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0393 | 0.1030 | 0.3714 | 0.1375 | -0.0637 [-0.0714, -0.0633] | 0.2335 [0.2249, 0.2357] | 0.2997 [0.2955, 0.3131] | -470.7 % | 100 | yes | pass |
| at=8,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 1.4877 | 0.5639 | 0.0391 | 0.1182 | 0.9235 [0.9004, 0.9248] | -0.0790 [-0.0944, -0.0787] | -1.0068 [-1.0187, -0.9892] | -109.0 % | 100 | yes | pass |
| at=8,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 0.0976 | 0.1788 | 0.0162 | 0.0590 | -0.0811 [-0.0814, -0.0809] | -0.0427 [-0.0428, -0.0426] | 0.0385 [0.0380, 0.0389] | -47.5 % | 20 | yes | pass |
| at=none,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=tiling | tiling | none | 26.2557 | 6.5025 | 36.2260 | 5.9909 | 19.7521 [19.7298, 19.7772] | 30.2341 [30.0448, 30.4021] | 10.5084 [10.2984, 10.6260] | +53.2 % | 10 | yes | pass |
| at=none,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=tiling | tiling | none | 3.2709 | 3.8845 | 2.7564 | 3.3896 | -0.6124 [-0.6151, -0.6112] | -0.6324 [-0.6346, -0.6308] | -0.0182 [-0.0211, -0.0152] | +3.0 % | 100 | yes | pass |
| at=plain,footprint-mib=1024,kernel=k6,placement=cpu,type=four,update=atomic,vary=update | update | plain | 6.0611 | 7.3925 | 5.9829 | 7.2558 | -1.3330 [-1.3385, -1.3303] | -1.2732 [-1.2752, -1.2712] | 0.0606 [0.0558, 0.0634] | -4.5 % | 20 | yes | pass |
| at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,type=four,vary=generator | generator | rmat | 30.6738 | 4.1770 | 188.3055 | 68.2557 | 26.4970 [26.4846, 26.5209] | 120.4664 [119.4394, 121.5338] | 93.9574 [92.9520, 95.0625] | +354.6 % | 10 | yes | pass |
| at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,type=four,vary=generator | generator | rmat | 1.2727 | 1.7648 | 65.9852 | 65.9157 | -0.4919 [-0.4922, -0.4910] | 0.0717 [0.0491, 0.0805] | 0.5634 [0.5423, 0.5722] | -114.5 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | sharing | shared | 0.1931 | 0.2402 | 0.1913 | 0.2428 | -0.0472 [-0.0473, -0.0467] | -0.0514 [-0.0517, -0.0513] | -0.0044 [-0.0050, -0.0042] | +9.2 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 0.1923 | 0.2425 | 0.3790 | 0.4100 | -0.0500 [-0.0506, -0.0493] | -0.0314 [-0.0318, -0.0306] | 0.0189 [0.0174, 0.0192] | -37.8 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | sharing | shared | 0.0385 | 0.0942 | 0.1641 | 0.2164 | -0.0558 [-0.0559, -0.0556] | -0.0521 [-0.0530, -0.0512] | 0.0036 [0.0028, 0.0043] | -6.4 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | sharing | shared | 0.0355 | 0.0927 | 0.1809 | 0.2324 | -0.0571 [-0.0574, -0.0568] | -0.0515 [-0.0518, -0.0511] | 0.0056 [0.0050, 0.0060] | -9.9 % | 60 | yes | pass |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | sharing | shared | 30.8498 | 5.6827 | 30.4063 | 4.0858 | 25.1782 [25.1547, 25.6213] | 26.3198 [26.3158, 26.3260] | 1.1336 [0.7083, 1.1654] | +4.5 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing | sharing | shared | 1.2784 | 1.7695 | 1.2771 | 1.7716 | -0.4911 [-0.4917, -0.4905] | -0.4944 [-0.4950, -0.4935] | -0.0032 [-0.0041, -0.0025] | +0.7 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0457 | 0.0697 | 0.0665 | 0.0886 | -0.0241 [-0.0242, -0.0239] | -0.0221 [-0.0222, -0.0220] | 0.0020 [0.0017, 0.0021] | -8.2 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 1.5148 | 0.0985 | 1.5156 | 0.6816 | 1.4163 [1.4157, 1.4167] | 0.8342 [0.8335, 0.8349] | -0.5826 [-0.5838, -0.5809] | -41.1 % | 70 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0521 | 0.0456 | 0.0532 | 0.6126 | 0.0063 [0.0053, 0.0069] | -0.5595 [-0.5597, -0.5592] | -0.5674 [-0.5701, -0.5656] | -9043.8 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 1.5012 | 0.0976 | 1.5170 | 0.7578 | 1.4035 [1.4028, 1.4042] | 0.7594 [0.7589, 0.7598] | -0.6449 [-0.6460, -0.6436] | -45.9 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0517 | 0.0441 | 0.0513 | 0.7006 | 0.0078 [0.0073, 0.0083] | -0.6499 [-0.6504, -0.6494] | -0.6590 [-0.6606, -0.6569] | -8489.9 % | 80 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 1.5112 | 0.2157 | 1.4853 | 0.2183 | 1.2955 [1.2934, 1.2983] | 1.2672 [1.2659, 1.2682] | -0.0281 [-0.0301, -0.0254] | -2.2 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | sharing | shared | 0.0517 | 0.0853 | 0.0521 | 0.0855 | -0.0336 [-0.0341, -0.0331] | -0.0332 [-0.0335, -0.0328] | 0.0006 [0.0002, 0.0011] | -1.8 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.1141 | 0.1093 | 0.1119 | 0.2828 | 0.0049 [0.0045, 0.0054] | -0.1709 [-0.1718, -0.1699] | -0.1759 [-0.1770, -0.1752] | -3556.2 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.1153 | 0.1104 | 0.1144 | 0.7357 | 0.0053 [0.0045, 0.0055] | -0.6211 [-0.6222, -0.6204] | -0.6263 [-0.6274, -0.6254] | -11805.3 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.1249 | 0.2229 | 0.1257 | 0.2230 | -0.0973 [-0.0990, -0.0966] | -0.0963 [-0.0971, -0.0954] | 0.0020 [0.0007, 0.0031] | -2.1 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 7.2627 | 44.0425 | 7.2294 | 42.3572 | -36.7802 [-36.7858, -36.7774] | -35.1272 [-35.1416, -35.1187] | 1.6550 [1.6425, 1.6581] | -4.5 % | 10 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 433.6746 | 0.5126 | 433.7350 | 5.1567 | 433.1623 [433.0096, 433.3397] | 428.5824 [428.4817, 428.7859] | -4.5931 [-4.8091, -4.2669] | -1.1 % | 10 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1 | sharing | shared | 433.5235 | 0.5107 | 433.5817 | 10.7031 | 433.0135 [432.6889, 433.2104] | 422.8821 [422.7529, 423.0022] | -10.0851 [-10.4575, -9.7750] | -2.3 % | 10 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 433.5928 | 44.4440 | 433.5835 | 43.0155 | 389.1481 [389.1093, 389.2267] | 390.5455 [390.5003, 390.6369] | 1.3924 [1.3116, 1.4551] | +0.4 % | 20 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing | sharing | shared | 26.7088 | 6.5257 | 23.0845 | 6.4954 | 20.1851 [20.1605, 20.2174] | 16.5911 [16.5802, 16.5966] | -3.5967 [-3.6245, -3.5801] | -17.8 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing | sharing | shared | 3.2816 | 3.8705 | 3.2776 | 3.8709 | -0.5893 [-0.5903, -0.5878] | -0.5938 [-0.5957, -0.5916] | -0.0043 [-0.0069, -0.0018] | +0.7 % | 100 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 26.7668 | 5.0384 | 23.1233 | 5.3290 | 21.7280 [21.6777, 21.7457] | 17.7949 [17.7777, 17.7995] | -3.9267 [-3.9507, -3.8883] | -18.1 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 26.4625 | 5.0446 | 23.1119 | 5.3847 | 21.4135 [21.3902, 21.4881] | 17.7281 [17.7139, 17.7379] | -3.6876 [-3.7628, -3.6545] | -17.2 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 26.3549 | 6.5280 | 23.0167 | 6.5997 | 19.8274 [19.8203, 19.8691] | 16.4168 [16.3950, 16.4268] | -3.4244 [-3.4583, -3.3973] | -17.3 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 3.4542 | 3.5479 | 3.6012 | 3.6473 | -0.0928 [-0.0975, -0.0872] | -0.0454 [-0.0507, -0.0422] | 0.0454 [0.0429, 0.0520] | -49.0 % | 20 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 3.5517 | 3.5669 | 3.5976 | 3.8791 | -0.0157 [-0.0179, -0.0141] | -0.2808 [-0.2830, -0.2793] | -0.2654 [-0.2690, -0.2624] | +1692.0 % | 100 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 3.4827 | 4.0132 | 3.6101 | 3.9932 | -0.5266 [-0.5324, -0.5221] | -0.3838 [-0.3933, -0.3740] | 0.1413 [0.1366, 0.1537] | -26.8 % | 10 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 8.0730 | 0.5599 | 8.0996 | 1.7231 | 7.5129 [7.5079, 7.5191] | 6.3747 [6.3606, 6.3826] | -1.1380 [-1.1515, -1.1259] | -15.1 % | 10 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1 | sharing | shared | 8.0868 | 0.5623 | 8.1088 | 5.3978 | 7.5250 [7.5137, 7.5310] | 2.7150 [2.7014, 2.7477] | -4.8019 [-4.8196, -4.7801] | -63.8 % | 10 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | sharing | shared | 8.0980 | 5.6368 | 8.1037 | 5.6599 | 2.4604 [2.4578, 2.4637] | 2.4434 [2.4397, 2.4478] | -0.0146 [-0.0197, -0.0112] | -0.6 % | 100 | yes | pass |
| at=sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8 | scope | sys | 0.0395 | 0.1011 | 0.4040 | 0.1191 | -0.0616 [-0.0621, -0.0544] | 0.2845 [0.2742, 0.2857] | 0.3443 [0.3400, 0.3491] | -559.2 % | 100 | yes | pass |

## Host phases

The CPU phase before every pass, timed on the CPU clock (ms per pass), and the state check's median load latency on the preparing core after the phase (ns per sampled load), per variant.

| cell | direct home CPU ms | direct home state ns | copy home CPU ms | copy home state ns | direct level CPU ms | direct level state ns | copy level CPU ms | copy level state ns |
|---|---|---|---|---|---|---|---|---|
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | 5.2227 | 67.0 | 5.2258 | 73.5 | 5.3756 | 100.4 | 5.3876 | 94.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 2.7464 | 65.6 | 2.7579 | 82.2 | 2.6594 | 88.5 | 2.6623 | 90.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | 4.9922 | 63.8 | 5.1391 | 75.8 | 5.0451 | 98.2 | 5.0376 | 82.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | 2.8629 | 64.0 | 2.9836 | 87.6 | 3.0807 | 90.2 | 3.1453 | 88.9 |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | 1.2307 | - | 1.2169 | - | 1.6507 | - | 1.6560 | - |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing | 2.3811 | - | 3.7190 | - | 3.6957 | - | 3.1236 | - |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | 0.5233 | 67.1 | 0.5273 | 68.6 | 0.5200 | 67.2 | 0.5230 | 70.6 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 3.6218 | 76.2 | 3.6177 | 128.0 | 3.6162 | 135.4 | 4.0673 | 138.8 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | 3.6287 | 124.5 | 3.6318 | 164.2 | 3.6190 | 221.2 | 4.0882 | 188.0 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32 | 3.6362 | 121.4 | 3.6284 | 169.1 | 3.6141 | 201.0 | 4.1168 | 219.1 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=8 | 3.6216 | 94.1 | 3.6260 | 150.9 | 3.6184 | 171.5 | 4.0984 | 182.6 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | 22.4322 | 269.9 | 19.8147 | 273.4 | 22.5358 | 297.9 | 19.8099 | 300.4 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | 20.0028 | 265.9 | 19.9706 | 260.8 | 20.0028 | 291.0 | 19.9705 | 320.4 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 4.5327 | 360.1 | 4.5147 | 429.4 | 4.5251 | 437.8 | 4.5604 | 430.6 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32 | 5.0734 | 401.0 | 4.8368 | 453.2 | 4.6492 | 472.5 | 4.6536 | 448.5 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | 27.4640 | 539.9 | 27.4963 | 576.4 | 27.7202 | 573.0 | 27.2608 | 579.0 |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 1.8594 | 146.8 | 1.8296 | 170.5 | 2.8576 | 146.6 | 2.9484 | 148.4 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 32.3107 | 305.9 | 31.5374 | 317.5 | 33.5231 | 307.9 | 31.9075 | 275.9 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1 | 33.1150 | 301.5 | 32.1130 | 314.2 | 34.6450 | 308.5 | 33.7871 | 296.5 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 268.4796 | 384.0 | 269.1687 | 379.0 | 268.1941 | 368.4 | 268.9907 | 384.0 |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing | 27.2457 | - | 27.2040 | - | 28.2060 | - | 28.2362 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing | 62.8914 | - | 62.9766 | - | 62.5096 | - | 62.5644 | - |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | 1.9054 | 71.9 | 1.9773 | 112.8 | 1.9882 | 123.0 | 2.0198 | 124.5 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | 1.9617 | 102.4 | 1.9764 | 124.1 | 1.9934 | 152.4 | 2.0342 | 142.4 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1 | 13.2904 | 252.9 | 13.4057 | 258.0 | 13.2525 | 268.8 | 13.3100 | 273.2 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.5829 | 162.8 | 2.6010 | 204.1 | 2.5703 | 213.4 | 2.5447 | 213.8 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.5696 | 214.2 | 2.5677 | 245.1 | 2.5528 | 274.5 | 2.5513 | 270.4 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1 | 16.2208 | 483.6 | 15.7395 | 515.2 | 16.4070 | 508.2 | 15.7901 | 537.8 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | 23.8589 | 541.1 | 23.5533 | 575.2 | 23.9029 | 573.2 | 24.3163 | 569.9 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1 | 23.8842 | 558.8 | 25.4545 | 589.0 | 24.1069 | 625.1 | 23.5947 | 576.9 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | 160.4802 | 613.9 | 165.3000 | 629.2 | 167.6512 | 626.4 | 165.1673 | 613.1 |

## Per cell

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x41cbc0000000, copy home 0x41ccc0000000, direct level 0x41cd80000000, copy level 0x41ce40000000
- factor effect within the cell: on the direct route 0.3321 [0.3319, 0.3324] ms, on the copy route 0.0321 [0.0189, 0.0364] ms; change relative to the copy call at home: +291.0 %
- per repetition: direct home 8.429e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.8 SMMU translation requests; direct level 1.341e+08 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x5643c0000000, copy home 0x564480000000, direct level 0x564540000000, copy level 0x564600000000
- factor effect within the cell: on the direct route -1.4486 [-1.4487, -1.4484] ms, on the copy route -0.4418 [-0.4593, -0.4293] ms; change relative to the copy call at home: -178.5 %
- per repetition: direct home 5.366e+08 link read bytes and 0 SMMU translation requests; copy home 3.354e+07 link read bytes and 533 SMMU translation requests; direct level 8.429e+06 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4db480000000, copy home 0x4db540000000, direct level 0x4db600000000, copy level 0x4db6c0000000
- factor effect within the cell: on the direct route -0.0814 [-0.0814, -0.0813] ms, on the copy route -0.1199 [-0.1203, -0.1194] ms; change relative to the copy call at home: +21.6 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 519.8 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=none,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=tiling

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4a58c0000000, copy home 0x4a59c0000000, direct level 0x4a5a80000000, copy level 0x4a5b80000000
- factor effect within the cell: on the direct route 9.9947 [9.7856, 10.1113] ms, on the copy route -0.5106 [-0.5172, -0.5045] ms; change relative to the copy call at home: +161.6 %
- per repetition: direct home 6.423e+09 link read bytes and 3.614e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 1.31e+10 link read bytes and 3.643e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=none,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=tiling

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x53dd80000000, copy home 0x53dec0000000, direct level 0x53df80000000, copy level 0x53e080000000
- factor effect within the cell: on the direct route -0.5121 [-0.5155, -0.5099] ms, on the copy route -0.4943 [-0.4970, -0.4916] ms; change relative to the copy call at home: -0.5 %
- per repetition: direct home 0 link read bytes and 5938 SMMU translation requests; copy home 0 link read bytes and 5434 SMMU translation requests; direct level 0 link read bytes and 9014 SMMU translation requests; copy level 0 link read bytes and 5428 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=1024,kernel=k6,placement=cpu,type=four,update=atomic,vary=update

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x450c40000000, copy home 0x450d40000000, direct level 0x450e00000000, copy level 0x450ec0000000
- factor effect within the cell: on the direct route -0.0764 [-0.0807, -0.0727] ms, on the copy route -0.1355 [-0.1379, -0.1336] ms; change relative to the copy call at home: +0.8 %
- per repetition: direct home 0 link read bytes and 4209 SMMU translation requests; copy home 1.074e+09 link read bytes and 3.278e+04 SMMU translation requests; direct level 1.074e+09 link read bytes and 4579 SMMU translation requests; copy level 1.074e+09 link read bytes and 3.278e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,type=four,vary=generator

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x434940000000, copy home 0x434a80000000, direct level 0x434b40000000, copy level 0x434c00000000
- factor effect within the cell: on the direct route 157.6157 [157.0298, 158.1819] ms, on the copy route 64.0784 [63.1150, 64.1046] ms; change relative to the copy call at home: +2249.4 %
- per repetition: direct home 3.203e+09 link read bytes and 0 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.689e+04 SMMU translation requests; direct level 2.853e+09 link read bytes and 0 SMMU translation requests; copy level 1.074e+09 link read bytes and 1.689e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,type=four,vary=generator

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x5e1a80000000, copy home 0x5e1b80000000, direct level 0x5e1c40000000, copy level 0x5e1d00000000
- factor effect within the cell: on the direct route 64.7120 [63.8041, 64.7404] ms, on the copy route 64.1511 [63.2401, 64.1807] ms; change relative to the copy call at home: +31.9 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 0 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x492700000000, copy home 0x492780000000, direct level 0x492800000000, copy level 0x492880000000
- factor effect within the cell: on the direct route -0.0019 [-0.0021, -0.0017] ms, on the copy route 0.0027 [0.0023, 0.0031] ms; change relative to the copy call at home: -1.8 %
- per repetition: direct home 6.711e+07 link read bytes and 2200 SMMU translation requests; copy home 6.711e+07 link read bytes and 1043 SMMU translation requests; direct level 6.711e+07 link read bytes and 2110 SMMU translation requests; copy level 6.711e+07 link read bytes and 1043 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x55a380000000, copy home 0x55a440000000, direct level 0x55a4c0000000, copy level 0x55a540000000
- factor effect within the cell: on the direct route 0.1865 [0.1859, 0.1872] ms, on the copy route 0.1675 [0.1669, 0.1689] ms; change relative to the copy call at home: +7.8 %
- per repetition: direct home 6.711e+07 link read bytes and 2242 SMMU translation requests; copy home 6.711e+07 link read bytes and 1043 SMMU translation requests; direct level 6.711e+07 link read bytes and 1792 SMMU translation requests; copy level 6.711e+07 link read bytes and 1058 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x401980000000, copy home 0x401a40000000, direct level 0x401ac0000000, copy level 0x401b40000000
- factor effect within the cell: on the direct route 0.1255 [0.1251, 0.1259] ms, on the copy route 0.1220 [0.1217, 0.1223] ms; change relative to the copy call at home: +3.8 %
- per repetition: direct home 0 link read bytes and 2894 SMMU translation requests; copy home 0 link read bytes and 3895 SMMU translation requests; direct level 0 link read bytes and 2036 SMMU translation requests; copy level 0 link read bytes and 1546 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x513080000000, copy home 0x513100000000, direct level 0x5131c0000000, copy level 0x513240000000
- factor effect within the cell: on the direct route 0.1453 [0.1451, 0.1456] ms, on the copy route 0.1397 [0.1394, 0.1402] ms; change relative to the copy call at home: +6.1 %
- per repetition: direct home 0 link read bytes and 2914 SMMU translation requests; copy home 0 link read bytes and 3859 SMMU translation requests; direct level 0 link read bytes and 2103 SMMU translation requests; copy level 0 link read bytes and 1607 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x525740000000, copy home 0x525840000000, direct level 0x525900000000, copy level 0x5259c0000000
- factor effect within the cell: on the direct route -0.4374 [-0.4493, -0.4329] ms, on the copy route -1.5961 [-1.6048, -1.1372] ms; change relative to the copy call at home: +19.9 %
- per repetition: direct home 3.195e+09 link read bytes and 0 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.689e+04 SMMU translation requests; direct level 3.2e+09 link read bytes and 0 SMMU translation requests; copy level 1.074e+09 link read bytes and 1.689e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x48f640000000, copy home 0x48f740000000, direct level 0x48f800000000, copy level 0x48f8c0000000
- factor effect within the cell: on the direct route -0.0013 [-0.0021, -0.0007] ms, on the copy route 0.0021 [0.0016, 0.0027] ms; change relative to the copy call at home: -0.2 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 0 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x52e740000000, copy home 0x52e840000000, direct level 0x52e900000000, copy level 0x52e9c0000000
- factor effect within the cell: on the direct route 0.0208 [0.0208, 0.0209] ms, on the copy route 0.0189 [0.0187, 0.0191] ms; change relative to the copy call at home: +2.8 %
- per repetition: direct home 8.429e+06 link read bytes and 315.4 SMMU translation requests; copy home 8.38e+06 link read bytes and 131.2 SMMU translation requests; direct level 8.429e+06 link read bytes and 296.1 SMMU translation requests; copy level 8.38e+06 link read bytes and 142.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x577440000000, copy home 0x577540000000, direct level 0x577600000000, copy level 0x5776c0000000
- factor effect within the cell: on the direct route 0.0014 [0.0004, 0.0024] ms, on the copy route 0.5834 [0.5828, 0.5840] ms; change relative to the copy call at home: -591.3 %
- per repetition: direct home 5.366e+08 link read bytes and 816.2 SMMU translation requests; copy home 0 link read bytes and 14.72 SMMU translation requests; direct level 5.366e+08 link read bytes and 813 SMMU translation requests; copy level 1.074e+08 link read bytes and 2.323e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x5b3380000000, copy home 0x5b3480000000, direct level 0x5b3540000000, copy level 0x5b3600000000
- factor effect within the cell: on the direct route 0.0010 [0.0006, 0.0017] ms, on the copy route 0.5669 [0.5667, 0.5676] ms; change relative to the copy call at home: -1244.8 %
- per repetition: direct home 8.429e+06 link read bytes and 330.5 SMMU translation requests; copy home 0 link read bytes and 15.04 SMMU translation requests; direct level 8.429e+06 link read bytes and 329.4 SMMU translation requests; copy level 1.074e+08 link read bytes and 2.349e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x5b2ac0000000, copy home 0x5b2bc0000000, direct level 0x5b2c80000000, copy level 0x5b2d40000000
- factor effect within the cell: on the direct route 0.0158 [0.0152, 0.0168] ms, on the copy route 0.6606 [0.6600, 0.6614] ms; change relative to the copy call at home: -661.0 %
- per repetition: direct home 5.366e+08 link read bytes and 838.9 SMMU translation requests; copy home 0 link read bytes and 14.72 SMMU translation requests; direct level 5.366e+08 link read bytes and 813.6 SMMU translation requests; copy level 1.074e+08 link read bytes and 5.061e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=8

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5dc980000000, copy home 0x5dca40000000, direct level 0x5dcb00000000, copy level 0x5dcbc0000000
- factor effect within the cell: on the direct route -0.0005 [-0.0008, -0.0002] ms, on the copy route 0.6568 [0.6562, 0.6576] ms; change relative to the copy call at home: -1494.6 %
- per repetition: direct home 8.429e+06 link read bytes and 329.1 SMMU translation requests; copy home 0 link read bytes and 14.72 SMMU translation requests; direct level 8.428e+06 link read bytes and 329.5 SMMU translation requests; copy level 1.074e+08 link read bytes and 5.08e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4e0ec0000000, copy home 0x4e0fc0000000, direct level 0x4e1080000000, copy level 0x4e1140000000
- factor effect within the cell: on the direct route -0.0254 [-0.0264, -0.0235] ms, on the copy route 0.0030 [0.0007, 0.0046] ms; change relative to the copy call at home: -13.0 %
- per repetition: direct home 5.366e+08 link read bytes and 472.2 SMMU translation requests; copy home 3.354e+07 link read bytes and 539 SMMU translation requests; direct level 5.366e+08 link read bytes and 492.8 SMMU translation requests; copy level 3.354e+07 link read bytes and 539.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x5cb780000000, copy home 0x5cb840000000, direct level 0x5cb900000000, copy level 0x5cb9c0000000
- factor effect within the cell: on the direct route 0.0007 [0.0003, 0.0009] ms, on the copy route 0.0001 [-0.0004, 0.0009] ms; change relative to the copy call at home: +0.7 %
- per repetition: direct home 8.429e+06 link read bytes and 319.9 SMMU translation requests; copy home 8.38e+06 link read bytes and 147.6 SMMU translation requests; direct level 8.429e+06 link read bytes and 319.1 SMMU translation requests; copy level 8.38e+06 link read bytes and 149.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4dd300000000, copy home 0x4dd400000000, direct level 0x4dd4c0000000, copy level 0x4dd580000000
- factor effect within the cell: on the direct route -0.0024 [-0.0025, -0.0020] ms, on the copy route 0.1740 [0.1731, 0.1746] ms; change relative to the copy call at home: -160.9 %
- per repetition: direct home 0 link read bytes and 946 SMMU translation requests; copy home 0 link read bytes and 16 SMMU translation requests; direct level 0 link read bytes and 947.7 SMMU translation requests; copy level 0 link read bytes and 3.975e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5041c0000000, copy home 0x5042c0000000, direct level 0x504380000000, copy level 0x504440000000
- factor effect within the cell: on the direct route -0.0011 [-0.0013, -0.0008] ms, on the copy route 0.6248 [0.6244, 0.6265] ms; change relative to the copy call at home: -567.5 %
- per repetition: direct home 0 link read bytes and 950.3 SMMU translation requests; copy home 0 link read bytes and 16 SMMU translation requests; direct level 0 link read bytes and 943.3 SMMU translation requests; copy level 0 link read bytes and 4.809e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x47f300000000, copy home 0x47f400000000, direct level 0x47f4c0000000, copy level 0x47f580000000
- factor effect within the cell: on the direct route 0.0007 [0.0001, 0.0012] ms, on the copy route -0.0007 [-0.0020, 0.0001] ms; change relative to the copy call at home: +0.9 %
- per repetition: direct home 0 link read bytes and 945.8 SMMU translation requests; copy home 0 link read bytes and 549.5 SMMU translation requests; direct level 0 link read bytes and 943.2 SMMU translation requests; copy level 0 link read bytes and 547.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x54b1c0000000, copy home 0x54b640000000, direct level 0x54bac0000000, copy level 0x54bf40000000
- factor effect within the cell: on the direct route -0.0319 [-0.0435, -0.0234] ms, on the copy route -1.6851 [-1.6894, -1.6754] ms; change relative to the copy call at home: +3.8 %
- per repetition: direct home 3.355e+07 link read bytes and 2.026e+06 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; direct level 3.355e+07 link read bytes and 2.016e+06 SMMU translation requests; copy level 1.723e+10 link read bytes and 2.623e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x49c2c0000000, copy home 0x49c740000000, direct level 0x49cbc0000000, copy level 0x49d080000000
- factor effect within the cell: on the direct route 0.0490 [-0.1659, 0.3830] ms, on the copy route 4.6447 [4.6418, 4.6499] ms; change relative to the copy call at home: -896.1 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 0 link read bytes and 2.5 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy level 1.718e+09 link read bytes and 2.996e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5cc240000000, copy home 0x5cc700000000, direct level 0x5ccb80000000, copy level 0x5cd040000000
- factor effect within the cell: on the direct route 0.1023 [-0.2648, 0.4102] ms, on the copy route 10.1930 [10.1862, 10.1976] ms; change relative to the copy call at home: -1974.7 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 0 link read bytes and 2.112 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy level 1.718e+09 link read bytes and 6.431e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5d5ac0000000, copy home 0x5d5f40000000, direct level 0x5d63c0000000, copy level 0x5d6880000000
- factor effect within the cell: on the direct route -0.0481 [-0.0944, 0.0244] ms, on the copy route -1.4258 [-1.4467, -1.4071] ms; change relative to the copy call at home: +3.1 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy level 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5b5940000000, copy home 0x5b5a80000000, direct level 0x5b5b40000000, copy level 0x5b5c40000000
- factor effect within the cell: on the direct route -3.6231 [-3.6584, -3.6084] ms, on the copy route -0.0291 [-0.0346, -0.0261] ms; change relative to the copy call at home: -55.1 %
- per repetition: direct home 6.422e+09 link read bytes and 3.623e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 6.423e+09 link read bytes and 3.615e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x416800000000, copy home 0x416900000000, direct level 0x416a00000000, copy level 0x416ac0000000
- factor effect within the cell: on the direct route -0.0036 [-0.0049, -0.0016] ms, on the copy route 0.0001 [-0.0011, 0.0011] ms; change relative to the copy call at home: -0.1 %
- per repetition: direct home 0 link read bytes and 5490 SMMU translation requests; copy home 0 link read bytes and 6092 SMMU translation requests; direct level 0 link read bytes and 5460 SMMU translation requests; copy level 0 link read bytes and 6013 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x57d840000000, copy home 0x57d940000000, direct level 0x57da40000000, copy level 0x57db00000000
- factor effect within the cell: on the direct route -3.6360 [-3.6688, -3.5936] ms, on the copy route 0.2897 [0.2824, 0.2968] ms; change relative to the copy call at home: -77.9 %
- per repetition: direct home 6.422e+09 link read bytes and 3.612e+04 SMMU translation requests; copy home 0 link read bytes and 8209 SMMU translation requests; direct level 6.423e+09 link read bytes and 3.596e+04 SMMU translation requests; copy level 5.369e+07 link read bytes and 2.484e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x562700000000, copy home 0x562800000000, direct level 0x5628c0000000, copy level 0x5629c0000000
- factor effect within the cell: on the direct route -3.3484 [-3.4266, -3.3175] ms, on the copy route 0.3376 [0.3353, 0.3433] ms; change relative to the copy call at home: -73.1 %
- per repetition: direct home 6.422e+09 link read bytes and 3.61e+04 SMMU translation requests; copy home 0 link read bytes and 8209 SMMU translation requests; direct level 6.423e+09 link read bytes and 3.621e+04 SMMU translation requests; copy level 5.369e+07 link read bytes and 3.31e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x567ec0000000, copy home 0x567fc0000000, direct level 0x568080000000, copy level 0x568180000000
- factor effect within the cell: on the direct route -3.3540 [-3.3839, -3.3190] ms, on the copy route 0.0743 [0.0636, 0.0783] ms; change relative to the copy call at home: -52.5 %
- per repetition: direct home 6.422e+09 link read bytes and 3.614e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 6.423e+09 link read bytes and 3.6e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.646e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x50cc40000000, copy home 0x50cd80000000, direct level 0x50ce80000000, copy level 0x50cf40000000
- factor effect within the cell: on the direct route 0.1444 [0.1422, 0.1485] ms, on the copy route 0.1005 [0.0954, 0.1056] ms; change relative to the copy call at home: +1.3 %
- per repetition: direct home 0 link read bytes and 4.268e+04 SMMU translation requests; copy home 0 link read bytes and 1.288e+04 SMMU translation requests; direct level 0 link read bytes and 4.151e+04 SMMU translation requests; copy level 0 link read bytes and 3.022e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x4fe940000000, copy home 0x4fea40000000, direct level 0x4feb00000000, copy level 0x4fec00000000
- factor effect within the cell: on the direct route 0.0463 [0.0441, 0.0492] ms, on the copy route 0.3122 [0.3108, 0.3138] ms; change relative to the copy call at home: -7.4 %
- per repetition: direct home 0 link read bytes and 3.86e+04 SMMU translation requests; copy home 0 link read bytes and 1.279e+04 SMMU translation requests; direct level 0 link read bytes and 4.158e+04 SMMU translation requests; copy level 0 link read bytes and 3.594e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x54e800000000, copy home 0x54e940000000, direct level 0x54ea00000000, copy level 0x54eb00000000
- factor effect within the cell: on the direct route 0.1220 [0.1175, 0.1334] ms, on the copy route -0.0204 [-0.0281, -0.0073] ms; change relative to the copy call at home: +3.5 %
- per repetition: direct home 0 link read bytes and 4.258e+04 SMMU translation requests; copy home 0 link read bytes and 3.168e+04 SMMU translation requests; direct level 0 link read bytes and 4.125e+04 SMMU translation requests; copy level 0 link read bytes and 3.081e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x481000000000, copy home 0x481280000000, direct level 0x481500000000, copy level 0x4817c0000000
- factor effect within the cell: on the direct route 0.0272 [0.0171, 0.0316] ms, on the copy route 1.1630 [1.1617, 1.1747] ms; change relative to the copy call at home: -203.3 %
- per repetition: direct home 0 link read bytes and 1.328e+05 SMMU translation requests; copy home 0 link read bytes and 16.81 SMMU translation requests; direct level 0 link read bytes and 1.327e+05 SMMU translation requests; copy level 0 link read bytes and 3.147e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x47cfc0000000, copy home 0x47d280000000, direct level 0x47d500000000, copy level 0x47d7c0000000
- factor effect within the cell: on the direct route 0.0191 [0.0136, 0.0308] ms, on the copy route 4.8356 [4.7918, 4.8445] ms; change relative to the copy call at home: -854.0 %
- per repetition: direct home 0 link read bytes and 1.33e+05 SMMU translation requests; copy home 0 link read bytes and 16.83 SMMU translation requests; direct level 0 link read bytes and 1.327e+05 SMMU translation requests; copy level 0 link read bytes and 3.401e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x4cb240000000, copy home 0x4cb500000000, direct level 0x4cb780000000, copy level 0x4cba40000000
- factor effect within the cell: on the direct route 0.0057 [0.0040, 0.0092] ms, on the copy route 0.0236 [0.0184, 0.0283] ms; change relative to the copy call at home: -0.3 %
- per repetition: direct home 0 link read bytes and 1.329e+05 SMMU translation requests; copy home 0 link read bytes and 2.742e+05 SMMU translation requests; direct level 0 link read bytes and 1.327e+05 SMMU translation requests; copy level 0 link read bytes and 2.884e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x4e5e40000000, copy home 0x4e5f40000000, direct level 0x4e6000000000, copy level 0x4e60c0000000
- factor effect within the cell: on the direct route 0.3644 [0.3642, 0.3646] ms, on the copy route 0.0205 [0.0161, 0.0248] ms; change relative to the copy call at home: +340.5 %
- per repetition: direct home 8.429e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.8 SMMU translation requests; direct level 1.341e+08 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.9 SMMU translation requests; multiplexed rows voided: 0

