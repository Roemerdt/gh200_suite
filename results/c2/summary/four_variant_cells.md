# Four-variant cells: direct and copy route at home and at a level of one factor, recomputed from raw rows

Times are per repetition in ms (one pass for the direct route, one complete call for the copy route). Each round runs the four variants once in the order the seed drew; the route difference at home (A - B) and at the level (C - D) and the change of the route difference, (C - D) - (A - B), are formed within each round and given as median with 95 % rank interval. A negative route difference means direct access is faster; a negative change means the level moved the comparison towards direct access. The relative change is the change over the route difference at home, given only where that difference excludes zero. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | level | direct home ms | copy home ms | direct level ms | copy level ms | route difference home ms [interval] | route difference level ms [interval] | change ms [interval] | relative change | rounds | change excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| at=1,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0302 | 0.0532 | 0.0300 | 0.0527 | -0.0230 [-0.0232, -0.0229] | -0.0228 [-0.0230, -0.0224] | 0.0003 [0.0001, 0.0006] | -1.3 % | 10 | yes | pass |
| at=1,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=four,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0090 | 0.0504 | 0.0091 | 0.0504 | -0.0414 [-0.0415, -0.0412] | -0.0413 [-0.0415, -0.0411] | 0.0000 [-0.0002, 0.0002] | -0.1 % | 20 | no | pass |
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=k,working-set-mib=32 | k | 1 | 1.5011 | 0.1834 | 0.1000 | 0.1232 | 1.3175 [1.3168, 1.3183] | -0.0232 [-0.0233, -0.0230] | -1.3407 [-1.3414, -1.3402] | -101.8 % | 10 | yes | pass |
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0378 | 0.0608 | 0.3696 | 0.0752 | -0.0230 [-0.0232, -0.0221] | 0.2943 [0.2938, 0.2947] | 0.3171 [0.3165, 0.3177] | -1380.2 % | 10 | yes | pass |
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=four,vary=k,working-set-mib=32 | k | 1 | 0.0973 | 0.1790 | 0.0175 | 0.1192 | -0.0817 [-0.0820, -0.0814] | -0.1017 [-0.1018, -0.1016] | -0.0200 [-0.0203, -0.0198] | +24.5 % | 20 | yes | pass |
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=four,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0160 | 0.0582 | 0.0301 | 0.0748 | -0.0422 [-0.0423, -0.0421] | -0.0447 [-0.0449, -0.0445] | -0.0025 [-0.0027, -0.0023] | +6.0 % | 20 | yes | pass |
| at=1,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0311 | 0.0540 | 0.0532 | 0.0546 | -0.0230 [-0.0231, -0.0228] | -0.0014 [-0.0015, -0.0012] | 0.0216 [0.0215, 0.0218] | -94.2 % | 10 | yes | pass |
| at=1,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=four,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0093 | 0.0499 | 0.0102 | 0.0500 | -0.0407 [-0.0408, -0.0405] | -0.0398 [-0.0398, -0.0397] | 0.0009 [0.0007, 0.0011] | -2.1 % | 20 | yes | pass |
| at=1,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0319 | 0.0548 | 0.0988 | 0.0584 | -0.0229 [-0.0232, -0.0225] | 0.0404 [0.0400, 0.0407] | 0.0633 [0.0628, 0.0639] | -276.9 % | 10 | yes | pass |
| at=1,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=four,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0104 | 0.0503 | 0.0132 | 0.0584 | -0.0399 [-0.0401, -0.0398] | -0.0453 [-0.0454, -0.0452] | -0.0054 [-0.0059, -0.0053] | +13.6 % | 40 | yes | pass |
| at=1,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0607 | 0.0849 | 1.4490 | 0.1344 | -0.0242 [-0.0246, -0.0237] | 1.3144 [1.3091, 1.3191] | 1.3386 [1.3326, 1.3434] | -5540.1 % | 10 | yes | pass |
| at=1,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=four,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0388 | 0.0838 | 0.0910 | 0.1340 | -0.0450 [-0.0451, -0.0448] | -0.0430 [-0.0433, -0.0427] | 0.0020 [0.0018, 0.0023] | -4.3 % | 10 | yes | pass |
| at=1,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sweeps | sweeps | 1 | 26.3164 | 6.5105 | 3.0856 | 3.6271 | 19.8044 [19.7833, 19.8164] | -0.5443 [-0.5475, -0.5358] | -20.3501 [-20.3595, -20.3195] | -102.8 % | 10 | yes | pass |
| at=1,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sweeps | sweeps | 1 | 3.2764 | 3.8735 | 0.3978 | 1.0451 | -0.5966 [-0.6044, -0.5910] | -0.6473 [-0.6479, -0.6460] | -0.0503 [-0.0554, -0.0429] | +8.4 % | 10 | yes | pass |
| at=16384,footprint-mib=1024,kernel=k3,placement=cpu,type=four,vary=footprint | footprint | 16384 | 5.3850 | 3.4128 | 432.8167 | 44.8026 | 1.9718 [1.9589, 1.9736] | 388.0162 [387.9290, 388.0822] | 386.0537 [385.9578, 386.1233] | +19578.6 % | 10 | yes | pass |
| at=16384,footprint-mib=1024,kernel=k3,placement=hbm,type=four,vary=footprint | footprint | 16384 | 0.4677 | 1.1211 | 425.0927 | 10.6295 | -0.6539 [-0.6546, -0.6525] | 414.4151 [414.2402, 414.6741] | 415.0677 [414.8951, 415.3280] | -63474.6 % | 10 | yes | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=f | f | 1of100 | 2.9124 | 3.2761 | 0.0384 | 0.0532 | -0.3641 [-0.3649, -0.3622] | -0.0148 [-0.0148, -0.0146] | 0.3493 [0.3475, 0.3503] | -95.9 % | 10 | yes | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=four,vary=f | f | 1of100 | 0.2982 | 0.9463 | 0.0103 | 0.0327 | -0.6482 [-0.6489, -0.6465] | -0.0224 [-0.0227, -0.0224] | 0.6257 [0.6240, 0.6265] | -96.5 % | 10 | yes | pass |
| at=2g,footprint-mib=11520,kernel=k3,placement=cpu,type=four,vary=partition | partition | 2g | 240.0515 | 32.8839 | 5.6745 | 31.0896 | 207.1706 [206.7574, 207.3031] | -25.4160 [-25.4245, -25.4042] | -232.5722 [-232.7074, -232.1819] | -112.3 % | 10 | yes | pass |
| at=2g,footprint-mib=12288,kernel=k3,placement=cpu,type=four,vary=partition | partition | 2g | 279.2898 | 34.8461 | 5.6740 | 33.0171 | 244.4458 [244.3951, 244.5323] | -27.3428 [-27.3495, -27.3336] | -271.8476 [-271.8745, -271.7766] | -111.2 % | 20 | yes | pass |
| at=2g,footprint-mib=12288,kernel=k3,placement=hbm,type=four,vary=partition | partition | 2g | 284.8781 | 8.0946 | 165.4890 | 8.2653 | 276.7863 [276.7333, 276.8556] | 157.2258 [155.8040, 158.3826] | -119.2500 [-120.5717, -117.3079] | -43.1 % | 20 | yes | pass |
| at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=partition | partition | 2g | 432.8717 | 46.2716 | 5.8492 | 42.9827 | 386.5708 [386.5365, 386.6452] | -37.1394 [-37.1584, -37.0639] | -423.6733 [-423.7443, -423.5673] | -109.6 % | 30 | yes | pass |
| at=2g,footprint-mib=24576,kernel=k3,placement=cpu,type=four,vary=partition | partition | 2g | 598.4864 | 65.9786 | 6.7221 | 63.9245 | 532.4605 [532.4393, 532.5107] | -57.2051 [-57.2665, -57.1121] | -589.5819 [-589.7466, -589.4958] | -110.7 % | 70 | yes | pass |
| at=2g,footprint-mib=32768,kernel=k3,placement=cpu,type=four,vary=partition | partition | 2g | 685.1368 | 86.5676 | 11.7753 | 85.1873 | 598.5657 [598.5512, 598.5919] | -73.4009 [-73.8355, -73.0042] | -671.7768 [-672.3632, -671.4593] | -112.2 % | 100 | yes | pass |
| at=2g,footprint-mib=4096,kernel=k3,placement=cpu,type=four,vary=partition | partition | 2g | 5.5591 | 11.9509 | 5.5449 | 12.1252 | -6.3856 [-6.4438, -6.3567] | -6.5798 [-6.5879, -6.5773] | -0.1973 [-0.2229, -0.1350] | +3.1 % | 10 | yes | pass |
| at=2g,footprint-mib=4096,kernel=k3,placement=hbm,type=four,vary=partition | partition | 2g | 5.1811 | 3.0264 | 3.7404 | 3.2013 | 2.1548 [2.0935, 2.1580] | 0.5393 [0.5134, 0.5694] | -1.6081 [-1.6411, -1.5460] | -74.6 % | 10 | yes | pass |
| at=2g,footprint-mib=8192,kernel=k3,placement=cpu,type=four,vary=partition | partition | 2g | 7.8882 | 23.6507 | 5.5802 | 22.7461 | -15.8287 [-15.9031, -15.7543] | -17.1718 [-17.1938, -17.1552] | -1.3330 [-1.4241, -1.2688] | +8.4 % | 10 | yes | pass |
| at=2g,footprint-mib=8192,kernel=k3,placement=hbm,type=four,vary=partition | partition | 2g | 7.8239 | 5.5592 | 5.8381 | 5.7423 | 2.2653 [2.2527, 2.2734] | 0.0955 [0.0736, 0.1496] | -2.1698 [-2.1826, -2.1141] | -95.8 % | 10 | yes | pass |
| at=2g,footprint-mib=9728,kernel=k3,placement=cpu,type=four,vary=partition | partition | 2g | 128.2513 | 27.3509 | 5.6577 | 27.5202 | 100.9030 [100.8306, 101.0183] | -21.8628 [-21.8726, -21.8152] | -122.7589 [-122.8813, -122.6961] | -121.7 % | 10 | yes | pass |
| at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-order | page-order | 2m | 432.8162 | 46.2907 | 5.3779 | 42.7093 | 386.5367 [386.4782, 386.6583] | -37.3315 [-37.3370, -37.3251] | -423.8668 [-424.0119, -423.8077] | -109.7 % | 10 | yes | pass |
| at=512m,footprint-mib=1024,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 5.3687 | 3.4194 | 5.3300 | 3.1225 | 1.9495 [1.9479, 1.9505] | 2.2075 [2.2061, 2.2080] | 0.2580 [0.2559, 0.2600] | +13.2 % | 10 | yes | pass |
| at=512m,footprint-mib=1024,kernel=k3,placement=hbm,type=four,vary=page-size | page-size | 512m | 0.4654 | 1.1186 | 0.4648 | 1.1148 | -0.6532 [-0.6543, -0.6523] | -0.6499 [-0.6511, -0.6488] | 0.0037 [0.0020, 0.0045] | -0.6 % | 10 | yes | pass |
| at=512m,footprint-mib=11520,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 239.7232 | 32.7386 | 5.3828 | 30.1317 | 206.9838 [206.8681, 207.0494] | -24.7486 [-24.7597, -24.7441] | -231.7386 [-231.7941, -231.6114] | -112.0 % | 10 | yes | pass |
| at=512m,footprint-mib=12288,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 279.5318 | 34.9162 | 5.3825 | 32.1057 | 244.6096 [244.4449, 244.7103] | -26.7250 [-26.7356, -26.7177] | -271.3382 [-271.4439, -271.1673] | -110.9 % | 10 | yes | pass |
| at=512m,footprint-mib=1536,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 5.3702 | 4.8066 | 5.3484 | 4.4440 | 0.5635 [0.5626, 0.5671] | 0.9043 [0.9034, 0.9056] | 0.3413 [0.3370, 0.3428] | +60.6 % | 10 | yes | pass |
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 432.7329 | 46.4995 | 5.3847 | 42.6342 | 386.2334 [386.1596, 386.3565] | -37.2521 [-37.2589, -37.2368] | -423.4932 [-423.5981, -423.4061] | -109.6 % | 10 | yes | pass |
| at=512m,footprint-mib=16384,kernel=k3p,placement=cpu,type=four,vary=page-size | page-size | 512m | 7.0316 | 46.3169 | 0.0995 | 42.1951 | -39.2819 [-39.2916, -39.2763] | -42.0956 [-42.1031, -42.0881] | -2.8120 [-2.8241, -2.7953] | +7.2 % | 10 | yes | pass |
| at=512m,footprint-mib=2048,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 5.3716 | 6.2281 | 5.3566 | 5.7638 | -0.8567 [-0.8583, -0.8554] | -0.4072 [-0.4105, -0.4062] | 0.4484 [0.4466, 0.4495] | -52.3 % | 30 | yes | pass |
| at=512m,footprint-mib=24576,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 598.2695 | 65.6629 | 5.3878 | 63.6880 | 532.6095 [532.4835, 532.6806] | -58.3032 [-58.3213, -58.2854] | -590.9212 [-590.9959, -590.8297] | -110.9 % | 10 | yes | pass |
| at=512m,footprint-mib=256,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 5.3653 | 1.2049 | 5.1756 | 1.1069 | 4.1607 [4.1593, 4.1613] | 4.0689 [4.0682, 4.0694] | -0.0919 [-0.0927, -0.0899] | -2.2 % | 10 | yes | pass |
| at=512m,footprint-mib=256,kernel=k3,placement=hbm,type=four,vary=page-size | page-size | 512m | 0.4278 | 1.0811 | 0.4243 | 1.0805 | -0.6533 [-0.6534, -0.6528] | -0.6561 [-0.6571, -0.6554] | -0.0032 [-0.0038, -0.0020] | +0.5 % | 10 | yes | pass |
| at=512m,footprint-mib=32768,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 685.0753 | 85.9678 | 5.3904 | 84.7344 | 599.0979 [599.0396, 599.1357] | -79.3479 [-79.3638, -79.3419] | -678.4491 [-678.4963, -678.3803] | -113.2 % | 20 | yes | pass |
| at=512m,footprint-mib=4096,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 5.5040 | 11.9964 | 5.3707 | 11.0356 | -6.4912 [-6.5204, -6.4587] | -5.6645 [-5.6666, -5.6604] | 0.8211 [0.7886, 0.8559] | -12.6 % | 10 | yes | pass |
| at=512m,footprint-mib=4096,kernel=k3,placement=hbm,type=four,vary=page-size | page-size | 512m | 5.1328 | 3.0417 | 0.4754 | 3.0353 | 2.0885 [2.0789, 2.0990] | -2.5597 [-2.5621, -2.5538] | -4.6472 [-4.6584, -4.6317] | -222.5 % | 10 | yes | pass |
| at=512m,footprint-mib=8192,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 7.7570 | 23.4925 | 5.3796 | 21.5859 | -15.7348 [-15.7488, -15.7305] | -16.2066 [-16.2084, -16.2022] | -0.4707 [-0.4742, -0.4585] | +3.0 % | 10 | yes | pass |
| at=512m,footprint-mib=8192,kernel=k3,placement=hbm,type=four,vary=page-size | page-size | 512m | 7.8108 | 5.5896 | 0.4770 | 5.5663 | 2.2142 [2.1071, 2.2289] | -5.0895 [-5.1129, -5.0809] | -7.3093 [-7.3291, -7.2013] | -330.1 % | 10 | yes | pass |
| at=512m,footprint-mib=9728,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 128.4394 | 27.3750 | 5.3810 | 26.7701 | 101.0553 [100.9925, 101.1210] | -21.3896 [-21.4574, -21.3529] | -122.4570 [-122.5683, -122.3720] | -121.2 % | 10 | yes | pass |
| at=8,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 0.1004 | 0.1309 | 0.0298 | 0.0533 | -0.0305 [-0.0310, -0.0302] | -0.0236 [-0.0239, -0.0232] | 0.0070 [0.0063, 0.0074] | -23.1 % | 10 | yes | pass |
| at=8,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 0.0176 | 0.1196 | 0.0089 | 0.0506 | -0.1021 [-0.1022, -0.1018] | -0.0416 [-0.0417, -0.0416] | 0.0604 [0.0600, 0.0605] | -59.2 % | 50 | yes | pass |
| at=8,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 1.5005 | 0.1826 | 0.0375 | 0.0606 | 1.3180 [1.3170, 1.3186] | -0.0231 [-0.0233, -0.0227] | -1.3409 [-1.3416, -1.3401] | -101.7 % | 10 | yes | pass |
| at=8,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 0.0975 | 0.1810 | 0.0160 | 0.0582 | -0.0835 [-0.0837, -0.0833] | -0.0422 [-0.0423, -0.0420] | 0.0413 [0.0412, 0.0416] | -49.5 % | 20 | yes | pass |
| at=8,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 0.1936 | 0.1320 | 0.0308 | 0.0536 | 0.0616 [0.0612, 0.0619] | -0.0228 [-0.0229, -0.0226] | -0.0844 [-0.0848, -0.0840] | -137.0 % | 10 | yes | pass |
| at=8,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 0.0233 | 0.1244 | 0.0093 | 0.0501 | -0.1011 [-0.1021, -0.1010] | -0.0408 [-0.0409, -0.0408] | 0.0603 [0.0598, 0.0613] | -59.6 % | 10 | yes | pass |
| at=8,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 0.3770 | 0.1424 | 0.0315 | 0.0545 | 0.2346 [0.2342, 0.2348] | -0.0230 [-0.0232, -0.0229] | -0.2576 [-0.2578, -0.2573] | -109.8 % | 10 | yes | pass |
| at=8,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 0.0341 | 0.1336 | 0.0103 | 0.0502 | -0.0995 [-0.0997, -0.0994] | -0.0399 [-0.0400, -0.0398] | 0.0597 [0.0594, 0.0599] | -60.0 % | 20 | yes | pass |
| at=8,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 5.9750 | 0.3842 | 0.0603 | 0.0847 | 5.5908 [5.5840, 5.6001] | -0.0243 [-0.0246, -0.0242] | -5.6154 [-5.6244, -5.6083] | -100.4 % | 10 | yes | pass |
| at=8,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 0.3451 | 0.3745 | 0.0388 | 0.0837 | -0.0293 [-0.0298, -0.0291] | -0.0449 [-0.0451, -0.0448] | -0.0157 [-0.0164, -0.0154] | +53.6 % | 10 | yes | pass |
| at=hbm,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=placement | placement | hbm | 2.9130 | 3.2604 | 0.2975 | 0.9455 | -0.3473 [-0.3491, -0.3463] | -0.6480 [-0.6490, -0.6473] | -0.3005 [-0.3023, -0.2988] | +86.5 % | 10 | yes | pass |
| at=none,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=tiling | tiling | none | 26.6884 | 6.5011 | 36.2404 | 5.9383 | 20.1888 [20.1566, 20.2347] | 30.3007 [29.9752, 30.3419] | 10.1194 [9.7953, 10.1510] | +50.1 % | 10 | yes | pass |
| at=none,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=tiling | tiling | none | 3.2728 | 3.8530 | 2.7551 | 3.3893 | -0.5821 [-0.5888, -0.5758] | -0.6348 [-0.6438, -0.6283] | -0.0538 [-0.0611, -0.0436] | +9.2 % | 10 | yes | pass |
| at=off512m,footprint-mib=8192,kernel=k3,placement=cpu,type=four,vary=alignment | alignment | off512m | 7.8878 | 23.4966 | 48.6311 | 23.2313 | -15.6107 [-15.7553, -15.5959] | 25.4054 [25.0405, 25.4800] | 41.0101 [40.6364, 41.1935] | -262.7 % | 10 | yes | pass |
| at=plain,footprint-mib=1024,kernel=k6,placement=cpu,type=four,update=atomic,vary=update | update | plain | 6.0577 | 7.3806 | 5.9719 | 7.2354 | -1.3245 [-1.3316, -1.3177] | -1.2637 [-1.2718, -1.2546] | 0.0615 [0.0491, 0.0771] | -4.6 % | 10 | yes | pass |
| at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,type=four,vary=generator | generator | rmat | 30.8436 | 4.1934 | 189.0968 | 67.7799 | 26.6517 [26.6319, 26.6637] | 121.3589 [120.3253, 122.3391] | 94.7028 [93.6794, 95.7344] | +355.3 % | 10 | yes | pass |
| at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,type=four,vary=generator | generator | rmat | 1.2733 | 1.7622 | 65.8685 | 65.9340 | -0.4887 [-0.4901, -0.4833] | -0.0573 [-0.1169, 0.0091] | 0.4290 [0.3664, 0.4986] | -87.8 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | sharing | shared | 0.0199 | 0.0342 | 0.0207 | 0.0360 | -0.0144 [-0.0146, -0.0141] | -0.0154 [-0.0157, -0.0152] | -0.0012 [-0.0014, -0.0007] | +8.6 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 0.0203 | 0.0353 | 0.0210 | 0.0366 | -0.0151 [-0.0153, -0.0147] | -0.0156 [-0.0159, -0.0153] | -0.0006 [-0.0010, 0.0005] | +4.2 % | 10 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | sharing | shared | 0.0201 | 0.0347 | 0.0201 | 0.0345 | -0.0145 [-0.0148, -0.0142] | -0.0144 [-0.0147, -0.0143] | 0.0001 [-0.0002, 0.0004] | -0.4 % | 20 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | sharing | shared | 0.0123 | 0.0319 | 0.0123 | 0.0322 | -0.0196 [-0.0197, -0.0195] | -0.0200 [-0.0204, -0.0199] | -0.0005 [-0.0009, -0.0002] | +2.5 % | 30 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | sharing | shared | 0.0122 | 0.0319 | 0.0123 | 0.0322 | -0.0197 [-0.0198, -0.0195] | -0.0199 [-0.0201, -0.0197] | -0.0001 [-0.0009, 0.0001] | +0.6 % | 20 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | sharing | shared | 0.0123 | 0.0321 | 0.0123 | 0.0324 | -0.0198 [-0.0199, -0.0195] | -0.0199 [-0.0201, -0.0197] | -0.0002 [-0.0005, 0.0001] | +0.9 % | 20 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | sharing | shared | 2.9317 | 3.3149 | 2.9197 | 3.2041 | -0.3829 [-0.3859, -0.3814] | -0.2840 [-0.2850, -0.2825] | 0.0985 [0.0967, 0.1010] | -25.7 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 2.9307 | 3.3185 | 3.0679 | 3.3062 | -0.3877 [-0.3914, -0.3862] | -0.2398 [-0.2601, -0.2114] | 0.1495 [0.1293, 0.1818] | -38.5 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | sharing | shared | 2.9159 | 3.2904 | 2.9052 | 3.1835 | -0.3739 [-0.3751, -0.3732] | -0.2779 [-0.2789, -0.2768] | 0.0964 [0.0950, 0.0969] | -25.8 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | sharing | shared | 0.3374 | 0.9794 | 0.3404 | 0.9791 | -0.6424 [-0.6431, -0.6403] | -0.6390 [-0.6399, -0.6369] | 0.0027 [0.0013, 0.0057] | -0.4 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | sharing | shared | 0.3870 | 1.0795 | 0.4065 | 1.0791 | -0.6920 [-0.6947, -0.6909] | -0.6724 [-0.6742, -0.6700] | 0.0210 [0.0168, 0.0238] | -3.0 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | sharing | shared | 0.3359 | 0.9753 | 0.3387 | 0.9760 | -0.6391 [-0.6405, -0.6382] | -0.6370 [-0.6380, -0.6351] | 0.0024 [0.0003, 0.0052] | -0.4 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | sharing | shared | 0.3790 | 0.4644 | 0.3751 | 0.4576 | -0.0857 [-0.0876, -0.0842] | -0.0823 [-0.0835, -0.0803] | 0.0037 [0.0015, 0.0053] | -4.4 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 0.3791 | 0.4669 | 0.6701 | 0.7178 | -0.0872 [-0.0884, -0.0863] | -0.0440 [-0.0483, -0.0415] | 0.0429 [0.0398, 0.0459] | -49.2 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | sharing | shared | 0.3730 | 0.4510 | 0.3702 | 0.4499 | -0.0779 [-0.0784, -0.0772] | -0.0798 [-0.0801, -0.0794] | -0.0016 [-0.0024, -0.0013] | +2.0 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | sharing | shared | 0.0731 | 0.1891 | 0.2067 | 0.2833 | -0.1161 [-0.1164, -0.1157] | -0.0770 [-0.0782, -0.0724] | 0.0398 [0.0378, 0.0429] | -34.3 % | 30 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | sharing | shared | 0.0696 | 0.2086 | 0.2920 | 0.3647 | -0.1388 [-0.1406, -0.1375] | -0.0728 [-0.0729, -0.0721] | 0.0660 [0.0646, 0.0680] | -47.5 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | sharing | shared | 0.0593 | 0.1576 | 0.0590 | 0.1588 | -0.0984 [-0.0990, -0.0970] | -0.0998 [-0.1002, -0.0992] | -0.0015 [-0.0032, -0.0002] | +1.5 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | sharing | shared | 0.0228 | 0.0420 | 0.0226 | 0.0412 | -0.0191 [-0.0196, -0.0189] | -0.0185 [-0.0191, -0.0182] | 0.0007 [-0.0000, 0.0014] | -3.5 % | 10 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 0.0225 | 0.0404 | 0.0248 | 0.0450 | -0.0180 [-0.0181, -0.0177] | -0.0202 [-0.0204, -0.0200] | -0.0021 [-0.0026, -0.0019] | +11.4 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | sharing | shared | 0.0224 | 0.0406 | 0.0225 | 0.0403 | -0.0181 [-0.0184, -0.0180] | -0.0178 [-0.0182, -0.0175] | 0.0004 [-0.0000, 0.0008] | -2.3 % | 20 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | sharing | shared | 0.0124 | 0.0317 | 0.0132 | 0.0322 | -0.0192 [-0.0195, -0.0190] | -0.0189 [-0.0192, -0.0187] | 0.0004 [0.0000, 0.0007] | -2.3 % | 30 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | sharing | shared | 0.0124 | 0.0320 | 0.0138 | 0.0328 | -0.0196 [-0.0198, -0.0192] | -0.0189 [-0.0193, -0.0188] | 0.0007 [0.0003, 0.0010] | -3.3 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | sharing | shared | 0.0123 | 0.0315 | 0.0122 | 0.0316 | -0.0191 [-0.0194, -0.0189] | -0.0192 [-0.0195, -0.0190] | -0.0002 [-0.0005, 0.0005] | +1.1 % | 10 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | sharing | shared | 0.7437 | 0.8877 | 0.7371 | 0.8664 | -0.1437 [-0.1457, -0.1427] | -0.1292 [-0.1301, -0.1290] | 0.0144 [0.0126, 0.0164] | -10.0 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 0.7361 | 0.8755 | 0.8465 | 0.9362 | -0.1393 [-0.1398, -0.1388] | -0.0923 [-0.0982, -0.0883] | 0.0455 [0.0403, 0.0500] | -32.6 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | sharing | shared | 0.7335 | 0.8606 | 0.7342 | 0.8577 | -0.1270 [-0.1273, -0.1264] | -0.1237 [-0.1239, -0.1229] | 0.0034 [0.0028, 0.0042] | -2.7 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | sharing | shared | 0.1111 | 0.7854 | 0.1775 | 0.7534 | -0.6752 [-0.6866, -0.6646] | -0.5764 [-0.5770, -0.5755] | 0.0942 [0.0890, 0.1071] | -14.0 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | sharing | shared | 0.1222 | 0.7932 | 0.1998 | 0.7691 | -0.6712 [-0.6729, -0.6703] | -0.5685 [-0.5695, -0.5677] | 0.1024 [0.1017, 0.1036] | -15.3 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | sharing | shared | 0.0986 | 0.7497 | 0.1006 | 0.7492 | -0.6510 [-0.6527, -0.6507] | -0.6485 [-0.6492, -0.6482] | 0.0026 [0.0014, 0.0044] | -0.4 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | sharing | shared | 0.1001 | 0.1339 | 0.1011 | 0.1341 | -0.0338 [-0.0340, -0.0335] | -0.0332 [-0.0336, -0.0325] | 0.0006 [0.0002, 0.0016] | -1.9 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 0.0986 | 0.1332 | 0.1934 | 0.2172 | -0.0345 [-0.0352, -0.0340] | -0.0243 [-0.0247, -0.0234] | 0.0104 [0.0098, 0.0111] | -30.2 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | sharing | shared | 0.0998 | 0.1328 | 0.0998 | 0.1328 | -0.0329 [-0.0336, -0.0327] | -0.0329 [-0.0335, -0.0326] | 0.0002 [-0.0010, 0.0007] | -0.7 % | 10 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | sharing | shared | 0.0235 | 0.0557 | 0.0572 | 0.0890 | -0.0321 [-0.0325, -0.0318] | -0.0320 [-0.0323, -0.0315] | 0.0003 [-0.0004, 0.0008] | -0.9 % | 10 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | sharing | shared | 0.0223 | 0.0516 | 0.0927 | 0.1226 | -0.0295 [-0.0300, -0.0291] | -0.0301 [-0.0312, -0.0295] | -0.0008 [-0.0015, -0.0004] | +2.6 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | sharing | shared | 0.0236 | 0.0554 | 0.0227 | 0.0545 | -0.0318 [-0.0321, -0.0316] | -0.0317 [-0.0320, -0.0315] | 0.0000 [-0.0003, 0.0005] | -0.1 % | 20 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | sharing | shared | 0.1906 | 0.2398 | 0.1900 | 0.2397 | -0.0492 [-0.0497, -0.0481] | -0.0497 [-0.0505, -0.0493] | -0.0006 [-0.0023, 0.0001] | +1.2 % | 10 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 0.1914 | 0.2399 | 0.3760 | 0.4048 | -0.0487 [-0.0496, -0.0475] | -0.0294 [-0.0342, -0.0276] | 0.0194 [0.0147, 0.0213] | -39.9 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | sharing | shared | 0.1913 | 0.2392 | 0.1906 | 0.2386 | -0.0479 [-0.0480, -0.0475] | -0.0480 [-0.0484, -0.0474] | -0.0001 [-0.0008, 0.0005] | +0.2 % | 10 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | sharing | shared | 0.0381 | 0.0960 | 0.1213 | 0.1682 | -0.0578 [-0.0581, -0.0575] | -0.0468 [-0.0476, -0.0457] | 0.0109 [0.0103, 0.0114] | -18.9 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | sharing | shared | 0.0354 | 0.0914 | 0.1768 | 0.2224 | -0.0561 [-0.0562, -0.0554] | -0.0454 [-0.0473, -0.0444] | 0.0103 [0.0084, 0.0117] | -18.4 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | sharing | shared | 0.0365 | 0.0917 | 0.0353 | 0.0916 | -0.0551 [-0.0554, -0.0546] | -0.0563 [-0.0567, -0.0558] | -0.0011 [-0.0020, -0.0009] | +2.0 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | sharing | shared | 0.0359 | 0.0590 | 0.0358 | 0.0592 | -0.0232 [-0.0234, -0.0230] | -0.0233 [-0.0236, -0.0230] | -0.0002 [-0.0005, 0.0002] | +0.8 % | 20 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 0.0356 | 0.0589 | 0.0560 | 0.0773 | -0.0233 [-0.0237, -0.0230] | -0.0214 [-0.0215, -0.0212] | 0.0020 [0.0014, 0.0023] | -8.7 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | sharing | shared | 0.0357 | 0.0592 | 0.0357 | 0.0588 | -0.0234 [-0.0239, -0.0232] | -0.0231 [-0.0235, -0.0227] | 0.0003 [-0.0001, 0.0008] | -1.3 % | 10 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | sharing | shared | 0.0142 | 0.0323 | 0.0226 | 0.0466 | -0.0181 [-0.0183, -0.0179] | -0.0241 [-0.0243, -0.0239] | -0.0060 [-0.0064, -0.0057] | +33.0 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | sharing | shared | 0.0144 | 0.0316 | 0.0286 | 0.0502 | -0.0172 [-0.0174, -0.0170] | -0.0216 [-0.0220, -0.0213] | -0.0045 [-0.0051, -0.0042] | +26.0 % | 30 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | sharing | shared | 0.0143 | 0.0318 | 0.0146 | 0.0319 | -0.0175 [-0.0180, -0.0173] | -0.0173 [-0.0175, -0.0171] | 0.0001 [-0.0002, 0.0006] | -0.8 % | 20 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | sharing | shared | 0.2880 | 0.3590 | 0.2824 | 0.3511 | -0.0710 [-0.0723, -0.0697] | -0.0689 [-0.0705, -0.0681] | 0.0016 [0.0011, 0.0028] | -2.3 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 0.2860 | 0.3532 | 0.5479 | 0.5863 | -0.0676 [-0.0731, -0.0661] | -0.0378 [-0.0424, -0.0324] | 0.0317 [0.0229, 0.0361] | -46.9 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | sharing | shared | 0.2782 | 0.3497 | 0.2811 | 0.3483 | -0.0715 [-0.0719, -0.0710] | -0.0672 [-0.0676, -0.0668] | 0.0042 [0.0037, 0.0050] | -5.8 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | sharing | shared | 0.0547 | 0.1407 | 0.1878 | 0.2447 | -0.0861 [-0.0871, -0.0855] | -0.0565 [-0.0578, -0.0554] | 0.0296 [0.0283, 0.0311] | -34.4 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | sharing | shared | 0.0501 | 0.1406 | 0.2574 | 0.3083 | -0.0907 [-0.0913, -0.0895] | -0.0505 [-0.0520, -0.0500] | 0.0399 [0.0383, 0.0410] | -43.9 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | sharing | shared | 0.0486 | 0.1259 | 0.0485 | 0.1275 | -0.0774 [-0.0781, -0.0762] | -0.0790 [-0.0794, -0.0781] | -0.0014 [-0.0028, -0.0003] | +1.8 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | sharing | shared | 30.8258 | 4.7074 | 30.4671 | 4.1073 | 26.1326 [26.0944, 26.6173] | 26.3606 [26.3532, 26.3659] | 0.2257 [-0.2547, 0.2563] | +0.9 % | 100 | no | pass |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing | sharing | shared | 1.2811 | 1.7687 | 1.2767 | 1.7641 | -0.4883 [-0.4909, -0.4849] | -0.4870 [-0.4882, -0.4832] | 0.0012 [-0.0011, 0.0057] | -0.3 % | 10 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=1,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0371 | 0.0557 | 0.0363 | 0.0544 | -0.0186 [-0.0191, -0.0177] | -0.0179 [-0.0186, -0.0178] | 0.0007 [-0.0005, 0.0012] | -3.7 % | 10 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=1,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0368 | 0.0547 | 0.0557 | 0.0747 | -0.0179 [-0.0181, -0.0175] | -0.0190 [-0.0194, -0.0180] | -0.0009 [-0.0016, -0.0006] | +5.1 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=1,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0363 | 0.0536 | 0.0359 | 0.0536 | -0.0174 [-0.0179, -0.0170] | -0.0176 [-0.0184, -0.0173] | -0.0003 [-0.0009, 0.0005] | +1.7 % | 10 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0449 | 0.0637 | 0.0440 | 0.0626 | -0.0189 [-0.0190, -0.0187] | -0.0187 [-0.0188, -0.0181] | 0.0003 [-0.0001, 0.0006] | -1.5 % | 20 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0447 | 0.0636 | 0.0637 | 0.0823 | -0.0189 [-0.0198, -0.0182] | -0.0186 [-0.0192, -0.0178] | 0.0006 [-0.0005, 0.0010] | -3.2 % | 10 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0435 | 0.0604 | 0.0434 | 0.0604 | -0.0168 [-0.0173, -0.0167] | -0.0172 [-0.0175, -0.0168] | -0.0003 [-0.0007, 0.0003] | +1.8 % | 20 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=2,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0377 | 0.0548 | 0.0367 | 0.0537 | -0.0173 [-0.0175, -0.0165] | -0.0172 [-0.0174, -0.0167] | -0.0003 [-0.0005, 0.0009] | +1.5 % | 20 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=2,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0378 | 0.0550 | 0.0548 | 0.0729 | -0.0172 [-0.0176, -0.0169] | -0.0180 [-0.0185, -0.0176] | -0.0009 [-0.0013, -0.0002] | +5.4 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=2,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0368 | 0.0535 | 0.0366 | 0.0532 | -0.0169 [-0.0171, -0.0161] | -0.0167 [-0.0168, -0.0163] | 0.0002 [-0.0006, 0.0006] | -1.4 % | 10 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=4,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0391 | 0.0572 | 0.0386 | 0.0558 | -0.0179 [-0.0182, -0.0176] | -0.0173 [-0.0176, -0.0171] | 0.0005 [0.0000, 0.0010] | -2.7 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=4,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0388 | 0.0560 | 0.0582 | 0.0751 | -0.0174 [-0.0177, -0.0166] | -0.0170 [-0.0175, -0.0163] | 0.0005 [-0.0007, 0.0013] | -2.6 % | 10 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=4,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0381 | 0.0554 | 0.0379 | 0.0548 | -0.0172 [-0.0178, -0.0168] | -0.0170 [-0.0176, -0.0163] | 0.0004 [-0.0005, 0.0011] | -2.5 % | 10 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=64,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0677 | 0.0881 | 0.0666 | 0.0868 | -0.0205 [-0.0208, -0.0197] | -0.0199 [-0.0210, -0.0193] | 0.0003 [-0.0010, 0.0010] | -1.2 % | 10 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=64,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0675 | 0.0875 | 0.0855 | 0.1038 | -0.0200 [-0.0204, -0.0194] | -0.0183 [-0.0190, -0.0182] | 0.0014 [0.0009, 0.0020] | -7.0 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=64,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0670 | 0.0863 | 0.0667 | 0.0858 | -0.0192 [-0.0196, -0.0190] | -0.0192 [-0.0196, -0.0188] | 0.0001 [-0.0004, 0.0007] | -0.7 % | 10 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.1137 | 0.0392 | 0.1129 | 0.6230 | 0.0747 [0.0739, 0.0753] | -0.5102 [-0.5105, -0.5097] | -0.5851 [-0.5859, -0.5837] | -783.6 % | 50 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0428 | 0.0380 | 0.0436 | 0.6077 | 0.0048 [0.0042, 0.0052] | -0.5643 [-0.5647, -0.5641] | -0.5697 [-0.5731, -0.5685] | -11989.5 % | 70 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.1178 | 0.1446 | 0.1199 | 0.1445 | -0.0270 [-0.0280, -0.0264] | -0.0240 [-0.0248, -0.0232] | 0.0027 [0.0020, 0.0040] | -10.0 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | sharing | shared | 0.0464 | 0.0696 | 0.0472 | 0.0705 | -0.0229 [-0.0234, -0.0224] | -0.0228 [-0.0237, -0.0225] | -0.0001 [-0.0008, 0.0004] | +0.3 % | 40 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.0314 | 0.0431 | 0.0320 | 0.1954 | -0.0119 [-0.0120, -0.0116] | -0.1636 [-0.1647, -0.1610] | -0.1517 [-0.1528, -0.1492] | +1273.3 % | 40 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.0463 | 0.1644 | 0.0502 | 0.1633 | -0.1180 [-0.2192, -0.1174] | -0.1130 [-0.1140, -0.1124] | 0.0055 [0.0041, 0.0081] | -4.7 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 1.5119 | 0.0984 | 1.5140 | 0.6790 | 1.4135 [1.4128, 1.4143] | 0.8350 [0.8345, 0.8353] | -0.5787 [-0.5799, -0.5778] | -40.9 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0502 | 0.0429 | 0.0506 | 0.6177 | 0.0074 [0.0068, 0.0078] | -0.5672 [-0.5678, -0.5669] | -0.5754 [-0.5783, -0.5743] | -7826.9 % | 40 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 1.5045 | 0.0975 | 1.5192 | 0.7484 | 1.4071 [1.4064, 1.4075] | 0.7707 [0.7700, 0.7712] | -0.6365 [-0.6374, -0.6352] | -45.2 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0506 | 0.0431 | 0.0502 | 0.6917 | 0.0073 [0.0070, 0.0083] | -0.6413 [-0.6429, -0.6410] | -0.6497 [-0.6535, -0.6483] | -8851.0 % | 50 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 1.4980 | 0.2057 | 1.5203 | 0.2085 | 1.2923 [1.2915, 1.2939] | 1.3121 [1.3115, 1.3135] | 0.0195 [0.0177, 0.0213] | +1.5 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | sharing | shared | 0.0543 | 0.0769 | 0.0551 | 0.0781 | -0.0228 [-0.0231, -0.0224] | -0.0227 [-0.0238, -0.0222] | -0.0002 [-0.0012, 0.0006] | +0.9 % | 40 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.1142 | 0.1094 | 0.1139 | 0.2551 | 0.0048 [0.0043, 0.0054] | -0.1413 [-0.1445, -0.1403] | -0.1465 [-0.1495, -0.1450] | -3062.5 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.1144 | 0.1088 | 0.1165 | 0.7318 | 0.0056 [0.0049, 0.0064] | -0.6153 [-0.6159, -0.6142] | -0.6212 [-0.6225, -0.6190] | -11134.0 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.1278 | 0.2282 | 0.1284 | 0.2270 | -0.1003 [-0.1017, -0.0998] | -0.0987 [-0.0994, -0.0980] | 0.0021 [0.0009, 0.0029] | -2.1 % | 40 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.2044 | 0.0395 | 0.2058 | 0.6285 | 0.1647 [0.1641, 0.1650] | -0.4227 [-0.4229, -0.4225] | -0.5875 [-0.5880, -0.5865] | -356.8 % | 70 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0441 | 0.0391 | 0.0445 | 0.6075 | 0.0052 [0.0048, 0.0059] | -0.5633 [-0.5636, -0.5630] | -0.5723 [-0.5739, -0.5697] | -11107.7 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.2085 | 0.1455 | 0.2099 | 0.1454 | 0.0631 [0.0627, 0.0638] | 0.0644 [0.0636, 0.0656] | 0.0015 [0.0006, 0.0025] | +2.4 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | sharing | shared | 0.0480 | 0.0707 | 0.0483 | 0.0711 | -0.0226 [-0.0229, -0.0224] | -0.0225 [-0.0228, -0.0222] | 0.0002 [-0.0005, 0.0008] | -0.7 % | 60 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.0409 | 0.0555 | 0.0407 | 0.2055 | -0.0146 [-0.0147, -0.0144] | -0.1645 [-0.1662, -0.1630] | -0.1498 [-0.1515, -0.1486] | +1029.7 % | 70 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.0556 | 0.9225 | 0.0581 | 0.6827 | -0.8671 [-0.9027, -0.7812] | -0.6245 [-0.7136, -0.5249] | 0.2173 [0.1473, 0.2626] | -25.1 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.3928 | 0.0499 | 0.3915 | 0.6310 | 0.3430 [0.3422, 0.3435] | -0.2395 [-0.2398, -0.2393] | -0.5826 [-0.5836, -0.5815] | -169.9 % | 70 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0448 | 0.0395 | 0.0459 | 0.6075 | 0.0054 [0.0050, 0.0058] | -0.5621 [-0.5626, -0.5615] | -0.5704 [-0.5726, -0.5669] | -10530.2 % | 50 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.3913 | 0.1502 | 0.3965 | 0.1528 | 0.2409 [0.2406, 0.2421] | 0.2437 [0.2432, 0.2453] | 0.0027 [0.0015, 0.0044] | +1.1 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | sharing | shared | 0.0499 | 0.0716 | 0.0507 | 0.0719 | -0.0218 [-0.0220, -0.0215] | -0.0216 [-0.0220, -0.0213] | 0.0002 [-0.0004, 0.0006] | -0.8 % | 50 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.0521 | 0.0625 | 0.0519 | 0.2089 | -0.0103 [-0.0110, -0.0099] | -0.1570 [-0.1587, -0.1556] | -0.1468 [-0.1481, -0.1459] | +1428.9 % | 30 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.0649 | 0.9259 | 0.0671 | 0.6278 | -0.8612 [-0.9696, -0.8516] | -0.5612 [-0.6523, -0.5292] | 0.3155 [0.2000, 0.4150] | -36.6 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 5.9980 | 0.2952 | 6.0066 | 0.8784 | 5.7044 [5.7021, 5.7088] | 5.1280 [5.1272, 5.1301] | -0.5782 [-0.5799, -0.5752] | -10.1 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0735 | 0.0645 | 0.0737 | 0.6365 | 0.0089 [0.0083, 0.0092] | -0.5631 [-0.5637, -0.5626] | -0.5729 [-0.5744, -0.5718] | -6418.5 % | 80 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 5.9830 | 0.3970 | 5.9347 | 0.4005 | 5.5861 [5.5793, 5.6065] | 5.5341 [5.5303, 5.5398] | -0.0512 [-0.0706, -0.0414] | -0.9 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | sharing | shared | 0.0776 | 0.1026 | 0.0787 | 0.1035 | -0.0248 [-0.0258, -0.0240] | -0.0247 [-0.0258, -0.0240] | 0.0003 [-0.0010, 0.0010] | -1.1 % | 20 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.3589 | 0.3049 | 0.3586 | 0.4463 | 0.0534 [0.0528, 0.0553] | -0.0879 [-0.0894, -0.0862] | -0.1419 [-0.1436, -0.1394] | -265.5 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.3757 | 2.7497 | 0.3850 | 0.9855 | -2.3733 [-2.7423, -2.0886] | -0.5999 [-0.6965, -0.5846] | 1.7979 [1.3803, 2.2574] | -75.8 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 5.4369 | 0.4911 | 5.4074 | 1.0762 | 4.9454 [4.9300, 4.9508] | 4.3325 [4.3273, 4.3565] | -0.6012 [-0.6185, -0.5897] | -12.2 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 5.3847 | 3.4663 | 5.3806 | 3.5047 | 1.9183 [1.9158, 1.9197] | 1.8759 [1.8549, 1.8774] | -0.0439 [-0.0634, -0.0385] | -2.3 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 0.5993 | 0.5544 | 0.6004 | 0.6580 | 0.0448 [0.0397, 0.0466] | -0.0574 [-0.0633, -0.0510] | -0.1014 [-0.1086, -0.0928] | -226.4 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | sharing | shared | 0.6905 | 1.3070 | 0.6903 | 1.2907 | -0.6168 [-0.6197, -0.6135] | -0.6008 [-0.6021, -0.5983] | 0.0166 [0.0150, 0.0187] | -2.7 % | 10 | yes | pass |
| at=shared,footprint-mib=11520,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 240.4099 | 0.5145 | 240.4010 | 3.9854 | 239.8945 [239.8153, 239.9211] | 236.4392 [236.3878, 236.5171] | -3.4604 [-3.5164, -3.3688] | -1.4 % | 30 | yes | pass |
| at=shared,footprint-mib=11520,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 240.0524 | 33.3600 | 240.0516 | 31.8869 | 206.6860 [206.6078, 206.7844] | 208.1782 [208.1028, 208.2421] | 1.4728 [1.3638, 1.6657] | +0.7 % | 20 | yes | pass |
| at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 279.7643 | 0.5199 | 279.8474 | 4.2203 | 279.2444 [279.1080, 279.3033] | 275.6335 [275.4739, 275.7427] | -3.6035 [-3.6671, -3.4208] | -1.3 % | 10 | yes | pass |
| at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 279.6866 | 35.3151 | 279.7177 | 33.9388 | 244.3631 [244.2807, 244.4538] | 245.7875 [245.7102, 245.9014] | 1.3745 [1.2878, 1.5587] | +0.6 % | 20 | yes | pass |
| at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 283.7183 | 0.5736 | 284.9785 | 2.4588 | 283.1456 [282.8274, 283.2988] | 282.5284 [282.2679, 282.7275] | -0.5699 [-0.7550, -0.3695] | -0.2 % | 10 | yes | pass |
| at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | sharing | shared | 285.3312 | 8.3302 | 282.5239 | 8.2905 | 276.9943 [276.8449, 277.2427] | 274.2363 [273.9773, 274.4733] | -2.7622 [-2.9485, -2.5520] | -1.0 % | 10 | yes | pass |
| at=shared,footprint-mib=1536,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 5.4545 | 0.5019 | 5.4436 | 1.2622 | 4.9527 [4.9502, 4.9745] | 4.1801 [4.1627, 4.2086] | -0.7714 [-0.8109, -0.7445] | -15.6 % | 10 | yes | pass |
| at=shared,footprint-mib=1536,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 5.3833 | 4.9120 | 5.3781 | 4.8935 | 0.4705 [0.4698, 0.4736] | 0.4857 [0.4798, 0.4926] | 0.0111 [0.0089, 0.0210] | +2.4 % | 10 | yes | pass |
| at=shared,footprint-mib=16384,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | sharing | shared | 483.3537 | 49.1697 | 482.9713 | 45.9651 | 434.1883 [434.1175, 434.2924] | 437.0037 [436.9455, 437.0732] | 2.8055 [2.7609, 2.9370] | +0.6 % | 10 | yes | pass |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 7.2559 | 46.0952 | 7.2257 | 42.5934 | -38.8401 [-38.8484, -38.8336] | -35.3687 [-35.3779, -35.3506] | 3.4735 [3.4556, 3.4925] | -8.9 % | 10 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 433.5392 | 0.5191 | 433.5504 | 5.2858 | 433.0210 [432.8795, 433.0829] | 428.2769 [428.2021, 428.3247] | -4.7524 [-4.8396, -4.5627] | -1.1 % | 10 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1 | sharing | shared | 433.5873 | 0.5174 | 433.6692 | 10.6582 | 433.0697 [432.9996, 433.2360] | 423.0070 [422.9121, 423.1157] | -10.0471 [-10.2899, -9.8650] | -2.3 % | 10 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 433.5624 | 46.7860 | 433.5325 | 43.2120 | 386.7560 [386.6110, 386.9785] | 390.3241 [390.2599, 390.4417] | 3.5827 [3.2801, 3.7709] | +0.9 % | 10 | yes | pass |
| at=shared,footprint-mib=2048,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 5.4472 | 0.5042 | 5.4680 | 1.3031 | 4.9435 [4.9403, 5.0003] | 4.1637 [4.1325, 4.1981] | -0.7797 [-0.8360, -0.7519] | -15.8 % | 10 | yes | pass |
| at=shared,footprint-mib=2048,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 5.4032 | 6.2955 | 5.3922 | 6.3377 | -0.8922 [-0.8952, -0.8889] | -0.9446 [-0.9592, -0.9384] | -0.0526 [-0.0626, -0.0468] | +5.9 % | 10 | yes | pass |
| at=shared,footprint-mib=24576,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | sharing | shared | 751.9911 | 74.7598 | 751.7769 | 73.2511 | 677.2143 [677.1797, 677.2813] | 678.5407 [678.3910, 678.6355] | 1.3429 [1.1065, 1.4749] | +0.2 % | 20 | yes | pass |
| at=shared,footprint-mib=24576,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 598.3750 | 0.5204 | 598.4190 | 7.6365 | 597.8558 [597.6896, 597.9697] | 590.8565 [590.7107, 591.1343] | -7.0373 [-7.1217, -6.7473] | -1.2 % | 10 | yes | pass |
| at=shared,footprint-mib=24576,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 598.3220 | 68.0425 | 598.3486 | 64.2185 | 530.2726 [530.0984, 530.4976] | 534.1281 [534.0138, 534.2918] | 3.8344 [3.6010, 4.1129] | +0.7 % | 10 | yes | pass |
| at=shared,footprint-mib=256,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | sharing | shared | 7.3888 | 1.0774 | 7.3703 | 1.0124 | 6.3134 [6.3080, 6.3392] | 6.3581 [6.3561, 6.3590] | 0.0402 [0.0192, 0.0525] | +0.6 % | 100 | yes | pass |
| at=shared,footprint-mib=256,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing | sharing | shared | 0.2146 | 0.8883 | 0.2157 | 0.8891 | -0.6739 [-0.6752, -0.6729] | -0.6735 [-0.6739, -0.6725] | 0.0008 [-0.0004, 0.0017] | -0.1 % | 10 | no | pass |
| at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 5.3837 | 0.4449 | 5.3870 | 0.6069 | 4.9388 [4.9380, 4.9393] | 4.7803 [4.7794, 4.7809] | -0.1585 [-0.1595, -0.1572] | -3.2 % | 10 | yes | pass |
| at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 5.3933 | 1.2190 | 5.3866 | 1.2618 | 4.1740 [4.1728, 4.1765] | 4.1248 [4.1228, 4.1276] | -0.0488 [-0.0531, -0.0465] | -1.2 % | 10 | yes | pass |
| at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 0.5042 | 0.5028 | 0.4968 | 0.5538 | 0.0019 [0.0003, 0.0024] | -0.0576 [-0.0590, -0.0547] | -0.0595 [-0.0630, -0.0550] | -3122.1 % | 10 | yes | pass |
| at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | sharing | shared | 0.5970 | 1.2544 | 0.5852 | 1.1197 | -0.6564 [-0.6585, -0.6541] | -0.5341 [-0.5363, -0.5323] | 0.1233 [0.1203, 0.1250] | -18.8 % | 20 | yes | pass |
| at=shared,footprint-mib=32768,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | sharing | shared | 971.5030 | 92.8712 | 970.9788 | 89.8565 | 878.6426 [878.5545, 878.8013] | 881.1522 [880.9793, 881.3277] | 2.4554 [2.3115, 2.7246] | +0.3 % | 10 | yes | pass |
| at=shared,footprint-mib=32768,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 684.9934 | 0.5176 | 685.0633 | 9.9001 | 684.4765 [684.4058, 684.5189] | 675.1603 [675.0379, 675.2262] | -9.2899 [-9.4452, -9.2427] | -1.4 % | 10 | yes | pass |
| at=shared,footprint-mib=32768,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 684.9676 | 87.3821 | 684.9969 | 85.3158 | 597.5844 [597.4548, 597.7412] | 599.6749 [599.5418, 599.8035] | 2.1360 [1.9171, 2.2781] | +0.4 % | 10 | yes | pass |
| at=shared,footprint-mib=4096,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | sharing | shared | 123.8101 | 12.5399 | 121.5360 | 12.6250 | 111.2704 [111.1947, 111.2945] | 108.9141 [108.8116, 108.9634] | -2.3582 [-2.4227, -2.2367] | -2.1 % | 10 | yes | pass |
| at=shared,footprint-mib=4096,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing | sharing | shared | 7.0846 | 9.5889 | 7.0597 | 9.5903 | -2.5036 [-2.5086, -2.4967] | -2.5319 [-2.5494, -2.5216] | -0.0292 [-0.0465, -0.0169] | +1.2 % | 10 | yes | pass |
| at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 5.6997 | 0.5036 | 5.7532 | 1.7889 | 5.1967 [5.1729, 5.2646] | 3.9730 [3.9396, 4.0593] | -1.2334 [-1.3011, -1.1706] | -23.7 % | 10 | yes | pass |
| at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 5.4952 | 11.9977 | 5.5256 | 12.1706 | -6.5002 [-6.5281, -6.4771] | -6.6292 [-6.6957, -6.6079] | -0.1334 [-0.1957, -0.0970] | +2.1 % | 10 | yes | pass |
| at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 5.3155 | 0.5621 | 5.3360 | 1.1205 | 4.7523 [4.7508, 4.7581] | 4.2186 [4.2100, 4.2258] | -0.5373 [-0.5408, -0.5260] | -11.3 % | 10 | yes | pass |
| at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | sharing | shared | 5.3324 | 3.2227 | 5.3392 | 3.2238 | 2.1086 [2.0998, 2.1154] | 2.1173 [2.1014, 2.1246] | 0.0052 [-0.0028, 0.0204] | +0.2 % | 10 | no | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=1,tiling=tiles,type=four,vary=sharing | sharing | shared | 3.7777 | 3.7318 | 3.0544 | 3.6760 | 0.0463 [0.0402, 0.0502] | -0.6215 [-0.6258, -0.6181] | -0.6689 [-0.6731, -0.6601] | -1443.4 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=16,tiling=tiles,type=four,vary=sharing | sharing | shared | 54.1416 | 9.7609 | 46.0260 | 9.7270 | 44.3778 [44.3544, 44.4219] | 36.2954 [36.2653, 36.3159] | -8.1031 [-8.1473, -8.0529] | -18.3 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=2,tiling=tiles,type=four,vary=sharing | sharing | shared | 7.1423 | 4.1422 | 5.9160 | 4.0719 | 2.9993 [2.9961, 3.0070] | 1.8441 [1.8426, 1.8505] | -1.1558 [-1.1631, -1.1516] | -38.5 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=4,tiling=tiles,type=four,vary=sharing | sharing | shared | 13.5641 | 4.9248 | 11.6284 | 4.8880 | 8.6398 [8.6242, 8.6534] | 6.7394 [6.7355, 6.7501] | -1.8972 [-1.9103, -1.8799] | -22.0 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=64,tiling=tiles,type=four,vary=sharing | sharing | shared | 218.3446 | 29.0724 | 182.8777 | 29.0389 | 189.2923 [189.1930, 189.3911] | 153.8585 [153.8229, 153.8941] | -35.4189 [-35.5604, -35.3584] | -18.7 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing | sharing | shared | 26.5402 | 6.5190 | 22.8716 | 6.4422 | 20.0172 [19.9988, 20.0328] | 16.4315 [16.4201, 16.4380] | -3.5914 [-3.5994, -3.5761] | -17.9 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=1,tiling=tiles,type=four,vary=sharing | sharing | shared | 0.4112 | 1.0582 | 0.4111 | 1.0571 | -0.6471 [-0.6483, -0.6459] | -0.6466 [-0.6475, -0.6446] | 0.0010 [0.0002, 0.0019] | -0.2 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=16,tiling=tiles,type=four,vary=sharing | sharing | shared | 6.5625 | 7.0601 | 6.5155 | 7.0625 | -0.4955 [-0.5188, -0.4858] | -0.5465 [-0.5640, -0.5346] | -0.0566 [-0.0694, -0.0080] | +11.4 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=2,tiling=tiles,type=four,vary=sharing | sharing | shared | 0.8190 | 1.4579 | 0.8244 | 1.4597 | -0.6391 [-0.6417, -0.6377] | -0.6348 [-0.6372, -0.6336] | 0.0032 [0.0016, 0.0077] | -0.5 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=4,tiling=tiles,type=four,vary=sharing | sharing | shared | 1.6405 | 2.2610 | 1.6342 | 2.2581 | -0.6208 [-0.6238, -0.6176] | -0.6232 [-0.6264, -0.6200] | -0.0043 [-0.0066, 0.0024] | +0.7 % | 10 | no | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=64,tiling=tiles,type=four,vary=sharing | sharing | shared | 26.0504 | 26.4322 | 26.0597 | 26.4569 | -0.3858 [-0.4192, -0.3626] | -0.3774 [-0.4460, -0.3508] | 0.0046 [-0.0548, 0.0671] | -1.2 % | 10 | no | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing | sharing | shared | 3.2608 | 3.8671 | 3.2825 | 3.8687 | -0.6093 [-0.6157, -0.6036] | -0.5847 [-0.5911, -0.5789] | 0.0252 [0.0163, 0.0332] | -4.1 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=1,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 3.7322 | 2.2306 | 3.0918 | 2.5299 | 1.5014 [1.4998, 1.5048] | 0.5617 [0.5598, 0.5649] | -0.9399 [-0.9429, -0.9376] | -62.6 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=16,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 52.5741 | 8.2306 | 45.9217 | 8.5312 | 44.3558 [44.3095, 44.3891] | 37.3771 [37.3522, 37.4086] | -6.9766 [-7.0158, -6.9325] | -15.7 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=2,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 7.0453 | 2.6330 | 6.0058 | 2.9309 | 4.4111 [4.4069, 4.4213] | 3.0753 [3.0721, 3.0780] | -1.3387 [-1.3492, -1.3292] | -30.3 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=4,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 13.6090 | 3.4390 | 11.6451 | 3.7369 | 10.1705 [10.1535, 10.1912] | 7.9094 [7.8992, 7.9230] | -2.2536 [-2.2839, -2.2281] | -22.2 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=64,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 214.9367 | 27.5607 | 182.5522 | 27.8099 | 187.3820 [187.2541, 187.4346] | 154.7519 [154.7182, 154.7811] | -32.6493 [-32.6793, -32.4856] | -17.4 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 26.4606 | 5.0393 | 23.0075 | 5.3337 | 21.4240 [21.4000, 21.4413] | 17.6742 [17.6636, 17.6809] | -3.7471 [-3.7660, -3.7334] | -17.5 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 25.9355 | 5.0368 | 23.1159 | 5.3757 | 20.8979 [20.8876, 20.9152] | 17.7402 [17.7252, 17.7596] | -3.1570 [-3.1788, -3.1364] | -15.1 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=1,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 3.7534 | 3.7329 | 3.1232 | 3.7711 | 0.0217 [0.0152, 0.0276] | -0.6453 [-0.6675, -0.6422] | -0.6671 [-0.6947, -0.6594] | -3072.0 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=16,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 54.1213 | 9.7626 | 45.9064 | 9.8384 | 44.3607 [44.3268, 44.4155] | 36.0708 [36.0532, 36.0946] | -8.2828 [-8.3373, -8.2475] | -18.7 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=2,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 6.8037 | 4.1218 | 5.9593 | 4.1740 | 2.6833 [2.6630, 2.6897] | 1.7839 [1.7785, 1.7879] | -0.8995 [-0.9113, -0.8802] | -33.5 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=4,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 13.5123 | 4.9259 | 11.7142 | 4.9835 | 8.5870 [8.5773, 8.5994] | 6.7293 [6.7134, 6.7377] | -1.8578 [-1.8819, -1.8344] | -21.6 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=64,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 214.0181 | 29.0229 | 182.9349 | 29.1477 | 184.9729 [184.9042, 185.0819] | 153.7938 [153.7552, 153.8039] | -31.2255 [-31.3111, -31.1058] | -16.9 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 26.5905 | 6.5365 | 23.2107 | 6.6250 | 20.0515 [20.0412, 20.0769] | 16.5830 [16.5679, 16.6170] | -3.4746 [-3.4941, -3.4242] | -17.3 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=1,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 0.5640 | 0.7517 | 0.5871 | 0.8428 | -0.1876 [-0.1898, -0.1870] | -0.2558 [-0.2569, -0.2542] | -0.0676 [-0.0692, -0.0665] | +36.0 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=16,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 6.6987 | 6.7788 | 6.8127 | 6.8699 | -0.0808 [-0.0866, -0.0606] | -0.0560 [-0.0715, -0.0457] | 0.0181 [0.0052, 0.0346] | -22.4 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=2,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 1.0491 | 1.1516 | 1.1715 | 1.2443 | -0.1019 [-0.1039, -0.1005] | -0.0727 [-0.0787, -0.0709] | 0.0282 [0.0247, 0.0329] | -27.6 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=4,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 1.9482 | 1.9627 | 1.9762 | 2.0476 | -0.0149 [-0.0215, -0.0080] | -0.0717 [-0.0724, -0.0684] | -0.0554 [-0.0633, -0.0502] | +372.8 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=64,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 25.9389 | 26.0556 | 26.0230 | 26.1391 | -0.1093 [-0.1838, -0.0817] | -0.1075 [-0.1540, -0.1030] | -0.0127 [-0.0629, 0.0468] | +11.6 % | 10 | no | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 3.5567 | 3.5542 | 3.4976 | 3.6449 | 0.0035 [-0.0013, 0.0121] | -0.1473 [-0.1583, -0.1413] | -0.1506 [-0.1745, -0.1405] | - | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 3.5644 | 3.5587 | 3.5935 | 3.8659 | 0.0093 [-0.0043, 0.0108] | -0.2719 [-0.2886, -0.2647] | -0.2814 [-0.2949, -0.2656] | - | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=1,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 0.6522 | 1.1997 | 0.5901 | 1.1756 | -0.5476 [-0.5487, -0.5440] | -0.5857 [-0.5881, -0.5826] | -0.0375 [-0.0422, -0.0334] | +6.8 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=16,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 6.6887 | 7.2177 | 6.8124 | 7.1942 | -0.5253 [-0.5481, -0.5205] | -0.3816 [-0.3875, -0.3709] | 0.1468 [0.1287, 0.1676] | -28.0 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=2,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 1.1313 | 1.5990 | 1.1380 | 1.5744 | -0.4669 [-0.4727, -0.4602] | -0.4372 [-0.4401, -0.4345] | 0.0297 [0.0199, 0.0386] | -6.4 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=4,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 1.9490 | 2.4012 | 1.8784 | 2.3789 | -0.4520 [-0.4564, -0.4460] | -0.5004 [-0.5043, -0.4959] | -0.0485 [-0.0533, -0.0450] | +10.7 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=64,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 26.1535 | 26.6075 | 26.1437 | 26.5346 | -0.4487 [-0.4881, -0.4171] | -0.3838 [-0.4309, -0.3620] | 0.0698 [-0.0139, 0.0998] | -15.6 % | 10 | no | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 3.5638 | 4.0138 | 3.5021 | 3.9834 | -0.4485 [-0.4554, -0.4425] | -0.4791 [-0.4927, -0.4752] | -0.0325 [-0.0443, -0.0106] | +7.2 % | 10 | yes | pass |
| at=shared,footprint-mib=8192,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | sharing | shared | 247.2339 | 25.0841 | 246.8743 | 25.1106 | 222.1581 [221.9981, 222.1987] | 221.7695 [221.7161, 221.8744] | -0.3505 [-0.4510, -0.1733] | -0.2 % | 10 | yes | pass |
| at=shared,footprint-mib=8192,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing | sharing | shared | 15.1288 | 20.2279 | 15.1189 | 20.2074 | -5.1038 [-5.1148, -5.0840] | -5.0892 [-5.1010, -5.0748] | 0.0175 [-0.0263, 0.0378] | -0.3 % | 10 | no | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 7.9066 | 0.5163 | 7.8641 | 3.0766 | 7.3909 [7.3895, 7.3945] | 4.8323 [4.7776, 4.9032] | -2.5701 [-2.6199, -2.5344] | -34.8 % | 30 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 7.8828 | 23.5930 | 7.8568 | 23.6048 | -15.7102 [-15.7266, -15.6944] | -15.7572 [-15.7707, -15.7259] | -0.0368 [-0.1799, -0.0001] | +0.2 % | 10 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 8.0742 | 0.5646 | 8.0971 | 1.6750 | 7.5084 [7.5058, 7.5144] | 6.4221 [6.4168, 6.4323] | -1.0800 [-1.0990, -1.0774] | -14.4 % | 20 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1 | sharing | shared | 8.0727 | 0.5674 | 8.0911 | 5.4880 | 7.5037 [7.4999, 7.5093] | 2.6017 [2.5944, 2.6551] | -4.9010 [-4.9064, -4.8484] | -65.3 % | 10 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | sharing | shared | 8.0907 | 5.7471 | 8.1018 | 5.7462 | 2.3447 [2.3343, 2.3540] | 2.3632 [2.3466, 2.3775] | 0.0158 [0.0057, 0.0346] | +0.7 % | 10 | yes | pass |
| at=shared,footprint-mib=9728,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 128.4095 | 0.5137 | 128.4990 | 3.5248 | 127.8951 [127.8549, 127.9436] | 124.9744 [124.9195, 125.0073] | -2.8981 [-3.0194, -2.7850] | -2.3 % | 20 | yes | pass |
| at=shared,footprint-mib=9728,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 128.2762 | 27.3478 | 128.3016 | 27.4515 | 100.9171 [100.8382, 101.0022] | 100.8670 [100.7480, 100.9299] | -0.0407 [-0.1569, 0.0585] | -0.0 % | 10 | no | pass |
| at=sys,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8 | scope | sys | 0.0302 | 0.0536 | 0.0306 | 0.0536 | -0.0234 [-0.0237, -0.0233] | -0.0229 [-0.0231, -0.0228] | 0.0005 [0.0003, 0.0008] | -2.0 % | 10 | yes | pass |
| at=sys,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=four,vary=scope,working-set-mib=8 | scope | sys | 0.0088 | 0.0500 | 0.0096 | 0.0499 | -0.0411 [-0.0412, -0.0411] | -0.0403 [-0.0405, -0.0402] | 0.0009 [0.0007, 0.0010] | -2.1 % | 40 | yes | pass |
| at=sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8 | scope | sys | 0.0379 | 0.0614 | 0.4024 | 0.0836 | -0.0234 [-0.0236, -0.0232] | 0.3186 [0.3172, 0.3196] | 0.3422 [0.3407, 0.3429] | -1461.0 % | 10 | yes | pass |
| at=sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=four,vary=scope,working-set-mib=8 | scope | sys | 0.0160 | 0.0582 | 0.0382 | 0.0829 | -0.0422 [-0.0424, -0.0421] | -0.0446 [-0.0450, -0.0445] | -0.0025 [-0.0028, -0.0022] | +6.0 % | 20 | yes | pass |
| at=sys,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8 | scope | sys | 0.0310 | 0.0537 | 0.0560 | 0.0565 | -0.0227 [-0.0227, -0.0226] | -0.0005 [-0.0006, -0.0003] | 0.0222 [0.0220, 0.0223] | -98.0 % | 10 | yes | pass |
| at=sys,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=four,vary=scope,working-set-mib=8 | scope | sys | 0.0093 | 0.0498 | 0.0115 | 0.0511 | -0.0406 [-0.0406, -0.0405] | -0.0396 [-0.0400, -0.0393] | 0.0009 [0.0006, 0.0012] | -2.3 % | 30 | yes | pass |
| at=sys,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8 | scope | sys | 0.0319 | 0.0547 | 0.1061 | 0.0594 | -0.0228 [-0.0229, -0.0227] | 0.0467 [0.0464, 0.0469] | 0.0695 [0.0692, 0.0698] | -305.1 % | 10 | yes | pass |
| at=sys,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=four,vary=scope,working-set-mib=8 | scope | sys | 0.0103 | 0.0501 | 0.0154 | 0.0583 | -0.0398 [-0.0400, -0.0397] | -0.0429 [-0.0432, -0.0427] | -0.0030 [-0.0036, -0.0028] | +7.5 % | 10 | yes | pass |
| at=sys,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8 | scope | sys | 0.0607 | 0.0844 | 1.5858 | 0.1716 | -0.0237 [-0.0238, -0.0233] | 1.4141 [1.4071, 1.4204] | 1.4378 [1.4308, 1.4440] | -6067.6 % | 10 | yes | pass |
| at=sys,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=four,vary=scope,working-set-mib=8 | scope | sys | 0.0388 | 0.0833 | 0.1280 | 0.1684 | -0.0445 [-0.0447, -0.0444] | -0.0402 [-0.0407, -0.0400] | 0.0044 [0.0038, 0.0048] | -9.9 % | 20 | yes | pass |

