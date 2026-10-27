# Route cells: direct route against copy route, recomputed from raw rows

Times are per repetition in ms: one pass for the direct route, one complete call (copy-in, kernel, copy-out) for the copy route. The route difference is direct minus copy within a repeat, as median with its 95 % rank interval; a negative value means direct access is faster. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | direct ms | copy ms | route difference ms [interval] | relative to copy | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|
| alignment=off512m,footprint-mib=8192,kernel=k3,placement=cpu | 48.1696 | 23.4753 | 24.6943 [24.6168, 24.7183] | +105.2 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 2.9135 | 3.2732 | -0.3598 [-0.3615, -0.3569] | -11.0 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | 0.2986 | 0.9471 | -0.6485 [-0.6499, -0.6472] | -68.5 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=cpu | 45.6092 | 46.4955 | -0.8890 [-0.9050, -0.8309] | -1.9 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=hbm | 5.7494 | 14.6625 | -8.9149 [-8.9467, -8.8833] | -60.8 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=19456,kernel=k1,placement=cpu | 54.1659 | 54.0988 | 0.0728 [0.0628, 0.0794] | +0.1 % | 100 | yes | pass |
| f-den=1,f-num=1,footprint-mib=23296,kernel=k1,placement=cpu | 64.9823 | 62.0231 | 2.9714 [2.9374, 3.0127] | +4.8 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=cpu | 67.8226 | 67.6243 | 0.1871 [0.1765, 0.2107] | +0.3 % | 50 | yes | pass |
| f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=hbm | 9.6078 | 22.6581 | -13.0517 [-13.0924, -12.9371] | -57.6 % | 30 | yes | pass |
| f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu | 0.7308 | 0.8603 | -0.1293 [-0.1305, -0.1290] | -15.0 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm | 0.0785 | 0.7321 | -0.6537 [-0.6543, -0.6530] | -89.3 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=cpu | 89.9999 | 87.1456 | 2.8593 [2.8259, 2.9264] | +3.3 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu | 11.6671 | 12.6128 | -0.9460 [-0.9545, -0.9411] | -7.5 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=hbm | 1.1738 | 3.6726 | -2.4986 [-2.5002, -2.4977] | -68.0 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,sharing=shared,state=clean | 0.1917 | 0.2420 | -0.0504 [-0.0505, -0.0501] | -20.8 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,sharing=shared,state=dirty | 0.3336 | 0.3647 | -0.0310 [-0.0321, -0.0298] | -8.5 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,sharing=shared,state=evicted | 0.1922 | 0.2404 | -0.0481 [-0.0491, -0.0477] | -20.0 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,sharing=shared,state=clean | 0.1595 | 0.2099 | -0.0502 [-0.0521, -0.0485] | -23.9 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,sharing=shared,state=dirty | 0.1419 | 0.1920 | -0.0498 [-0.0505, -0.0492] | -26.0 % | 20 | yes | pass |
| f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,sharing=shared,state=evicted | 0.0365 | 0.0941 | -0.0576 [-0.0581, -0.0575] | -61.1 % | 20 | yes | pass |
| f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=cpu | 23.1646 | 23.0780 | 0.0881 [0.0821, 0.0986] | +0.4 % | 40 | yes | pass |
| f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=hbm | 2.4084 | 7.3989 | -4.9904 [-4.9969, -4.9856] | -67.4 % | 10 | yes | pass |
| f-den=10,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 0.3005 | 0.3599 | -0.0594 [-0.0597, -0.0591] | -16.5 % | 10 | yes | pass |
| f-den=10,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | 0.0381 | 0.1243 | -0.0862 [-0.0864, -0.0860] | -69.3 % | 10 | yes | pass |
| f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=cpu | 2.6435 | 3.2517 | -0.6080 [-0.6099, -0.6046] | -18.7 % | 10 | yes | pass |
| f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=hbm | 0.2765 | 0.8776 | -0.6011 [-0.6021, -0.6004] | -68.5 % | 10 | yes | pass |
| f-den=100,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 0.0380 | 0.0519 | -0.0139 [-0.0140, -0.0138] | -26.8 % | 10 | yes | pass |
| f-den=100,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | 0.0102 | 0.0328 | -0.0225 [-0.0229, -0.0224] | -68.8 % | 10 | yes | pass |
| f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 0.0158 | 0.0176 | -0.0018 [-0.0018, -0.0018] | -10.4 % | 10 | yes | pass |
| f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | 0.0080 | 0.0143 | -0.0063 [-0.0063, -0.0062] | -43.8 % | 10 | yes | pass |
| f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 1.4646 | 1.6202 | -0.1556 [-0.1694, -0.1456] | -9.6 % | 10 | yes | pass |
| f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | 0.1604 | 0.5156 | -0.3552 [-0.3556, -0.3544] | -68.9 % | 10 | yes | pass |
| f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=cpu | 2.2055 | 3.2180 | -1.0126 [-1.0131, -1.0098] | -31.5 % | 10 | yes | pass |
| f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=hbm | 0.2346 | 0.7462 | -0.5116 [-0.5122, -0.5112] | -68.6 % | 10 | yes | pass |
| footprint-mib=1024,generator=rmat,kernel=k4,placement=cpu | 123.2263 | 67.4324 | 55.6008 [54.9361, 55.9639] | +82.5 % | 10 | yes | pass |
| footprint-mib=1024,generator=rmat,kernel=k4,placement=hbm | 34.7294 | 65.9121 | -31.0269 [-31.2717, -30.5728] | -47.1 % | 10 | yes | pass |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,sharing=shared | 30.7219 | 4.1663 | 26.5550 [26.5367, 26.6021] | +637.4 % | 10 | yes | pass |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,sharing=shared | 1.2805 | 1.7662 | -0.4850 [-0.4908, -0.4829] | -27.5 % | 10 | yes | pass |
| footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu | 30.8239 | 4.1677 | 26.6562 [26.6359, 26.6709] | +639.6 % | 10 | yes | pass |
| footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm | 1.2725 | 1.7690 | -0.4958 [-0.4988, -0.4941] | -28.0 % | 10 | yes | pass |
| footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,state=clean,working-set-mib=8 | 0.0441 | 0.0619 | -0.0179 [-0.0181, -0.0172] | -28.9 % | 20 | yes | pass |
| footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,state=dirty,working-set-mib=8 | 0.0662 | 0.0826 | -0.0165 [-0.0170, -0.0161] | -19.9 % | 10 | yes | pass |
| footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,state=evicted,working-set-mib=8 | 0.0437 | 0.0608 | -0.0171 [-0.0175, -0.0170] | -28.2 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.01,working-set-mib=32 | 1.5126 | 0.2021 | 1.3101 [1.3089, 1.3121] | +648.4 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.01,working-set-mib=8 | 0.0447 | 0.1493 | -0.1047 [-0.1056, -0.1040] | -70.1 % | 30 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.1,working-set-mib=32 | 1.5080 | 0.6788 | 0.8291 [0.8281, 0.8300] | +122.1 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.1,working-set-mib=8 | 0.0482 | 0.6217 | -0.5731 [-0.5743, -0.5727] | -92.2 % | 20 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=1,working-set-mib=32 | 1.5192 | 3.1926 | -1.6730 [-1.6747, -1.6712] | -52.4 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=1,working-set-mib=8 | 0.0524 | 3.0931 | -3.0402 [-3.0409, -3.0396] | -98.3 % | 100 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.01,working-set-mib=32 | 1.4995 | 0.3920 | 1.1076 [1.1065, 1.1088] | +282.5 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.01,working-set-mib=8 | 0.0444 | 0.3379 | -0.2936 [-0.2945, -0.2928] | -86.9 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.1,working-set-mib=32 | 1.5021 | 0.7482 | 0.7541 [0.7530, 0.7564] | +100.8 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.1,working-set-mib=8 | 0.0475 | 0.6929 | -0.6456 [-0.6464, -0.6447] | -93.2 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=1,working-set-mib=32 | 1.5225 | 3.2420 | -1.7200 [-1.7214, -1.7163] | -53.1 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=1,working-set-mib=8 | 0.0527 | 3.1806 | -3.1278 [-3.1293, -3.1266] | -98.3 % | 80 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=runs,sharing=shared,w=1,working-set-mib=32 | 1.5095 | 3.1200 | -1.6109 [-1.6130, -1.6090] | -51.6 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=runs,sharing=shared,w=1,working-set-mib=8 | 0.0514 | 3.0622 | -3.0104 [-3.0109, -3.0100] | -98.3 % | 90 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=0.01,working-set-mib=32 | 1.5112 | 0.1920 | 1.3191 [1.3184, 1.3195] | +687.0 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=0.01,working-set-mib=8 | 0.0449 | 0.0629 | -0.0179 [-0.0184, -0.0177] | -28.5 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=0.1,working-set-mib=32 | 1.5140 | 0.1960 | 1.3182 [1.3176, 1.3196] | +672.5 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=0.1,working-set-mib=8 | 0.0502 | 0.0734 | -0.0233 [-0.0236, -0.0227] | -31.8 % | 20 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=1,working-set-mib=32 | 1.5246 | 0.2036 | 1.3207 [1.3186, 1.3244] | +648.7 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=1,working-set-mib=8 | 0.0535 | 0.0764 | -0.0226 [-0.0228, -0.0222] | -29.6 % | 70 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=0.01,working-set-mib=32 | 0.1062 | 0.2194 | -0.1130 [-0.1140, -0.1123] | -51.5 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=0.1,working-set-mib=32 | 0.1139 | 0.2782 | -0.1641 [-0.1653, -0.1629] | -59.0 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=1,working-set-mib=32 | 0.1295 | 0.8691 | -0.7401 [-0.7429, -0.7384] | -85.2 % | 20 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=0.01,working-set-mib=32 | 0.1066 | 0.4148 | -0.3080 [-0.3100, -0.3074] | -74.3 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=0.1,working-set-mib=32 | 0.1157 | 0.7351 | -0.6197 [-0.6208, -0.6178] | -84.3 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=1,working-set-mib=32 | 0.1259 | 3.1202 | -2.9949 [-2.9970, -2.9930] | -96.0 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=runs,sharing=shared,w=1,working-set-mib=32 | 0.1315 | 3.2729 | -3.1418 [-3.1519, -3.1053] | -96.0 % | 70 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,sharing=shared,w=0.01,working-set-mib=32 | 0.1061 | 0.1969 | -0.0909 [-0.0923, -0.0884] | -46.1 % | 40 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,sharing=shared,w=0.1,working-set-mib=32 | 0.1145 | 0.1998 | -0.0854 [-0.0866, -0.0846] | -42.7 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,sharing=shared,w=1,working-set-mib=32 | 0.1281 | 0.2230 | -0.0951 [-0.0959, -0.0945] | -42.6 % | 20 | yes | pass |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.01 | 5.4348 | 0.5978 | 4.8360 [4.8211, 4.8382] | +808.9 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.1 | 5.4383 | 0.9982 | 4.4423 [4.4369, 4.4544] | +445.0 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=1 | 5.4361 | 3.7335 | 1.7007 [1.6855, 1.7303] | +45.6 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.01 | 5.4362 | 0.7939 | 4.6425 [4.6414, 4.6444] | +584.8 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.1 | 5.4346 | 1.1403 | 4.2939 [4.2788, 4.2956] | +376.6 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=1 | 5.4280 | 3.7021 | 1.7226 [1.7085, 1.7404] | +46.5 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=runs,sharing=shared,w=1 | 5.3809 | 3.5699 | 1.8109 [1.8037, 1.8138] | +50.7 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=0.01 | 5.4362 | 3.4679 | 1.9686 [1.9665, 1.9699] | +56.8 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=0.1 | 5.4356 | 3.5122 | 1.9218 [1.9085, 1.9239] | +54.7 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=1 | 5.4280 | 3.6193 | 1.8082 [1.8002, 1.8130] | +50.0 % | 10 | yes | pass |
| footprint-mib=1024,k=1,kernel=k2,placement=cpu,working-set-mib=1024 | 2.9640 | 3.3180 | -0.3549 [-0.3570, -0.3523] | -10.7 % | 10 | yes | pass |
| footprint-mib=1024,k=1,kernel=k2,placement=cpu,working-set-mib=32 | 0.1013 | 0.1295 | -0.0282 [-0.0288, -0.0277] | -21.8 % | 10 | yes | pass |
| footprint-mib=1024,k=1,kernel=k2,placement=hbm,working-set-mib=1024 | 0.3347 | 2.8899 | -2.5551 [-2.5569, -2.5519] | -88.4 % | 10 | yes | pass |
| footprint-mib=1024,k=1,kernel=k2,placement=hbm,working-set-mib=32 | 0.0174 | 0.1181 | -0.1007 [-0.1009, -0.1005] | -85.3 % | 20 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,rotated=1,working-set-mib=8 | 0.3761 | 0.0763 | 0.2998 [0.2994, 0.3001] | +393.0 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,scope=sys,working-set-mib=8 | 0.4088 | 0.0845 | 0.3244 [0.3237, 0.3251] | +384.0 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,tiling=tiles,working-set-mib=8 | 0.0368 | 0.0613 | -0.0244 [-0.0246, -0.0242] | -39.9 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=1024 | 47.0181 | 8.1463 | 38.8702 [38.8536, 38.8809] | +477.2 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=32 | 1.5029 | 0.1902 | 1.3126 [1.3122, 1.3131] | +690.2 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=8 | 0.0378 | 0.0613 | -0.0236 [-0.0237, -0.0233] | -38.4 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,rotated=1,working-set-mib=8 | 0.0303 | 0.0751 | -0.0448 [-0.0449, -0.0447] | -59.6 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,scope=sys,working-set-mib=8 | 0.0382 | 0.0829 | -0.0447 [-0.0447, -0.0446] | -53.9 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,tiling=tiles,working-set-mib=8 | 0.0153 | 0.0582 | -0.0430 [-0.0434, -0.0427] | -73.8 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=1024 | 5.1601 | 5.8093 | -0.6488 [-0.6534, -0.6403] | -11.2 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=32 | 0.0999 | 0.1804 | -0.0805 [-0.0810, -0.0800] | -44.6 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=8 | 0.0161 | 0.0589 | -0.0428 [-0.0429, -0.0427] | -72.7 % | 10 | yes | pass |
| footprint-mib=1024,k=2,kernel=k2,placement=cpu,working-set-mib=1024 | 5.9001 | 3.6220 | 2.2775 [2.2728, 2.2828] | +62.9 % | 10 | yes | pass |
| footprint-mib=1024,k=2,kernel=k2,placement=cpu,working-set-mib=32 | 0.1930 | 0.1352 | 0.0579 [0.0577, 0.0582] | +42.8 % | 10 | yes | pass |
| footprint-mib=1024,k=2,kernel=k2,placement=hbm,working-set-mib=1024 | 0.6594 | 3.2110 | -2.5517 [-2.5540, -2.5505] | -79.5 % | 10 | yes | pass |
| footprint-mib=1024,k=2,kernel=k2,placement=hbm,working-set-mib=32 | 0.0234 | 0.1228 | -0.0995 [-0.0997, -0.0991] | -81.0 % | 10 | yes | pass |
| footprint-mib=1024,k=4,kernel=k2,placement=cpu,working-set-mib=1024 | 11.7382 | 4.2740 | 7.4638 [7.4579, 7.4680] | +174.6 % | 10 | yes | pass |
| footprint-mib=1024,k=4,kernel=k2,placement=cpu,working-set-mib=32 | 0.3809 | 0.1410 | 0.2398 [0.2396, 0.2401] | +170.0 % | 10 | yes | pass |
| footprint-mib=1024,k=4,kernel=k2,placement=hbm,working-set-mib=1024 | 1.3027 | 3.8529 | -2.5507 [-2.5544, -2.5492] | -66.2 % | 10 | yes | pass |
| footprint-mib=1024,k=4,kernel=k2,placement=hbm,working-set-mib=32 | 0.0347 | 0.1332 | -0.0986 [-0.0989, -0.0976] | -74.0 % | 10 | yes | pass |
| footprint-mib=1024,k=64,kernel=k2,placement=cpu,working-set-mib=1024 | 187.1472 | 23.5646 | 163.5919 [163.5754, 163.6072] | +694.2 % | 10 | yes | pass |
| footprint-mib=1024,k=64,kernel=k2,placement=cpu,working-set-mib=32 | 5.9591 | 0.3820 | 5.5775 [5.5709, 5.5847] | +1460.0 % | 10 | yes | pass |
| footprint-mib=1024,k=64,kernel=k2,placement=hbm,working-set-mib=1024 | 20.5925 | 23.1501 | -2.5626 [-2.5832, -2.5372] | -11.1 % | 10 | yes | pass |
| footprint-mib=1024,k=64,kernel=k2,placement=hbm,working-set-mib=32 | 0.3414 | 0.3731 | -0.0317 [-0.0324, -0.0312] | -8.5 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k3,placement=cpu | 5.3702 | 3.4551 | 1.9160 [1.9131, 1.9169] | +55.5 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k3,placement=hbm | 0.4652 | 1.1155 | -0.6503 [-0.6522, -0.6499] | -58.3 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k6,layout=line,placement=cpu,update=atomic | 3.4572 | 6.9125 | -3.4561 [-3.4604, -3.4464] | -50.0 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k6,layout=line,placement=hbm,update=atomic | 0.3396 | 1.6018 | -1.2622 [-1.2649, -1.2602] | -78.8 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=cpu,update=atomic | 6.0337 | 7.3580 | -1.3268 [-1.3339, -1.3170] | -18.0 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=cpu,update=plain | 6.0631 | 7.3385 | -1.2759 [-1.2822, -1.2722] | -17.4 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=cpu,update=returned | 6.1181 | 7.4524 | -1.3332 [-1.3430, -1.3259] | -17.9 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=hbm,update=atomic | 0.8174 | 2.0975 | -1.2804 [-1.2813, -1.2788] | -61.0 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=hbm,update=plain | 0.7686 | 2.0383 | -1.2698 [-1.2709, -1.2676] | -62.3 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=hbm,update=returned | 0.8981 | 2.1695 | -1.2714 [-1.2726, -1.2707] | -58.6 % | 10 | yes | pass |
| footprint-mib=11520,kernel=k3,placement=cpu | 240.0888 | 32.4886 | 207.5970 [207.5611, 207.6986] | +639.0 % | 10 | yes | pass |
| footprint-mib=1536,kernel=k3,placement=cpu | 5.3707 | 4.8344 | 0.5363 [0.5329, 0.5373] | +11.1 % | 10 | yes | pass |
| footprint-mib=16,kernel=k6,placement=cpu,update=atomic | 1.5094 | 0.2059 | 1.3033 [1.3025, 1.3046] | +632.9 % | 10 | yes | pass |
| footprint-mib=16,kernel=k6,placement=hbm,update=atomic | 0.0770 | 0.1941 | -0.1171 [-0.1178, -0.1170] | -60.3 % | 10 | yes | pass |
| footprint-mib=16384,generator=uniform,kernel=k4,placement=cpu | 483.2695 | 47.9533 | 435.3191 [435.2627, 435.3541] | +907.8 % | 10 | yes | pass |
| footprint-mib=16384,generator=uniform,kernel=k4,placement=hbm | 32.2353 | 42.3584 | -10.1286 [-10.1548, -10.0975] | -23.9 % | 10 | yes | pass |
| footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,sharing=shared,state=dirty | 7.2207 | 45.0645 | -37.8423 [-37.8687, -37.8358] | -84.0 % | 10 | yes | pass |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.01 | 433.5660 | 2.0077 | 431.5594 [431.3762, 431.6727] | +21494.8 % | 10 | yes | pass |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.1 | 433.5287 | 5.1577 | 428.3697 [428.3251, 428.5340] | +8305.4 % | 10 | yes | pass |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=1 | 432.9635 | 45.8060 | 387.1577 [386.9188, 387.6095] | +845.2 % | 10 | yes | pass |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.01 | 433.5031 | 5.2565 | 428.2626 [428.1834, 428.3139] | +8147.3 % | 40 | yes | pass |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.1 | 433.4473 | 10.4708 | 422.9765 [422.8276, 423.1408] | +4039.6 % | 10 | yes | pass |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=1 | 432.7667 | 49.6546 | 383.1112 [382.9140, 383.2247] | +771.6 % | 10 | yes | pass |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=runs,sharing=shared,w=1 | 433.3808 | 45.4516 | 387.9388 [387.8589, 388.0427] | +853.5 % | 10 | yes | pass |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=0.01 | 433.4433 | 45.4710 | 387.9742 [387.8685, 388.0842] | +853.2 % | 10 | yes | pass |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=0.1 | 433.3441 | 44.9468 | 388.4042 [388.3334, 388.5176] | +864.1 % | 10 | yes | pass |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=1 | 433.2855 | 45.8353 | 387.4526 [387.3174, 387.5918] | +845.3 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,page-order=2m,placement=cpu | 5.3795 | 46.3313 | -40.9523 [-40.9850, -40.9451] | -88.4 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,page-order=2m,placement=hbm | 2.5222 | 10.6142 | -8.0901 [-8.1381, -8.0677] | -76.2 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,page-order=64k,placement=cpu | 5.2137 | 46.7860 | -41.5734 [-41.5840, -41.5606] | -88.9 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,page-order=64k,placement=hbm | 1.6145 | 10.5822 | -8.9681 [-8.9834, -8.9508] | -84.7 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu | 5.3806 | 42.6245 | -37.2439 [-37.2470, -37.2411] | -87.4 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,page-size=512m,placement=hbm | 0.4783 | 10.6524 | -10.1741 [-10.1905, -10.1605] | -95.5 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,partition=2g,placement=cpu | 5.6906 | 46.6593 | -40.9652 [-40.9849, -40.9053] | -87.8 % | 20 | yes | pass |
| footprint-mib=16384,kernel=k3,partition=2g,placement=hbm | 284.5030 | 10.8414 | 273.6289 [271.3852, 275.2746] | +2523.9 % | 30 | yes | pass |
| footprint-mib=16384,kernel=k3,placement=cpu | 432.7179 | 46.8195 | 385.8804 [385.6977, 386.0570] | +824.2 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,placement=hbm | 425.7907 | 10.7258 | 415.0369 [414.8601, 415.1591] | +3869.5 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3p,page-size=512m,placement=cpu | 0.0931 | 42.1833 | -42.0902 [-42.0955, -42.0868] | -99.8 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3p,placement=cpu | 7.0158 | 45.3267 | -38.3060 [-38.3237, -38.2955] | -84.5 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k6,placement=cpu,update=atomic | 95.7826 | 116.3413 | -20.5839 [-20.6335, -20.4956] | -17.7 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k6,placement=hbm,update=atomic | 13.1014 | 33.5205 | -20.4218 [-20.4510, -20.3522] | -60.9 % | 10 | yes | pass |
| footprint-mib=2048,kernel=k3,placement=cpu | 5.3705 | 6.2088 | -0.8385 [-0.8405, -0.8343] | -13.5 % | 10 | yes | pass |
| footprint-mib=24576,generator=uniform,kernel=k4,placement=cpu | 751.8495 | 73.6668 | 678.2211 [678.0347, 678.4902] | +920.7 % | 10 | yes | pass |
| footprint-mib=24576,kernel=k3,placement=cpu | 597.3971 | 67.6407 | 529.7570 [529.5749, 529.7854] | +783.2 % | 10 | yes | pass |
| footprint-mib=24576,kernel=k3,placement=hbm | 589.9615 | 15.7107 | 574.2555 [574.0326, 574.4864] | +3655.2 % | 10 | yes | pass |
| footprint-mib=256,generator=uniform,kernel=k4,placement=cpu | 7.3817 | 1.0122 | 6.3695 [6.3589, 6.3737] | +629.3 % | 10 | yes | pass |
| footprint-mib=256,generator=uniform,kernel=k4,placement=hbm | 0.2115 | 0.8880 | -0.6766 [-0.6770, -0.6761] | -76.2 % | 10 | yes | pass |
| footprint-mib=256,kernel=k3,placement=cpu | 5.3644 | 1.2025 | 4.1620 [4.1606, 4.1626] | +346.1 % | 10 | yes | pass |
| footprint-mib=256,kernel=k3,placement=hbm | 0.4264 | 1.0806 | -0.6541 [-0.6546, -0.6532] | -60.5 % | 10 | yes | pass |
| footprint-mib=256,kernel=k6,placement=cpu,update=atomic | 1.5126 | 1.8700 | -0.3579 [-0.3601, -0.3569] | -19.1 % | 10 | yes | pass |
| footprint-mib=256,kernel=k6,placement=hbm,update=atomic | 0.2047 | 0.5341 | -0.3294 [-0.3300, -0.3291] | -61.7 % | 10 | yes | pass |
| footprint-mib=32768,generator=uniform,kernel=k4,placement=cpu | 971.4641 | 90.8319 | 880.6329 [880.4077, 880.7094] | +969.5 % | 10 | yes | pass |
| footprint-mib=32768,kernel=k3,placement=cpu | 684.9832 | 86.9406 | 598.0317 [597.9326, 598.1206] | +687.9 % | 10 | yes | pass |
| footprint-mib=32768,kernel=k6,placement=cpu,update=atomic | 190.4033 | 228.8376 | -38.4402 [-38.4657, -38.3293] | -16.8 % | 10 | yes | pass |
| footprint-mib=4096,generator=uniform,kernel=k4,placement=cpu | 123.8257 | 12.4689 | 111.3584 [111.3130, 111.3942] | +893.1 % | 10 | yes | pass |
| footprint-mib=4096,generator=uniform,kernel=k4,placement=hbm | 7.0760 | 9.5815 | -2.5051 [-2.5127, -2.4991] | -26.1 % | 10 | yes | pass |
| footprint-mib=4096,kernel=k3,placement=cpu | 5.5551 | 11.9283 | -6.3708 [-6.4168, -6.3316] | -53.4 % | 10 | yes | pass |
| footprint-mib=4096,kernel=k3,placement=hbm | 5.1222 | 3.0242 | 2.0967 [2.0921, 2.1030] | +69.3 % | 10 | yes | pass |
| footprint-mib=4096,kernel=k6,placement=cpu,update=atomic | 24.1551 | 26.2770 | -2.1188 [-2.1404, -2.1131] | -8.1 % | 10 | yes | pass |
| footprint-mib=4096,kernel=k6,placement=hbm,update=atomic | 3.2724 | 8.3851 | -5.1154 [-5.1253, -5.1000] | -61.0 % | 10 | yes | pass |
| footprint-mib=512,host=reads,kernel=k5,placement=cpu,sharing=shared,sweeps=8,tiling=tiles | 27.0149 | 6.5153 | 20.5028 [20.4829, 20.5111] | +314.7 % | 10 | yes | pass |
| footprint-mib=512,host=reads,kernel=k5,placement=hbm,sharing=shared,sweeps=8,tiling=tiles | 3.2634 | 3.8624 | -0.5998 [-0.6016, -0.5963] | -15.5 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=0.01 | 26.5323 | 5.0853 | 21.4496 [21.4112, 21.4633] | +421.8 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=0.1 | 26.8248 | 5.3036 | 21.5240 [21.4926, 21.5486] | +405.8 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=1 | 26.2720 | 6.7462 | 19.5273 [19.5120, 19.5432] | +289.5 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=0.01 | 26.4258 | 5.2037 | 21.2170 [21.2040, 21.2500] | +407.7 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=0.1 | 26.5873 | 5.3733 | 21.2130 [21.1892, 21.2630] | +394.8 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=1 | 26.4926 | 6.6705 | 19.8192 [19.7924, 19.8555] | +297.1 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=runs,sharing=shared,sweeps=8,tiling=tiles,w=1 | 26.5684 | 6.6975 | 19.8704 [19.8491, 19.9004] | +296.7 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sharing=shared,sweeps=8,tiling=tiles,w=0.01 | 26.8268 | 6.5101 | 20.3161 [20.2964, 20.3397] | +312.1 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sharing=shared,sweeps=8,tiling=tiles,w=0.1 | 26.6174 | 6.5449 | 20.0697 [20.0560, 20.0994] | +306.6 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sharing=shared,sweeps=8,tiling=tiles,w=1 | 26.2973 | 6.7726 | 19.5342 [19.4809, 19.5517] | +288.4 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=0.01 | 3.4618 | 3.6128 | -0.1519 [-0.1555, -0.1451] | -4.2 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=0.1 | 3.4839 | 3.6578 | -0.1733 [-0.1775, -0.1700] | -4.7 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=1 | 3.5818 | 3.9804 | -0.3984 [-0.4055, -0.3941] | -10.0 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=0.01 | 3.6134 | 3.6874 | -0.0747 [-0.0841, -0.0717] | -2.0 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=0.1 | 3.5905 | 3.8615 | -0.2718 [-0.2828, -0.2639] | -7.0 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=1 | 3.6006 | 5.0587 | -1.4606 [-1.4666, -1.4423] | -28.9 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=runs,sharing=shared,sweeps=8,tiling=tiles,w=1 | 3.5425 | 4.8141 | -1.2706 [-1.2778, -1.2608] | -26.4 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sharing=shared,sweeps=8,tiling=tiles,w=0.01 | 3.6174 | 3.8770 | -0.2596 [-0.2714, -0.2558] | -6.7 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sharing=shared,sweeps=8,tiling=tiles,w=0.1 | 3.5817 | 3.8952 | -0.3124 [-0.3220, -0.3102] | -8.0 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sharing=shared,sweeps=8,tiling=tiles,w=1 | 3.5924 | 3.9833 | -0.3921 [-0.3967, -0.3813] | -9.8 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=1,tiling=tiles | 3.6935 | 3.6875 | 0.0061 [0.0053, 0.0065] | +0.2 % | 70 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=16,tiling=tiles | 52.5185 | 9.6880 | 42.8292 [42.7996, 42.8570] | +442.1 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=2,tiling=tiles | 6.8056 | 4.0760 | 2.7298 [2.7277, 2.7371] | +67.0 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=4,tiling=tiles | 13.4699 | 4.8958 | 8.5753 [8.5622, 8.5874] | +175.2 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=64,tiling=tiles | 214.9020 | 29.0811 | 185.8237 [185.7933, 185.9760] | +639.0 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=none | 42.0502 | 6.0109 | 36.0376 [35.9775, 36.1054] | +599.5 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles | 26.2710 | 6.4935 | 19.7778 [19.7465, 19.8139] | +304.6 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=hbm,sweeps=1,tiling=tiles | 0.3959 | 1.0460 | -0.6500 [-0.6521, -0.6497] | -62.1 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=hbm,sweeps=16,tiling=tiles | 6.5301 | 7.0977 | -0.5714 [-0.5752, -0.5555] | -8.1 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=hbm,sweeps=2,tiling=tiles | 0.8091 | 1.4443 | -0.6350 [-0.6357, -0.6338] | -44.0 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=hbm,sweeps=4,tiling=tiles | 1.6371 | 2.2538 | -0.6164 [-0.6202, -0.6148] | -27.3 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=hbm,sweeps=64,tiling=tiles | 26.2656 | 26.4518 | -0.1771 [-0.1970, -0.1617] | -0.7 % | 70 | yes | pass |
| footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=none | 2.7512 | 3.3914 | -0.6425 [-0.6497, -0.6358] | -18.9 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles | 3.2515 | 3.8707 | -0.6194 [-0.6230, -0.6147] | -16.0 % | 10 | yes | pass |
| footprint-mib=64,kernel=k6,placement=cpu,update=atomic | 1.5090 | 0.5914 | 0.9175 [0.9155, 0.9182] | +155.1 % | 10 | yes | pass |
| footprint-mib=64,kernel=k6,placement=hbm,update=atomic | 0.1663 | 0.2567 | -0.0903 [-0.0906, -0.0902] | -35.2 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1,placement=cpu | 191.3116 | 12.3682 | 178.9429 [178.9396, 178.9467] | +1446.8 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1,placement=hbm | 12.2926 | 12.3631 | -0.0710 [-0.0720, -0.0703] | -0.6 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1024,placement=cpu | 12.4758 | 0.8395 | 11.6360 [11.6315, 11.6391] | +1386.0 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1024,placement=hbm | 0.7659 | 0.8335 | -0.0676 [-0.0684, -0.0667] | -8.1 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1048576,placement=cpu | 7.9403 | 0.2487 | 7.6917 [7.6840, 7.7315] | +3093.1 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1048576,placement=hbm | 0.1814 | 0.2439 | -0.0624 [-0.0629, -0.0617] | -25.6 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=16,placement=cpu | 82.2402 | 5.1069 | 77.1336 [77.1282, 77.1351] | +1510.4 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=16,placement=hbm | 5.0302 | 5.0455 | -0.0152 [-0.0155, -0.0147] | -0.3 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=256,placement=cpu | 48.2074 | 2.7614 | 45.4460 [45.4417, 45.4510] | +1645.8 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=256,placement=hbm | 2.6883 | 2.7026 | -0.0145 [-0.0148, -0.0140] | -0.5 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=4096,placement=cpu | 6.2133 | 0.3408 | 5.8725 [5.8667, 5.8888] | +1723.0 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=4096,placement=hbm | 0.2666 | 0.2811 | -0.0145 [-0.0145, -0.0144] | -5.2 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=65536,placement=cpu | 4.2061 | 0.2649 | 3.9414 [3.9407, 3.9425] | +1488.0 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=65536,placement=hbm | 0.1941 | 0.2092 | -0.0151 [-0.0152, -0.0150] | -7.2 % | 10 | yes | pass |
| footprint-mib=8192,generator=rmat,kernel=k4,placement=cpu | 1002.4992 | 414.7581 | 587.7351 [587.0896, 588.4687] | +141.7 % | 10 | yes | pass |
| footprint-mib=8192,generator=rmat,kernel=k4,placement=hbm | 394.9172 | 397.2846 | -2.4337 [-2.4572, -2.2584] | -0.6 % | 10 | yes | pass |
| footprint-mib=8192,generator=uniform,kernel=k4,placement=cpu | 247.7496 | 24.9564 | 222.8045 [222.7346, 222.8998] | +892.8 % | 10 | yes | pass |
| footprint-mib=8192,generator=uniform,kernel=k4,placement=hbm | 15.1516 | 20.2136 | -5.0644 [-5.0821, -5.0414] | -25.1 % | 10 | yes | pass |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=0.01 | 8.1057 | 1.2363 | 6.8685 [6.8661, 6.8750] | +555.6 % | 10 | yes | pass |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=0.1 | 8.1134 | 1.7226 | 6.3922 [6.3847, 6.3970] | +371.1 % | 10 | yes | pass |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=1 | 8.1157 | 5.6467 | 2.4691 [2.4426, 2.4825] | +43.7 % | 10 | yes | pass |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=0.01 | 8.1162 | 2.8550 | 5.2630 [5.2406, 5.2857] | +184.3 % | 20 | yes | pass |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=0.1 | 8.1083 | 5.3876 | 2.7229 [2.7092, 2.7325] | +50.5 % | 10 | yes | pass |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=1 | 8.1172 | 24.4206 | -16.3065 [-16.3113, -16.2964] | -66.8 % | 10 | yes | pass |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=runs,sharing=shared,w=1 | 8.1064 | 20.9428 | -12.8334 [-12.8559, -12.8271] | -61.3 % | 10 | yes | pass |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,sharing=shared,w=0.01 | 8.1123 | 5.6109 | 2.5004 [2.4936, 2.5075] | +44.6 % | 10 | yes | pass |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,sharing=shared,w=0.1 | 8.1043 | 5.6278 | 2.4781 [2.4691, 2.4885] | +44.0 % | 10 | yes | pass |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,sharing=shared,w=1 | 8.1246 | 5.6263 | 2.4988 [2.4830, 2.5065] | +44.4 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu | 7.7466 | 23.4853 | -15.7377 [-15.7542, -15.7329] | -67.0 % | 20 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=hbm | 7.8200 | 5.5757 | 2.2418 [2.2238, 2.2621] | +40.2 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k6,placement=cpu,update=atomic | 48.0932 | 58.7682 | -10.6840 [-10.7199, -10.6444] | -18.2 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k6,placement=hbm,update=atomic | 6.5655 | 16.7425 | -10.1755 [-10.2038, -10.1537] | -60.8 % | 10 | yes | pass |
| footprint-mib=9728,kernel=k3,placement=cpu | 128.4080 | 27.3206 | 101.0837 [100.9906, 101.1339] | +370.0 % | 10 | yes | pass |

