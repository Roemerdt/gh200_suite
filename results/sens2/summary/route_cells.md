# Route cells: direct route against copy route, recomputed from raw rows

Times are per repetition in ms: one pass for the direct route, one complete call (copy-in, kernel, copy-out) for the copy route. The route difference is direct minus copy within a repeat, as median with its 95 % rank interval; a negative value means direct access is faster. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | direct ms | copy ms | route difference ms [interval] | relative to copy | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|
| copy=ce-pageable-1-256m-none-whole,footprint-mib=256,kernel=k3,placement=cpu | 5.3732 | 1.1934 | 4.1798 [4.1792, 4.1806] | +350.2 % | 10 | yes | pass |
| copy=ce-registered-1-4m-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=1024 | 46.7501 | 8.1037 | 38.6510 [38.6243, 38.6694] | +477.0 % | 10 | yes | pass |
| copy=ce-registered-1-64m-pipe-touched,f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=cpu | 2.6522 | 2.7513 | -0.0991 [-0.1012, -0.0978] | -3.6 % | 10 | yes | pass |
| copy=ce-registered-1-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=2,tiling=tiles | 7.7133 | 3.4235 | 4.2876 [4.2804, 4.2934] | +125.2 % | 10 | yes | pass |
| copy=ce-registered-1-whole-none-whole,footprint-mib=16384,kernel=k3,placement=cpu | 433.4192 | 46.2396 | 387.1848 [387.0212, 387.3718] | +837.3 % | 10 | yes | pass |
| copy=ce-registered-1-whole-none-whole,footprint-mib=4096,kernel=k3,placement=cpu | 5.5522 | 11.8944 | -6.3417 [-6.3882, -6.3070] | -53.3 % | 10 | yes | pass |
| copy=ce-registered-1-whole-none-whole,footprint-mib=8192,kernel=k3,placement=cpu | 7.7455 | 23.3090 | -15.5629 [-15.5710, -15.5593] | -66.8 % | 10 | yes | pass |
| copy=ce-registered-2-256m-pipe-whole,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu | 11.5854 | 11.5630 | 0.0226 [0.0204, 0.0247] | +0.2 % | 50 | yes | pass |
| copy=ce-registered-2-64m-pipe-whole,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 2.9096 | 3.0097 | -0.1000 [-0.1029, -0.0990] | -3.3 % | 10 | yes | pass |
| copy=ce-registered-2-64m-pipe-whole,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu | 0.7252 | 0.7936 | -0.0684 [-0.0690, -0.0677] | -8.6 % | 10 | yes | pass |
| copy=ce-registered-2-64m-pipe-whole-kernel,footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu | 31.0726 | 3.3300 | 27.7446 [27.7368, 27.7789] | +833.2 % | 10 | yes | pass |
| copy=ce-registered-2-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=1,tiling=tiles | 3.9257 | 3.0238 | 0.9022 [0.8978, 0.9036] | +29.8 % | 10 | yes | pass |
| copy=ce-registered-2-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=16,tiling=tiles | 61.8174 | 9.0356 | 52.7859 [52.7590, 52.8113] | +584.2 % | 10 | yes | pass |
| copy=ce-registered-2-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=none | 46.9038 | 5.4102 | 41.4910 [41.4502, 41.5051] | +766.9 % | 10 | yes | pass |
| copy=ce-registered-2-whole-none-whole,footprint-mib=1024,kernel=k3,placement=cpu | 5.3798 | 3.4037 | 1.9761 [1.9745, 1.9771] | +58.1 % | 10 | yes | pass |
| copy=ce-registered-2-whole-none-whole,footprint-mib=1536,kernel=k3,placement=cpu | 5.3797 | 4.8273 | 0.5524 [0.5510, 0.5564] | +11.4 % | 10 | yes | pass |
| copy=ce-registered-2-whole-none-whole,footprint-mib=2048,kernel=k3,placement=cpu | 5.3789 | 6.2377 | -0.8591 [-0.8625, -0.8550] | -13.8 % | 10 | yes | pass |
| copy=ce-registered-2-whole-none-whole-kernel,footprint-mib=1024,kernel=k6,placement=cpu,update=atomic | 6.0384 | 6.5997 | -0.5611 [-0.5628, -0.5571] | -8.5 % | 10 | yes | pass |
| copy=ce-registered-4-64m-pipe-touched,f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=cpu | 2.2090 | 2.2817 | -0.0726 [-0.0735, -0.0703] | -3.2 % | 10 | yes | pass |
| copy=ce-registered-4-64m-pipe-whole-kernel,footprint-mib=256,generator=uniform,kernel=k4,placement=cpu | 7.3944 | 0.8946 | 6.4996 [6.4928, 6.5018] | +726.6 % | 10 | yes | pass |
| copy=ce-registered-4-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=4,tiling=tiles | 15.4536 | 4.2327 | 11.2215 [11.2036, 11.2391] | +265.1 % | 10 | yes | pass |
| copy=ce-registered-4-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=64,tiling=tiles | 247.1152 | 28.3416 | 218.7732 [218.7146, 218.7832] | +771.9 % | 10 | yes | pass |
| copy=ce-registered-4-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles | 30.9157 | 5.8258 | 25.0894 [25.0737, 25.1204] | +430.7 % | 10 | yes | pass |
| copy=ce-registered-4-whole-none-whole,footprint-mib=24576,kernel=k3,placement=cpu | 598.3297 | 69.4319 | 528.9060 [528.7665, 529.1102] | +761.8 % | 10 | yes | pass |
| copy=ce-registered-4-whole-none-whole,footprint-mib=32768,kernel=k3,placement=cpu | 684.9811 | 92.8079 | 592.1699 [592.0720, 592.3424] | +638.1 % | 10 | yes | pass |
| copy=kernel-pageable-1-256m-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1,placement=hbm | 12.2921 | 12.3085 | -0.0163 [-0.0171, -0.0158] | -0.1 % | 10 | yes | pass |
| copy=kernel-pageable-1-64m-none-touched,footprint-mib=1024,k=1,kernel=k2,placement=hbm,working-set-mib=32 | 0.0178 | 0.0527 | -0.0349 [-0.0350, -0.0347] | -66.3 % | 10 | yes | pass |
| copy=kernel-pageable-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=32 | 1.4930 | 0.1822 | 1.3110 [1.3105, 1.3116] | +719.7 % | 10 | yes | pass |
| copy=kernel-pageable-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=8 | 0.0378 | 0.0537 | -0.0159 [-0.0161, -0.0158] | -29.7 % | 10 | yes | pass |
| copy=kernel-pageable-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=8 | 0.0163 | 0.0338 | -0.0174 [-0.0177, -0.0173] | -51.6 % | 10 | yes | pass |
| copy=kernel-pageable-1-whole-none-touched,footprint-mib=1024,k=4,kernel=k2,placement=hbm,working-set-mib=32 | 0.0347 | 0.0606 | -0.0259 [-0.0260, -0.0258] | -42.7 % | 10 | yes | pass |
| copy=kernel-pageable-1-whole-none-whole,footprint-mib=256,kernel=k3,placement=hbm | 0.4260 | 0.6024 | -0.1764 [-0.1768, -0.1758] | -29.3 % | 10 | yes | pass |
| copy=kernel-pageable-1-whole-none-whole-kernel,footprint-mib=256,generator=uniform,kernel=k4,placement=hbm | 0.2115 | 0.3787 | -0.1671 [-0.1676, -0.1668] | -44.1 % | 10 | yes | pass |
| copy=kernel-registered-1-16m-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=cpu,rotated=1,working-set-mib=8 | 0.3734 | 0.0683 | 0.3052 [0.3047, 0.3056] | +447.1 % | 10 | yes | pass |
| copy=kernel-registered-1-16m-none-whole-kernel,footprint-mib=16,kernel=k6,placement=hbm,update=atomic | 0.0732 | 0.0956 | -0.0224 [-0.0225, -0.0224] | -23.5 % | 10 | yes | pass |
| copy=kernel-registered-1-16m-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1024,placement=cpu | 12.4831 | 0.8220 | 11.6611 [11.6577, 11.6660] | +1418.6 % | 10 | yes | pass |
| copy=kernel-registered-1-16m-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu | 8.7672 | 0.2314 | 8.5357 [8.5311, 8.5380] | +3689.1 % | 10 | yes | pass |
| copy=kernel-registered-1-256m-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=hbm,rotated=1,working-set-mib=8 | 0.0301 | 0.0486 | -0.0184 [-0.0186, -0.0184] | -38.0 % | 10 | yes | pass |
| copy=kernel-registered-1-256m-none-whole-kernel,footprint-mib=256,kernel=k6,placement=cpu,update=atomic | 1.5035 | 1.6704 | -0.1674 [-0.1676, -0.1648] | -10.0 % | 10 | yes | pass |
| copy=kernel-registered-1-4m-none-touched,footprint-mib=1024,k=64,kernel=k2,placement=hbm,working-set-mib=32 | 0.3441 | 0.3016 | 0.0426 [0.0415, 0.0431] | +14.1 % | 10 | yes | pass |
| copy=kernel-registered-1-64m-none-touched,footprint-mib=1024,k=2,kernel=k2,placement=cpu,working-set-mib=32 | 0.1921 | 0.1260 | 0.0661 [0.0660, 0.0663] | +52.5 % | 10 | yes | pass |
| copy=kernel-registered-1-64m-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1024,placement=hbm | 0.7660 | 0.7814 | -0.0154 [-0.0159, -0.0150] | -2.0 % | 10 | yes | pass |
| copy=kernel-registered-1-whole-none-touched,footprint-mib=1024,k=1,kernel=k2,placement=cpu,working-set-mib=32 | 0.1000 | 0.1228 | -0.0228 [-0.0236, -0.0217] | -18.6 % | 10 | yes | pass |
| copy=kernel-registered-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=32 | 0.0957 | 0.1080 | -0.0123 [-0.0125, -0.0122] | -11.4 % | 10 | yes | pass |
| copy=kernel-registered-1-whole-none-touched,footprint-mib=1024,k=2,kernel=k2,placement=hbm,working-set-mib=32 | 0.0235 | 0.0545 | -0.0310 [-0.0312, -0.0307] | -56.9 % | 10 | yes | pass |
| copy=kernel-registered-1-whole-none-touched,footprint-mib=1024,k=4,kernel=k2,placement=cpu,working-set-mib=32 | 0.3780 | 0.1332 | 0.2448 [0.2446, 0.2450] | +183.8 % | 10 | yes | pass |
| copy=kernel-registered-1-whole-none-whole,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm | 0.0792 | 0.2547 | -0.1755 [-0.1756, -0.1751] | -68.9 % | 10 | yes | pass |
| copy=kernel-registered-1-whole-none-whole,footprint-mib=11520,kernel=k3,placement=cpu | 240.4489 | 32.2662 | 208.1987 [208.0800, 208.2637] | +645.3 % | 10 | yes | pass |
| copy=kernel-registered-1-whole-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1,placement=cpu | 191.3083 | 12.3498 | 178.9589 [178.9565, 178.9640] | +1449.1 % | 10 | yes | pass |
| copy=kernel-registered-1-whole-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1048576,placement=hbm | 0.1942 | 0.1911 | 0.0031 [0.0030, 0.0032] | +1.6 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 2.9054 | 3.2286 | -0.3235 [-0.3256, -0.3219] | -10.0 % | 20 | yes | pass |
| f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu | 0.7280 | 0.8469 | -0.1190 [-0.1195, -0.1185] | -14.0 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm | 0.0783 | 0.7328 | -0.6545 [-0.6549, -0.6544] | -89.3 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu | 11.5762 | 12.5777 | -1.0004 [-1.0132, -0.9978] | -8.0 % | 10 | yes | pass |
| f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=cpu | 2.6454 | 3.1961 | -0.5508 [-0.5519, -0.5488] | -17.2 % | 10 | yes | pass |
| f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=cpu | 2.2114 | 3.1578 | -0.9467 [-0.9481, -0.9432] | -30.0 % | 10 | yes | pass |
| footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu | 31.1141 | 4.1339 | 26.9815 [26.9620, 26.9895] | +652.7 % | 20 | yes | pass |
| footprint-mib=1024,k=1,kernel=k2,placement=cpu,working-set-mib=32 | 0.0998 | 0.1292 | -0.0294 [-0.0295, -0.0291] | -22.7 % | 10 | yes | pass |
| footprint-mib=1024,k=1,kernel=k2,placement=hbm,working-set-mib=32 | 0.0174 | 0.1182 | -0.1009 [-0.1012, -0.1008] | -85.3 % | 20 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,rotated=1,working-set-mib=8 | 0.3730 | 0.0760 | 0.2970 [0.2968, 0.2972] | +390.7 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=1024 | 46.7233 | 8.0746 | 38.6438 [38.6327, 38.6625] | +478.6 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=32 | 1.4852 | 0.1822 | 1.3032 [1.3026, 1.3038] | +715.3 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=8 | 0.0376 | 0.0615 | -0.0239 [-0.0240, -0.0238] | -38.9 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,rotated=1,working-set-mib=8 | 0.0302 | 0.0748 | -0.0446 [-0.0448, -0.0445] | -59.6 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=32 | 0.0977 | 0.1776 | -0.0799 [-0.0800, -0.0798] | -45.0 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=8 | 0.0161 | 0.0589 | -0.0427 [-0.0428, -0.0426] | -72.6 % | 10 | yes | pass |
| footprint-mib=1024,k=2,kernel=k2,placement=cpu,working-set-mib=32 | 0.1920 | 0.1314 | 0.0605 [0.0601, 0.0607] | +46.1 % | 10 | yes | pass |
| footprint-mib=1024,k=2,kernel=k2,placement=hbm,working-set-mib=32 | 0.0235 | 0.1228 | -0.0993 [-0.0996, -0.0987] | -80.9 % | 10 | yes | pass |
| footprint-mib=1024,k=4,kernel=k2,placement=cpu,working-set-mib=32 | 0.3738 | 0.1358 | 0.2380 [0.2377, 0.2382] | +175.3 % | 10 | yes | pass |
| footprint-mib=1024,k=4,kernel=k2,placement=hbm,working-set-mib=32 | 0.0350 | 0.1314 | -0.0965 [-0.0967, -0.0960] | -73.4 % | 10 | yes | pass |
| footprint-mib=1024,k=64,kernel=k2,placement=hbm,working-set-mib=32 | 0.3476 | 0.3740 | -0.0265 [-0.0267, -0.0259] | -7.1 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k3,placement=cpu | 5.3786 | 3.4114 | 1.9670 [1.9635, 1.9690] | +57.7 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=cpu,update=atomic | 6.0285 | 7.3660 | -1.3388 [-1.3426, -1.3310] | -18.2 % | 10 | yes | pass |
| footprint-mib=11520,kernel=k3,placement=cpu | 240.1108 | 32.6152 | 207.4943 [207.3806, 207.5538] | +636.2 % | 10 | yes | pass |
| footprint-mib=1536,kernel=k3,placement=cpu | 5.3789 | 4.8321 | 0.5467 [0.5455, 0.5477] | +11.3 % | 10 | yes | pass |
| footprint-mib=16,kernel=k6,placement=hbm,update=atomic | 0.0776 | 0.1951 | -0.1175 [-0.1178, -0.1173] | -60.3 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,placement=cpu | 433.3436 | 46.2523 | 387.0928 [386.8943, 387.1396] | +836.9 % | 10 | yes | pass |
| footprint-mib=2048,kernel=k3,placement=cpu | 5.3795 | 6.2478 | -0.8689 [-0.8697, -0.8667] | -13.9 % | 10 | yes | pass |
| footprint-mib=24576,kernel=k3,placement=cpu | 598.3089 | 69.3546 | 528.9450 [528.7874, 528.9768] | +762.7 % | 30 | yes | pass |
| footprint-mib=256,generator=uniform,kernel=k4,placement=cpu | 7.4108 | 0.9997 | 6.4094 [6.4027, 6.4132] | +641.2 % | 10 | yes | pass |
| footprint-mib=256,generator=uniform,kernel=k4,placement=hbm | 0.2109 | 0.8869 | -0.6759 [-0.6768, -0.6749] | -76.2 % | 10 | yes | pass |
| footprint-mib=256,kernel=k3,placement=cpu | 5.3724 | 1.1889 | 4.1836 [4.1832, 4.1840] | +351.9 % | 10 | yes | pass |
| footprint-mib=256,kernel=k3,placement=hbm | 0.4258 | 1.0823 | -0.6564 [-0.6571, -0.6553] | -60.6 % | 10 | yes | pass |
| footprint-mib=256,kernel=k6,placement=cpu,update=atomic | 1.5042 | 1.8553 | -0.3509 [-0.3546, -0.3493] | -18.9 % | 10 | yes | pass |
| footprint-mib=32768,kernel=k3,placement=cpu | 685.0761 | 92.7943 | 592.2755 [592.1860, 592.3286] | +638.3 % | 10 | yes | pass |
| footprint-mib=4096,kernel=k3,placement=cpu | 5.5211 | 11.8948 | -6.3705 [-6.4037, -6.3293] | -53.6 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=1,tiling=tiles | 3.9191 | 3.6822 | 0.2362 [0.2335, 0.2427] | +6.4 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=16,tiling=tiles | 61.6698 | 9.6773 | 51.9983 [51.9312, 52.0141] | +537.3 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=2,tiling=tiles | 7.7246 | 4.0850 | 3.6395 [3.6371, 3.6443] | +89.1 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=4,tiling=tiles | 15.4930 | 4.8845 | 10.6071 [10.5997, 10.6172] | +217.2 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=64,tiling=tiles | 247.9283 | 29.0765 | 218.8422 [218.8022, 218.9157] | +752.6 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=none | 47.0844 | 6.0196 | 41.0680 [40.9856, 41.1039] | +682.2 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles | 30.9352 | 6.4837 | 24.4525 [24.4391, 24.4671] | +377.1 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1,placement=cpu | 191.3129 | 12.3698 | 178.9437 [178.9393, 179.0103] | +1446.6 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1,placement=hbm | 12.2922 | 12.3627 | -0.0706 [-0.0722, -0.0700] | -0.6 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1024,placement=cpu | 12.4803 | 0.8401 | 11.6396 [11.6360, 11.6460] | +1385.5 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1024,placement=hbm | 0.7662 | 0.8347 | -0.0685 [-0.0695, -0.0682] | -8.2 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1048576,placement=cpu | 8.6055 | 0.2490 | 8.3567 [8.3525, 8.3620] | +3356.7 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1048576,placement=hbm | 0.1836 | 0.2445 | -0.0609 [-0.0613, -0.0605] | -24.9 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu | 7.7466 | 23.3727 | -15.6259 [-15.6341, -15.6226] | -66.9 % | 10 | yes | pass |

