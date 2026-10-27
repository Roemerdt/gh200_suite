# Factor cells: the direct route at a level of one factor against its home level, recomputed from raw rows

Times are per pass in ms. The factor effect on direct access is level minus home within a repeat, as median with its 95 % rank interval; a positive value means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | level | home ms | level ms | effect ms [interval] | relative to home | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=k,working-set-mib=32 | k | 1 | 1.5016 | 0.1005 | -1.4011 [-1.4015, -1.4004] | -93.3 % | 10 | yes | pass |
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0379 | 0.3750 | 0.3371 [0.3367, 0.3373] | +889.0 % | 10 | yes | pass |
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=k,working-set-mib=32 | k | 1 | 0.0975 | 0.0174 | -0.0800 [-0.0801, -0.0800] | -82.1 % | 10 | yes | pass |
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0160 | 0.0301 | 0.0141 [0.0141, 0.0142] | +88.5 % | 10 | yes | pass |
| at=1,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sweeps | sweeps | 1 | 26.2826 | 3.2641 | -23.0188 [-23.0486, -23.0035] | -87.6 % | 10 | yes | pass |
| at=1,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sweeps | sweeps | 1 | 3.2671 | 0.3974 | -2.8697 [-2.8761, -2.8635] | -87.8 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 45.6076 | 2.7511 | -42.8565 [-42.8786, -42.8443] | -94.0 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 5.5612 | 0.2992 | -5.2620 [-5.2911, -5.2470] | -94.6 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 67.9456 | 2.7446 | -65.1995 [-65.2449, -65.1738] | -96.0 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 9.4105 | 0.2992 | -9.1112 [-9.2591, -9.0753] | -96.8 % | 40 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 0.7339 | 2.9116 | 2.1777 [2.1768, 2.1785] | +296.7 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 0.0785 | 0.2972 | 0.2187 [0.2187, 0.2187] | +278.5 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 90.0948 | 2.7494 | -87.3434 [-87.3735, -87.3296] | -96.9 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 15.3672 | 0.3003 | -15.0669 [-15.1847, -14.8874] | -98.0 % | 90 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 11.6696 | 2.8189 | -8.8505 [-8.8521, -8.8485] | -75.8 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 1.1746 | 0.2966 | -0.8780 [-0.8789, -0.8775] | -74.7 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 23.1761 | 2.7451 | -20.4318 [-20.4386, -20.4248] | -88.2 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 2.3383 | 0.2988 | -2.0395 [-2.0403, -2.0378] | -87.2 % | 10 | yes | pass |
| at=1024,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=working-set,working-set-mib=32 | working-set | 1024 | 1.4836 | 47.2551 | 45.7718 [45.7606, 45.8098] | +3085.2 % | 10 | yes | pass |
| at=1024,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=working-set,working-set-mib=32 | working-set | 1024 | 0.0944 | 5.1626 | 5.0682 [5.0649, 5.0697] | +5369.5 % | 10 | yes | pass |
| at=1024,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint | footprint | 1024 | 0.0791 | 0.8165 | 0.7373 [0.7369, 0.7382] | +931.5 % | 10 | yes | pass |
| at=1024,footprint-mib=16384,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 483.2074 | 28.3551 | -454.8658 [-454.9229, -454.7788] | -94.1 % | 10 | yes | pass |
| at=1024,footprint-mib=16384,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 32.0763 | 1.2736 | -30.8033 [-30.8168, -30.7872] | -96.0 % | 10 | yes | pass |
| at=1024,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 433.3497 | 5.3467 | -428.0029 [-428.0713, -427.8887] | -98.8 % | 10 | yes | pass |
| at=1024,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 424.8581 | 0.4665 | -424.3917 [-424.4842, -424.2416] | -99.9 % | 10 | yes | pass |
| at=1024,footprint-mib=24576,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 752.1856 | 28.4766 | -723.7277 [-723.8071, -723.5808] | -96.2 % | 10 | yes | pass |
| at=1024,footprint-mib=24576,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 597.3555 | 5.3473 | -592.0079 [-592.1014, -591.8914] | -99.1 % | 10 | yes | pass |
| at=1024,footprint-mib=24576,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 589.9977 | 0.4665 | -589.5313 [-589.6538, -589.4218] | -99.9 % | 10 | yes | pass |
| at=1024,footprint-mib=256,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 7.3471 | 30.7466 | 23.3975 [23.3810, 23.4337] | +318.5 % | 10 | yes | pass |
| at=1024,footprint-mib=256,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 0.2108 | 1.2709 | 1.0600 [1.0591, 1.0622] | +502.7 % | 10 | yes | pass |
| at=1024,footprint-mib=256,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 5.3520 | 5.3712 | 0.0190 [0.0187, 0.0197] | +0.4 % | 10 | yes | pass |
| at=1024,footprint-mib=256,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 0.4268 | 0.4649 | 0.0382 [0.0379, 0.0383] | +8.9 % | 10 | yes | pass |
| at=1024,footprint-mib=256,kernel=k6,placement=cpu,type=factor,update=atomic,vary=footprint | footprint | 1024 | 1.5043 | 6.0194 | 4.5146 [4.5071, 4.5174] | +300.1 % | 10 | yes | pass |
| at=1024,footprint-mib=256,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint | footprint | 1024 | 0.2053 | 0.8155 | 0.6103 [0.6099, 0.6107] | +297.2 % | 10 | yes | pass |
| at=1024,footprint-mib=32768,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 971.3735 | 28.3277 | -943.0545 [-943.1093, -942.9616] | -97.1 % | 10 | yes | pass |
| at=1024,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 684.9772 | 5.3463 | -679.6310 [-679.7477, -679.5563] | -99.2 % | 10 | yes | pass |
| at=1024,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 679.4714 | 0.4669 | -679.0046 [-679.1152, -678.9453] | -99.9 % | 10 | yes | pass |
| at=1024,footprint-mib=4096,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 123.5831 | 28.5049 | -95.0820 [-95.1223, -95.0493] | -76.9 % | 10 | yes | pass |
| at=1024,footprint-mib=4096,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 7.0540 | 1.2721 | -5.7817 [-5.7850, -5.7796] | -82.0 % | 10 | yes | pass |
| at=1024,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 5.4947 | 5.3519 | -0.1432 [-0.1613, -0.1361] | -2.6 % | 50 | yes | pass |
| at=1024,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 5.0999 | 0.4652 | -4.6347 [-4.6382, -4.6302] | -90.9 % | 10 | yes | pass |
| at=1024,footprint-mib=4096,kernel=k6,placement=cpu,type=factor,update=atomic,vary=footprint | footprint | 1024 | 24.1188 | 5.8295 | -18.2896 [-18.3013, -18.2546] | -75.8 % | 10 | yes | pass |
| at=1024,footprint-mib=4096,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint | footprint | 1024 | 3.2774 | 0.8168 | -2.4605 [-2.4641, -2.4591] | -75.1 % | 10 | yes | pass |
| at=1024,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=factor,vary=keys | keys | 1024 | 191.3094 | 12.4941 | -178.8164 [-178.8223, -178.8142] | -93.5 % | 10 | yes | pass |
| at=1024,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=factor,vary=keys | keys | 1024 | 12.2937 | 0.7660 | -11.5277 [-11.5282, -11.5272] | -93.8 % | 10 | yes | pass |
| at=1024,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,type=factor,vary=keys | keys | 1024 | 8.5773 | 12.4792 | 3.9019 [3.8960, 3.9066] | +45.5 % | 10 | yes | pass |
| at=1024,footprint-mib=8,kernel=k6,keys=1048576,placement=hbm,type=factor,vary=keys | keys | 1024 | 0.1786 | 0.7657 | 0.5871 [0.5869, 0.5872] | +328.6 % | 10 | yes | pass |
| at=1024,footprint-mib=8192,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 248.7896 | 28.6014 | -220.1945 [-220.2228, -220.1558] | -88.5 % | 10 | yes | pass |
| at=1024,footprint-mib=8192,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 15.0612 | 1.2713 | -13.7880 [-13.7959, -13.7830] | -91.5 % | 10 | yes | pass |
| at=1024,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 7.7831 | 5.3516 | -2.4311 [-2.4336, -2.4298] | -31.2 % | 10 | yes | pass |
| at=1024,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 7.7181 | 0.4671 | -7.2511 [-7.2572, -7.2394] | -93.9 % | 10 | yes | pass |
| at=16,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sweeps | sweeps | 16 | 26.7594 | 46.5589 | 19.7954 [19.7912, 19.8191] | +74.0 % | 10 | yes | pass |
| at=16,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sweeps | sweeps | 16 | 3.2404 | 6.5158 | 3.2754 [3.2643, 3.2838] | +101.1 % | 10 | yes | pass |
| at=1of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 1of10 | 2.9109 | 0.3018 | -2.6091 [-2.6096, -2.6088] | -89.6 % | 10 | yes | pass |
| at=1of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 1of10 | 0.2963 | 0.0378 | -0.2585 [-0.2585, -0.2584] | -87.2 % | 10 | yes | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 1of100 | 2.9118 | 0.0382 | -2.8737 [-2.8743, -2.8730] | -98.7 % | 10 | yes | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 1of100 | 0.2966 | 0.0101 | -0.2866 [-0.2866, -0.2864] | -96.6 % | 10 | yes | pass |
| at=1of1000,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 1of1000 | 2.9165 | 0.0158 | -2.9006 [-2.9010, -2.9001] | -99.5 % | 10 | yes | pass |
| at=1of1000,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 1of1000 | 0.2975 | 0.0079 | -0.2896 [-0.2896, -0.2895] | -97.3 % | 10 | yes | pass |
| at=1of2,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 1of2 | 2.9089 | 1.4668 | -1.4420 [-1.4432, -1.4414] | -49.6 % | 10 | yes | pass |
| at=1of2,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 1of2 | 0.2981 | 0.1601 | -0.1380 [-0.1382, -0.1379] | -46.3 % | 10 | yes | pass |
| at=2,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=k,working-set-mib=32 | k | 2 | 1.4909 | 0.1938 | -1.2971 [-1.2982, -1.2968] | -87.0 % | 10 | yes | pass |
| at=2,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=k,working-set-mib=32 | k | 2 | 0.0990 | 0.0235 | -0.0755 [-0.0756, -0.0752] | -76.3 % | 10 | yes | pass |
| at=2,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sweeps | sweeps | 2 | 26.6586 | 6.1366 | -20.5226 [-20.5419, -20.4989] | -77.0 % | 10 | yes | pass |
| at=2,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sweeps | sweeps | 2 | 3.2285 | 0.8144 | -2.4140 [-2.4226, -2.4097] | -74.8 % | 10 | yes | pass |
| at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=partition | partition | 2g | 433.5351 | 5.6956 | -427.8352 [-427.9556, -427.7497] | -98.7 % | 10 | yes | pass |
| at=2m,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=page-order | page-order | 2m | 5.3809 | 5.3147 | -0.0661 [-0.0670, -0.0645] | -1.2 % | 10 | yes | pass |
| at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 432.8905 | 5.3791 | -427.5115 [-427.6565, -427.3509] | -98.8 % | 10 | yes | pass |
| at=2m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 425.3538 | 2.4962 | -422.8536 [-422.9059, -422.5430] | -99.4 % | 10 | yes | pass |
| at=2m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 685.0154 | 5.4265 | -679.5933 [-679.7354, -679.4770] | -99.2 % | 10 | yes | pass |
| at=2m,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 678.6251 | 4.1790 | -674.4450 [-674.4952, -674.3097] | -99.4 % | 10 | yes | pass |
| at=2m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 5.5789 | 5.3503 | -0.2282 [-0.2389, -0.2204] | -4.1 % | 10 | yes | pass |
| at=2m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 5.1076 | 0.4274 | -4.6802 [-4.6842, -4.6753] | -91.6 % | 10 | yes | pass |
| at=2m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 7.8877 | 5.3603 | -2.5272 [-2.5287, -2.5254] | -32.0 % | 10 | yes | pass |
| at=2m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 7.8037 | 0.4750 | -7.3285 [-7.3348, -7.3258] | -93.9 % | 10 | yes | pass |
| at=3of4,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 3of4 | 2.9200 | 2.2067 | -0.7134 [-0.7137, -0.7108] | -24.4 % | 10 | yes | pass |
| at=3of4,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 3of4 | 0.2975 | 0.2338 | -0.0637 [-0.0638, -0.0636] | -21.4 % | 10 | yes | pass |
| at=4,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=k,working-set-mib=32 | k | 4 | 1.4974 | 0.3804 | -1.1170 [-1.1178, -1.1160] | -74.6 % | 10 | yes | pass |
| at=4,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=k,working-set-mib=32 | k | 4 | 0.0963 | 0.0348 | -0.0614 [-0.0615, -0.0614] | -63.8 % | 10 | yes | pass |
| at=4,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=repeat | repeat | 4 | 6.0367 | 18.0833 | 12.0423 [12.0377, 12.0522] | +199.5 % | 10 | yes | pass |
| at=4,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=repeat | repeat | 4 | 0.8177 | 1.6394 | 0.8217 [0.8185, 0.8225] | +100.5 % | 10 | yes | pass |
| at=4,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sweeps | sweeps | 4 | 26.6114 | 11.8732 | -14.7397 [-14.7834, -14.6926] | -55.4 % | 10 | yes | pass |
| at=4,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sweeps | sweeps | 4 | 3.2684 | 1.6207 | -1.6482 [-1.6511, -1.6426] | -50.4 % | 10 | yes | pass |
| at=512m,footprint-mib=1024,kernel=k3,placement=cpu,type=factor,vary=page-size | page-size | 512m | 5.3722 | 5.3302 | -0.0423 [-0.0427, -0.0408] | -0.8 % | 10 | yes | pass |
| at=512m,footprint-mib=1024,kernel=k3,placement=hbm,type=factor,vary=page-size | page-size | 512m | 0.4651 | 0.4644 | -0.0007 [-0.0007, -0.0006] | -0.1 % | 100 | yes | pass |
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-size | page-size | 512m | 432.7710 | 5.3852 | -427.3855 [-427.4406, -427.1681] | -98.8 % | 10 | yes | pass |
| at=512m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-size | page-size | 512m | 424.8261 | 0.4782 | -424.3478 [-424.4478, -424.1960] | -99.9 % | 10 | yes | pass |
| at=512m,footprint-mib=16384,kernel=k3p,placement=cpu,type=factor,vary=page-size | page-size | 512m | 7.0112 | 0.0998 | -6.9114 [-6.9161, -6.9056] | -98.6 % | 10 | yes | pass |
| at=512m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-size | page-size | 512m | 684.8646 | 5.3919 | -679.4725 [-679.6405, -679.3682] | -99.2 % | 10 | yes | pass |
| at=512m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-size | page-size | 512m | 5.5799 | 5.3704 | -0.2092 [-0.2311, -0.1897] | -3.7 % | 10 | yes | pass |
| at=512m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-size | page-size | 512m | 5.1201 | 0.4756 | -4.6443 [-4.6494, -4.6401] | -90.7 % | 10 | yes | pass |
| at=512m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-size | page-size | 512m | 7.7412 | 5.3787 | -2.3627 [-2.3645, -2.3603] | -30.5 % | 10 | yes | pass |
| at=512m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-size | page-size | 512m | 7.6815 | 0.4771 | -7.2043 [-7.2087, -7.2016] | -93.8 % | 10 | yes | pass |
| at=64,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=k,working-set-mib=32 | k | 64 | 1.4872 | 5.9479 | 4.4609 [4.4553, 4.4621] | +300.0 % | 10 | yes | pass |
| at=64,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=k,working-set-mib=32 | k | 64 | 0.0975 | 0.3587 | 0.2613 [0.2609, 0.2625] | +268.1 % | 10 | yes | pass |
| at=64,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sweeps | sweeps | 64 | 26.9761 | 184.0233 | 157.0334 [157.0094, 157.0960] | +582.1 % | 10 | yes | pass |
| at=64,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sweeps | sweeps | 64 | 3.2501 | 26.1417 | 22.8926 [22.8561, 22.9137] | +704.4 % | 10 | yes | pass |
| at=64k,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=page-order | page-order | 64k | 5.3798 | 5.1784 | -0.2014 [-0.2023, -0.1999] | -3.7 % | 10 | yes | pass |
| at=64k,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 432.9823 | 5.2120 | -427.7690 [-427.8685, -427.5920] | -98.8 % | 10 | yes | pass |
| at=64k,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 425.0561 | 1.6135 | -423.4422 [-423.5142, -423.3239] | -99.6 % | 10 | yes | pass |
| at=64k,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 683.9654 | 5.2677 | -678.6974 [-678.7970, -678.5576] | -99.2 % | 10 | yes | pass |
| at=64k,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 679.6291 | 3.3277 | -676.2983 [-676.4017, -676.2038] | -99.5 % | 10 | yes | pass |
| at=64k,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 5.4694 | 5.1428 | -0.3283 [-0.3590, -0.3040] | -6.0 % | 10 | yes | pass |
| at=64k,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 5.0987 | 0.4105 | -4.6881 [-4.6946, -4.6835] | -91.9 % | 10 | yes | pass |
| at=64k,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 7.8885 | 5.1730 | -2.7167 [-2.7188, -2.7140] | -34.4 % | 10 | yes | pass |
| at=64k,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 7.8126 | 0.4446 | -7.3680 [-7.3762, -7.3661] | -94.3 % | 10 | yes | pass |
| at=8,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=working-set,working-set-mib=32 | working-set | 8 | 1.4817 | 0.0377 | -1.4440 [-1.4445, -1.4438] | -97.5 % | 10 | yes | pass |
| at=8,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=working-set,working-set-mib=32 | working-set | 8 | 0.0974 | 0.0162 | -0.0812 [-0.0813, -0.0811] | -83.4 % | 10 | yes | pass |
| at=9of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 9of10 | 2.9094 | 2.6507 | -0.2589 [-0.2599, -0.2580] | -8.9 % | 10 | yes | pass |
| at=9of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 9of10 | 0.2985 | 0.2764 | -0.0221 [-0.0222, -0.0220] | -7.4 % | 10 | yes | pass |
| at=hbm,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=placement | placement | hbm | 9.9581 | 9.9576 | -0.0005 [-0.0026, 0.0027] | -0.0 % | 100 | no | pass |
| at=hbm,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=plain,vary=placement | placement | hbm | 2.2788 | 2.2685 | -0.0045 [-0.0091, -0.0005] | -0.2 % | 100 | yes | pass |
| at=hbm,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=placement | placement | hbm | 12.7759 | 17.7638 | 4.9018 [4.6509, 4.9765] | +38.4 % | 60 | yes | pass |
| at=hbm,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=plain,vary=placement | placement | hbm | 2.3430 | 2.7301 | 0.3901 [0.3711, 0.4097] | +16.7 % | 10 | yes | pass |
| at=line,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=layout | layout | line | 6.0429 | 3.5451 | -2.4967 [-2.5102, -2.4902] | -41.3 % | 10 | yes | pass |
| at=line,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=layout | layout | line | 0.8148 | 0.3392 | -0.4754 [-0.4766, -0.4747] | -58.4 % | 10 | yes | pass |
| at=none,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=tiling | tiling | none | 26.6305 | 37.7010 | 11.0697 [10.9725, 11.1961] | +41.6 % | 10 | yes | pass |
| at=none,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=tiling | tiling | none | 3.2568 | 2.7482 | -0.5077 [-0.5228, -0.5034] | -15.6 % | 10 | yes | pass |
| at=off512m,footprint-mib=1024,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3306 | 5.3297 | -0.0007 [-0.0009, -0.0006] | -0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=1024,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4648 | 0.4648 | 0.0000 [0.0000, 0.0001] | +0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=1024,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3701 | 5.3709 | 0.0008 [0.0006, 0.0009] | +0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=1024,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4655 | 0.4652 | -0.0003 [-0.0003, -0.0002] | -0.1 % | 100 | yes | pass |
| at=off512m,footprint-mib=11520,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3785 | 5.3781 | -0.0004 [-0.0006, -0.0002] | -0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=11520,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 240.5095 | 240.3306 | -0.1679 [-0.1968, -0.1366] | -0.1 % | 100 | yes | pass |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3791 | 5.3788 | -0.0004 [-0.0005, -0.0002] | -0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4778 | 0.4774 | -0.0004 [-0.0005, -0.0004] | -0.1 % | 100 | yes | pass |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 279.2966 | 279.3463 | 0.0630 [0.0340, 0.0926] | +0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | alignment | off512m | 254.4431 | 281.2439 | 26.7481 [26.6360, 26.9692] | +10.5 % | 10 | yes | pass |
| at=off512m,footprint-mib=1536,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3476 | 5.3479 | 0.0004 [0.0002, 0.0006] | +0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=1536,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3707 | 5.3695 | -0.0012 [-0.0014, -0.0010] | -0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3809 | 5.3809 | 0.0001 [-0.0001, 0.0002] | +0.0 % | 100 | no | pass |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4782 | 0.4776 | -0.0006 [-0.0006, -0.0005] | -0.1 % | 80 | yes | pass |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 432.9250 | 432.8409 | -0.0637 [-0.0909, -0.0332] | -0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | alignment | off512m | 425.4888 | 424.9894 | -0.4917 [-0.5326, -0.4382] | -0.1 % | 70 | yes | pass |
| at=off512m,footprint-mib=2048,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3572 | 5.3568 | -0.0004 [-0.0006, -0.0002] | -0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=2048,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3726 | 5.3696 | -0.0030 [-0.0032, -0.0027] | -0.1 % | 30 | yes | pass |
| at=off512m,footprint-mib=24576,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3806 | 5.3810 | 0.0003 [0.0001, 0.0004] | +0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=24576,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 598.4352 | 598.4451 | 0.0171 [-0.0311, 0.0692] | +0.0 % | 100 | no | pass |
| at=off512m,footprint-mib=256,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.1754 | 5.1757 | 0.0003 [0.0001, 0.0004] | +0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=256,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4242 | 0.4240 | -0.0002 [-0.0002, -0.0002] | -0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=256,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3460 | 5.3557 | 0.0096 [0.0091, 0.0101] | +0.2 % | 10 | yes | pass |
| at=off512m,footprint-mib=256,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4251 | 0.4255 | 0.0005 [0.0004, 0.0005] | +0.1 % | 100 | yes | pass |
| at=off512m,footprint-mib=32768,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3818 | 5.3819 | 0.0001 [-0.0001, 0.0003] | +0.0 % | 100 | no | pass |
| at=off512m,footprint-mib=32768,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 683.9941 | 684.0725 | 0.0983 [0.0682, 0.1216] | +0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3694 | 5.3698 | 0.0003 [0.0002, 0.0004] | +0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4754 | 0.4755 | 0.0001 [0.0001, 0.0002] | +0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.5731 | 5.5575 | -0.0171 [-0.0255, -0.0106] | -0.3 % | 100 | yes | pass |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | alignment | off512m | 5.1229 | 5.1128 | -0.0100 [-0.0112, -0.0087] | -0.2 % | 100 | yes | pass |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3767 | 5.3759 | -0.0006 [-0.0008, -0.0005] | -0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4770 | 0.4769 | -0.0001 [-0.0002, -0.0001] | -0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 7.8869 | 48.5842 | 40.6965 [40.6404, 40.7215] | +516.0 % | 10 | yes | pass |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | alignment | off512m | 7.8220 | 43.2729 | 35.4493 [35.3653, 35.4838] | +453.2 % | 10 | yes | pass |
| at=off512m,footprint-mib=9728,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3772 | 5.3782 | 0.0010 [0.0008, 0.0012] | +0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=9728,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 128.2567 | 128.2883 | 0.0374 [0.0116, 0.0686] | +0.0 % | 100 | yes | pass |
| at=plain,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | plain | 9.9414 | 2.3716 | -7.5687 [-7.5791, -7.5580] | -76.1 % | 10 | yes | pass |
| at=plain,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | plain | 9.9612 | 2.3758 | -7.5840 [-7.6021, -7.5785] | -76.1 % | 10 | yes | pass |
| at=plain,footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | plain | 10.2810 | 2.4247 | -7.8672 [-7.8779, -7.8502] | -76.5 % | 10 | yes | pass |
| at=plain,footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | plain | 10.2057 | 2.3815 | -7.8210 [-7.8424, -7.8033] | -76.6 % | 10 | yes | pass |
| at=plain,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | plain | 6.0151 | 6.0118 | -0.0030 [-0.0045, -0.0018] | -0.0 % | 100 | yes | pass |
| at=plain,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | plain | 0.8161 | 0.7684 | -0.0477 [-0.0484, -0.0472] | -5.8 % | 10 | yes | pass |
| at=plain,footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | plain | 10.5873 | 2.3234 | -8.2630 [-8.3161, -8.1770] | -78.0 % | 10 | yes | pass |
| at=plain,footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | plain | 10.7831 | 2.4679 | -8.3230 [-8.4030, -8.2608] | -77.2 % | 10 | yes | pass |
| at=plain,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | plain | 0.0758 | 0.0791 | 0.0032 [0.0032, 0.0033] | +4.3 % | 10 | yes | pass |
| at=plain,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | plain | 12.5767 | 2.3458 | -10.2372 [-10.2656, -10.1150] | -81.4 % | 10 | yes | pass |
| at=plain,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | plain | 17.7165 | 2.7346 | -14.9886 [-15.0418, -14.9058] | -84.6 % | 10 | yes | pass |
| at=returned,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | returned | 10.1464 | 39.7166 | 29.5391 [28.1928, 33.1263] | +291.1 % | 100 | yes | pass |
| at=returned,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | returned | 10.1828 | 42.8570 | 32.6699 [32.4442, 32.8985] | +320.8 % | 50 | yes | pass |
| at=returned,footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | returned | 10.2567 | 40.6359 | 30.3804 [29.8965, 30.6783] | +296.2 % | 80 | yes | pass |
| at=returned,footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | returned | 10.2563 | 41.3700 | 31.1223 [29.7317, 31.2679] | +303.4 % | 100 | yes | pass |
| at=returned,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | returned | 6.0510 | 6.0585 | 0.0082 [0.0066, 0.0094] | +0.1 % | 100 | yes | pass |
| at=returned,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | returned | 0.8173 | 0.8974 | 0.0803 [0.0796, 0.0815] | +9.8 % | 10 | yes | pass |
| at=returned,footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | returned | 10.6496 | 41.6360 | 30.9834 [30.7029, 31.1341] | +290.9 % | 40 | yes | pass |
| at=returned,footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | returned | 10.6314 | 42.0618 | 31.3907 [30.6926, 32.0844] | +295.3 % | 100 | yes | pass |
| at=returned,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | returned | 0.0769 | 0.1291 | 0.0522 [0.0521, 0.0522] | +67.8 % | 10 | yes | pass |
| at=returned,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | returned | 12.9600 | 44.7770 | 31.7949 [31.4391, 32.1096] | +245.3 % | 40 | yes | pass |
| at=returned,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | returned | 17.5515 | 47.5575 | 29.9526 [26.9673, 30.8460] | +170.7 % | 100 | yes | pass |
| at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=generator | generator | rmat | 30.6829 | 188.7934 | 158.1047 [158.0427, 158.1805] | +515.3 % | 10 | yes | pass |
| at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=generator | generator | rmat | 1.2721 | 65.4615 | 64.1887 [63.6643, 64.7241] | +5045.8 % | 10 | yes | pass |
| at=rmat,footprint-mib=8192,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=generator | generator | rmat | 247.3702 | 986.7168 | 739.3316 [739.2552, 739.6090] | +298.9 % | 10 | yes | pass |
| at=rmat,footprint-mib=8192,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=generator | generator | rmat | 15.1374 | 395.4900 | 380.3439 [377.9015, 382.9981] | +2512.6 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing | sharing | shared | 0.0201 | 0.0212 | 0.0012 [0.0010, 0.0012] | +5.9 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0203 | 0.0210 | 0.0007 [0.0006, 0.0007] | +3.4 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0201 | 0.0203 | 0.0002 [0.0002, 0.0003] | +1.1 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing | sharing | shared | 0.0202 | 0.0210 | 0.0007 [0.0006, 0.0008] | +3.6 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0201 | 0.0209 | 0.0008 [0.0008, 0.0009] | +4.2 % | 30 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0201 | 0.0201 | -0.0000 [-0.0001, 0.0000] | -0.0 % | 100 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing | sharing | shared | 0.1930 | 0.1932 | 0.0002 [0.0001, 0.0003] | +0.1 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 0.1927 | 0.3790 | 0.1865 [0.1858, 0.1868] | +96.8 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing | sharing | shared | 0.1916 | 0.1922 | 0.0006 [0.0005, 0.0007] | +0.3 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0375 | 0.1553 | 0.1176 [0.1173, 0.1185] | +313.1 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0348 | 0.1815 | 0.1467 [0.1463, 0.1470] | +421.3 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0374 | 0.0364 | -0.0010 [-0.0011, -0.0009] | -2.6 % | 40 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing | sharing | shared | 0.1926 | 0.1931 | 0.0005 [0.0004, 0.0006] | +0.3 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 0.1927 | 0.3833 | 0.1906 [0.1902, 0.1910] | +98.9 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing | sharing | shared | 0.1928 | 0.1928 | -0.0000 [-0.0001, 0.0001] | -0.0 % | 100 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0374 | 0.1624 | 0.1250 [0.1244, 0.1263] | +334.5 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0348 | 0.1849 | 0.1501 [0.1496, 0.1506] | +431.6 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0373 | 0.0361 | -0.0013 [-0.0015, -0.0012] | -3.4 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0152 | 0.0598 | 0.0446 [0.0445, 0.0447] | +293.7 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0149 | 0.0582 | 0.0432 [0.0429, 0.0435] | +289.8 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0152 | 0.0156 | 0.0004 [0.0004, 0.0005] | +2.8 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0150 | 0.0594 | 0.0443 [0.0442, 0.0445] | +295.6 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0155 | 0.0544 | 0.0389 [0.0385, 0.0393] | +251.0 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0157 | 0.0160 | 0.0003 [0.0002, 0.0004] | +2.1 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0556 | 0.2208 | 0.1649 [0.1638, 0.1665] | +296.6 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0498 | 0.2629 | 0.2132 [0.2126, 0.2135] | +428.1 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0495 | 0.0491 | -0.0003 [-0.0004, -0.0002] | -0.6 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0548 | 0.2350 | 0.1801 [0.1792, 0.1805] | +328.5 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0483 | 0.2649 | 0.2165 [0.2161, 0.2169] | +447.9 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0493 | 0.0489 | -0.0004 [-0.0005, -0.0003] | -0.8 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=factor,vary=sharing | sharing | shared | 30.7630 | 30.4972 | -0.2788 [-0.2956, -0.2497] | -0.9 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=factor,vary=sharing | sharing | shared | 1.2770 | 1.2772 | 0.0003 [-0.0004, 0.0011] | +0.0 % | 100 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0445 | 0.0625 | 0.0180 [0.0177, 0.0184] | +40.4 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0453 | 0.0646 | 0.0193 [0.0190, 0.0199] | +42.7 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0445 | 0.0446 | 0.0000 [-0.0001, 0.0001] | +0.0 % | 100 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0457 | 0.0649 | 0.0191 [0.0186, 0.0196] | +41.7 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0449 | 0.0656 | 0.0207 [0.0204, 0.0210] | +46.2 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0441 | 0.0441 | -0.0000 [-0.0001, 0.0000] | -0.1 % | 100 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32 | sharing | shared | 1.4892 | 1.5008 | 0.0117 [0.0109, 0.0120] | +0.8 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8 | sharing | shared | 0.0439 | 0.0440 | 0.0001 [0.0001, 0.0001] | +0.2 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 1.5065 | 1.5117 | 0.0053 [0.0050, 0.0057] | +0.3 % | 30 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0511 | 0.0518 | 0.0008 [0.0007, 0.0009] | +1.6 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 1.5060 | 1.5140 | 0.0078 [0.0075, 0.0085] | +0.5 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8 | sharing | shared | 0.0532 | 0.0539 | 0.0008 [0.0007, 0.0010] | +1.5 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32 | sharing | shared | 0.1053 | 0.1091 | 0.0039 [0.0034, 0.0042] | +3.7 % | 80 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.1167 | 0.1162 | -0.0005 [-0.0007, -0.0003] | -0.4 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.1286 | 0.1309 | 0.0021 [0.0019, 0.0024] | +1.6 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32 | sharing | shared | 1.5119 | 1.4980 | -0.0141 [-0.0153, -0.0128] | -0.9 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8 | sharing | shared | 0.0444 | 0.0443 | -0.0000 [-0.0001, 0.0000] | -0.1 % | 100 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 1.5090 | 1.4994 | -0.0089 [-0.0103, -0.0085] | -0.6 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0513 | 0.0512 | -0.0002 [-0.0003, 0.0000] | -0.3 % | 100 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 1.4976 | 1.5101 | 0.0123 [0.0115, 0.0128] | +0.8 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8 | sharing | shared | 0.0504 | 0.0512 | 0.0008 [0.0006, 0.0011] | +1.5 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32 | sharing | shared | 0.1070 | 0.1061 | -0.0009 [-0.0010, -0.0009] | -0.9 % | 70 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.1155 | 0.1153 | -0.0003 [-0.0004, -0.0001] | -0.3 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.1273 | 0.1255 | -0.0017 [-0.0020, -0.0016] | -1.4 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01 | sharing | shared | 5.4333 | 5.4340 | 0.0008 [0.0004, 0.0018] | +0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1 | sharing | shared | 5.4215 | 5.4200 | -0.0013 [-0.0150, -0.0009] | -0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1 | sharing | shared | 5.3967 | 5.3945 | -0.0027 [-0.0035, -0.0018] | -0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01 | sharing | shared | 5.4196 | 5.4332 | 0.0136 [0.0123, 0.0142] | +0.3 % | 60 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1 | sharing | shared | 5.4354 | 5.4341 | -0.0016 [-0.0022, -0.0003] | -0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1 | sharing | shared | 5.4108 | 5.4073 | -0.0034 [-0.0048, -0.0018] | -0.1 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 7.2584 | 7.2197 | -0.0388 [-0.0428, -0.0350] | -0.5 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 7.2626 | 7.2489 | -0.0144 [-0.0165, -0.0121] | -0.2 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01 | sharing | shared | 433.7298 | 433.7366 | -0.0138 [-0.0343, 0.0250] | -0.0 % | 100 | no | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1 | sharing | shared | 433.5120 | 433.5122 | 0.0124 [-0.0225, 0.0610] | +0.0 % | 100 | no | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1 | sharing | shared | 433.4888 | 433.5556 | 0.0717 [0.0403, 0.1037] | +0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01 | sharing | shared | 433.5926 | 433.6354 | 0.0553 [0.0192, 0.0781] | +0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1 | sharing | shared | 433.6111 | 433.6605 | 0.0633 [0.0222, 0.0929] | +0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1 | sharing | shared | 433.5393 | 433.6132 | 0.0762 [0.0259, 0.1048] | +0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing | sharing | shared | 26.4860 | 23.3776 | -3.1205 [-3.1449, -3.0903] | -11.8 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing | sharing | shared | 3.2708 | 3.2680 | -0.0035 [-0.0046, -0.0022] | -0.1 % | 100 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | sharing | shared | 26.4726 | 23.4547 | -3.0241 [-3.0356, -3.0000] | -11.4 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | sharing | shared | 26.6193 | 23.3547 | -3.2704 [-3.2997, -3.2233] | -12.3 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | sharing | shared | 26.3832 | 23.5594 | -2.8399 [-2.8575, -2.7761] | -10.8 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | sharing | shared | 3.5666 | 3.5962 | 0.0313 [0.0280, 0.0338] | +0.9 % | 40 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | sharing | shared | 3.5507 | 3.4820 | -0.0689 [-0.0742, -0.0631] | -1.9 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | sharing | shared | 3.4770 | 3.5094 | 0.0329 [0.0303, 0.0349] | +0.9 % | 40 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | sharing | shared | 26.5308 | 23.2783 | -3.2479 [-3.2983, -3.2166] | -12.2 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | sharing | shared | 26.3312 | 23.4360 | -2.8901 [-2.9131, -2.8670] | -11.0 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | sharing | shared | 27.2346 | 23.5666 | -3.6604 [-3.6947, -3.6409] | -13.4 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | sharing | shared | 3.4680 | 3.4624 | -0.0057 [-0.0080, -0.0046] | -0.2 % | 100 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | sharing | shared | 3.4569 | 3.4599 | 0.0041 [0.0019, 0.0062] | +0.1 % | 100 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | sharing | shared | 3.5649 | 3.5192 | -0.0447 [-0.0479, -0.0397] | -1.3 % | 30 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01 | sharing | shared | 8.0834 | 8.1040 | 0.0204 [0.0190, 0.0227] | +0.3 % | 40 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1 | sharing | shared | 8.0729 | 8.0935 | 0.0208 [0.0191, 0.0227] | +0.3 % | 70 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=1 | sharing | shared | 8.0922 | 8.1015 | 0.0091 [0.0076, 0.0110] | +0.1 % | 100 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01 | sharing | shared | 8.0712 | 8.0992 | 0.0261 [0.0248, 0.0284] | +0.3 % | 80 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1 | sharing | shared | 8.0855 | 8.0950 | 0.0089 [0.0077, 0.0110] | +0.1 % | 100 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=1 | sharing | shared | 8.1057 | 8.1271 | 0.0216 [0.0188, 0.0229] | +0.3 % | 50 | yes | pass |
| at=sorted,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=index-order | index-order | sorted | 433.4533 | 5.0524 | -428.4001 [-428.5434, -428.3011] | -98.8 % | 10 | yes | pass |
| at=stadd,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | stadd | 9.9489 | 7.9686 | -1.9784 [-2.0511, -1.9677] | -19.9 % | 10 | yes | pass |
| at=stadd,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | stadd | 10.1436 | 8.0149 | -2.1288 [-2.1367, -2.1224] | -21.0 % | 10 | yes | pass |
| at=stadd,footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | stadd | 10.2952 | 7.9942 | -2.3008 [-2.3187, -2.2919] | -22.3 % | 10 | yes | pass |
| at=stadd,footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | stadd | 10.2999 | 8.1071 | -2.1934 [-2.2146, -2.1779] | -21.3 % | 10 | yes | pass |
| at=stadd,footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | stadd | 10.8318 | 8.0075 | -2.8206 [-2.9016, -2.7079] | -26.0 % | 10 | yes | pass |
| at=stadd,footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | stadd | 10.8444 | 8.0689 | -2.7782 [-2.8031, -2.7371] | -25.6 % | 10 | yes | pass |
| at=stadd,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | stadd | 12.9138 | 9.1102 | -3.8678 [-3.8960, -3.6726] | -30.0 % | 30 | yes | pass |
| at=stadd,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | stadd | 17.2694 | 11.4586 | -5.8217 [-5.8935, -5.7356] | -33.7 % | 10 | yes | pass |
| at=tiles,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=tiling,working-set-mib=8 | tiling | tiles | 0.0379 | 0.0368 | -0.0011 [-0.0011, -0.0010] | -2.8 % | 10 | yes | pass |
| at=tiles,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=tiling,working-set-mib=8 | tiling | tiles | 0.0160 | 0.0153 | -0.0007 [-0.0007, -0.0007] | -4.2 % | 10 | yes | pass |
| at=warp,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,type=factor,vary=strategy | strategy | warp | 8.2580 | 8.7600 | 0.5023 [0.4982, 0.5050] | +6.1 % | 10 | yes | pass |
| at=warp,footprint-mib=8,kernel=k6,keys=1048576,placement=hbm,type=factor,vary=strategy | strategy | warp | 0.1780 | 0.2863 | 0.1083 [0.1081, 0.1089] | +60.8 % | 10 | yes | pass |
| at=warp,footprint-mib=8,kernel=k6,keys=4096,placement=cpu,type=factor,vary=strategy | strategy | warp | 6.2118 | 6.1902 | -0.0228 [-0.0260, -0.0183] | -0.4 % | 100 | yes | pass |
| at=warp,footprint-mib=8,kernel=k6,keys=4096,placement=hbm,type=factor,vary=strategy | strategy | warp | 0.2662 | 0.2823 | 0.0160 [0.0159, 0.0161] | +6.0 % | 10 | yes | pass |
| at=warp,footprint-mib=8,kernel=k6,keys=65536,placement=cpu,type=factor,vary=strategy | strategy | warp | 4.1027 | 4.0966 | -0.0060 [-0.0065, -0.0055] | -0.1 % | 40 | yes | pass |
| at=warp,footprint-mib=8,kernel=k6,keys=65536,placement=hbm,type=factor,vary=strategy | strategy | warp | 0.1925 | 0.2862 | 0.0937 [0.0936, 0.0941] | +48.7 % | 10 | yes | pass |