## Host phases

The CPU phase before every pass, timed on the CPU clock (ms per pass), and the state check's median load latency on the preparing core after the phase (ns per sampled load), per variant.

| cell | direct CPU ms | direct state ns | copy CPU ms | copy state ns |
|---|---|---|---|---|
| f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,sharing=shared,state=clean | - | - | - | - |
| f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,sharing=shared,state=dirty | - | - | - | - |
| f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,sharing=shared,state=evicted | - | - | - | - |
| f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,sharing=shared,state=clean | - | - | - | - |
| f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,sharing=shared,state=dirty | - | - | - | - |
| f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,sharing=shared,state=evicted | - | - | - | - |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,sharing=shared | - | - | - | - |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,sharing=shared | - | - | - | - |
| footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,state=clean,working-set-mib=8 | - | - | - | - |
| footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,state=dirty,working-set-mib=8 | - | - | - | - |
| footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,state=evicted,working-set-mib=8 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.01,working-set-mib=32 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.01,working-set-mib=8 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.1,working-set-mib=32 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.1,working-set-mib=8 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=1,working-set-mib=32 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=1,working-set-mib=8 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.01,working-set-mib=32 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.01,working-set-mib=8 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.1,working-set-mib=32 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.1,working-set-mib=8 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=1,working-set-mib=32 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=1,working-set-mib=8 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=runs,sharing=shared,w=1,working-set-mib=32 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=runs,sharing=shared,w=1,working-set-mib=8 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=0.01,working-set-mib=32 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=0.01,working-set-mib=8 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=0.1,working-set-mib=32 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=0.1,working-set-mib=8 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=1,working-set-mib=32 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=1,working-set-mib=8 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=0.01,working-set-mib=32 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=0.1,working-set-mib=32 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=1,working-set-mib=32 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=0.01,working-set-mib=32 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=0.1,working-set-mib=32 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=1,working-set-mib=32 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=runs,sharing=shared,w=1,working-set-mib=32 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,sharing=shared,w=0.01,working-set-mib=32 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,sharing=shared,w=0.1,working-set-mib=32 | - | - | - | - |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,sharing=shared,w=1,working-set-mib=32 | - | - | - | - |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.01 | - | - | - | - |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.1 | - | - | - | - |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=1 | - | - | - | - |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.01 | - | - | - | - |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.1 | - | - | - | - |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=1 | - | - | - | - |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=runs,sharing=shared,w=1 | - | - | - | - |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=0.01 | - | - | - | - |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=0.1 | - | - | - | - |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=1 | - | - | - | - |
| footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,sharing=shared,state=dirty | - | - | - | - |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.01 | - | - | - | - |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.1 | - | - | - | - |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=1 | - | - | - | - |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.01 | - | - | - | - |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.1 | - | - | - | - |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=1 | - | - | - | - |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=runs,sharing=shared,w=1 | - | - | - | - |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=0.01 | - | - | - | - |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=0.1 | - | - | - | - |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=1 | - | - | - | - |
| footprint-mib=512,host=reads,kernel=k5,placement=cpu,sharing=shared,sweeps=8,tiling=tiles | - | - | - | - |
| footprint-mib=512,host=reads,kernel=k5,placement=hbm,sharing=shared,sweeps=8,tiling=tiles | - | - | - | - |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=0.01 | - | - | - | - |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=0.1 | - | - | - | - |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=1 | - | - | - | - |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=0.01 | - | - | - | - |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=0.1 | - | - | - | - |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=1 | - | - | - | - |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=runs,sharing=shared,sweeps=8,tiling=tiles,w=1 | - | - | - | - |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sharing=shared,sweeps=8,tiling=tiles,w=0.01 | - | - | - | - |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sharing=shared,sweeps=8,tiling=tiles,w=0.1 | - | - | - | - |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sharing=shared,sweeps=8,tiling=tiles,w=1 | - | - | - | - |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=0.01 | - | - | - | - |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=0.1 | - | - | - | - |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=1 | - | - | - | - |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=0.01 | - | - | - | - |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=0.1 | - | - | - | - |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=1 | - | - | - | - |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=runs,sharing=shared,sweeps=8,tiling=tiles,w=1 | - | - | - | - |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sharing=shared,sweeps=8,tiling=tiles,w=0.01 | - | - | - | - |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sharing=shared,sweeps=8,tiling=tiles,w=0.1 | - | - | - | - |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sharing=shared,sweeps=8,tiling=tiles,w=1 | - | - | - | - |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=0.01 | - | - | - | - |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=0.1 | - | - | - | - |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=1 | - | - | - | - |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=0.01 | - | - | - | - |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=0.1 | - | - | - | - |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=1 | - | - | - | - |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=runs,sharing=shared,w=1 | - | - | - | - |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,sharing=shared,w=0.01 | - | - | - | - |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,sharing=shared,w=0.1 | - | - | - | - |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,sharing=shared,w=1 | - | - | - | - |