## Host phases

The CPU phase before every pass, timed on the CPU clock (ms per pass), and the state check's median load latency on the preparing core after the phase (ns per sampled load), per variant.

| cell | direct home CPU ms | direct home state ns | copy home CPU ms | copy home state ns | direct level CPU ms | direct level state ns | copy level CPU ms | copy level state ns |
|---|---|---|---|---|---|---|---|---|
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | 0.3289 | 7.6 | 0.3312 | 25.6 | 0.3315 | 12.8 | 0.3331 | 14.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 0.2893 | 7.8 | 0.2887 | 26.1 | 0.2816 | 23.6 | 0.2832 | 22.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | 0.3062 | 185.1 | 0.3087 | 169.8 | 0.3057 | 71.1 | 0.3053 | 71.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | 0.7306 | 7.1 | 0.7332 | 17.9 | 0.7528 | 23.0 | 0.7528 | 18.8 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | 0.7245 | 7.4 | 0.7226 | 32.2 | 0.6657 | 35.6 | 0.6715 | 37.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | 0.6979 | 358.2 | 0.7026 | 339.4 | 0.6948 | 360.4 | 0.7001 | 352.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | 228.4949 | 200.6 | 229.3174 | 290.4 | 230.0764 | 269.8 | 232.6285 | 322.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 109.6818 | 207.4 | 111.1444 | 304.8 | 108.4513 | 257.2 | 108.9490 | 362.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | 167.6960 | 208.1 | 172.8574 | 253.6 | 168.4941 | 247.4 | 167.1007 | 300.8 |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | 316.6246 | 551.4 | 316.7138 | 567.8 | 316.9971 | 582.0 | 316.6478 | 572.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | 142.3564 | 642.2 | 142.3414 | 652.8 | 142.0956 | 606.8 | 142.2945 | 635.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | 187.2331 | 575.8 | 188.0279 | 575.8 | 187.4903 | 617.6 | 187.5280 | 644.6 |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | 27.8155 | 99.9 | 27.6445 | 118.8 | 29.0713 | 169.5 | 28.9385 | 175.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 13.7652 | 113.6 | 13.7649 | 136.9 | 14.0100 | 155.0 | 13.7625 | 157.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | 21.1175 | 202.1 | 21.3543 | 240.0 | 21.0825 | 250.1 | 21.0511 | 230.8 |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | 35.7015 | 357.0 | 36.0282 | 356.2 | 40.0974 | 364.6 | 39.5123 | 374.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | 17.8376 | 292.2 | 17.9526 | 338.8 | 17.4458 | 296.9 | 18.3182 | 323.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | 23.9818 | 490.9 | 24.0705 | 511.5 | 23.7714 | 498.4 | 24.1017 | 518.6 |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | 0.6388 | 26.0 | 0.6380 | 40.9 | 0.6543 | 41.2 | 0.6575 | 43.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 0.4715 | 29.4 | 0.4745 | 40.5 | 0.4372 | 42.0 | 0.4414 | 37.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | 0.5483 | 196.4 | 0.5523 | 189.6 | 0.5474 | 108.5 | 0.5505 | 122.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | 1.0379 | 43.0 | 1.0376 | 39.9 | 1.1365 | 50.1 | 1.1440 | 49.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | 0.8608 | 40.2 | 0.8759 | 46.9 | 0.8518 | 51.9 | 0.8520 | 47.6 |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | 0.9342 | 372.2 | 0.9491 | 364.9 | 0.9372 | 369.9 | 0.9465 | 364.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | 57.4079 | 142.8 | 56.1422 | 221.5 | 58.2755 | 202.9 | 58.2378 | 229.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 27.2931 | 170.2 | 27.2967 | 223.0 | 27.2871 | 221.5 | 27.4693 | 262.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | 43.0460 | 198.8 | 43.0388 | 244.8 | 42.0727 | 252.8 | 42.4686 | 239.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | 77.1556 | 413.8 | 77.1588 | 416.6 | 79.7340 | 431.9 | 79.0770 | 431.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | 36.1277 | 416.0 | 36.1451 | 461.8 | 35.7715 | 453.6 | 36.0507 | 461.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | 47.3957 | 523.2 | 47.2846 | 542.6 | 47.2876 | 536.0 | 47.4724 | 554.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | 6.8503 | 44.9 | 6.9320 | 43.6 | 7.4726 | 100.5 | 7.6284 | 77.6 |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 4.3868 | 43.1 | 4.3550 | 43.1 | 3.5952 | 47.4 | 3.5969 | 50.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | 5.5176 | 205.6 | 5.5149 | 203.1 | 5.4700 | 219.6 | 5.4537 | 212.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | 7.6125 | 42.8 | 7.5282 | 43.4 | 9.1385 | 49.4 | 10.0719 | 46.8 |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | 5.5424 | 131.5 | 5.7580 | 134.4 | 4.1848 | 161.4 | 4.9394 | 167.6 |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | 6.4361 | 390.0 | 6.4468 | 432.9 | 5.9281 | 383.4 | 6.4478 | 431.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | 14.4507 | 48.5 | 14.4659 | 50.2 | 14.7877 | 79.6 | 14.9045 | 67.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 7.2392 | 96.1 | 7.1769 | 87.9 | 6.9887 | 107.0 | 7.0563 | 98.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | 10.7444 | 203.4 | 10.7010 | 201.8 | 10.7837 | 207.2 | 10.7261 | 207.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | 17.6321 | 205.9 | 15.0114 | 188.1 | 19.5695 | 252.1 | 19.6409 | 198.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | 8.5343 | 279.2 | 8.3413 | 240.0 | 8.5414 | 265.2 | 9.4815 | 251.8 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | 12.3285 | 448.6 | 12.2987 | 453.9 | 11.9607 | 416.2 | 12.3163 | 465.6 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | 1.8679 | 40.2 | 1.8587 | 42.2 | 1.9993 | 42.6 | 2.0163 | 43.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 1.1147 | 65.0 | 1.0945 | 61.2 | 1.0817 | 68.8 | 1.0696 | 69.6 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | 1.5314 | 200.5 | 1.5601 | 231.4 | 1.5245 | 196.0 | 1.5340 | 204.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | 2.2930 | 66.4 | 2.2957 | 49.5 | 2.7419 | 78.0 | 2.7477 | 70.6 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | 1.4861 | 78.9 | 1.4841 | 72.5 | 1.5003 | 98.8 | 1.5005 | 85.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | 1.9390 | 371.5 | 1.9741 | 371.1 | 1.9416 | 363.0 | 1.9364 | 372.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | 22.0316 | 81.8 | 22.0905 | 78.4 | 22.1240 | 113.0 | 21.9486 | 123.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 10.3651 | 59.4 | 10.3690 | 70.6 | 10.3960 | 84.6 | 10.4267 | 78.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | 16.0046 | 196.6 | 15.9747 | 205.4 | 15.8481 | 219.2 | 15.8619 | 214.8 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | 27.0459 | 291.2 | 27.1622 | 233.9 | 30.1567 | 261.0 | 29.6035 | 249.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | 12.2969 | 260.8 | 12.9018 | 269.0 | 12.9928 | 286.2 | 13.9086 | 300.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | 18.0814 | 474.1 | 18.0728 | 509.0 | 17.8192 | 464.5 | 18.1622 | 507.4 |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | 1.2612 | - | 1.2424 | - | 1.6531 | - | 1.6596 | - |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing | 2.5489 | - | 3.6515 | - | 3.6959 | - | 3.1277 | - |
| at=shared,footprint-mib=1024,host=state,k=1,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8 | 2.0609 | 51.8 | 2.0630 | 59.8 | 2.0584 | 60.6 | 2.0760 | 59.5 |
| at=shared,footprint-mib=1024,host=state,k=1,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | 1.1213 | 43.0 | 1.1215 | 46.8 | 1.1114 | 46.4 | 1.1219 | 49.4 |
| at=shared,footprint-mib=1024,host=state,k=1,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8 | 1.5518 | 199.6 | 1.5993 | 189.5 | 1.5477 | 200.2 | 1.5482 | 203.9 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8 | 2.0583 | 43.9 | 2.0562 | 43.8 | 2.0527 | 47.8 | 2.0682 | 43.0 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | 1.1214 | 43.1 | 1.1189 | 45.2 | 1.1298 | 45.6 | 1.1214 | 42.4 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8 | 1.5561 | 199.6 | 1.5632 | 199.2 | 1.5499 | 198.1 | 1.5487 | 197.8 |
| at=shared,footprint-mib=1024,host=state,k=2,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8 | 2.0576 | 56.5 | 2.0628 | 73.1 | 2.0556 | 68.6 | 2.0584 | 71.2 |
| at=shared,footprint-mib=1024,host=state,k=2,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | 1.1278 | 92.9 | 1.1336 | 85.9 | 1.1360 | 86.2 | 1.1344 | 73.2 |
| at=shared,footprint-mib=1024,host=state,k=2,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8 | 1.5456 | 217.2 | 1.5824 | 206.2 | 1.5455 | 218.2 | 1.5492 | 236.2 |
| at=shared,footprint-mib=1024,host=state,k=4,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8 | 2.0580 | 67.9 | 2.0614 | 65.1 | 2.0575 | 75.1 | 2.0579 | 72.9 |
| at=shared,footprint-mib=1024,host=state,k=4,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | 1.1470 | 44.1 | 1.1163 | 44.6 | 1.1094 | 45.0 | 1.1137 | 44.0 |
| at=shared,footprint-mib=1024,host=state,k=4,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8 | 1.5487 | 197.9 | 1.5522 | 198.8 | 1.5588 | 216.6 | 1.5498 | 205.8 |
| at=shared,footprint-mib=1024,host=state,k=64,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8 | 2.0798 | 42.6 | 2.0564 | 42.8 | 2.0576 | 48.9 | 2.0621 | 44.4 |
| at=shared,footprint-mib=1024,host=state,k=64,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | 1.1207 | 61.4 | 1.1247 | 63.1 | 1.1256 | 64.4 | 1.1215 | 62.9 |
| at=shared,footprint-mib=1024,host=state,k=64,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8 | 1.5522 | 205.0 | 1.5464 | 211.9 | 1.5634 | 203.0 | 1.5456 | 205.9 |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 3.8541 | 89.1 | 3.8948 | 128.2 | 4.0661 | 133.1 | 5.7178 | 139.9 |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | 3.9013 | 90.6 | 3.9658 | 155.5 | 4.1556 | 167.2 | 5.9050 | 177.1 |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | 68.5657 | 194.9 | 68.8248 | 299.6 | 68.6046 | 329.5 | 68.7926 | 305.2 |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | 68.5730 | 205.5 | 68.8352 | 302.1 | 68.6293 | 340.5 | 68.8512 | 323.4 |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 4.9838 | 378.2 | 5.0040 | 441.2 | 4.9936 | 446.1 | 4.9992 | 444.8 |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | 137.3523 | 672.9 | 137.3509 | 765.4 | 136.9878 | 594.8 | 137.1921 | 581.4 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 3.9615 | 108.9 | 3.8889 | 156.6 | 4.5111 | 166.9 | 5.6317 | 171.9 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | 3.8762 | 129.9 | 3.9765 | 226.0 | 4.1418 | 237.5 | 5.8736 | 236.4 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32 | 4.0900 | 94.8 | 3.8765 | 136.8 | 4.5194 | 151.5 | 5.8770 | 160.5 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=8 | 3.9924 | 142.5 | 3.9069 | 182.1 | 4.2283 | 207.2 | 6.0063 | 218.8 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | 68.5629 | 194.9 | 68.7596 | 295.0 | 68.6509 | 328.8 | 68.7901 | 293.1 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | 68.5563 | 199.1 | 68.8120 | 305.8 | 68.6261 | 320.5 | 68.8529 | 328.5 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 5.1468 | 339.1 | 5.1511 | 364.5 | 5.1112 | 400.1 | 5.1054 | 407.0 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32 | 5.1600 | 360.8 | 5.1176 | 406.1 | 5.1039 | 432.6 | 5.0276 | 432.0 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | 137.3939 | 661.2 | 137.3999 | 665.8 | 137.0367 | 599.9 | 137.2335 | 586.9 |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 3.9002 | 71.2 | 3.9151 | 123.8 | 4.1193 | 136.4 | 5.8563 | 148.9 |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | 3.8859 | 91.5 | 3.9301 | 123.1 | 4.1384 | 129.2 | 5.9704 | 139.1 |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | 68.5851 | 199.4 | 68.8129 | 295.9 | 68.5925 | 319.5 | 68.8696 | 311.5 |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | 68.5625 | 197.8 | 68.8237 | 318.2 | 68.6212 | 345.5 | 68.8317 | 318.2 |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 5.1041 | 377.6 | 5.1201 | 425.4 | 5.0779 | 462.4 | 5.0448 | 472.8 |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | 137.3827 | 664.5 | 137.3913 | 704.4 | 136.9887 | 576.9 | 137.3620 | 570.8 |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 3.9076 | 65.9 | 3.8722 | 128.5 | 4.1165 | 123.2 | 5.8087 | 166.8 |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | 3.9689 | 107.6 | 4.0066 | 154.4 | 4.1997 | 173.0 | 5.9858 | 175.0 |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | 68.5388 | 205.6 | 68.7889 | 287.6 | 68.6028 | 321.9 | 68.8492 | 318.9 |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | 68.4665 | 198.8 | 68.7030 | 296.5 | 68.5152 | 330.9 | 68.7206 | 338.0 |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 5.1474 | 344.9 | 5.1433 | 381.1 | 5.1450 | 433.0 | 5.1770 | 440.4 |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | 137.3538 | 668.6 | 137.3618 | 669.5 | 136.9997 | 629.4 | 137.2115 | 591.2 |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 4.2907 | 101.9 | 3.8651 | 145.5 | 4.9300 | 149.8 | 5.7379 | 165.6 |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | 3.8915 | 96.8 | 3.9897 | 170.6 | 4.1483 | 170.6 | 6.0504 | 157.1 |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | 68.6637 | 200.0 | 68.9113 | 299.6 | 68.7345 | 332.5 | 68.7382 | 342.1 |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | 68.4195 | 200.1 | 68.6900 | 291.9 | 68.5183 | 322.5 | 68.6835 | 330.8 |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 5.0517 | 367.0 | 5.0716 | 394.2 | 5.0568 | 411.5 | 5.0426 | 427.9 |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | 137.3848 | 666.9 | 137.4140 | 690.1 | 137.0118 | 575.8 | 137.4019 | 593.5 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 4.0167 | 123.8 | 4.0071 | 179.9 | 4.0587 | 187.0 | 4.3520 | 179.9 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 67.6677 | 227.4 | 67.6193 | 301.0 | 67.9928 | 333.1 | 67.8788 | 345.1 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | 4.5475 | 376.5 | 4.5571 | 410.4 | 4.5405 | 440.0 | 4.5312 | 460.4 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | 137.0435 | 670.2 | 137.0622 | 696.8 | 136.9737 | 636.2 | 137.0359 | 595.6 |
| at=shared,footprint-mib=11520,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 26.8081 | 278.6 | 27.4618 | 311.8 | 26.7587 | 317.0 | 27.3107 | 282.5 |
| at=shared,footprint-mib=11520,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 760.0527 | 348.0 | 759.7194 | 381.4 | 760.3656 | 379.0 | 758.9851 | 393.9 |
| at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 27.0524 | 279.8 | 27.4777 | 315.4 | 26.9351 | 317.1 | 27.6901 | 281.4 |
| at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 810.5497 | 357.4 | 810.2033 | 384.8 | 811.1004 | 374.6 | 810.1656 | 389.8 |
| at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | 33.2631 | 608.4 | 33.8531 | 601.2 | 34.1174 | 588.1 | 33.3437 | 581.6 |
| at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | 1638.5495 | 746.4 | 1638.6468 | 734.5 | 1638.4932 | 664.9 | 1638.5401 | 662.2 |
| at=shared,footprint-mib=1536,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 6.2260 | 149.4 | 6.3259 | 202.1 | 5.9544 | 214.9 | 6.3741 | 231.6 |
| at=shared,footprint-mib=1536,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 101.2576 | 208.6 | 101.2161 | 305.4 | 101.8693 | 343.1 | 101.5479 | 378.5 |
| at=shared,footprint-mib=16384,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | 25.9593 | - | 25.9141 | - | 26.5126 | - | 26.4982 | - |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 1.9223 | 137.8 | 1.9492 | 147.1 | 2.9238 | 154.8 | 3.0017 | 149.1 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 34.3278 | 320.5 | 35.4150 | 318.8 | 34.5858 | 308.5 | 34.5382 | 277.1 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1 | 39.7322 | 318.2 | 39.0150 | 341.9 | 39.0600 | 320.8 | 39.9406 | 302.9 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 1085.0418 | 373.1 | 1084.5567 | 382.9 | 1079.8406 | 370.6 | 1082.0981 | 391.0 |
| at=shared,footprint-mib=2048,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 8.5489 | 147.9 | 7.7530 | 200.4 | 7.9155 | 206.8 | 8.3015 | 208.8 |
| at=shared,footprint-mib=2048,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 135.0310 | 215.0 | 134.9601 | 325.8 | 135.5249 | 358.9 | 135.2183 | 380.8 |
| at=shared,footprint-mib=24576,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | 39.3520 | - | 39.3828 | - | 39.9645 | - | 39.9703 | - |
| at=shared,footprint-mib=24576,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 51.5498 | 390.0 | 53.0989 | 350.8 | 51.8479 | 362.9 | 53.2875 | 277.5 |
| at=shared,footprint-mib=24576,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 1625.5390 | 378.5 | 1624.8746 | 389.4 | 1623.9410 | 394.5 | 1623.8419 | 394.1 |
| at=shared,footprint-mib=256,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | 0.3104 | - | 0.3101 | - | 0.4150 | - | 0.4160 | - |
| at=shared,footprint-mib=256,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing | 0.3204 | - | 0.3130 | - | 0.8986 | - | 0.8891 | - |
| at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 1.1603 | 71.6 | 1.1542 | 99.1 | 1.1949 | 106.2 | 1.2709 | 122.1 |
| at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 16.9090 | 163.6 | 16.9028 | 216.4 | 17.1471 | 252.8 | 17.1279 | 246.0 |
| at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | 1.7007 | 72.0 | 1.6983 | 108.8 | 1.6678 | 107.1 | 1.6815 | 130.2 |
| at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | 34.6403 | 411.1 | 34.6421 | 430.6 | 34.6100 | 415.2 | 34.6537 | 406.1 |
| at=shared,footprint-mib=32768,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | 52.5533 | - | 52.5996 | - | 53.1440 | - | 53.1178 | - |
| at=shared,footprint-mib=32768,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 67.6374 | 365.6 | 68.9877 | 362.5 | 67.8635 | 356.4 | 67.0671 | 288.9 |
| at=shared,footprint-mib=32768,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 2167.8886 | 385.0 | 2166.8960 | 387.9 | 2170.7416 | 385.2 | 2166.6463 | 397.6 |
| at=shared,footprint-mib=4096,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | 5.9656 | - | 5.8902 | - | 6.6247 | - | 6.6430 | - |
| at=shared,footprint-mib=4096,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing | 14.8380 | - | 14.8517 | - | 14.8263 | - | 14.4565 | - |
| at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 14.2204 | 208.4 | 14.1488 | 246.5 | 14.1118 | 255.2 | 14.2289 | 252.9 |
| at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 269.9840 | 270.1 | 269.8766 | 361.9 | 270.4747 | 382.6 | 270.0742 | 385.4 |
| at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | 14.4448 | 509.9 | 15.3010 | 551.1 | 14.4034 | 556.6 | 14.6843 | 567.6 |
| at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | 546.5900 | 724.0 | 546.6194 | 724.9 | 546.6468 | 666.6 | 546.5652 | 687.1 |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=1,tiling=tiles,type=four,vary=sharing | 27.1891 | - | 27.1735 | - | 28.2504 | - | 28.2757 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=16,tiling=tiles,type=four,vary=sharing | 27.3129 | - | 27.2966 | - | 28.2752 | - | 28.3012 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=2,tiling=tiles,type=four,vary=sharing | 27.2524 | - | 27.2317 | - | 28.2781 | - | 28.2854 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=4,tiling=tiles,type=four,vary=sharing | 27.2509 | - | 27.2347 | - | 28.3018 | - | 28.3032 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=64,tiling=tiles,type=four,vary=sharing | 27.5344 | - | 27.5159 | - | 28.1793 | - | 28.2061 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing | 27.3058 | - | 27.2762 | - | 28.2377 | - | 28.2927 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=1,tiling=tiles,type=four,vary=sharing | 62.8468 | - | 62.9561 | - | 62.3991 | - | 62.4713 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=16,tiling=tiles,type=four,vary=sharing | 62.9381 | - | 62.9776 | - | 62.5295 | - | 62.6445 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=2,tiling=tiles,type=four,vary=sharing | 62.8692 | - | 62.9408 | - | 62.4135 | - | 62.4728 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=4,tiling=tiles,type=four,vary=sharing | 62.8296 | - | 62.9433 | - | 62.4435 | - | 62.4971 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=64,tiling=tiles,type=four,vary=sharing | 63.0740 | - | 63.0755 | - | 63.0578 | - | 63.0402 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing | 62.9167 | - | 62.9678 | - | 62.5047 | - | 62.5246 | - |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=1,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.1445 | 78.8 | 2.1329 | 118.6 | 2.2509 | 149.6 | 2.3045 | 146.2 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=16,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.2374 | 104.2 | 2.1577 | 119.9 | 2.2403 | 120.1 | 2.3424 | 119.4 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=2,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.1831 | 71.6 | 2.1596 | 101.8 | 2.3415 | 114.9 | 2.3387 | 109.6 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=4,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.1753 | 106.8 | 2.1397 | 145.0 | 2.2535 | 173.6 | 2.3385 | 166.8 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=64,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.1368 | 96.1 | 2.1512 | 134.6 | 2.1826 | 146.6 | 2.1729 | 131.0 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.2137 | 73.0 | 2.1430 | 103.5 | 2.2600 | 104.1 | 2.3272 | 104.6 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.1735 | 88.0 | 2.1307 | 126.6 | 2.1785 | 137.4 | 2.3264 | 137.1 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=1,tiling=tiles,type=four,vary=sharing,w=1 | 33.8788 | 188.4 | 33.8178 | 269.8 | 34.0710 | 253.4 | 34.3424 | 300.4 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=16,tiling=tiles,type=four,vary=sharing,w=1 | 33.9340 | 178.9 | 33.8941 | 264.2 | 34.1140 | 264.4 | 34.3276 | 289.4 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=2,tiling=tiles,type=four,vary=sharing,w=1 | 33.8747 | 190.2 | 33.7906 | 271.0 | 34.0836 | 270.0 | 34.3252 | 318.5 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=4,tiling=tiles,type=four,vary=sharing,w=1 | 33.9738 | 190.0 | 33.8462 | 295.1 | 34.1207 | 298.2 | 34.2908 | 347.0 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=64,tiling=tiles,type=four,vary=sharing,w=1 | 33.9884 | 180.2 | 33.9280 | 322.0 | 34.1576 | 326.6 | 34.3620 | 321.1 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1 | 33.8480 | 183.1 | 33.7658 | 268.5 | 34.0078 | 274.6 | 34.2837 | 303.0 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=1,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.5839 | 168.8 | 2.5821 | 196.4 | 2.5515 | 229.9 | 2.5232 | 224.4 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=16,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.9313 | 197.1 | 2.9418 | 275.5 | 2.8742 | 272.5 | 2.8764 | 268.1 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=2,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.9065 | 190.4 | 2.9033 | 194.9 | 2.7737 | 227.1 | 2.7477 | 210.6 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=4,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.9461 | 186.9 | 2.9651 | 232.9 | 2.9157 | 251.5 | 2.8807 | 238.8 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=64,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.6282 | 225.4 | 2.6308 | 258.2 | 2.6051 | 280.5 | 2.6081 | 304.2 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.5893 | 207.8 | 2.5900 | 231.0 | 2.5689 | 266.9 | 2.5905 | 247.0 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.9310 | 212.1 | 3.0051 | 242.2 | 2.8846 | 260.5 | 2.9133 | 245.5 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=1,tiling=tiles,type=four,vary=sharing,w=1 | 68.8983 | 554.4 | 68.8725 | 555.8 | 68.7653 | 545.5 | 68.9083 | 554.1 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=16,tiling=tiles,type=four,vary=sharing,w=1 | 68.9263 | 522.1 | 68.9142 | 581.8 | 68.9030 | 561.8 | 68.8670 | 573.5 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=2,tiling=tiles,type=four,vary=sharing,w=1 | 68.9241 | 551.1 | 68.8980 | 563.9 | 68.9090 | 544.5 | 68.8982 | 551.5 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=4,tiling=tiles,type=four,vary=sharing,w=1 | 68.9676 | 539.1 | 68.9320 | 563.8 | 68.8683 | 657.8 | 68.9415 | 646.4 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=64,tiling=tiles,type=four,vary=sharing,w=1 | 68.8964 | 542.9 | 68.9190 | 597.9 | 68.9247 | 650.6 | 68.9180 | 646.2 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1 | 68.9135 | 500.2 | 68.8654 | 532.2 | 68.8626 | 522.6 | 68.8755 | 546.5 |
| at=shared,footprint-mib=8192,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | 12.4018 | - | 12.4340 | - | 13.2628 | - | 13.2495 | - |
| at=shared,footprint-mib=8192,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing | 29.6596 | - | 29.6703 | - | 29.6544 | - | 29.6732 | - |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 23.5255 | 246.8 | 23.4560 | 271.4 | 23.8554 | 281.2 | 24.4788 | 269.1 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 540.2856 | 342.9 | 540.0302 | 373.6 | 540.7495 | 405.1 | 539.8879 | 389.1 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | 23.9493 | 557.6 | 23.4413 | 576.4 | 23.8211 | 573.0 | 23.9853 | 596.8 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1 | 23.4869 | 548.6 | 23.3524 | 572.0 | 23.7906 | 586.0 | 23.7879 | 583.1 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | 1092.6554 | 742.5 | 1092.7341 | 734.9 | 1092.8771 | 666.8 | 1092.6264 | 651.4 |
| at=shared,footprint-mib=9728,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 26.2656 | 276.6 | 27.0279 | 288.9 | 26.6859 | 291.8 | 26.6900 | 278.9 |
| at=shared,footprint-mib=9728,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 641.1709 | 352.8 | 640.9570 | 375.0 | 642.0839 | 401.6 | 641.2903 | 383.2 |

