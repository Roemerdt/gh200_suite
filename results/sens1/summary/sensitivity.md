# Route verdicts against the frozen and the fastest copy

Per setting whose simplest copy was frozen within the floor: the route difference (direct minus copy, ms, median with its 95 % rank interval; negative means direct access is faster) with the frozen copy and with the fastest copy, and the verdict (the faster route, or '-' when not resolvable) under the absolute route floor and under the relative floor (8.0 % of the copy route, the 90th percentile over 113 route-axis contrasts of c1 against c2, at least the A/A' floor of 0.0628 ms). 'campaign' is the verdict of the frozen cell in c1 with c2 as replicate, absolute floor.

Verdicts that change with the fastest copy: 4 of 50 under the absolute floor, 11 of 50 under the relative floor.

| kernel | plac. | setting | frozen copy | route diff, frozen | fastest copy | route diff, fastest | abs: campaign / frozen / fastest | rel: frozen / fastest |
|---|---|---|---|---|---|---|---|---|
| k1 | cpu | f-den=1,f-num=1,footprint-mib=1024 | ce-pageable-1-whole-none-whole | -0.3069 [-0.3094, -0.3052] | ce-registered-2-64m-pipe-whole | -0.0816 [-0.0848, -0.0794] | - / - / - | direct / - |
| k1 | cpu | f-den=1,f-num=1,footprint-mib=256 | ce-pageable-1-whole-none-whole | -0.1091 [-0.1095, -0.1082] | ce-registered-2-64m-pipe-whole | -0.0715 [-0.0721, -0.0713] | - / - / - | direct / direct |
| k1 | cpu | f-den=1,f-num=1,footprint-mib=4096 | ce-pageable-1-whole-none-whole | -0.9934 [-0.9972, -0.9880] | ce-registered-2-256m-pipe-whole | 0.0468 [0.0433, 0.0512] | direct / direct / - | - / - |
| k1 | cpu | f-den=10,f-num=9,footprint-mib=1024 | ce-pageable-1-whole-none-whole | -0.5562 [-0.5569, -0.5544] | ce-registered-1-64m-pipe-touched | -0.0897 [-0.0923, -0.0889] | - / - / - | direct / - |
| k1 | cpu | f-den=4,f-num=3,footprint-mib=1024 | ce-pageable-1-whole-none-whole | -0.9731 [-0.9738, -0.9724] | ce-registered-4-64m-pipe-touched | -0.0724 [-0.0735, -0.0702] | direct / direct / - | direct / - |
| k1 | hbm | f-den=1,f-num=1,footprint-mib=256 | ce-pageable-1-whole-none-whole | -0.6538 [-0.6542, -0.6531] | kernel-registered-1-whole-none-whole | -0.1762 [-0.1765, -0.1758] | - / - / - | direct / direct |
| k2 | cpu | footprint-mib=1024,k=1,working-set-mib=32 | ce-registered-1-whole-none-touched | -0.0301 [-0.0306, -0.0297] | kernel-registered-1-whole-none-touched | -0.0224 [-0.0228, -0.0222] | - / - / - | - / - |
| k2 | cpu | footprint-mib=1024,k=16,rotated=1,working-set-mib=8 | ce-registered-1-whole-none-touched | 0.2967 [0.2958, 0.2971] | kernel-registered-1-16m-none-touched | 0.3050 [0.3043, 0.3054] | - / - / - | copy / copy |
| k2 | cpu | footprint-mib=1024,k=16,working-set-mib=1024 | ce-registered-1-whole-none-touched | 38.6371 [38.6185, 38.6468] | ce-registered-1-4m-none-touched | 38.6920 [38.6515, 38.7134] | copy / copy / copy | copy / copy |
| k2 | cpu | footprint-mib=1024,k=16,working-set-mib=32 | ce-registered-1-whole-none-touched | 1.3096 [1.3084, 1.3102] | kernel-pageable-1-whole-none-touched | 1.3087 [1.3079, 1.3095] | copy / copy / copy | copy / copy |
| k2 | cpu | footprint-mib=1024,k=16,working-set-mib=8 | ce-registered-1-whole-none-touched | -0.0236 [-0.0238, -0.0235] | kernel-pageable-1-whole-none-touched | -0.0160 [-0.0161, -0.0160] | - / - / - | - / - |
| k2 | cpu | footprint-mib=1024,k=2,working-set-mib=32 | ce-registered-1-whole-none-touched | 0.0613 [0.0611, 0.0618] | kernel-registered-1-64m-none-touched | 0.0662 [0.0658, 0.0664] | - / - / - | - / copy |
| k2 | cpu | footprint-mib=1024,k=4,working-set-mib=32 | ce-registered-1-whole-none-touched | 0.2365 [0.2364, 0.2370] | kernel-registered-1-whole-none-touched | 0.2405 [0.2402, 0.2406] | - / - / - | copy / copy |
| k2 | hbm | footprint-mib=1024,k=1,working-set-mib=32 | ce-pageable-1-whole-none-touched | -0.1018 [-0.1021, -0.1014] | kernel-pageable-1-64m-none-touched | -0.0325 [-0.0327, -0.0324] | - / - / - | direct / - |
| k2 | hbm | footprint-mib=1024,k=16,rotated=1,working-set-mib=8 | ce-pageable-1-whole-none-touched | -0.0447 [-0.0448, -0.0445] | kernel-registered-1-256m-none-touched | -0.0178 [-0.0179, -0.0178] | - / - / - | - / - |
| k2 | hbm | footprint-mib=1024,k=16,working-set-mib=32 | ce-pageable-1-whole-none-touched | -0.0823 [-0.0826, -0.0819] | kernel-registered-1-whole-none-touched | -0.0120 [-0.0122, -0.0119] | - / - / - | direct / - |
| k2 | hbm | footprint-mib=1024,k=16,working-set-mib=8 | ce-pageable-1-whole-none-touched | -0.0426 [-0.0426, -0.0424] | kernel-pageable-1-whole-none-touched | -0.0175 [-0.0176, -0.0174] | - / - / - | - / - |
| k2 | hbm | footprint-mib=1024,k=2,working-set-mib=32 | ce-pageable-1-whole-none-touched | -0.1006 [-0.1009, -0.0996] | kernel-registered-1-whole-none-touched | -0.0316 [-0.0318, -0.0314] | - / - / - | direct / - |
| k2 | hbm | footprint-mib=1024,k=4,working-set-mib=32 | ce-pageable-1-whole-none-touched | -0.0987 [-0.0991, -0.0986] | kernel-pageable-1-whole-none-touched | -0.0256 [-0.0258, -0.0251] | - / - / - | direct / - |
| k2 | hbm | footprint-mib=1024,k=64,working-set-mib=32 | ce-pageable-1-whole-none-touched | -0.0333 [-0.0339, -0.0324] | kernel-registered-1-4m-none-touched | 0.0481 [0.0472, 0.0489] | - / - / - | - / - |
| k3 | cpu | footprint-mib=1024 | ce-pageable-1-whole-none-whole | 1.9868 [1.9861, 1.9881] | ce-registered-2-whole-none-whole | 1.9945 [1.9928, 1.9978] | copy / copy / copy | copy / copy |
| k3 | cpu | footprint-mib=11520 | ce-pageable-1-whole-none-whole | 207.1762 [207.0536, 207.2942] | kernel-registered-1-whole-none-whole | 207.8076 [207.7129, 207.8454] | copy / copy / copy | copy / copy |
| k3 | cpu | footprint-mib=1536 | ce-pageable-1-whole-none-whole | 0.5552 [0.5533, 0.5565] | ce-registered-2-whole-none-whole | 0.5533 [0.5523, 0.5566] | - / - / - | copy / copy |
| k3 | cpu | footprint-mib=16384 | ce-pageable-1-whole-none-whole | 386.5545 [386.4594, 386.6122] | ce-registered-1-whole-none-whole | 386.5097 [386.3769, 386.5777] | copy / copy / copy | copy / copy |
| k3 | cpu | footprint-mib=2048 | ce-pageable-1-whole-none-whole | -0.8718 [-0.8741, -0.8700] | ce-registered-2-whole-none-whole | -0.8646 [-0.8691, -0.8622] | direct / direct / direct | direct / direct |
| k3 | cpu | footprint-mib=24576 | ce-pageable-1-whole-none-whole | 528.0288 [527.9586, 528.0751] | ce-registered-4-whole-none-whole | 528.0435 [527.9312, 528.1896] | copy / copy / copy | copy / copy |
| k3 | cpu | footprint-mib=256 | ce-pageable-1-whole-none-whole | 4.1842 [4.1833, 4.1853] | ce-pageable-1-256m-none-whole | 4.1788 [4.1784, 4.1796] | copy / copy / copy | copy / copy |
| k3 | cpu | footprint-mib=32768 | ce-pageable-1-whole-none-whole | 592.2302 [592.1306, 592.3278] | ce-registered-4-whole-none-whole | 591.2619 [591.2128, 591.3097] | copy / copy / copy | copy / copy |
| k3 | cpu | footprint-mib=4096 | ce-pageable-1-whole-none-whole | -6.3172 [-6.3626, -6.3061] | ce-registered-1-whole-none-whole | -6.3308 [-6.3527, -6.2988] | direct / direct / direct | direct / direct |
| k3 | cpu | footprint-mib=8192 | ce-pageable-1-whole-none-whole | -15.5717 [-15.5741, -15.5586] | ce-registered-1-whole-none-whole | -15.5575 [-15.5693, -15.5523] | direct / direct / direct | direct / direct |
| k3 | hbm | footprint-mib=256 | ce-pageable-1-whole-none-whole | -0.6555 [-0.6563, -0.6550] | kernel-pageable-1-whole-none-whole | -0.1754 [-0.1761, -0.1751] | - / - / - | direct / direct |
| k4 | cpu | footprint-mib=1024,generator=uniform | ce-pageable-1-whole-none-whole | 26.9941 [26.9783, 27.0083] | ce-registered-2-64m-pipe-whole-kernel | 27.8079 [27.7901, 27.8434] | copy / copy / copy | copy / copy |
| k4 | cpu | footprint-mib=256,generator=uniform | ce-pageable-1-whole-none-whole | 6.3951 [6.3927, 6.4023] | ce-registered-4-64m-pipe-whole-kernel | 6.5029 [6.5012, 6.5056] | copy / copy / copy | copy / copy |
| k4 | hbm | footprint-mib=256,generator=uniform | ce-pageable-1-whole-none-whole | -0.6759 [-0.6765, -0.6754] | kernel-pageable-1-whole-none-whole-kernel | -0.1665 [-0.1666, -0.1662] | - / - / - | direct / direct |
| k5 | cpu | footprint-mib=512,sweeps=1,tiling=tiles | ce-pageable-1-whole-none-whole | 0.2523 [0.2495, 0.2548] | ce-registered-2-64m-pipe-whole-kernel | 0.8898 [0.8858, 0.8925] | - / - / copy | - / copy |
| k5 | cpu | footprint-mib=512,sweeps=16,tiling=tiles | ce-pageable-1-whole-none-whole | 52.6559 [52.6332, 52.6856] | ce-registered-2-64m-pipe-whole-kernel | 53.1280 [53.1157, 53.1741] | copy / copy / copy | copy / copy |
| k5 | cpu | footprint-mib=512,sweeps=2,tiling=tiles | ce-pageable-1-whole-none-whole | 3.7062 [3.6980, 3.7095] | ce-registered-1-64m-pipe-whole-kernel | 4.3640 [4.3598, 4.3705] | copy / copy / copy | copy / copy |
| k5 | cpu | footprint-mib=512,sweeps=4,tiling=tiles | ce-pageable-1-whole-none-whole | 10.6526 [10.6399, 10.6628] | ce-registered-4-64m-pipe-whole-kernel | 11.3883 [11.3802, 11.4049] | copy / copy / copy | copy / copy |
| k5 | cpu | footprint-mib=512,sweeps=64,tiling=tiles | ce-pageable-1-whole-none-whole | 219.6114 [219.5447, 219.6839] | ce-registered-4-64m-pipe-whole-kernel | 221.1905 [221.0968, 221.2476] | copy / copy / copy | copy / copy |
| k5 | cpu | footprint-mib=512,sweeps=8,tiling=none | ce-pageable-1-whole-none-whole | 40.9032 [40.8590, 40.9380] | ce-registered-2-64m-pipe-whole-kernel | 41.5842 [41.5624, 41.6401] | copy / copy / copy | copy / copy |
| k5 | cpu | footprint-mib=512,sweeps=8,tiling=tiles | ce-pageable-1-whole-none-whole | 24.6952 [24.6671, 24.7116] | ce-registered-4-64m-pipe-whole-kernel | 25.2544 [25.2254, 25.2759] | copy / copy / copy | copy / copy |
| k6 | cpu | footprint-mib=1024,update=atomic | ce-pageable-1-whole-none-whole | -1.2952 [-1.3041, -1.2864] | ce-registered-2-whole-none-whole-kernel | -0.5510 [-0.5596, -0.5460] | direct / direct / - | direct / direct |
| k6 | cpu | footprint-mib=256,update=atomic | ce-pageable-1-whole-none-whole | -0.3632 [-0.3645, -0.3619] | kernel-registered-1-256m-none-whole-kernel | -0.1712 [-0.1723, -0.1705] | - / - / - | direct / direct |
| k6 | cpu | footprint-mib=8,keys=1 | ce-pageable-1-whole-none-whole | 178.9399 [178.9383, 178.9433] | kernel-registered-1-whole-none-whole-kernel | 178.9593 [178.9573, 178.9603] | copy / copy / copy | copy / copy |
| k6 | cpu | footprint-mib=8,keys=1024 | ce-pageable-1-whole-none-whole | 11.6514 [11.6477, 11.6581] | kernel-registered-1-16m-none-whole-kernel | 11.6713 [11.6645, 11.6770] | copy / copy / copy | copy / copy |
| k6 | cpu | footprint-mib=8,keys=1048576 | ce-pageable-1-whole-none-whole | 7.8076 [7.8050, 7.8093] | kernel-registered-1-16m-none-whole-kernel | 7.7832 [7.7809, 7.7862] | copy / copy / copy | copy / copy |
| k6 | hbm | footprint-mib=16,update=atomic | ce-pageable-1-whole-none-whole | -0.1110 [-0.1111, -0.1105] | kernel-registered-1-16m-none-whole-kernel | -0.0202 [-0.0203, -0.0202] | - / - / - | direct / - |
| k6 | hbm | footprint-mib=8,keys=1 | ce-pageable-1-whole-none-whole | -0.0707 [-0.0715, -0.0692] | kernel-pageable-1-256m-none-whole-kernel | -0.0155 [-0.0162, -0.0148] | - / - / - | - / - |
| k6 | hbm | footprint-mib=8,keys=1024 | ce-pageable-1-whole-none-whole | -0.0687 [-0.0695, -0.0682] | kernel-registered-1-64m-none-whole-kernel | -0.0148 [-0.0151, -0.0142] | - / - / - | direct / - |
| k6 | hbm | footprint-mib=8,keys=1048576 | ce-pageable-1-whole-none-whole | -0.0487 [-0.0489, -0.0483] | kernel-registered-1-whole-none-whole-kernel | -0.0129 [-0.0131, -0.0127] | - / - / - | - / - |