## Host phases

The CPU phase before every pass, timed on the CPU clock (ms per pass), and the state check's median load latency on the preparing core after the phase (ns per sampled load), per variant.

| cell | home CPU ms | home state ns | level CPU ms | level state ns |
|---|---|---|---|---|
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing | 0.2776 | 64.1 | 0.2743 | 61.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | 0.2415 | 58.9 | 0.2435 | 62.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing | 0.2668 | 175.6 | 0.2607 | 73.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing | 0.2592 | 64.1 | 0.2545 | 62.8 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | 0.2395 | 62.8 | 0.2362 | 63.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing | 0.2445 | 191.2 | 0.2394 | 70.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing | 5.3002 | 63.1 | 5.9064 | 130.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | 2.7733 | 98.4 | 3.3382 | 108.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing | 3.9655 | 213.2 | 3.9531 | 216.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | 5.0644 | 138.6 | 5.8838 | 201.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | 2.8591 | 62.4 | 3.5184 | 99.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | 3.9553 | 464.2 | 3.8484 | 424.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing | 5.2537 | 59.4 | 5.3780 | 123.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | 2.7490 | 111.6 | 2.6658 | 162.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing | 3.4244 | 199.9 | 3.4138 | 218.6 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | 4.9609 | 225.1 | 5.1851 | 329.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | 2.8721 | 142.0 | 2.9273 | 200.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | 3.2305 | 464.0 | 3.2288 | 421.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | 1.1897 | 71.2 | 1.2649 | 82.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | 0.9225 | 74.0 | 1.0152 | 75.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | 1.0234 | 372.4 | 1.0268 | 414.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | 1.1778 | 70.0 | 1.1953 | 78.8 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | 0.9042 | 69.9 | 0.9308 | 72.6 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | 0.9631 | 382.5 | 0.9726 | 383.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | 7.3530 | 152.9 | 8.1820 | 250.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | 4.0805 | 342.9 | 5.1634 | 344.8 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | 5.5643 | 485.1 | 5.4952 | 459.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | 7.1763 | 67.4 | 7.3911 | 121.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | 3.9726 | 281.5 | 4.0241 | 270.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | 4.5430 | 489.6 | 4.6342 | 528.1 |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=factor,vary=sharing | 1.8520 | - | 1.6475 | - |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=factor,vary=sharing | 2.3395 | - | 3.6951 | - |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8 | 0.9281 | 71.9 | 0.9260 | 78.2 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8 | 0.6613 | 67.9 | 0.6537 | 77.1 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8 | 0.7141 | 197.1 | 0.7144 | 198.4 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8 | 0.8711 | 69.4 | 0.8644 | 82.0 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8 | 0.5339 | 67.4 | 0.5334 | 70.2 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8 | 0.6306 | 196.9 | 0.6297 | 195.5 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32 | 0.5798 | 75.4 | 0.5892 | 133.0 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8 | 0.5838 | 73.9 | 0.5879 | 118.9 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32 | 4.2337 | 123.5 | 4.2504 | 179.4 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8 | 4.0729 | 111.8 | 4.0697 | 176.8 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32 | 27.6903 | 261.2 | 28.4753 | 275.1 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8 | 27.9240 | 254.1 | 27.9159 | 263.8 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32 | 0.9723 | 73.2 | 0.9766 | 108.0 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32 | 5.1915 | 328.1 | 5.1818 | 368.6 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32 | 32.5416 | 535.2 | 32.7444 | 579.5 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32 | 0.5460 | 67.9 | 0.5576 | 98.5 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8 | 0.5474 | 73.8 | 0.5478 | 115.2 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32 | 3.7313 | 109.8 | 3.7308 | 168.5 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8 | 3.6093 | 119.1 | 3.6081 | 184.6 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32 | 22.4377 | 259.2 | 22.4297 | 280.1 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8 | 20.0055 | 252.9 | 20.0043 | 260.8 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32 | 0.9761 | 72.5 | 0.9628 | 107.5 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32 | 4.5834 | 347.6 | 4.5640 | 426.5 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32 | 27.7618 | 536.9 | 27.7653 | 578.2 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01 | 0.5787 | 65.9 | 0.7391 | 101.8 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1 | 4.4943 | 145.8 | 5.0762 | 186.0 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1 | 26.8838 | 303.4 | 26.6368 | 306.1 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01 | 0.5594 | 66.2 | 0.6254 | 106.6 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1 | 3.8607 | 98.2 | 4.1964 | 161.6 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1 | 22.4255 | 247.8 | 22.4420 | 275.2 |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | 1.8641 | 192.5 | 2.7874 | 194.5 |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | 1.8687 | 150.5 | 2.9112 | 148.0 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01 | 8.5508 | 179.5 | 8.9640 | 203.2 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1 | 38.3939 | 294.1 | 38.2479 | 315.0 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1 | 346.7502 | 379.2 | 348.1583 | 371.0 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01 | 6.8179 | 182.5 | 7.4652 | 183.8 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1 | 33.8194 | 290.0 | 33.7006 | 287.6 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1 | 268.5138 | 368.2 | 268.6434 | 370.6 |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing | 27.6891 | - | 28.1653 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing | 62.8736 | - | 62.5168 | - |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | 0.4348 | 59.0 | 0.4954 | 77.6 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | 2.3959 | 96.8 | 2.6536 | 139.8 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | 15.1110 | 280.6 | 17.6227 | 277.0 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | 0.8545 | 71.4 | 0.9055 | 95.0 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | 3.0068 | 219.5 | 3.0524 | 244.2 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | 17.3603 | 472.1 | 17.4559 | 518.1 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | 0.3756 | 59.0 | 0.3997 | 66.6 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | 1.9184 | 88.8 | 2.0042 | 129.1 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | 12.4203 | 222.8 | 12.7696 | 283.0 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | 0.7896 | 73.5 | 0.8104 | 110.9 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | 2.5736 | 213.0 | 2.5904 | 263.6 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | 16.1495 | 492.9 | 16.2131 | 539.5 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01 | 4.7327 | 343.9 | 4.7872 | 337.4 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1 | 27.6682 | 543.4 | 27.6033 | 589.9 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=1 | 196.5360 | 621.4 | 193.8568 | 641.6 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01 | 3.9543 | 362.0 | 3.9705 | 405.4 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1 | 23.6132 | 547.0 | 23.6236 | 578.9 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=1 | 189.6559 | 633.6 | 192.1635 | 619.9 |

