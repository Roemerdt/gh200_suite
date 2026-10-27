# Route cells: direct route against copy route, recomputed from raw rows

Times are per repetition in ms: one pass for the direct route, one complete call (copy-in, kernel, copy-out) for the copy route. The route difference is direct minus copy within a repeat, as median with its 95 % rank interval; a negative value means direct access is faster. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | direct ms | copy ms | route difference ms [interval] | relative to copy | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|
| copy=ce-pageable-1-256m-none-whole,footprint-mib=256,kernel=k3,placement=cpu | 5.3718 | 1.1929 | 4.1788 [4.1784, 4.1796] | +350.3 % | 10 | yes | pass |
| copy=ce-registered-1-4m-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=1024 | 46.7757 | 8.0834 | 38.6920 [38.6515, 38.7134] | +478.7 % | 10 | yes | pass |
| copy=ce-registered-1-64m-pipe-touched,f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=cpu | 2.6458 | 2.7356 | -0.0897 [-0.0923, -0.0889] | -3.3 % | 10 | yes | pass |
| copy=ce-registered-1-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=2,tiling=tiles | 7.7912 | 3.4255 | 4.3640 [4.3598, 4.3705] | +127.4 % | 10 | yes | pass |
| copy=ce-registered-1-whole-none-whole,footprint-mib=16384,kernel=k3,placement=cpu | 432.7391 | 46.2338 | 386.5097 [386.3769, 386.5777] | +836.0 % | 10 | yes | pass |
| copy=ce-registered-1-whole-none-whole,footprint-mib=4096,kernel=k3,placement=cpu | 5.5538 | 11.8808 | -6.3308 [-6.3527, -6.2988] | -53.3 % | 10 | yes | pass |
| copy=ce-registered-1-whole-none-whole,footprint-mib=8192,kernel=k3,placement=cpu | 7.7451 | 23.3063 | -15.5575 [-15.5693, -15.5523] | -66.8 % | 10 | yes | pass |
| copy=ce-registered-2-256m-pipe-whole,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu | 11.5780 | 11.5311 | 0.0468 [0.0433, 0.0512] | +0.4 % | 20 | yes | pass |
| copy=ce-registered-2-64m-pipe-whole,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 2.9054 | 2.9872 | -0.0816 [-0.0848, -0.0794] | -2.7 % | 10 | yes | pass |
| copy=ce-registered-2-64m-pipe-whole,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu | 0.7253 | 0.7968 | -0.0715 [-0.0721, -0.0713] | -9.0 % | 10 | yes | pass |
| copy=ce-registered-2-64m-pipe-whole-kernel,footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu | 31.1374 | 3.3280 | 27.8079 [27.7901, 27.8434] | +835.6 % | 10 | yes | pass |
| copy=ce-registered-2-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=1,tiling=tiles | 3.9192 | 3.0289 | 0.8898 [0.8858, 0.8925] | +29.4 % | 10 | yes | pass |
| copy=ce-registered-2-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=16,tiling=tiles | 62.1481 | 9.0148 | 53.1280 [53.1157, 53.1741] | +589.3 % | 10 | yes | pass |
| copy=ce-registered-2-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=none | 46.9856 | 5.4015 | 41.5842 [41.5624, 41.6401] | +769.9 % | 10 | yes | pass |
| copy=ce-registered-2-whole-none-whole,footprint-mib=1024,kernel=k3,placement=cpu | 5.3786 | 3.3837 | 1.9945 [1.9928, 1.9978] | +58.9 % | 10 | yes | pass |
| copy=ce-registered-2-whole-none-whole,footprint-mib=1536,kernel=k3,placement=cpu | 5.3795 | 4.8262 | 0.5533 [0.5523, 0.5566] | +11.5 % | 10 | yes | pass |
| copy=ce-registered-2-whole-none-whole,footprint-mib=2048,kernel=k3,placement=cpu | 5.3793 | 6.2438 | -0.8646 [-0.8691, -0.8622] | -13.8 % | 10 | yes | pass |
| copy=ce-registered-2-whole-none-whole-kernel,footprint-mib=1024,kernel=k6,placement=cpu,update=atomic | 6.0481 | 6.5988 | -0.5510 [-0.5596, -0.5460] | -8.4 % | 10 | yes | pass |
| copy=ce-registered-4-64m-pipe-touched,f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=cpu | 2.2077 | 2.2796 | -0.0724 [-0.0735, -0.0702] | -3.2 % | 10 | yes | pass |
| copy=ce-registered-4-64m-pipe-whole-kernel,footprint-mib=256,generator=uniform,kernel=k4,placement=cpu | 7.3987 | 0.8953 | 6.5029 [6.5012, 6.5056] | +726.4 % | 10 | yes | pass |
| copy=ce-registered-4-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=4,tiling=tiles | 15.6103 | 4.2157 | 11.3883 [11.3802, 11.4049] | +270.1 % | 10 | yes | pass |
| copy=ce-registered-4-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=64,tiling=tiles | 249.4406 | 28.2681 | 221.1905 [221.0968, 221.2476] | +782.5 % | 10 | yes | pass |
| copy=ce-registered-4-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles | 31.0877 | 5.8332 | 25.2544 [25.2254, 25.2759] | +432.9 % | 10 | yes | pass |
| copy=ce-registered-4-whole-none-whole,footprint-mib=24576,kernel=k3,placement=cpu | 597.3710 | 69.3398 | 528.0435 [527.9312, 528.1896] | +761.5 % | 10 | yes | pass |
| copy=ce-registered-4-whole-none-whole,footprint-mib=32768,kernel=k3,placement=cpu | 683.9616 | 92.7066 | 591.2619 [591.2128, 591.3097] | +637.8 % | 10 | yes | pass |
| copy=kernel-pageable-1-256m-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1,placement=hbm | 12.2932 | 12.3085 | -0.0155 [-0.0162, -0.0148] | -0.1 % | 10 | yes | pass |
| copy=kernel-pageable-1-64m-none-touched,footprint-mib=1024,k=1,kernel=k2,placement=hbm,working-set-mib=32 | 0.0176 | 0.0501 | -0.0325 [-0.0327, -0.0324] | -64.9 % | 10 | yes | pass |
| copy=kernel-pageable-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=32 | 1.4918 | 0.1831 | 1.3087 [1.3079, 1.3095] | +714.7 % | 10 | yes | pass |
| copy=kernel-pageable-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=8 | 0.0379 | 0.0539 | -0.0160 [-0.0161, -0.0160] | -29.7 % | 10 | yes | pass |
| copy=kernel-pageable-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=8 | 0.0163 | 0.0338 | -0.0175 [-0.0176, -0.0174] | -51.8 % | 10 | yes | pass |
| copy=kernel-pageable-1-whole-none-touched,footprint-mib=1024,k=4,kernel=k2,placement=hbm,working-set-mib=32 | 0.0346 | 0.0602 | -0.0256 [-0.0258, -0.0251] | -42.5 % | 10 | yes | pass |
| copy=kernel-pageable-1-whole-none-whole,footprint-mib=256,kernel=k3,placement=hbm | 0.4267 | 0.6020 | -0.1754 [-0.1761, -0.1751] | -29.1 % | 10 | yes | pass |
| copy=kernel-pageable-1-whole-none-whole-kernel,footprint-mib=256,generator=uniform,kernel=k4,placement=hbm | 0.2115 | 0.3779 | -0.1665 [-0.1666, -0.1662] | -44.1 % | 10 | yes | pass |
| copy=kernel-registered-1-16m-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=cpu,rotated=1,working-set-mib=8 | 0.3732 | 0.0682 | 0.3050 [0.3043, 0.3054] | +447.2 % | 10 | yes | pass |
| copy=kernel-registered-1-16m-none-whole-kernel,footprint-mib=16,kernel=k6,placement=hbm,update=atomic | 0.0796 | 0.0998 | -0.0202 [-0.0203, -0.0202] | -20.3 % | 10 | yes | pass |
| copy=kernel-registered-1-16m-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1024,placement=cpu | 12.4931 | 0.8218 | 11.6713 [11.6645, 11.6770] | +1420.3 % | 10 | yes | pass |
| copy=kernel-registered-1-16m-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu | 8.0149 | 0.2317 | 7.7832 [7.7809, 7.7862] | +3358.8 % | 10 | yes | pass |
| copy=kernel-registered-1-256m-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=hbm,rotated=1,working-set-mib=8 | 0.0300 | 0.0478 | -0.0178 [-0.0179, -0.0178] | -37.3 % | 10 | yes | pass |
| copy=kernel-registered-1-256m-none-whole-kernel,footprint-mib=256,kernel=k6,placement=cpu,update=atomic | 1.5000 | 1.6713 | -0.1712 [-0.1723, -0.1705] | -10.2 % | 10 | yes | pass |
| copy=kernel-registered-1-4m-none-touched,footprint-mib=1024,k=64,kernel=k2,placement=hbm,working-set-mib=32 | 0.3520 | 0.3040 | 0.0481 [0.0472, 0.0489] | +15.8 % | 10 | yes | pass |
| copy=kernel-registered-1-64m-none-touched,footprint-mib=1024,k=2,kernel=k2,placement=cpu,working-set-mib=32 | 0.1915 | 0.1253 | 0.0662 [0.0658, 0.0664] | +52.8 % | 10 | yes | pass |
| copy=kernel-registered-1-64m-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1024,placement=hbm | 0.7661 | 0.7809 | -0.0148 [-0.0151, -0.0142] | -1.9 % | 10 | yes | pass |
| copy=kernel-registered-1-whole-none-touched,footprint-mib=1024,k=1,kernel=k2,placement=cpu,working-set-mib=32 | 0.0995 | 0.1220 | -0.0224 [-0.0228, -0.0222] | -18.4 % | 10 | yes | pass |
| copy=kernel-registered-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=32 | 0.0978 | 0.1098 | -0.0120 [-0.0122, -0.0119] | -10.9 % | 10 | yes | pass |
| copy=kernel-registered-1-whole-none-touched,footprint-mib=1024,k=2,kernel=k2,placement=hbm,working-set-mib=32 | 0.0236 | 0.0551 | -0.0316 [-0.0318, -0.0314] | -57.2 % | 10 | yes | pass |
| copy=kernel-registered-1-whole-none-touched,footprint-mib=1024,k=4,kernel=k2,placement=cpu,working-set-mib=32 | 0.3754 | 0.1349 | 0.2405 [0.2402, 0.2406] | +178.3 % | 10 | yes | pass |
| copy=kernel-registered-1-whole-none-whole,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm | 0.0788 | 0.2550 | -0.1762 [-0.1765, -0.1758] | -69.1 % | 10 | yes | pass |
| copy=kernel-registered-1-whole-none-whole,footprint-mib=11520,kernel=k3,placement=cpu | 240.1664 | 32.3579 | 207.8076 [207.7129, 207.8454] | +642.2 % | 10 | yes | pass |
| copy=kernel-registered-1-whole-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1,placement=cpu | 191.3099 | 12.3505 | 178.9593 [178.9573, 178.9603] | +1449.0 % | 10 | yes | pass |
| copy=kernel-registered-1-whole-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1048576,placement=hbm | 0.1790 | 0.1919 | -0.0129 [-0.0131, -0.0127] | -6.7 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 2.9130 | 3.2200 | -0.3069 [-0.3094, -0.3052] | -9.5 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu | 0.7292 | 0.8382 | -0.1091 [-0.1095, -0.1082] | -13.0 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm | 0.0785 | 0.7323 | -0.6538 [-0.6542, -0.6531] | -89.3 % | 30 | yes | pass |
| f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu | 11.5772 | 12.5700 | -0.9934 [-0.9972, -0.9880] | -7.9 % | 10 | yes | pass |
| f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=cpu | 2.6510 | 3.2067 | -0.5562 [-0.5569, -0.5544] | -17.3 % | 10 | yes | pass |
| f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=cpu | 2.2068 | 3.1800 | -0.9731 [-0.9738, -0.9724] | -30.6 % | 10 | yes | pass |
| footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu | 31.1598 | 4.1647 | 26.9941 [26.9783, 27.0083] | +648.2 % | 10 | yes | pass |
| footprint-mib=1024,k=1,kernel=k2,placement=cpu,working-set-mib=32 | 0.1001 | 0.1302 | -0.0301 [-0.0306, -0.0297] | -23.1 % | 10 | yes | pass |
| footprint-mib=1024,k=1,kernel=k2,placement=hbm,working-set-mib=32 | 0.0176 | 0.1194 | -0.1018 [-0.1021, -0.1014] | -85.3 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,rotated=1,working-set-mib=8 | 0.3731 | 0.0766 | 0.2967 [0.2958, 0.2971] | +387.4 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=1024 | 46.7128 | 8.0761 | 38.6371 [38.6185, 38.6468] | +478.4 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=32 | 1.4975 | 0.1880 | 1.3096 [1.3084, 1.3102] | +696.5 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=8 | 0.0377 | 0.0613 | -0.0236 [-0.0238, -0.0235] | -38.5 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,rotated=1,working-set-mib=8 | 0.0303 | 0.0750 | -0.0447 [-0.0448, -0.0445] | -59.6 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=32 | 0.0992 | 0.1815 | -0.0823 [-0.0826, -0.0819] | -45.3 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=8 | 0.0160 | 0.0586 | -0.0426 [-0.0426, -0.0424] | -72.7 % | 10 | yes | pass |
| footprint-mib=1024,k=2,kernel=k2,placement=cpu,working-set-mib=32 | 0.1928 | 0.1314 | 0.0613 [0.0611, 0.0618] | +46.6 % | 10 | yes | pass |
| footprint-mib=1024,k=2,kernel=k2,placement=hbm,working-set-mib=32 | 0.0234 | 0.1241 | -0.1006 [-0.1009, -0.0996] | -81.1 % | 10 | yes | pass |
| footprint-mib=1024,k=4,kernel=k2,placement=cpu,working-set-mib=32 | 0.3744 | 0.1378 | 0.2365 [0.2364, 0.2370] | +171.7 % | 10 | yes | pass |
| footprint-mib=1024,k=4,kernel=k2,placement=hbm,working-set-mib=32 | 0.0339 | 0.1326 | -0.0987 [-0.0991, -0.0986] | -74.4 % | 10 | yes | pass |
| footprint-mib=1024,k=64,kernel=k2,placement=hbm,working-set-mib=32 | 0.3411 | 0.3744 | -0.0333 [-0.0339, -0.0324] | -8.9 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k3,placement=cpu | 5.3779 | 3.3910 | 1.9868 [1.9861, 1.9881] | +58.6 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=cpu,update=atomic | 6.0446 | 7.3411 | -1.2952 [-1.3041, -1.2864] | -17.6 % | 10 | yes | pass |
| footprint-mib=11520,kernel=k3,placement=cpu | 239.7712 | 32.5913 | 207.1762 [207.0536, 207.2942] | +635.7 % | 10 | yes | pass |
| footprint-mib=1536,kernel=k3,placement=cpu | 5.3794 | 4.8241 | 0.5552 [0.5533, 0.5565] | +11.5 % | 10 | yes | pass |
| footprint-mib=16,kernel=k6,placement=hbm,update=atomic | 0.0752 | 0.1862 | -0.1110 [-0.1111, -0.1105] | -59.6 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,placement=cpu | 432.7576 | 46.2056 | 386.5545 [386.4594, 386.6122] | +836.6 % | 10 | yes | pass |
| footprint-mib=2048,kernel=k3,placement=cpu | 5.3793 | 6.2514 | -0.8718 [-0.8741, -0.8700] | -13.9 % | 10 | yes | pass |
| footprint-mib=24576,kernel=k3,placement=cpu | 597.3886 | 69.3364 | 528.0288 [527.9586, 528.0751] | +761.5 % | 10 | yes | pass |
| footprint-mib=256,generator=uniform,kernel=k4,placement=cpu | 7.3951 | 0.9992 | 6.3951 [6.3927, 6.4023] | +640.0 % | 10 | yes | pass |
| footprint-mib=256,generator=uniform,kernel=k4,placement=hbm | 0.2118 | 0.8877 | -0.6759 [-0.6765, -0.6754] | -76.1 % | 10 | yes | pass |
| footprint-mib=256,kernel=k3,placement=cpu | 5.3734 | 1.1889 | 4.1842 [4.1833, 4.1853] | +351.9 % | 10 | yes | pass |
| footprint-mib=256,kernel=k3,placement=hbm | 0.4254 | 1.0810 | -0.6555 [-0.6563, -0.6550] | -60.6 % | 10 | yes | pass |
| footprint-mib=256,kernel=k6,placement=cpu,update=atomic | 1.4867 | 1.8497 | -0.3632 [-0.3645, -0.3619] | -19.6 % | 10 | yes | pass |
| footprint-mib=32768,kernel=k3,placement=cpu | 685.0266 | 92.8096 | 592.2302 [592.1306, 592.3278] | +638.1 % | 10 | yes | pass |
| footprint-mib=4096,kernel=k3,placement=cpu | 5.5788 | 11.8971 | -6.3172 [-6.3626, -6.3061] | -53.1 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=1,tiling=tiles | 3.9341 | 3.6823 | 0.2523 [0.2495, 0.2548] | +6.9 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=16,tiling=tiles | 62.3641 | 9.6993 | 52.6559 [52.6332, 52.6856] | +542.9 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=2,tiling=tiles | 7.7904 | 4.0837 | 3.7062 [3.6980, 3.7095] | +90.8 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=4,tiling=tiles | 15.5423 | 4.8895 | 10.6526 [10.6399, 10.6628] | +217.9 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=64,tiling=tiles | 248.6472 | 29.0410 | 219.6114 [219.5447, 219.6839] | +756.2 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=none | 46.9159 | 6.0124 | 40.9032 [40.8590, 40.9380] | +680.3 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles | 31.1861 | 6.4874 | 24.6952 [24.6671, 24.7116] | +380.7 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1,placement=cpu | 191.3093 | 12.3694 | 178.9399 [178.9383, 178.9433] | +1446.6 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1,placement=hbm | 12.2920 | 12.3629 | -0.0707 [-0.0715, -0.0692] | -0.6 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1024,placement=cpu | 12.4922 | 0.8407 | 11.6514 [11.6477, 11.6581] | +1385.9 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1024,placement=hbm | 0.7662 | 0.8349 | -0.0687 [-0.0695, -0.0682] | -8.2 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1048576,placement=cpu | 8.0557 | 0.2481 | 7.8076 [7.8050, 7.8093] | +3147.6 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1048576,placement=hbm | 0.1958 | 0.2445 | -0.0487 [-0.0489, -0.0483] | -19.9 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu | 7.7456 | 23.3169 | -15.5717 [-15.5741, -15.5586] | -66.8 % | 10 | yes | pass |