## Per cell

### route/at=1,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x441b40000000, copy home 0x441c40000000, direct level 0x441d00000000, copy level 0x441dc0000000
- factor effect within the cell: on the direct route -0.0002 [-0.0002, -0.0002] ms, on the copy route -0.0005 [-0.0008, -0.0003] ms; change relative to the copy call at home: +0.6 %
- per repetition: direct home 8.38e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.7 SMMU translation requests; direct level 8.38e+06 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=four,vary=rotated,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x58d6c0000000, copy home 0x58d7c0000000, direct level 0x58d880000000, copy level 0x58d940000000
- factor effect within the cell: on the direct route 0.0001 [0.0001, 0.0001] ms, on the copy route 0.0001 [-0.0001, 0.0003] ms; change relative to the copy call at home: +0.1 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 134.2 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=k,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 1.0568 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5eef80000000, copy home 0x5ef040000000, direct level 0x5ef100000000, copy level 0x5ef1c0000000
- factor effect within the cell: on the direct route -1.4011 [-1.4016, -1.4004] ms, on the copy route -0.0602 [-0.0603, -0.0601] ms; change relative to the copy call at home: -730.9 %
- per repetition: direct home 5.365e+08 link read bytes and 0 SMMU translation requests; copy home 3.354e+07 link read bytes and 532.9 SMMU translation requests; direct level 3.354e+07 link read bytes and 0 SMMU translation requests; copy level 3.354e+07 link read bytes and 533 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x447d00000000, copy home 0x447dc0000000, direct level 0x447e80000000, copy level 0x447f40000000
- factor effect within the cell: on the direct route 0.3318 [0.3312, 0.3320] ms, on the copy route 0.0145 [0.0141, 0.0153] ms; change relative to the copy call at home: +522.0 %
- per repetition: direct home 8.382e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.7 SMMU translation requests; direct level 1.341e+08 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=four,vary=k,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 1.0568 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x48f100000000, copy home 0x48f200000000, direct level 0x48f2c0000000, copy level 0x48f380000000
- factor effect within the cell: on the direct route -0.0798 [-0.0798, -0.0797] ms, on the copy route -0.0597 [-0.0600, -0.0595] ms; change relative to the copy call at home: -11.2 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 519.8 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 519.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=four,vary=rotated,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4ecf80000000, copy home 0x4ed0c0000000, direct level 0x4ed180000000, copy level 0x4ed240000000
- factor effect within the cell: on the direct route 0.0141 [0.0140, 0.0141] ms, on the copy route 0.0165 [0.0164, 0.0167] ms; change relative to the copy call at home: -4.3 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 134.5 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 135 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4e72c0000000, copy home 0x4e73c0000000, direct level 0x4e7480000000, copy level 0x4e7540000000
- factor effect within the cell: on the direct route 0.0221 [0.0221, 0.0222] ms, on the copy route 0.0005 [0.0004, 0.0007] ms; change relative to the copy call at home: +40.0 %
- per repetition: direct home 8.382e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.7 SMMU translation requests; direct level 1.676e+07 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=four,vary=rotated,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x451980000000, copy home 0x451a40000000, direct level 0x451b00000000, copy level 0x451bc0000000
- factor effect within the cell: on the direct route 0.0009 [0.0009, 0.0009] ms, on the copy route 0.0001 [-0.0002, 0.0002] ms; change relative to the copy call at home: +1.7 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 134 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x599640000000, copy home 0x599740000000, direct level 0x599800000000, copy level 0x5998c0000000
- factor effect within the cell: on the direct route 0.0669 [0.0668, 0.0669] ms, on the copy route 0.0036 [0.0030, 0.0041] ms; change relative to the copy call at home: +115.6 %
- per repetition: direct home 8.382e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.7 SMMU translation requests; direct level 3.352e+07 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=four,vary=rotated,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4d1140000000, copy home 0x4d12c0000000, direct level 0x4d1380000000, copy level 0x4d1440000000
- factor effect within the cell: on the direct route 0.0028 [0.0028, 0.0028] ms, on the copy route 0.0082 [0.0080, 0.0086] ms; change relative to the copy call at home: -10.8 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 134.2 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4309c0000000, copy home 0x430ac0000000, direct level 0x430b80000000, copy level 0x430c40000000
- factor effect within the cell: on the direct route 1.3883 [1.3824, 1.3930] ms, on the copy route 0.0496 [0.0492, 0.0500] ms; change relative to the copy call at home: +1577.1 %
- per repetition: direct home 8.382e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.7 SMMU translation requests; direct level 5.363e+08 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=four,vary=rotated,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x531540000000, copy home 0x531680000000, direct level 0x531740000000, copy level 0x531800000000
- factor effect within the cell: on the direct route 0.0522 [0.0521, 0.0522] ms, on the copy route 0.0502 [0.0499, 0.0504] ms; change relative to the copy call at home: +2.3 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 135.1 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 135.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sweeps