## Per cell

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=k,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x597a40000000; level: placement cpu, 199 passes per interval, cursor 0, buffer at 0x597b40000000
- per repetition: home 5.365e+08 link read bytes and 0 SMMU translation requests; level 3.354e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=rotated,working-set-mib=8

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 528 passes per interval, cursor 1, buffer at 0x48a7c0000000; level: placement cpu, 54 passes per interval, cursor 1, buffer at 0x48a880000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 1.341e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=k,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 206 passes per interval, cursor 1, buffer at 0x434dc0000000; level: placement hbm, 1151 passes per interval, cursor 1, buffer at 0x434ec0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=rotated,working-set-mib=8

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 1253 passes per interval, cursor 1, buffer at 0x5e62c0000000; level: placement hbm, 666 passes per interval, cursor 1, buffer at 0x5e63c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sweeps

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x440900000000; level: placement cpu, 7 passes per interval, cursor 0, buffer at 0x440a40000000
- per repetition: home 6.422e+09 link read bytes and 3.611e+04 SMMU translation requests; level 8.028e+08 link read bytes and 3174 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sweeps

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 7 passes per interval, cursor 0, buffer at 0x447180000000; level: placement hbm, 51 passes per interval, cursor 0, buffer at 0x447240000000
- per repetition: home 0 link read bytes and 5539 SMMU translation requests; level 0 link read bytes and 574.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4895c0000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x489a80000000
- per repetition: home 1.718e+10 link read bytes and 2.718e+05 SMMU translation requests; level 1.074e+09 link read bytes and 2767 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x551fc0000000; level: placement hbm, 67 passes per interval, cursor 0, buffer at 0x552480000000
- per repetition: home 0 link read bytes and 7.164e+05 SMMU translation requests; level 0 link read bytes and 658.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x53b7c0000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x53be80000000
- per repetition: home 2.577e+10 link read bytes and 4.063e+05 SMMU translation requests; level 1.074e+09 link read bytes and 2654 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x4dcc40000000; level: placement hbm, 67 passes per interval, cursor 0, buffer at 0x4dd2c0000000
- per repetition: home 0 link read bytes and 1.138e+06 SMMU translation requests; level 0 link read bytes and 663.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 28 passes per interval, cursor 0, buffer at 0x5841c0000000; level: placement cpu, 7 passes per interval, cursor 0, buffer at 0x584300000000
- per repetition: home 2.684e+08 link read bytes and 0 SMMU translation requests; level 1.074e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 255 passes per interval, cursor 0, buffer at 0x5ff4c0000000; level: placement hbm, 68 passes per interval, cursor 0, buffer at 0x5ff580000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x582200000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x582ac0000000
- per repetition: home 3.436e+10 link read bytes and 5.464e+05 SMMU translation requests; level 1.074e+09 link read bytes and 2612 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x565500000000; level: placement hbm, 67 passes per interval, cursor 0, buffer at 0x565dc0000000
- per repetition: home 0 link read bytes and 1.618e+06 SMMU translation requests; level 0 link read bytes and 659.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x5d4900000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x5d4ac0000000
- per repetition: home 4.295e+09 link read bytes and 0 SMMU translation requests; level 1.074e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 18 passes per interval, cursor 0, buffer at 0x565740000000; level: placement hbm, 68 passes per interval, cursor 0, buffer at 0x5658c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4bdd00000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x4bdf80000000
- per repetition: home 8.59e+09 link read bytes and 1.093e+05 SMMU translation requests; level 1.074e+09 link read bytes and 2647 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 9 passes per interval, cursor 0, buffer at 0x469340000000; level: placement hbm, 67 passes per interval, cursor 0, buffer at 0x469600000000
- per repetition: home 0 link read bytes and 4.085e+04 SMMU translation requests; level 0 link read bytes and 715 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=working-set,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x4d4740000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4d4840000000
- per repetition: home 5.365e+08 link read bytes and 0 SMMU translation requests; level 1.718e+10 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=working-set,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 223 passes per interval, cursor 1, buffer at 0x483c80000000; level: placement hbm, 4 passes per interval, cursor 0, buffer at 0x483d80000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 253 passes per interval, cursor 0, buffer at 0x4d3980000000; level: placement hbm, 25 passes per interval, cursor 0, buffer at 0x4d3a00000000
- per repetition: home 0 link read bytes and 2.899 SMMU translation requests; level 0 link read bytes and 1462 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=16384,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x43bf80000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x43c440000000
- per repetition: home 4.961e+10 link read bytes and 2.725e+05 SMMU translation requests; level 3.196e+09 link read bytes and 1.762e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=16384,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=footprint

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x41af00000000; level: placement hbm, 16 passes per interval, cursor 0, buffer at 0x41b3c0000000
- per repetition: home 0 link read bytes and 4.966e+05 SMMU translation requests; level 0 link read bytes and 2003 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5baa40000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5baf00000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 4354 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x507a80000000; level: placement hbm, 44 passes per interval, cursor 0, buffer at 0x507f00000000
- per repetition: home 0 link read bytes and 1.206e+08 SMMU translation requests; level 0 link read bytes and 396.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=24576,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5c2900000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5c2fc0000000
- per repetition: home 7.685e+10 link read bytes and 5.055e+05 SMMU translation requests; level 3.198e+09 link read bytes and 1.757e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=24576,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4f7280000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4f7900000000
- per repetition: home 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; level 5.369e+08 link read bytes and 4355 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=24576,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x45b300000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x45b9c0000000
- per repetition: home 0 link read bytes and 1.667e+08 SMMU translation requests; level 0 link read bytes and 404.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=256,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x523880000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x523940000000
- per repetition: home 7.682e+08 link read bytes and 0 SMMU translation requests; level 3.197e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=256,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 95 passes per interval, cursor 0, buffer at 0x4c26c0000000; level: placement hbm, 16 passes per interval, cursor 0, buffer at 0x4c2780000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=256,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x536840000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x536900000000
- per repetition: home 5.368e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=256,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 47 passes per interval, cursor 0, buffer at 0x473ec0000000; level: placement hbm, 44 passes per interval, cursor 0, buffer at 0x473f80000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=256,kernel=k6,placement=cpu,type=factor,update=atomic,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x453700000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4537c0000000
- per repetition: home 0 link read bytes and 311.9 SMMU translation requests; level 0 link read bytes and 4200 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=256,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 98 passes per interval, cursor 0, buffer at 0x5e5e00000000; level: placement hbm, 25 passes per interval, cursor 0, buffer at 0x5e5ec0000000
- per repetition: home 0 link read bytes and 109.3 SMMU translation requests; level 0 link read bytes and 1269 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=32768,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x488800000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x489100000000
- per repetition: home 9.935e+10 link read bytes and 7.548e+05 SMMU translation requests; level 3.198e+09 link read bytes and 1.762e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x478580000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x478e00000000
- per repetition: home 5.369e+08 link read bytes and 1.912e+08 SMMU translation requests; level 5.369e+08 link read bytes and 4358 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5ef340000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x5efc00000000
- per repetition: home 0 link read bytes and 1.909e+08 SMMU translation requests; level 0 link read bytes and 405.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=4096,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x52dcc0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x52de80000000
- per repetition: home 1.287e+10 link read bytes and 6.873e+04 SMMU translation requests; level 3.195e+09 link read bytes and 1.762e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=4096,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x457480000000; level: placement hbm, 16 passes per interval, cursor 0, buffer at 0x457640000000
- per repetition: home 0 link read bytes and 3.883e+04 SMMU translation requests; level 0 link read bytes and 2106 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4cab80000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4cad00000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x4c3dc0000000; level: placement hbm, 44 passes per interval, cursor 0, buffer at 0x4c3f80000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=4096,kernel=k6,placement=cpu,type=factor,update=atomic,vary=footprint

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x41f4c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x41f680000000
- per repetition: home 0 link read bytes and 6.624e+04 SMMU translation requests; level 0 link read bytes and 4198 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=4096,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 7 passes per interval, cursor 0, buffer at 0x4d3b40000000; level: placement hbm, 25 passes per interval, cursor 0, buffer at 0x4d3d00000000
- per repetition: home 0 link read bytes and 1.731e+04 SMMU translation requests; level 0 link read bytes and 1247 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=factor,vary=keys

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x491500000000; level: placement cpu, 2 passes per interval, cursor 0, buffer at 0x4915c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=factor,vary=keys

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x461580000000; level: placement hbm, 27 passes per interval, cursor 0, buffer at 0x461640000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,type=factor,vary=keys

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x45b100000000; level: placement cpu, 2 passes per interval, cursor 0, buffer at 0x45b1c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8,kernel=k6,keys=1048576,placement=hbm,type=factor,vary=keys

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 113 passes per interval, cursor 0, buffer at 0x56d640000000; level: placement hbm, 27 passes per interval, cursor 0, buffer at 0x56d700000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8192,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4df7c0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4dfa80000000
- per repetition: home 2.555e+10 link read bytes and 1.366e+05 SMMU translation requests; level 3.198e+09 link read bytes and 1.763e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8192,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=footprint

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x5d9fc0000000; level: placement hbm, 16 passes per interval, cursor 0, buffer at 0x5da280000000
- per repetition: home 0 link read bytes and 1.241e+05 SMMU translation requests; level 0 link read bytes and 2138 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x5ef340000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5ef600000000
- per repetition: home 5.369e+08 link read bytes and 1.531e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4356 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x491480000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x491740000000
- per repetition: home 0 link read bytes and 1.537e+04 SMMU translation requests; level 0 link read bytes and 404.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=16,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sweeps

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5aaf80000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5ab080000000
- per repetition: home 6.422e+09 link read bytes and 3.608e+04 SMMU translation requests; level 1.285e+10 link read bytes and 3.6e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=16,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sweeps

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 7 passes per interval, cursor 0, buffer at 0x5a4280000000; level: placement hbm, 4 passes per interval, cursor 0, buffer at 0x5a4380000000
- per repetition: home 0 link read bytes and 5962 SMMU translation requests; level 0 link read bytes and 9634 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 7 passes per interval, cursor 0, buffer at 0x5a9140000000; level: placement cpu, 67 passes per interval, cursor 0, buffer at 0x5a9200000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 1.074e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 68 passes per interval, cursor 0, buffer at 0x4913c0000000; level: placement hbm, 530 passes per interval, cursor 1, buffer at 0x4914c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 7 passes per interval, cursor 0, buffer at 0x5a2bc0000000; level: placement cpu, 525 passes per interval, cursor 0, buffer at 0x5a2cc0000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 1.074e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 68 passes per interval, cursor 0, buffer at 0x415280000000; level: placement hbm, 1990 passes per interval, cursor 1, buffer at 0x415380000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of1000,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 7 passes per interval, cursor 0, buffer at 0x538f40000000; level: placement cpu, 1264 passes per interval, cursor 1, buffer at 0x539040000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 1.074e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of1000,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 68 passes per interval, cursor 0, buffer at 0x5ee480000000; level: placement hbm, 2533 passes per interval, cursor 1, buffer at 0x5ee580000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of2,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 7 passes per interval, cursor 0, buffer at 0x5a01c0000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5a02c0000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of2,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 68 passes per interval, cursor 0, buffer at 0x4a9400000000; level: placement hbm, 125 passes per interval, cursor 0, buffer at 0x4a9500000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=k,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x589a80000000; level: placement cpu, 104 passes per interval, cursor 0, buffer at 0x589b40000000
- per repetition: home 5.366e+08 link read bytes and 0 SMMU translation requests; level 6.708e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=k,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 203 passes per interval, cursor 1, buffer at 0x50f8c0000000; level: placement hbm, 853 passes per interval, cursor 1, buffer at 0x50f9c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sweeps

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x544900000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x544a40000000
- per repetition: home 6.422e+09 link read bytes and 3.622e+04 SMMU translation requests; level 1.606e+09 link read bytes and 8973 SMMU translation requests; multiplexed rows voided: 0