## Per cell

### route/copy=ce-pageable-1-256m-none-whole,footprint-mib=256,kernel=k3,placement=cpu

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 50.0 GB/s over the touched lines; buffer at 0x42c9c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 17 calls per interval; first call of an interval: copy-in 0.7604 ms, kernel 0.4265 ms, copy-out 0.0136 ms; source buffer at 0x42ca80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.368e+08 (256.0 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 0, copy 4114; multiplexed rows voided: 0

### route/copy=ce-registered-1-4m-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=1024

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 23.0 GB/s over the touched lines; buffer at 0x4de900000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 2.9169 ms, kernel 5.1482 ms, copy-out 0.0129 ms; source buffer at 0x4dea00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.718e+10 (2048.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.639e+04; multiplexed rows voided: 0

### route/copy=ce-registered-1-64m-pipe-touched,f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 8 passes per interval, 365.2 GB/s over the touched lines; buffer at 0x4eac40000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 8 calls per interval; first call of an interval: copy-in 2.7054 ms, kernel 0.0286 ms, copy-out 0.0131 ms; source buffer at 0x4ead40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 9.664e+08 (128.0 per touched line), copy 9.664e+08; SMMU translation requests per repetition: direct 0, copy 1.645e+04; multiplexed rows voided: 0

### route/copy=ce-registered-1-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=2,tiling=tiles

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 68.9 GB/s over the touched lines; buffer at 0x4cd580000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 1.5353 ms, kernel 0.4580 ms, copy-out 1.4426 ms; source buffer at 0x4cd680000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.606e+09 (382.8 per touched line), copy 5.378e+08; SMMU translation requests per repetition: direct 1.202e+04, copy 9686; multiplexed rows voided: 0

### route/copy=ce-registered-1-whole-none-whole,footprint-mib=16384,kernel=k3,placement=cpu

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x4f7d40000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 45.7167 ms, kernel 0.4998 ms, copy-out 0.0147 ms; source buffer at 0x4f8200000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 1.211e+08, copy 2.622e+05; multiplexed rows voided: 0

### route/copy=ce-registered-1-whole-none-whole,footprint-mib=4096,kernel=k3,placement=cpu

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 304.3 GB/s over the touched lines; buffer at 0x59a880000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 11.3953 ms, kernel 0.4772 ms, copy-out 0.0143 ms; source buffer at 0x59aa40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (40.7 per touched line), copy 4.295e+09; SMMU translation requests per repetition: direct 0, copy 6.556e+04; multiplexed rows voided: 0

### route/copy=ce-registered-1-whole-none-whole,footprint-mib=8192,kernel=k3,placement=cpu

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 245.3 GB/s over the touched lines; buffer at 0x57c440000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 22.7947 ms, kernel 0.4940 ms, copy-out 0.0145 ms; source buffer at 0x57c6c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (36.2 per touched line), copy 8.607e+09; SMMU translation requests per repetition: direct 4129, copy 1.311e+05; multiplexed rows voided: 0

### route/copy=ce-registered-2-256m-pipe-whole,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 371.0 GB/s over the touched lines; buffer at 0x4b9b80000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 11.4390 ms, kernel 0.0822 ms, copy-out 0.0149 ms; source buffer at 0x4b9d80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 4.295e+09 (128.0 per touched line), copy 4.295e+09; SMMU translation requests per repetition: direct 0, copy 6.556e+04; multiplexed rows voided: 0

### route/copy=ce-registered-2-64m-pipe-whole,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 7 passes per interval, 369.6 GB/s over the touched lines; buffer at 0x55ee80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9528 ms, kernel 0.0291 ms, copy-out 0.0146 ms; source buffer at 0x55ef80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+09 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/copy=ce-registered-2-64m-pipe-whole,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 28 passes per interval, 370.1 GB/s over the touched lines; buffer at 0x5f77c0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 26 calls per interval; first call of an interval: copy-in 0.7638 ms, kernel 0.0271 ms, copy-out 0.0144 ms; source buffer at 0x5f78c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.684e+08 (128.0 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 0, copy 4110; multiplexed rows voided: 0

### route/copy=ce-registered-2-64m-pipe-whole-kernel,footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 34.5 GB/s over the touched lines; buffer at 0x41b1c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 3.1661 ms, kernel 0.0848 ms, copy-out 0.0883 ms; source buffer at 0x41b300000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.196e+09 (381.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.783e+04; multiplexed rows voided: 0

### route/copy=ce-registered-2-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=1,tiling=tiles

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 137.0 GB/s over the touched lines; buffer at 0x592dc0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 1.5402 ms, kernel 0.0579 ms, copy-out 1.4438 ms; source buffer at 0x592ec0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.028e+08 (191.4 per touched line), copy 5.378e+08; SMMU translation requests per repetition: direct 3692, copy 9473; multiplexed rows voided: 0

### route/copy=ce-registered-2-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=16,tiling=tiles

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 8.6 GB/s over the touched lines; buffer at 0x5af900000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 1.5366 ms, kernel 6.0491 ms, copy-out 1.4426 ms; source buffer at 0x5afa00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.284e+10 (3062.3 per touched line), copy 5.378e+08; SMMU translation requests per repetition: direct 3.608e+04, copy 1.114e+04; multiplexed rows voided: 0

### route/copy=ce-registered-2-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=none

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 11.4 GB/s over the touched lines; buffer at 0x5d47c0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.5253 ms, kernel 2.4442 ms, copy-out 1.4406 ms; source buffer at 0x5d48c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.308e+10 (3117.8 per touched line), copy 5.378e+08; SMMU translation requests per repetition: direct 3.031e+04, copy 1.043e+04; multiplexed rows voided: 0

### route/copy=ce-registered-2-whole-none-whole,footprint-mib=1024,kernel=k3,placement=cpu

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 172.6 GB/s over the touched lines; buffer at 0x478640000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 2.9092 ms, kernel 0.4661 ms, copy-out 0.0141 ms; source buffer at 0x478740000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.641e+04; multiplexed rows voided: 0

### route/copy=ce-registered-2-whole-none-whole,footprint-mib=1536,kernel=k3,placement=cpu

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 220.5 GB/s over the touched lines; buffer at 0x563fc0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 4.3469 ms, kernel 0.4698 ms, copy-out 0.0142 ms; source buffer at 0x5640c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (57.9 per touched line), copy 1.611e+09; SMMU translation requests per repetition: direct 0, copy 2.46e+04; multiplexed rows voided: 0

### route/copy=ce-registered-2-whole-none-whole,footprint-mib=2048,kernel=k3,placement=cpu

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 252.3 GB/s over the touched lines; buffer at 0x47a480000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 5.7620 ms, kernel 0.4734 ms, copy-out 0.0175 ms; source buffer at 0x47a5c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (50.6 per touched line), copy 2.147e+09; SMMU translation requests per repetition: direct 0, copy 3.279e+04; multiplexed rows voided: 0

### route/copy=ce-registered-2-whole-none-whole-kernel,footprint-mib=1024,kernel=k6,placement=cpu,update=atomic

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 177.5 GB/s over the touched lines; buffer at 0x45de80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 2.9226 ms, kernel 0.8043 ms, copy-out 2.8871 ms; source buffer at 0x45df80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 4209, copy 2.072e+04; multiplexed rows voided: 0

### route/copy=ce-registered-4-64m-pipe-touched,f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 10 passes per interval, 364.8 GB/s over the touched lines; buffer at 0x5844c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 9 calls per interval; first call of an interval: copy-in 2.2530 ms, kernel 0.0243 ms, copy-out 0.0115 ms; source buffer at 0x584580000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.053e+08 (128.0 per touched line), copy 8.053e+08; SMMU translation requests per repetition: direct 0, copy 1.732e+04; multiplexed rows voided: 0

### route/copy=ce-registered-4-64m-pipe-whole-kernel,footprint-mib=256,generator=uniform,kernel=k4,placement=cpu

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 36.3 GB/s over the touched lines; buffer at 0x45e2c0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 23 calls per interval; first call of an interval: copy-in 0.8177 ms, kernel 0.0633 ms, copy-out 0.0252 ms; source buffer at 0x45e3c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 7.688e+08 (366.6 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 0, copy 4410; multiplexed rows voided: 0

### route/copy=ce-registered-4-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=4,tiling=tiles

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 34.4 GB/s over the touched lines; buffer at 0x4e9440000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 1.5252 ms, kernel 1.2579 ms, copy-out 1.4440 ms; source buffer at 0x4e9540000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.211e+09 (765.6 per touched line), copy 5.378e+08; SMMU translation requests per repetition: direct 1.801e+04, copy 9991; multiplexed rows voided: 0

### route/copy=ce-registered-4-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=64,tiling=tiles

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 2.2 GB/s over the touched lines; buffer at 0x50c180000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 1.5389 ms, kernel 25.2853 ms, copy-out 1.4431 ms; source buffer at 0x50c280000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.138e+10 (12249.0 per touched line), copy 5.378e+08; SMMU translation requests per repetition: direct 3.601e+04, copy 1.704e+04; multiplexed rows voided: 0

### route/copy=ce-registered-4-64m-pipe-whole-kernel,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 17.3 GB/s over the touched lines; buffer at 0x4a8bc0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.5334 ms, kernel 2.8645 ms, copy-out 1.4427 ms; source buffer at 0x4a8cc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.1 per touched line), copy 5.378e+08; SMMU translation requests per repetition: direct 3.606e+04, copy 1.042e+04; multiplexed rows voided: 0

### route/copy=ce-registered-4-whole-none-whole,footprint-mib=24576,kernel=k3,placement=cpu

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 3.4 GB/s over the touched lines; buffer at 0x4b3980000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 68.8147 ms, kernel 0.5062 ms, copy-out 0.0157 ms; source buffer at 0x4b4040000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (33.4 per touched line), copy 2.585e+10; SMMU translation requests per repetition: direct 1.671e+08, copy 3.932e+05; multiplexed rows voided: 0

### route/copy=ce-registered-4-whole-none-whole,footprint-mib=32768,kernel=k3,placement=cpu

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 3.0 GB/s over the touched lines; buffer at 0x58ce00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 92.1783 ms, kernel 0.5109 ms, copy-out 0.0143 ms; source buffer at 0x58d6c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (33.0 per touched line), copy 3.448e+10; SMMU translation requests per repetition: direct 1.912e+08, copy 5.243e+05; multiplexed rows voided: 0

### route/copy=kernel-pageable-1-256m-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1,placement=hbm

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x5e6c80000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 0.0145 ms, kernel 12.2908 ms, copy-out 0.0076 ms; source buffer at 0x5e6d00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-pageable-1-64m-none-touched,footprint-mib=1024,k=1,kernel=k2,placement=hbm,working-set-mib=32

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 1140 passes per interval, 1910.1 GB/s over the touched lines; buffer at 0x5cad40000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 402 calls per interval; first call of an interval: copy-in 0.0266 ms, kernel 0.0168 ms, copy-out 0.0109 ms; source buffer at 0x5cae00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-pageable-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=32

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.5 GB/s over the touched lines; buffer at 0x5bd9c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 110 calls per interval; first call of an interval: copy-in 0.1036 ms, kernel 0.0728 ms, copy-out 0.0136 ms; source buffer at 0x5bda80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.365e+08 (2047.6 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-pageable-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=8

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 529 passes per interval, 221.3 GB/s over the touched lines; buffer at 0x54f140000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 373 calls per interval; first call of an interval: copy-in 0.0344 ms, kernel 0.0154 ms, copy-out 0.0146 ms; source buffer at 0x54f240000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-pageable-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=8

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 1230 passes per interval, 514.6 GB/s over the touched lines; buffer at 0x5a1080000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 596 calls per interval; first call of an interval: copy-in 0.0144 ms, kernel 0.0156 ms, copy-out 0.0124 ms; source buffer at 0x5a11c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-pageable-1-whole-none-touched,footprint-mib=1024,k=4,kernel=k2,placement=hbm,working-set-mib=32

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 580 passes per interval, 969.8 GB/s over the touched lines; buffer at 0x4b2d00000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 334 calls per interval; first call of an interval: copy-in 0.0256 ms, kernel 0.0282 ms, copy-out 0.0129 ms; source buffer at 0x4b2e00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-pageable-1-whole-none-whole,footprint-mib=256,kernel=k3,placement=hbm

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 47 passes per interval, 628.9 GB/s over the touched lines; buffer at 0x5e4e40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 34 calls per interval; first call of an interval: copy-in 0.1601 ms, kernel 0.4341 ms, copy-out 0.0137 ms; source buffer at 0x5e4f00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-pageable-1-whole-none-whole-kernel,footprint-mib=256,generator=uniform,kernel=k4,placement=hbm

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 95 passes per interval, 1269.1 GB/s over the touched lines; buffer at 0x5c1940000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 53 calls per interval; first call of an interval: copy-in 0.1624 ms, kernel 0.2138 ms, copy-out 0.0078 ms; source buffer at 0x5c1a00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-16m-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=cpu,rotated=1,working-set-mib=8

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 54 passes per interval, 22.5 GB/s over the touched lines; buffer at 0x513a40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 295 calls per interval; first call of an interval: copy-in 0.0345 ms, kernel 0.0282 ms, copy-out 0.0104 ms; source buffer at 0x513b40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.341e+08 (2048.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-16m-none-whole-kernel,footprint-mib=16,kernel=k6,placement=hbm,update=atomic

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 252 passes per interval, 210.8 GB/s over the touched lines; buffer at 0x51b180000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 201 calls per interval; first call of an interval: copy-in 0.0180 ms, kernel 0.0829 ms, copy-out 0.0119 ms; source buffer at 0x51b240000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-16m-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1024,placement=cpu

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x5d4540000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 25 calls per interval; first call of an interval: copy-in 0.0360 ms, kernel 0.7680 ms, copy-out 0.0266 ms; source buffer at 0x5d4600000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-16m-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 1.0 GB/s over the touched lines; buffer at 0x4da980000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 87 calls per interval; first call of an interval: copy-in 0.0349 ms, kernel 0.1785 ms, copy-out 0.0268 ms; source buffer at 0x4daa00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-256m-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=hbm,rotated=1,working-set-mib=8

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 668 passes per interval, 279.7 GB/s over the touched lines; buffer at 0x4ca840000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 420 calls per interval; first call of an interval: copy-in 0.0138 ms, kernel 0.0284 ms, copy-out 0.0142 ms; source buffer at 0x4ca940000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-256m-none-whole-kernel,footprint-mib=256,kernel=k6,placement=cpu,update=atomic

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 179.0 GB/s over the touched lines; buffer at 0x55eb00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 12 calls per interval; first call of an interval: copy-in 0.7582 ms, kernel 0.2044 ms, copy-out 0.7201 ms; source buffer at 0x55ec00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 315.5, copy 431.7; multiplexed rows voided: 0

### route/copy=kernel-registered-1-4m-none-touched,footprint-mib=1024,k=64,kernel=k2,placement=hbm,working-set-mib=32

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 58 passes per interval, 95.3 GB/s over the touched lines; buffer at 0x54fb40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 67 calls per interval; first call of an interval: copy-in 0.0249 ms, kernel 0.2711 ms, copy-out 0.0120 ms; source buffer at 0x54fc00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-64m-none-touched,footprint-mib=1024,k=2,kernel=k2,placement=cpu,working-set-mib=32

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 105 passes per interval, 175.1 GB/s over the touched lines; buffer at 0x5209c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 161 calls per interval; first call of an interval: copy-in 0.1033 ms, kernel 0.0164 ms, copy-out 0.0120 ms; source buffer at 0x520ac0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.708e+07 (256.0 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-64m-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1024,placement=hbm

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 27 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x537500000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 26 calls per interval; first call of an interval: copy-in 0.0142 ms, kernel 0.7676 ms, copy-out 0.0079 ms; source buffer at 0x5375c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-whole-none-touched,footprint-mib=1024,k=1,kernel=k2,placement=cpu,working-set-mib=32

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 202 passes per interval, 336.9 GB/s over the touched lines; buffer at 0x5dde00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 165 calls per interval; first call of an interval: copy-in 0.1055 ms, kernel 0.0125 ms, copy-out 0.0141 ms; source buffer at 0x5ddf00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.354e+07 (128.0 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-whole-none-touched,footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=32

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 214 passes per interval, 342.9 GB/s over the touched lines; buffer at 0x495c40000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 183 calls per interval; first call of an interval: copy-in 0.0257 ms, kernel 0.0765 ms, copy-out 0.0108 ms; source buffer at 0x495d40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-whole-none-touched,footprint-mib=1024,k=2,kernel=k2,placement=hbm,working-set-mib=32

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 849 passes per interval, 1420.9 GB/s over the touched lines; buffer at 0x5e1f40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 366 calls per interval; first call of an interval: copy-in 0.0254 ms, kernel 0.0206 ms, copy-out 0.0143 ms; source buffer at 0x5e2000000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-whole-none-touched,footprint-mib=1024,k=4,kernel=k2,placement=cpu,working-set-mib=32

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 54 passes per interval, 89.3 GB/s over the touched lines; buffer at 0x420ec0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 149 calls per interval; first call of an interval: copy-in 0.1047 ms, kernel 0.0246 ms, copy-out 0.0127 ms; source buffer at 0x420f80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.342e+08 (512.0 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-whole-none-whole,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 254 passes per interval, 3405.5 GB/s over the touched lines; buffer at 0x454880000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 79 calls per interval; first call of an interval: copy-in 0.1610 ms, kernel 0.0869 ms, copy-out 0.0126 ms; source buffer at 0x454940000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-whole-none-whole,footprint-mib=11520,kernel=k3,placement=cpu

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 8.2 GB/s over the touched lines; buffer at 0x4441c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 31.8461 ms, kernel 0.4945 ms, copy-out 0.0152 ms; source buffer at 0x444540000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.9 per touched line), copy 1.208e+10; SMMU translation requests per repetition: direct 6.725e+07, copy 1.928e+05; multiplexed rows voided: 0

### route/copy=kernel-registered-1-whole-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1,placement=cpu

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x5ad240000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 0.0359 ms, kernel 12.2916 ms, copy-out 0.0266 ms; source buffer at 0x5ad2c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/copy=kernel-registered-1-whole-none-whole-kernel,footprint-mib=8,kernel=k6,keys=1048576,placement=hbm

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 112 passes per interval, 46.9 GB/s over the touched lines; buffer at 0x58b700000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 105 calls per interval; first call of an interval: copy-in 0.0143 ms, kernel 0.1791 ms, copy-out 0.0077 ms; source buffer at 0x58b7c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 7 passes per interval, 368.6 GB/s over the touched lines; buffer at 0x4e2880000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9193 ms, kernel 0.2975 ms, copy-out 0.0141 ms; source buffer at 0x4e2980000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+09 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 28 passes per interval, 368.1 GB/s over the touched lines; buffer at 0x5e6540000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 24 calls per interval; first call of an interval: copy-in 0.7550 ms, kernel 0.0819 ms, copy-out 0.0113 ms; source buffer at 0x5e6640000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.684e+08 (128.0 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 0, copy 4110; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 255 passes per interval, 3419.1 GB/s over the touched lines; buffer at 0x4e0540000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 28 calls per interval; first call of an interval: copy-in 0.6480 ms, kernel 0.0817 ms, copy-out 0.0124 ms; source buffer at 0x4e0600000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 4111; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 371.0 GB/s over the touched lines; buffer at 0x5da900000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 11.3927 ms, kernel 1.1670 ms, copy-out 0.0147 ms; source buffer at 0x5daa80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 4.295e+09 (128.0 per touched line), copy 4.295e+09; SMMU translation requests per repetition: direct 0, copy 6.556e+04; multiplexed rows voided: 0

### route/f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 8 passes per interval, 364.5 GB/s over the touched lines; buffer at 0x49ce00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9240 ms, kernel 0.2779 ms, copy-out 0.0152 ms; source buffer at 0x49cf00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 9.664e+08 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 10 passes per interval, 364.9 GB/s over the touched lines; buffer at 0x5d80c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9420 ms, kernel 0.2329 ms, copy-out 0.0127 ms; source buffer at 0x5d8180000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.053e+08 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 34.5 GB/s over the touched lines; buffer at 0x46fb80000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 2.9509 ms, kernel 1.1005 ms, copy-out 0.1199 ms; source buffer at 0x46fcc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.196e+09 (381.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.689e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=1,kernel=k2,placement=cpu,working-set-mib=32

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 198 passes per interval, 335.0 GB/s over the touched lines; buffer at 0x50fa40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 156 calls per interval; first call of an interval: copy-in 0.1080 ms, kernel 0.0149 ms, copy-out 0.0156 ms; source buffer at 0x50fb40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.354e+07 (128.0 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 533; multiplexed rows voided: 0

### route/footprint-mib=1024,k=1,kernel=k2,placement=hbm,working-set-mib=32

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 1151 passes per interval, 1905.4 GB/s over the touched lines; buffer at 0x52a740000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 171 calls per interval; first call of an interval: copy-in 0.0954 ms, kernel 0.0217 ms, copy-out 0.0133 ms; source buffer at 0x52a840000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 518.6; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,rotated=1,working-set-mib=8

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 54 passes per interval, 22.5 GB/s over the touched lines; buffer at 0x4fba80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 267 calls per interval; first call of an interval: copy-in 0.0392 ms, kernel 0.0301 ms, copy-out 0.0099 ms; source buffer at 0x4fbb80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.341e+08 (2048.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 0, copy 132.6; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=1024

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 23.0 GB/s over the touched lines; buffer at 0x4b56c0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 2.9146 ms, kernel 5.1494 ms, copy-out 0.0150 ms; source buffer at 0x4b57c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.718e+10 (2048.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.639e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=32

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.4 GB/s over the touched lines; buffer at 0x45b4c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 106 calls per interval; first call of an interval: copy-in 0.1057 ms, kernel 0.0755 ms, copy-out 0.0126 ms; source buffer at 0x45b5c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.365e+08 (2047.6 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 532.9; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=8

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 530 passes per interval, 222.3 GB/s over the touched lines; buffer at 0x5e8000000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 328 calls per interval; first call of an interval: copy-in 0.0404 ms, kernel 0.0163 ms, copy-out 0.0134 ms; source buffer at 0x5e8100000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 0, copy 132.6; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,rotated=1,working-set-mib=8

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 660 passes per interval, 277.0 GB/s over the touched lines; buffer at 0x41a000000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 268 calls per interval; first call of an interval: copy-in 0.0361 ms, kernel 0.0349 ms, copy-out 0.0144 ms; source buffer at 0x41a0c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 133.8; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=32

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 201 passes per interval, 338.1 GB/s over the touched lines; buffer at 0x40b2c0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 112 calls per interval; first call of an interval: copy-in 0.0946 ms, kernel 0.0827 ms, copy-out 0.0093 ms; source buffer at 0x40b380000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 518.8; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=8

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 1242 passes per interval, 523.6 GB/s over the touched lines; buffer at 0x54bcc0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 341 calls per interval; first call of an interval: copy-in 0.0358 ms, kernel 0.0200 ms, copy-out 0.0132 ms; source buffer at 0x54bd80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 134.8; multiplexed rows voided: 0

### route/footprint-mib=1024,k=2,kernel=k2,placement=cpu,working-set-mib=32

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 104 passes per interval, 174.0 GB/s over the touched lines; buffer at 0x550b40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 149 calls per interval; first call of an interval: copy-in 0.1082 ms, kernel 0.0188 ms, copy-out 0.0129 ms; source buffer at 0x550c40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.708e+07 (256.0 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 532.9; multiplexed rows voided: 0

### route/footprint-mib=1024,k=2,kernel=k2,placement=hbm,working-set-mib=32

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 857 passes per interval, 1430.2 GB/s over the touched lines; buffer at 0x578f40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 165 calls per interval; first call of an interval: copy-in 0.0949 ms, kernel 0.0257 ms, copy-out 0.0094 ms; source buffer at 0x579080000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 518.5; multiplexed rows voided: 0

### route/footprint-mib=1024,k=4,kernel=k2,placement=cpu,working-set-mib=32

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 53 passes per interval, 89.6 GB/s over the touched lines; buffer at 0x5384c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 143 calls per interval; first call of an interval: copy-in 0.1066 ms, kernel 0.0271 ms, copy-out 0.0138 ms; source buffer at 0x538580000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.342e+08 (512.0 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 533; multiplexed rows voided: 0

### route/footprint-mib=1024,k=4,kernel=k2,placement=hbm,working-set-mib=32

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 577 passes per interval, 988.7 GB/s over the touched lines; buffer at 0x4cfb40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 151 calls per interval; first call of an interval: copy-in 0.0947 ms, kernel 0.0338 ms, copy-out 0.0155 ms; source buffer at 0x4cfd00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 518.8; multiplexed rows voided: 0

### route/footprint-mib=1024,k=64,kernel=k2,placement=hbm,working-set-mib=32

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 63 passes per interval, 98.3 GB/s over the touched lines; buffer at 0x52ef00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 54 calls per interval; first call of an interval: copy-in 0.0953 ms, kernel 0.2787 ms, copy-out 0.0112 ms; source buffer at 0x52f000000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 518.9; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k3,placement=cpu

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 172.6 GB/s over the touched lines; buffer at 0x49af00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 2.9159 ms, kernel 0.4687 ms, copy-out 0.0146 ms; source buffer at 0x49b000000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.641e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=cpu,update=atomic

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 177.6 GB/s over the touched lines; buffer at 0x4a8c00000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 2.9287 ms, kernel 0.8098 ms, copy-out 3.6152 ms; source buffer at 0x4a8d00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 4182, copy 3.278e+04; multiplexed rows voided: 0

### route/footprint-mib=11520,kernel=k3,placement=cpu

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 8.2 GB/s over the touched lines; buffer at 0x440180000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 32.0739 ms, kernel 0.4998 ms, copy-out 0.0148 ms; source buffer at 0x4404c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.9 per touched line), copy 1.211e+10; SMMU translation requests per repetition: direct 6.714e+07, copy 1.843e+05; multiplexed rows voided: 0

### route/footprint-mib=1536,kernel=k3,placement=cpu

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 220.5 GB/s over the touched lines; buffer at 0x45dc80000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 4.3450 ms, kernel 0.4736 ms, copy-out 0.0142 ms; source buffer at 0x45dd80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (57.9 per touched line), copy 1.611e+09; SMMU translation requests per repetition: direct 0, copy 2.46e+04; multiplexed rows voided: 0

### route/footprint-mib=16,kernel=k6,placement=hbm,update=atomic

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 260 passes per interval, 223.0 GB/s over the touched lines; buffer at 0x459b00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 105 calls per interval; first call of an interval: copy-in 0.0568 ms, kernel 0.0784 ms, copy-out 0.0625 ms; source buffer at 0x459bc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 132.5; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x42cdc0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 45.6877 ms, kernel 0.5044 ms, copy-out 0.0130 ms; source buffer at 0x42d240000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 1.211e+08, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=2048,kernel=k3,placement=cpu

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 252.3 GB/s over the touched lines; buffer at 0x46c740000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 5.7693 ms, kernel 0.4761 ms, copy-out 0.0146 ms; source buffer at 0x46c880000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (50.6 per touched line), copy 2.147e+09; SMMU translation requests per repetition: direct 0, copy 3.279e+04; multiplexed rows voided: 0

### route/footprint-mib=24576,kernel=k3,placement=cpu

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 3.4 GB/s over the touched lines; buffer at 0x4bce80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 68.8129 ms, kernel 0.5092 ms, copy-out 0.0133 ms; source buffer at 0x4bd540000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (33.4 per touched line), copy 2.585e+10; SMMU translation requests per repetition: direct 1.671e+08, copy 3.932e+05; multiplexed rows voided: 0

### route/footprint-mib=256,generator=uniform,kernel=k4,placement=cpu

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 36.3 GB/s over the touched lines; buffer at 0x4f5ec0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 20 calls per interval; first call of an interval: copy-in 0.7588 ms, kernel 0.2125 ms, copy-out 0.0392 ms; source buffer at 0x4f5f40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 7.685e+08 (366.5 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 0, copy 4229; multiplexed rows voided: 0

### route/footprint-mib=256,generator=uniform,kernel=k4,placement=hbm

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 95 passes per interval, 1267.2 GB/s over the touched lines; buffer at 0x4b5500000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 23 calls per interval; first call of an interval: copy-in 0.6472 ms, kernel 0.2135 ms, copy-out 0.0360 ms; source buffer at 0x4b55c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 4228; multiplexed rows voided: 0

### route/footprint-mib=256,kernel=k3,placement=cpu

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 49.9 GB/s over the touched lines; buffer at 0x4f0500000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 17 calls per interval; first call of an interval: copy-in 0.7566 ms, kernel 0.4274 ms, copy-out 0.0132 ms; source buffer at 0x4f05c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.368e+08 (256.0 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 0, copy 4116; multiplexed rows voided: 0

### route/footprint-mib=256,kernel=k3,placement=hbm

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 47 passes per interval, 630.8 GB/s over the touched lines; buffer at 0x4a7540000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 19 calls per interval; first call of an interval: copy-in 0.6476 ms, kernel 0.4288 ms, copy-out 0.0121 ms; source buffer at 0x4a7600000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 4114; multiplexed rows voided: 0

### route/footprint-mib=256,kernel=k6,placement=cpu,update=atomic

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 180.6 GB/s over the touched lines; buffer at 0x4c6f00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 11 calls per interval; first call of an interval: copy-in 0.7522 ms, kernel 0.1971 ms, copy-out 0.9141 ms; source buffer at 0x4c6fc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 318.8, copy 8196; multiplexed rows voided: 0

### route/footprint-mib=32768,kernel=k3,placement=cpu

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 3.0 GB/s over the touched lines; buffer at 0x5c7d40000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 92.2763 ms, kernel 0.5181 ms, copy-out 0.0144 ms; source buffer at 0x5c8600000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (33.0 per touched line), copy 3.448e+10; SMMU translation requests per repetition: direct 1.912e+08, copy 5.243e+05; multiplexed rows voided: 0

### route/footprint-mib=4096,kernel=k3,placement=cpu

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 303.0 GB/s over the touched lines; buffer at 0x454f40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 11.4084 ms, kernel 0.4808 ms, copy-out 0.0147 ms; source buffer at 0x4550c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (40.7 per touched line), copy 4.295e+09; SMMU translation requests per repetition: direct 0, copy 6.556e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=1,tiling=tiles

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 136.5 GB/s over the touched lines; buffer at 0x460640000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 1.4732 ms, kernel 0.4142 ms, copy-out 1.8128 ms; source buffer at 0x460740000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.028e+08 (191.4 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3684, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=16,tiling=tiles

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 8.6 GB/s over the touched lines; buffer at 0x4d67c0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 1.4687 ms, kernel 6.4228 ms, copy-out 1.8142 ms; source buffer at 0x4d6900000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.284e+10 (3062.3 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.593e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=2,tiling=tiles

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 68.9 GB/s over the touched lines; buffer at 0x5dfe00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 1.4723 ms, kernel 0.8183 ms, copy-out 1.8144 ms; source buffer at 0x5dff00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.606e+09 (382.8 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 1.201e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=4,tiling=tiles

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 34.5 GB/s over the touched lines; buffer at 0x53a840000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 1.4686 ms, kernel 1.6216 ms, copy-out 1.8147 ms; source buffer at 0x53a940000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.211e+09 (765.6 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 1.798e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=64,tiling=tiles

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 2.2 GB/s over the touched lines; buffer at 0x4129c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 1.4721 ms, kernel 25.7505 ms, copy-out 1.8134 ms; source buffer at 0x412ac0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.138e+10 (12249.0 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.595e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=none

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 11.4 GB/s over the touched lines; buffer at 0x457c00000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.4682 ms, kernel 2.7432 ms, copy-out 1.8154 ms; source buffer at 0x457d40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.307e+10 (3116.8 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.028e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 17.2 GB/s over the touched lines; buffer at 0x54da00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.4682 ms, kernel 3.2243 ms, copy-out 1.8154 ms; source buffer at 0x54db00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.1 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.607e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1,placement=cpu

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x55ac00000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 0.0394 ms, kernel 12.2933 ms, copy-out 0.0384 ms; source buffer at 0x55acc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1,placement=hbm

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x4573c0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 0.0357 ms, kernel 12.2937 ms, copy-out 0.0372 ms; source buffer at 0x457480000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1024,placement=cpu

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x4b7500000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 24 calls per interval; first call of an interval: copy-in 0.0392 ms, kernel 0.7704 ms, copy-out 0.0396 ms; source buffer at 0x4b7580000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1024,placement=hbm

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 27 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x53a340000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 25 calls per interval; first call of an interval: copy-in 0.0363 ms, kernel 0.7704 ms, copy-out 0.0381 ms; source buffer at 0x53a3c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1048576,placement=cpu

- first variant A, seed 103; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 1.0 GB/s over the touched lines; buffer at 0x4e4800000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 81 calls per interval; first call of an interval: copy-in 0.0395 ms, kernel 0.1804 ms, copy-out 0.0407 ms; source buffer at 0x4e48c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1048576,placement=hbm

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 111 passes per interval, 42.9 GB/s over the touched lines; buffer at 0x55b1c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 83 calls per interval; first call of an interval: copy-in 0.0357 ms, kernel 0.1825 ms, copy-out 0.0392 ms; source buffer at 0x55b280000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu

- first variant B, seed 103; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 245.3 GB/s over the touched lines; buffer at 0x587c80000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 22.8028 ms, kernel 0.4968 ms, copy-out 0.0148 ms; source buffer at 0x587f00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (36.2 per touched line), copy 8.607e+09; SMMU translation requests per repetition: direct 4118, copy 1.311e+05; multiplexed rows voided: 0