## Per cell

### route/copy=ce-pageable-1-256m-none-whole,footprint-mib=256,kernel=k3,placement=cpu

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 49.9 GB/s over the touched lines; buffer at 0x58b180000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 17 calls per interval; first call of an interval: copy-in 0.7611 ms, kernel 0.4275 ms, copy-out 0.0147 ms; source buffer at 0x58b240000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.368e+08 (256.0 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 0, copy 4115; multiplexed rows voided: 0

### route/copy=ce-registered-1-4m-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=1024

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 23.0 GB/s over the touched lines; buffer at 0x5575c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 2.9349 ms, kernel 5.1588 ms, copy-out 0.0144 ms; source buffer at 0x5576c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.718e+10 (2048.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.639e+04; multiplexed rows voided: 0

### route/copy=ce-registered-1-64m-pipe-touched,f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 8 passes per interval, 364.4 GB/s over the touched lines; buffer at 0x5f3980000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 8 calls per interval; first call of an interval: copy-in 2.7189 ms, kernel 0.0269 ms, copy-out 0.0122 ms; source buffer at 0x5f3a80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 9.664e+08 (128.0 per touched line), copy 9.664e+08; SMMU translation requests per repetition: direct 0, copy 1.644e+04; multiplexed rows voided: 0

### route/copy=ce-registered-1-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=2,tiling=tiles

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 69.6 GB/s over the touched lines; buffer at 0x41f400000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 1.5343 ms, kernel 0.4577 ms, copy-out 1.4442 ms; source buffer at 0x41f500000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.605e+09 (382.8 per touched line), copy 5.378e+08; SMMU translation requests per repetition: direct 1.207e+04, copy 9698; multiplexed rows voided: 0

### route/copy=ce-registered-1-whole-none-whole,footprint-mib=16384,kernel=k3,placement=cpu

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x479640000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 45.7233 ms, kernel 0.5000 ms, copy-out 0.0153 ms; source buffer at 0x479b00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 1.211e+08, copy 2.622e+05; multiplexed rows voided: 0

### route/copy=ce-registered-1-whole-none-whole,footprint-mib=4096,kernel=k3,placement=cpu

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 304.4 GB/s over the touched lines; buffer at 0x5f2e80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 11.4075 ms, kernel 0.4771 ms, copy-out 0.0137 ms; source buffer at 0x5f3040000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (40.7 per touched line), copy 4.295e+09; SMMU translation requests per repetition: direct 0, copy 6.556e+04; multiplexed rows voided: 0

### route/copy=ce-registered-1-whole-none-whole,footprint-mib=8192,kernel=k3,placement=cpu

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 245.3 GB/s over the touched lines; buffer at 0x47f740000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 22.7996 ms, kernel 0.4933 ms, copy-out 0.0158 ms; source buffer at 0x47fa00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (36.2 per touched line), copy 8.607e+09; SMMU translation requests per repetition: direct 4111, copy 1.311e+05; multiplexed rows voided: 0

### route/copy=ce-registered-2-256m-pipe-whole,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 370.7 GB/s over the touched lines; buffer at 0x444240000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 11.4708 ms, kernel 0.0841 ms, copy-out 0.0129 ms; source buffer at 0x444400000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 4.295e+09 (128.0 per touched line), copy 4.295e+09; SMMU translation requests per repetition: direct 0, copy 6.556e+04; multiplexed rows voided: 0

### route/copy=ce-registered-2-64m-pipe-whole,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 7 passes per interval, 369.0 GB/s over the touched lines; buffer at 0x4972c0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9784 ms, kernel 0.0289 ms, copy-out 0.0125 ms; source buffer at 0x4973c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+09 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/copy=ce-registered-2-64m-pipe-whole,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 28 passes per interval, 370.1 GB/s over the touched lines; buffer at 0x461380000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 26 calls per interval; first call of an interval: copy-in 0.7630 ms, kernel 0.0291 ms, copy-out 0.0113 ms; source buffer at 0x461440000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.684e+08 (128.0 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 0, copy 4110; multiplexed rows voided: 0

### route/copy=ce-registered-2-64m-pipe-whole-kernel,footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 34.6 GB/s over the touched lines; buffer at 0x582f40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 3.1662 ms, kernel 0.0846 ms, copy-out 0.0887 ms; source buffer at 0x583040000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.198e+09 (381.3 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.783e+04; multiplexed rows voided: 0

### route/copy=ce-registered-2-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=1,tiling=tiles

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 136.8 GB/s over the touched lines; buffer at 0x54fc00000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 1.5326 ms, kernel 0.0597 ms, copy-out 1.4432 ms; source buffer at 0x54fd00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.027e+08 (191.4 per touched line), copy 5.378e+08; SMMU translation requests per repetition: direct 3688, copy 9482; multiplexed rows voided: 0

### route/copy=ce-registered-2-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=16,tiling=tiles

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 8.7 GB/s over the touched lines; buffer at 0x509240000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 1.5399 ms, kernel 6.0576 ms, copy-out 1.4463 ms; source buffer at 0x509340000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.284e+10 (3062.3 per touched line), copy 5.378e+08; SMMU translation requests per repetition: direct 3.602e+04, copy 1.121e+04; multiplexed rows voided: 0

### route/copy=ce-registered-2-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=none

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 11.4 GB/s over the touched lines; buffer at 0x4da3c0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.5349 ms, kernel 2.4445 ms, copy-out 1.4432 ms; source buffer at 0x4da4c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.308e+10 (3118.0 per touched line), copy 5.378e+08; SMMU translation requests per repetition: direct 3.038e+04, copy 1.041e+04; multiplexed rows voided: 0

### route/copy=ce-registered-2-whole-none-whole,footprint-mib=1024,kernel=k3,placement=cpu

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 172.6 GB/s over the touched lines; buffer at 0x46c0c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 2.9304 ms, kernel 0.4661 ms, copy-out 0.0147 ms; source buffer at 0x46c1c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.641e+04; multiplexed rows voided: 0

### route/copy=ce-registered-2-whole-none-whole,footprint-mib=1536,kernel=k3,placement=cpu

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 220.5 GB/s over the touched lines; buffer at 0x5ee240000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 4.3490 ms, kernel 0.4706 ms, copy-out 0.0142 ms; source buffer at 0x5ee340000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (57.9 per touched line), copy 1.611e+09; SMMU translation requests per repetition: direct 0, copy 2.46e+04; multiplexed rows voided: 0

### route/copy=ce-registered-2-whole-none-whole,footprint-mib=2048,kernel=k3,placement=cpu

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 252.3 GB/s over the touched lines; buffer at 0x441940000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 5.7601 ms, kernel 0.4732 ms, copy-out 0.0140 ms; source buffer at 0x441a80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (50.6 per touched line), copy 2.147e+09; SMMU translation requests per repetition: direct 0, copy 3.279e+04; multiplexed rows voided: 0

### route/copy=ce-registered-2-whole-none-whole-kernel,footprint-mib=1024,kernel=k6,placement=cpu,update=atomic

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 177.8 GB/s over the touched lines; buffer at 0x5f03c0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 2.9152 ms, kernel 0.8078 ms, copy-out 2.8850 ms; source buffer at 0x5f0480000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 4193, copy 2.073e+04; multiplexed rows voided: 0

### route/copy=ce-registered-4-64m-pipe-touched,f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 10 passes per interval, 364.5 GB/s over the touched lines; buffer at 0x438180000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 9 calls per interval; first call of an interval: copy-in 2.2519 ms, kernel 0.0236 ms, copy-out 0.0119 ms; source buffer at 0x438280000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.053e+08 (128.0 per touched line), copy 8.053e+08; SMMU translation requests per repetition: direct 0, copy 1.733e+04; multiplexed rows voided: 0

### route/copy=ce-registered-4-64m-pipe-whole-kernel,footprint-mib=256,generator=uniform,kernel=k4,placement=cpu

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 36.3 GB/s over the touched lines; buffer at 0x50cdc0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 23 calls per interval; first call of an interval: copy-in 0.8126 ms, kernel 0.0649 ms, copy-out 0.0253 ms; source buffer at 0x50ce80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 7.686e+08 (366.5 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 0, copy 4411; multiplexed rows voided: 0

### route/copy=ce-registered-4-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=4,tiling=tiles

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 34.7 GB/s over the touched lines; buffer at 0x5040c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 1.5356 ms, kernel 1.2640 ms, copy-out 1.4448 ms; source buffer at 0x5041c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.211e+09 (765.6 per touched line), copy 5.378e+08; SMMU translation requests per repetition: direct 1.801e+04, copy 9982; multiplexed rows voided: 0

### route/copy=ce-registered-4-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=64,tiling=tiles

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 2.2 GB/s over the touched lines; buffer at 0x53c440000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 1.5387 ms, kernel 25.3622 ms, copy-out 1.4421 ms; source buffer at 0x53c540000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.138e+10 (12249.1 per touched line), copy 5.378e+08; SMMU translation requests per repetition: direct 3.618e+04, copy 1.724e+04; multiplexed rows voided: 0

### route/copy=ce-registered-4-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 17.4 GB/s over the touched lines; buffer at 0x425100000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.5328 ms, kernel 2.8575 ms, copy-out 1.4420 ms; source buffer at 0x425200000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.1 per touched line), copy 5.378e+08; SMMU translation requests per repetition: direct 3.611e+04, copy 1.045e+04; multiplexed rows voided: 0

### route/copy=ce-registered-4-whole-none-whole,footprint-mib=24576,kernel=k3,placement=cpu

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 3.4 GB/s over the touched lines; buffer at 0x52eec0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 68.9092 ms, kernel 0.5050 ms, copy-out 0.0172 ms; source buffer at 0x52f580000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (33.4 per touched line), copy 2.585e+10; SMMU translation requests per repetition: direct 1.671e+08, copy 3.932e+05; multiplexed rows voided: 0

### route/copy=ce-registered-4-whole-none-whole,footprint-mib=32768,kernel=k3,placement=cpu

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 3.0 GB/s over the touched lines; buffer at 0x46ecc0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 92.2811 ms, kernel 0.5105 ms, copy-out 0.0135 ms; source buffer at 0x46f580000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (33.0 per touched line), copy 3.448e+10; SMMU translation requests per repetition: direct 1.912e+08, copy 5.243e+05; multiplexed rows voided: 0

### route/copy=kernel-pageable-1-256m-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1,placement=hbm

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x4545c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 0.0138 ms, kernel 12.2908 ms, copy-out 0.0076 ms; source buffer at 0x454680000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-pageable-1-64m-none-touched,footprint-mib=1024,k=1,kernel=k2,placement=hbm,working-set-mib=32

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 1133 passes per interval, 1887.1 GB/s over the touched lines; buffer at 0x474880000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 387 calls per interval; first call of an interval: copy-in 0.0257 ms, kernel 0.0170 ms, copy-out 0.0112 ms; source buffer at 0x474980000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-pageable-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=32

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.5 GB/s over the touched lines; buffer at 0x5f1480000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 111 calls per interval; first call of an interval: copy-in 0.1037 ms, kernel 0.0726 ms, copy-out 0.0132 ms; source buffer at 0x5f1540000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.365e+08 (2047.7 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-pageable-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=8

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 530 passes per interval, 221.7 GB/s over the touched lines; buffer at 0x446740000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 377 calls per interval; first call of an interval: copy-in 0.0336 ms, kernel 0.0156 ms, copy-out 0.0142 ms; source buffer at 0x446800000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-pageable-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=8

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 1225 passes per interval, 512.9 GB/s over the touched lines; buffer at 0x562840000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 595 calls per interval; first call of an interval: copy-in 0.0140 ms, kernel 0.0157 ms, copy-out 0.0100 ms; source buffer at 0x562940000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-pageable-1-whole-none-touched,footprint-mib=1024,k=4,kernel=k2,placement=hbm,working-set-mib=32

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 578 passes per interval, 965.9 GB/s over the touched lines; buffer at 0x4e7580000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 332 calls per interval; first call of an interval: copy-in 0.0260 ms, kernel 0.0282 ms, copy-out 0.0145 ms; source buffer at 0x4e7680000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-pageable-1-whole-none-whole,footprint-mib=256,kernel=k3,placement=hbm

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 47 passes per interval, 629.9 GB/s over the touched lines; buffer at 0x59e5c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 34 calls per interval; first call of an interval: copy-in 0.1621 ms, kernel 0.4344 ms, copy-out 0.0134 ms; source buffer at 0x59e680000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-pageable-1-whole-none-whole-kernel,footprint-mib=256,generator=uniform,kernel=k4,placement=hbm

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 95 passes per interval, 1269.4 GB/s over the touched lines; buffer at 0x5af880000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 53 calls per interval; first call of an interval: copy-in 0.1629 ms, kernel 0.2141 ms, copy-out 0.0078 ms; source buffer at 0x5af940000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-16m-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=cpu,rotated=1,working-set-mib=8

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 54 passes per interval, 22.4 GB/s over the touched lines; buffer at 0x5fbe80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 294 calls per interval; first call of an interval: copy-in 0.0341 ms, kernel 0.0287 ms, copy-out 0.0117 ms; source buffer at 0x5fbf40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.341e+08 (2048.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-16m-none-whole-kernel,footprint-mib=16,kernel=k6,placement=hbm,update=atomic

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 274 passes per interval, 229.2 GB/s over the touched lines; buffer at 0x5bf780000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 210 calls per interval; first call of an interval: copy-in 0.0178 ms, kernel 0.0778 ms, copy-out 0.0113 ms; source buffer at 0x5bf800000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-16m-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1024,placement=cpu

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x50af40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 25 calls per interval; first call of an interval: copy-in 0.0354 ms, kernel 0.7678 ms, copy-out 0.0268 ms; source buffer at 0x50b000000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-16m-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 1.0 GB/s over the touched lines; buffer at 0x47ffc0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 87 calls per interval; first call of an interval: copy-in 0.0356 ms, kernel 0.1788 ms, copy-out 0.0269 ms; source buffer at 0x480040000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-256m-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=hbm,rotated=1,working-set-mib=8

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 665 passes per interval, 278.3 GB/s over the touched lines; buffer at 0x5e90c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 413 calls per interval; first call of an interval: copy-in 0.0142 ms, kernel 0.0286 ms, copy-out 0.0147 ms; source buffer at 0x5e91c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-256m-none-whole-kernel,footprint-mib=256,kernel=k6,placement=cpu,update=atomic

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 178.5 GB/s over the touched lines; buffer at 0x50ddc0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 13 calls per interval; first call of an interval: copy-in 0.7584 ms, kernel 0.2052 ms, copy-out 0.7195 ms; source buffer at 0x50de80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 313.9, copy 422; multiplexed rows voided: 0

### route/copy=kernel-registered-1-4m-none-touched,footprint-mib=1024,k=64,kernel=k2,placement=hbm,working-set-mib=32

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 59 passes per interval, 97.5 GB/s over the touched lines; buffer at 0x5f5300000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 67 calls per interval; first call of an interval: copy-in 0.0248 ms, kernel 0.2678 ms, copy-out 0.0111 ms; source buffer at 0x5f5400000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-64m-none-touched,footprint-mib=1024,k=2,kernel=k2,placement=cpu,working-set-mib=32

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 105 passes per interval, 174.6 GB/s over the touched lines; buffer at 0x564a40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 160 calls per interval; first call of an interval: copy-in 0.1036 ms, kernel 0.0163 ms, copy-out 0.0121 ms; source buffer at 0x564b00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.708e+07 (256.0 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-64m-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1024,placement=hbm

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 27 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x4c1840000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 26 calls per interval; first call of an interval: copy-in 0.0148 ms, kernel 0.7678 ms, copy-out 0.0081 ms; source buffer at 0x4c18c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-whole-none-touched,footprint-mib=1024,k=1,kernel=k2,placement=cpu,working-set-mib=32

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 201 passes per interval, 335.5 GB/s over the touched lines; buffer at 0x4a21c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 163 calls per interval; first call of an interval: copy-in 0.1043 ms, kernel 0.0132 ms, copy-out 0.0148 ms; source buffer at 0x4a22c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.354e+07 (128.0 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=32

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 217 passes per interval, 350.5 GB/s over the touched lines; buffer at 0x5f2ac0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 186 calls per interval; first call of an interval: copy-in 0.0255 ms, kernel 0.0753 ms, copy-out 0.0131 ms; source buffer at 0x5f2bc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-whole-none-touched,footprint-mib=1024,k=2,kernel=k2,placement=hbm,working-set-mib=32

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 851 passes per interval, 1426.8 GB/s over the touched lines; buffer at 0x55adc0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 369 calls per interval; first call of an interval: copy-in 0.0257 ms, kernel 0.0204 ms, copy-out 0.0135 ms; source buffer at 0x55aec0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-whole-none-touched,footprint-mib=1024,k=4,kernel=k2,placement=cpu,working-set-mib=32

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 53 passes per interval, 88.7 GB/s over the touched lines; buffer at 0x50aac0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 151 calls per interval; first call of an interval: copy-in 0.1032 ms, kernel 0.0245 ms, copy-out 0.0142 ms; source buffer at 0x50abc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.342e+08 (512.0 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-whole-none-whole,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 255 passes per interval, 3389.9 GB/s over the touched lines; buffer at 0x548d40000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 79 calls per interval; first call of an interval: copy-in 0.1619 ms, kernel 0.0872 ms, copy-out 0.0111 ms; source buffer at 0x548e00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-whole-none-whole,footprint-mib=11520,kernel=k3,placement=cpu

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 8.2 GB/s over the touched lines; buffer at 0x5bd640000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 31.7575 ms, kernel 0.4935 ms, copy-out 0.0152 ms; source buffer at 0x5bd980000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.9 per touched line), copy 1.208e+10; SMMU translation requests per repetition: direct 6.723e+07, copy 1.925e+05; multiplexed rows voided: 0

### route/copy=kernel-registered-1-whole-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1,placement=cpu

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x57d200000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 0.0360 ms, kernel 12.2911 ms, copy-out 0.0268 ms; source buffer at 0x57d280000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-whole-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1048576,placement=hbm

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 104 passes per interval, 43.2 GB/s over the touched lines; buffer at 0x454280000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 106 calls per interval; first call of an interval: copy-in 0.0139 ms, kernel 0.1782 ms, copy-out 0.0076 ms; source buffer at 0x454340000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 7 passes per interval, 369.6 GB/s over the touched lines; buffer at 0x4b10c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9305 ms, kernel 0.2976 ms, copy-out 0.0121 ms; source buffer at 0x4b11c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+09 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 28 passes per interval, 368.7 GB/s over the touched lines; buffer at 0x5e9540000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 24 calls per interval; first call of an interval: copy-in 0.7581 ms, kernel 0.0801 ms, copy-out 0.0161 ms; source buffer at 0x5e9600000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.684e+08 (128.0 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 0, copy 4111; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 255 passes per interval, 3426.2 GB/s over the touched lines; buffer at 0x46b800000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 28 calls per interval; first call of an interval: copy-in 0.6479 ms, kernel 0.0812 ms, copy-out 0.0126 ms; source buffer at 0x46b8c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 4110; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 371.0 GB/s over the touched lines; buffer at 0x57da40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 11.3998 ms, kernel 1.1665 ms, copy-out 0.0147 ms; source buffer at 0x57dbc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 4.295e+09 (128.0 per touched line), copy 4.295e+09; SMMU translation requests per repetition: direct 0, copy 6.556e+04; multiplexed rows voided: 0

### route/f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 8 passes per interval, 365.3 GB/s over the touched lines; buffer at 0x5fd840000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9162 ms, kernel 0.2755 ms, copy-out 0.0119 ms; source buffer at 0x5fd980000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 9.664e+08 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 10 passes per interval, 364.2 GB/s over the touched lines; buffer at 0x447b80000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9195 ms, kernel 0.2325 ms, copy-out 0.0130 ms; source buffer at 0x447c80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.053e+08 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 34.5 GB/s over the touched lines; buffer at 0x51bd00000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 2.9158 ms, kernel 1.1065 ms, copy-out 0.1203 ms; source buffer at 0x51bdc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.195e+09 (380.9 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.689e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=1,kernel=k2,placement=cpu,working-set-mib=32

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 198 passes per interval, 335.9 GB/s over the touched lines; buffer at 0x4d9d40000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 156 calls per interval; first call of an interval: copy-in 0.1059 ms, kernel 0.0148 ms, copy-out 0.0123 ms; source buffer at 0x4d9e40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.354e+07 (128.0 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 532.9; multiplexed rows voided: 0

### route/footprint-mib=1024,k=1,kernel=k2,placement=hbm,working-set-mib=32

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 1151 passes per interval, 1930.2 GB/s over the touched lines; buffer at 0x5abec0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 171 calls per interval; first call of an interval: copy-in 0.0966 ms, kernel 0.0216 ms, copy-out 0.0124 ms; source buffer at 0x5abfc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 520.1; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,rotated=1,working-set-mib=8

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 54 passes per interval, 22.5 GB/s over the touched lines; buffer at 0x5b1b00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 267 calls per interval; first call of an interval: copy-in 0.0393 ms, kernel 0.0299 ms, copy-out 0.0101 ms; source buffer at 0x5b1c00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.341e+08 (2048.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 0, copy 132.6; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=1024

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 23.0 GB/s over the touched lines; buffer at 0x534dc0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 2.9154 ms, kernel 5.1584 ms, copy-out 0.0117 ms; source buffer at 0x534ec0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.718e+10 (2048.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.639e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=32

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.6 GB/s over the touched lines; buffer at 0x498ec0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 106 calls per interval; first call of an interval: copy-in 0.1069 ms, kernel 0.0755 ms, copy-out 0.0119 ms; source buffer at 0x498f80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.365e+08 (2047.7 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 532.9; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=8

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 530 passes per interval, 223.1 GB/s over the touched lines; buffer at 0x42f900000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 328 calls per interval; first call of an interval: copy-in 0.0382 ms, kernel 0.0163 ms, copy-out 0.0143 ms; source buffer at 0x42fa00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 0, copy 132.6; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,rotated=1,working-set-mib=8

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 660 passes per interval, 277.4 GB/s over the touched lines; buffer at 0x600040000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 268 calls per interval; first call of an interval: copy-in 0.0368 ms, kernel 0.0353 ms, copy-out 0.0149 ms; source buffer at 0x600100000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 134.1; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=32

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 201 passes per interval, 343.3 GB/s over the touched lines; buffer at 0x4bfb00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 112 calls per interval; first call of an interval: copy-in 0.0956 ms, kernel 0.0826 ms, copy-out 0.0094 ms; source buffer at 0x4bfbc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 517.9; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=8

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 1242 passes per interval, 519.3 GB/s over the touched lines; buffer at 0x47f200000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 341 calls per interval; first call of an interval: copy-in 0.0364 ms, kernel 0.0206 ms, copy-out 0.0131 ms; source buffer at 0x47f300000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 134.5; multiplexed rows voided: 0

### route/footprint-mib=1024,k=2,kernel=k2,placement=cpu,working-set-mib=32

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 104 passes per interval, 174.7 GB/s over the touched lines; buffer at 0x572940000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 149 calls per interval; first call of an interval: copy-in 0.1052 ms, kernel 0.0188 ms, copy-out 0.0117 ms; source buffer at 0x572a40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.708e+07 (256.0 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 532.9; multiplexed rows voided: 0

### route/footprint-mib=1024,k=2,kernel=k2,placement=hbm,working-set-mib=32

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 857 passes per interval, 1427.3 GB/s over the touched lines; buffer at 0x471300000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 165 calls per interval; first call of an interval: copy-in 0.0960 ms, kernel 0.0257 ms, copy-out 0.0104 ms; source buffer at 0x471400000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 518.9; multiplexed rows voided: 0

### route/footprint-mib=1024,k=4,kernel=k2,placement=cpu,working-set-mib=32

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 53 passes per interval, 89.7 GB/s over the touched lines; buffer at 0x4fc500000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 143 calls per interval; first call of an interval: copy-in 0.1030 ms, kernel 0.0272 ms, copy-out 0.0111 ms; source buffer at 0x4fc600000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.342e+08 (512.0 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 533; multiplexed rows voided: 0

### route/footprint-mib=1024,k=4,kernel=k2,placement=hbm,working-set-mib=32

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 577 passes per interval, 959.1 GB/s over the touched lines; buffer at 0x4a62c0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 151 calls per interval; first call of an interval: copy-in 0.0956 ms, kernel 0.0344 ms, copy-out 0.0128 ms; source buffer at 0x4a63c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 519.8; multiplexed rows voided: 0

### route/footprint-mib=1024,k=64,kernel=k2,placement=hbm,working-set-mib=32

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 63 passes per interval, 96.5 GB/s over the touched lines; buffer at 0x4b0b00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 54 calls per interval; first call of an interval: copy-in 0.0942 ms, kernel 0.2772 ms, copy-out 0.0105 ms; source buffer at 0x4b0c00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 521.4; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k3,placement=cpu

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 172.6 GB/s over the touched lines; buffer at 0x52fa00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 2.9362 ms, kernel 0.4686 ms, copy-out 0.0136 ms; source buffer at 0x52fb00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.641e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=cpu,update=atomic

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 178.1 GB/s over the touched lines; buffer at 0x505740000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 2.9527 ms, kernel 0.8098 ms, copy-out 3.6175 ms; source buffer at 0x505800000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 4177, copy 3.278e+04; multiplexed rows voided: 0

### route/footprint-mib=11520,kernel=k3,placement=cpu

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 8.2 GB/s over the touched lines; buffer at 0x5fc600000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 32.0960 ms, kernel 0.5023 ms, copy-out 0.0160 ms; source buffer at 0x5fc980000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.9 per touched line), copy 1.211e+10; SMMU translation requests per repetition: direct 6.714e+07, copy 1.843e+05; multiplexed rows voided: 0

### route/footprint-mib=1536,kernel=k3,placement=cpu

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 220.5 GB/s over the touched lines; buffer at 0x4f5ec0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 4.3539 ms, kernel 0.4737 ms, copy-out 0.0138 ms; source buffer at 0x4f5fc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (57.9 per touched line), copy 1.611e+09; SMMU translation requests per repetition: direct 0, copy 2.46e+04; multiplexed rows voided: 0

### route/footprint-mib=16,kernel=k6,placement=hbm,update=atomic

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 260 passes per interval, 216.2 GB/s over the touched lines; buffer at 0x401840000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 105 calls per interval; first call of an interval: copy-in 0.0563 ms, kernel 0.0843 ms, copy-out 0.0643 ms; source buffer at 0x401900000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 124.1; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x4be900000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 45.7324 ms, kernel 0.5048 ms, copy-out 0.0150 ms; source buffer at 0x4bedc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 1.211e+08, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=2048,kernel=k3,placement=cpu

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 252.3 GB/s over the touched lines; buffer at 0x4b41c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 5.7666 ms, kernel 0.4766 ms, copy-out 0.0154 ms; source buffer at 0x4b4300000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (50.6 per touched line), copy 2.147e+09; SMMU translation requests per repetition: direct 0, copy 3.279e+04; multiplexed rows voided: 0

### route/footprint-mib=24576,kernel=k3,placement=cpu

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 3.4 GB/s over the touched lines; buffer at 0x4a11c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 68.8278 ms, kernel 0.5121 ms, copy-out 0.0145 ms; source buffer at 0x4a1880000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (33.4 per touched line), copy 2.585e+10; SMMU translation requests per repetition: direct 1.671e+08, copy 3.932e+05; multiplexed rows voided: 0

### route/footprint-mib=256,generator=uniform,kernel=k4,placement=cpu

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 36.2 GB/s over the touched lines; buffer at 0x568c00000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 20 calls per interval; first call of an interval: copy-in 0.7608 ms, kernel 0.2122 ms, copy-out 0.0384 ms; source buffer at 0x568cc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 7.683e+08 (366.3 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 0, copy 4228; multiplexed rows voided: 0

### route/footprint-mib=256,generator=uniform,kernel=k4,placement=hbm

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 95 passes per interval, 1272.5 GB/s over the touched lines; buffer at 0x5340c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 23 calls per interval; first call of an interval: copy-in 0.6470 ms, kernel 0.2131 ms, copy-out 0.0377 ms; source buffer at 0x534180000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 4228; multiplexed rows voided: 0

### route/footprint-mib=256,kernel=k3,placement=cpu

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 50.0 GB/s over the touched lines; buffer at 0x4c8c00000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 17 calls per interval; first call of an interval: copy-in 0.7569 ms, kernel 0.4276 ms, copy-out 0.0134 ms; source buffer at 0x4c8cc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.368e+08 (256.0 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 0, copy 4115; multiplexed rows voided: 0

### route/footprint-mib=256,kernel=k3,placement=hbm

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 47 passes per interval, 630.2 GB/s over the touched lines; buffer at 0x4b8980000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 19 calls per interval; first call of an interval: copy-in 0.6478 ms, kernel 0.4282 ms, copy-out 0.0141 ms; source buffer at 0x4b8a80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 4115; multiplexed rows voided: 0

### route/footprint-mib=256,kernel=k6,placement=cpu,update=atomic

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 178.5 GB/s over the touched lines; buffer at 0x4e8080000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 11 calls per interval; first call of an interval: copy-in 0.7570 ms, kernel 0.1963 ms, copy-out 0.9127 ms; source buffer at 0x4e8140000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 312, copy 8196; multiplexed rows voided: 0

### route/footprint-mib=32768,kernel=k3,placement=cpu

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 3.0 GB/s over the touched lines; buffer at 0x528d00000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 92.2632 ms, kernel 0.5151 ms, copy-out 0.0175 ms; source buffer at 0x529580000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (33.0 per touched line), copy 3.448e+10; SMMU translation requests per repetition: direct 1.912e+08, copy 5.243e+05; multiplexed rows voided: 0

### route/footprint-mib=4096,kernel=k3,placement=cpu

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 306.1 GB/s over the touched lines; buffer at 0x44f9c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 11.4053 ms, kernel 0.4802 ms, copy-out 0.0164 ms; source buffer at 0x44fb80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (40.7 per touched line), copy 4.295e+09; SMMU translation requests per repetition: direct 0, copy 6.556e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=1,tiling=tiles

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 137.0 GB/s over the touched lines; buffer at 0x446b80000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 1.4715 ms, kernel 0.4147 ms, copy-out 1.8136 ms; source buffer at 0x446c80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.027e+08 (191.4 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3684, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=16,tiling=tiles

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 8.7 GB/s over the touched lines; buffer at 0x532d80000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 1.4670 ms, kernel 6.4197 ms, copy-out 1.8158 ms; source buffer at 0x532e80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.284e+10 (3062.3 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.597e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=2,tiling=tiles

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 69.5 GB/s over the touched lines; buffer at 0x52a700000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 1.4729 ms, kernel 0.8168 ms, copy-out 1.8135 ms; source buffer at 0x52a800000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.606e+09 (382.8 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 1.2e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=4,tiling=tiles

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 34.7 GB/s over the touched lines; buffer at 0x466440000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 1.4742 ms, kernel 1.6154 ms, copy-out 1.8147 ms; source buffer at 0x466540000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.211e+09 (765.6 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 1.796e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=64,tiling=tiles

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 2.2 GB/s over the touched lines; buffer at 0x5bdc00000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 1.4761 ms, kernel 25.7841 ms, copy-out 1.8131 ms; source buffer at 0x5bdd00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.138e+10 (12249.1 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.614e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=none

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 11.4 GB/s over the touched lines; buffer at 0x464c80000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.4767 ms, kernel 2.7396 ms, copy-out 1.8146 ms; source buffer at 0x464d80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.308e+10 (3118.7 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.017e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 17.4 GB/s over the touched lines; buffer at 0x44b480000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.4733 ms, kernel 3.2137 ms, copy-out 1.8176 ms; source buffer at 0x44b580000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.1 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.589e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1,placement=cpu

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x401e00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 0.0396 ms, kernel 12.2933 ms, copy-out 0.0389 ms; source buffer at 0x401e80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1,placement=hbm

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x4bdd80000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 0.0359 ms, kernel 12.2932 ms, copy-out 0.0376 ms; source buffer at 0x4bde00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1024,placement=cpu

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x46acc0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 24 calls per interval; first call of an interval: copy-in 0.0396 ms, kernel 0.7712 ms, copy-out 0.0411 ms; source buffer at 0x46ad80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1024,placement=hbm

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 27 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x5da9c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 25 calls per interval; first call of an interval: copy-in 0.0359 ms, kernel 0.7699 ms, copy-out 0.0352 ms; source buffer at 0x5daa80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1048576,placement=cpu

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 1.0 GB/s over the touched lines; buffer at 0x53f2c0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 81 calls per interval; first call of an interval: copy-in 0.0393 ms, kernel 0.1816 ms, copy-out 0.0385 ms; source buffer at 0x53f380000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1048576,placement=hbm

- first variant B, seed 107; repeats alternated as drawn: yes
- direct route: 111 passes per interval, 45.7 GB/s over the touched lines; buffer at 0x58ec00000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 83 calls per interval; first call of an interval: copy-in 0.0354 ms, kernel 0.1824 ms, copy-out 0.0358 ms; source buffer at 0x58ecc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu

- first variant A, seed 107; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 245.3 GB/s over the touched lines; buffer at 0x5456c0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 22.8563 ms, kernel 0.4975 ms, copy-out 0.0175 ms; source buffer at 0x545940000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (36.2 per touched line), copy 8.607e+09; SMMU translation requests per repetition: direct 4098, copy 1.311e+05; multiplexed rows voided: 0