### route/at=2,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sweeps

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 7 passes per interval, cursor 0, buffer at 0x4146c0000000; level: placement hbm, 26 passes per interval, cursor 0, buffer at 0x414800000000
- per repetition: home 0 link read bytes and 5980 SMMU translation requests; level 0 link read bytes and 1482 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=partition

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4f2400000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4f28c0000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 2.971e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x56ba00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x56bec0000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.368e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4d09c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4d0e40000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.368e+08 link read bytes and 6.293e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x45ff40000000; level: placement hbm, 9 passes per interval, cursor 0, buffer at 0x4603c0000000
- per repetition: home 0 link read bytes and 1.207e+08 SMMU translation requests; level 0 link read bytes and 5.706e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4e8680000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4e8f40000000
- per repetition: home 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; level 5.368e+08 link read bytes and 1.307e+06 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5e7b40000000; level: placement hbm, 5 passes per interval, cursor 0, buffer at 0x5e8400000000
- per repetition: home 0 link read bytes and 1.91e+08 SMMU translation requests; level 0 link read bytes and 1.056e+06 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x540200000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5403c0000000
- per repetition: home 5.369e+08 link read bytes and 72 SMMU translation requests; level 5.368e+08 link read bytes and 343.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x50c5c0000000; level: placement hbm, 47 passes per interval, cursor 0, buffer at 0x50c740000000
- per repetition: home 0 link read bytes and 78 SMMU translation requests; level 0 link read bytes and 34.24 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x4793c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x479640000000
- per repetition: home 5.369e+08 link read bytes and 4.424e+04 SMMU translation requests; level 5.368e+08 link read bytes and 6.642e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x4f9500000000; level: placement hbm, 45 passes per interval, cursor 0, buffer at 0x4f9780000000
- per repetition: home 0 link read bytes and 4.427e+04 SMMU translation requests; level 0 link read bytes and 7251 SMMU translation requests; multiplexed rows voided: 0