## Per cell

### route/alignment=off512m,footprint-mib=8192,kernel=k3,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 39.4 GB/s over the touched lines; buffer at 0x4f1420000000 (offset in its 16 GiB window: 536870912 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 22.9630 ms, kernel 0.4971 ms, copy-out 0.0137 ms; source buffer at 0x4f1820000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (36.2 per touched line), copy 8.607e+09; SMMU translation requests per repetition: direct 1.358e+07, copy 1.311e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 7 passes per interval, 368.5 GB/s over the touched lines; buffer at 0x491f80000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9694 ms, kernel 0.2969 ms, copy-out 0.0141 ms; source buffer at 0x492080000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+09 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 67 passes per interval, 3595.9 GB/s over the touched lines; buffer at 0x5f5f80000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 22 calls per interval; first call of an interval: copy-in 0.8965 ms, kernel 0.0410 ms, copy-out 0.0112 ms; source buffer at 0x5f60c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=cpu

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 376.7 GB/s over the touched lines; buffer at 0x59da80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 46.3964 ms, kernel 0.0822 ms, copy-out 0.0151 ms; source buffer at 0x59df40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.718e+10 (128.0 per touched line), copy 1.718e+10; SMMU translation requests per repetition: direct 2.71e+05, copy 2.622e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=hbm

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 2988.1 GB/s over the touched lines; buffer at 0x46e900000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 14.5229 ms, kernel 0.1263 ms, copy-out 0.0127 ms; source buffer at 0x46ed80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 7.051e+05, copy 4.83e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=19456,kernel=k1,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 376.6 GB/s over the touched lines; buffer at 0x57f680000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 54.0004 ms, kernel 0.0826 ms, copy-out 0.0156 ms; source buffer at 0x57fc00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.04e+10 (128.0 per touched line), copy 2.04e+10; SMMU translation requests per repetition: direct 3.226e+05, copy 3.113e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=23296,kernel=k1,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 375.9 GB/s over the touched lines; buffer at 0x591100000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 61.9206 ms, kernel 0.0845 ms, copy-out 0.0158 ms; source buffer at 0x591740000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.443e+10 (128.0 per touched line), copy 2.443e+10; SMMU translation requests per repetition: direct 3.835e+05, copy 3.728e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 380.0 GB/s over the touched lines; buffer at 0x5fc540000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 67.5284 ms, kernel 0.0829 ms, copy-out 0.0154 ms; source buffer at 0x5fcbc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.577e+10 (128.0 per touched line), copy 2.577e+10; SMMU translation requests per repetition: direct 4.069e+05, copy 3.933e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=hbm

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 2682.2 GB/s over the touched lines; buffer at 0x560400000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 22.6009 ms, kernel 0.0414 ms, copy-out 0.0132 ms; source buffer at 0x560a80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.134e+06, copy 1.031e+06; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 28 passes per interval, 367.3 GB/s over the touched lines; buffer at 0x536d40000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 24 calls per interval; first call of an interval: copy-in 0.7732 ms, kernel 0.0806 ms, copy-out 0.0169 ms; source buffer at 0x536e40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.684e+08 (128.0 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 0, copy 4110; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 255 passes per interval, 3421.0 GB/s over the touched lines; buffer at 0x4cd780000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 28 calls per interval; first call of an interval: copy-in 0.6480 ms, kernel 0.0814 ms, copy-out 0.0112 ms; source buffer at 0x4cd840000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 4110; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=cpu

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 381.8 GB/s over the touched lines; buffer at 0x543f40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 87.0477 ms, kernel 0.0814 ms, copy-out 0.0167 ms; source buffer at 0x5447c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.436e+10 (128.0 per touched line), copy 3.436e+10; SMMU translation requests per repetition: direct 5.45e+05, copy 5.243e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 368.1 GB/s over the touched lines; buffer at 0x5114c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 11.4392 ms, kernel 1.1646 ms, copy-out 0.0154 ms; source buffer at 0x511640000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 4.295e+09 (128.0 per touched line), copy 4.295e+09; SMMU translation requests per repetition: direct 0, copy 6.556e+04; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=hbm

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 18 passes per interval, 3658.9 GB/s over the touched lines; buffer at 0x5519c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 3.6256 ms, kernel 0.0424 ms, copy-out 0.0120 ms; source buffer at 0x551b80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 912.3, copy 3659; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,sharing=shared,state=clean

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 350.0 GB/s over the touched lines; buffer at 0x58e240000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.2157 ms, kernel 0.0269 ms, copy-out 0.0129 ms; source buffer at 0x58e2c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.711e+07 (128.0 per touched line), copy 6.711e+07; SMMU translation requests per repetition: direct 1826, copy 1043; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,sharing=shared,state=dirty

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 201.2 GB/s over the touched lines; buffer at 0x5d3700000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.3324 ms, kernel 0.0270 ms, copy-out 0.0123 ms; source buffer at 0x5d3780000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.711e+07 (128.0 per touched line), copy 6.711e+07; SMMU translation requests per repetition: direct 1449, copy 1072; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,sharing=shared,state=evicted

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 349.2 GB/s over the touched lines; buffer at 0x407640000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.2123 ms, kernel 0.0271 ms, copy-out 0.0116 ms; source buffer at 0x407700000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.711e+07 (128.0 per touched line), copy 6.711e+07; SMMU translation requests per repetition: direct 2057, copy 1043; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,sharing=shared,state=clean

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 420.7 GB/s over the touched lines; buffer at 0x585f00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1795 ms, kernel 0.0236 ms, copy-out 0.0145 ms; source buffer at 0x585f80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1995, copy 1541; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,sharing=shared,state=dirty

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 472.9 GB/s over the touched lines; buffer at 0x4a1fc0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1576 ms, kernel 0.0269 ms, copy-out 0.0139 ms; source buffer at 0x4a2040000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 2253, copy 1887; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,sharing=shared,state=evicted

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 1839.1 GB/s over the touched lines; buffer at 0x4a1300000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.0661 ms, kernel 0.0244 ms, copy-out 0.0135 ms; source buffer at 0x4a13c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 2851, copy 3952; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 370.8 GB/s over the touched lines; buffer at 0x4f3040000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 22.9818 ms, kernel 0.0809 ms, copy-out 0.0146 ms; source buffer at 0x4f32c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.59e+09 (128.0 per touched line), copy 8.59e+09; SMMU translation requests per repetition: direct 2.754e+04, copy 1.311e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=hbm

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 9 passes per interval, 3566.6 GB/s over the touched lines; buffer at 0x5a2e80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 7.5221 ms, kernel 0.0407 ms, copy-out 0.0132 ms; source buffer at 0x5a3140000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 3.827e+04, copy 1.705e+05; multiplexed rows voided: 0

### route/f-den=10,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 67 passes per interval, 357.3 GB/s over the touched lines; buffer at 0x558e80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 56 calls per interval; first call of an interval: copy-in 0.3367 ms, kernel 0.0173 ms, copy-out 0.0126 ms; source buffer at 0x558f80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+08 (128.0 per touched line), copy 1.074e+08; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/f-den=10,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 526 passes per interval, 2819.5 GB/s over the touched lines; buffer at 0x58fa80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 162 calls per interval; first call of an interval: copy-in 0.0743 ms, kernel 0.0457 ms, copy-out 0.0137 ms; source buffer at 0x58fb80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 8 passes per interval, 365.6 GB/s over the touched lines; buffer at 0x46ed40000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9710 ms, kernel 0.2758 ms, copy-out 0.0129 ms; source buffer at 0x46ee00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 9.664e+08 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=hbm

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 73 passes per interval, 3495.4 GB/s over the touched lines; buffer at 0x55eb80000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 23 calls per interval; first call of an interval: copy-in 0.8301 ms, kernel 0.0396 ms, copy-out 0.0120 ms; source buffer at 0x55ecc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/f-den=100,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 527 passes per interval, 282.7 GB/s over the touched lines; buffer at 0x4c30c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 386 calls per interval; first call of an interval: copy-in 0.0409 ms, kernel 0.0078 ms, copy-out 0.0122 ms; source buffer at 0x4c31c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+07 (128.0 per touched line), copy 1.074e+07; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/f-den=100,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1974 passes per interval, 1049.6 GB/s over the touched lines; buffer at 0x5ba200000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 622 calls per interval; first call of an interval: copy-in 0.0155 ms, kernel 0.0081 ms, copy-out 0.0128 ms; source buffer at 0x5ba2c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1266 passes per interval, 67.9 GB/s over the touched lines; buffer at 0x466340000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 1138 calls per interval; first call of an interval: copy-in 0.0159 ms, kernel 0.0073 ms, copy-out 0.0052 ms; source buffer at 0x466400000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+06 (128.0 per touched line), copy 1.074e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 2521 passes per interval, 133.5 GB/s over the touched lines; buffer at 0x411300000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 1394 calls per interval; first call of an interval: copy-in 0.0114 ms, kernel 0.0076 ms, copy-out 0.0044 ms; source buffer at 0x4113c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 366.6 GB/s over the touched lines; buffer at 0x5ae180000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 13 calls per interval; first call of an interval: copy-in 1.5281 ms, kernel 0.0569 ms, copy-out 0.0138 ms; source buffer at 0x5ae280000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (128.0 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 125 passes per interval, 3347.1 GB/s over the touched lines; buffer at 0x56c480000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 39 calls per interval; first call of an interval: copy-in 0.4862 ms, kernel 0.0255 ms, copy-out 0.0112 ms; source buffer at 0x56c580000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 10 passes per interval, 365.1 GB/s over the touched lines; buffer at 0x48af00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9804 ms, kernel 0.2318 ms, copy-out 0.0129 ms; source buffer at 0x48b000000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.053e+08 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=hbm

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 86 passes per interval, 3432.4 GB/s over the touched lines; buffer at 0x5de240000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 27 calls per interval; first call of an interval: copy-in 0.7047 ms, kernel 0.0345 ms, copy-out 0.0121 ms; source buffer at 0x5de300000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=rmat,kernel=k4,placement=cpu

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 8.7 GB/s over the touched lines; buffer at 0x5bdc40000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 2.9919 ms, kernel 64.3166 ms, copy-out 0.1216 ms; source buffer at 0x5bdd80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.137e+09 (373.9 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.688e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=rmat,kernel=k4,placement=hbm

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 30.9 GB/s over the touched lines; buffer at 0x4b5640000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 0.6380 ms, kernel 65.2552 ms, copy-out 0.0179 ms; source buffer at 0x4b5740000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,sharing=shared

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 35.0 GB/s over the touched lines; buffer at 0x5eaa40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 2.9541 ms, kernel 1.1001 ms, copy-out 0.1202 ms; source buffer at 0x5eab80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.201e+09 (381.6 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.689e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,sharing=shared

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 16 passes per interval, 838.6 GB/s over the touched lines; buffer at 0x577f40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 12 calls per interval; first call of an interval: copy-in 0.6477 ms, kernel 1.1129 ms, copy-out 0.0180 ms; source buffer at 0x578000000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 34.8 GB/s over the touched lines; buffer at 0x4d2340000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 2.9511 ms, kernel 1.1058 ms, copy-out 0.1222 ms; source buffer at 0x4d2440000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.196e+09 (380.9 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.689e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 16 passes per interval, 843.8 GB/s over the touched lines; buffer at 0x5e6280000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 12 calls per interval; first call of an interval: copy-in 0.6479 ms, kernel 1.1084 ms, copy-out 0.0188 ms; source buffer at 0x5e63c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,state=clean,working-set-mib=8

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 190.0 GB/s over the touched lines; buffer at 0x572440000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.0443 ms, kernel 0.0162 ms, copy-out 0.0124 ms; source buffer at 0x572500000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 288.6, copy 130.6; multiplexed rows voided: 0

### route/footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,state=dirty,working-set-mib=8

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 126.7 GB/s over the touched lines; buffer at 0x57c180000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.0583 ms, kernel 0.0162 ms, copy-out 0.0139 ms; source buffer at 0x57c2c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 236.8, copy 138.1; multiplexed rows voided: 0

### route/footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,state=evicted,working-set-mib=8

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 192.0 GB/s over the touched lines; buffer at 0x4ab540000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.0469 ms, kernel 0.0162 ms, copy-out 0.0117 ms; source buffer at 0x4ab640000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 321.6, copy 130.9; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.01,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.2 GB/s over the touched lines; buffer at 0x4c1780000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1220 ms, kernel 0.0735 ms, copy-out 0.0174 ms; source buffer at 0x4c1880000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.365e+08 (2047.6 per touched line), copy 1.074e+07; SMMU translation requests per repetition: direct 874.9, copy 2.808e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.01,working-set-mib=8

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 187.7 GB/s over the touched lines; buffer at 0x4c7e40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1240 ms, kernel 0.0174 ms, copy-out 0.0174 ms; source buffer at 0x4c7f40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 1.074e+07; SMMU translation requests per repetition: direct 329.9, copy 2.823e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.1,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.2 GB/s over the touched lines; buffer at 0x43e8c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 34 calls per interval; first call of an interval: copy-in 0.5541 ms, kernel 0.0880 ms, copy-out 0.0175 ms; source buffer at 0x43e9c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.365e+08 (2047.7 per touched line), copy 1.074e+08; SMMU translation requests per repetition: direct 732.8, copy 1.943e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.1,working-set-mib=8

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 173.8 GB/s over the touched lines; buffer at 0x55b080000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 42 calls per interval; first call of an interval: copy-in 0.5557 ms, kernel 0.0190 ms, copy-out 0.0171 ms; source buffer at 0x55b180000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 1.074e+08; SMMU translation requests per repetition: direct 334.8, copy 1.908e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=1,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.1 GB/s over the touched lines; buffer at 0x461640000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 3.0809 ms, kernel 0.0874 ms, copy-out 0.0137 ms; source buffer at 0x461740000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.365e+08 (2047.5 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=1,working-set-mib=8

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 159.9 GB/s over the touched lines; buffer at 0x596b80000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 3.0453 ms, kernel 0.0184 ms, copy-out 0.0144 ms; source buffer at 0x596c40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.01,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.4 GB/s over the touched lines; buffer at 0x541100000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.3059 ms, kernel 0.0729 ms, copy-out 0.0158 ms; source buffer at 0x541200000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.365e+08 (2047.7 per touched line), copy 1.074e+07; SMMU translation requests per repetition: direct 931.3, copy 5.767e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.01,working-set-mib=8

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 188.8 GB/s over the touched lines; buffer at 0x4b2440000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.3077 ms, kernel 0.0174 ms, copy-out 0.0157 ms; source buffer at 0x4b2540000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 1.074e+07; SMMU translation requests per repetition: direct 336.6, copy 5.705e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.1,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.3 GB/s over the touched lines; buffer at 0x4db800000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 28 calls per interval; first call of an interval: copy-in 0.6753 ms, kernel 0.0740 ms, copy-out 0.0150 ms; source buffer at 0x4db8c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.366e+08 (2047.8 per touched line), copy 1.074e+08; SMMU translation requests per repetition: direct 817.2, copy 5.063e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.1,working-set-mib=8

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 176.4 GB/s over the touched lines; buffer at 0x5d8240000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 30 calls per interval; first call of an interval: copy-in 0.6749 ms, kernel 0.0174 ms, copy-out 0.0151 ms; source buffer at 0x5d8340000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 1.074e+08; SMMU translation requests per repetition: direct 329.1, copy 5.059e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=1,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.0 GB/s over the touched lines; buffer at 0x4e9600000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 3.1520 ms, kernel 0.0789 ms, copy-out 0.0162 ms; source buffer at 0x4e9740000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.365e+08 (2047.7 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.639e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=1,working-set-mib=8

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 159.0 GB/s over the touched lines; buffer at 0x5fa540000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 3.1472 ms, kernel 0.0176 ms, copy-out 0.0126 ms; source buffer at 0x5fa600000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 313.8, copy 1.639e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=runs,sharing=shared,w=1,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.2 GB/s over the touched lines; buffer at 0x404d00000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 3.0233 ms, kernel 0.0784 ms, copy-out 0.0160 ms; source buffer at 0x404dc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.366e+08 (2047.8 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.647e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=runs,sharing=shared,w=1,working-set-mib=8

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 163.1 GB/s over the touched lines; buffer at 0x5961c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 3.0239 ms, kernel 0.0177 ms, copy-out 0.0114 ms; source buffer at 0x5962c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 219.4, copy 1.644e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=0.01,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.2 GB/s over the touched lines; buffer at 0x43ea80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1100 ms, kernel 0.0754 ms, copy-out 0.0158 ms; source buffer at 0x43eb80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.365e+08 (2047.6 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 739.4, copy 544.2; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=0.01,working-set-mib=8

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 186.8 GB/s over the touched lines; buffer at 0x499440000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.0438 ms, kernel 0.0163 ms, copy-out 0.0125 ms; source buffer at 0x499500000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 324.1, copy 135.6; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=0.1,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.2 GB/s over the touched lines; buffer at 0x461f80000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1261 ms, kernel 0.0757 ms, copy-out 0.0129 ms; source buffer at 0x462080000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.365e+08 (2047.6 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 799.8, copy 544.2; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=0.1,working-set-mib=8

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 166.8 GB/s over the touched lines; buffer at 0x452b00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.0581 ms, kernel 0.0164 ms, copy-out 0.0138 ms; source buffer at 0x452bc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 322.3, copy 155.1; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=1,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.0 GB/s over the touched lines; buffer at 0x421000000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1282 ms, kernel 0.0756 ms, copy-out 0.0124 ms; source buffer at 0x421100000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.365e+08 (2047.5 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 533.2; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=1,working-set-mib=8

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 156.6 GB/s over the touched lines; buffer at 0x4e9bc0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.0524 ms, kernel 0.0163 ms, copy-out 0.0172 ms; source buffer at 0x4e9c80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 300.2, copy 131.2; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=0.01,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 315.8 GB/s over the touched lines; buffer at 0x407500000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1288 ms, kernel 0.0847 ms, copy-out 0.0144 ms; source buffer at 0x407600000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 951.9, copy 2.912e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=0.1,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 294.4 GB/s over the touched lines; buffer at 0x5a5d80000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1930 ms, kernel 0.0860 ms, copy-out 0.0148 ms; source buffer at 0x5a5e40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 951.4, copy 3.92e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=1,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 258.9 GB/s over the touched lines; buffer at 0x531c00000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 24 calls per interval; first call of an interval: copy-in 0.7830 ms, kernel 0.0852 ms, copy-out 0.0182 ms; source buffer at 0x531cc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 949.1, copy 4.044e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=0.01,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 314.6 GB/s over the touched lines; buffer at 0x4affc0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 49 calls per interval; first call of an interval: copy-in 0.3446 ms, kernel 0.0884 ms, copy-out 0.0168 ms; source buffer at 0x4b0100000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 946, copy 5.852e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=0.1,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 290.0 GB/s over the touched lines; buffer at 0x4ccc80000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 28 calls per interval; first call of an interval: copy-in 0.6613 ms, kernel 0.0931 ms, copy-out 0.0125 ms; source buffer at 0x4ccd40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 954.6, copy 4.818e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=1,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 266.5 GB/s over the touched lines; buffer at 0x4e80c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 3.0208 ms, kernel 0.1057 ms, copy-out 0.0176 ms; source buffer at 0x4e81c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 955.2, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=runs,sharing=shared,w=1,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 255.1 GB/s over the touched lines; buffer at 0x50ff00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 8 calls per interval; first call of an interval: copy-in 2.5622 ms, kernel 0.1058 ms, copy-out 0.0169 ms; source buffer at 0x510000000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 956.7, copy 1.641e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,sharing=shared,w=0.01,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 316.2 GB/s over the touched lines; buffer at 0x4c8900000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1033 ms, kernel 0.0868 ms, copy-out 0.0123 ms; source buffer at 0x4c8a00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 949.4, copy 547.6; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,sharing=shared,w=0.1,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 292.8 GB/s over the touched lines; buffer at 0x414ac0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1074 ms, kernel 0.0937 ms, copy-out 0.0172 ms; source buffer at 0x414b80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 948.7, copy 547.3; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,sharing=shared,w=1,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 261.9 GB/s over the touched lines; buffer at 0x5c7600000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1168 ms, kernel 0.1068 ms, copy-out 0.0153 ms; source buffer at 0x5c7700000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 949.8, copy 547.9; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.01

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 170.8 GB/s over the touched lines; buffer at 0x5ed000000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 34 calls per interval; first call of an interval: copy-in 0.1253 ms, kernel 0.4711 ms, copy-out 0.0160 ms; source buffer at 0x5ed100000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+07; SMMU translation requests per repetition: direct 1.734e+04, copy 2.5e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.1

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 170.7 GB/s over the touched lines; buffer at 0x46e380000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 21 calls per interval; first call of an interval: copy-in 0.5069 ms, kernel 0.4775 ms, copy-out 0.0171 ms; source buffer at 0x46e480000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+08; SMMU translation requests per repetition: direct 1.312e+04, copy 2.351e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=1

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 170.8 GB/s over the touched lines; buffer at 0x4f4a00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 3.2469 ms, kernel 0.4771 ms, copy-out 0.0187 ms; source buffer at 0x4f4ac0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 1.089e+04, copy 1.189e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.01

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 170.8 GB/s over the touched lines; buffer at 0x4afa40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 26 calls per interval; first call of an interval: copy-in 0.3152 ms, kernel 0.4705 ms, copy-out 0.0132 ms; source buffer at 0x4afb40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+07; SMMU translation requests per repetition: direct 1.74e+04, copy 5.813e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.1

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 170.8 GB/s over the touched lines; buffer at 0x4fd540000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 18 calls per interval; first call of an interval: copy-in 0.6668 ms, kernel 0.4709 ms, copy-out 0.0143 ms; source buffer at 0x4fd640000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+08; SMMU translation requests per repetition: direct 1.742e+04, copy 5.086e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=1

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 171.0 GB/s over the touched lines; buffer at 0x415080000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 3.2137 ms, kernel 0.4794 ms, copy-out 0.0139 ms; source buffer at 0x415180000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 1.301e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=runs,sharing=shared,w=1

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 172.5 GB/s over the touched lines; buffer at 0x5d1c00000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 3.0828 ms, kernel 0.4795 ms, copy-out 0.0153 ms; source buffer at 0x5d1d00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.649e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=0.01

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 170.8 GB/s over the touched lines; buffer at 0x477080000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 2.9850 ms, kernel 0.4723 ms, copy-out 0.0160 ms; source buffer at 0x477140000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 1.741e+04, copy 1.641e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=0.1

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 170.8 GB/s over the touched lines; buffer at 0x49e440000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 3.0336 ms, kernel 0.4732 ms, copy-out 0.0156 ms; source buffer at 0x49e500000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 1.739e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=1

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 171.0 GB/s over the touched lines; buffer at 0x5e08c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 3.1316 ms, kernel 0.4808 ms, copy-out 0.0158 ms; source buffer at 0x5e09c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 1.307e+04, copy 1.651e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=1,kernel=k2,placement=cpu,working-set-mib=1024

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 7 passes per interval, 362.3 GB/s over the touched lines; buffer at 0x5d6940000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9774 ms, kernel 0.3334 ms, copy-out 0.0147 ms; source buffer at 0x5d6a40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+09 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=1,kernel=k2,placement=cpu,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 198 passes per interval, 331.1 GB/s over the touched lines; buffer at 0x46a580000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 156 calls per interval; first call of an interval: copy-in 0.1061 ms, kernel 0.0149 ms, copy-out 0.0099 ms; source buffer at 0x46a640000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.354e+07 (128.0 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 532.9; multiplexed rows voided: 0

### route/footprint-mib=1024,k=1,kernel=k2,placement=hbm,working-set-mib=1024

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 60 passes per interval, 3207.7 GB/s over the touched lines; buffer at 0x5eae40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.5443 ms, kernel 0.3388 ms, copy-out 0.0150 ms; source buffer at 0x5eaf40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=1,kernel=k2,placement=hbm,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1151 passes per interval, 1929.5 GB/s over the touched lines; buffer at 0x502dc0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 171 calls per interval; first call of an interval: copy-in 0.0960 ms, kernel 0.0220 ms, copy-out 0.0124 ms; source buffer at 0x502ec0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 521.3; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,rotated=1,working-set-mib=8

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 54 passes per interval, 22.3 GB/s over the touched lines; buffer at 0x5724c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 267 calls per interval; first call of an interval: copy-in 0.0387 ms, kernel 0.0301 ms, copy-out 0.0106 ms; source buffer at 0x5725c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.341e+08 (2048.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 0, copy 132.6; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,scope=sys,working-set-mib=8

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 20.5 GB/s over the touched lines; buffer at 0x5b9b40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 238 calls per interval; first call of an interval: copy-in 0.0406 ms, kernel 0.0383 ms, copy-out 0.0116 ms; source buffer at 0x5b9c40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.341e+08 (2048.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 0, copy 132.6; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,tiling=tiles,working-set-mib=8

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 544 passes per interval, 227.5 GB/s over the touched lines; buffer at 0x4aaa40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 328 calls per interval; first call of an interval: copy-in 0.0403 ms, kernel 0.0155 ms, copy-out 0.0112 ms; source buffer at 0x4aab40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.38e+06 (128.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 0, copy 132.6; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=1024

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 22.8 GB/s over the touched lines; buffer at 0x4383c0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 2.9738 ms, kernel 5.1589 ms, copy-out 0.0136 ms; source buffer at 0x4384c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.718e+10 (2048.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.639e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.3 GB/s over the touched lines; buffer at 0x4e70c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 106 calls per interval; first call of an interval: copy-in 0.1107 ms, kernel 0.0758 ms, copy-out 0.0129 ms; source buffer at 0x4e7180000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.365e+08 (2047.4 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 532.9; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=8

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 530 passes per interval, 221.8 GB/s over the touched lines; buffer at 0x4eb5c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 328 calls per interval; first call of an interval: copy-in 0.0403 ms, kernel 0.0163 ms, copy-out 0.0150 ms; source buffer at 0x4eb680000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 0, copy 132.6; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,rotated=1,working-set-mib=8

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 660 passes per interval, 276.2 GB/s over the touched lines; buffer at 0x56acc0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 268 calls per interval; first call of an interval: copy-in 0.0353 ms, kernel 0.0341 ms, copy-out 0.0151 ms; source buffer at 0x56adc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 133.9; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,scope=sys,working-set-mib=8

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 525 passes per interval, 219.4 GB/s over the touched lines; buffer at 0x4b10c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 242 calls per interval; first call of an interval: copy-in 0.0362 ms, kernel 0.0436 ms, copy-out 0.0152 ms; source buffer at 0x4b11c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 133.9; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,tiling=tiles,working-set-mib=8

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1311 passes per interval, 549.0 GB/s over the touched lines; buffer at 0x5e4140000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 348 calls per interval; first call of an interval: copy-in 0.0367 ms, kernel 0.0202 ms, copy-out 0.0139 ms; source buffer at 0x5e4240000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 134.6; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=1024

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 208.1 GB/s over the touched lines; buffer at 0x5f1d00000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 0.6358 ms, kernel 5.1663 ms, copy-out 0.0108 ms; source buffer at 0x5f1e00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 201 passes per interval, 335.7 GB/s over the touched lines; buffer at 0x407ac0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 112 calls per interval; first call of an interval: copy-in 0.0944 ms, kernel 0.0816 ms, copy-out 0.0133 ms; source buffer at 0x407bc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 517.7; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=8

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1242 passes per interval, 519.9 GB/s over the touched lines; buffer at 0x5127c0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 341 calls per interval; first call of an interval: copy-in 0.0367 ms, kernel 0.0208 ms, copy-out 0.0136 ms; source buffer at 0x5128c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 134.4; multiplexed rows voided: 0

### route/footprint-mib=1024,k=2,kernel=k2,placement=cpu,working-set-mib=1024

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 182.0 GB/s over the touched lines; buffer at 0x49a380000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 2.9565 ms, kernel 0.6576 ms, copy-out 0.0128 ms; source buffer at 0x49a440000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.147e+09 (256.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.639e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=2,kernel=k2,placement=cpu,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 104 passes per interval, 173.8 GB/s over the touched lines; buffer at 0x468300000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 149 calls per interval; first call of an interval: copy-in 0.1119 ms, kernel 0.0190 ms, copy-out 0.0123 ms; source buffer at 0x4683c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.708e+07 (256.0 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 532.9; multiplexed rows voided: 0

### route/footprint-mib=1024,k=2,kernel=k2,placement=hbm,working-set-mib=1024

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 31 passes per interval, 1628.4 GB/s over the touched lines; buffer at 0x4360c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.5438 ms, kernel 0.6614 ms, copy-out 0.0141 ms; source buffer at 0x4361c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=2,kernel=k2,placement=hbm,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 857 passes per interval, 1436.0 GB/s over the touched lines; buffer at 0x5be940000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 165 calls per interval; first call of an interval: copy-in 0.0952 ms, kernel 0.0257 ms, copy-out 0.0096 ms; source buffer at 0x5bea40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 520.2; multiplexed rows voided: 0

### route/footprint-mib=1024,k=4,kernel=k2,placement=cpu,working-set-mib=1024

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 91.5 GB/s over the touched lines; buffer at 0x596e40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 2.9662 ms, kernel 1.2971 ms, copy-out 0.0167 ms; source buffer at 0x596f40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 4.295e+09 (512.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=4,kernel=k2,placement=cpu,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 53 passes per interval, 88.1 GB/s over the touched lines; buffer at 0x5abd00000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 143 calls per interval; first call of an interval: copy-in 0.1070 ms, kernel 0.0271 ms, copy-out 0.0120 ms; source buffer at 0x5abe00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.342e+08 (512.0 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 533; multiplexed rows voided: 0

### route/footprint-mib=1024,k=4,kernel=k2,placement=hbm,working-set-mib=1024

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 16 passes per interval, 824.3 GB/s over the touched lines; buffer at 0x52d980000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 2.5425 ms, kernel 1.3026 ms, copy-out 0.0130 ms; source buffer at 0x52da40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=4,kernel=k2,placement=hbm,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 577 passes per interval, 966.3 GB/s over the touched lines; buffer at 0x560080000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 151 calls per interval; first call of an interval: copy-in 0.0947 ms, kernel 0.0339 ms, copy-out 0.0157 ms; source buffer at 0x560140000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 518.1; multiplexed rows voided: 0

### route/footprint-mib=1024,k=64,kernel=k2,placement=cpu,working-set-mib=1024

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 5.7 GB/s over the touched lines; buffer at 0x47c4c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 2.9645 ms, kernel 20.5816 ms, copy-out 0.0140 ms; source buffer at 0x47c5c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.872e+10 (8192.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.639e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=64,kernel=k2,placement=cpu,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 5.6 GB/s over the touched lines; buffer at 0x537fc0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 53 calls per interval; first call of an interval: copy-in 0.1067 ms, kernel 0.2694 ms, copy-out 0.0144 ms; source buffer at 0x538080000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.145e+09 (8187.1 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 532.9; multiplexed rows voided: 0

### route/footprint-mib=1024,k=64,kernel=k2,placement=hbm,working-set-mib=1024

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 52.1 GB/s over the touched lines; buffer at 0x5712c0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 2.5432 ms, kernel 20.5924 ms, copy-out 0.0151 ms; source buffer at 0x5713c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=64,kernel=k2,placement=hbm,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 63 passes per interval, 98.2 GB/s over the touched lines; buffer at 0x550940000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 54 calls per interval; first call of an interval: copy-in 0.0949 ms, kernel 0.2766 ms, copy-out 0.0111 ms; source buffer at 0x550a40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 518.4; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k3,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 172.9 GB/s over the touched lines; buffer at 0x48c140000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 2.9821 ms, kernel 0.4678 ms, copy-out 0.0163 ms; source buffer at 0x48c240000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.641e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k3,placement=hbm

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 44 passes per interval, 1995.7 GB/s over the touched lines; buffer at 0x59ac80000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 18 calls per interval; first call of an interval: copy-in 0.6349 ms, kernel 0.4744 ms, copy-out 0.0140 ms; source buffer at 0x59ad80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,layout=line,placement=cpu,update=atomic

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 310.6 GB/s over the touched lines; buffer at 0x4220c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 2.9879 ms, kernel 0.3198 ms, copy-out 3.6153 ms; source buffer at 0x422180000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 2901, copy 3.278e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,layout=line,placement=hbm,update=atomic

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 59 passes per interval, 3161.8 GB/s over the touched lines; buffer at 0x4a9400000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 13 calls per interval; first call of an interval: copy-in 0.7241 ms, kernel 0.3224 ms, copy-out 0.6378 ms; source buffer at 0x4a9500000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 420.7, copy 2816; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=cpu,update=atomic

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 178.0 GB/s over the touched lines; buffer at 0x464c80000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 2.9481 ms, kernel 0.8085 ms, copy-out 3.6144 ms; source buffer at 0x464d80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 4191, copy 3.278e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=cpu,update=plain

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 177.1 GB/s over the touched lines; buffer at 0x4d2fc0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 2.9763 ms, kernel 0.7592 ms, copy-out 3.6152 ms; source buffer at 0x4d30c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+09 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 4519, copy 3.278e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=cpu,update=returned

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 175.5 GB/s over the touched lines; buffer at 0x443680000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 2.9622 ms, kernel 0.8862 ms, copy-out 3.6156 ms; source buffer at 0x443740000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+09 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 4515, copy 3.278e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=hbm,update=atomic

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 25 passes per interval, 1313.5 GB/s over the touched lines; buffer at 0x58b4c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 10 calls per interval; first call of an interval: copy-in 0.7121 ms, kernel 0.8169 ms, copy-out 0.6392 ms; source buffer at 0x58b5c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1360, copy 3686; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=hbm,update=plain

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 27 passes per interval, 1397.0 GB/s over the touched lines; buffer at 0x5bd200000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 10 calls per interval; first call of an interval: copy-in 0.7155 ms, kernel 0.7576 ms, copy-out 0.6388 ms; source buffer at 0x5bd300000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 2739, copy 3664; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=hbm,update=returned

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 23 passes per interval, 1195.6 GB/s over the touched lines; buffer at 0x4aed40000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 10 calls per interval; first call of an interval: copy-in 0.7169 ms, kernel 0.8873 ms, copy-out 0.6382 ms; source buffer at 0x4aee00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 2980, copy 3674; multiplexed rows voided: 0

### route/footprint-mib=11520,kernel=k3,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 8.2 GB/s over the touched lines; buffer at 0x441540000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 31.9674 ms, kernel 0.5020 ms, copy-out 0.0146 ms; source buffer at 0x441880000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.9 per touched line), copy 1.211e+10; SMMU translation requests per repetition: direct 6.713e+07, copy 1.843e+05; multiplexed rows voided: 0

### route/footprint-mib=1536,kernel=k3,placement=cpu

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 220.8 GB/s over the touched lines; buffer at 0x497540000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 4.3570 ms, kernel 0.4720 ms, copy-out 0.0124 ms; source buffer at 0x497640000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (57.9 per touched line), copy 1.611e+09; SMMU translation requests per repetition: direct 0, copy 2.46e+04; multiplexed rows voided: 0

### route/footprint-mib=16,kernel=k6,placement=cpu,update=atomic

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 11.1 GB/s over the touched lines; buffer at 0x407d80000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 98 calls per interval; first call of an interval: copy-in 0.0638 ms, kernel 0.0800 ms, copy-out 0.0720 ms; source buffer at 0x407e00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 1.678e+07; SMMU translation requests per repetition: direct 0, copy 127.2; multiplexed rows voided: 0

### route/footprint-mib=16,kernel=k6,placement=hbm,update=atomic

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 260 passes per interval, 217.8 GB/s over the touched lines; buffer at 0x4125c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 105 calls per interval; first call of an interval: copy-in 0.0564 ms, kernel 0.0839 ms, copy-out 0.0650 ms; source buffer at 0x4126c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 127.1; multiplexed rows voided: 0

### route/footprint-mib=16384,generator=uniform,kernel=k4,placement=cpu

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 35.5 GB/s over the touched lines; buffer at 0x402ac0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 46.0865 ms, kernel 0.5093 ms, copy-out 1.3520 ms; source buffer at 0x402f80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 4.962e+10 (369.7 per touched line), copy 1.718e+10; SMMU translation requests per repetition: direct 2.764e+05, copy 2.765e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,generator=uniform,kernel=k4,placement=hbm

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 533.0 GB/s over the touched lines; buffer at 0x500e80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 10.1589 ms, kernel 31.9025 ms, copy-out 0.2966 ms; source buffer at 0x501340000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4.677e+05, copy 6.356e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,sharing=shared,state=dirty

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 4.6 GB/s over the touched lines; buffer at 0x411a40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 44.9961 ms, kernel 0.0641 ms, copy-out 0.0163 ms; source buffer at 0x411ec0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.355e+07 (128.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 2.014e+06, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.01

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x485540000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 11 calls per interval; first call of an interval: copy-in 1.5012 ms, kernel 0.4975 ms, copy-out 0.0158 ms; source buffer at 0x485a00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.718e+08; SMMU translation requests per repetition: direct 1.211e+08, copy 4.039e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.1

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x54c840000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 4.6242 ms, kernel 0.4989 ms, copy-out 0.0160 ms; source buffer at 0x54cd00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.718e+09; SMMU translation requests per repetition: direct 1.211e+08, copy 2.942e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=1

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x47ef00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 45.2914 ms, kernel 0.4986 ms, copy-out 0.0145 ms; source buffer at 0x47f3c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.718e+10; SMMU translation requests per repetition: direct 1.211e+08, copy 3.134e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.01

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x4af8c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 4.6543 ms, kernel 0.4989 ms, copy-out 0.0145 ms; source buffer at 0x4afd40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.718e+08; SMMU translation requests per repetition: direct 1.211e+08, copy 9.975e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.1

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x519680000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 9.9623 ms, kernel 0.4998 ms, copy-out 0.0133 ms; source buffer at 0x519b40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.718e+09; SMMU translation requests per repetition: direct 1.211e+08, copy 7.576e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=1

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x4c8280000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 49.1328 ms, kernel 0.5058 ms, copy-out 0.0129 ms; source buffer at 0x4c8740000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.718e+10; SMMU translation requests per repetition: direct 1.211e+08, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=runs,sharing=shared,w=1

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x503340000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 44.9240 ms, kernel 0.5123 ms, copy-out 0.0150 ms; source buffer at 0x503800000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 1.211e+08, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=0.01

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x5b9900000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 44.9405 ms, kernel 0.5104 ms, copy-out 0.0162 ms; source buffer at 0x5b9dc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 1.211e+08, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=0.1

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x42d140000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 44.4159 ms, kernel 0.5138 ms, copy-out 0.0141 ms; source buffer at 0x42d5c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 1.211e+08, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=1

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x4574c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 45.3010 ms, kernel 0.5166 ms, copy-out 0.0142 ms; source buffer at 0x457940000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 1.211e+08, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-order=2m,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 375.3 GB/s over the touched lines; buffer at 0x59a000000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 45.8482 ms, kernel 0.4665 ms, copy-out 0.0140 ms; source buffer at 0x59a4c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.368e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 6.295e+05, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-order=2m,placement=hbm

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 8 passes per interval, 800.4 GB/s over the touched lines; buffer at 0x4a9b40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 10.1179 ms, kernel 0.4649 ms, copy-out 0.0132 ms; source buffer at 0x4a9fc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 5.716e+05, copy 6.555e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-order=64k,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 387.2 GB/s over the touched lines; buffer at 0x53b800000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 46.3118 ms, kernel 0.4559 ms, copy-out 0.0162 ms; source buffer at 0x53bc80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.386e+08 (34.1 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 2.789e+05, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-order=64k,placement=hbm

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 13 passes per interval, 1250.5 GB/s over the touched lines; buffer at 0x535100000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 10.1207 ms, kernel 0.4529 ms, copy-out 0.0130 ms; source buffer at 0x535580000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 3.982e+05, copy 6.587e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 375.2 GB/s over the touched lines; buffer at 0x50f240000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 42.1172 ms, kernel 0.4908 ms, copy-out 0.0141 ms; source buffer at 0x50f6c0000000
- AnonHugePages after population (kB): direct 16777216, copy 16777216; after the series: direct 16777216, copy 16777216
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 0, copy 532; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-size=512m,placement=hbm

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 42 passes per interval, 4221.3 GB/s over the touched lines; buffer at 0x519d00000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 10.1627 ms, kernel 0.4886 ms, copy-out 0.0140 ms; source buffer at 0x51a1c0000000
- AnonHugePages after population (kB): direct 16777216, copy 16777216; after the series: direct 16777216, copy 16777216
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,partition=2g,placement=cpu

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 354.8 GB/s over the touched lines; buffer at 0x48b700000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 45.9672 ms, kernel 0.6769 ms, copy-out 0.0132 ms; source buffer at 0x48bbc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 3.076e+05, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,partition=2g,placement=hbm

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 7.1 GB/s over the touched lines; buffer at 0x5df500000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 10.1478 ms, kernel 0.6701 ms, copy-out 0.0151 ms; source buffer at 0x5df980000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 8.049e+07, copy 6.528e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x4007c0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 46.2996 ms, kernel 0.5045 ms, copy-out 0.0148 ms; source buffer at 0x400c80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 1.211e+08, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=hbm

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x45c680000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 10.2353 ms, kernel 0.4985 ms, copy-out 0.0118 ms; source buffer at 0x45cb40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.207e+08, copy 6.58e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3p,page-size=512m,placement=cpu

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 215 passes per interval, 360.3 GB/s over the touched lines; buffer at 0x4199c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 42.1190 ms, kernel 0.0521 ms, copy-out 0.0102 ms; source buffer at 0x419e40000000
- AnonHugePages after population (kB): direct 16777216, copy 16777216; after the series: direct 16777216, copy 16777216
- link read bytes per repetition: direct 3.355e+07 (128.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 0, copy 531; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3p,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 4.8 GB/s over the touched lines; buffer at 0x577500000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 45.2486 ms, kernel 0.0620 ms, copy-out 0.0147 ms; source buffer at 0x5779c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.355e+07 (128.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 1.957e+06, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k6,placement=cpu,update=atomic

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 179.4 GB/s over the touched lines; buffer at 0x526f40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 45.1034 ms, kernel 13.1862 ms, copy-out 58.0359 ms; source buffer at 0x527400000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 2.797e+05, copy 5.243e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k6,placement=hbm,update=atomic

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 1311.3 GB/s over the touched lines; buffer at 0x433a80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 10.1535 ms, kernel 13.1908 ms, copy-out 10.1432 ms; source buffer at 0x433f00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 5.036e+05, copy 9.371e+05; multiplexed rows voided: 0

### route/footprint-mib=2048,kernel=k3,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 252.7 GB/s over the touched lines; buffer at 0x5fbdc0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 5.7271 ms, kernel 0.4755 ms, copy-out 0.0168 ms; source buffer at 0x5fbf00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (50.6 per touched line), copy 2.147e+09; SMMU translation requests per repetition: direct 0, copy 3.279e+04; multiplexed rows voided: 0

### route/footprint-mib=24576,generator=uniform,kernel=k4,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 34.3 GB/s over the touched lines; buffer at 0x41a4c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 71.1252 ms, kernel 0.5116 ms, copy-out 2.0277 ms; source buffer at 0x41ab80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 7.682e+10 (381.6 per touched line), copy 2.577e+10; SMMU translation requests per repetition: direct 5.051e+05, copy 4.145e+05; multiplexed rows voided: 0

### route/footprint-mib=24576,kernel=k3,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 3.4 GB/s over the touched lines; buffer at 0x413b80000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 67.1151 ms, kernel 0.5103 ms, copy-out 0.0145 ms; source buffer at 0x414240000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (33.4 per touched line), copy 2.585e+10; SMMU translation requests per repetition: direct 1.671e+08, copy 3.932e+05; multiplexed rows voided: 0

### route/footprint-mib=24576,kernel=k3,placement=hbm

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 3.5 GB/s over the touched lines; buffer at 0x592580000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 15.1990 ms, kernel 0.5072 ms, copy-out 0.0137 ms; source buffer at 0x592c00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.667e+08, copy 1.217e+06; multiplexed rows voided: 0

### route/footprint-mib=256,generator=uniform,kernel=k4,placement=cpu

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 36.4 GB/s over the touched lines; buffer at 0x45b000000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 20 calls per interval; first call of an interval: copy-in 0.7723 ms, kernel 0.2123 ms, copy-out 0.0379 ms; source buffer at 0x45b0c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 7.679e+08 (366.2 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 0, copy 4228; multiplexed rows voided: 0

### route/footprint-mib=256,generator=uniform,kernel=k4,placement=hbm

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 95 passes per interval, 1269.2 GB/s over the touched lines; buffer at 0x528e40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 23 calls per interval; first call of an interval: copy-in 0.6488 ms, kernel 0.2135 ms, copy-out 0.0378 ms; source buffer at 0x528f00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 4229; multiplexed rows voided: 0

### route/footprint-mib=256,kernel=k3,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 50.0 GB/s over the touched lines; buffer at 0x470600000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 17 calls per interval; first call of an interval: copy-in 0.7707 ms, kernel 0.4282 ms, copy-out 0.0134 ms; source buffer at 0x470700000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.368e+08 (256.0 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 0, copy 4115; multiplexed rows voided: 0

### route/footprint-mib=256,kernel=k3,placement=hbm

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 47 passes per interval, 629.3 GB/s over the touched lines; buffer at 0x42aa80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 19 calls per interval; first call of an interval: copy-in 0.6477 ms, kernel 0.4280 ms, copy-out 0.0131 ms; source buffer at 0x42ab40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 4115; multiplexed rows voided: 0

### route/footprint-mib=256,kernel=k6,placement=cpu,update=atomic

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 177.5 GB/s over the touched lines; buffer at 0x4cc900000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 11 calls per interval; first call of an interval: copy-in 0.7730 ms, kernel 0.1982 ms, copy-out 0.9120 ms; source buffer at 0x4cc9c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 311.9, copy 8198; multiplexed rows voided: 0

### route/footprint-mib=256,kernel=k6,placement=hbm,update=atomic

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 98 passes per interval, 1311.4 GB/s over the touched lines; buffer at 0x5ec1c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 38 calls per interval; first call of an interval: copy-in 0.2060 ms, kernel 0.2042 ms, copy-out 0.1718 ms; source buffer at 0x5ec280000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 114.2, copy 229.2; multiplexed rows voided: 0

### route/footprint-mib=32768,generator=uniform,kernel=k4,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 35.4 GB/s over the touched lines; buffer at 0x49a500000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 87.6107 ms, kernel 0.5172 ms, copy-out 2.7055 ms; source buffer at 0x49ae00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 9.936e+10 (370.2 per touched line), copy 3.436e+10; SMMU translation requests per repetition: direct 7.559e+05, copy 5.527e+05; multiplexed rows voided: 0

### route/footprint-mib=32768,kernel=k3,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 3.0 GB/s over the touched lines; buffer at 0x5ac8c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 86.4093 ms, kernel 0.5161 ms, copy-out 0.0131 ms; source buffer at 0x5ad180000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (33.0 per touched line), copy 3.448e+10; SMMU translation requests per repetition: direct 1.912e+08, copy 5.243e+05; multiplexed rows voided: 0

### route/footprint-mib=32768,kernel=k6,placement=cpu,update=atomic

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 180.5 GB/s over the touched lines; buffer at 0x5fc840000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 86.2266 ms, kernel 26.4336 ms, copy-out 116.1808 ms; source buffer at 0x5fd100000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 3.448e+10; SMMU translation requests per repetition: direct 9.438e+05, copy 1.049e+06; multiplexed rows voided: 0

### route/footprint-mib=4096,generator=uniform,kernel=k4,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 34.7 GB/s over the touched lines; buffer at 0x5b5700000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 11.6886 ms, kernel 0.4458 ms, copy-out 0.3411 ms; source buffer at 0x5b58c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.287e+10 (383.6 per touched line), copy 4.295e+09; SMMU translation requests per repetition: direct 6.874e+04, copy 6.82e+04; multiplexed rows voided: 0

### route/footprint-mib=4096,generator=uniform,kernel=k4,placement=hbm

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 607.0 GB/s over the touched lines; buffer at 0x4d5400000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 2.5445 ms, kernel 6.9725 ms, copy-out 0.0740 ms; source buffer at 0x4d5600000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 3.779e+04, copy 4.972e+04; multiplexed rows voided: 0

### route/footprint-mib=4096,kernel=k3,placement=cpu

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 304.2 GB/s over the touched lines; buffer at 0x588c40000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 11.4389 ms, kernel 0.4816 ms, copy-out 0.0122 ms; source buffer at 0x588dc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (40.7 per touched line), copy 4.295e+09; SMMU translation requests per repetition: direct 0, copy 6.556e+04; multiplexed rows voided: 0

### route/footprint-mib=4096,kernel=k3,placement=hbm

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 330.0 GB/s over the touched lines; buffer at 0x494600000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.5296 ms, kernel 0.4872 ms, copy-out 0.0149 ms; source buffer at 0x494780000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1207, copy 1573; multiplexed rows voided: 0

### route/footprint-mib=4096,kernel=k6,placement=cpu,update=atomic

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 177.8 GB/s over the touched lines; buffer at 0x52c740000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 11.4745 ms, kernel 3.2686 ms, copy-out 11.5269 ms; source buffer at 0x52c8c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 4.295e+09; SMMU translation requests per repetition: direct 6.63e+04, copy 1.325e+05; multiplexed rows voided: 0

### route/footprint-mib=4096,kernel=k6,placement=hbm,update=atomic

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 7 passes per interval, 1312.5 GB/s over the touched lines; buffer at 0x563e80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 2.6047 ms, kernel 3.2804 ms, copy-out 2.5326 ms; source buffer at 0x564040000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.798e+04, copy 4.513e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=reads,kernel=k5,placement=cpu,sharing=shared,sweeps=8,tiling=tiles

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 19.9 GB/s over the touched lines; buffer at 0x5c5300000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.5011 ms, kernel 3.2278 ms, copy-out 1.8129 ms; source buffer at 0x5c5400000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.611e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=reads,kernel=k5,placement=hbm,sharing=shared,sweeps=8,tiling=tiles

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 7 passes per interval, 164.5 GB/s over the touched lines; buffer at 0x40e000000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 0.3429 ms, kernel 3.2142 ms, copy-out 0.3202 ms; source buffer at 0x40e100000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 5483, copy 5977; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=0.01

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.2 GB/s over the touched lines; buffer at 0x5877c0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 0.0714 ms, kernel 3.2065 ms, copy-out 1.8132 ms; source buffer at 0x5878c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+06; SMMU translation requests per repetition: direct 3.618e+04, copy 2.315e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=0.1

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.0 GB/s over the touched lines; buffer at 0x498bc0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 0.2734 ms, kernel 3.2154 ms, copy-out 1.8142 ms; source buffer at 0x498cc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+07; SMMU translation requests per repetition: direct 3.621e+04, copy 2.517e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=1

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.4 GB/s over the touched lines; buffer at 0x422240000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 1.7059 ms, kernel 3.2194 ms, copy-out 1.8152 ms; source buffer at 0x422340000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.619e+04, copy 1.467e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=0.01

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.3 GB/s over the touched lines; buffer at 0x5fcd80000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 0.1682 ms, kernel 3.2252 ms, copy-out 1.8137 ms; source buffer at 0x5fce80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+06; SMMU translation requests per repetition: direct 3.617e+04, copy 3.659e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=0.1

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.2 GB/s over the touched lines; buffer at 0x45d840000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 0.3435 ms, kernel 3.2215 ms, copy-out 1.8150 ms; source buffer at 0x45d940000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+07; SMMU translation requests per repetition: direct 3.615e+04, copy 3.329e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=1

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.3 GB/s over the touched lines; buffer at 0x59b040000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.6447 ms, kernel 3.2235 ms, copy-out 1.8124 ms; source buffer at 0x59b180000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.605e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=runs,sharing=shared,sweeps=8,tiling=tiles,w=1

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.2 GB/s over the touched lines; buffer at 0x43a880000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 1.6470 ms, kernel 3.2377 ms, copy-out 1.8145 ms; source buffer at 0x43a9c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.625e+04, copy 1.651e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sharing=shared,sweeps=8,tiling=tiles,w=0.01

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.0 GB/s over the touched lines; buffer at 0x52df40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.4852 ms, kernel 3.2116 ms, copy-out 1.8137 ms; source buffer at 0x52e080000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.611e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sharing=shared,sweeps=8,tiling=tiles,w=0.1

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.2 GB/s over the touched lines; buffer at 0x54ccc0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.5129 ms, kernel 3.2194 ms, copy-out 1.8159 ms; source buffer at 0x54cdc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.622e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sharing=shared,sweeps=8,tiling=tiles,w=1

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.4 GB/s over the touched lines; buffer at 0x5932c0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 1.7218 ms, kernel 3.2417 ms, copy-out 1.8137 ms; source buffer at 0x5933c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.603e+04, copy 1.662e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=0.01

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 155.1 GB/s over the touched lines; buffer at 0x4d13c0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 0.0743 ms, kernel 3.2219 ms, copy-out 0.3268 ms; source buffer at 0x4d14c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4.513e+04, copy 2.773e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=0.1

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 154.1 GB/s over the touched lines; buffer at 0x50f7c0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 0.1276 ms, kernel 3.2240 ms, copy-out 0.3169 ms; source buffer at 0x50f880000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4.48e+04, copy 2.93e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=1

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 149.9 GB/s over the touched lines; buffer at 0x445f00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 0.4481 ms, kernel 3.2213 ms, copy-out 0.3150 ms; source buffer at 0x446000000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4.138e+04, copy 3.32e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=0.01

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 148.6 GB/s over the touched lines; buffer at 0x53e400000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 0.1721 ms, kernel 3.2100 ms, copy-out 0.3229 ms; source buffer at 0x53e500000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4.148e+04, copy 4.084e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=0.1

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 149.5 GB/s over the touched lines; buffer at 0x460a00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 0.3434 ms, kernel 3.2235 ms, copy-out 0.3163 ms; source buffer at 0x460b00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4.156e+04, copy 3.622e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=1

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 149.1 GB/s over the touched lines; buffer at 0x559e00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.5307 ms, kernel 3.2184 ms, copy-out 0.3157 ms; source buffer at 0x559f00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4.112e+04, copy 2.118e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=runs,sharing=shared,sweeps=8,tiling=tiles,w=1

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 151.6 GB/s over the touched lines; buffer at 0x54d540000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 1.2983 ms, kernel 3.2170 ms, copy-out 0.3161 ms; source buffer at 0x54d640000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 3.847e+04, copy 2.117e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sharing=shared,sweeps=8,tiling=tiles,w=0.01

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 148.4 GB/s over the touched lines; buffer at 0x46f480000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 0.3786 ms, kernel 3.2224 ms, copy-out 0.3203 ms; source buffer at 0x46f5c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4.168e+04, copy 3.626e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sharing=shared,sweeps=8,tiling=tiles,w=0.1

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 149.9 GB/s over the touched lines; buffer at 0x54d300000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 0.3587 ms, kernel 3.2249 ms, copy-out 0.3185 ms; source buffer at 0x54d400000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4.154e+04, copy 3.537e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sharing=shared,sweeps=8,tiling=tiles,w=1

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 149.4 GB/s over the touched lines; buffer at 0x5e1a40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 0.4549 ms, kernel 3.2276 ms, copy-out 0.3152 ms; source buffer at 0x5e1b40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4.124e+04, copy 3.204e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=1,tiling=tiles

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 145.4 GB/s over the touched lines; buffer at 0x4b81c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 1.4784 ms, kernel 0.4137 ms, copy-out 1.8135 ms; source buffer at 0x4b8280000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.028e+08 (191.4 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3699, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=16,tiling=tiles

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 10.2 GB/s over the touched lines; buffer at 0x5a6c40000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 1.4677 ms, kernel 6.4193 ms, copy-out 1.8142 ms; source buffer at 0x5a6dc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.284e+10 (3062.4 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.604e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=2,tiling=tiles

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 78.9 GB/s over the touched lines; buffer at 0x46bfc0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 1.4646 ms, kernel 0.8174 ms, copy-out 1.8123 ms; source buffer at 0x46c0c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.606e+09 (382.8 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 1.203e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=4,tiling=tiles

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 39.9 GB/s over the touched lines; buffer at 0x468380000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 1.4833 ms, kernel 1.6193 ms, copy-out 1.8138 ms; source buffer at 0x468480000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.211e+09 (765.6 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 1.802e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=64,tiling=tiles

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 2.5 GB/s over the touched lines; buffer at 0x560480000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 1.4906 ms, kernel 25.7743 ms, copy-out 1.8129 ms; source buffer at 0x5605c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.138e+10 (12249.7 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.611e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=none

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 12.8 GB/s over the touched lines; buffer at 0x51b800000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.4696 ms, kernel 2.7449 ms, copy-out 1.8155 ms; source buffer at 0x51b900000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.307e+10 (3115.7 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.267e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.4 GB/s over the touched lines; buffer at 0x4134c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.4808 ms, kernel 3.2176 ms, copy-out 1.8129 ms; source buffer at 0x4135c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.624e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=1,tiling=tiles

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 51 passes per interval, 1356.2 GB/s over the touched lines; buffer at 0x459a80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 20 calls per interval; first call of an interval: copy-in 0.3861 ms, kernel 0.4087 ms, copy-out 0.3205 ms; source buffer at 0x459bc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 570.6, copy 1658; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=16,tiling=tiles

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 82.2 GB/s over the touched lines; buffer at 0x47f1c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 0.3814 ms, kernel 6.4372 ms, copy-out 0.3215 ms; source buffer at 0x47f300000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 9625, copy 1.105e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=2,tiling=tiles

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 26 passes per interval, 663.6 GB/s over the touched lines; buffer at 0x486b40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 14 calls per interval; first call of an interval: copy-in 0.3846 ms, kernel 0.8115 ms, copy-out 0.3217 ms; source buffer at 0x486c40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1492, copy 2354; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=4,tiling=tiles

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 13 passes per interval, 327.9 GB/s over the touched lines; buffer at 0x53d900000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 9 calls per interval; first call of an interval: copy-in 0.3896 ms, kernel 1.6159 ms, copy-out 0.3219 ms; source buffer at 0x53da00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 2968, copy 3519; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=64,tiling=tiles

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.4 GB/s over the touched lines; buffer at 0x43b040000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 0.3938 ms, kernel 25.7350 ms, copy-out 0.3215 ms; source buffer at 0x43b140000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 3.843e+04, copy 3.518e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=none

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 8 passes per interval, 195.1 GB/s over the touched lines; buffer at 0x47e4c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 0.3870 ms, kernel 2.7406 ms, copy-out 0.3227 ms; source buffer at 0x47e600000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 9830, copy 5402; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 7 passes per interval, 165.1 GB/s over the touched lines; buffer at 0x4f3fc0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 0.3887 ms, kernel 3.2234 ms, copy-out 0.3218 ms; source buffer at 0x4f4100000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 5981, copy 5468; multiplexed rows voided: 0

### route/footprint-mib=64,kernel=k6,placement=cpu,update=atomic

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 44.5 GB/s over the touched lines; buffer at 0x5f0ec0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 34 calls per interval; first call of an interval: copy-in 0.2120 ms, kernel 0.1568 ms, copy-out 0.2386 ms; source buffer at 0x5f0f40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 6.711e+07; SMMU translation requests per repetition: direct 93.32, copy 2053; multiplexed rows voided: 0

### route/footprint-mib=64,kernel=k6,placement=hbm,update=atomic

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 122 passes per interval, 403.6 GB/s over the touched lines; buffer at 0x567900000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 79 calls per interval; first call of an interval: copy-in 0.0629 ms, kernel 0.1698 ms, copy-out 0.0424 ms; source buffer at 0x5679c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 23.84, copy 37.59; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1,placement=cpu

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x4f9540000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 0.0402 ms, kernel 12.2925 ms, copy-out 0.0404 ms; source buffer at 0x4f9600000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1,placement=hbm

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x409d40000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 0.0367 ms, kernel 12.2936 ms, copy-out 0.0368 ms; source buffer at 0x409dc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1024,placement=cpu

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x553240000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 24 calls per interval; first call of an interval: copy-in 0.0397 ms, kernel 0.7685 ms, copy-out 0.0403 ms; source buffer at 0x5532c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1024,placement=hbm

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 27 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x42b140000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 25 calls per interval; first call of an interval: copy-in 0.0353 ms, kernel 0.7693 ms, copy-out 0.0369 ms; source buffer at 0x42b200000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1048576,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 1.1 GB/s over the touched lines; buffer at 0x45ad80000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 81 calls per interval; first call of an interval: copy-in 0.0401 ms, kernel 0.1809 ms, copy-out 0.0396 ms; source buffer at 0x45ae00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1048576,placement=hbm

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 111 passes per interval, 46.2 GB/s over the touched lines; buffer at 0x471f40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 83 calls per interval; first call of an interval: copy-in 0.0360 ms, kernel 0.1825 ms, copy-out 0.0358 ms; source buffer at 0x471fc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=16,placement=cpu

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x548b40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 0.0402 ms, kernel 5.0315 ms, copy-out 0.0431 ms; source buffer at 0x548c00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=16,placement=hbm

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x575500000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 0.0147 ms, kernel 5.0303 ms, copy-out 0.0077 ms; source buffer at 0x575580000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=256,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x428400000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 8 calls per interval; first call of an interval: copy-in 0.0396 ms, kernel 2.6903 ms, copy-out 0.0407 ms; source buffer at 0x428480000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=256,placement=hbm

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 8 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x5267c0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 8 calls per interval; first call of an interval: copy-in 0.0144 ms, kernel 2.6889 ms, copy-out 0.0082 ms; source buffer at 0x526840000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=4096,placement=cpu

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x449c40000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 59 calls per interval; first call of an interval: copy-in 0.0397 ms, kernel 0.2697 ms, copy-out 0.0378 ms; source buffer at 0x449d00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=4096,placement=hbm

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 76 passes per interval, 0.1 GB/s over the touched lines; buffer at 0x54d480000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 72 calls per interval; first call of an interval: copy-in 0.0138 ms, kernel 0.2682 ms, copy-out 0.0079 ms; source buffer at 0x54d500000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=65536,placement=cpu

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 5 passes per interval, 0.1 GB/s over the touched lines; buffer at 0x54b180000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 76 calls per interval; first call of an interval: copy-in 0.0398 ms, kernel 0.1963 ms, copy-out 0.0377 ms; source buffer at 0x54b200000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=65536,placement=hbm

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 104 passes per interval, 2.7 GB/s over the touched lines; buffer at 0x49b7c0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 97 calls per interval; first call of an interval: copy-in 0.0145 ms, kernel 0.1953 ms, copy-out 0.0079 ms; source buffer at 0x49b840000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8192,generator=rmat,kernel=k4,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 8.6 GB/s over the touched lines; buffer at 0x5e01c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 22.5065 ms, kernel 391.5722 ms, copy-out 0.6767 ms; source buffer at 0x5e0600000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.415e+10 (359.9 per touched line), copy 8.607e+09; SMMU translation requests per repetition: direct 1.551e+05, copy 1.355e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,generator=rmat,kernel=k4,placement=hbm

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 21.8 GB/s over the touched lines; buffer at 0x464ec0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 5.3224 ms, kernel 391.8114 ms, copy-out 0.1477 ms; source buffer at 0x465180000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.764e+05, copy 4.03e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,generator=uniform,kernel=k4,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 34.7 GB/s over the touched lines; buffer at 0x4aeb00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 23.7988 ms, kernel 0.4808 ms, copy-out 0.6770 ms; source buffer at 0x4aedc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.552e+10 (380.3 per touched line), copy 8.59e+09; SMMU translation requests per repetition: direct 1.364e+05, copy 1.386e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,generator=uniform,kernel=k4,placement=hbm

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 566.9 GB/s over the touched lines; buffer at 0x496440000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 5.0915 ms, kernel 14.9694 ms, copy-out 0.1487 ms; source buffer at 0x496700000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.34e+05, copy 3.249e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=0.01

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 234.4 GB/s over the touched lines; buffer at 0x497c40000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 17 calls per interval; first call of an interval: copy-in 0.7684 ms, kernel 0.4903 ms, copy-out 0.0195 ms; source buffer at 0x497ec0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.327e+05, copy 2.063e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=0.1

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 234.2 GB/s over the touched lines; buffer at 0x43db40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 13 calls per interval; first call of an interval: copy-in 1.3532 ms, kernel 0.4886 ms, copy-out 0.0166 ms; source buffer at 0x43ddc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.326e+05, copy 3.14e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=1

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 234.1 GB/s over the touched lines; buffer at 0x524f40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 5.1415 ms, kernel 0.4887 ms, copy-out 0.0179 ms; source buffer at 0x5251c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.329e+05, copy 3.125e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=0.01

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 234.1 GB/s over the touched lines; buffer at 0x42f0c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 8 calls per interval; first call of an interval: copy-in 2.5523 ms, kernel 0.4992 ms, copy-out 0.0153 ms; source buffer at 0x42f380000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.329e+05, copy 5.045e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=0.1

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 234.3 GB/s over the touched lines; buffer at 0x5dad80000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 5.2442 ms, kernel 0.4984 ms, copy-out 0.0141 ms; source buffer at 0x5db040000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.327e+05, copy 3.583e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=1

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 234.1 GB/s over the touched lines; buffer at 0x55c1c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 23.8937 ms, kernel 0.5083 ms, copy-out 0.0161 ms; source buffer at 0x55c440000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.329e+05, copy 1.311e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=runs,sharing=shared,w=1

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 234.4 GB/s over the touched lines; buffer at 0x535b40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 20.4186 ms, kernel 0.5061 ms, copy-out 0.0140 ms; source buffer at 0x535dc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.328e+05, copy 1.323e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,sharing=shared,w=0.01

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 234.2 GB/s over the touched lines; buffer at 0x511c00000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 5.1017 ms, kernel 0.4900 ms, copy-out 0.0172 ms; source buffer at 0x511e80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.328e+05, copy 2.886e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,sharing=shared,w=0.1

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 234.5 GB/s over the touched lines; buffer at 0x4dd940000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 5.1181 ms, kernel 0.4900 ms, copy-out 0.0159 ms; source buffer at 0x4ddbc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.329e+05, copy 2.895e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,sharing=shared,w=1

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 233.9 GB/s over the touched lines; buffer at 0x45f800000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 5.1203 ms, kernel 0.4898 ms, copy-out 0.0184 ms; source buffer at 0x45fa80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.328e+05, copy 2.878e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 245.3 GB/s over the touched lines; buffer at 0x4251c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 22.9704 ms, kernel 0.4973 ms, copy-out 0.0153 ms; source buffer at 0x425480000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (36.2 per touched line), copy 8.607e+09; SMMU translation requests per repetition: direct 4121, copy 1.311e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=hbm

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 243.0 GB/s over the touched lines; buffer at 0x492f80000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 5.0661 ms, kernel 0.4891 ms, copy-out 0.0158 ms; source buffer at 0x493240000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4.427e+04, copy 1.147e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k6,placement=cpu,update=atomic

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 178.6 GB/s over the touched lines; buffer at 0x57e500000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 23.2321 ms, kernel 6.5854 ms, copy-out 28.9575 ms; source buffer at 0x57e7c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.607e+09; SMMU translation requests per repetition: direct 1.316e+05, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k6,placement=hbm,update=atomic

- first variant B, seed 71; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 1308.3 GB/s over the touched lines; buffer at 0x4204c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 5.1189 ms, kernel 6.5760 ms, copy-out 5.0721 ms; source buffer at 0x420780000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 5.991e+04, copy 2.125e+05; multiplexed rows voided: 0

### route/footprint-mib=9728,kernel=k3,placement=cpu

- first variant A, seed 71; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 15.1 GB/s over the touched lines; buffer at 0x4dd840000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 26.8127 ms, kernel 0.4923 ms, copy-out 0.0132 ms; source buffer at 0x4ddb40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (35.5 per touched line), copy 1.02e+10; SMMU translation requests per repetition: direct 3.597e+07, copy 1.625e+05; multiplexed rows voided: 0