- seed 73; every round ran in the drawn order: yes; floor 1.0568 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x403440000000, copy home 0x403540000000, direct level 0x403600000000, copy level 0x403700000000
- factor effect within the cell: on the direct route -23.2353 [-23.2448, -23.2030] ms, on the copy route -2.8837 [-2.8890, -2.8787] ms; change relative to the copy call at home: -312.6 %
- per repetition: direct home 6.422e+09 link read bytes and 3.619e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 8.028e+08 link read bytes and 3180 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sweeps

- seed 73; every round ran in the drawn order: yes; floor 1.0568 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5a9180000000, copy home 0x5a9280000000, direct level 0x5a9340000000, copy level 0x5a9440000000
- factor effect within the cell: on the direct route -2.8787 [-2.8800, -2.8755] ms, on the copy route -2.8289 [-2.8336, -2.8213] ms; change relative to the copy call at home: -1.3 %
- per repetition: direct home 0 link read bytes and 5522 SMMU translation requests; copy home 0 link read bytes and 5504 SMMU translation requests; direct level 0 link read bytes and 575.5 SMMU translation requests; copy level 0 link read bytes and 1644 SMMU translation requests; multiplexed rows voided: 0

### route/at=16384,footprint-mib=1024,kernel=k3,placement=cpu,type=four,vary=footprint

- seed 73; every round ran in the drawn order: yes; floor 1.0568 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x591980000000, copy home 0x591a80000000, direct level 0x591b40000000, copy level 0x592000000000
- factor effect within the cell: on the direct route 427.4383 [427.3457, 427.4938] ms, on the copy route 41.3873 [41.3718, 41.3958] ms; change relative to the copy call at home: +11312.0 %
- per repetition: direct home 5.369e+08 link read bytes and 4342 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.64e+04 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy level 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=16384,footprint-mib=1024,kernel=k3,placement=hbm,type=four,vary=footprint

- seed 73; every round ran in the drawn order: yes; floor 1.0568 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x50bf00000000, copy home 0x50c040000000, direct level 0x50c100000000, copy level 0x50c5c0000000
- factor effect within the cell: on the direct route 424.6250 [424.4107, 424.8268] ms, on the copy route 9.5090 [9.4988, 9.5321] ms; change relative to the copy call at home: +37023.7 %
- per repetition: direct home 0 link read bytes and 403.8 SMMU translation requests; copy home 0 link read bytes and 2714 SMMU translation requests; direct level 0 link read bytes and 1.207e+08 SMMU translation requests; copy level 0 link read bytes and 6.566e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=f

- seed 73; every round ran in the drawn order: yes; floor 1.0568 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x55e440000000, copy home 0x55e540000000, direct level 0x55e600000000, copy level 0x55e6c0000000
- factor effect within the cell: on the direct route -2.8740 [-2.8746, -2.8734] ms, on the copy route -3.2230 [-3.2243, -3.2225] ms; change relative to the copy call at home: +10.7 %
- per repetition: direct home 1.074e+09 link read bytes and 0 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.64e+04 SMMU translation requests; direct level 1.074e+07 link read bytes and 0 SMMU translation requests; copy level 1.074e+07 link read bytes and 0.04178 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=four,vary=f

- seed 73; every round ran in the drawn order: yes; floor 1.0568 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4c17c0000000, copy home 0x4c18c0000000, direct level 0x4c1980000000, copy level 0x4c1a40000000
- factor effect within the cell: on the direct route -0.2879 [-0.2880, -0.2878] ms, on the copy route -0.9136 [-0.9142, -0.9122] ms; change relative to the copy call at home: +66.1 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 0 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=11520,kernel=k3,placement=cpu,type=four,vary=partition

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x54b500000000, copy home 0x54b880000000, direct level 0x54bbc0000000, copy level 0x54bf40000000
- factor effect within the cell: on the direct route -234.3764 [-234.5276, -233.9641] ms, on the copy route -1.8014 [-1.8097, -1.7783] ms; change relative to the copy call at home: -707.3 %
- per repetition: direct home 5.369e+08 link read bytes and 6.723e+07 SMMU translation requests; copy home 1.211e+10 link read bytes and 1.843e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.887e+05 SMMU translation requests; copy level 1.211e+10 link read bytes and 1.843e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=12288,kernel=k3,placement=cpu,type=four,vary=partition

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x49cdc0000000, copy home 0x49d180000000, direct level 0x49d500000000, copy level 0x49d8c0000000
- factor effect within the cell: on the direct route -273.6145 [-273.6891, -273.5708] ms, on the copy route -1.8264 [-1.8379, -1.8092] ms; change relative to the copy call at home: -780.1 %
- per repetition: direct home 5.369e+08 link read bytes and 7.819e+07 SMMU translation requests; copy home 1.292e+10 link read bytes and 1.966e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 2.013e+05 SMMU translation requests; copy level 1.292e+10 link read bytes and 1.966e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=12288,kernel=k3,placement=hbm,type=four,vary=partition

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x497b00000000, copy home 0x497e80000000, direct level 0x498200000000, copy level 0x498600000000
- factor effect within the cell: on the direct route -119.0859 [-120.3959, -117.0995] ms, on the copy route 0.1743 [0.1581, 0.1843] ms; change relative to the copy call at home: -1473.2 %
- per repetition: direct home 0 link read bytes and 7.776e+07 SMMU translation requests; copy home 0 link read bytes and 4.585e+05 SMMU translation requests; direct level 0 link read bytes and 4.524e+07 SMMU translation requests; copy level 0 link read bytes and 4.581e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=partition

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5ac240000000, copy home 0x5ac700000000, direct level 0x5acb80000000, copy level 0x5ad040000000
- factor effect within the cell: on the direct route -426.9297 [-427.0261, -426.8856] ms, on the copy route -3.2877 [-3.2960, -3.2767] ms; change relative to the copy call at home: -915.6 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 3.7e+05 SMMU translation requests; copy level 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=24576,kernel=k3,placement=cpu,type=four,vary=partition

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x581300000000, copy home 0x581980000000, direct level 0x582000000000, copy level 0x5826c0000000
- factor effect within the cell: on the direct route -591.7312 [-591.8175, -591.6368] ms, on the copy route -2.0543 [-2.0606, -2.0504] ms; change relative to the copy call at home: -893.6 %
- per repetition: direct home 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; copy home 2.585e+10 link read bytes and 3.933e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 8.794e+05 SMMU translation requests; copy level 2.585e+10 link read bytes and 3.933e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=32768,kernel=k3,placement=cpu,type=four,vary=partition

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x5c2380000000, copy home 0x5c2c00000000, direct level 0x5c3480000000, copy level 0x5c3d40000000
- factor effect within the cell: on the direct route -673.3172 [-673.7639, -672.8954] ms, on the copy route -1.3793 [-1.3861, -1.3718] ms; change relative to the copy call at home: -776.0 %
- per repetition: direct home 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; copy home 3.448e+10 link read bytes and 5.244e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 2.592e+06 SMMU translation requests; copy level 3.448e+10 link read bytes and 5.244e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=4096,kernel=k3,placement=cpu,type=four,vary=partition

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5e9dc0000000, copy home 0x5e9f40000000, direct level 0x5ea0c0000000, copy level 0x5ea280000000
- factor effect within the cell: on the direct route -0.0143 [-0.0455, 0.0371] ms, on the copy route 0.1748 [0.1720, 0.1839] ms; change relative to the copy call at home: -1.7 %
- per repetition: direct home 5.369e+08 link read bytes and 1243 SMMU translation requests; copy home 4.295e+09 link read bytes and 6.556e+04 SMMU translation requests; direct level 5.369e+08 link read bytes and 1691 SMMU translation requests; copy level 4.295e+09 link read bytes and 6.556e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=4096,kernel=k3,placement=hbm,type=four,vary=partition

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4f8a00000000, copy home 0x4f8b80000000, direct level 0x4f8d00000000, copy level 0x4f8ec0000000
- factor effect within the cell: on the direct route -1.4389 [-1.4698, -1.3659] ms, on the copy route 0.1760 [0.1695, 0.1804] ms; change relative to the copy call at home: -53.1 %
- per repetition: direct home 0 link read bytes and 1.66e+04 SMMU translation requests; copy home 0 link read bytes and 2.474e+04 SMMU translation requests; direct level 0 link read bytes and 1.123e+04 SMMU translation requests; copy level 0 link read bytes and 2.418e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=8192,kernel=k3,placement=cpu,type=four,vary=partition

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4fe640000000, copy home 0x4fe900000000, direct level 0x4feb80000000, copy level 0x4fee40000000
- factor effect within the cell: on the direct route -2.3078 [-2.3347, -2.1670] ms, on the copy route -0.9010 [-0.9217, -0.8887] ms; change relative to the copy call at home: -5.6 %
- per repetition: direct home 5.369e+08 link read bytes and 4.417e+04 SMMU translation requests; copy home 8.607e+09 link read bytes and 1.311e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 3.416e+04 SMMU translation requests; copy level 8.607e+09 link read bytes and 1.311e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=8192,kernel=k3,placement=hbm,type=four,vary=partition

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x504800000000, copy home 0x504ac0000000, direct level 0x504d40000000, copy level 0x505000000000
- factor effect within the cell: on the direct route -1.9856 [-2.0141, -1.9375] ms, on the copy route 0.1842 [0.1766, 0.1919] ms; change relative to the copy call at home: -39.0 %
- per repetition: direct home 0 link read bytes and 4.428e+04 SMMU translation requests; copy home 0 link read bytes and 1.152e+05 SMMU translation requests; direct level 0 link read bytes and 3.492e+04 SMMU translation requests; copy level 0 link read bytes and 1.173e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=9728,kernel=k3,placement=cpu,type=four,vary=partition

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x53e080000000, copy home 0x53e380000000, direct level 0x53e680000000, copy level 0x53e980000000
- factor effect within the cell: on the direct route -122.5959 [-122.6990, -122.5438] ms, on the copy route 0.1614 [0.1311, 0.1841] ms; change relative to the copy call at home: -448.8 %
- per repetition: direct home 5.369e+08 link read bytes and 3.597e+07 SMMU translation requests; copy home 1.02e+10 link read bytes and 1.625e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.313e+05 SMMU translation requests; copy level 1.02e+10 link read bytes and 1.628e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-order

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x435580000000, copy home 0x435a00000000, direct level 0x435e80000000, copy level 0x436340000000
- factor effect within the cell: on the direct route -427.4381 [-427.5590, -427.4010] ms, on the copy route -3.5789 [-3.5953, -3.5580] ms; change relative to the copy call at home: -915.7 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; direct level 5.368e+08 link read bytes and 6.28e+05 SMMU translation requests; copy level 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=1024,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4659c0000000, copy home 0x465ac0000000, direct level 0x465b80000000, copy level 0x465c80000000
- factor effect within the cell: on the direct route -0.0390 [-0.0396, -0.0382] ms, on the copy route -0.2965 [-0.2992, -0.2951] ms; change relative to the copy call at home: +7.5 %
- per repetition: direct home 5.369e+08 link read bytes and 0 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.641e+04 SMMU translation requests; direct level 5.369e+08 link read bytes and 0 SMMU translation requests; copy level 1.074e+09 link read bytes and 51.14 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=1024,kernel=k3,placement=hbm,type=four,vary=page-size

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4aba40000000, copy home 0x4abb00000000, direct level 0x4abbc0000000, copy level 0x4abd00000000
- factor effect within the cell: on the direct route -0.0006 [-0.0007, -0.0004] ms, on the copy route -0.0044 [-0.0048, -0.0025] ms; change relative to the copy call at home: +0.3 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 0 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=11520,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x480e00000000, copy home 0x481180000000, direct level 0x4814c0000000, copy level 0x481880000000
- factor effect within the cell: on the direct route -234.3420 [-234.4143, -234.2376] ms, on the copy route -2.6057 [-2.6203, -2.5916] ms; change relative to the copy call at home: -707.8 %
- per repetition: direct home 5.369e+08 link read bytes and 6.714e+07 SMMU translation requests; copy home 1.211e+10 link read bytes and 1.843e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 111.1 SMMU translation requests; copy level 1.211e+10 link read bytes and 379 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=12288,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x574f80000000, copy home 0x575300000000, direct level 0x575680000000, copy level 0x575a40000000
- factor effect within the cell: on the direct route -274.1501 [-274.2430, -274.0056] ms, on the copy route -2.8142 [-2.8345, -2.7951] ms; change relative to the copy call at home: -777.1 %
- per repetition: direct home 5.369e+08 link read bytes and 7.814e+07 SMMU translation requests; copy home 1.292e+10 link read bytes and 1.966e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 116.5 SMMU translation requests; copy level 1.292e+10 link read bytes and 404 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=1536,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x526740000000, copy home 0x526840000000, direct level 0x526940000000, copy level 0x526a40000000
- factor effect within the cell: on the direct route -0.0219 [-0.0225, -0.0215] ms, on the copy route -0.3632 [-0.3644, -0.3591] ms; change relative to the copy call at home: +7.1 %
- per repetition: direct home 5.369e+08 link read bytes and 0 SMMU translation requests; copy home 1.611e+09 link read bytes and 2.46e+04 SMMU translation requests; direct level 5.369e+08 link read bytes and 0 SMMU translation requests; copy level 1.611e+09 link read bytes and 67 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5269c0000000, copy home 0x526e40000000, direct level 0x5272c0000000, copy level 0x527780000000
- factor effect within the cell: on the direct route -427.3498 [-427.4610, -427.2914] ms, on the copy route -3.8620 [-3.8884, -3.8520] ms; change relative to the copy call at home: -910.7 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 148.1 SMMU translation requests; copy level 1.723e+10 link read bytes and 532 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=16384,kernel=k3p,placement=cpu,type=four,vary=page-size

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5d7840000000, copy home 0x5d7d00000000, direct level 0x5d8180000000, copy level 0x5d8600000000
- factor effect within the cell: on the direct route -6.9321 [-6.9419, -6.9236] ms, on the copy route -4.1249 [-4.1292, -4.1137] ms; change relative to the copy call at home: -6.1 %
- per repetition: direct home 3.355e+07 link read bytes and 1.962e+06 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; direct level 3.355e+07 link read bytes and 2.988 SMMU translation requests; copy level 1.723e+10 link read bytes and 531 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=2048,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4ed940000000, copy home 0x4eda80000000, direct level 0x4edb80000000, copy level 0x4edcc0000000
- factor effect within the cell: on the direct route -0.0148 [-0.0154, -0.0145] ms, on the copy route -0.4638 [-0.4650, -0.4603] ms; change relative to the copy call at home: +7.2 %
- per repetition: direct home 5.369e+08 link read bytes and 0 SMMU translation requests; copy home 2.147e+09 link read bytes and 3.279e+04 SMMU translation requests; direct level 5.369e+08 link read bytes and 0 SMMU translation requests; copy level 2.147e+09 link read bytes and 83 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=24576,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5dad00000000, copy home 0x5db3c0000000, direct level 0x5dba40000000, copy level 0x5dc100000000
- factor effect within the cell: on the direct route -592.8810 [-592.9529, -592.7908] ms, on the copy route -1.9857 [-1.9971, -1.9570] ms; change relative to the copy call at home: -899.9 %
- per repetition: direct home 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; copy home 2.585e+10 link read bytes and 3.932e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 214.6 SMMU translation requests; copy level 2.585e+10 link read bytes and 788 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=256,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x418a00000000, copy home 0x418b00000000, direct level 0x418bc0000000, copy level 0x418c80000000
- factor effect within the cell: on the direct route -0.1895 [-0.1905, -0.1889] ms, on the copy route -0.0976 [-0.0993, -0.0969] ms; change relative to the copy call at home: -7.6 %
- per repetition: direct home 5.368e+08 link read bytes and 0 SMMU translation requests; copy home 2.684e+08 link read bytes and 4116 SMMU translation requests; direct level 5.368e+08 link read bytes and 0 SMMU translation requests; copy level 2.684e+08 link read bytes and 26.89 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=256,kernel=k3,placement=hbm,type=four,vary=page-size

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5f7340000000, copy home 0x5f7440000000, direct level 0x5f74c0000000, copy level 0x5f75c0000000
- factor effect within the cell: on the direct route -0.0036 [-0.0038, -0.0034] ms, on the copy route -0.0003 [-0.0014, 0.0002] ms; change relative to the copy call at home: -0.3 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 4116 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 27.42 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=32768,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x58b480000000, copy home 0x58bd00000000, direct level 0x58c580000000, copy level 0x58ce40000000
- factor effect within the cell: on the direct route -679.6850 [-679.7325, -679.6335] ms, on the copy route -1.2324 [-1.2425, -1.2079] ms; change relative to the copy call at home: -789.2 %
- per repetition: direct home 5.369e+08 link read bytes and 1.912e+08 SMMU translation requests; copy home 3.448e+10 link read bytes and 5.244e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 278.4 SMMU translation requests; copy level 3.448e+10 link read bytes and 1043 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=4096,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4968c0000000, copy home 0x496a40000000, direct level 0x496bc0000000, copy level 0x496d80000000
- factor effect within the cell: on the direct route -0.1337 [-0.1711, -0.1062] ms, on the copy route -0.9602 [-0.9669, -0.9525] ms; change relative to the copy call at home: +6.8 %
- per repetition: direct home 5.369e+08 link read bytes and 0 SMMU translation requests; copy home 4.295e+09 link read bytes and 6.556e+04 SMMU translation requests; direct level 5.369e+08 link read bytes and 0 SMMU translation requests; copy level 4.295e+09 link read bytes and 147.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=4096,kernel=k3,placement=hbm,type=four,vary=page-size

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x513300000000, copy home 0x5134c0000000, direct level 0x513640000000, copy level 0x513800000000
- factor effect within the cell: on the direct route -4.6574 [-4.6590, -4.6487] ms, on the copy route -0.0060 [-0.0208, -0.0010] ms; change relative to the copy call at home: -152.8 %
- per repetition: direct home 0 link read bytes and 3410 SMMU translation requests; copy home 0 link read bytes and 4893 SMMU translation requests; direct level 0 link read bytes and 2.25 SMMU translation requests; copy level 0 link read bytes and 23.29 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=8192,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4d4ac0000000, copy home 0x4d4d40000000, direct level 0x4d4fc0000000, copy level 0x4d5280000000
- factor effect within the cell: on the direct route -2.3763 [-2.3802, -2.3673] ms, on the copy route -1.9052 [-1.9152, -1.9014] ms; change relative to the copy call at home: -2.0 %
- per repetition: direct home 5.369e+08 link read bytes and 7903 SMMU translation requests; copy home 8.607e+09 link read bytes and 1.311e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 83 SMMU translation requests; copy level 8.607e+09 link read bytes and 276 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=8192,kernel=k3,placement=hbm,type=four,vary=page-size

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x463a80000000, copy home 0x463d00000000, direct level 0x463f80000000, copy level 0x464240000000
- factor effect within the cell: on the direct route -7.3338 [-7.3390, -7.2178] ms, on the copy route -0.0179 [-0.0308, 0.0021] ms; change relative to the copy call at home: -130.8 %
- per repetition: direct home 0 link read bytes and 4.419e+04 SMMU translation requests; copy home 0 link read bytes and 1.131e+05 SMMU translation requests; direct level 0 link read bytes and 8.024 SMMU translation requests; copy level 0 link read bytes and 74.38 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=9728,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5a82c0000000, copy home 0x5a85c0000000, direct level 0x5a88c0000000, copy level 0x5a8c00000000
- factor effect within the cell: on the direct route -123.0572 [-123.1132, -122.9883] ms, on the copy route -0.6026 [-0.6542, -0.5348] ms; change relative to the copy call at home: -447.3 %
- per repetition: direct home 5.369e+08 link read bytes and 3.597e+07 SMMU translation requests; copy home 1.02e+10 link read bytes and 1.622e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 96.25 SMMU translation requests; copy level 1.02e+10 link read bytes and 321 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x45a800000000, copy home 0x45a8c0000000, direct level 0x45a980000000, copy level 0x45aa40000000
- factor effect within the cell: on the direct route -0.0706 [-0.0707, -0.0706] ms, on the copy route -0.0777 [-0.0781, -0.0769] ms; change relative to the copy call at home: +5.4 %
- per repetition: direct home 3.354e+07 link read bytes and 0 SMMU translation requests; copy home 3.354e+07 link read bytes and 533 SMMU translation requests; direct level 8.38e+06 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5a6e40000000, copy home 0x5a6f40000000, direct level 0x5a7000000000, copy level 0x5a70c0000000
- factor effect within the cell: on the direct route -0.0086 [-0.0086, -0.0086] ms, on the copy route -0.0690 [-0.0692, -0.0686] ms; change relative to the copy call at home: +50.5 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 520.2 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4da900000000, copy home 0x4da9c0000000, direct level 0x4daa80000000, copy level 0x4dab40000000
- factor effect within the cell: on the direct route -1.4630 [-1.4634, -1.4625] ms, on the copy route -0.1222 [-0.1228, -0.1214] ms; change relative to the copy call at home: -734.5 %
- per repetition: direct home 5.365e+08 link read bytes and 0 SMMU translation requests; copy home 3.354e+07 link read bytes and 533.1 SMMU translation requests; direct level 8.382e+06 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x517440000000, copy home 0x517540000000, direct level 0x517600000000, copy level 0x5176c0000000
- factor effect within the cell: on the direct route -0.0815 [-0.0816, -0.0815] ms, on the copy route -0.1229 [-0.1231, -0.1227] ms; change relative to the copy call at home: +22.8 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 520.6 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x510e80000000, copy home 0x510f80000000, direct level 0x511040000000, copy level 0x511100000000
- factor effect within the cell: on the direct route -0.1628 [-0.1629, -0.1628] ms, on the copy route -0.0785 [-0.0788, -0.0781] ms; change relative to the copy call at home: -63.9 %
- per repetition: direct home 6.708e+07 link read bytes and 0 SMMU translation requests; copy home 3.354e+07 link read bytes and 533 SMMU translation requests; direct level 8.382e+06 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x506700000000, copy home 0x5067c0000000, direct level 0x506880000000, copy level 0x506940000000
- factor effect within the cell: on the direct route -0.0140 [-0.0140, -0.0140] ms, on the copy route -0.0743 [-0.0753, -0.0738] ms; change relative to the copy call at home: +48.4 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 519.4 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5a14c0000000, copy home 0x5a15c0000000, direct level 0x5a1680000000, copy level 0x5a1740000000
- factor effect within the cell: on the direct route -0.3455 [-0.3456, -0.3454] ms, on the copy route -0.0879 [-0.0883, -0.0876] ms; change relative to the copy call at home: -180.9 %
- per repetition: direct home 1.342e+08 link read bytes and 0 SMMU translation requests; copy home 3.354e+07 link read bytes and 533.1 SMMU translation requests; direct level 8.382e+06 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5c6940000000, copy home 0x5c6a40000000, direct level 0x5c6b00000000, copy level 0x5c6bc0000000
- factor effect within the cell: on the direct route -0.0238 [-0.0238, -0.0238] ms, on the copy route -0.0835 [-0.0837, -0.0832] ms; change relative to the copy call at home: +44.7 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 519.6 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x55c180000000, copy home 0x55c280000000, direct level 0x55c340000000, copy level 0x55c400000000
- factor effect within the cell: on the direct route -5.9146 [-5.9236, -5.9092] ms, on the copy route -0.2997 [-0.3009, -0.2992] ms; change relative to the copy call at home: -1461.6 %
- per repetition: direct home 2.145e+09 link read bytes and 0 SMMU translation requests; copy home 3.354e+07 link read bytes and 533.1 SMMU translation requests; direct level 8.382e+06 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x414a00000000, copy home 0x414b00000000, direct level 0x414bc0000000, copy level 0x414c80000000
- factor effect within the cell: on the direct route -0.3062 [-0.3067, -0.3056] ms, on the copy route -0.2904 [-0.2911, -0.2900] ms; change relative to the copy call at home: -4.2 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 524.6 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=hbm,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=placement