### route/at=3of4,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 7 passes per interval, cursor 0, buffer at 0x4b9280000000; level: placement cpu, 10 passes per interval, cursor 0, buffer at 0x4b9340000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 8.053e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=3of4,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 68 passes per interval, cursor 0, buffer at 0x4a2940000000; level: placement hbm, 86 passes per interval, cursor 0, buffer at 0x4a2a40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=4,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=k,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x49cac0000000; level: placement cpu, 53 passes per interval, cursor 0, buffer at 0x49cb80000000
- per repetition: home 5.366e+08 link read bytes and 0 SMMU translation requests; level 1.342e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=4,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=k,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 209 passes per interval, cursor 1, buffer at 0x521a00000000; level: placement hbm, 575 passes per interval, cursor 1, buffer at 0x521b00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=4,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=repeat

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x434d00000000; level: placement cpu, 2 passes per interval, cursor 0, buffer at 0x434e00000000
- per repetition: home 0 link read bytes and 4226 SMMU translation requests; level 0 link read bytes and 8266 SMMU translation requests; multiplexed rows voided: 0

### route/at=4,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=repeat

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 25 passes per interval, cursor 0, buffer at 0x4e0340000000; level: placement hbm, 13 passes per interval, cursor 0, buffer at 0x4e0400000000
- per repetition: home 0 link read bytes and 1265 SMMU translation requests; level 0 link read bytes and 1981 SMMU translation requests; multiplexed rows voided: 0

### route/at=4,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sweeps

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4712c0000000; level: placement cpu, 2 passes per interval, cursor 0, buffer at 0x4713c0000000
- per repetition: home 6.422e+09 link read bytes and 3.608e+04 SMMU translation requests; level 3.211e+09 link read bytes and 1.797e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=4,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sweeps

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 7 passes per interval, cursor 0, buffer at 0x570600000000; level: placement hbm, 13 passes per interval, cursor 0, buffer at 0x570700000000
- per repetition: home 0 link read bytes and 5504 SMMU translation requests; level 0 link read bytes and 2973 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=1024,kernel=k3,placement=cpu,type=factor,vary=page-size

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x43d940000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x43da40000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=1024,kernel=k3,placement=hbm,type=factor,vary=page-size

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 44 passes per interval, cursor 0, buffer at 0x5c5500000000; level: placement hbm, 44 passes per interval, cursor 0, buffer at 0x5c5600000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-size

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5fa7c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5fac40000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 149.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-size

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x4a41c0000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x4a4640000000
- per repetition: home 0 link read bytes and 1.206e+08 SMMU translation requests; level 0 link read bytes and 14.25 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=16384,kernel=k3p,placement=cpu,type=factor,vary=page-size

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x475180000000; level: placement cpu, 201 passes per interval, cursor 0, buffer at 0x475600000000
- per repetition: home 3.355e+07 link read bytes and 1.956e+06 SMMU translation requests; level 3.355e+07 link read bytes and 2.965 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-size

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x477680000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x477f00000000
- per repetition: home 5.369e+08 link read bytes and 1.912e+08 SMMU translation requests; level 5.369e+08 link read bytes and 279.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-size

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4c4400000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4c45c0000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-size

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x4f1880000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x4f1a00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-size

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x480200000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x480480000000
- per repetition: home 5.369e+08 link read bytes and 4109 SMMU translation requests; level 5.369e+08 link read bytes and 84.75 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-size

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x551940000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x551c00000000
- per repetition: home 0 link read bytes and 4183 SMMU translation requests; level 0 link read bytes and 7.929 SMMU translation requests; multiplexed rows voided: 0

### route/at=64,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=k,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x57a240000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x57a300000000
- per repetition: home 5.366e+08 link read bytes and 0 SMMU translation requests; level 2.146e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=64,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=k,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 206 passes per interval, cursor 1, buffer at 0x500480000000; level: placement hbm, 61 passes per interval, cursor 1, buffer at 0x500580000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=64,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sweeps

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4a2280000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4a2380000000
- per repetition: home 6.422e+09 link read bytes and 3.611e+04 SMMU translation requests; level 5.138e+10 link read bytes and 3.594e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=64,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sweeps

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 7 passes per interval, cursor 0, buffer at 0x5d1a40000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5d1b80000000
- per repetition: home 0 link read bytes and 5971 SMMU translation requests; level 0 link read bytes and 3.854e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x42a000000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x42a480000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.386e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x567280000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x567700000000
- per repetition: home 5.369e+08 link read bytes and 1.212e+08 SMMU translation requests; level 5.386e+08 link read bytes and 2.777e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5c9ac0000000; level: placement hbm, 13 passes per interval, cursor 0, buffer at 0x5c9f80000000
- per repetition: home 0 link read bytes and 1.207e+08 SMMU translation requests; level 0 link read bytes and 3.988e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x565b80000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x566400000000
- per repetition: home 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; level 5.39e+08 link read bytes and 8.274e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5b2c80000000; level: placement hbm, 7 passes per interval, cursor 0, buffer at 0x5b3500000000
- per repetition: home 0 link read bytes and 1.91e+08 SMMU translation requests; level 0 link read bytes and 8.67e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5f47c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5f4980000000
- per repetition: home 5.369e+08 link read bytes and 74.12 SMMU translation requests; level 5.36e+08 link read bytes and 154.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x5ca640000000; level: placement hbm, 49 passes per interval, cursor 0, buffer at 0x5ca7c0000000
- per repetition: home 0 link read bytes and 72 SMMU translation requests; level 0 link read bytes and 32.98 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x47f7c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x47fa80000000
- per repetition: home 5.369e+08 link read bytes and 4.42e+04 SMMU translation requests; level 5.371e+08 link read bytes and 3.434e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x54eb40000000; level: placement hbm, 46 passes per interval, cursor 0, buffer at 0x54ee00000000
- per repetition: home 0 link read bytes and 4.426e+04 SMMU translation requests; level 0 link read bytes and 4379 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=working-set,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x44b440000000; level: placement cpu, 531 passes per interval, cursor 1, buffer at 0x44b500000000
- per repetition: home 5.366e+08 link read bytes and 0 SMMU translation requests; level 8.382e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=working-set,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 206 passes per interval, cursor 1, buffer at 0x526140000000; level: placement hbm, 1239 passes per interval, cursor 1, buffer at 0x526280000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=9of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 7 passes per interval, cursor 0, buffer at 0x52dec0000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x52dfc0000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 9.664e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=9of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 68 passes per interval, cursor 0, buffer at 0x435ec0000000; level: placement hbm, 73 passes per interval, cursor 0, buffer at 0x435fc0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=hbm,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=placement

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x4b6800000000; level: placement hbm, 2 passes per interval, cursor 0, buffer at 0x4b68c0000000
- no hardware counters in this cell

### route/at=hbm,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=plain,vary=placement

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 9 passes per interval, cursor 0, buffer at 0x489d80000000; level: placement hbm, 9 passes per interval, cursor 0, buffer at 0x489e40000000
- no hardware counters in this cell

### route/at=hbm,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=placement

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x48e580000000; level: placement hbm, 2 passes per interval, cursor 0, buffer at 0x48e640000000
- no hardware counters in this cell

### route/at=hbm,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=plain,vary=placement

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 9 passes per interval, cursor 0, buffer at 0x5948c0000000; level: placement hbm, 8 passes per interval, cursor 0, buffer at 0x5949c0000000
- no hardware counters in this cell

### route/at=line,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=layout

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x58d900000000; level: placement cpu, 6 passes per interval, cursor 0, buffer at 0x58da40000000
- per repetition: home 0 link read bytes and 4234 SMMU translation requests; level 0 link read bytes and 2888 SMMU translation requests; multiplexed rows voided: 0