- seed 73; every round ran in the drawn order: yes; floor 1.0568 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement hbm; buffers: direct home 0x581080000000, copy home 0x581180000000, direct level 0x581240000000, copy level 0x581300000000
- factor effect within the cell: on the direct route -2.6156 [-2.6170, -2.6146] ms, on the copy route -2.3146 [-2.3172, -2.3136] ms; change relative to the copy call at home: -9.2 %
- per repetition: direct home 1.074e+09 link read bytes and 0 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.64e+04 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 0.7273 SMMU translation requests; multiplexed rows voided: 0

### route/at=none,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=tiling

- seed 73; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5cf280000000, copy home 0x5cf380000000, direct level 0x5cf440000000, copy level 0x5cf540000000
- factor effect within the cell: on the direct route 9.5563 [9.2308, 9.5882] ms, on the copy route -0.5648 [-0.5696, -0.5538] ms; change relative to the copy call at home: +155.7 %
- per repetition: direct home 6.422e+09 link read bytes and 3.601e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 1.307e+10 link read bytes and 3.571e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=none,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=tiling

- seed 73; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x445fc0000000, copy home 0x4460c0000000, direct level 0x446180000000, copy level 0x446280000000
- factor effect within the cell: on the direct route -0.5203 [-0.5239, -0.5099] ms, on the copy route -0.4626 [-0.4706, -0.4557] ms; change relative to the copy call at home: -1.4 %
- per repetition: direct home 0 link read bytes and 5481 SMMU translation requests; copy home 0 link read bytes and 5457 SMMU translation requests; direct level 0 link read bytes and 9078 SMMU translation requests; copy level 0 link read bytes and 5399 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=8192,kernel=k3,placement=cpu,type=four,vary=alignment

- seed 73; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4aed40000000, copy home 0x4af000000000, direct level 0x4af420000000, copy level 0x4afc20000000
- factor effect within the cell: on the direct route 40.7394 [40.3753, 40.8935] ms, on the copy route -0.2670 [-0.2754, -0.2570] ms; change relative to the copy call at home: +174.5 %
- per repetition: direct home 5.369e+08 link read bytes and 4.395e+04 SMMU translation requests; copy home 8.607e+09 link read bytes and 1.311e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.368e+07 SMMU translation requests; copy level 8.607e+09 link read bytes and 1.311e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=1024,kernel=k6,placement=cpu,type=four,update=atomic,vary=update

- seed 73; every round ran in the drawn order: yes; floor 0.2722 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x56a400000000, copy home 0x56a500000000, direct level 0x56a5c0000000, copy level 0x56a680000000
- factor effect within the cell: on the direct route -0.0842 [-0.0911, -0.0790] ms, on the copy route -0.1438 [-0.1541, -0.1402] ms; change relative to the copy call at home: +0.8 %
- per repetition: direct home 0 link read bytes and 4180 SMMU translation requests; copy home 1.074e+09 link read bytes and 3.278e+04 SMMU translation requests; direct level 1.074e+09 link read bytes and 4534 SMMU translation requests; copy level 1.074e+09 link read bytes and 3.278e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,type=four,vary=generator

- seed 73; every round ran in the drawn order: yes; floor 0.5037 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x50eac0000000, copy home 0x50ebc0000000, direct level 0x50ec80000000, copy level 0x50ed40000000
- factor effect within the cell: on the direct route 158.2533 [157.6997, 158.8261] ms, on the copy route 63.5860 [63.0239, 64.0888] ms; change relative to the copy call at home: +2258.4 %
- per repetition: direct home 3.197e+09 link read bytes and 0 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.689e+04 SMMU translation requests; direct level 2.853e+09 link read bytes and 0 SMMU translation requests; copy level 1.074e+09 link read bytes and 1.688e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,type=four,vary=generator