### route/at=line,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=layout

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 25 passes per interval, cursor 0, buffer at 0x568d80000000; level: placement hbm, 59 passes per interval, cursor 0, buffer at 0x568e80000000
- per repetition: home 0 link read bytes and 1350 SMMU translation requests; level 0 link read bytes and 434.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=none,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=tiling

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x454980000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x454a80000000
- per repetition: home 6.422e+09 link read bytes and 3.616e+04 SMMU translation requests; level 1.307e+10 link read bytes and 3.465e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=none,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=tiling

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 7 passes per interval, cursor 0, buffer at 0x593e80000000; level: placement hbm, 8 passes per interval, cursor 0, buffer at 0x593f80000000
- per repetition: home 0 link read bytes and 6006 SMMU translation requests; level 0 link read bytes and 9746 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=1024,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x44bd80000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x44c020000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=1024,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 44 passes per interval, cursor 0, buffer at 0x545300000000; level: placement hbm, 44 passes per interval, cursor 0, buffer at 0x545420000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=1024,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5a3540000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5a3820000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=1024,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 43 passes per interval, cursor 0, buffer at 0x563180000000; level: placement hbm, 44 passes per interval, cursor 0, buffer at 0x563420000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=11520,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x521280000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x521820000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=11520,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4defc0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4df420000000
- per repetition: home 5.369e+08 link read bytes and 6.722e+07 SMMU translation requests; level 5.369e+08 link read bytes and 6.718e+07 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=12288,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x40b980000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x40c020000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=12288,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 42 passes per interval, cursor 0, buffer at 0x417b40000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x418020000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=12288,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x450380000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x450820000000
- per repetition: home 5.369e+08 link read bytes and 7.82e+07 SMMU translation requests; level 5.369e+08 link read bytes and 7.82e+07 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=12288,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5a9140000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5a9820000000
- per repetition: home 0 link read bytes and 7.777e+07 SMMU translation requests; level 0 link read bytes and 7.775e+07 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=1536,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x59c780000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x59cc20000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=1536,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x575e40000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x576020000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4cc3c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4ccc20000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=16384,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 42 passes per interval, cursor 0, buffer at 0x410e00000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x411420000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=16384,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4f6080000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4f6820000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=16384,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x4ba080000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x4ba820000000
- per repetition: home 0 link read bytes and 1.207e+08 SMMU translation requests; level 0 link read bytes and 1.207e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=2048,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x40e180000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x40e420000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=2048,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4d9a00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4d9c20000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=24576,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x524cc0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x525420000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=24576,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4942c0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x494c20000000
- per repetition: home 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=256,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x447500000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x447820000000
- per repetition: home 5.368e+08 link read bytes and 0 SMMU translation requests; level 5.368e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=256,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 48 passes per interval, cursor 0, buffer at 0x58cdc0000000; level: placement hbm, 48 passes per interval, cursor 0, buffer at 0x58d020000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=256,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5eaa00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5eac20000000
- per repetition: home 5.368e+08 link read bytes and 0 SMMU translation requests; level 5.368e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=256,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 48 passes per interval, cursor 0, buffer at 0x53c4c0000000; level: placement hbm, 48 passes per interval, cursor 0, buffer at 0x53c820000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=32768,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x415680000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x416020000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=32768,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5ead40000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5eb820000000
- per repetition: home 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=4096,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5e3880000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5e3c20000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=4096,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 43 passes per interval, cursor 0, buffer at 0x4f4280000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x4f4420000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=4096,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4c7940000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4c7c20000000
- per repetition: home 5.369e+08 link read bytes and 4427 SMMU translation requests; level 5.369e+08 link read bytes and 4802 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=4096,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x50ae00000000; level: placement hbm, 4 passes per interval, cursor 0, buffer at 0x50b020000000
- per repetition: home 0 link read bytes and 4408 SMMU translation requests; level 0 link read bytes and 4802 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=8192,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x47fc80000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x480020000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=8192,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 42 passes per interval, cursor 0, buffer at 0x51f0c0000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x51f420000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=8192,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x419e00000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x41a420000000
- per repetition: home 5.369e+08 link read bytes and 4.396e+04 SMMU translation requests; level 5.369e+08 link read bytes and 1.368e+07 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=8192,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x53e380000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x53e820000000
- per repetition: home 0 link read bytes and 4.388e+04 SMMU translation requests; level 0 link read bytes and 1.36e+07 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=9728,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x42e740000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x42ec20000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=9728,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5b9b40000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5ba020000000
- per repetition: home 5.369e+08 link read bytes and 3.598e+07 SMMU translation requests; level 5.369e+08 link read bytes and 3.597e+07 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x4e6e40000000; level: placement cpu, 9 passes per interval, cursor 0, buffer at 0x4e6ec0000000
- no hardware counters in this cell

### route/at=plain,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x460a80000000; level: placement hbm, 9 passes per interval, cursor 0, buffer at 0x460b40000000
- no hardware counters in this cell

### route/at=plain,footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x5416c0000000; level: placement cpu, 9 passes per interval, cursor 0, buffer at 0x541780000000
- no hardware counters in this cell

### route/at=plain,footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x5dff00000000; level: placement hbm, 9 passes per interval, cursor 0, buffer at 0x5dff80000000
- no hardware counters in this cell

### route/at=plain,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x472980000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x472a80000000
- per repetition: home 0 link read bytes and 4202 SMMU translation requests; level 1.074e+09 link read bytes and 4530 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 25 passes per interval, cursor 0, buffer at 0x57bc80000000; level: placement hbm, 27 passes per interval, cursor 0, buffer at 0x57bd40000000
- per repetition: home 0 link read bytes and 1244 SMMU translation requests; level 0 link read bytes and 2724 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x51ad00000000; level: placement cpu, 9 passes per interval, cursor 0, buffer at 0x51adc0000000
- no hardware counters in this cell

### route/at=plain,footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x57f0c0000000; level: placement hbm, 9 passes per interval, cursor 0, buffer at 0x57f140000000
- no hardware counters in this cell

### route/at=plain,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 264 passes per interval, cursor 0, buffer at 0x548280000000; level: placement hbm, 253 passes per interval, cursor 0, buffer at 0x548300000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x5f9cc0000000; level: placement cpu, 9 passes per interval, cursor 0, buffer at 0x5f9d80000000
- no hardware counters in this cell

### route/at=plain,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x4a4500000000; level: placement hbm, 8 passes per interval, cursor 0, buffer at 0x4a4580000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x4f9ec0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4f9f80000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x46dac0000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x46db80000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x4c8540000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4c8600000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x5d4740000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5d4800000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x555f80000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x556040000000
- per repetition: home 0 link read bytes and 4212 SMMU translation requests; level 1.074e+09 link read bytes and 4494 SMMU translation requests; multiplexed rows voided: 0

### route/at=returned,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 25 passes per interval, cursor 0, buffer at 0x5a07c0000000; level: placement hbm, 23 passes per interval, cursor 0, buffer at 0x5a0900000000
- per repetition: home 0 link read bytes and 1279 SMMU translation requests; level 0 link read bytes and 3018 SMMU translation requests; multiplexed rows voided: 0

### route/at=returned,footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x5bc780000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5bc800000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x4ae1c0000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x4ae240000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 261 passes per interval, cursor 0, buffer at 0x4d3f80000000; level: placement hbm, 155 passes per interval, cursor 0, buffer at 0x4d4040000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=returned,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x4ff680000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4ff740000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x56e500000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x56e5c0000000
- no hardware counters in this cell

### route/at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=generator

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5fe140000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5fe240000000
- per repetition: home 3.201e+09 link read bytes and 0 SMMU translation requests; level 2.853e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=generator

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 16 passes per interval, cursor 0, buffer at 0x579800000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x579900000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=rmat,footprint-mib=8192,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=generator

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x42b5c0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x42b880000000
- per repetition: home 2.555e+10 link read bytes and 1.365e+05 SMMU translation requests; level 2.415e+10 link read bytes and 1.641e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=rmat,footprint-mib=8192,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=generator

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x457180000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x457440000000
- per repetition: home 0 link read bytes and 1.37e+05 SMMU translation requests; level 0 link read bytes and 1.636e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5d8b00000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5d8bc0000000
- per repetition: home 5.243e+05 link read bytes and 29.25 SMMU translation requests; level 5.243e+05 link read bytes and 26.52 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x48e800000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x48e880000000
- per repetition: home 5.243e+05 link read bytes and 0.78 SMMU translation requests; level 5.243e+05 link read bytes and 0.78 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x595680000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x595700000000
- per repetition: home 5.243e+05 link read bytes and 28.08 SMMU translation requests; level 5.243e+05 link read bytes and 30.42 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x54a000000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x54a080000000
- per repetition: home 5.243e+05 link read bytes and 1.56 SMMU translation requests; level 5.243e+05 link read bytes and 1.17 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5126c0000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x512740000000
- per repetition: home 5.243e+05 link read bytes and 0.78 SMMU translation requests; level 5.243e+05 link read bytes and 0.78 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x53d0c0000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x53d140000000
- per repetition: home 5.243e+05 link read bytes and 0.78 SMMU translation requests; level 5.243e+05 link read bytes and 0.78 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5ecec0000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5ecf80000000
- per repetition: home 6.711e+07 link read bytes and 2175 SMMU translation requests; level 6.711e+07 link read bytes and 1705 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x531540000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5315c0000000
- per repetition: home 6.711e+07 link read bytes and 2082 SMMU translation requests; level 6.711e+07 link read bytes and 1591 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x51ba80000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x51bb40000000
- per repetition: home 6.711e+07 link read bytes and 1793 SMMU translation requests; level 6.711e+07 link read bytes and 1717 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5425c0000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x542680000000
- per repetition: home 0 link read bytes and 2893 SMMU translation requests; level 0 link read bytes and 2158 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5fd300000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5fd380000000
- per repetition: home 0 link read bytes and 2924 SMMU translation requests; level 0 link read bytes and 2109 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x460f40000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x461000000000
- per repetition: home 0 link read bytes and 2912 SMMU translation requests; level 0 link read bytes and 2808 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5f2100000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5f2180000000
- per repetition: home 6.711e+07 link read bytes and 2098 SMMU translation requests; level 6.711e+07 link read bytes and 2085 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x410a80000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x410b00000000
- per repetition: home 6.711e+07 link read bytes and 2140 SMMU translation requests; level 6.711e+07 link read bytes and 1814 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x4aa080000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x4aa140000000
- per repetition: home 6.711e+07 link read bytes and 2093 SMMU translation requests; level 6.711e+07 link read bytes and 2017 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4bf100000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4bf1c0000000
- per repetition: home 0 link read bytes and 2918 SMMU translation requests; level 0 link read bytes and 2090 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5d4280000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5d4300000000
- per repetition: home 0 link read bytes and 2932 SMMU translation requests; level 0 link read bytes and 2061 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4a0740000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4a0800000000
- per repetition: home 0 link read bytes and 2911 SMMU translation requests; level 0 link read bytes and 2892 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5f6a00000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5f6ac0000000
- per repetition: home 0 link read bytes and 400.2 SMMU translation requests; level 0 link read bytes and 296.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x437340000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x437400000000
- per repetition: home 0 link read bytes and 398.3 SMMU translation requests; level 0 link read bytes and 306 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4a3380000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4a3440000000
- per repetition: home 0 link read bytes and 373.7 SMMU translation requests; level 0 link read bytes and 339.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x56d3c0000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x56d480000000
- per repetition: home 0 link read bytes and 379.1 SMMU translation requests; level 0 link read bytes and 302.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4c8900000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4c89c0000000
- per repetition: home 0 link read bytes and 405.3 SMMU translation requests; level 0 link read bytes and 340.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x473dc0000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x473e80000000
- per repetition: home 0 link read bytes and 403 SMMU translation requests; level 0 link read bytes and 380.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4f9cc0000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4f9d80000000
- per repetition: home 0 link read bytes and 4562 SMMU translation requests; level 0 link read bytes and 2737 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x498400000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4984c0000000
- per repetition: home 0 link read bytes and 4511 SMMU translation requests; level 0 link read bytes and 2742 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x58a5c0000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x58a640000000
- per repetition: home 0 link read bytes and 4506 SMMU translation requests; level 0 link read bytes and 4286 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x573940000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x573a00000000
- per repetition: home 0 link read bytes and 4589 SMMU translation requests; level 0 link read bytes and 2604 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x489240000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x489300000000
- per repetition: home 0 link read bytes and 4358 SMMU translation requests; level 0 link read bytes and 2722 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x501a40000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x501ac0000000
- per repetition: home 0 link read bytes and 4512 SMMU translation requests; level 0 link read bytes and 4294 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=factor,vary=sharing

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4e8f40000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4e9000000000
- per repetition: home 3.195e+09 link read bytes and 0 SMMU translation requests; level 3.194e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=factor,vary=sharing

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 16 passes per interval, cursor 0, buffer at 0x545540000000; level: placement hbm, 16 passes per interval, cursor 0, buffer at 0x545680000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5d4980000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5d4a80000000
- per repetition: home 8.382e+06 link read bytes and 336.2 SMMU translation requests; level 8.382e+06 link read bytes and 312.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x4e6980000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x4e6a40000000
- per repetition: home 8.382e+06 link read bytes and 329.1 SMMU translation requests; level 8.382e+06 link read bytes and 318.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x4ba480000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x4ba580000000
- per repetition: home 8.382e+06 link read bytes and 331.7 SMMU translation requests; level 8.382e+06 link read bytes and 330.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x57a380000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x57a480000000
- per repetition: home 8.382e+06 link read bytes and 335.6 SMMU translation requests; level 8.382e+06 link read bytes and 312.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x520bc0000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x520c80000000
- per repetition: home 8.382e+06 link read bytes and 328.7 SMMU translation requests; level 8.382e+06 link read bytes and 312.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x549b40000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x549c40000000
- per repetition: home 8.382e+06 link read bytes and 332.2 SMMU translation requests; level 8.382e+06 link read bytes and 334.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x58b980000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x58ba40000000
- per repetition: home 5.366e+08 link read bytes and 672 SMMU translation requests; level 5.365e+08 link read bytes and 806.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x564480000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x564540000000
- per repetition: home 8.382e+06 link read bytes and 336.1 SMMU translation requests; level 8.382e+06 link read bytes and 335 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x499740000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x499800000000
- per repetition: home 5.366e+08 link read bytes and 781.2 SMMU translation requests; level 5.365e+08 link read bytes and 787 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x594900000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5949c0000000
- per repetition: home 8.382e+06 link read bytes and 331.3 SMMU translation requests; level 8.382e+06 link read bytes and 332.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x49bfc0000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x49c0c0000000
- per repetition: home 5.366e+08 link read bytes and 166.6 SMMU translation requests; level 5.365e+08 link read bytes and 188 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x550f80000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x551040000000
- per repetition: home 8.382e+06 link read bytes and 320.5 SMMU translation requests; level 8.382e+06 link read bytes and 321.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x549400000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x549500000000
- per repetition: home 0 link read bytes and 951 SMMU translation requests; level 0 link read bytes and 947 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x454080000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x4541c0000000
- per repetition: home 0 link read bytes and 949.1 SMMU translation requests; level 0 link read bytes and 953.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x432a40000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x432b40000000
- per repetition: home 0 link read bytes and 951.5 SMMU translation requests; level 0 link read bytes and 956.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x503e00000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x503f00000000
- per repetition: home 5.365e+08 link read bytes and 667.3 SMMU translation requests; level 5.366e+08 link read bytes and 804.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5eb400000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5eb4c0000000
- per repetition: home 8.382e+06 link read bytes and 322.3 SMMU translation requests; level 8.382e+06 link read bytes and 323.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x512b80000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x512c80000000
- per repetition: home 5.365e+08 link read bytes and 731.2 SMMU translation requests; level 5.366e+08 link read bytes and 799.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x460040000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x460140000000
- per repetition: home 8.382e+06 link read bytes and 327 SMMU translation requests; level 8.382e+06 link read bytes and 323.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x51da80000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x51db40000000
- per repetition: home 5.365e+08 link read bytes and 327.3 SMMU translation requests; level 5.365e+08 link read bytes and 274.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5cedc0000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5cee80000000
- per repetition: home 8.382e+06 link read bytes and 319.8 SMMU translation requests; level 8.382e+06 link read bytes and 321.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x486980000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x486a80000000
- per repetition: home 0 link read bytes and 949.4 SMMU translation requests; level 0 link read bytes and 951.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x511100000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x511200000000
- per repetition: home 0 link read bytes and 943.9 SMMU translation requests; level 0 link read bytes and 949.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x469640000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x469740000000
- per repetition: home 0 link read bytes and 946.4 SMMU translation requests; level 0 link read bytes and 950.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4d7680000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4d7740000000
- per repetition: home 5.369e+08 link read bytes and 1.735e+04 SMMU translation requests; level 5.369e+08 link read bytes and 1.74e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x47c240000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x47c300000000
- per repetition: home 5.369e+08 link read bytes and 1.31e+04 SMMU translation requests; level 5.369e+08 link read bytes and 1.305e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x422cc0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x422dc0000000
- per repetition: home 5.369e+08 link read bytes and 4363 SMMU translation requests; level 5.369e+08 link read bytes and 4353 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4c2300000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4c23c0000000
- per repetition: home 5.369e+08 link read bytes and 1.303e+04 SMMU translation requests; level 5.369e+08 link read bytes and 1.741e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5af340000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5af440000000
- per repetition: home 5.369e+08 link read bytes and 1.734e+04 SMMU translation requests; level 5.369e+08 link read bytes and 1.732e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4594c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4595c0000000
- per repetition: home 5.369e+08 link read bytes and 8695 SMMU translation requests; level 5.369e+08 link read bytes and 8673 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x417440000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x417900000000
- per repetition: home 3.355e+07 link read bytes and 2.025e+06 SMMU translation requests; level 3.355e+07 link read bytes and 2.014e+06 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5dd1c0000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5dd640000000
- per repetition: home 3.355e+07 link read bytes and 2.025e+06 SMMU translation requests; level 3.355e+07 link read bytes and 2.021e+06 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x424540000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x424a00000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x48ec40000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x48f100000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5ff4c0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5ff940000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x417040000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4174c0000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x503540000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x503a00000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x587640000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x587ac0000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5ff000000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5ff140000000
- per repetition: home 6.422e+09 link read bytes and 3.592e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.602e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 7 passes per interval, cursor 0, buffer at 0x5e9900000000; level: placement hbm, 7 passes per interval, cursor 0, buffer at 0x5e9a00000000
- per repetition: home 0 link read bytes and 5495 SMMU translation requests; level 0 link read bytes and 5467 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x58f7c0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x58f8c0000000
- per repetition: home 6.422e+09 link read bytes and 3.607e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.594e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x495e40000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x495f40000000
- per repetition: home 6.422e+09 link read bytes and 3.597e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.586e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5b3d80000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5b3ec0000000
- per repetition: home 6.422e+09 link read bytes and 3.623e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.603e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x53ad80000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x53ae80000000
- per repetition: home 0 link read bytes and 3.886e+04 SMMU translation requests; level 0 link read bytes and 4.186e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x43f640000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x43f740000000
- per repetition: home 0 link read bytes and 3.86e+04 SMMU translation requests; level 0 link read bytes and 4.492e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x43fb00000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x43fc40000000
- per repetition: home 0 link read bytes and 4.272e+04 SMMU translation requests; level 0 link read bytes and 4.481e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x41be40000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x41bf40000000
- per repetition: home 6.422e+09 link read bytes and 3.629e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.609e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x40a0c0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x40a1c0000000
- per repetition: home 6.422e+09 link read bytes and 3.611e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.598e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4a22c0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4a23c0000000
- per repetition: home 6.422e+09 link read bytes and 3.598e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.572e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x583100000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x583240000000
- per repetition: home 0 link read bytes and 4.277e+04 SMMU translation requests; level 0 link read bytes and 4.505e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x4bda80000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x4bdb80000000
- per repetition: home 0 link read bytes and 4.261e+04 SMMU translation requests; level 0 link read bytes and 4.48e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x477640000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x477740000000
- per repetition: home 0 link read bytes and 3.876e+04 SMMU translation requests; level 0 link read bytes and 4.465e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x5b6400000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x5b6680000000
- per repetition: home 0 link read bytes and 1.328e+05 SMMU translation requests; level 0 link read bytes and 1.328e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x432200000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x432480000000
- per repetition: home 0 link read bytes and 1.327e+05 SMMU translation requests; level 0 link read bytes and 1.328e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=1

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x4e2780000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x4e2a40000000
- per repetition: home 0 link read bytes and 1.329e+05 SMMU translation requests; level 0 link read bytes and 1.328e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x523ec0000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x524180000000
- per repetition: home 0 link read bytes and 1.329e+05 SMMU translation requests; level 0 link read bytes and 1.328e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x4815c0000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x481880000000
- per repetition: home 0 link read bytes and 1.329e+05 SMMU translation requests; level 0 link read bytes and 1.341e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=1

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x5dadc0000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x5db080000000
- per repetition: home 0 link read bytes and 1.327e+05 SMMU translation requests; level 0 link read bytes and 1.339e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=sorted,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=index-order

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5922c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x592780000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.438e+08 link read bytes and 2.796e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=stadd,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x407740000000; level: placement cpu, 3 passes per interval, cursor 0, buffer at 0x407800000000
- no hardware counters in this cell

### route/at=stadd,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x4969c0000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x496a80000000
- no hardware counters in this cell

### route/at=stadd,footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x4fd140000000; level: placement cpu, 3 passes per interval, cursor 0, buffer at 0x4fd200000000
- no hardware counters in this cell

### route/at=stadd,footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x409680000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x409740000000
- no hardware counters in this cell

### route/at=stadd,footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x4b80c0000000; level: placement cpu, 3 passes per interval, cursor 0, buffer at 0x4b8140000000
- no hardware counters in this cell

### route/at=stadd,footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x4d0cc0000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x4d0d80000000
- no hardware counters in this cell

### route/at=stadd,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x578540000000; level: placement cpu, 3 passes per interval, cursor 0, buffer at 0x578600000000
- no hardware counters in this cell

### route/at=stadd,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x56f480000000; level: placement hbm, 2 passes per interval, cursor 0, buffer at 0x56f540000000
- no hardware counters in this cell

### route/at=tiles,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=tiling,working-set-mib=8

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 529 passes per interval, cursor 1, buffer at 0x5d5080000000; level: placement cpu, 544 passes per interval, cursor 1, buffer at 0x5d5140000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 8.38e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=tiles,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=tiling,working-set-mib=8

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 1251 passes per interval, cursor 1, buffer at 0x5fdc80000000; level: placement hbm, 1305 passes per interval, cursor 1, buffer at 0x5fdd80000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,type=factor,vary=strategy

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x551c00000000; level: placement cpu, 3 passes per interval, cursor 0, buffer at 0x551c80000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp,footprint-mib=8,kernel=k6,keys=1048576,placement=hbm,type=factor,vary=strategy

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 113 passes per interval, cursor 0, buffer at 0x494240000000; level: placement hbm, 70 passes per interval, cursor 0, buffer at 0x4942c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp,footprint-mib=8,kernel=k6,keys=4096,placement=cpu,type=factor,vary=strategy

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x427b00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x427b80000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp,footprint-mib=8,kernel=k6,keys=4096,placement=hbm,type=factor,vary=strategy

- first variant B, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 76 passes per interval, cursor 0, buffer at 0x553100000000; level: placement hbm, 71 passes per interval, cursor 0, buffer at 0x5531c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp,footprint-mib=8,kernel=k6,keys=65536,placement=cpu,type=factor,vary=strategy

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement cpu, 5 passes per interval, cursor 0, buffer at 0x575240000000; level: placement cpu, 5 passes per interval, cursor 0, buffer at 0x575300000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp,footprint-mib=8,kernel=k6,keys=65536,placement=hbm,type=factor,vary=strategy

- first variant A, seed 71; repeats alternated as drawn: yes
- home: placement hbm, 104 passes per interval, cursor 0, buffer at 0x43a780000000; level: placement hbm, 70 passes per interval, cursor 0, buffer at 0x43a800000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