- seed 73; every round ran in the drawn order: yes; floor 0.5037 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5aedc0000000, copy home 0x5aeec0000000, direct level 0x5aef80000000, copy level 0x5af040000000
- factor effect within the cell: on the direct route 64.5926 [64.5331, 64.6240] ms, on the copy route 64.1723 [64.0980, 64.2047] ms; change relative to the copy call at home: +24.3 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 0 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x517640000000, copy home 0x517700000000, direct level 0x517780000000, copy level 0x517800000000
- factor effect within the cell: on the direct route 0.0007 [0.0007, 0.0009] ms, on the copy route 0.0019 [0.0015, 0.0022] ms; change relative to the copy call at home: -3.6 %
- per repetition: direct home 5.243e+05 link read bytes and 0.78 SMMU translation requests; copy home 5.243e+05 link read bytes and 0.68 SMMU translation requests; direct level 5.243e+05 link read bytes and 0.78 SMMU translation requests; copy level 5.243e+05 link read bytes and 0.68 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4b5940000000, copy home 0x4b5a00000000, direct level 0x4b5a80000000, copy level 0x4b5b00000000
- factor effect within the cell: on the direct route 0.0007 [0.0006, 0.0009] ms, on the copy route 0.0014 [0.0005, 0.0017] ms; change relative to the copy call at home: -1.8 %
- per repetition: direct home 5.243e+05 link read bytes and 0.78 SMMU translation requests; copy home 5.243e+05 link read bytes and 0.66 SMMU translation requests; direct level 5.243e+05 link read bytes and 0.78 SMMU translation requests; copy level 5.243e+05 link read bytes and 0.67 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5ddcc0000000, copy home 0x5ddd40000000, direct level 0x5dddc0000000, copy level 0x5dde40000000
- factor effect within the cell: on the direct route 0.0000 [-0.0001, 0.0001] ms, on the copy route -0.0001 [-0.0005, 0.0002] ms; change relative to the copy call at home: +0.2 %
- per repetition: direct home 5.243e+05 link read bytes and 0.78 SMMU translation requests; copy home 5.243e+05 link read bytes and 0.66 SMMU translation requests; direct level 5.243e+05 link read bytes and 0.78 SMMU translation requests; copy level 5.243e+05 link read bytes and 0.68 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4dcd00000000, copy home 0x4dcdc0000000, direct level 0x4dce40000000, copy level 0x4dcec0000000
- factor effect within the cell: on the direct route -0.0000 [-0.0001, 0.0001] ms, on the copy route 0.0005 [0.0002, 0.0009] ms; change relative to the copy call at home: -1.5 %
- per repetition: direct home 0 link read bytes and 39 SMMU translation requests; copy home 0 link read bytes and 39 SMMU translation requests; direct level 0 link read bytes and 39 SMMU translation requests; copy level 0 link read bytes and 39 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x40f500000000, copy home 0x40f580000000, direct level 0x40f600000000, copy level 0x40f680000000
- factor effect within the cell: on the direct route 0.0000 [-0.0000, 0.0001] ms, on the copy route 0.0002 [-0.0001, 0.0009] ms; change relative to the copy call at home: -0.4 %
- per repetition: direct home 0 link read bytes and 39 SMMU translation requests; copy home 0 link read bytes and 39 SMMU translation requests; direct level 0 link read bytes and 39 SMMU translation requests; copy level 0 link read bytes and 39 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5de6c0000000, copy home 0x5de740000000, direct level 0x5de7c0000000, copy level 0x5de840000000
- factor effect within the cell: on the direct route 0.0001 [-0.0000, 0.0002] ms, on the copy route 0.0003 [0.0000, 0.0004] ms; change relative to the copy call at home: -0.6 %
- per repetition: direct home 0 link read bytes and 39 SMMU translation requests; copy home 0 link read bytes and 39 SMMU translation requests; direct level 0 link read bytes and 39 SMMU translation requests; copy level 0 link read bytes and 39 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5c8f80000000, copy home 0x5c9080000000, direct level 0x5c9140000000, copy level 0x5c9200000000
- factor effect within the cell: on the direct route -0.0119 [-0.0122, -0.0111] ms, on the copy route -0.1105 [-0.1133, -0.1088] ms; change relative to the copy call at home: +3.0 %
- per repetition: direct home 1.074e+09 link read bytes and 418.4 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.64e+04 SMMU translation requests; direct level 1.074e+09 link read bytes and 422 SMMU translation requests; copy level 1.074e+09 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x59d780000000, copy home 0x59d880000000, direct level 0x59d940000000, copy level 0x59da00000000
- factor effect within the cell: on the direct route 0.1376 [0.1144, 0.1713] ms, on the copy route -0.0133 [-0.0174, 0.0008] ms; change relative to the copy call at home: +4.5 %
- per repetition: direct home 1.074e+09 link read bytes and 819 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.64e+04 SMMU translation requests; direct level 1.074e+09 link read bytes and 416.1 SMMU translation requests; copy level 1.074e+09 link read bytes and 1.649e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x46c780000000, copy home 0x46c840000000, direct level 0x46c900000000, copy level 0x46c9c0000000
- factor effect within the cell: on the direct route -0.0104 [-0.0110, -0.0097] ms, on the copy route -0.1067 [-0.1074, -0.1056] ms; change relative to the copy call at home: +2.9 %
- per repetition: direct home 1.074e+09 link read bytes and 408.9 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.64e+04 SMMU translation requests; direct level 1.074e+09 link read bytes and 411.5 SMMU translation requests; copy level 1.074e+09 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5e5f00000000, copy home 0x5e6000000000, direct level 0x5e60c0000000, copy level 0x5e6180000000
- factor effect within the cell: on the direct route 0.0029 [0.0016, 0.0050] ms, on the copy route 0.0005 [-0.0015, 0.0010] ms; change relative to the copy call at home: +0.3 %
- per repetition: direct home 0 link read bytes and 5.03e+04 SMMU translation requests; copy home 0 link read bytes and 4.48e+04 SMMU translation requests; direct level 0 link read bytes and 4.986e+04 SMMU translation requests; copy level 0 link read bytes and 4.509e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5e5b80000000, copy home 0x5e5c80000000, direct level 0x5e5d40000000, copy level 0x5e5e00000000
- factor effect within the cell: on the direct route 0.0200 [0.0180, 0.0219] ms, on the copy route -0.0001 [-0.0025, 0.0012] ms; change relative to the copy call at home: +1.9 %
- per repetition: direct home 0 link read bytes and 4.989e+04 SMMU translation requests; copy home 0 link read bytes and 4.901e+04 SMMU translation requests; direct level 0 link read bytes and 5.27e+04 SMMU translation requests; copy level 0 link read bytes and 4.736e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4eab00000000, copy home 0x4eac00000000, direct level 0x4eacc0000000, copy level 0x4ead80000000
- factor effect within the cell: on the direct route 0.0027 [0.0016, 0.0050] ms, on the copy route 0.0005 [-0.0007, 0.0014] ms; change relative to the copy call at home: +0.2 %
- per repetition: direct home 0 link read bytes and 5.085e+04 SMMU translation requests; copy home 0 link read bytes and 4.5e+04 SMMU translation requests; direct level 0 link read bytes and 5.048e+04 SMMU translation requests; copy level 0 link read bytes and 4.509e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x52fb40000000, copy home 0x52fc00000000, direct level 0x52fc80000000, copy level 0x52fd00000000
- factor effect within the cell: on the direct route -0.0037 [-0.0044, -0.0036] ms, on the copy route -0.0077 [-0.0091, -0.0059] ms; change relative to the copy call at home: +0.8 %
- per repetition: direct home 1.342e+08 link read bytes and 0 SMMU translation requests; copy home 1.342e+08 link read bytes and 2060 SMMU translation requests; direct level 1.342e+08 link read bytes and 80.41 SMMU translation requests; copy level 1.342e+08 link read bytes and 2060 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4a7080000000, copy home 0x4a7100000000, direct level 0x4a7180000000, copy level 0x4a7200000000
- factor effect within the cell: on the direct route 0.2909 [0.2898, 0.2952] ms, on the copy route 0.2496 [0.2471, 0.2511] ms; change relative to the copy call at home: +9.2 %
- per repetition: direct home 1.342e+08 link read bytes and 0 SMMU translation requests; copy home 1.342e+08 link read bytes and 2060 SMMU translation requests; direct level 1.342e+08 link read bytes and 0 SMMU translation requests; copy level 1.342e+08 link read bytes and 2060 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x524680000000, copy home 0x524780000000, direct level 0x524800000000, copy level 0x524880000000
- factor effect within the cell: on the direct route -0.0027 [-0.0031, -0.0026] ms, on the copy route -0.0010 [-0.0014, -0.0003] ms; change relative to the copy call at home: -0.4 %
- per repetition: direct home 1.342e+08 link read bytes and 0 SMMU translation requests; copy home 1.342e+08 link read bytes and 2060 SMMU translation requests; direct level 1.342e+08 link read bytes and 0 SMMU translation requests; copy level 1.342e+08 link read bytes and 2060 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x47df40000000, copy home 0x47e040000000, direct level 0x47e0c0000000, copy level 0x47e140000000
- factor effect within the cell: on the direct route 0.1334 [0.1322, 0.1365] ms, on the copy route 0.0943 [0.0923, 0.0961] ms; change relative to the copy call at home: +21.1 %
- per repetition: direct home 0 link read bytes and 6542 SMMU translation requests; copy home 0 link read bytes and 6497 SMMU translation requests; direct level 0 link read bytes and 3790 SMMU translation requests; copy level 0 link read bytes and 3581 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x58ab40000000, copy home 0x58ac00000000, direct level 0x58ac80000000, copy level 0x58ad00000000
- factor effect within the cell: on the direct route 0.2223 [0.2220, 0.2226] ms, on the copy route 0.1563 [0.1542, 0.1578] ms; change relative to the copy call at home: +31.6 %
- per repetition: direct home 0 link read bytes and 7320 SMMU translation requests; copy home 0 link read bytes and 6743 SMMU translation requests; direct level 0 link read bytes and 3573 SMMU translation requests; copy level 0 link read bytes and 3391 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5cac40000000, copy home 0x5cacc0000000, direct level 0x5cad40000000, copy level 0x5cae00000000
- factor effect within the cell: on the direct route -0.0001 [-0.0008, -0.0000] ms, on the copy route 0.0013 [-0.0002, 0.0026] ms; change relative to the copy call at home: -1.0 %
- per repetition: direct home 0 link read bytes and 6275 SMMU translation requests; copy home 0 link read bytes and 7438 SMMU translation requests; direct level 0 link read bytes and 5910 SMMU translation requests; copy level 0 link read bytes and 7621 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x43efc0000000, copy home 0x43f040000000, direct level 0x43f0c0000000, copy level 0x43f140000000
- factor effect within the cell: on the direct route -0.0002 [-0.0004, 0.0001] ms, on the copy route -0.0010 [-0.0011, -0.0002] ms; change relative to the copy call at home: +1.6 %
- per repetition: direct home 2.097e+06 link read bytes and 1.62 SMMU translation requests; copy home 2.097e+06 link read bytes and 1 SMMU translation requests; direct level 2.097e+06 link read bytes and 2.18 SMMU translation requests; copy level 2.097e+06 link read bytes and 1 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5d1ec0000000, copy home 0x5d1f80000000, direct level 0x5d2000000000, copy level 0x5d2080000000
- factor effect within the cell: on the direct route 0.0023 [0.0022, 0.0024] ms, on the copy route 0.0044 [0.0042, 0.0049] ms; change relative to the copy call at home: -5.1 %
- per repetition: direct home 2.097e+06 link read bytes and 1.82 SMMU translation requests; copy home 2.097e+06 link read bytes and 1 SMMU translation requests; direct level 2.097e+06 link read bytes and 1.6 SMMU translation requests; copy level 2.097e+06 link read bytes and 1.32 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x47c140000000, copy home 0x47c200000000, direct level 0x47c280000000, copy level 0x47c300000000
- factor effect within the cell: on the direct route 0.0001 [0.0000, 0.0001] ms, on the copy route -0.0004 [-0.0007, 0.0000] ms; change relative to the copy call at home: +1.0 %
- per repetition: direct home 2.097e+06 link read bytes and 0.74 SMMU translation requests; copy home 2.097e+06 link read bytes and 1 SMMU translation requests; direct level 2.097e+06 link read bytes and 1.48 SMMU translation requests; copy level 2.097e+06 link read bytes and 1 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x477500000000, copy home 0x4775c0000000, direct level 0x477640000000, copy level 0x4776c0000000
- factor effect within the cell: on the direct route 0.0008 [0.0007, 0.0008] ms, on the copy route 0.0004 [0.0001, 0.0008] ms; change relative to the copy call at home: +1.4 %
- per repetition: direct home 0 link read bytes and 95.83 SMMU translation requests; copy home 0 link read bytes and 101.8 SMMU translation requests; direct level 0 link read bytes and 91.71 SMMU translation requests; copy level 0 link read bytes and 99.75 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4d6800000000, copy home 0x4d68c0000000, direct level 0x4d6940000000, copy level 0x4d69c0000000
- factor effect within the cell: on the direct route 0.0014 [0.0013, 0.0014] ms, on the copy route 0.0007 [0.0005, 0.0011] ms; change relative to the copy call at home: +2.0 %
- per repetition: direct home 0 link read bytes and 95.82 SMMU translation requests; copy home 0 link read bytes and 97.62 SMMU translation requests; direct level 0 link read bytes and 91.04 SMMU translation requests; copy level 0 link read bytes and 93.59 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x45dec0000000, copy home 0x45df80000000, direct level 0x45e000000000, copy level 0x45e080000000
- factor effect within the cell: on the direct route -0.0000 [-0.0002, 0.0001] ms, on the copy route 0.0001 [-0.0004, 0.0004] ms; change relative to the copy call at home: -0.6 %
- per repetition: direct home 0 link read bytes and 94.73 SMMU translation requests; copy home 0 link read bytes and 100.8 SMMU translation requests; direct level 0 link read bytes and 88.4 SMMU translation requests; copy level 0 link read bytes and 84.27 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5f1b80000000, copy home 0x5f1c40000000, direct level 0x5f1d00000000, copy level 0x5f1d80000000
- factor effect within the cell: on the direct route -0.0065 [-0.0074, -0.0059] ms, on the copy route -0.0212 [-0.0228, -0.0195] ms; change relative to the copy call at home: +1.6 %
- per repetition: direct home 2.684e+08 link read bytes and 0 SMMU translation requests; copy home 2.684e+08 link read bytes and 4110 SMMU translation requests; direct level 2.684e+08 link read bytes and 66.78 SMMU translation requests; copy level 2.684e+08 link read bytes and 4110 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x4f1440000000, copy home 0x4f14c0000000, direct level 0x4f1580000000, copy level 0x4f1600000000
- factor effect within the cell: on the direct route 0.1100 [0.1067, 0.1168] ms, on the copy route 0.0607 [0.0568, 0.0948] ms; change relative to the copy call at home: +5.2 %
- per repetition: direct home 2.684e+08 link read bytes and 0 SMMU translation requests; copy home 2.684e+08 link read bytes and 4110 SMMU translation requests; direct level 2.684e+08 link read bytes and 0 SMMU translation requests; copy level 2.684e+08 link read bytes and 4112 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x496280000000, copy home 0x496340000000, direct level 0x4963c0000000, copy level 0x496440000000
- factor effect within the cell: on the direct route 0.0007 [0.0003, 0.0010] ms, on the copy route -0.0028 [-0.0034, -0.0020] ms; change relative to the copy call at home: +0.4 %
- per repetition: direct home 2.684e+08 link read bytes and 0 SMMU translation requests; copy home 2.684e+08 link read bytes and 4110 SMMU translation requests; direct level 2.684e+08 link read bytes and 0 SMMU translation requests; copy level 2.684e+08 link read bytes and 4110 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x577400000000, copy home 0x5774c0000000, direct level 0x577540000000, copy level 0x5775c0000000
- factor effect within the cell: on the direct route 0.0663 [0.0651, 0.0667] ms, on the copy route -0.0331 [-0.0440, -0.0226] ms; change relative to the copy call at home: +12.0 %
- per repetition: direct home 0 link read bytes and 1.298e+04 SMMU translation requests; copy home 0 link read bytes and 4115 SMMU translation requests; direct level 0 link read bytes and 8692 SMMU translation requests; copy level 0 link read bytes and 4115 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4975c0000000, copy home 0x497680000000, direct level 0x497700000000, copy level 0x4977c0000000
- factor effect within the cell: on the direct route 0.0780 [0.0771, 0.0786] ms, on the copy route -0.0246 [-0.0259, -0.0239] ms; change relative to the copy call at home: +12.9 %
- per repetition: direct home 0 link read bytes and 1.397e+04 SMMU translation requests; copy home 0 link read bytes and 4115 SMMU translation requests; direct level 0 link read bytes and 1.16e+04 SMMU translation requests; copy level 0 link read bytes and 4115 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5cefc0000000, copy home 0x5cf080000000, direct level 0x5cf140000000, copy level 0x5cf1c0000000
- factor effect within the cell: on the direct route 0.0021 [0.0014, 0.0023] ms, on the copy route -0.0004 [-0.0022, 0.0004] ms; change relative to the copy call at home: +0.3 %
- per repetition: direct home 0 link read bytes and 1.225e+04 SMMU translation requests; copy home 0 link read bytes and 4117 SMMU translation requests; direct level 0 link read bytes and 1.195e+04 SMMU translation requests; copy level 0 link read bytes and 4115 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x476e80000000, copy home 0x476f40000000, direct level 0x476fc0000000, copy level 0x477040000000
- factor effect within the cell: on the direct route 0.0009 [0.0007, 0.0011] ms, on the copy route 0.0003 [-0.0005, 0.0005] ms; change relative to the copy call at home: +0.5 %
- per repetition: direct home 3.355e+07 link read bytes and 50.09 SMMU translation requests; copy home 3.355e+07 link read bytes and 523.7 SMMU translation requests; direct level 3.355e+07 link read bytes and 11.84 SMMU translation requests; copy level 3.355e+07 link read bytes and 523.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x590340000000, copy home 0x590400000000, direct level 0x590480000000, copy level 0x590500000000
- factor effect within the cell: on the direct route 0.0948 [0.0938, 0.0954] ms, on the copy route 0.0841 [0.0833, 0.0847] ms; change relative to the copy call at home: +7.8 %
- per repetition: direct home 3.355e+07 link read bytes and 52.19 SMMU translation requests; copy home 3.355e+07 link read bytes and 523.8 SMMU translation requests; direct level 3.355e+07 link read bytes and 19.38 SMMU translation requests; copy level 3.355e+07 link read bytes and 524 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4e8d80000000, copy home 0x4e8e40000000, direct level 0x4e8ec0000000, copy level 0x4e8f40000000
- factor effect within the cell: on the direct route -0.0000 [-0.0002, 0.0001] ms, on the copy route -0.0002 [-0.0007, 0.0009] ms; change relative to the copy call at home: +0.2 %
- per repetition: direct home 3.355e+07 link read bytes and 51.28 SMMU translation requests; copy home 3.355e+07 link read bytes and 523.8 SMMU translation requests; direct level 3.355e+07 link read bytes and 50.58 SMMU translation requests; copy level 3.355e+07 link read bytes and 523.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x594e00000000, copy home 0x594e80000000, direct level 0x594f00000000, copy level 0x594f80000000
- factor effect within the cell: on the direct route 0.0337 [0.0332, 0.0341] ms, on the copy route 0.0334 [0.0331, 0.0336] ms; change relative to the copy call at home: +0.5 %
- per repetition: direct home 0 link read bytes and 1439 SMMU translation requests; copy home 0 link read bytes and 1961 SMMU translation requests; direct level 0 link read bytes and 1510 SMMU translation requests; copy level 0 link read bytes and 1246 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4ef880000000, copy home 0x4ef900000000, direct level 0x4ef980000000, copy level 0x4efa00000000
- factor effect within the cell: on the direct route 0.0704 [0.0699, 0.0705] ms, on the copy route 0.0711 [0.0704, 0.0715] ms; change relative to the copy call at home: -1.5 %
- per repetition: direct home 0 link read bytes and 1587 SMMU translation requests; copy home 0 link read bytes and 1869 SMMU translation requests; direct level 0 link read bytes and 1429 SMMU translation requests; copy level 0 link read bytes and 991.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x514b00000000, copy home 0x514b80000000, direct level 0x514c00000000, copy level 0x514c80000000
- factor effect within the cell: on the direct route -0.0009 [-0.0010, -0.0007] ms, on the copy route -0.0008 [-0.0012, -0.0006] ms; change relative to the copy call at home: +0.0 %
- per repetition: direct home 0 link read bytes and 1401 SMMU translation requests; copy home 0 link read bytes and 2025 SMMU translation requests; direct level 0 link read bytes and 1478 SMMU translation requests; copy level 0 link read bytes and 1773 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4ca580000000, copy home 0x4ca640000000, direct level 0x4ca6c0000000, copy level 0x4ca740000000
- factor effect within the cell: on the direct route -0.0007 [-0.0012, -0.0004] ms, on the copy route -0.0004 [-0.0006, 0.0012] ms; change relative to the copy call at home: -0.2 %
- per repetition: direct home 6.711e+07 link read bytes and 20.99 SMMU translation requests; copy home 6.711e+07 link read bytes and 1035 SMMU translation requests; direct level 6.711e+07 link read bytes and 21.47 SMMU translation requests; copy level 6.711e+07 link read bytes and 1035 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5cdc80000000, copy home 0x5cdd00000000, direct level 0x5cdd80000000, copy level 0x5cde00000000
- factor effect within the cell: on the direct route 0.1846 [0.1789, 0.1855] ms, on the copy route 0.1647 [0.1642, 0.1664] ms; change relative to the copy call at home: +8.1 %
- per repetition: direct home 6.711e+07 link read bytes and 47.28 SMMU translation requests; copy home 6.711e+07 link read bytes and 1036 SMMU translation requests; direct level 6.711e+07 link read bytes and 36.44 SMMU translation requests; copy level 6.711e+07 link read bytes and 1036 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x44d2c0000000, copy home 0x44d380000000, direct level 0x44d400000000, copy level 0x44d480000000
- factor effect within the cell: on the direct route -0.0007 [-0.0009, -0.0005] ms, on the copy route -0.0007 [-0.0010, -0.0001] ms; change relative to the copy call at home: -0.0 %
- per repetition: direct home 6.711e+07 link read bytes and 44.4 SMMU translation requests; copy home 6.711e+07 link read bytes and 1036 SMMU translation requests; direct level 6.711e+07 link read bytes and 45.23 SMMU translation requests; copy level 6.711e+07 link read bytes and 1036 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x526400000000, copy home 0x5264c0000000, direct level 0x526540000000, copy level 0x5265c0000000
- factor effect within the cell: on the direct route 0.0832 [0.0823, 0.0836] ms, on the copy route 0.0722 [0.0708, 0.0730] ms; change relative to the copy call at home: +11.4 %
- per repetition: direct home 0 link read bytes and 2872 SMMU translation requests; copy home 0 link read bytes and 3908 SMMU translation requests; direct level 0 link read bytes and 2387 SMMU translation requests; copy level 0 link read bytes and 1827 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x486dc0000000, copy home 0x486e80000000, direct level 0x486f00000000, copy level 0x486f80000000
- factor effect within the cell: on the direct route 0.1413 [0.1402, 0.1430] ms, on the copy route 0.1313 [0.1300, 0.1321] ms; change relative to the copy call at home: +11.3 %
- per repetition: direct home 0 link read bytes and 2976 SMMU translation requests; copy home 0 link read bytes and 3905 SMMU translation requests; direct level 0 link read bytes and 2170 SMMU translation requests; copy level 0 link read bytes and 1671 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x421240000000, copy home 0x4212c0000000, direct level 0x421340000000, copy level 0x4213c0000000
- factor effect within the cell: on the direct route -0.0013 [-0.0016, -0.0011] ms, on the copy route -0.0000 [-0.0006, 0.0008] ms; change relative to the copy call at home: -1.2 %
- per repetition: direct home 0 link read bytes and 2921 SMMU translation requests; copy home 0 link read bytes and 3915 SMMU translation requests; direct level 0 link read bytes and 2894 SMMU translation requests; copy level 0 link read bytes and 3878 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x50fd40000000, copy home 0x50fe00000000, direct level 0x50fe80000000, copy level 0x50ff00000000
- factor effect within the cell: on the direct route 0.0000 [-0.0001, 0.0001] ms, on the copy route 0.0001 [-0.0002, 0.0005] ms; change relative to the copy call at home: -0.3 %
- per repetition: direct home 8.389e+06 link read bytes and 6.71 SMMU translation requests; copy home 8.389e+06 link read bytes and 2.94 SMMU translation requests; direct level 8.389e+06 link read bytes and 7.42 SMMU translation requests; copy level 8.389e+06 link read bytes and 2.94 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x56d980000000, copy home 0x56da40000000, direct level 0x56dac0000000, copy level 0x56db40000000
- factor effect within the cell: on the direct route 0.0204 [0.0202, 0.0205] ms, on the copy route 0.0183 [0.0181, 0.0190] ms; change relative to the copy call at home: +3.4 %
- per repetition: direct home 8.389e+06 link read bytes and 7.28 SMMU translation requests; copy home 8.389e+06 link read bytes and 2.94 SMMU translation requests; direct level 8.389e+06 link read bytes and 5.09 SMMU translation requests; copy level 8.389e+06 link read bytes and 3.28 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x44e200000000, copy home 0x44e2c0000000, direct level 0x44e340000000, copy level 0x44e3c0000000
- factor effect within the cell: on the direct route -0.0001 [-0.0002, 0.0001] ms, on the copy route -0.0003 [-0.0009, -0.0000] ms; change relative to the copy call at home: +0.5 %
- per repetition: direct home 8.389e+06 link read bytes and 0 SMMU translation requests; copy home 8.389e+06 link read bytes and 2.94 SMMU translation requests; direct level 8.389e+06 link read bytes and 7.69 SMMU translation requests; copy level 8.389e+06 link read bytes and 2.94 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4f9100000000, copy home 0x4f91c0000000, direct level 0x4f9240000000, copy level 0x4f92c0000000
- factor effect within the cell: on the direct route 0.0083 [0.0082, 0.0083] ms, on the copy route 0.0142 [0.0140, 0.0146] ms; change relative to the copy call at home: -18.5 %
- per repetition: direct home 0 link read bytes and 416.2 SMMU translation requests; copy home 0 link read bytes and 435.7 SMMU translation requests; direct level 0 link read bytes and 385.1 SMMU translation requests; copy level 0 link read bytes and 370.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4b17c0000000, copy home 0x4b1840000000, direct level 0x4b18c0000000, copy level 0x4b1940000000
- factor effect within the cell: on the direct route 0.0142 [0.0141, 0.0142] ms, on the copy route 0.0186 [0.0182, 0.0189] ms; change relative to the copy call at home: -14.1 %
- per repetition: direct home 0 link read bytes and 413.6 SMMU translation requests; copy home 0 link read bytes and 422 SMMU translation requests; direct level 0 link read bytes and 424.8 SMMU translation requests; copy level 0 link read bytes and 401.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5e4040000000, copy home 0x5e4100000000, direct level 0x5e4180000000, copy level 0x5e4200000000
- factor effect within the cell: on the direct route 0.0003 [0.0002, 0.0003] ms, on the copy route 0.0002 [-0.0003, 0.0004] ms; change relative to the copy call at home: +0.4 %
- per repetition: direct home 0 link read bytes and 414.5 SMMU translation requests; copy home 0 link read bytes and 431 SMMU translation requests; direct level 0 link read bytes and 360.7 SMMU translation requests; copy level 0 link read bytes and 387.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x432ec0000000, copy home 0x432f80000000, direct level 0x433000000000, copy level 0x433080000000
- factor effect within the cell: on the direct route -0.0057 [-0.0063, -0.0052] ms, on the copy route -0.0075 [-0.0089, -0.0066] ms; change relative to the copy call at home: +0.5 %
- per repetition: direct home 1.007e+08 link read bytes and 0 SMMU translation requests; copy home 1.007e+08 link read bytes and 1564 SMMU translation requests; direct level 1.007e+08 link read bytes and 66.29 SMMU translation requests; copy level 1.007e+08 link read bytes and 1564 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x541940000000, copy home 0x541a00000000, direct level 0x541a80000000, copy level 0x541b00000000
- factor effect within the cell: on the direct route 0.2617 [0.2552, 0.2677] ms, on the copy route 0.2324 [0.2244, 0.2364] ms; change relative to the copy call at home: +9.0 %
- per repetition: direct home 1.007e+08 link read bytes and 63.83 SMMU translation requests; copy home 1.007e+08 link read bytes and 1550 SMMU translation requests; direct level 1.007e+08 link read bytes and 48.24 SMMU translation requests; copy level 1.007e+08 link read bytes and 1550 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4ee680000000, copy home 0x4ee740000000, direct level 0x4ee7c0000000, copy level 0x4ee840000000
- factor effect within the cell: on the direct route 0.0029 [0.0027, 0.0030] ms, on the copy route -0.0015 [-0.0021, -0.0006] ms; change relative to the copy call at home: +1.2 %
- per repetition: direct home 1.007e+08 link read bytes and 68.65 SMMU translation requests; copy home 1.007e+08 link read bytes and 1564 SMMU translation requests; direct level 1.007e+08 link read bytes and 65.21 SMMU translation requests; copy level 1.007e+08 link read bytes and 1564 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x537340000000, copy home 0x537400000000, direct level 0x537480000000, copy level 0x537500000000
- factor effect within the cell: on the direct route 0.1334 [0.1319, 0.1349] ms, on the copy route 0.1034 [0.1027, 0.1042] ms; change relative to the copy call at home: +21.1 %
- per repetition: direct home 0 link read bytes and 4533 SMMU translation requests; copy home 0 link read bytes and 5423 SMMU translation requests; direct level 0 link read bytes and 2976 SMMU translation requests; copy level 0 link read bytes and 2769 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x516100000000, copy home 0x516180000000, direct level 0x516200000000, copy level 0x5162c0000000
- factor effect within the cell: on the direct route 0.2073 [0.2070, 0.2078] ms, on the copy route 0.1681 [0.1660, 0.1691] ms; change relative to the copy call at home: +28.3 %
- per repetition: direct home 0 link read bytes and 4569 SMMU translation requests; copy home 0 link read bytes and 5914 SMMU translation requests; direct level 0 link read bytes and 2700 SMMU translation requests; copy level 0 link read bytes and 2662 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4fc380000000, copy home 0x4fc440000000, direct level 0x4fc4c0000000, copy level 0x4fc540000000
- factor effect within the cell: on the direct route -0.0002 [-0.0005, 0.0001] ms, on the copy route 0.0012 [-0.0003, 0.0028] ms; change relative to the copy call at home: -1.1 %
- per repetition: direct home 0 link read bytes and 4497 SMMU translation requests; copy home 0 link read bytes and 5676 SMMU translation requests; direct level 0 link read bytes and 4320 SMMU translation requests; copy level 0 link read bytes and 5649 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x4ac300000000, copy home 0x4ac3c0000000, direct level 0x4ac480000000, copy level 0x4ac540000000
- factor effect within the cell: on the direct route -0.3587 [-0.3655, -0.3510] ms, on the copy route -0.5981 [-0.6226, -0.0860] ms; change relative to the copy call at home: +4.8 %
- per repetition: direct home 3.194e+09 link read bytes and 0 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.689e+04 SMMU translation requests; direct level 3.193e+09 link read bytes and 0 SMMU translation requests; copy level 1.074e+09 link read bytes and 1.689e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x547c80000000, copy home 0x547d80000000, direct level 0x547e40000000, copy level 0x547f00000000
- factor effect within the cell: on the direct route -0.0041 [-0.0057, 0.0035] ms, on the copy route -0.0048 [-0.0060, -0.0012] ms; change relative to the copy call at home: +0.1 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 0 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=1,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x530340000000, copy home 0x530400000000, direct level 0x5304c0000000, copy level 0x530580000000
- factor effect within the cell: on the direct route -0.0010 [-0.0013, -0.0005] ms, on the copy route -0.0013 [-0.0021, -0.0004] ms; change relative to the copy call at home: +1.2 %
- per repetition: direct home 8.38e+06 link read bytes and 319.9 SMMU translation requests; copy home 8.38e+06 link read bytes and 131.1 SMMU translation requests; direct level 8.38e+06 link read bytes and 319.5 SMMU translation requests; copy level 8.38e+06 link read bytes and 131 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=1,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5a98c0000000, copy home 0x5a9980000000, direct level 0x5a9a40000000, copy level 0x5a9b00000000
- factor effect within the cell: on the direct route 0.0189 [0.0185, 0.0192] ms, on the copy route 0.0200 [0.0193, 0.0205] ms; change relative to the copy call at home: -1.7 %
- per repetition: direct home 8.38e+06 link read bytes and 327.6 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.38e+06 link read bytes and 314.7 SMMU translation requests; copy level 8.38e+06 link read bytes and 140.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=1,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4d2e40000000, copy home 0x4d2f00000000, direct level 0x4d2fc0000000, copy level 0x4d3080000000
- factor effect within the cell: on the direct route -0.0003 [-0.0005, -0.0002] ms, on the copy route -0.0001 [-0.0008, 0.0003] ms; change relative to the copy call at home: -0.6 %
- per repetition: direct home 8.38e+06 link read bytes and 302.4 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.38e+06 link read bytes and 302.7 SMMU translation requests; copy level 8.38e+06 link read bytes and 130.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x44e040000000, copy home 0x44e140000000, direct level 0x44e200000000, copy level 0x44e2c0000000
- factor effect within the cell: on the direct route -0.0008 [-0.0009, -0.0007] ms, on the copy route -0.0010 [-0.0015, -0.0008] ms; change relative to the copy call at home: +0.4 %
- per repetition: direct home 8.382e+06 link read bytes and 325.2 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 323.6 SMMU translation requests; copy level 8.38e+06 link read bytes and 130.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x49f680000000, copy home 0x49f780000000, direct level 0x49f840000000, copy level 0x49f900000000
- factor effect within the cell: on the direct route 0.0192 [0.0189, 0.0195] ms, on the copy route 0.0190 [0.0178, 0.0194] ms; change relative to the copy call at home: +0.9 %
- per repetition: direct home 8.382e+06 link read bytes and 326.2 SMMU translation requests; copy home 8.38e+06 link read bytes and 131.1 SMMU translation requests; direct level 8.382e+06 link read bytes and 312.4 SMMU translation requests; copy level 8.38e+06 link read bytes and 139.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x405400000000, copy home 0x4054c0000000, direct level 0x405580000000, copy level 0x405640000000
- factor effect within the cell: on the direct route -0.0002 [-0.0003, -0.0001] ms, on the copy route 0.0002 [-0.0006, 0.0005] ms; change relative to the copy call at home: -0.5 %
- per repetition: direct home 8.382e+06 link read bytes and 316.3 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 319.2 SMMU translation requests; copy level 8.38e+06 link read bytes and 130.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=2,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x42bc00000000, copy home 0x42bcc0000000, direct level 0x42bd80000000, copy level 0x42be40000000
- factor effect within the cell: on the direct route -0.0010 [-0.0013, -0.0009] ms, on the copy route -0.0011 [-0.0017, -0.0006] ms; change relative to the copy call at home: -0.5 %
- per repetition: direct home 8.382e+06 link read bytes and 316.1 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 313.8 SMMU translation requests; copy level 8.38e+06 link read bytes and 130.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=2,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x54df00000000, copy home 0x54dfc0000000, direct level 0x54e080000000, copy level 0x54e140000000
- factor effect within the cell: on the direct route 0.0172 [0.0169, 0.0174] ms, on the copy route 0.0179 [0.0173, 0.0185] ms; change relative to the copy call at home: -1.7 %
- per repetition: direct home 8.382e+06 link read bytes and 328.7 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 315.9 SMMU translation requests; copy level 8.38e+06 link read bytes and 142.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=2,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5f7f00000000, copy home 0x5f7fc0000000, direct level 0x5f8080000000, copy level 0x5f8140000000
- factor effect within the cell: on the direct route -0.0002 [-0.0003, -0.0001] ms, on the copy route -0.0003 [-0.0008, 0.0003] ms; change relative to the copy call at home: +0.4 %
- per repetition: direct home 8.382e+06 link read bytes and 318.7 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 317.1 SMMU translation requests; copy level 8.38e+06 link read bytes and 131 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=4,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5ac5c0000000, copy home 0x5ac6c0000000, direct level 0x5ac780000000, copy level 0x5ac840000000
- factor effect within the cell: on the direct route -0.0006 [-0.0008, -0.0002] ms, on the copy route -0.0011 [-0.0016, -0.0007] ms; change relative to the copy call at home: +0.8 %
- per repetition: direct home 8.382e+06 link read bytes and 314.6 SMMU translation requests; copy home 8.38e+06 link read bytes and 131 SMMU translation requests; direct level 8.382e+06 link read bytes and 317.4 SMMU translation requests; copy level 8.38e+06 link read bytes and 131 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=4,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4e0a00000000, copy home 0x4e0b80000000, direct level 0x4e0c40000000, copy level 0x4e0d00000000
- factor effect within the cell: on the direct route 0.0194 [0.0189, 0.0199] ms, on the copy route 0.0191 [0.0184, 0.0196] ms; change relative to the copy call at home: +0.8 %
- per repetition: direct home 8.382e+06 link read bytes and 329.9 SMMU translation requests; copy home 8.38e+06 link read bytes and 131.1 SMMU translation requests; direct level 8.382e+06 link read bytes and 312.5 SMMU translation requests; copy level 8.38e+06 link read bytes and 138.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=4,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x56c040000000, copy home 0x56c100000000, direct level 0x56c1c0000000, copy level 0x56c280000000
- factor effect within the cell: on the direct route -0.0001 [-0.0004, 0.0000] ms, on the copy route -0.0006 [-0.0011, 0.0002] ms; change relative to the copy call at home: +0.8 %
- per repetition: direct home 8.382e+06 link read bytes and 302.5 SMMU translation requests; copy home 8.38e+06 link read bytes and 131.2 SMMU translation requests; direct level 8.382e+06 link read bytes and 303.1 SMMU translation requests; copy level 8.38e+06 link read bytes and 130.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=64,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5b3380000000, copy home 0x5b34c0000000, direct level 0x5b3580000000, copy level 0x5b3640000000
- factor effect within the cell: on the direct route -0.0010 [-0.0013, -0.0008] ms, on the copy route -0.0013 [-0.0020, -0.0003] ms; change relative to the copy call at home: +0.3 %
- per repetition: direct home 8.382e+06 link read bytes and 296.9 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 297.6 SMMU translation requests; copy level 8.38e+06 link read bytes and 130.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=64,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x497600000000, copy home 0x497700000000, direct level 0x4977c0000000, copy level 0x497880000000
- factor effect within the cell: on the direct route 0.0180 [0.0179, 0.0180] ms, on the copy route 0.0165 [0.0159, 0.0170] ms; change relative to the copy call at home: +1.6 %
- per repetition: direct home 8.382e+06 link read bytes and 317 SMMU translation requests; copy home 8.38e+06 link read bytes and 131.3 SMMU translation requests; direct level 8.382e+06 link read bytes and 303.9 SMMU translation requests; copy level 8.38e+06 link read bytes and 143.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=64,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4e2e40000000, copy home 0x4e2f00000000, direct level 0x4e2fc0000000, copy level 0x4e3080000000
- factor effect within the cell: on the direct route -0.0002 [-0.0006, -0.0001] ms, on the copy route -0.0004 [-0.0011, 0.0003] ms; change relative to the copy call at home: +0.2 %
- per repetition: direct home 8.382e+06 link read bytes and 302.5 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 300.3 SMMU translation requests; copy level 8.38e+06 link read bytes and 130.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5e4f40000000, copy home 0x5e5000000000, direct level 0x5e50c0000000, copy level 0x5e5180000000
- factor effect within the cell: on the direct route -0.0004 [-0.0011, 0.0005] ms, on the copy route 0.5840 [0.5833, 0.5845] ms; change relative to the copy call at home: -1491.0 %
- per repetition: direct home 3.354e+07 link read bytes and 687.1 SMMU translation requests; copy home 0 link read bytes and 11.52 SMMU translation requests; direct level 3.354e+07 link read bytes and 550.5 SMMU translation requests; copy level 1.074e+08 link read bytes and 8624 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x412300000000, copy home 0x412400000000, direct level 0x4124c0000000, copy level 0x412580000000
- factor effect within the cell: on the direct route 0.0008 [0.0007, 0.0010] ms, on the copy route 0.5702 [0.5694, 0.5708] ms; change relative to the copy call at home: -1498.0 %
- per repetition: direct home 8.38e+06 link read bytes and 329.5 SMMU translation requests; copy home 0 link read bytes and 10.72 SMMU translation requests; direct level 8.38e+06 link read bytes and 327.7 SMMU translation requests; copy level 1.074e+08 link read bytes and 7210 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x45b3c0000000, copy home 0x45b4c0000000, direct level 0x45b580000000, copy level 0x45b640000000
- factor effect within the cell: on the direct route 0.0023 [0.0019, 0.0029] ms, on the copy route -0.0007 [-0.0014, 0.0006] ms; change relative to the copy call at home: +1.9 %
- per repetition: direct home 3.354e+07 link read bytes and 16.11 SMMU translation requests; copy home 3.354e+07 link read bytes and 533.2 SMMU translation requests; direct level 3.354e+07 link read bytes and 16.8 SMMU translation requests; copy level 3.354e+07 link read bytes and 533.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x424040000000, copy home 0x424140000000, direct level 0x424200000000, copy level 0x4242c0000000
- factor effect within the cell: on the direct route 0.0005 [0.0001, 0.0011] ms, on the copy route 0.0008 [0.0006, 0.0017] ms; change relative to the copy call at home: -0.1 %
- per repetition: direct home 8.38e+06 link read bytes and 316.3 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.38e+06 link read bytes and 318.9 SMMU translation requests; copy level 8.38e+06 link read bytes and 131.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x54bd00000000, copy home 0x54bdc0000000, direct level 0x54be80000000, copy level 0x54bf40000000
- factor effect within the cell: on the direct route 0.0006 [0.0004, 0.0009] ms, on the copy route 0.1522 [0.1503, 0.1533] ms; change relative to the copy call at home: -351.9 %
- per repetition: direct home 0 link read bytes and 946.5 SMMU translation requests; copy home 0 link read bytes and 16 SMMU translation requests; direct level 0 link read bytes and 949.6 SMMU translation requests; copy level 0 link read bytes and 3.374e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x42bdc0000000, copy home 0x42bf00000000, direct level 0x42bfc0000000, copy level 0x42c080000000
- factor effect within the cell: on the direct route 0.0040 [0.0033, 0.0045] ms, on the copy route -0.0011 [-0.0029, -0.0002] ms; change relative to the copy call at home: +3.4 %
- per repetition: direct home 0 link read bytes and 920.9 SMMU translation requests; copy home 0 link read bytes and 548.8 SMMU translation requests; direct level 0 link read bytes and 920.7 SMMU translation requests; copy level 0 link read bytes and 550.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x4dc1c0000000, copy home 0x4dc280000000, direct level 0x4dc340000000, copy level 0x4dc400000000
- factor effect within the cell: on the direct route 0.0024 [0.0020, 0.0033] ms, on the copy route 0.5810 [0.5804, 0.5825] ms; change relative to the copy call at home: -588.1 %
- per repetition: direct home 5.365e+08 link read bytes and 678.6 SMMU translation requests; copy home 0 link read bytes and 11.52 SMMU translation requests; direct level 5.365e+08 link read bytes and 521.8 SMMU translation requests; copy level 1.074e+08 link read bytes and 9282 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5d3e40000000, copy home 0x5d3f00000000, direct level 0x5d3fc0000000, copy level 0x5d4080000000
- factor effect within the cell: on the direct route 0.0003 [0.0001, 0.0007] ms, on the copy route 0.5751 [0.5746, 0.5755] ms; change relative to the copy call at home: -1342.0 %
- per repetition: direct home 8.382e+06 link read bytes and 328.6 SMMU translation requests; copy home 0 link read bytes and 10.56 SMMU translation requests; direct level 8.382e+06 link read bytes and 327.7 SMMU translation requests; copy level 1.074e+08 link read bytes and 7791 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x45ea00000000, copy home 0x45eb00000000, direct level 0x45ebc0000000, copy level 0x45ec80000000
- factor effect within the cell: on the direct route 0.0152 [0.0145, 0.0158] ms, on the copy route 0.6517 [0.6509, 0.6525] ms; change relative to the copy call at home: -652.8 %
- per repetition: direct home 5.365e+08 link read bytes and 664.3 SMMU translation requests; copy home 0 link read bytes and 12.16 SMMU translation requests; direct level 5.365e+08 link read bytes and 526.7 SMMU translation requests; copy level 1.074e+08 link read bytes and 5.062e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x51f5c0000000, copy home 0x51f6c0000000, direct level 0x51f780000000, copy level 0x51f840000000
- factor effect within the cell: on the direct route -0.0002 [-0.0009, 0.0003] ms, on the copy route 0.6486 [0.6483, 0.6492] ms; change relative to the copy call at home: -1508.5 %
- per repetition: direct home 8.382e+06 link read bytes and 327 SMMU translation requests; copy home 0 link read bytes and 10.72 SMMU translation requests; direct level 8.382e+06 link read bytes and 324.3 SMMU translation requests; copy level 1.074e+08 link read bytes and 5.1e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5db0c0000000, copy home 0x5db180000000, direct level 0x5db240000000, copy level 0x5db300000000
- factor effect within the cell: on the direct route 0.0221 [0.0213, 0.0230] ms, on the copy route 0.0030 [0.0010, 0.0042] ms; change relative to the copy call at home: +9.5 %
- per repetition: direct home 5.366e+08 link read bytes and 63.25 SMMU translation requests; copy home 3.354e+07 link read bytes and 533.2 SMMU translation requests; direct level 5.365e+08 link read bytes and 61.46 SMMU translation requests; copy level 3.354e+07 link read bytes and 533.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x555740000000, copy home 0x555840000000, direct level 0x555900000000, copy level 0x5559c0000000
- factor effect within the cell: on the direct route 0.0006 [0.0002, 0.0014] ms, on the copy route 0.0011 [0.0005, 0.0016] ms; change relative to the copy call at home: -0.3 %
- per repetition: direct home 8.382e+06 link read bytes and 323.2 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 322.6 SMMU translation requests; copy level 8.38e+06 link read bytes and 131.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5f9600000000, copy home 0x5f96c0000000, direct level 0x5f9780000000, copy level 0x5f9840000000
- factor effect within the cell: on the direct route -0.0005 [-0.0009, 0.0002] ms, on the copy route 0.1463 [0.1448, 0.1487] ms; change relative to the copy call at home: -133.9 %
- per repetition: direct home 0 link read bytes and 951.2 SMMU translation requests; copy home 0 link read bytes and 16 SMMU translation requests; direct level 0 link read bytes and 953 SMMU translation requests; copy level 0 link read bytes and 3.354e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x56bb80000000, copy home 0x56bc80000000, direct level 0x56bd40000000, copy level 0x56be00000000
- factor effect within the cell: on the direct route 0.0021 [0.0016, 0.0029] ms, on the copy route 0.6231 [0.6210, 0.6240] ms; change relative to the copy call at home: -570.9 %
- per repetition: direct home 0 link read bytes and 946.5 SMMU translation requests; copy home 0 link read bytes and 16 SMMU translation requests; direct level 0 link read bytes and 944.3 SMMU translation requests; copy level 0 link read bytes and 4.795e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5abcc0000000, copy home 0x5abdc0000000, direct level 0x5abe80000000, copy level 0x5abf40000000
- factor effect within the cell: on the direct route 0.0006 [0.0002, 0.0010] ms, on the copy route -0.0012 [-0.0021, -0.0004] ms; change relative to the copy call at home: +0.9 %
- per repetition: direct home 0 link read bytes and 951.4 SMMU translation requests; copy home 0 link read bytes and 550.1 SMMU translation requests; direct level 0 link read bytes and 951 SMMU translation requests; copy level 0 link read bytes and 552 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x545e80000000, copy home 0x545f80000000, direct level 0x546040000000, copy level 0x546100000000
- factor effect within the cell: on the direct route 0.0014 [0.0011, 0.0018] ms, on the copy route 0.5893 [0.5888, 0.5896] ms; change relative to the copy call at home: -1489.2 %
- per repetition: direct home 6.708e+07 link read bytes and 682.5 SMMU translation requests; copy home 0 link read bytes and 11.52 SMMU translation requests; direct level 6.708e+07 link read bytes and 538.4 SMMU translation requests; copy level 1.074e+08 link read bytes and 8436 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4a7cc0000000, copy home 0x4a7d80000000, direct level 0x4a7e40000000, copy level 0x4a7f00000000
- factor effect within the cell: on the direct route 0.0004 [0.0001, 0.0005] ms, on the copy route 0.5689 [0.5684, 0.5694] ms; change relative to the copy call at home: -1464.7 %
- per repetition: direct home 8.382e+06 link read bytes and 329.1 SMMU translation requests; copy home 0 link read bytes and 10.72 SMMU translation requests; direct level 8.382e+06 link read bytes and 328.6 SMMU translation requests; copy level 1.074e+08 link read bytes and 7200 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5cfd80000000, copy home 0x5cfe80000000, direct level 0x5cff40000000, copy level 0x5d0000000000
- factor effect within the cell: on the direct route 0.0013 [0.0010, 0.0024] ms, on the copy route -0.0000 [-0.0007, 0.0007] ms; change relative to the copy call at home: +1.1 %
- per repetition: direct home 6.708e+07 link read bytes and 8.29 SMMU translation requests; copy home 3.354e+07 link read bytes and 533.2 SMMU translation requests; direct level 6.708e+07 link read bytes and 0 SMMU translation requests; copy level 3.354e+07 link read bytes and 533 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x430180000000, copy home 0x430240000000, direct level 0x430300000000, copy level 0x4303c0000000
- factor effect within the cell: on the direct route 0.0004 [0.0000, 0.0010] ms, on the copy route 0.0003 [-0.0000, 0.0009] ms; change relative to the copy call at home: +0.2 %
- per repetition: direct home 8.382e+06 link read bytes and 317 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 317.9 SMMU translation requests; copy level 8.38e+06 link read bytes and 131.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x508380000000, copy home 0x508440000000, direct level 0x508500000000, copy level 0x5085c0000000
- factor effect within the cell: on the direct route -0.0002 [-0.0003, -0.0001] ms, on the copy route 0.1495 [0.1484, 0.1514] ms; change relative to the copy call at home: -270.2 %
- per repetition: direct home 0 link read bytes and 946 SMMU translation requests; copy home 0 link read bytes and 16 SMMU translation requests; direct level 0 link read bytes and 949.7 SMMU translation requests; copy level 0 link read bytes and 3.554e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x53ebc0000000, copy home 0x53ecc0000000, direct level 0x53ed80000000, copy level 0x53ee40000000
- factor effect within the cell: on the direct route 0.0024 [0.0020, 0.0027] ms, on the copy route -0.2155 [-0.2608, -0.1435] ms; change relative to the copy call at home: +23.6 %
- per repetition: direct home 0 link read bytes and 942.4 SMMU translation requests; copy home 0 link read bytes and 550.4 SMMU translation requests; direct level 0 link read bytes and 944.8 SMMU translation requests; copy level 0 link read bytes and 550.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5f5200000000, copy home 0x5f5300000000, direct level 0x5f53c0000000, copy level 0x5f5480000000
- factor effect within the cell: on the direct route -0.0012 [-0.0015, -0.0010] ms, on the copy route 0.5813 [0.5808, 0.5819] ms; change relative to the copy call at home: -1167.7 %
- per repetition: direct home 1.342e+08 link read bytes and 697.3 SMMU translation requests; copy home 0 link read bytes and 12.16 SMMU translation requests; direct level 1.342e+08 link read bytes and 542.2 SMMU translation requests; copy level 1.074e+08 link read bytes and 1.028e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x585040000000, copy home 0x585140000000, direct level 0x585200000000, copy level 0x5852c0000000
- factor effect within the cell: on the direct route 0.0009 [0.0005, 0.0014] ms, on the copy route 0.5685 [0.5677, 0.5694] ms; change relative to the copy call at home: -1445.4 %
- per repetition: direct home 8.382e+06 link read bytes and 328.8 SMMU translation requests; copy home 0 link read bytes and 10.4 SMMU translation requests; direct level 8.382e+06 link read bytes and 325.9 SMMU translation requests; copy level 1.074e+08 link read bytes and 7746 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x413dc0000000, copy home 0x413ec0000000, direct level 0x413f80000000, copy level 0x414040000000
- factor effect within the cell: on the direct route 0.0051 [0.0048, 0.0063] ms, on the copy route 0.0029 [0.0017, 0.0033] ms; change relative to the copy call at home: +1.8 %
- per repetition: direct home 1.342e+08 link read bytes and 9.01 SMMU translation requests; copy home 3.354e+07 link read bytes and 533.2 SMMU translation requests; direct level 1.342e+08 link read bytes and 16.46 SMMU translation requests; copy level 3.354e+07 link read bytes and 533 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5fba40000000, copy home 0x5fbb40000000, direct level 0x5fbc00000000, copy level 0x5fbcc0000000
- factor effect within the cell: on the direct route 0.0006 [0.0004, 0.0012] ms, on the copy route 0.0005 [-0.0001, 0.0013] ms; change relative to the copy call at home: +0.2 %
- per repetition: direct home 8.382e+06 link read bytes and 319.7 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 322 SMMU translation requests; copy level 8.38e+06 link read bytes and 131.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4f9200000000, copy home 0x4f9300000000, direct level 0x4f93c0000000, copy level 0x4f9480000000
- factor effect within the cell: on the direct route -0.0002 [-0.0005, 0.0000] ms, on the copy route 0.1466 [0.1457, 0.1477] ms; change relative to the copy call at home: -234.9 %
- per repetition: direct home 0 link read bytes and 937.2 SMMU translation requests; copy home 0 link read bytes and 16 SMMU translation requests; direct level 0 link read bytes and 940.7 SMMU translation requests; copy level 0 link read bytes and 3.421e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x5368c0000000, copy home 0x536980000000, direct level 0x536a40000000, copy level 0x536b00000000
- factor effect within the cell: on the direct route 0.0021 [0.0016, 0.0025] ms, on the copy route -0.3140 [-0.4137, -0.1993] ms; change relative to the copy call at home: +34.1 %
- per repetition: direct home 0 link read bytes and 941.2 SMMU translation requests; copy home 0 link read bytes and 550.4 SMMU translation requests; direct level 0 link read bytes and 941.7 SMMU translation requests; copy level 0 link read bytes and 549.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x55ac80000000, copy home 0x55ad40000000, direct level 0x55ae00000000, copy level 0x55aec0000000
- factor effect within the cell: on the direct route 0.0091 [0.0078, 0.0110] ms, on the copy route 0.5838 [0.5824, 0.5898] ms; change relative to the copy call at home: -195.9 %
- per repetition: direct home 2.145e+09 link read bytes and 677.2 SMMU translation requests; copy home 0 link read bytes and 12.16 SMMU translation requests; direct level 2.145e+09 link read bytes and 661.8 SMMU translation requests; copy level 1.074e+08 link read bytes and 8896 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x404fc0000000, copy home 0x4050c0000000, direct level 0x405180000000, copy level 0x405240000000
- factor effect within the cell: on the direct route 0.0001 [-0.0002, 0.0005] ms, on the copy route 0.5725 [0.5720, 0.5731] ms; change relative to the copy call at home: -888.2 %
- per repetition: direct home 8.382e+06 link read bytes and 328.8 SMMU translation requests; copy home 0 link read bytes and 10.24 SMMU translation requests; direct level 8.382e+06 link read bytes and 328 SMMU translation requests; copy level 1.074e+08 link read bytes and 6784 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x54dcc0000000, copy home 0x54ddc0000000, direct level 0x54de80000000, copy level 0x54df40000000
- factor effect within the cell: on the direct route -0.0472 [-0.0677, -0.0393] ms, on the copy route 0.0035 [0.0028, 0.0038] ms; change relative to the copy call at home: -12.9 %
- per repetition: direct home 2.145e+09 link read bytes and 207.4 SMMU translation requests; copy home 3.354e+07 link read bytes and 533.2 SMMU translation requests; direct level 2.145e+09 link read bytes and 101.1 SMMU translation requests; copy level 3.354e+07 link read bytes and 533.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4841c0000000, copy home 0x4842c0000000, direct level 0x484380000000, copy level 0x484440000000
- factor effect within the cell: on the direct route 0.0012 [0.0004, 0.0017] ms, on the copy route 0.0008 [-0.0003, 0.0020] ms; change relative to the copy call at home: +0.3 %
- per repetition: direct home 8.382e+06 link read bytes and 316.3 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 318.7 SMMU translation requests; copy level 8.38e+06 link read bytes and 131.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x41ca80000000, copy home 0x41cb80000000, direct level 0x41cc40000000, copy level 0x41cd00000000
- factor effect within the cell: on the direct route -0.0003 [-0.0016, 0.0007] ms, on the copy route 0.1409 [0.1397, 0.1430] ms; change relative to the copy call at home: -46.5 %
- per repetition: direct home 0 link read bytes and 945.9 SMMU translation requests; copy home 0 link read bytes and 16 SMMU translation requests; direct level 0 link read bytes and 952.3 SMMU translation requests; copy level 0 link read bytes and 3.221e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x404340000000, copy home 0x404440000000, direct level 0x404500000000, copy level 0x4045c0000000
- factor effect within the cell: on the direct route 0.0092 [0.0090, 0.0096] ms, on the copy route -1.7896 [-2.2464, -1.3712] ms; change relative to the copy call at home: +65.4 %
- per repetition: direct home 0 link read bytes and 961 SMMU translation requests; copy home 0 link read bytes and 549 SMMU translation requests; direct level 0 link read bytes and 961.8 SMMU translation requests; copy level 0 link read bytes and 551 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5e3740000000, copy home 0x5e3840000000, direct level 0x5e3900000000, copy level 0x5e3a00000000
- factor effect within the cell: on the direct route -0.0164 [-0.0347, -0.0058] ms, on the copy route 0.5840 [0.5836, 0.5860] ms; change relative to the copy call at home: -122.4 %
- per repetition: direct home 5.369e+08 link read bytes and 1.741e+04 SMMU translation requests; copy home 0 link read bytes and 14.37 SMMU translation requests; direct level 5.369e+08 link read bytes and 8730 SMMU translation requests; copy level 1.074e+08 link read bytes and 1.628e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5fa680000000, copy home 0x5fa780000000, direct level 0x5fa840000000, copy level 0x5fa940000000
- factor effect within the cell: on the direct route -0.0045 [-0.0054, -0.0032] ms, on the copy route 0.0397 [0.0350, 0.0580] ms; change relative to the copy call at home: -1.3 %
- per repetition: direct home 5.369e+08 link read bytes and 0 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.641e+04 SMMU translation requests; direct level 5.369e+08 link read bytes and 0 SMMU translation requests; copy level 1.074e+09 link read bytes and 1.646e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5ee2c0000000, copy home 0x5ee400000000, direct level 0x5ee4c0000000, copy level 0x5ee5c0000000
- factor effect within the cell: on the direct route 0.0012 [-0.0012, 0.0034] ms, on the copy route 0.1036 [0.0930, 0.1080] ms; change relative to the copy call at home: -18.3 %
- per repetition: direct home 0 link read bytes and 1.741e+04 SMMU translation requests; copy home 0 link read bytes and 16.77 SMMU translation requests; direct level 0 link read bytes and 1.741e+04 SMMU translation requests; copy level 0 link read bytes and 3.683e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4f1180000000, copy home 0x4f1280000000, direct level 0x4f1340000000, copy level 0x4f1440000000
- factor effect within the cell: on the direct route -0.0004 [-0.0021, 0.0017] ms, on the copy route -0.0170 [-0.0175, -0.0138] ms; change relative to the copy call at home: +1.3 %
- per repetition: direct home 0 link read bytes and 1.74e+04 SMMU translation requests; copy home 0 link read bytes and 3.636e+04 SMMU translation requests; direct level 0 link read bytes and 1.74e+04 SMMU translation requests; copy level 0 link read bytes and 3.696e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=11520,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x551a80000000, copy home 0x551dc0000000, direct level 0x552140000000, copy level 0x5524c0000000
- factor effect within the cell: on the direct route 0.0139 [-0.0533, 0.1076] ms, on the copy route 3.4701 [3.4219, 3.4976] ms; change relative to the copy call at home: -672.6 %
- per repetition: direct home 5.369e+08 link read bytes and 6.723e+07 SMMU translation requests; copy home 0 link read bytes and 4.213 SMMU translation requests; direct level 5.369e+08 link read bytes and 6.722e+07 SMMU translation requests; copy level 1.208e+09 link read bytes and 2.106e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=11520,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4b6000000000, copy home 0x4b6340000000, direct level 0x4b66c0000000, copy level 0x4b6a40000000
- factor effect within the cell: on the direct route -0.0261 [-0.0642, 0.2242] ms, on the copy route -1.4782 [-1.4955, -1.4439] ms; change relative to the copy call at home: +4.4 %
- per repetition: direct home 5.369e+08 link read bytes and 6.724e+07 SMMU translation requests; copy home 1.211e+10 link read bytes and 1.843e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 6.722e+07 SMMU translation requests; copy level 1.211e+10 link read bytes and 1.844e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5deac0000000, copy home 0x5dee40000000, direct level 0x5df1c0000000, copy level 0x5df580000000
- factor effect within the cell: on the direct route 0.0798 [0.0453, 0.2754] ms, on the copy route 3.7008 [3.6891, 3.7226] ms; change relative to the copy call at home: -693.2 %
- per repetition: direct home 5.369e+08 link read bytes and 7.819e+07 SMMU translation requests; copy home 0 link read bytes and 3.125 SMMU translation requests; direct level 5.369e+08 link read bytes and 7.82e+07 SMMU translation requests; copy level 1.288e+09 link read bytes and 2.219e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4f5040000000, copy home 0x4f53c0000000, direct level 0x4f5740000000, copy level 0x4f5b00000000
- factor effect within the cell: on the direct route 0.0007 [-0.0994, 0.1570] ms, on the copy route -1.3746 [-1.3967, -1.3651] ms; change relative to the copy call at home: +3.9 %
- per repetition: direct home 5.369e+08 link read bytes and 7.818e+07 SMMU translation requests; copy home 1.292e+10 link read bytes and 1.967e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 7.818e+07 SMMU translation requests; copy level 1.292e+10 link read bytes and 1.967e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4a6740000000, copy home 0x4a6b00000000, direct level 0x4a6e80000000, copy level 0x4a7240000000
- factor effect within the cell: on the direct route 1.3116 [1.1267, 1.5030] ms, on the copy route 1.8843 [1.8597, 1.8949] ms; change relative to the copy call at home: -99.4 %
- per repetition: direct home 0 link read bytes and 7.777e+07 SMMU translation requests; copy home 0 link read bytes and 16.78 SMMU translation requests; direct level 0 link read bytes and 7.778e+07 SMMU translation requests; copy level 0 link read bytes and 4.466e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x512700000000, copy home 0x512ac0000000, direct level 0x512e40000000, copy level 0x513200000000
- factor effect within the cell: on the direct route -2.8066 [-2.9343, -2.6618] ms, on the copy route -0.0381 [-0.0884, 0.0142] ms; change relative to the copy call at home: -33.2 %
- per repetition: direct home 0 link read bytes and 7.777e+07 SMMU translation requests; copy home 0 link read bytes and 4.446e+05 SMMU translation requests; direct level 0 link read bytes and 7.777e+07 SMMU translation requests; copy level 0 link read bytes and 4.518e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1536,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x58a7c0000000, copy home 0x58a8c0000000, direct level 0x58a9c0000000, copy level 0x58aac0000000
- factor effect within the cell: on the direct route -0.0117 [-0.0520, 0.0113] ms, on the copy route 0.7604 [0.7558, 0.7669] ms; change relative to the copy call at home: -153.7 %
- per repetition: direct home 5.369e+08 link read bytes and 1.923e+04 SMMU translation requests; copy home 0 link read bytes and 12.61 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.924e+04 SMMU translation requests; copy level 1.611e+08 link read bytes and 1.867e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1536,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x530380000000, copy home 0x530480000000, direct level 0x530580000000, copy level 0x530680000000
- factor effect within the cell: on the direct route -0.0053 [-0.0064, -0.0033] ms, on the copy route -0.0164 [-0.0261, -0.0124] ms; change relative to the copy call at home: +0.2 %
- per repetition: direct home 5.369e+08 link read bytes and 0 SMMU translation requests; copy home 1.611e+09 link read bytes and 2.46e+04 SMMU translation requests; direct level 5.369e+08 link read bytes and 0 SMMU translation requests; copy level 1.611e+09 link read bytes and 2.463e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x443e40000000, copy home 0x444300000000, direct level 0x4447c0000000, copy level 0x444c40000000
- factor effect within the cell: on the direct route -0.4046 [-0.4378, -0.2849] ms, on the copy route -3.2051 [-3.2144, -3.1750] ms; change relative to the copy call at home: +5.7 %
- per repetition: direct home 4.962e+10 link read bytes and 2.726e+05 SMMU translation requests; copy home 1.718e+10 link read bytes and 2.766e+05 SMMU translation requests; direct level 4.961e+10 link read bytes and 2.733e+05 SMMU translation requests; copy level 1.718e+10 link read bytes and 2.766e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x502780000000, copy home 0x502c40000000, direct level 0x5030c0000000, copy level 0x503540000000
- factor effect within the cell: on the direct route -0.0278 [-0.0426, -0.0075] ms, on the copy route -3.4995 [-3.5038, -3.4925] ms; change relative to the copy call at home: +7.5 %
- per repetition: direct home 3.355e+07 link read bytes and 2.024e+06 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; direct level 3.355e+07 link read bytes and 2.015e+06 SMMU translation requests; copy level 1.723e+10 link read bytes and 2.623e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4ff640000000, copy home 0x4ffb00000000, direct level 0x4fff80000000, copy level 0x500440000000
- factor effect within the cell: on the direct route 0.0229 [-0.1042, 0.1501] ms, on the copy route 4.7674 [4.6973, 4.7900] ms; change relative to the copy call at home: -915.5 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 0 link read bytes and 3.35 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy level 1.718e+09 link read bytes and 2.935e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4433c0000000, copy home 0x443880000000, direct level 0x443d00000000, copy level 0x4441c0000000
- factor effect within the cell: on the direct route 0.0906 [-0.1364, 0.2741] ms, on the copy route 10.1402 [10.1275, 10.1569] ms; change relative to the copy call at home: -1942.0 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 0 link read bytes and 2.346 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy level 1.718e+09 link read bytes and 6.984e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x579540000000, copy home 0x579a00000000, direct level 0x579e80000000, copy level 0x57a340000000
- factor effect within the cell: on the direct route -0.0193 [-0.2607, 0.2215] ms, on the copy route -3.5771 [-3.6147, -3.5494] ms; change relative to the copy call at home: +7.7 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy level 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=2048,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x473200000000, copy home 0x473300000000, direct level 0x473400000000, copy level 0x473540000000
- factor effect within the cell: on the direct route 0.0203 [-0.0394, 0.0489] ms, on the copy route 0.7978 [0.7949, 0.8020] ms; change relative to the copy call at home: -154.6 %
- per repetition: direct home 5.369e+08 link read bytes and 1.697e+04 SMMU translation requests; copy home 0 link read bytes and 10 SMMU translation requests; direct level 5.369e+08 link read bytes and 2.543e+04 SMMU translation requests; copy level 2.147e+08 link read bytes and 2.122e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=2048,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4c0b40000000, copy home 0x4c0c80000000, direct level 0x4c0d80000000, copy level 0x4c0ec0000000
- factor effect within the cell: on the direct route -0.0113 [-0.0116, -0.0097] ms, on the copy route 0.0421 [0.0355, 0.0519] ms; change relative to the copy call at home: -0.8 %
- per repetition: direct home 5.369e+08 link read bytes and 0 SMMU translation requests; copy home 2.147e+09 link read bytes and 3.279e+04 SMMU translation requests; direct level 5.369e+08 link read bytes and 0 SMMU translation requests; copy level 2.147e+09 link read bytes and 3.281e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=24576,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x532e00000000, copy home 0x5334c0000000, direct level 0x533b80000000, copy level 0x534200000000
- factor effect within the cell: on the direct route -0.1910 [-0.3413, -0.0964] ms, on the copy route -1.4995 [-1.6345, -1.4595] ms; change relative to the copy call at home: +1.8 %
- per repetition: direct home 7.683e+10 link read bytes and 5.096e+05 SMMU translation requests; copy home 2.577e+10 link read bytes and 4.146e+05 SMMU translation requests; direct level 7.684e+10 link read bytes and 4.994e+05 SMMU translation requests; copy level 2.577e+10 link read bytes and 4.146e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=24576,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x426f80000000, copy home 0x427640000000, direct level 0x427cc0000000, copy level 0x428380000000
- factor effect within the cell: on the direct route 0.0686 [-0.1086, 0.2950] ms, on the copy route 7.1155 [6.9998, 7.1271] ms; change relative to the copy call at home: -1352.2 %
- per repetition: direct home 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; copy home 0 link read bytes and 2.141 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; copy level 2.577e+09 link read bytes and 5.348e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=24576,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x454040000000, copy home 0x454700000000, direct level 0x454d80000000, copy level 0x455440000000
- factor effect within the cell: on the direct route 0.0300 [-0.2140, 0.2727] ms, on the copy route -3.8228 [-3.8453, -3.7962] ms; change relative to the copy call at home: +5.6 %
- per repetition: direct home 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; copy home 2.585e+10 link read bytes and 3.933e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; copy level 2.585e+10 link read bytes and 3.933e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=256,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x432200000000, copy home 0x4322c0000000, direct level 0x432340000000, copy level 0x4323c0000000
- factor effect within the cell: on the direct route -0.0178 [-0.0200, -0.0161] ms, on the copy route -0.0645 [-0.0667, -0.0350] ms; change relative to the copy call at home: +3.7 %
- per repetition: direct home 7.678e+08 link read bytes and 0 SMMU translation requests; copy home 2.684e+08 link read bytes and 4229 SMMU translation requests; direct level 7.683e+08 link read bytes and 0 SMMU translation requests; copy level 2.684e+08 link read bytes and 4228 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=256,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x53d940000000, copy home 0x53da00000000, direct level 0x53da80000000, copy level 0x53db00000000
- factor effect within the cell: on the direct route 0.0014 [0.0003, 0.0020] ms, on the copy route 0.0007 [0.0001, 0.0009] ms; change relative to the copy call at home: +0.1 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 4228 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 4228 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x42b9c0000000, copy home 0x42bac0000000, direct level 0x42bb40000000, copy level 0x42bc00000000
- factor effect within the cell: on the direct route 0.0036 [0.0027, 0.0042] ms, on the copy route 0.1619 [0.1616, 0.1626] ms; change relative to the copy call at home: -35.6 %
- per repetition: direct home 5.368e+08 link read bytes and 4953 SMMU translation requests; copy home 0 link read bytes and 16.24 SMMU translation requests; direct level 5.368e+08 link read bytes and 4972 SMMU translation requests; copy level 2.684e+07 link read bytes and 8553 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4fb980000000, copy home 0x4fba40000000, direct level 0x4fbb00000000, copy level 0x4fbbc0000000
- factor effect within the cell: on the direct route -0.0060 [-0.0080, -0.0051] ms, on the copy route 0.0430 [0.0417, 0.0440] ms; change relative to the copy call at home: -4.0 %
- per repetition: direct home 5.368e+08 link read bytes and 0 SMMU translation requests; copy home 2.684e+08 link read bytes and 4130 SMMU translation requests; direct level 5.368e+08 link read bytes and 0 SMMU translation requests; copy level 2.684e+08 link read bytes and 4130 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x444e80000000, copy home 0x444f40000000, direct level 0x444fc0000000, copy level 0x4450c0000000
- factor effect within the cell: on the direct route -0.0070 [-0.0094, -0.0056] ms, on the copy route 0.0522 [0.0481, 0.0539] ms; change relative to the copy call at home: -11.8 %
- per repetition: direct home 0 link read bytes and 4982 SMMU translation requests; copy home 0 link read bytes and 16.78 SMMU translation requests; direct level 0 link read bytes and 4978 SMMU translation requests; copy level 0 link read bytes and 9308 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5adc00000000, copy home 0x5adcc0000000, direct level 0x5add80000000, copy level 0x5ade40000000
- factor effect within the cell: on the direct route -0.0125 [-0.0128, -0.0117] ms, on the copy route -0.1358 [-0.1389, -0.1321] ms; change relative to the copy call at home: +9.8 %
- per repetition: direct home 0 link read bytes and 4970 SMMU translation requests; copy home 0 link read bytes and 4132 SMMU translation requests; direct level 0 link read bytes and 4960 SMMU translation requests; copy level 0 link read bytes and 4132 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=32768,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4555c0000000, copy home 0x455ec0000000, direct level 0x456780000000, copy level 0x457000000000
- factor effect within the cell: on the direct route -0.5412 [-0.7438, -0.3418] ms, on the copy route -3.0119 [-3.0664, -2.9850] ms; change relative to the copy call at home: +2.6 %
- per repetition: direct home 9.935e+10 link read bytes and 7.696e+05 SMMU translation requests; copy home 3.436e+10 link read bytes and 5.527e+05 SMMU translation requests; direct level 9.935e+10 link read bytes and 7.572e+05 SMMU translation requests; copy level 3.436e+10 link read bytes and 5.528e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=32768,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5b1780000000, copy home 0x5b2000000000, direct level 0x5b2880000000, copy level 0x5b3140000000
- factor effect within the cell: on the direct route 0.0949 [-0.0644, 0.1427] ms, on the copy route 9.3834 [9.3754, 9.3945] ms; change relative to the copy call at home: -1794.9 %
- per repetition: direct home 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; copy home 0 link read bytes and 1.308 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.912e+08 SMMU translation requests; copy level 3.436e+09 link read bytes and 8.794e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=32768,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4fbd80000000, copy home 0x4fc640000000, direct level 0x4fcec0000000, copy level 0x4fd780000000
- factor effect within the cell: on the direct route 0.0480 [-0.0934, 0.2013] ms, on the copy route -2.0607 [-2.1113, -2.0105] ms; change relative to the copy call at home: +2.4 %
- per repetition: direct home 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; copy home 3.448e+10 link read bytes and 5.245e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; copy level 3.448e+10 link read bytes and 5.246e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=4096,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x404340000000, copy home 0x4044c0000000, direct level 0x404680000000, copy level 0x404800000000
- factor effect within the cell: on the direct route -2.2769 [-2.3289, -2.1460] ms, on the copy route 0.0855 [0.0780, 0.0919] ms; change relative to the copy call at home: -18.8 %
- per repetition: direct home 1.286e+10 link read bytes and 6.865e+04 SMMU translation requests; copy home 4.295e+09 link read bytes and 6.83e+04 SMMU translation requests; direct level 1.285e+10 link read bytes and 6.876e+04 SMMU translation requests; copy level 4.295e+09 link read bytes and 6.832e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=4096,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x56ff40000000, copy home 0x570100000000, direct level 0x570280000000, copy level 0x570400000000
- factor effect within the cell: on the direct route -0.0249 [-0.0284, -0.0211] ms, on the copy route 0.0036 [-0.0086, 0.0254] ms; change relative to the copy call at home: -0.3 %
- per repetition: direct home 0 link read bytes and 4.162e+04 SMMU translation requests; copy home 0 link read bytes and 5.68e+04 SMMU translation requests; direct level 0 link read bytes and 4.342e+04 SMMU translation requests; copy level 0 link read bytes and 5.65e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4ca100000000, copy home 0x4ca280000000, direct level 0x4ca400000000, copy level 0x4ca5c0000000
- factor effect within the cell: on the direct route 0.0501 [-0.0208, 0.1134] ms, on the copy route 1.2852 [1.2674, 1.2949] ms; change relative to the copy call at home: -244.9 %
- per repetition: direct home 5.369e+08 link read bytes and 2.498e+04 SMMU translation requests; copy home 0 link read bytes and 5.662 SMMU translation requests; direct level 5.369e+08 link read bytes and 4.166e+04 SMMU translation requests; copy level 4.295e+08 link read bytes and 2.679e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x484c40000000, copy home 0x484e00000000, direct level 0x484f80000000, copy level 0x485140000000
- factor effect within the cell: on the direct route 0.0392 [0.0050, 0.0684] ms, on the copy route 0.1734 [0.1540, 0.2060] ms; change relative to the copy call at home: -1.1 %
- per repetition: direct home 5.369e+08 link read bytes and 1194 SMMU translation requests; copy home 4.295e+09 link read bytes and 6.556e+04 SMMU translation requests; direct level 5.369e+08 link read bytes and 1228 SMMU translation requests; copy level 4.295e+09 link read bytes and 6.557e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x566e00000000, copy home 0x566f80000000, direct level 0x567100000000, copy level 0x5672c0000000
- factor effect within the cell: on the direct route 0.0211 [0.0173, 0.0250] ms, on the copy route 0.5580 [0.5478, 0.5638] ms; change relative to the copy call at home: -95.6 %
- per repetition: direct home 0 link read bytes and 6.66e+04 SMMU translation requests; copy home 0 link read bytes and 16.84 SMMU translation requests; direct level 0 link read bytes and 6.664e+04 SMMU translation requests; copy level 0 link read bytes and 1.551e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x43adc0000000, copy home 0x43af80000000, direct level 0x43b100000000, copy level 0x43b2c0000000
- factor effect within the cell: on the direct route 0.0076 [-0.0008, 0.0148] ms, on the copy route 0.0010 [-0.0125, 0.0132] ms; change relative to the copy call at home: +0.2 %
- per repetition: direct home 0 link read bytes and 6.662e+04 SMMU translation requests; copy home 0 link read bytes and 1.379e+05 SMMU translation requests; direct level 0 link read bytes and 6.661e+04 SMMU translation requests; copy level 0 link read bytes and 1.37e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=1,tiling=tiles,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x473e00000000, copy home 0x473f00000000, direct level 0x474000000000, copy level 0x4740c0000000
- factor effect within the cell: on the direct route -0.7229 [-0.7280, -0.7137] ms, on the copy route -0.0540 [-0.0584, -0.0522] ms; change relative to the copy call at home: -17.9 %
- per repetition: direct home 8.028e+08 link read bytes and 3704 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 8.028e+08 link read bytes and 3165 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=16,tiling=tiles,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5f1600000000, copy home 0x5f1700000000, direct level 0x5f17c0000000, copy level 0x5f18c0000000
- factor effect within the cell: on the direct route -8.1398 [-8.1804, -8.0855] ms, on the copy route -0.0365 [-0.0559, -0.0316] ms; change relative to the copy call at home: -83.0 %
- per repetition: direct home 1.284e+10 link read bytes and 3.619e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 1.285e+10 link read bytes and 3.595e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=2,tiling=tiles,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5c1400000000, copy home 0x5c1500000000, direct level 0x5c15c0000000, copy level 0x5c16c0000000
- factor effect within the cell: on the direct route -1.2282 [-1.2366, -1.2197] ms, on the copy route -0.0701 [-0.0741, -0.0680] ms; change relative to the copy call at home: -27.9 %
- per repetition: direct home 1.606e+09 link read bytes and 1.2e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 1.606e+09 link read bytes and 8945 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=4,tiling=tiles,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4e9400000000, copy home 0x4e9500000000, direct level 0x4e9600000000, copy level 0x4e96c0000000
- factor effect within the cell: on the direct route -1.9371 [-1.9459, -1.9178] ms, on the copy route -0.0372 [-0.0431, -0.0323] ms; change relative to the copy call at home: -38.5 %
- per repetition: direct home 3.211e+09 link read bytes and 1.807e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 3.211e+09 link read bytes and 1.795e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=64,tiling=tiles,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x59dfc0000000, copy home 0x59e0c0000000, direct level 0x59e180000000, copy level 0x59e280000000
- factor effect within the cell: on the direct route -35.4445 [-35.5948, -35.3898] ms, on the copy route -0.0411 [-0.0698, -0.0110] ms; change relative to the copy call at home: -121.8 %
- per repetition: direct home 5.138e+10 link read bytes and 3.605e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 5.138e+10 link read bytes and 3.586e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x56da40000000, copy home 0x56db40000000, direct level 0x56dc40000000, copy level 0x56dd00000000
- factor effect within the cell: on the direct route -3.6645 [-3.6793, -3.6417] ms, on the copy route -0.0758 [-0.0842, -0.0656] ms; change relative to the copy call at home: -55.1 %
- per repetition: direct home 6.422e+09 link read bytes and 3.605e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 6.423e+09 link read bytes and 3.585e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=1,tiling=tiles,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4c8980000000, copy home 0x4c8a80000000, direct level 0x4c8b40000000, copy level 0x4c8c40000000
- factor effect within the cell: on the direct route -0.0001 [-0.0007, 0.0007] ms, on the copy route -0.0014 [-0.0019, 0.0001] ms; change relative to the copy call at home: +0.1 %
- per repetition: direct home 0 link read bytes and 590.3 SMMU translation requests; copy home 0 link read bytes and 1903 SMMU translation requests; direct level 0 link read bytes and 591.8 SMMU translation requests; copy level 0 link read bytes and 1806 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=16,tiling=tiles,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x52cd80000000, copy home 0x52ce80000000, direct level 0x52cf80000000, copy level 0x52d040000000
- factor effect within the cell: on the direct route -0.0501 [-0.0659, -0.0224] ms, on the copy route 0.0063 [-0.0116, 0.0102] ms; change relative to the copy call at home: -0.8 %
- per repetition: direct home 0 link read bytes and 9632 SMMU translation requests; copy home 0 link read bytes and 1.195e+04 SMMU translation requests; direct level 0 link read bytes and 9583 SMMU translation requests; copy level 0 link read bytes and 1.202e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=2,tiling=tiles,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x589300000000, copy home 0x589440000000, direct level 0x589500000000, copy level 0x589600000000
- factor effect within the cell: on the direct route 0.0052 [0.0031, 0.0079] ms, on the copy route 0.0015 [0.0003, 0.0033] ms; change relative to the copy call at home: +0.2 %
- per repetition: direct home 0 link read bytes and 1683 SMMU translation requests; copy home 0 link read bytes and 2624 SMMU translation requests; direct level 0 link read bytes and 1529 SMMU translation requests; copy level 0 link read bytes and 2601 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=4,tiling=tiles,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x56f140000000, copy home 0x56f240000000, direct level 0x56f340000000, copy level 0x56f440000000
- factor effect within the cell: on the direct route -0.0060 [-0.0089, 0.0011] ms, on the copy route -0.0020 [-0.0059, -0.0014] ms; change relative to the copy call at home: -0.2 %
- per repetition: direct home 0 link read bytes and 2966 SMMU translation requests; copy home 0 link read bytes and 3992 SMMU translation requests; direct level 0 link read bytes and 2944 SMMU translation requests; copy level 0 link read bytes and 4083 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=64,tiling=tiles,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x56e8c0000000, copy home 0x56e9c0000000, direct level 0x56eac0000000, copy level 0x56eb80000000
- factor effect within the cell: on the direct route 0.0142 [-0.0287, 0.0750] ms, on the copy route 0.0276 [-0.0687, 0.0580] ms; change relative to the copy call at home: +0.0 %
- per repetition: direct home 0 link read bytes and 4.143e+04 SMMU translation requests; copy home 0 link read bytes and 3.785e+04 SMMU translation requests; direct level 0 link read bytes and 3.824e+04 SMMU translation requests; copy level 0 link read bytes and 3.916e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x466a40000000, copy home 0x466b80000000, direct level 0x466c40000000, copy level 0x466d40000000
- factor effect within the cell: on the direct route 0.0244 [0.0163, 0.0370] ms, on the copy route -0.0008 [-0.0034, 0.0032] ms; change relative to the copy call at home: +0.7 %
- per repetition: direct home 0 link read bytes and 5989 SMMU translation requests; copy home 0 link read bytes and 5893 SMMU translation requests; direct level 0 link read bytes and 5435 SMMU translation requests; copy level 0 link read bytes and 6161 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=1,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4e7100000000, copy home 0x4e7200000000, direct level 0x4e7300000000, copy level 0x4e73c0000000
- factor effect within the cell: on the direct route -0.6406 [-0.6437, -0.6383] ms, on the copy route 0.2994 [0.2984, 0.3000] ms; change relative to the copy call at home: -42.1 %
- per repetition: direct home 8.028e+08 link read bytes and 2.217e+04 SMMU translation requests; copy home 0 link read bytes and 8209 SMMU translation requests; direct level 8.028e+08 link read bytes and 1.907e+04 SMMU translation requests; copy level 5.369e+07 link read bytes and 2.393e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=16,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x435900000000, copy home 0x435a00000000, direct level 0x435ac0000000, copy level 0x435bc0000000
- factor effect within the cell: on the direct route -6.6741 [-6.7069, -6.6329] ms, on the copy route 0.3003 [0.2929, 0.3220] ms; change relative to the copy call at home: -84.8 %
- per repetition: direct home 1.284e+10 link read bytes and 3.609e+04 SMMU translation requests; copy home 0 link read bytes and 8209 SMMU translation requests; direct level 1.285e+10 link read bytes and 3.601e+04 SMMU translation requests; copy level 5.369e+07 link read bytes and 2.459e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=2,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x50a140000000, copy home 0x50a240000000, direct level 0x50a300000000, copy level 0x50a400000000
- factor effect within the cell: on the direct route -1.0391 [-1.0487, -1.0328] ms, on the copy route 0.2974 [0.2964, 0.3005] ms; change relative to the copy call at home: -50.8 %
- per repetition: direct home 1.606e+09 link read bytes and 3.621e+04 SMMU translation requests; copy home 0 link read bytes and 8209 SMMU translation requests; direct level 1.606e+09 link read bytes and 3.612e+04 SMMU translation requests; copy level 5.369e+07 link read bytes and 2.372e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=4,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4b5680000000, copy home 0x4b5780000000, direct level 0x4b5840000000, copy level 0x4b5940000000
- factor effect within the cell: on the direct route -1.9534 [-1.9864, -1.9372] ms, on the copy route 0.2991 [0.2918, 0.3030] ms; change relative to the copy call at home: -65.5 %
- per repetition: direct home 3.211e+09 link read bytes and 3.598e+04 SMMU translation requests; copy home 0 link read bytes and 8209 SMMU translation requests; direct level 3.211e+09 link read bytes and 3.597e+04 SMMU translation requests; copy level 5.369e+07 link read bytes and 2.462e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=64,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x412c80000000, copy home 0x412dc0000000, direct level 0x412e80000000, copy level 0x412f80000000
- factor effect within the cell: on the direct route -32.3832 [-32.4629, -32.2705] ms, on the copy route 0.2336 [0.1943, 0.2805] ms; change relative to the copy call at home: -118.5 %
- per repetition: direct home 5.138e+10 link read bytes and 3.616e+04 SMMU translation requests; copy home 0 link read bytes and 8208 SMMU translation requests; direct level 5.138e+10 link read bytes and 3.59e+04 SMMU translation requests; copy level 5.369e+07 link read bytes and 2.459e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4801c0000000, copy home 0x4802c0000000, direct level 0x4803c0000000, copy level 0x480480000000
- factor effect within the cell: on the direct route -3.4543 [-3.4688, -3.4356] ms, on the copy route 0.2937 [0.2872, 0.2995] ms; change relative to the copy call at home: -74.4 %
- per repetition: direct home 6.422e+09 link read bytes and 3.603e+04 SMMU translation requests; copy home 0 link read bytes and 8209 SMMU translation requests; direct level 6.423e+09 link read bytes and 3.589e+04 SMMU translation requests; copy level 5.369e+07 link read bytes and 2.491e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x51e5c0000000, copy home 0x51e6c0000000, direct level 0x51e7c0000000, copy level 0x51e8c0000000
- factor effect within the cell: on the direct route -2.8134 [-2.8376, -2.7906] ms, on the copy route 0.3438 [0.3333, 0.3459] ms; change relative to the copy call at home: -62.7 %
- per repetition: direct home 6.422e+09 link read bytes and 3.612e+04 SMMU translation requests; copy home 0 link read bytes and 8209 SMMU translation requests; direct level 6.423e+09 link read bytes and 3.609e+04 SMMU translation requests; copy level 5.369e+07 link read bytes and 3.309e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=1,tiling=tiles,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x56ad00000000, copy home 0x56ae00000000, direct level 0x56af00000000, copy level 0x56afc0000000
- factor effect within the cell: on the direct route -0.6303 [-0.6336, -0.6245] ms, on the copy route 0.0375 [0.0318, 0.0546] ms; change relative to the copy call at home: -17.9 %
- per repetition: direct home 8.028e+08 link read bytes and 3682 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 8.028e+08 link read bytes and 3168 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.645e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=16,tiling=tiles,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4f4080000000, copy home 0x4f4180000000, direct level 0x4f4240000000, copy level 0x4f4340000000
- factor effect within the cell: on the direct route -8.2039 [-8.2607, -8.1620] ms, on the copy route 0.0758 [0.0690, 0.0856] ms; change relative to the copy call at home: -84.8 %
- per repetition: direct home 1.284e+10 link read bytes and 3.603e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 1.285e+10 link read bytes and 3.598e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.645e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=2,tiling=tiles,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5f7200000000, copy home 0x5f7300000000, direct level 0x5f7400000000, copy level 0x5f74c0000000
- factor effect within the cell: on the direct route -0.8461 [-0.8541, -0.8265] ms, on the copy route 0.0523 [0.0506, 0.0544] ms; change relative to the copy call at home: -21.8 %
- per repetition: direct home 1.606e+09 link read bytes and 1.202e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 1.606e+09 link read bytes and 9014 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.645e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=4,tiling=tiles,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x451980000000, copy home 0x451a80000000, direct level 0x451b40000000, copy level 0x451c40000000
- factor effect within the cell: on the direct route -1.8042 [-1.8186, -1.7757] ms, on the copy route 0.0584 [0.0522, 0.0624] ms; change relative to the copy call at home: -37.7 %
- per repetition: direct home 3.211e+09 link read bytes and 1.804e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 3.211e+09 link read bytes and 1.8e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.646e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=64,tiling=tiles,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5727c0000000, copy home 0x5728c0000000, direct level 0x572980000000, copy level 0x572a80000000
- factor effect within the cell: on the direct route -31.0703 [-31.1771, -30.9728] ms, on the copy route 0.1269 [0.0788, 0.1816] ms; change relative to the copy call at home: -107.6 %
- per repetition: direct home 5.138e+10 link read bytes and 3.616e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 5.138e+10 link read bytes and 3.604e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.646e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x421ec0000000, copy home 0x422000000000, direct level 0x4220c0000000, copy level 0x4221c0000000
- factor effect within the cell: on the direct route -3.3859 [-3.4048, -3.3437] ms, on the copy route 0.0857 [0.0805, 0.0953] ms; change relative to the copy call at home: -53.2 %
- per repetition: direct home 6.422e+09 link read bytes and 3.602e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 6.423e+09 link read bytes and 3.596e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.647e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=1,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x48ed40000000, copy home 0x48ee40000000, direct level 0x48ef00000000, copy level 0x48f000000000
- factor effect within the cell: on the direct route 0.0233 [0.0218, 0.0247] ms, on the copy route 0.0910 [0.0903, 0.0918] ms; change relative to the copy call at home: -9.0 %
- per repetition: direct home 0 link read bytes and 3.046e+04 SMMU translation requests; copy home 0 link read bytes and 1.278e+04 SMMU translation requests; direct level 0 link read bytes and 3.261e+04 SMMU translation requests; copy level 0 link read bytes and 2.929e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=16,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x53efc0000000, copy home 0x53f0c0000000, direct level 0x53f180000000, copy level 0x53f280000000
- factor effect within the cell: on the direct route 0.1106 [0.1008, 0.1192] ms, on the copy route 0.0919 [0.0834, 0.1022] ms; change relative to the copy call at home: +0.3 %
- per repetition: direct home 0 link read bytes and 4.235e+04 SMMU translation requests; copy home 0 link read bytes and 1.295e+04 SMMU translation requests; direct level 0 link read bytes and 4.123e+04 SMMU translation requests; copy level 0 link read bytes and 3.024e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=2,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x43ef80000000, copy home 0x43f080000000, direct level 0x43f180000000, copy level 0x43f240000000
- factor effect within the cell: on the direct route 0.1217 [0.1188, 0.1253] ms, on the copy route 0.0928 [0.0909, 0.0960] ms; change relative to the copy call at home: +2.4 %
- per repetition: direct home 0 link read bytes and 4.279e+04 SMMU translation requests; copy home 0 link read bytes and 1.278e+04 SMMU translation requests; direct level 0 link read bytes and 4.179e+04 SMMU translation requests; copy level 0 link read bytes and 2.962e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=4,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x55bd00000000, copy home 0x55be00000000, direct level 0x55bf00000000, copy level 0x55bfc0000000
- factor effect within the cell: on the direct route 0.0276 [0.0236, 0.0331] ms, on the copy route 0.0850 [0.0829, 0.0895] ms; change relative to the copy call at home: -2.8 %
- per repetition: direct home 0 link read bytes and 3.868e+04 SMMU translation requests; copy home 0 link read bytes and 1.274e+04 SMMU translation requests; direct level 0 link read bytes and 4.164e+04 SMMU translation requests; copy level 0 link read bytes and 3.08e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=64,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4aa400000000, copy home 0x4aa500000000, direct level 0x4aa640000000, copy level 0x4aa700000000
- factor effect within the cell: on the direct route 0.0754 [0.0492, 0.1242] ms, on the copy route 0.0877 [0.0285, 0.1384] ms; change relative to the copy call at home: -0.0 %
- per repetition: direct home 0 link read bytes and 3.85e+04 SMMU translation requests; copy home 0 link read bytes and 1.381e+04 SMMU translation requests; direct level 0 link read bytes and 4.274e+04 SMMU translation requests; copy level 0 link read bytes and 2.96e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5dfd80000000, copy home 0x5dfe80000000, direct level 0x5dff80000000, copy level 0x5e00c0000000
- factor effect within the cell: on the direct route -0.0588 [-0.0702, -0.0525] ms, on the copy route 0.0897 [0.0858, 0.0987] ms; change relative to the copy call at home: -4.2 %
- per repetition: direct home 0 link read bytes and 3.858e+04 SMMU translation requests; copy home 0 link read bytes and 1.288e+04 SMMU translation requests; direct level 0 link read bytes and 4.503e+04 SMMU translation requests; copy level 0 link read bytes and 2.98e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x550f80000000, copy home 0x5510c0000000, direct level 0x551180000000, copy level 0x551280000000
- factor effect within the cell: on the direct route 0.0274 [0.0158, 0.0394] ms, on the copy route 0.3072 [0.3039, 0.3132] ms; change relative to the copy call at home: -7.9 %
- per repetition: direct home 0 link read bytes and 3.844e+04 SMMU translation requests; copy home 0 link read bytes and 1.318e+04 SMMU translation requests; direct level 0 link read bytes and 4.16e+04 SMMU translation requests; copy level 0 link read bytes and 3.585e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=1,tiling=tiles,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x436080000000, copy home 0x436180000000, direct level 0x436240000000, copy level 0x436340000000
- factor effect within the cell: on the direct route -0.0625 [-0.0654, -0.0605] ms, on the copy route -0.0244 [-0.0303, -0.0210] ms; change relative to the copy call at home: -3.1 %
- per repetition: direct home 0 link read bytes and 2.619e+04 SMMU translation requests; copy home 0 link read bytes and 3.152e+04 SMMU translation requests; direct level 0 link read bytes and 3.041e+04 SMMU translation requests; copy level 0 link read bytes and 3.068e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=16,tiling=tiles,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x50e440000000, copy home 0x50e580000000, direct level 0x50e640000000, copy level 0x50e740000000
- factor effect within the cell: on the direct route 0.1248 [0.1111, 0.1445] ms, on the copy route -0.0240 [-0.0312, -0.0106] ms; change relative to the copy call at home: +2.0 %
- per repetition: direct home 0 link read bytes and 4.238e+04 SMMU translation requests; copy home 0 link read bytes and 3.169e+04 SMMU translation requests; direct level 0 link read bytes and 3.829e+04 SMMU translation requests; copy level 0 link read bytes and 3.176e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=2,tiling=tiles,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5ac600000000, copy home 0x5ac700000000, direct level 0x5ac7c0000000, copy level 0x5ac8c0000000
- factor effect within the cell: on the direct route 0.0064 [-0.0028, 0.0142] ms, on the copy route -0.0228 [-0.0253, -0.0204] ms; change relative to the copy call at home: +1.9 %
- per repetition: direct home 0 link read bytes and 3.861e+04 SMMU translation requests; copy home 0 link read bytes and 3.202e+04 SMMU translation requests; direct level 0 link read bytes and 3.85e+04 SMMU translation requests; copy level 0 link read bytes and 3.127e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=4,tiling=tiles,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x455840000000, copy home 0x455940000000, direct level 0x455a40000000, copy level 0x455b00000000
- factor effect within the cell: on the direct route -0.0714 [-0.0762, -0.0677] ms, on the copy route -0.0241 [-0.0262, -0.0200] ms; change relative to the copy call at home: -2.0 %
- per repetition: direct home 0 link read bytes and 3.862e+04 SMMU translation requests; copy home 0 link read bytes and 3.155e+04 SMMU translation requests; direct level 0 link read bytes and 4.24e+04 SMMU translation requests; copy level 0 link read bytes and 3.182e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=64,tiling=tiles,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x42c500000000, copy home 0x42c600000000, direct level 0x42c700000000, copy level 0x42c7c0000000
- factor effect within the cell: on the direct route 0.0011 [-0.0521, 0.0552] ms, on the copy route -0.0519 [-0.1012, -0.0381] ms; change relative to the copy call at home: +0.3 %
- per repetition: direct home 0 link read bytes and 3.819e+04 SMMU translation requests; copy home 0 link read bytes and 3.59e+04 SMMU translation requests; direct level 0 link read bytes and 3.797e+04 SMMU translation requests; copy level 0 link read bytes and 3.586e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4ce300000000, copy home 0x4ce400000000, direct level 0x4ce4c0000000, copy level 0x4ce5c0000000
- factor effect within the cell: on the direct route -0.0601 [-0.0644, -0.0491] ms, on the copy route -0.0259 [-0.0366, -0.0221] ms; change relative to the copy call at home: -0.8 %
- per repetition: direct home 0 link read bytes and 3.852e+04 SMMU translation requests; copy home 0 link read bytes and 3.089e+04 SMMU translation requests; direct level 0 link read bytes and 4.239e+04 SMMU translation requests; copy level 0 link read bytes and 3.088e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5fdd80000000, copy home 0x5fe040000000, direct level 0x5fe2c0000000, copy level 0x5fe580000000
- factor effect within the cell: on the direct route -0.3585 [-0.4340, -0.1956] ms, on the copy route 0.0173 [-0.0223, 0.0682] ms; change relative to the copy call at home: -1.4 %
- per repetition: direct home 2.553e+10 link read bytes and 1.366e+05 SMMU translation requests; copy home 8.59e+09 link read bytes and 1.385e+05 SMMU translation requests; direct level 2.553e+10 link read bytes and 1.364e+05 SMMU translation requests; copy level 8.59e+09 link read bytes and 1.386e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x573680000000, copy home 0x573940000000, direct level 0x573bc0000000, copy level 0x573e40000000
- factor effect within the cell: on the direct route -0.0082 [-0.0131, 0.0055] ms, on the copy route -0.0218 [-0.0367, -0.0024] ms; change relative to the copy call at home: +0.1 %
- per repetition: direct home 0 link read bytes and 1.458e+05 SMMU translation requests; copy home 0 link read bytes and 3.334e+05 SMMU translation requests; direct level 0 link read bytes and 1.549e+05 SMMU translation requests; copy level 0 link read bytes and 3.222e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x575880000000, copy home 0x575b00000000, direct level 0x575d80000000, copy level 0x576040000000
- factor effect within the cell: on the direct route -0.0436 [-0.0444, -0.0420] ms, on the copy route 2.5603 [2.5215, 2.5786] ms; change relative to the copy call at home: -497.8 %
- per repetition: direct home 5.369e+08 link read bytes and 4.426e+04 SMMU translation requests; copy home 0 link read bytes and 2.525 SMMU translation requests; direct level 5.369e+08 link read bytes and 4.424e+04 SMMU translation requests; copy level 8.59e+08 link read bytes and 5.998e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x43f380000000, copy home 0x43f640000000, direct level 0x43f8c0000000, copy level 0x43fb80000000
- factor effect within the cell: on the direct route -0.0255 [-0.1692, -0.0220] ms, on the copy route 0.0123 [-0.0122, 0.0323] ms; change relative to the copy call at home: -0.2 %
- per repetition: direct home 5.369e+08 link read bytes and 4.426e+04 SMMU translation requests; copy home 8.607e+09 link read bytes and 1.311e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 4.422e+04 SMMU translation requests; copy level 8.607e+09 link read bytes and 1.311e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x503440000000, copy home 0x503700000000, direct level 0x503980000000, copy level 0x503c40000000
- factor effect within the cell: on the direct route 0.0246 [0.0206, 0.0297] ms, on the copy route 1.1103 [1.1031, 1.1157] ms; change relative to the copy call at home: -191.3 %
- per repetition: direct home 0 link read bytes and 1.327e+05 SMMU translation requests; copy home 0 link read bytes and 16.75 SMMU translation requests; direct level 0 link read bytes and 1.326e+05 SMMU translation requests; copy level 0 link read bytes and 3.021e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x431300000000, copy home 0x431580000000, direct level 0x431800000000, copy level 0x431ac0000000
- factor effect within the cell: on the direct route 0.0201 [0.0124, 0.0325] ms, on the copy route 4.9193 [4.8647, 4.9298] ms; change relative to the copy call at home: -863.7 %
- per repetition: direct home 0 link read bytes and 1.328e+05 SMMU translation requests; copy home 0 link read bytes and 16.82 SMMU translation requests; direct level 0 link read bytes and 1.326e+05 SMMU translation requests; copy level 0 link read bytes and 3.358e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5e81c0000000, copy home 0x5e8480000000, direct level 0x5e8700000000, copy level 0x5e89c0000000
- factor effect within the cell: on the direct route 0.0112 [0.0047, 0.0352] ms, on the copy route -0.0004 [-0.0139, 0.0066] ms; change relative to the copy call at home: +0.3 %
- per repetition: direct home 0 link read bytes and 1.327e+05 SMMU translation requests; copy home 0 link read bytes and 2.75e+05 SMMU translation requests; direct level 0 link read bytes and 1.325e+05 SMMU translation requests; copy level 0 link read bytes and 2.722e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=9728,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x570d00000000, copy home 0x571000000000, direct level 0x5712c0000000, copy level 0x571600000000
- factor effect within the cell: on the direct route 0.1087 [-0.0035, 0.1324] ms, on the copy route 3.0106 [2.9833, 3.0369] ms; change relative to the copy call at home: -564.1 %
- per repetition: direct home 5.369e+08 link read bytes and 3.597e+07 SMMU translation requests; copy home 0 link read bytes and 2.963 SMMU translation requests; direct level 5.369e+08 link read bytes and 3.598e+07 SMMU translation requests; copy level 1.02e+09 link read bytes and 1.713e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=9728,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 73; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5b0c00000000, copy home 0x5b0f00000000, direct level 0x5b11c0000000, copy level 0x5b1500000000
- factor effect within the cell: on the direct route 0.0464 [-0.0262, 0.1884] ms, on the copy route 0.1001 [0.0722, 0.1299] ms; change relative to the copy call at home: -0.1 %
- per repetition: direct home 5.369e+08 link read bytes and 3.598e+07 SMMU translation requests; copy home 1.02e+10 link read bytes and 1.621e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 3.597e+07 SMMU translation requests; copy level 1.02e+10 link read bytes and 1.624e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=sys,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2722 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5007c0000000, copy home 0x500880000000, direct level 0x500940000000, copy level 0x500a00000000
- factor effect within the cell: on the direct route 0.0005 [0.0005, 0.0005] ms, on the copy route 0.0000 [-0.0003, 0.0001] ms; change relative to the copy call at home: +0.9 %
- per repetition: direct home 8.38e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.7 SMMU translation requests; direct level 8.38e+06 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=sys,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=four,vary=scope,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2722 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x47ce80000000, copy home 0x47cf40000000, direct level 0x47d000000000, copy level 0x47d0c0000000
- factor effect within the cell: on the direct route 0.0008 [0.0008, 0.0008] ms, on the copy route -0.0001 [-0.0002, 0.0000] ms; change relative to the copy call at home: +1.7 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 134.4 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2722 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4eb8c0000000, copy home 0x4eb9c0000000, direct level 0x4eba80000000, copy level 0x4ebb40000000
- factor effect within the cell: on the direct route 0.3644 [0.3628, 0.3653] ms, on the copy route 0.0223 [0.0220, 0.0225] ms; change relative to the copy call at home: +557.6 %
- per repetition: direct home 8.382e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.7 SMMU translation requests; direct level 1.341e+08 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=four,vary=scope,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2722 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5a3540000000, copy home 0x5a3640000000, direct level 0x5a3700000000, copy level 0x5a37c0000000
- factor effect within the cell: on the direct route 0.0222 [0.0222, 0.0222] ms, on the copy route 0.0247 [0.0244, 0.0250] ms; change relative to the copy call at home: -4.3 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 134.4 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 135.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=sys,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2722 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x55e600000000, copy home 0x55e700000000, direct level 0x55e7c0000000, copy level 0x55e880000000
- factor effect within the cell: on the direct route 0.0250 [0.0250, 0.0250] ms, on the copy route 0.0028 [0.0027, 0.0030] ms; change relative to the copy call at home: +41.4 %
- per repetition: direct home 8.382e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.7 SMMU translation requests; direct level 1.676e+07 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=sys,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=four,vary=scope,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2722 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x43e740000000, copy home 0x43e840000000, direct level 0x43e900000000, copy level 0x43e9c0000000
- factor effect within the cell: on the direct route 0.0022 [0.0022, 0.0022] ms, on the copy route 0.0013 [0.0010, 0.0016] ms; change relative to the copy call at home: +1.9 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 134.1 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=sys,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2722 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x415240000000, copy home 0x415340000000, direct level 0x415400000000, copy level 0x4154c0000000
- factor effect within the cell: on the direct route 0.0742 [0.0742, 0.0743] ms, on the copy route 0.0046 [0.0045, 0.0051] ms; change relative to the copy call at home: +127.0 %
- per repetition: direct home 8.382e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.7 SMMU translation requests; direct level 3.352e+07 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=sys,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=four,vary=scope,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2722 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5d9080000000, copy home 0x5d9180000000, direct level 0x5d9240000000, copy level 0x5d9300000000
- factor effect within the cell: on the direct route 0.0051 [0.0051, 0.0051] ms, on the copy route 0.0081 [0.0079, 0.0087] ms; change relative to the copy call at home: -5.9 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 134.4 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=sys,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2722 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x58c880000000, copy home 0x58c9c0000000, direct level 0x58ca80000000, copy level 0x58cb40000000
- factor effect within the cell: on the direct route 1.5250 [1.5182, 1.5301] ms, on the copy route 0.0873 [0.0867, 0.0876] ms; change relative to the copy call at home: +1702.8 %
- per repetition: direct home 8.382e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.7 SMMU translation requests; direct level 5.363e+08 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=sys,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=four,vary=scope,working-set-mib=8

- seed 73; every round ran in the drawn order: yes; floor 0.2722 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5f6880000000, copy home 0x5f69c0000000, direct level 0x5f6a80000000, copy level 0x5f6b40000000
- factor effect within the cell: on the direct route 0.0892 [0.0891, 0.0893] ms, on the copy route 0.0848 [0.0845, 0.0853] ms; change relative to the copy call at home: +5.3 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 135.1 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 137.3 SMMU translation requests; multiplexed rows voided: 0

