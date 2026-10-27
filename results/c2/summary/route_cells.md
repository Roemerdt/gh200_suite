# Route cells: direct route against copy route, recomputed from raw rows

Times are per repetition in ms: one pass for the direct route, one complete call (copy-in, kernel, copy-out) for the copy route. The route difference is direct minus copy within a repeat, as median with its 95 % rank interval; a negative value means direct access is faster. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | direct ms | copy ms | route difference ms [interval] | relative to copy | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|
| alignment=off512m,footprint-mib=8192,kernel=k3,placement=cpu | 48.2502 | 23.5120 | 24.7300 [24.7118, 24.7419] | +105.2 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 2.9003 | 3.2682 | -0.3679 [-0.3700, -0.3669] | -11.3 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | 0.2990 | 0.9463 | -0.6473 [-0.6477, -0.6462] | -68.4 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=cpu | 45.8501 | 46.1220 | -0.2660 [-0.2837, -0.2521] | -0.6 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=hbm | 5.7308 | 14.6573 | -8.9177 [-8.9706, -8.9028] | -60.8 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=19456,kernel=k1,placement=cpu | 54.1191 | 55.2523 | -1.1283 [-1.1544, -1.0770] | -2.0 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=23296,kernel=k1,placement=cpu | 64.5364 | 65.0287 | -0.4889 [-0.5227, -0.4747] | -0.8 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=cpu | 68.2882 | 66.4569 | 1.8295 [1.7877, 1.8983] | +2.8 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=hbm | 9.5358 | 22.6286 | -13.0908 [-13.1631, -13.0126] | -57.9 % | 40 | yes | pass |
| f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu | 0.7310 | 0.8594 | -0.1280 [-0.1292, -0.1268] | -14.9 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm | 0.0783 | 0.7322 | -0.6539 [-0.6545, -0.6533] | -89.3 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=cpu | 90.4658 | 85.8238 | 4.6452 [4.6049, 4.7195] | +5.4 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu | 11.6980 | 12.6195 | -0.9204 [-0.9268, -0.9188] | -7.3 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=hbm | 1.1748 | 3.6747 | -2.4996 [-2.5018, -2.4972] | -68.0 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,sharing=shared,state=clean | 0.1910 | 0.2403 | -0.0495 [-0.0502, -0.0485] | -20.6 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,sharing=shared,state=dirty | 0.3216 | 0.3540 | -0.0323 [-0.0333, -0.0317] | -9.1 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,sharing=shared,state=evicted | 0.1905 | 0.2386 | -0.0480 [-0.0486, -0.0474] | -20.1 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,sharing=shared,state=clean | 0.0922 | 0.1382 | -0.0459 [-0.0463, -0.0451] | -33.2 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,sharing=shared,state=dirty | 0.1231 | 0.1692 | -0.0460 [-0.0464, -0.0453] | -27.2 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,sharing=shared,state=evicted | 0.0356 | 0.0918 | -0.0561 [-0.0564, -0.0559] | -61.2 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=cpu | 23.2754 | 23.2344 | 0.0427 [0.0367, 0.0469] | +0.2 % | 100 | yes | pass |
| f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=hbm | 2.4065 | 7.3923 | -4.9862 [-4.9955, -4.9813] | -67.5 % | 10 | yes | pass |
| f-den=10,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 0.2995 | 0.3607 | -0.0612 [-0.0616, -0.0606] | -17.0 % | 10 | yes | pass |
| f-den=10,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | 0.0383 | 0.1260 | -0.0876 [-0.0878, -0.0875] | -69.6 % | 10 | yes | pass |
| f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=cpu | 2.6433 | 3.2471 | -0.6036 [-0.6061, -0.6028] | -18.6 % | 10 | yes | pass |
| f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=hbm | 0.2763 | 0.8764 | -0.6001 [-0.6016, -0.5990] | -68.5 % | 10 | yes | pass |
| f-den=100,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 0.0382 | 0.0520 | -0.0138 [-0.0139, -0.0137] | -26.6 % | 10 | yes | pass |
| f-den=100,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | 0.0101 | 0.0317 | -0.0216 [-0.0217, -0.0215] | -68.1 % | 10 | yes | pass |
| f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 0.0158 | 0.0178 | -0.0019 [-0.0020, -0.0019] | -10.9 % | 10 | yes | pass |
| f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | 0.0082 | 0.0150 | -0.0068 [-0.0069, -0.0067] | -45.5 % | 10 | yes | pass |
| f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | 1.4679 | 1.6324 | -0.1642 [-0.1680, -0.1546] | -10.1 % | 10 | yes | pass |
| f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | 0.1615 | 0.5179 | -0.3564 [-0.3574, -0.3562] | -68.8 % | 10 | yes | pass |
| f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=cpu | 2.1929 | 3.2031 | -1.0098 [-1.0107, -1.0086] | -31.5 % | 10 | yes | pass |
| f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=hbm | 0.2348 | 0.7476 | -0.5127 [-0.5134, -0.5113] | -68.6 % | 10 | yes | pass |
| footprint-mib=1024,generator=rmat,kernel=k4,placement=cpu | 122.9874 | 68.2597 | 54.9185 [54.5613, 55.9934] | +80.5 % | 10 | yes | pass |
| footprint-mib=1024,generator=rmat,kernel=k4,placement=hbm | 34.3583 | 65.0194 | -30.7397 [-31.1672, -30.6365] | -47.3 % | 10 | yes | pass |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,sharing=shared | 30.7987 | 4.1829 | 26.6178 [26.6016, 26.6235] | +636.4 % | 10 | yes | pass |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,sharing=shared | 1.2805 | 1.7679 | -0.4877 [-0.4914, -0.4844] | -27.6 % | 10 | yes | pass |
| footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu | 30.7350 | 4.2036 | 26.5326 [26.5173, 26.5707] | +631.2 % | 10 | yes | pass |
| footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm | 1.2742 | 1.7581 | -0.4838 [-0.4848, -0.4810] | -27.5 % | 10 | yes | pass |
| footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,state=clean,working-set-mib=8 | 0.0440 | 0.0620 | -0.0179 [-0.0183, -0.0174] | -28.9 % | 10 | yes | pass |
| footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,state=dirty,working-set-mib=8 | 0.0621 | 0.0788 | -0.0168 [-0.0175, -0.0164] | -21.3 % | 10 | yes | pass |
| footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,state=evicted,working-set-mib=8 | 0.0432 | 0.0614 | -0.0182 [-0.0190, -0.0175] | -29.7 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.01,working-set-mib=32 | 1.5034 | 0.2034 | 1.3001 [1.2990, 1.3025] | +639.1 % | 30 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.01,working-set-mib=8 | 0.0445 | 0.1479 | -0.1034 [-0.1044, -0.1018] | -69.9 % | 20 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.1,working-set-mib=32 | 1.5097 | 0.6841 | 0.8255 [0.8245, 0.8263] | +120.7 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.1,working-set-mib=8 | 0.0470 | 0.6212 | -0.5741 [-0.5747, -0.5726] | -92.4 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=1,working-set-mib=32 | 1.5013 | 3.1737 | -1.6727 [-1.6746, -1.6712] | -52.7 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=1,working-set-mib=8 | 0.0530 | 3.1206 | -3.0677 [-3.0682, -3.0669] | -98.3 % | 100 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.01,working-set-mib=32 | 1.5014 | 0.3945 | 1.1071 [1.1046, 1.1089] | +280.7 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.01,working-set-mib=8 | 0.0441 | 0.3350 | -0.2909 [-0.2919, -0.2905] | -86.8 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.1,working-set-mib=32 | 1.5205 | 0.7462 | 0.7746 [0.7732, 0.7755] | +103.8 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.1,working-set-mib=8 | 0.0468 | 0.6932 | -0.6464 [-0.6472, -0.6452] | -93.3 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=1,working-set-mib=32 | 1.5132 | 3.2399 | -1.7264 [-1.7279, -1.7258] | -53.3 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=1,working-set-mib=8 | 0.0538 | 3.1739 | -3.1194 [-3.1202, -3.1188] | -98.3 % | 100 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=runs,sharing=shared,w=1,working-set-mib=32 | 1.5156 | 3.0912 | -1.5758 [-1.5797, -1.5735] | -51.0 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=runs,sharing=shared,w=1,working-set-mib=8 | 0.0516 | 3.0232 | -2.9719 [-2.9745, -2.9707] | -98.3 % | 90 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=0.01,working-set-mib=32 | 1.5111 | 0.1932 | 1.3176 [1.3159, 1.3190] | +682.1 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=0.01,working-set-mib=8 | 0.0443 | 0.0645 | -0.0202 [-0.0206, -0.0199] | -31.3 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=0.1,working-set-mib=32 | 1.5021 | 0.1962 | 1.3061 [1.3045, 1.3072] | +665.6 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=0.1,working-set-mib=8 | 0.0527 | 0.0718 | -0.0190 [-0.0197, -0.0183] | -26.4 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=1,working-set-mib=32 | 1.5176 | 0.2027 | 1.3149 [1.3144, 1.3159] | +648.7 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=1,working-set-mib=8 | 0.0546 | 0.0767 | -0.0222 [-0.0228, -0.0219] | -29.0 % | 60 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=0.01,working-set-mib=32 | 0.1051 | 0.2180 | -0.1128 [-0.1133, -0.1124] | -51.7 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=0.1,working-set-mib=32 | 0.1154 | 0.2487 | -0.1334 [-0.1336, -0.1324] | -53.6 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=1,working-set-mib=32 | 0.1287 | 0.9012 | -0.7722 [-0.7756, -0.7712] | -85.7 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=0.01,working-set-mib=32 | 0.1059 | 0.4109 | -0.3052 [-0.3081, -0.3043] | -74.3 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=0.1,working-set-mib=32 | 0.1140 | 0.7298 | -0.6154 [-0.6163, -0.6148] | -84.3 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=1,working-set-mib=32 | 0.1322 | 3.1236 | -2.9913 [-2.9926, -2.9903] | -95.8 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=runs,sharing=shared,w=1,working-set-mib=32 | 0.1321 | 2.6766 | -2.5441 [-2.5451, -2.5431] | -95.0 % | 20 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,sharing=shared,w=0.01,working-set-mib=32 | 0.1050 | 0.1910 | -0.0861 [-0.0887, -0.0852] | -45.1 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,sharing=shared,w=0.1,working-set-mib=32 | 0.1152 | 0.1990 | -0.0837 [-0.0856, -0.0824] | -42.1 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,sharing=shared,w=1,working-set-mib=32 | 0.1302 | 0.2271 | -0.0970 [-0.0993, -0.0960] | -42.7 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.01 | 5.4376 | 0.6038 | 4.8322 [4.8180, 4.8344] | +800.4 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.1 | 5.4223 | 1.0296 | 4.3949 [4.3763, 4.4124] | +426.9 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=1 | 5.3854 | 3.6810 | 1.7049 [1.6916, 1.7085] | +46.3 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.01 | 5.4351 | 0.7924 | 4.6424 [4.6414, 4.6439] | +585.9 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.1 | 5.4345 | 1.1449 | 4.2899 [4.2742, 4.2932] | +374.7 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=1 | 5.3801 | 3.6935 | 1.6871 [1.6849, 1.6887] | +45.7 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=runs,sharing=shared,w=1 | 5.3855 | 3.6208 | 1.7642 [1.7615, 1.7681] | +48.7 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=0.01 | 5.4349 | 3.4626 | 1.9724 [1.9570, 1.9737] | +57.0 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=0.1 | 5.4224 | 3.5178 | 1.9043 [1.8892, 1.9200] | +54.1 % | 10 | yes | pass |
| footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=1 | 5.3990 | 3.6264 | 1.7693 [1.7621, 1.7748] | +48.8 % | 10 | yes | pass |
| footprint-mib=1024,k=1,kernel=k2,placement=cpu,working-set-mib=1024 | 2.9671 | 3.2912 | -0.3243 [-0.3277, -0.3221] | -9.9 % | 10 | yes | pass |
| footprint-mib=1024,k=1,kernel=k2,placement=cpu,working-set-mib=32 | 0.1005 | 0.1326 | -0.0321 [-0.0325, -0.0320] | -24.2 % | 10 | yes | pass |
| footprint-mib=1024,k=1,kernel=k2,placement=hbm,working-set-mib=1024 | 0.3348 | 2.8894 | -2.5545 [-2.5561, -2.5526] | -88.4 % | 10 | yes | pass |
| footprint-mib=1024,k=1,kernel=k2,placement=hbm,working-set-mib=32 | 0.0174 | 0.1179 | -0.1005 [-0.1006, -0.1004] | -85.2 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,rotated=1,working-set-mib=8 | 0.3755 | 0.0764 | 0.2991 [0.2988, 0.2993] | +391.7 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,scope=sys,working-set-mib=8 | 0.4081 | 0.0839 | 0.3241 [0.3232, 0.3250] | +386.4 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,tiling=tiles,working-set-mib=8 | 0.0367 | 0.0605 | -0.0238 [-0.0239, -0.0235] | -39.3 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=1024 | 47.0073 | 8.0943 | 38.9166 [38.8994, 38.9252] | +480.8 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=32 | 1.4823 | 0.1852 | 1.2969 [1.2958, 1.2995] | +700.4 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=8 | 0.0380 | 0.0610 | -0.0230 [-0.0233, -0.0228] | -37.8 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,rotated=1,working-set-mib=8 | 0.0297 | 0.0747 | -0.0449 [-0.0450, -0.0449] | -60.2 % | 20 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,scope=sys,working-set-mib=8 | 0.0384 | 0.0837 | -0.0453 [-0.0453, -0.0451] | -54.1 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,tiling=tiles,working-set-mib=8 | 0.0153 | 0.0583 | -0.0430 [-0.0431, -0.0427] | -73.7 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=1024 | 5.1608 | 5.8133 | -0.6523 [-0.6596, -0.6428] | -11.2 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=32 | 0.0954 | 0.1817 | -0.0862 [-0.0868, -0.0862] | -47.5 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=8 | 0.0161 | 0.0588 | -0.0427 [-0.0431, -0.0426] | -72.6 % | 10 | yes | pass |
| footprint-mib=1024,k=2,kernel=k2,placement=cpu,working-set-mib=1024 | 5.9047 | 3.6135 | 2.2911 [2.2858, 2.2964] | +63.4 % | 10 | yes | pass |
| footprint-mib=1024,k=2,kernel=k2,placement=cpu,working-set-mib=32 | 0.1932 | 0.1318 | 0.0613 [0.0610, 0.0615] | +46.5 % | 10 | yes | pass |
| footprint-mib=1024,k=2,kernel=k2,placement=hbm,working-set-mib=1024 | 0.6590 | 3.2105 | -2.5512 [-2.5538, -2.5505] | -79.5 % | 10 | yes | pass |
| footprint-mib=1024,k=2,kernel=k2,placement=hbm,working-set-mib=32 | 0.0235 | 0.1258 | -0.1023 [-0.1024, -0.1022] | -81.3 % | 20 | yes | pass |
| footprint-mib=1024,k=4,kernel=k2,placement=cpu,working-set-mib=1024 | 11.7663 | 4.2473 | 7.5169 [7.5106, 7.5225] | +177.0 % | 10 | yes | pass |
| footprint-mib=1024,k=4,kernel=k2,placement=cpu,working-set-mib=32 | 0.3776 | 0.1408 | 0.2368 [0.2366, 0.2371] | +168.2 % | 10 | yes | pass |
| footprint-mib=1024,k=4,kernel=k2,placement=hbm,working-set-mib=1024 | 1.3026 | 3.8532 | -2.5512 [-2.5525, -2.5490] | -66.2 % | 10 | yes | pass |
| footprint-mib=1024,k=4,kernel=k2,placement=hbm,working-set-mib=32 | 0.0344 | 0.1339 | -0.0995 [-0.0996, -0.0994] | -74.3 % | 10 | yes | pass |
| footprint-mib=1024,k=64,kernel=k2,placement=cpu,working-set-mib=1024 | 187.8452 | 23.5655 | 164.2872 [164.2697, 164.3021] | +697.2 % | 10 | yes | pass |
| footprint-mib=1024,k=64,kernel=k2,placement=cpu,working-set-mib=32 | 5.9567 | 0.3846 | 5.5725 [5.5672, 5.5742] | +1449.1 % | 10 | yes | pass |
| footprint-mib=1024,k=64,kernel=k2,placement=hbm,working-set-mib=1024 | 20.5905 | 23.1367 | -2.5452 [-2.5791, -2.5265] | -11.0 % | 10 | yes | pass |
| footprint-mib=1024,k=64,kernel=k2,placement=hbm,working-set-mib=32 | 0.3440 | 0.3731 | -0.0294 [-0.0300, -0.0284] | -7.9 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k3,placement=cpu | 5.3701 | 3.4333 | 1.9366 [1.9351, 1.9394] | +56.4 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k3,placement=hbm | 0.4658 | 1.1181 | -0.6525 [-0.6536, -0.6518] | -58.4 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k6,layout=line,placement=cpu,update=atomic | 3.4728 | 6.9026 | -3.4304 [-3.4385, -3.4255] | -49.7 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k6,layout=line,placement=hbm,update=atomic | 0.3402 | 1.6051 | -1.2649 [-1.2660, -1.2620] | -78.8 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=cpu,update=atomic | 6.0664 | 7.4059 | -1.3405 [-1.3456, -1.3360] | -18.1 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=cpu,update=plain | 6.0701 | 7.3313 | -1.2610 [-1.2658, -1.2541] | -17.2 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=cpu,update=returned | 6.1389 | 7.4560 | -1.3169 [-1.3222, -1.3091] | -17.7 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=hbm,update=atomic | 0.8192 | 2.0967 | -1.2776 [-1.2799, -1.2757] | -60.9 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=hbm,update=plain | 0.7689 | 2.0392 | -1.2709 [-1.2730, -1.2667] | -62.3 % | 10 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=hbm,update=returned | 0.8974 | 2.1705 | -1.2730 [-1.2742, -1.2704] | -58.7 % | 10 | yes | pass |
| footprint-mib=11520,kernel=k3,placement=cpu | 240.0613 | 33.1553 | 206.8994 [206.8485, 207.0303] | +624.0 % | 10 | yes | pass |
| footprint-mib=1536,kernel=k3,placement=cpu | 5.3718 | 4.8501 | 0.5214 [0.5192, 0.5223] | +10.8 % | 10 | yes | pass |
| footprint-mib=16,kernel=k6,placement=cpu,update=atomic | 1.5047 | 0.1984 | 1.3063 [1.3054, 1.3067] | +658.4 % | 10 | yes | pass |
| footprint-mib=16,kernel=k6,placement=hbm,update=atomic | 0.0763 | 0.1865 | -0.1101 [-0.1106, -0.1097] | -59.1 % | 10 | yes | pass |
| footprint-mib=16384,generator=uniform,kernel=k4,placement=cpu | 483.3450 | 48.7141 | 434.6353 [434.4942, 434.6591] | +892.2 % | 10 | yes | pass |
| footprint-mib=16384,generator=uniform,kernel=k4,placement=hbm | 32.2475 | 42.3579 | -10.1024 [-10.1915, -10.0838] | -23.9 % | 10 | yes | pass |
| footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,sharing=shared,state=dirty | 7.2255 | 46.0306 | -38.8082 [-38.8199, -38.7982] | -84.3 % | 10 | yes | pass |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.01 | 433.5590 | 2.0225 | 431.5343 [431.4578, 431.5988] | +21336.2 % | 10 | yes | pass |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.1 | 432.8435 | 5.3551 | 427.4839 [427.4479, 427.6448] | +7982.7 % | 10 | yes | pass |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=1 | 433.6450 | 45.7843 | 387.8482 [387.7230, 387.9464] | +847.1 % | 10 | yes | pass |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.01 | 433.5408 | 5.2146 | 428.3205 [428.2626, 428.3773] | +8213.8 % | 40 | yes | pass |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.1 | 433.3461 | 10.5123 | 422.8404 [422.6782, 423.0166] | +4022.3 % | 10 | yes | pass |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=1 | 432.6938 | 49.9291 | 382.7542 [382.6753, 382.8454] | +766.6 % | 10 | yes | pass |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=runs,sharing=shared,w=1 | 433.4054 | 46.7281 | 386.6715 [386.6066, 386.7533] | +827.5 % | 10 | yes | pass |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=0.01 | 432.8441 | 46.3596 | 386.4910 [386.3713, 386.5587] | +833.7 % | 10 | yes | pass |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=0.1 | 433.4816 | 46.7595 | 386.7233 [386.6621, 386.8549] | +827.0 % | 10 | yes | pass |
| footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=1 | 432.7095 | 46.9854 | 385.7315 [385.5933, 385.7799] | +821.0 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,page-order=2m,placement=cpu | 5.3806 | 46.3288 | -40.9482 [-40.9601, -40.9396] | -88.4 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,page-order=2m,placement=hbm | 2.5193 | 10.6071 | -8.0919 [-8.1231, -8.0612] | -76.3 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,page-order=64k,placement=cpu | 5.2187 | 46.5271 | -41.3097 [-41.3371, -41.2977] | -88.8 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,page-order=64k,placement=hbm | 1.6131 | 10.6140 | -8.9997 [-9.0836, -8.9616] | -84.8 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu | 5.3799 | 42.6258 | -37.2455 [-37.4231, -37.2445] | -87.4 % | 40 | yes | pass |
| footprint-mib=16384,kernel=k3,page-size=512m,placement=hbm | 0.4784 | 10.6294 | -10.1508 [-10.1824, -10.1409] | -95.5 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,partition=2g,placement=cpu | 5.8185 | 45.7699 | -39.9429 [-39.9845, -39.9179] | -87.3 % | 20 | yes | pass |
| footprint-mib=16384,kernel=k3,partition=2g,placement=hbm | 284.1852 | 10.8413 | 273.3444 [269.3669, 274.9583] | +2521.3 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,placement=cpu | 432.6893 | 45.4233 | 387.2742 [387.1655, 387.2993] | +852.6 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3,placement=hbm | 426.0208 | 10.6457 | 415.3844 [415.2730, 415.4721] | +3901.9 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3p,page-size=512m,placement=cpu | 0.0990 | 42.1829 | -42.0839 [-42.0867, -42.0815] | -99.8 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k3p,placement=cpu | 7.0248 | 45.8584 | -38.8314 [-38.8393, -38.8298] | -84.7 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k6,placement=cpu,update=atomic | 95.6900 | 116.2522 | -20.5685 [-20.6148, -20.4937] | -17.7 % | 10 | yes | pass |
| footprint-mib=16384,kernel=k6,placement=hbm,update=atomic | 13.1061 | 33.4783 | -20.3665 [-20.4089, -20.3336] | -60.8 % | 10 | yes | pass |
| footprint-mib=2048,kernel=k3,placement=cpu | 5.3734 | 6.2988 | -0.9257 [-0.9285, -0.9227] | -14.7 % | 10 | yes | pass |
| footprint-mib=24576,generator=uniform,kernel=k4,placement=cpu | 752.0696 | 74.2642 | 677.8039 [677.6353, 677.9056] | +912.7 % | 10 | yes | pass |
| footprint-mib=24576,kernel=k3,placement=cpu | 598.2841 | 66.0707 | 532.2243 [531.9709, 532.3374] | +805.5 % | 10 | yes | pass |
| footprint-mib=24576,kernel=k3,placement=hbm | 590.1793 | 15.7007 | 574.4782 [574.2511, 574.5306] | +3658.9 % | 10 | yes | pass |
| footprint-mib=256,generator=uniform,kernel=k4,placement=cpu | 7.3570 | 1.0080 | 6.3487 [6.3431, 6.3582] | +629.8 % | 10 | yes | pass |
| footprint-mib=256,generator=uniform,kernel=k4,placement=hbm | 0.2108 | 0.8858 | -0.6749 [-0.6757, -0.6747] | -76.2 % | 10 | yes | pass |
| footprint-mib=256,kernel=k3,placement=cpu | 5.3641 | 1.2023 | 4.1615 [4.1608, 4.1623] | +346.1 % | 10 | yes | pass |
| footprint-mib=256,kernel=k3,placement=hbm | 0.4258 | 1.0808 | -0.6552 [-0.6560, -0.6543] | -60.6 % | 10 | yes | pass |
| footprint-mib=256,kernel=k6,placement=cpu,update=atomic | 1.5115 | 1.8691 | -0.3571 [-0.3588, -0.3562] | -19.1 % | 10 | yes | pass |
| footprint-mib=256,kernel=k6,placement=hbm,update=atomic | 0.2049 | 0.5334 | -0.3283 [-0.3290, -0.3278] | -61.6 % | 10 | yes | pass |
| footprint-mib=32768,generator=uniform,kernel=k4,placement=cpu | 971.4034 | 91.6185 | 879.6893 [879.5665, 879.9443] | +960.2 % | 10 | yes | pass |
| footprint-mib=32768,kernel=k3,placement=cpu | 684.9744 | 85.7282 | 599.2467 [599.0949, 599.4563] | +699.0 % | 10 | yes | pass |
| footprint-mib=32768,kernel=k6,placement=cpu,update=atomic | 190.3951 | 228.9191 | -38.5291 [-38.6381, -38.3513] | -16.8 % | 10 | yes | pass |
| footprint-mib=4096,generator=uniform,kernel=k4,placement=cpu | 123.6412 | 12.4576 | 111.1800 [111.1472, 111.2385] | +892.5 % | 10 | yes | pass |
| footprint-mib=4096,generator=uniform,kernel=k4,placement=hbm | 7.0776 | 9.5820 | -2.5052 [-2.5097, -2.4966] | -26.1 % | 10 | yes | pass |
| footprint-mib=4096,kernel=k3,placement=cpu | 5.5318 | 11.9555 | -6.4296 [-6.4500, -6.3967] | -53.8 % | 10 | yes | pass |
| footprint-mib=4096,kernel=k3,placement=hbm | 5.1265 | 3.0277 | 2.0997 [2.0885, 2.1028] | +69.3 % | 10 | yes | pass |
| footprint-mib=4096,kernel=k6,placement=cpu,update=atomic | 24.2056 | 26.3191 | -2.1239 [-2.1343, -2.1004] | -8.1 % | 10 | yes | pass |
| footprint-mib=4096,kernel=k6,placement=hbm,update=atomic | 3.2754 | 8.3725 | -5.0966 [-5.1053, -5.0931] | -60.9 % | 10 | yes | pass |
| footprint-mib=512,host=reads,kernel=k5,placement=cpu,sharing=shared,sweeps=8,tiling=tiles | 26.6195 | 6.5031 | 20.1176 [20.1066, 20.1376] | +309.4 % | 10 | yes | pass |
| footprint-mib=512,host=reads,kernel=k5,placement=hbm,sharing=shared,sweeps=8,tiling=tiles | 3.2667 | 3.8621 | -0.5952 [-0.6016, -0.5879] | -15.4 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=0.01 | 26.5773 | 5.0981 | 21.4790 [21.4502, 21.5269] | +421.3 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=0.1 | 26.5879 | 5.3231 | 21.2617 [21.2460, 21.2764] | +399.4 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=1 | 26.8550 | 6.7051 | 20.1549 [20.1239, 20.1763] | +300.6 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=0.01 | 26.0797 | 5.1956 | 20.8834 [20.8665, 20.9213] | +401.9 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=0.1 | 26.0422 | 5.3761 | 20.6658 [20.6336, 20.7355] | +384.4 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=1 | 26.3405 | 6.6636 | 19.6754 [19.6219, 19.7374] | +295.3 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=runs,sharing=shared,sweeps=8,tiling=tiles,w=1 | 26.1940 | 6.6179 | 19.5791 [19.5414, 19.6072] | +295.9 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sharing=shared,sweeps=8,tiling=tiles,w=0.01 | 26.1801 | 6.5036 | 19.6711 [19.6552, 19.7374] | +302.5 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sharing=shared,sweeps=8,tiling=tiles,w=0.1 | 26.7675 | 6.5461 | 20.2202 [20.1783, 20.2670] | +308.9 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sharing=shared,sweeps=8,tiling=tiles,w=1 | 26.1533 | 6.6870 | 19.4606 [19.4163, 19.4913] | +291.0 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=0.01 | 3.5968 | 3.6237 | -0.0274 [-0.0290, -0.0255] | -0.8 % | 30 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=0.1 | 3.4826 | 3.6614 | -0.1800 [-0.1866, -0.1705] | -4.9 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=1 | 3.4833 | 3.9936 | -0.5086 [-0.5206, -0.5046] | -12.7 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=0.01 | 3.6120 | 3.6982 | -0.0873 [-0.0925, -0.0786] | -2.4 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=0.1 | 3.5775 | 3.8624 | -0.2847 [-0.2858, -0.2750] | -7.4 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=1 | 3.5558 | 5.0457 | -1.4916 [-1.4956, -1.4833] | -29.6 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=runs,sharing=shared,sweeps=8,tiling=tiles,w=1 | 3.4825 | 4.8345 | -1.3514 [-1.3581, -1.3478] | -28.0 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sharing=shared,sweeps=8,tiling=tiles,w=0.01 | 3.4851 | 3.8737 | -0.3897 [-0.3924, -0.3851] | -10.1 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sharing=shared,sweeps=8,tiling=tiles,w=0.1 | 3.5904 | 3.8771 | -0.2882 [-0.2907, -0.2826] | -7.4 % | 10 | yes | pass |
| footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sharing=shared,sweeps=8,tiling=tiles,w=1 | 3.5684 | 3.9874 | -0.4181 [-0.4282, -0.4088] | -10.5 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=1,tiling=tiles | 3.7291 | 3.6970 | 0.0319 [0.0307, 0.0346] | +0.9 % | 20 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=16,tiling=tiles | 52.8800 | 9.6978 | 43.1837 [43.1409, 43.2503] | +445.3 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=2,tiling=tiles | 6.7906 | 4.0881 | 2.7008 [2.6974, 2.7058] | +66.1 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=4,tiling=tiles | 13.3525 | 4.9098 | 8.4431 [8.4261, 8.4697] | +172.0 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=64,tiling=tiles | 210.8980 | 29.0199 | 181.8770 [181.7972, 181.9518] | +626.7 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=none | 41.9177 | 6.0276 | 35.8908 [35.8003, 35.9087] | +595.4 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles | 26.4473 | 6.4979 | 19.9472 [19.9331, 19.9841] | +307.0 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=hbm,sweeps=1,tiling=tiles | 0.3990 | 1.0474 | -0.6484 [-0.6494, -0.6472] | -61.9 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=hbm,sweeps=16,tiling=tiles | 6.5416 | 7.0994 | -0.5564 [-0.5688, -0.5483] | -7.8 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=hbm,sweeps=2,tiling=tiles | 0.8135 | 1.4521 | -0.6383 [-0.6394, -0.6368] | -44.0 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=hbm,sweeps=4,tiling=tiles | 1.6299 | 2.2551 | -0.6253 [-0.6272, -0.6230] | -27.7 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=hbm,sweeps=64,tiling=tiles | 25.8874 | 26.3672 | -0.4776 [-0.5156, -0.4497] | -1.8 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=none | 2.7539 | 3.3948 | -0.6410 [-0.6505, -0.6310] | -18.9 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles | 3.2590 | 3.8840 | -0.6268 [-0.6329, -0.6214] | -16.1 % | 10 | yes | pass |
| footprint-mib=64,kernel=k6,placement=cpu,update=atomic | 1.5067 | 0.5951 | 0.9116 [0.9108, 0.9127] | +153.2 % | 10 | yes | pass |
| footprint-mib=64,kernel=k6,placement=hbm,update=atomic | 0.1641 | 0.2593 | -0.0951 [-0.0953, -0.0950] | -36.7 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1,placement=cpu | 191.3110 | 12.3706 | 178.9417 [178.9378, 179.2855] | +1446.5 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1,placement=hbm | 12.5381 | 12.3655 | 0.1727 [0.1717, 0.1744] | +1.4 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1024,placement=cpu | 12.4843 | 0.8408 | 11.6433 [11.6390, 11.6507] | +1384.7 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1024,placement=hbm | 0.7661 | 0.8342 | -0.0681 [-0.0689, -0.0669] | -8.2 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1048576,placement=cpu | 8.6579 | 0.2488 | 8.4091 [8.4000, 8.4123] | +3379.9 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1048576,placement=hbm | 0.1903 | 0.2445 | -0.0541 [-0.0544, -0.0526] | -22.1 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=16,placement=cpu | 82.2375 | 5.1160 | 77.1211 [77.1190, 77.1238] | +1507.5 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=16,placement=hbm | 5.0292 | 5.0457 | -0.0166 [-0.0173, -0.0162] | -0.3 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=256,placement=cpu | 48.6807 | 2.7676 | 45.9128 [45.9060, 45.9278] | +1659.0 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=256,placement=hbm | 2.6872 | 2.7033 | -0.0161 [-0.0165, -0.0154] | -0.6 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=4096,placement=cpu | 6.2089 | 0.3400 | 5.8688 [5.8656, 5.8791] | +1725.9 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=4096,placement=hbm | 0.2665 | 0.2803 | -0.0139 [-0.0140, -0.0138] | -5.0 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=65536,placement=cpu | 4.3332 | 0.2641 | 4.0689 [4.0683, 4.0701] | +1540.9 % | 10 | yes | pass |
| footprint-mib=8,kernel=k6,keys=65536,placement=hbm | 0.1930 | 0.2073 | -0.0143 [-0.0144, -0.0143] | -6.9 % | 10 | yes | pass |
| footprint-mib=8192,generator=rmat,kernel=k4,placement=cpu | 999.4046 | 415.2754 | 584.1203 [578.6142, 589.6582] | +140.7 % | 10 | yes | pass |
| footprint-mib=8192,generator=rmat,kernel=k4,placement=hbm | 395.6738 | 397.8027 | -2.1224 [-2.2423, -2.0335] | -0.5 % | 10 | yes | pass |
| footprint-mib=8192,generator=uniform,kernel=k4,placement=cpu | 247.2914 | 24.8986 | 222.3829 [222.2842, 222.4181] | +893.2 % | 10 | yes | pass |
| footprint-mib=8192,generator=uniform,kernel=k4,placement=hbm | 15.0957 | 20.2289 | -5.1299 [-5.2066, -5.1049] | -25.4 % | 10 | yes | pass |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=0.01 | 8.1119 | 1.2370 | 6.8743 [6.8691, 6.8808] | +555.7 % | 10 | yes | pass |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=0.1 | 8.0972 | 1.7195 | 6.3776 [6.3692, 6.3868] | +370.9 % | 10 | yes | pass |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=1 | 8.0958 | 5.7428 | 2.3536 [2.3428, 2.3686] | +41.0 % | 10 | yes | pass |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=0.01 | 8.1037 | 2.8935 | 5.2107 [5.1946, 5.2175] | +180.1 % | 20 | yes | pass |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=0.1 | 8.0988 | 5.3886 | 2.7086 [2.6997, 2.7122] | +50.3 % | 10 | yes | pass |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=1 | 8.1216 | 24.4214 | -16.3024 [-16.3177, -16.2900] | -66.8 % | 10 | yes | pass |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=runs,sharing=shared,w=1 | 8.1143 | 20.9666 | -12.8521 [-12.8575, -12.8404] | -61.3 % | 10 | yes | pass |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,sharing=shared,w=0.01 | 8.1020 | 5.6287 | 2.4737 [2.4611, 2.4988] | +43.9 % | 10 | yes | pass |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,sharing=shared,w=0.1 | 8.0912 | 5.6145 | 2.4764 [2.4727, 2.4819] | +44.1 % | 10 | yes | pass |
| footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,sharing=shared,w=1 | 8.1100 | 5.7651 | 2.3437 [2.3324, 2.3652] | +40.7 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu | 7.7449 | 23.4978 | -15.7533 [-15.7636, -15.7459] | -67.0 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=hbm | 7.8161 | 5.5663 | 2.2492 [2.2366, 2.2589] | +40.4 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k6,placement=cpu,update=atomic | 48.0254 | 58.7402 | -10.7164 [-10.7768, -10.7054] | -18.2 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k6,placement=hbm,update=atomic | 6.5706 | 16.7853 | -10.2083 [-10.2458, -10.1716] | -60.8 % | 10 | yes | pass |
| footprint-mib=9728,kernel=k3,placement=cpu | 128.4402 | 27.3152 | 101.0945 [101.0639, 101.2340] | +370.1 % | 10 | yes | pass |

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

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 39.4 GB/s over the touched lines; buffer at 0x4a4020000000 (offset in its 16 GiB window: 536870912 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 22.9998 ms, kernel 0.4985 ms, copy-out 0.0132 ms; source buffer at 0x4a4820000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (36.2 per touched line), copy 8.607e+09; SMMU translation requests per repetition: direct 1.358e+07, copy 1.311e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 7 passes per interval, 370.2 GB/s over the touched lines; buffer at 0x577340000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9660 ms, kernel 0.2983 ms, copy-out 0.0128 ms; source buffer at 0x577440000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+09 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 67 passes per interval, 3591.3 GB/s over the touched lines; buffer at 0x5d1c40000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 22 calls per interval; first call of an interval: copy-in 0.8966 ms, kernel 0.0406 ms, copy-out 0.0117 ms; source buffer at 0x5d1d40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 374.7 GB/s over the touched lines; buffer at 0x4f6a80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 46.0255 ms, kernel 0.0827 ms, copy-out 0.0143 ms; source buffer at 0x4f6f00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.718e+10 (128.0 per touched line), copy 1.718e+10; SMMU translation requests per repetition: direct 2.716e+05, copy 2.622e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=hbm

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 2997.8 GB/s over the touched lines; buffer at 0x43a3c0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 14.5059 ms, kernel 0.1283 ms, copy-out 0.0135 ms; source buffer at 0x43a840000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 7.076e+05, copy 4.853e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=19456,kernel=k1,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 377.0 GB/s over the touched lines; buffer at 0x5b8780000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 55.1552 ms, kernel 0.0805 ms, copy-out 0.0157 ms; source buffer at 0x5b8cc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.04e+10 (128.0 per touched line), copy 2.04e+10; SMMU translation requests per repetition: direct 3.216e+05, copy 3.113e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=23296,kernel=k1,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 378.5 GB/s over the touched lines; buffer at 0x56c200000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 64.9324 ms, kernel 0.0819 ms, copy-out 0.0161 ms; source buffer at 0x56c840000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.443e+10 (128.0 per touched line), copy 2.443e+10; SMMU translation requests per repetition: direct 3.841e+05, copy 3.728e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 377.4 GB/s over the touched lines; buffer at 0x5fe780000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 66.3597 ms, kernel 0.0849 ms, copy-out 0.0132 ms; source buffer at 0x5fee00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.577e+10 (128.0 per touched line), copy 2.577e+10; SMMU translation requests per repetition: direct 4.073e+05, copy 3.932e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=hbm

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 2702.4 GB/s over the touched lines; buffer at 0x527fc0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 22.5732 ms, kernel 0.0408 ms, copy-out 0.0127 ms; source buffer at 0x528640000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.141e+06, copy 1.021e+06; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 28 passes per interval, 367.2 GB/s over the touched lines; buffer at 0x5c80c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 24 calls per interval; first call of an interval: copy-in 0.7724 ms, kernel 0.0803 ms, copy-out 0.0135 ms; source buffer at 0x5c81c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.684e+08 (128.0 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 0, copy 4110; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 255 passes per interval, 3427.9 GB/s over the touched lines; buffer at 0x5193c0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 28 calls per interval; first call of an interval: copy-in 0.6478 ms, kernel 0.0815 ms, copy-out 0.0131 ms; source buffer at 0x519440000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 4110; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 379.8 GB/s over the touched lines; buffer at 0x5673c0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 85.7226 ms, kernel 0.0834 ms, copy-out 0.0165 ms; source buffer at 0x567c40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.436e+10 (128.0 per touched line), copy 3.436e+10; SMMU translation requests per repetition: direct 5.426e+05, copy 5.243e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 367.2 GB/s over the touched lines; buffer at 0x58b640000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 11.4412 ms, kernel 1.1663 ms, copy-out 0.0146 ms; source buffer at 0x58b800000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 4.295e+09 (128.0 per touched line), copy 4.295e+09; SMMU translation requests per repetition: direct 0, copy 6.555e+04; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=hbm

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 18 passes per interval, 3655.8 GB/s over the touched lines; buffer at 0x4b8b40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 3.6266 ms, kernel 0.0405 ms, copy-out 0.0137 ms; source buffer at 0x4b8d00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 984.7, copy 3658; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,sharing=shared,state=clean

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 351.3 GB/s over the touched lines; buffer at 0x5bb1c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.2132 ms, kernel 0.0272 ms, copy-out 0.0112 ms; source buffer at 0x5bb280000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.711e+07 (128.0 per touched line), copy 6.711e+07; SMMU translation requests per repetition: direct 0, copy 1035; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,sharing=shared,state=dirty

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 208.7 GB/s over the touched lines; buffer at 0x4c0600000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.3254 ms, kernel 0.0271 ms, copy-out 0.0106 ms; source buffer at 0x4c06c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.711e+07 (128.0 per touched line), copy 6.711e+07; SMMU translation requests per repetition: direct 38.28, copy 1037; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,sharing=shared,state=evicted

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 352.3 GB/s over the touched lines; buffer at 0x5f51c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.2099 ms, kernel 0.0260 ms, copy-out 0.0112 ms; source buffer at 0x5f5240000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.711e+07 (128.0 per touched line), copy 6.711e+07; SMMU translation requests per repetition: direct 0, copy 1036; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,sharing=shared,state=clean

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 727.6 GB/s over the touched lines; buffer at 0x486240000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1092 ms, kernel 0.0260 ms, copy-out 0.0140 ms; source buffer at 0x486300000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 2711, copy 2304; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,sharing=shared,state=dirty

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 545.3 GB/s over the touched lines; buffer at 0x47b0c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1415 ms, kernel 0.0240 ms, copy-out 0.0146 ms; source buffer at 0x47b180000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 2552, copy 2056; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,sharing=shared,state=evicted

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 1884.7 GB/s over the touched lines; buffer at 0x43edc0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.0634 ms, kernel 0.0242 ms, copy-out 0.0155 ms; source buffer at 0x43ee80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 2833, copy 3897; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 369.1 GB/s over the touched lines; buffer at 0x4c6740000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 23.1355 ms, kernel 0.0848 ms, copy-out 0.0136 ms; source buffer at 0x4c69c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.59e+09 (128.0 per touched line), copy 8.59e+09; SMMU translation requests per repetition: direct 2.732e+04, copy 1.311e+05; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=hbm

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 9 passes per interval, 3569.5 GB/s over the touched lines; buffer at 0x5c3600000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 7.4909 ms, kernel 0.0428 ms, copy-out 0.0139 ms; source buffer at 0x5c38c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 3.776e+04, copy 1.712e+05; multiplexed rows voided: 0

### route/f-den=10,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 67 passes per interval, 358.5 GB/s over the touched lines; buffer at 0x450d40000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 56 calls per interval; first call of an interval: copy-in 0.3353 ms, kernel 0.0189 ms, copy-out 0.0136 ms; source buffer at 0x450e80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+08 (128.0 per touched line), copy 1.074e+08; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/f-den=10,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 526 passes per interval, 2801.3 GB/s over the touched lines; buffer at 0x40ac40000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 162 calls per interval; first call of an interval: copy-in 0.0731 ms, kernel 0.0456 ms, copy-out 0.0160 ms; source buffer at 0x40ad00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 8 passes per interval, 365.6 GB/s over the touched lines; buffer at 0x462600000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9664 ms, kernel 0.2760 ms, copy-out 0.0129 ms; source buffer at 0x462700000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 9.664e+08 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=hbm

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 73 passes per interval, 3497.9 GB/s over the touched lines; buffer at 0x4980c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 23 calls per interval; first call of an interval: copy-in 0.8296 ms, kernel 0.0381 ms, copy-out 0.0103 ms; source buffer at 0x498180000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/f-den=100,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 527 passes per interval, 281.1 GB/s over the touched lines; buffer at 0x488200000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 386 calls per interval; first call of an interval: copy-in 0.0425 ms, kernel 0.0078 ms, copy-out 0.0132 ms; source buffer at 0x4882c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+07 (128.0 per touched line), copy 1.074e+07; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/f-den=100,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1974 passes per interval, 1062.2 GB/s over the touched lines; buffer at 0x4a1a00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 622 calls per interval; first call of an interval: copy-in 0.0154 ms, kernel 0.0080 ms, copy-out 0.0114 ms; source buffer at 0x4a1b00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1266 passes per interval, 67.9 GB/s over the touched lines; buffer at 0x5f8780000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 1138 calls per interval; first call of an interval: copy-in 0.0151 ms, kernel 0.0074 ms, copy-out 0.0049 ms; source buffer at 0x5f8880000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+06 (128.0 per touched line), copy 1.074e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 2521 passes per interval, 131.6 GB/s over the touched lines; buffer at 0x4dd0c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 1394 calls per interval; first call of an interval: copy-in 0.0115 ms, kernel 0.0076 ms, copy-out 0.0047 ms; source buffer at 0x4dd180000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 365.8 GB/s over the touched lines; buffer at 0x5a9e80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 13 calls per interval; first call of an interval: copy-in 1.5326 ms, kernel 0.0610 ms, copy-out 0.0128 ms; source buffer at 0x5a9f80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (128.0 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 125 passes per interval, 3323.3 GB/s over the touched lines; buffer at 0x42da00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 39 calls per interval; first call of an interval: copy-in 0.4884 ms, kernel 0.0252 ms, copy-out 0.0121 ms; source buffer at 0x42db00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 10 passes per interval, 367.2 GB/s over the touched lines; buffer at 0x5cde00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9666 ms, kernel 0.2328 ms, copy-out 0.0134 ms; source buffer at 0x5cdec0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.053e+08 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=hbm

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 86 passes per interval, 3429.5 GB/s over the touched lines; buffer at 0x49ec40000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 27 calls per interval; first call of an interval: copy-in 0.7046 ms, kernel 0.0352 ms, copy-out 0.0145 ms; source buffer at 0x49ed40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=rmat,kernel=k4,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 8.7 GB/s over the touched lines; buffer at 0x4c4a00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 3.0159 ms, kernel 65.1222 ms, copy-out 0.1221 ms; source buffer at 0x4c4b00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.139e+09 (374.2 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.689e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=rmat,kernel=k4,placement=hbm

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 31.3 GB/s over the touched lines; buffer at 0x425080000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 0.6365 ms, kernel 64.3634 ms, copy-out 0.0181 ms; source buffer at 0x425180000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,sharing=shared

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 34.9 GB/s over the touched lines; buffer at 0x4d4500000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 2.9684 ms, kernel 1.1047 ms, copy-out 0.1204 ms; source buffer at 0x4d4640000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.203e+09 (381.8 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.689e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,sharing=shared

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 16 passes per interval, 838.6 GB/s over the touched lines; buffer at 0x5d4900000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 12 calls per interval; first call of an interval: copy-in 0.6490 ms, kernel 1.1133 ms, copy-out 0.0182 ms; source buffer at 0x5d4a40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 34.9 GB/s over the touched lines; buffer at 0x5375c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 2.9868 ms, kernel 1.1047 ms, copy-out 0.1195 ms; source buffer at 0x5376c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.202e+09 (381.7 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.689e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 16 passes per interval, 842.7 GB/s over the touched lines; buffer at 0x5c9c40000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 12 calls per interval; first call of an interval: copy-in 0.6377 ms, kernel 1.1082 ms, copy-out 0.0186 ms; source buffer at 0x5c9d40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,state=clean,working-set-mib=8

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 190.5 GB/s over the touched lines; buffer at 0x4e62c0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.0439 ms, kernel 0.0164 ms, copy-out 0.0125 ms; source buffer at 0x4e63c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 311.2, copy 130.7; multiplexed rows voided: 0

### route/footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,state=dirty,working-set-mib=8

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 135.0 GB/s over the touched lines; buffer at 0x4cedc0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.0570 ms, kernel 0.0163 ms, copy-out 0.0156 ms; source buffer at 0x4ceec0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 306.1, copy 144.7; multiplexed rows voided: 0

### route/footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,state=evicted,working-set-mib=8

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 193.9 GB/s over the touched lines; buffer at 0x5e46c0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.0411 ms, kernel 0.0164 ms, copy-out 0.0117 ms; source buffer at 0x5e47c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 0, copy 130.3; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.01,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.3 GB/s over the touched lines; buffer at 0x499f00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1239 ms, kernel 0.0730 ms, copy-out 0.0160 ms; source buffer at 0x49a000000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.365e+08 (2047.5 per touched line), copy 1.074e+07; SMMU translation requests per repetition: direct 798.2, copy 2.772e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.01,working-set-mib=8

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 188.2 GB/s over the touched lines; buffer at 0x511340000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1239 ms, kernel 0.0174 ms, copy-out 0.0175 ms; source buffer at 0x511440000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 1.074e+07; SMMU translation requests per repetition: direct 335.5, copy 2.756e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.1,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.2 GB/s over the touched lines; buffer at 0x50fe80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 34 calls per interval; first call of an interval: copy-in 0.5648 ms, kernel 0.0870 ms, copy-out 0.0169 ms; source buffer at 0x50ff80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.365e+08 (2047.5 per touched line), copy 1.074e+08; SMMU translation requests per repetition: direct 393.8, copy 1.955e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.1,working-set-mib=8

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 178.2 GB/s over the touched lines; buffer at 0x419980000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 42 calls per interval; first call of an interval: copy-in 0.5623 ms, kernel 0.0187 ms, copy-out 0.0150 ms; source buffer at 0x419a80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 1.074e+08; SMMU translation requests per repetition: direct 330.6, copy 8440; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=1,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.3 GB/s over the touched lines; buffer at 0x4e0180000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 3.0655 ms, kernel 0.0859 ms, copy-out 0.0158 ms; source buffer at 0x4e0240000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.366e+08 (2047.9 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=1,working-set-mib=8

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 158.2 GB/s over the touched lines; buffer at 0x4e54c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 3.0719 ms, kernel 0.0185 ms, copy-out 0.0139 ms; source buffer at 0x4e5580000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 28.52, copy 0; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.01,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.3 GB/s over the touched lines; buffer at 0x48fc80000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.3080 ms, kernel 0.0727 ms, copy-out 0.0162 ms; source buffer at 0x48fd80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.365e+08 (2047.6 per touched line), copy 1.074e+07; SMMU translation requests per repetition: direct 727.1, copy 6.034e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.01,working-set-mib=8

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 189.9 GB/s over the touched lines; buffer at 0x526fc0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.3083 ms, kernel 0.0174 ms, copy-out 0.0154 ms; source buffer at 0x5270c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 1.074e+07; SMMU translation requests per repetition: direct 332.1, copy 5.743e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.1,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.1 GB/s over the touched lines; buffer at 0x594300000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 28 calls per interval; first call of an interval: copy-in 0.6707 ms, kernel 0.0739 ms, copy-out 0.0148 ms; source buffer at 0x5943c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.365e+08 (2047.5 per touched line), copy 1.074e+08; SMMU translation requests per repetition: direct 497, copy 5.07e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.1,working-set-mib=8

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 179.0 GB/s over the touched lines; buffer at 0x4d53c0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 30 calls per interval; first call of an interval: copy-in 0.6756 ms, kernel 0.0174 ms, copy-out 0.0144 ms; source buffer at 0x4d5480000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 1.074e+08; SMMU translation requests per repetition: direct 329.4, copy 5.105e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=1,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.2 GB/s over the touched lines; buffer at 0x5b5cc0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 3.1465 ms, kernel 0.0788 ms, copy-out 0.0172 ms; source buffer at 0x5b5dc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.366e+08 (2047.8 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.639e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=1,working-set-mib=8

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 155.8 GB/s over the touched lines; buffer at 0x4e8300000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 3.1442 ms, kernel 0.0177 ms, copy-out 0.0130 ms; source buffer at 0x4e8400000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 315.9, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=runs,sharing=shared,w=1,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.1 GB/s over the touched lines; buffer at 0x409740000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9997 ms, kernel 0.0787 ms, copy-out 0.0153 ms; source buffer at 0x409840000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.365e+08 (2047.7 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.643e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=runs,sharing=shared,w=1,working-set-mib=8

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 162.3 GB/s over the touched lines; buffer at 0x5f9500000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9828 ms, kernel 0.0178 ms, copy-out 0.0128 ms; source buffer at 0x5f9600000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 311.2, copy 1.646e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=0.01,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.2 GB/s over the touched lines; buffer at 0x435e80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1097 ms, kernel 0.0760 ms, copy-out 0.0175 ms; source buffer at 0x435f80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.365e+08 (2047.7 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 685.2, copy 541.4; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=0.01,working-set-mib=8

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 189.2 GB/s over the touched lines; buffer at 0x547f00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.0449 ms, kernel 0.0163 ms, copy-out 0.0135 ms; source buffer at 0x547fc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 330.3, copy 164.2; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=0.1,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.3 GB/s over the touched lines; buffer at 0x576280000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1257 ms, kernel 0.0759 ms, copy-out 0.0134 ms; source buffer at 0x576380000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.366e+08 (2047.7 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 296.6, copy 542.8; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=0.1,working-set-mib=8

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 158.9 GB/s over the touched lines; buffer at 0x5de540000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.0570 ms, kernel 0.0164 ms, copy-out 0.0142 ms; source buffer at 0x5de680000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 318.6, copy 150.6; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=1,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.1 GB/s over the touched lines; buffer at 0x4496c0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1222 ms, kernel 0.0755 ms, copy-out 0.0147 ms; source buffer at 0x4497c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.365e+08 (2047.5 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 61.79, copy 533.2; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,sharing=shared,w=1,working-set-mib=8

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 153.5 GB/s over the touched lines; buffer at 0x49df00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.0528 ms, kernel 0.0163 ms, copy-out 0.0150 ms; source buffer at 0x49dfc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 314.4, copy 132; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=0.01,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 319.0 GB/s over the touched lines; buffer at 0x4a3000000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1271 ms, kernel 0.0854 ms, copy-out 0.0138 ms; source buffer at 0x4a3140000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 948.7, copy 2.918e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=0.1,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 290.5 GB/s over the touched lines; buffer at 0x400980000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1610 ms, kernel 0.0865 ms, copy-out 0.0166 ms; source buffer at 0x400a80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 951.6, copy 3.047e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=1,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 260.7 GB/s over the touched lines; buffer at 0x5c8440000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 24 calls per interval; first call of an interval: copy-in 0.8115 ms, kernel 0.0851 ms, copy-out 0.0162 ms; source buffer at 0x5c8540000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 955.9, copy 3.84e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=0.01,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 316.7 GB/s over the touched lines; buffer at 0x5eeb00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 49 calls per interval; first call of an interval: copy-in 0.3351 ms, kernel 0.0872 ms, copy-out 0.0165 ms; source buffer at 0x5eec00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 952.6, copy 5.862e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=0.1,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 294.3 GB/s over the touched lines; buffer at 0x556e00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 28 calls per interval; first call of an interval: copy-in 0.6710 ms, kernel 0.0923 ms, copy-out 0.0150 ms; source buffer at 0x556f00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 949.5, copy 4.82e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=1,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 253.7 GB/s over the touched lines; buffer at 0x585c00000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 3.0113 ms, kernel 0.1053 ms, copy-out 0.0172 ms; source buffer at 0x585d00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 950.2, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=runs,sharing=shared,w=1,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 253.9 GB/s over the touched lines; buffer at 0x5b5240000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 8 calls per interval; first call of an interval: copy-in 2.5702 ms, kernel 0.1057 ms, copy-out 0.0164 ms; source buffer at 0x5b5340000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 957.6, copy 1.644e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,sharing=shared,w=0.01,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 319.5 GB/s over the touched lines; buffer at 0x5b5700000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1022 ms, kernel 0.0874 ms, copy-out 0.0121 ms; source buffer at 0x5b5800000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 948.2, copy 547.5; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,sharing=shared,w=0.1,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 291.0 GB/s over the touched lines; buffer at 0x578900000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1065 ms, kernel 0.0938 ms, copy-out 0.0138 ms; source buffer at 0x5789c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 958.6, copy 547.3; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,sharing=shared,w=1,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 257.7 GB/s over the touched lines; buffer at 0x4e0800000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 0.1154 ms, kernel 0.1095 ms, copy-out 0.0131 ms; source buffer at 0x4e08c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 924, copy 550.9; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.01

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 170.7 GB/s over the touched lines; buffer at 0x4b9a40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 34 calls per interval; first call of an interval: copy-in 0.1253 ms, kernel 0.4713 ms, copy-out 0.0162 ms; source buffer at 0x4b9b40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+07; SMMU translation requests per repetition: direct 1.739e+04, copy 2.849e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.1

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 171.2 GB/s over the touched lines; buffer at 0x41e6c0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 21 calls per interval; first call of an interval: copy-in 0.5384 ms, kernel 0.4777 ms, copy-out 0.0179 ms; source buffer at 0x41e7c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+08; SMMU translation requests per repetition: direct 1.307e+04, copy 2.53e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=1

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 172.4 GB/s over the touched lines; buffer at 0x489bc0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 3.1980 ms, kernel 0.4772 ms, copy-out 0.0142 ms; source buffer at 0x489cc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.01

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 170.8 GB/s over the touched lines; buffer at 0x47d840000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 26 calls per interval; first call of an interval: copy-in 0.3142 ms, kernel 0.4705 ms, copy-out 0.0140 ms; source buffer at 0x47d940000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+07; SMMU translation requests per repetition: direct 1.743e+04, copy 5.894e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.1

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 170.8 GB/s over the touched lines; buffer at 0x545dc0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 18 calls per interval; first call of an interval: copy-in 0.6720 ms, kernel 0.4723 ms, copy-out 0.0145 ms; source buffer at 0x545ec0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+08; SMMU translation requests per repetition: direct 1.735e+04, copy 5.097e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=1

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 172.6 GB/s over the touched lines; buffer at 0x401c80000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 3.2073 ms, kernel 0.4779 ms, copy-out 0.0148 ms; source buffer at 0x401dc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=runs,sharing=shared,w=1

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 172.4 GB/s over the touched lines; buffer at 0x5723c0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 3.1348 ms, kernel 0.4762 ms, copy-out 0.0140 ms; source buffer at 0x572480000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.654e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=0.01

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 170.8 GB/s over the touched lines; buffer at 0x5da440000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 2.9849 ms, kernel 0.4711 ms, copy-out 0.0145 ms; source buffer at 0x5da540000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 1.737e+04, copy 1.641e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=0.1

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 171.2 GB/s over the touched lines; buffer at 0x400a80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 3.0428 ms, kernel 0.4720 ms, copy-out 0.0140 ms; source buffer at 0x400b40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 1.31e+04, copy 1.641e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=1

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 171.9 GB/s over the touched lines; buffer at 0x4b8d80000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 3.1475 ms, kernel 0.4790 ms, copy-out 0.0138 ms; source buffer at 0x4b8e80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.657e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=1,kernel=k2,placement=cpu,working-set-mib=1024

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 7 passes per interval, 361.9 GB/s over the touched lines; buffer at 0x59c4c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.9488 ms, kernel 0.3339 ms, copy-out 0.0125 ms; source buffer at 0x59c580000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+09 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=1,kernel=k2,placement=cpu,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 198 passes per interval, 333.8 GB/s over the touched lines; buffer at 0x573080000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 156 calls per interval; first call of an interval: copy-in 0.1104 ms, kernel 0.0149 ms, copy-out 0.0153 ms; source buffer at 0x573180000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.354e+07 (128.0 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 532.9; multiplexed rows voided: 0

### route/footprint-mib=1024,k=1,kernel=k2,placement=hbm,working-set-mib=1024

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 60 passes per interval, 3206.7 GB/s over the touched lines; buffer at 0x552540000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.5433 ms, kernel 0.3380 ms, copy-out 0.0133 ms; source buffer at 0x552600000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=1,kernel=k2,placement=hbm,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1151 passes per interval, 1927.0 GB/s over the touched lines; buffer at 0x4ba000000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 171 calls per interval; first call of an interval: copy-in 0.0964 ms, kernel 0.0223 ms, copy-out 0.0124 ms; source buffer at 0x4ba0c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 518.5; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,rotated=1,working-set-mib=8

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 54 passes per interval, 22.3 GB/s over the touched lines; buffer at 0x56f440000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 267 calls per interval; first call of an interval: copy-in 0.0391 ms, kernel 0.0304 ms, copy-out 0.0115 ms; source buffer at 0x56f540000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.341e+08 (2048.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 0, copy 132.6; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,scope=sys,working-set-mib=8

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 20.5 GB/s over the touched lines; buffer at 0x52fc40000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 238 calls per interval; first call of an interval: copy-in 0.0379 ms, kernel 0.0382 ms, copy-out 0.0101 ms; source buffer at 0x52fd40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.341e+08 (2048.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 0, copy 132.6; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,tiling=tiles,working-set-mib=8

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 544 passes per interval, 228.2 GB/s over the touched lines; buffer at 0x4fa0c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 328 calls per interval; first call of an interval: copy-in 0.0403 ms, kernel 0.0155 ms, copy-out 0.0144 ms; source buffer at 0x4fa1c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.38e+06 (128.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 0, copy 132.6; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=1024

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 22.8 GB/s over the touched lines; buffer at 0x431cc0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 2.9307 ms, kernel 5.1468 ms, copy-out 0.0159 ms; source buffer at 0x431dc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.718e+10 (2048.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 22.6 GB/s over the touched lines; buffer at 0x49fe40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 106 calls per interval; first call of an interval: copy-in 0.1038 ms, kernel 0.0755 ms, copy-out 0.0135 ms; source buffer at 0x49ff40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.366e+08 (2047.8 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 532.9; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,working-set-mib=8

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 530 passes per interval, 220.7 GB/s over the touched lines; buffer at 0x5f96c0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 328 calls per interval; first call of an interval: copy-in 0.0388 ms, kernel 0.0163 ms, copy-out 0.0128 ms; source buffer at 0x5f97c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.382e+06 (128.0 per touched line), copy 8.38e+06; SMMU translation requests per repetition: direct 0, copy 132.6; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,rotated=1,working-set-mib=8

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 660 passes per interval, 281.8 GB/s over the touched lines; buffer at 0x501600000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 268 calls per interval; first call of an interval: copy-in 0.0358 ms, kernel 0.0346 ms, copy-out 0.0144 ms; source buffer at 0x501700000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 133.8; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,scope=sys,working-set-mib=8

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 525 passes per interval, 218.0 GB/s over the touched lines; buffer at 0x436880000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 242 calls per interval; first call of an interval: copy-in 0.0362 ms, kernel 0.0435 ms, copy-out 0.0149 ms; source buffer at 0x436980000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 134.4; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,tiling=tiles,working-set-mib=8

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1311 passes per interval, 547.0 GB/s over the touched lines; buffer at 0x526480000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 348 calls per interval; first call of an interval: copy-in 0.0363 ms, kernel 0.0198 ms, copy-out 0.0135 ms; source buffer at 0x526580000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 134.5; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=1024

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 208.1 GB/s over the touched lines; buffer at 0x48a000000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 0.6445 ms, kernel 5.1599 ms, copy-out 0.0129 ms; source buffer at 0x48a100000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 201 passes per interval, 351.4 GB/s over the touched lines; buffer at 0x5b92c0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 112 calls per interval; first call of an interval: copy-in 0.0943 ms, kernel 0.0826 ms, copy-out 0.0095 ms; source buffer at 0x5b9380000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 518.2; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,working-set-mib=8

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1242 passes per interval, 520.1 GB/s over the touched lines; buffer at 0x44d280000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 341 calls per interval; first call of an interval: copy-in 0.0371 ms, kernel 0.0213 ms, copy-out 0.0134 ms; source buffer at 0x44d340000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 134.5; multiplexed rows voided: 0

### route/footprint-mib=1024,k=2,kernel=k2,placement=cpu,working-set-mib=1024

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 181.8 GB/s over the touched lines; buffer at 0x58e2c0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 2.9494 ms, kernel 0.6569 ms, copy-out 0.0125 ms; source buffer at 0x58e3c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.147e+09 (256.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.639e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=2,kernel=k2,placement=cpu,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 104 passes per interval, 173.6 GB/s over the touched lines; buffer at 0x5b3b40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 149 calls per interval; first call of an interval: copy-in 0.1060 ms, kernel 0.0189 ms, copy-out 0.0112 ms; source buffer at 0x5b3c40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.708e+07 (256.0 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 533; multiplexed rows voided: 0

### route/footprint-mib=1024,k=2,kernel=k2,placement=hbm,working-set-mib=1024

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 31 passes per interval, 1629.3 GB/s over the touched lines; buffer at 0x4c0a80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.5440 ms, kernel 0.6598 ms, copy-out 0.0124 ms; source buffer at 0x4c0b80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=2,kernel=k2,placement=hbm,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 857 passes per interval, 1427.4 GB/s over the touched lines; buffer at 0x487f40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 165 calls per interval; first call of an interval: copy-in 0.0963 ms, kernel 0.0263 ms, copy-out 0.0096 ms; source buffer at 0x488040000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 519.2; multiplexed rows voided: 0

### route/footprint-mib=1024,k=4,kernel=k2,placement=cpu,working-set-mib=1024

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 91.3 GB/s over the touched lines; buffer at 0x5da800000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 2.9388 ms, kernel 1.3027 ms, copy-out 0.0126 ms; source buffer at 0x5da900000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 4.295e+09 (512.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=4,kernel=k2,placement=cpu,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 53 passes per interval, 88.8 GB/s over the touched lines; buffer at 0x5132c0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 143 calls per interval; first call of an interval: copy-in 0.1070 ms, kernel 0.0272 ms, copy-out 0.0119 ms; source buffer at 0x513400000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.342e+08 (512.0 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 533; multiplexed rows voided: 0

### route/footprint-mib=1024,k=4,kernel=k2,placement=hbm,working-set-mib=1024

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 16 passes per interval, 824.3 GB/s over the touched lines; buffer at 0x40ab80000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 2.5418 ms, kernel 1.3036 ms, copy-out 0.0128 ms; source buffer at 0x40ac80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.639e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=4,kernel=k2,placement=hbm,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 577 passes per interval, 973.9 GB/s over the touched lines; buffer at 0x468200000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 151 calls per interval; first call of an interval: copy-in 0.0948 ms, kernel 0.0343 ms, copy-out 0.0151 ms; source buffer at 0x468340000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 518.5; multiplexed rows voided: 0

### route/footprint-mib=1024,k=64,kernel=k2,placement=cpu,working-set-mib=1024

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 5.7 GB/s over the touched lines; buffer at 0x5e6300000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 2.9508 ms, kernel 20.5978 ms, copy-out 0.0149 ms; source buffer at 0x5e6400000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.872e+10 (8192.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.639e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=64,kernel=k2,placement=cpu,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 5.6 GB/s over the touched lines; buffer at 0x551380000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 53 calls per interval; first call of an interval: copy-in 0.1048 ms, kernel 0.2706 ms, copy-out 0.0126 ms; source buffer at 0x551440000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.145e+09 (8185.7 per touched line), copy 3.354e+07; SMMU translation requests per repetition: direct 0, copy 532.9; multiplexed rows voided: 0

### route/footprint-mib=1024,k=64,kernel=k2,placement=hbm,working-set-mib=1024

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 52.1 GB/s over the touched lines; buffer at 0x418600000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 2.5426 ms, kernel 20.5809 ms, copy-out 0.0132 ms; source buffer at 0x418700000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,k=64,kernel=k2,placement=hbm,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 63 passes per interval, 97.5 GB/s over the touched lines; buffer at 0x4cb9c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 54 calls per interval; first call of an interval: copy-in 0.0943 ms, kernel 0.2764 ms, copy-out 0.0105 ms; source buffer at 0x4cbac0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 519; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k3,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 172.9 GB/s over the touched lines; buffer at 0x54c9c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 2.9600 ms, kernel 0.4677 ms, copy-out 0.0144 ms; source buffer at 0x54cac0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (74.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 0, copy 1.641e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k3,placement=hbm

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 44 passes per interval, 1992.9 GB/s over the touched lines; buffer at 0x54b400000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 18 calls per interval; first call of an interval: copy-in 0.6379 ms, kernel 0.4753 ms, copy-out 0.0125 ms; source buffer at 0x54b500000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,layout=line,placement=cpu,update=atomic

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 309.2 GB/s over the touched lines; buffer at 0x470e00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 2.9769 ms, kernel 0.3212 ms, copy-out 3.6168 ms; source buffer at 0x470ec0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 2889, copy 3.278e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,layout=line,placement=hbm,update=atomic

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 59 passes per interval, 3155.9 GB/s over the touched lines; buffer at 0x40cf80000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 13 calls per interval; first call of an interval: copy-in 0.7202 ms, kernel 0.3234 ms, copy-out 0.6383 ms; source buffer at 0x40d080000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 410.9, copy 2859; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=cpu,update=atomic

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 177.0 GB/s over the touched lines; buffer at 0x554c80000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 2.9885 ms, kernel 0.8097 ms, copy-out 3.6164 ms; source buffer at 0x554d80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 4219, copy 3.278e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=cpu,update=plain

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 176.9 GB/s over the touched lines; buffer at 0x53c680000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 2.9682 ms, kernel 0.7612 ms, copy-out 3.6145 ms; source buffer at 0x53c780000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+09 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 4469, copy 3.278e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=cpu,update=returned

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 174.9 GB/s over the touched lines; buffer at 0x41dd80000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 2.9669 ms, kernel 0.8835 ms, copy-out 3.6162 ms; source buffer at 0x41de80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.074e+09 (128.0 per touched line), copy 1.074e+09; SMMU translation requests per repetition: direct 4472, copy 3.278e+04; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=hbm,update=atomic

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 25 passes per interval, 1310.7 GB/s over the touched lines; buffer at 0x48ae00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 10 calls per interval; first call of an interval: copy-in 0.7155 ms, kernel 0.8154 ms, copy-out 0.6392 ms; source buffer at 0x48af40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1324, copy 3609; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=hbm,update=plain

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 27 passes per interval, 1396.5 GB/s over the touched lines; buffer at 0x56be00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 10 calls per interval; first call of an interval: copy-in 0.7120 ms, kernel 0.7574 ms, copy-out 0.6383 ms; source buffer at 0x56bf80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 2739, copy 3891; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=hbm,update=returned

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 23 passes per interval, 1196.5 GB/s over the touched lines; buffer at 0x478900000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 10 calls per interval; first call of an interval: copy-in 0.7182 ms, kernel 0.8860 ms, copy-out 0.6387 ms; source buffer at 0x478a00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 2981, copy 3824; multiplexed rows voided: 0

### route/footprint-mib=11520,kernel=k3,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 8.2 GB/s over the touched lines; buffer at 0x501640000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 32.6397 ms, kernel 0.5005 ms, copy-out 0.0137 ms; source buffer at 0x5019c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.9 per touched line), copy 1.211e+10; SMMU translation requests per repetition: direct 6.714e+07, copy 1.843e+05; multiplexed rows voided: 0

### route/footprint-mib=1536,kernel=k3,placement=cpu

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 220.8 GB/s over the touched lines; buffer at 0x556b00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 4.3717 ms, kernel 0.4728 ms, copy-out 0.0139 ms; source buffer at 0x556c00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (57.9 per touched line), copy 1.611e+09; SMMU translation requests per repetition: direct 0, copy 2.46e+04; multiplexed rows voided: 0

### route/footprint-mib=16,kernel=k6,placement=cpu,update=atomic

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 11.2 GB/s over the touched lines; buffer at 0x536ac0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 98 calls per interval; first call of an interval: copy-in 0.0648 ms, kernel 0.0776 ms, copy-out 0.0672 ms; source buffer at 0x536b40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 1.678e+07; SMMU translation requests per repetition: direct 0, copy 130.4; multiplexed rows voided: 0

### route/footprint-mib=16,kernel=k6,placement=hbm,update=atomic

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 260 passes per interval, 219.8 GB/s over the touched lines; buffer at 0x569ec0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 105 calls per interval; first call of an interval: copy-in 0.0548 ms, kernel 0.0787 ms, copy-out 0.0623 ms; source buffer at 0x569f80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 40.17; multiplexed rows voided: 0

### route/footprint-mib=16384,generator=uniform,kernel=k4,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 35.5 GB/s over the touched lines; buffer at 0x430900000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 46.8548 ms, kernel 0.5069 ms, copy-out 1.3556 ms; source buffer at 0x430dc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 4.961e+10 (369.7 per touched line), copy 1.718e+10; SMMU translation requests per repetition: direct 2.726e+05, copy 2.765e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,generator=uniform,kernel=k4,placement=hbm

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 532.8 GB/s over the touched lines; buffer at 0x4b6280000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 10.1754 ms, kernel 31.8862 ms, copy-out 0.2975 ms; source buffer at 0x4b6740000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 5.013e+05, copy 6.473e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,sharing=shared,state=dirty

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 50 passes per interval, 4.6 GB/s over the touched lines; buffer at 0x483280000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 50 calls per interval; first call of an interval: copy-in 45.9606 ms, kernel 0.0646 ms, copy-out 0.0172 ms; source buffer at 0x483700000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.355e+07 (128.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 2.016e+06, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.01

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x5fa540000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 11 calls per interval; first call of an interval: copy-in 1.5148 ms, kernel 0.4989 ms, copy-out 0.0188 ms; source buffer at 0x5fa9c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.718e+08; SMMU translation requests per repetition: direct 1.211e+08, copy 4.045e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=0.1

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x49b6c0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 4.8208 ms, kernel 0.4997 ms, copy-out 0.0139 ms; source buffer at 0x49bb40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.718e+09; SMMU translation requests per repetition: direct 1.211e+08, copy 2.983e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,sharing=shared,w=1

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x42b180000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 45.2641 ms, kernel 0.4993 ms, copy-out 0.0152 ms; source buffer at 0x42b640000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.718e+10; SMMU translation requests per repetition: direct 1.211e+08, copy 3.132e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.01

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x590b80000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 4.6616 ms, kernel 0.5019 ms, copy-out 0.0150 ms; source buffer at 0x591040000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.718e+08; SMMU translation requests per repetition: direct 1.211e+08, copy 9.6e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=0.1

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x419280000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 9.9956 ms, kernel 0.5043 ms, copy-out 0.0163 ms; source buffer at 0x419740000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.718e+09; SMMU translation requests per repetition: direct 1.211e+08, copy 7.758e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,sharing=shared,w=1

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x5b5b00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 49.4098 ms, kernel 0.5037 ms, copy-out 0.0145 ms; source buffer at 0x5b5f80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.718e+10; SMMU translation requests per repetition: direct 1.211e+08, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=runs,sharing=shared,w=1

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x5eee40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 46.2008 ms, kernel 0.5091 ms, copy-out 0.0161 ms; source buffer at 0x5ef2c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 1.211e+08, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=0.01

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x56d900000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 45.8281 ms, kernel 0.5148 ms, copy-out 0.0148 ms; source buffer at 0x56dd80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 1.211e+08, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=0.1

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x476ec0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 46.2252 ms, kernel 0.5174 ms, copy-out 0.0170 ms; source buffer at 0x477340000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 1.211e+08, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,sharing=shared,w=1

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x439080000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 46.4511 ms, kernel 0.5139 ms, copy-out 0.0158 ms; source buffer at 0x439500000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 1.211e+08, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-order=2m,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 375.2 GB/s over the touched lines; buffer at 0x5bc3c0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 45.8433 ms, kernel 0.4699 ms, copy-out 0.0152 ms; source buffer at 0x5bc880000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.368e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 6.328e+05, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-order=2m,placement=hbm

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 8 passes per interval, 801.3 GB/s over the touched lines; buffer at 0x511500000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 10.1112 ms, kernel 0.4636 ms, copy-out 0.0142 ms; source buffer at 0x5119c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 5.735e+05, copy 6.637e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-order=64k,placement=cpu

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 386.8 GB/s over the touched lines; buffer at 0x5b52c0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 46.0575 ms, kernel 0.4563 ms, copy-out 0.0140 ms; source buffer at 0x5b5780000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.386e+08 (34.1 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 2.784e+05, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-order=64k,placement=hbm

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 13 passes per interval, 1251.5 GB/s over the touched lines; buffer at 0x4dc700000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 10.1220 ms, kernel 0.4524 ms, copy-out 0.0144 ms; source buffer at 0x4dcbc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4.008e+05, copy 6.562e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 375.3 GB/s over the touched lines; buffer at 0x40a100000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 42.1184 ms, kernel 0.4922 ms, copy-out 0.0128 ms; source buffer at 0x40a580000000
- AnonHugePages after population (kB): direct 16777216, copy 16777216; after the series: direct 16777216, copy 16777216
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 0, copy 532; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,page-size=512m,placement=hbm

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 42 passes per interval, 4220.1 GB/s over the touched lines; buffer at 0x4cbe80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 10.1368 ms, kernel 0.4884 ms, copy-out 0.0137 ms; source buffer at 0x4cc340000000
- AnonHugePages after population (kB): direct 16777216, copy 16777216; after the series: direct 16777216, copy 16777216
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,partition=2g,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 347.0 GB/s over the touched lines; buffer at 0x41ef80000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 45.0777 ms, kernel 0.6782 ms, copy-out 0.0135 ms; source buffer at 0x41f400000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 3.561e+05, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,partition=2g,placement=hbm

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 7.1 GB/s over the touched lines; buffer at 0x5f4900000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 10.1431 ms, kernel 0.6703 ms, copy-out 0.0148 ms; source buffer at 0x5f4dc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 8.029e+07, copy 6.533e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x5ed140000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 44.9023 ms, kernel 0.5051 ms, copy-out 0.0129 ms; source buffer at 0x5ed600000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (34.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 1.211e+08, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=hbm

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 4.7 GB/s over the touched lines; buffer at 0x53d680000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 10.1314 ms, kernel 0.4979 ms, copy-out 0.0129 ms; source buffer at 0x53db00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.207e+08, copy 6.575e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3p,page-size=512m,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 215 passes per interval, 338.8 GB/s over the touched lines; buffer at 0x5c9240000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 42.1189 ms, kernel 0.0519 ms, copy-out 0.0104 ms; source buffer at 0x5c9700000000
- AnonHugePages after population (kB): direct 16777216, copy 16777216; after the series: direct 16777216, copy 16777216
- link read bytes per repetition: direct 3.355e+07 (128.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 0, copy 531; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3p,placement=cpu

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 4.8 GB/s over the touched lines; buffer at 0x5aba80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 45.7810 ms, kernel 0.0620 ms, copy-out 0.0136 ms; source buffer at 0x5abf00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.355e+07 (128.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 1.96e+06, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k6,placement=cpu,update=atomic

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 179.5 GB/s over the touched lines; buffer at 0x4e4e80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 44.9244 ms, kernel 13.2964 ms, copy-out 58.0329 ms; source buffer at 0x4e5340000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 1.723e+10; SMMU translation requests per repetition: direct 2.882e+05, copy 5.244e+05; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k6,placement=hbm,update=atomic

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 1310.8 GB/s over the touched lines; buffer at 0x4f9600000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 10.1621 ms, kernel 13.1702 ms, copy-out 10.1326 ms; source buffer at 0x4f9a80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 5.025e+05, copy 9.455e+05; multiplexed rows voided: 0

### route/footprint-mib=2048,kernel=k3,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 252.6 GB/s over the touched lines; buffer at 0x4a54c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 5.8152 ms, kernel 0.4773 ms, copy-out 0.0138 ms; source buffer at 0x4a5600000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (50.6 per touched line), copy 2.147e+09; SMMU translation requests per repetition: direct 0, copy 3.279e+04; multiplexed rows voided: 0

### route/footprint-mib=24576,generator=uniform,kernel=k4,placement=cpu

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 34.3 GB/s over the touched lines; buffer at 0x517780000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 71.7182 ms, kernel 0.5125 ms, copy-out 2.0314 ms; source buffer at 0x517e40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 7.684e+10 (381.7 per touched line), copy 2.577e+10; SMMU translation requests per repetition: direct 5.056e+05, copy 4.146e+05; multiplexed rows voided: 0

### route/footprint-mib=24576,kernel=k3,placement=cpu

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 3.4 GB/s over the touched lines; buffer at 0x540980000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 65.5410 ms, kernel 0.5115 ms, copy-out 0.0158 ms; source buffer at 0x541000000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (33.4 per touched line), copy 2.585e+10; SMMU translation requests per repetition: direct 1.671e+08, copy 3.932e+05; multiplexed rows voided: 0

### route/footprint-mib=24576,kernel=k3,placement=hbm

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 3.5 GB/s over the touched lines; buffer at 0x432900000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 15.1757 ms, kernel 0.5066 ms, copy-out 0.0150 ms; source buffer at 0x432f80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.667e+08, copy 1.238e+06; multiplexed rows voided: 0

### route/footprint-mib=256,generator=uniform,kernel=k4,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 36.5 GB/s over the touched lines; buffer at 0x4f9740000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 20 calls per interval; first call of an interval: copy-in 0.7681 ms, kernel 0.2122 ms, copy-out 0.0397 ms; source buffer at 0x4f9840000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 7.683e+08 (366.4 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 0, copy 4229; multiplexed rows voided: 0

### route/footprint-mib=256,generator=uniform,kernel=k4,placement=hbm

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 95 passes per interval, 1273.1 GB/s over the touched lines; buffer at 0x48f180000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 23 calls per interval; first call of an interval: copy-in 0.6469 ms, kernel 0.2124 ms, copy-out 0.0378 ms; source buffer at 0x48f240000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 4228; multiplexed rows voided: 0

### route/footprint-mib=256,kernel=k3,placement=cpu

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 50.0 GB/s over the touched lines; buffer at 0x440ac0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 17 calls per interval; first call of an interval: copy-in 0.7704 ms, kernel 0.4275 ms, copy-out 0.0133 ms; source buffer at 0x440b80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.368e+08 (256.0 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 0, copy 4114; multiplexed rows voided: 0

### route/footprint-mib=256,kernel=k3,placement=hbm

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 47 passes per interval, 630.3 GB/s over the touched lines; buffer at 0x5cf240000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 19 calls per interval; first call of an interval: copy-in 0.6471 ms, kernel 0.4276 ms, copy-out 0.0149 ms; source buffer at 0x5cf300000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 4114; multiplexed rows voided: 0

### route/footprint-mib=256,kernel=k6,placement=cpu,update=atomic

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 177.6 GB/s over the touched lines; buffer at 0x5bde00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 11 calls per interval; first call of an interval: copy-in 0.7722 ms, kernel 0.1963 ms, copy-out 0.9151 ms; source buffer at 0x5bdec0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 2.684e+08; SMMU translation requests per repetition: direct 309.6, copy 8196; multiplexed rows voided: 0

### route/footprint-mib=256,kernel=k6,placement=hbm,update=atomic

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 98 passes per interval, 1309.8 GB/s over the touched lines; buffer at 0x518540000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 38 calls per interval; first call of an interval: copy-in 0.2090 ms, kernel 0.2039 ms, copy-out 0.1708 ms; source buffer at 0x518600000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 114.7, copy 249.2; multiplexed rows voided: 0

### route/footprint-mib=32768,generator=uniform,kernel=k4,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 35.4 GB/s over the touched lines; buffer at 0x49d000000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 88.3945 ms, kernel 0.5177 ms, copy-out 2.7077 ms; source buffer at 0x49d8c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 9.934e+10 (370.1 per touched line), copy 3.436e+10; SMMU translation requests per repetition: direct 7.472e+05, copy 5.526e+05; multiplexed rows voided: 0

### route/footprint-mib=32768,kernel=k3,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 3.0 GB/s over the touched lines; buffer at 0x471100000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 85.1968 ms, kernel 0.5151 ms, copy-out 0.0149 ms; source buffer at 0x4719c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (33.0 per touched line), copy 3.448e+10; SMMU translation requests per repetition: direct 1.912e+08, copy 5.243e+05; multiplexed rows voided: 0

### route/footprint-mib=32768,kernel=k6,placement=cpu,update=atomic

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 180.5 GB/s over the touched lines; buffer at 0x408d40000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 86.1821 ms, kernel 26.5542 ms, copy-out 116.1821 ms; source buffer at 0x4095c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 3.448e+10; SMMU translation requests per repetition: direct 9.698e+05, copy 1.049e+06; multiplexed rows voided: 0

### route/footprint-mib=4096,generator=uniform,kernel=k4,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 34.7 GB/s over the touched lines; buffer at 0x553e80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 11.6873 ms, kernel 0.4440 ms, copy-out 0.3412 ms; source buffer at 0x554040000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.285e+10 (382.9 per touched line), copy 4.295e+09; SMMU translation requests per repetition: direct 6.885e+04, copy 6.819e+04; multiplexed rows voided: 0

### route/footprint-mib=4096,generator=uniform,kernel=k4,placement=hbm

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 606.8 GB/s over the touched lines; buffer at 0x530140000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 2.5477 ms, kernel 6.9712 ms, copy-out 0.0736 ms; source buffer at 0x530300000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 3.924e+04, copy 4.736e+04; multiplexed rows voided: 0

### route/footprint-mib=4096,kernel=k3,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 305.5 GB/s over the touched lines; buffer at 0x464d00000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 11.4657 ms, kernel 0.4804 ms, copy-out 0.0151 ms; source buffer at 0x464ec0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (40.7 per touched line), copy 4.295e+09; SMMU translation requests per repetition: direct 0, copy 6.556e+04; multiplexed rows voided: 0

### route/footprint-mib=4096,kernel=k3,placement=hbm

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 329.7 GB/s over the touched lines; buffer at 0x562480000000 (offset in its 16 GiB window: 2147483648 bytes)
- copy route: 7 calls per interval; first call of an interval: copy-in 2.5295 ms, kernel 0.4861 ms, copy-out 0.0112 ms; source buffer at 0x562600000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1154, copy 1489; multiplexed rows voided: 0

### route/footprint-mib=4096,kernel=k6,placement=cpu,update=atomic

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 177.4 GB/s over the touched lines; buffer at 0x52c780000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 11.5200 ms, kernel 3.2633 ms, copy-out 11.5346 ms; source buffer at 0x52c900000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 4.295e+09; SMMU translation requests per repetition: direct 6.632e+04, copy 1.324e+05; multiplexed rows voided: 0

### route/footprint-mib=4096,kernel=k6,placement=hbm,update=atomic

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 7 passes per interval, 1311.3 GB/s over the touched lines; buffer at 0x4e3b80000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 2.6011 ms, kernel 3.2751 ms, copy-out 2.5427 ms; source buffer at 0x4e3d40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.773e+04, copy 4.601e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=reads,kernel=k5,placement=cpu,sharing=shared,sweeps=8,tiling=tiles

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.2 GB/s over the touched lines; buffer at 0x416f80000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.4905 ms, kernel 3.2293 ms, copy-out 1.8170 ms; source buffer at 0x417080000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.603e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=reads,kernel=k5,placement=hbm,sharing=shared,sweeps=8,tiling=tiles

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 7 passes per interval, 164.3 GB/s over the touched lines; buffer at 0x4e6100000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 0.3425 ms, kernel 3.2184 ms, copy-out 0.3180 ms; source buffer at 0x4e6200000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 5481, copy 5929; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=0.01

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.2 GB/s over the touched lines; buffer at 0x4ecc40000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 0.0721 ms, kernel 3.2192 ms, copy-out 1.8164 ms; source buffer at 0x4ecd40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+06; SMMU translation requests per repetition: direct 3.623e+04, copy 1.962e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=0.1

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.2 GB/s over the touched lines; buffer at 0x5d0b40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 0.2914 ms, kernel 3.2205 ms, copy-out 1.8138 ms; source buffer at 0x5d0c40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+07; SMMU translation requests per repetition: direct 3.622e+04, copy 2.033e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=1

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.0 GB/s over the touched lines; buffer at 0x55fe00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 1.6613 ms, kernel 3.2191 ms, copy-out 1.8195 ms; source buffer at 0x55ff00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.613e+04, copy 1.127e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=0.01

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.6 GB/s over the touched lines; buffer at 0x515440000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 0.1679 ms, kernel 3.2141 ms, copy-out 1.8136 ms; source buffer at 0x515580000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+06; SMMU translation requests per repetition: direct 3.62e+04, copy 3.646e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=0.1

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.6 GB/s over the touched lines; buffer at 0x55f900000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 0.3432 ms, kernel 3.2238 ms, copy-out 1.8142 ms; source buffer at 0x55fa00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+07; SMMU translation requests per repetition: direct 3.603e+04, copy 3.348e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=1

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.4 GB/s over the touched lines; buffer at 0x43ac40000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.6261 ms, kernel 3.2274 ms, copy-out 1.8130 ms; source buffer at 0x43ad40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.616e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=runs,sharing=shared,sweeps=8,tiling=tiles,w=1

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.5 GB/s over the touched lines; buffer at 0x5681c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 1.5777 ms, kernel 3.2194 ms, copy-out 1.8136 ms; source buffer at 0x5682c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.615e+04, copy 1.648e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sharing=shared,sweeps=8,tiling=tiles,w=0.01

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.5 GB/s over the touched lines; buffer at 0x5f3d40000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.4833 ms, kernel 3.2133 ms, copy-out 1.8153 ms; source buffer at 0x5f3e80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.616e+04, copy 1.641e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sharing=shared,sweeps=8,tiling=tiles,w=0.1

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.1 GB/s over the touched lines; buffer at 0x4c5e00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.5092 ms, kernel 3.2283 ms, copy-out 1.8148 ms; source buffer at 0x4c5f00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.637e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sharing=shared,sweeps=8,tiling=tiles,w=1

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.5 GB/s over the touched lines; buffer at 0x527440000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 1.6476 ms, kernel 3.2319 ms, copy-out 1.8162 ms; source buffer at 0x527540000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.616e+04, copy 1.654e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=0.01

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 149.3 GB/s over the touched lines; buffer at 0x549600000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 0.0742 ms, kernel 3.2376 ms, copy-out 0.3262 ms; source buffer at 0x549700000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4.171e+04, copy 2.775e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=0.1

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 154.2 GB/s over the touched lines; buffer at 0x54b180000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 0.1228 ms, kernel 3.2297 ms, copy-out 0.3156 ms; source buffer at 0x54b2c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4.508e+04, copy 2.959e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sharing=shared,sweeps=8,tiling=tiles,w=1

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 154.1 GB/s over the touched lines; buffer at 0x4ad000000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 0.4640 ms, kernel 3.2268 ms, copy-out 0.3156 ms; source buffer at 0x4ad140000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4.243e+04, copy 3.197e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=0.01

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 148.6 GB/s over the touched lines; buffer at 0x5fcf40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 0.1735 ms, kernel 3.2152 ms, copy-out 0.3227 ms; source buffer at 0x5fd040000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4.168e+04, copy 4.118e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=0.1

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 150.1 GB/s over the touched lines; buffer at 0x438840000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 0.3340 ms, kernel 3.2157 ms, copy-out 0.3191 ms; source buffer at 0x438940000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4.171e+04, copy 3.632e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sharing=shared,sweeps=8,tiling=tiles,w=1

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 151.0 GB/s over the touched lines; buffer at 0x5519c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.5160 ms, kernel 3.2210 ms, copy-out 0.3154 ms; source buffer at 0x551ac0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 3.852e+04, copy 2.125e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=runs,sharing=shared,sweeps=8,tiling=tiles,w=1

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 154.2 GB/s over the touched lines; buffer at 0x4fbb80000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 1.2893 ms, kernel 3.2368 ms, copy-out 0.3150 ms; source buffer at 0x4fbc80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4.268e+04, copy 2.135e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sharing=shared,sweeps=8,tiling=tiles,w=0.01

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 154.0 GB/s over the touched lines; buffer at 0x4f8a80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 0.3820 ms, kernel 3.2172 ms, copy-out 0.3207 ms; source buffer at 0x4f8b80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4.535e+04, copy 3.653e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sharing=shared,sweeps=8,tiling=tiles,w=0.1

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 149.5 GB/s over the touched lines; buffer at 0x43fa00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 0.3628 ms, kernel 3.2057 ms, copy-out 0.3155 ms; source buffer at 0x43fb00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4.166e+04, copy 3.659e+04; multiplexed rows voided: 0

### route/footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sharing=shared,sweeps=8,tiling=tiles,w=1

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 150.5 GB/s over the touched lines; buffer at 0x4a37c0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 0.4654 ms, kernel 3.2174 ms, copy-out 0.3175 ms; source buffer at 0x4a38c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 3.867e+04, copy 3.137e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=1,tiling=tiles

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 6 passes per interval, 144.0 GB/s over the touched lines; buffer at 0x5f9d80000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 1.4873 ms, kernel 0.4145 ms, copy-out 1.8142 ms; source buffer at 0x5f9e80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 8.028e+08 (191.4 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3695, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=16,tiling=tiles

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 10.2 GB/s over the touched lines; buffer at 0x5fcd80000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 1.4904 ms, kernel 6.4067 ms, copy-out 1.8134 ms; source buffer at 0x5fce80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.284e+10 (3062.4 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.604e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=2,tiling=tiles

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 79.1 GB/s over the touched lines; buffer at 0x4ca280000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 1.4755 ms, kernel 0.8194 ms, copy-out 1.8124 ms; source buffer at 0x4ca380000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.606e+09 (382.8 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 1.202e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=4,tiling=tiles

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 40.2 GB/s over the touched lines; buffer at 0x41da00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 5 calls per interval; first call of an interval: copy-in 1.4967 ms, kernel 1.6165 ms, copy-out 1.8135 ms; source buffer at 0x41db00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 3.211e+09 (765.6 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 1.807e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=64,tiling=tiles

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 2.5 GB/s over the touched lines; buffer at 0x44e000000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 1.4814 ms, kernel 25.7220 ms, copy-out 1.8147 ms; source buffer at 0x44e100000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.138e+10 (12249.8 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.62e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=none

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 12.8 GB/s over the touched lines; buffer at 0x557d40000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.4861 ms, kernel 2.7430 ms, copy-out 1.8148 ms; source buffer at 0x557e40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 1.307e+10 (3116.0 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.333e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.3 GB/s over the touched lines; buffer at 0x569500000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 1.4813 ms, kernel 3.2230 ms, copy-out 1.8134 ms; source buffer at 0x569640000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 6.422e+09 (1531.2 per touched line), copy 5.369e+08; SMMU translation requests per repetition: direct 3.618e+04, copy 1.64e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=1,tiling=tiles

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 51 passes per interval, 1345.5 GB/s over the touched lines; buffer at 0x5c9380000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 20 calls per interval; first call of an interval: copy-in 0.3818 ms, kernel 0.4085 ms, copy-out 0.3232 ms; source buffer at 0x5c9480000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 506.9, copy 1685; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=16,tiling=tiles

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 82.1 GB/s over the touched lines; buffer at 0x436740000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 3 calls per interval; first call of an interval: copy-in 0.3845 ms, kernel 6.4373 ms, copy-out 0.3207 ms; source buffer at 0x436840000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 9635, copy 1.075e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=2,tiling=tiles

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 26 passes per interval, 659.9 GB/s over the touched lines; buffer at 0x500e00000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 14 calls per interval; first call of an interval: copy-in 0.3833 ms, kernel 0.8137 ms, copy-out 0.3244 ms; source buffer at 0x500f00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1475, copy 2349; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=4,tiling=tiles

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 13 passes per interval, 329.4 GB/s over the touched lines; buffer at 0x425340000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 9 calls per interval; first call of an interval: copy-in 0.3852 ms, kernel 1.6091 ms, copy-out 0.3199 ms; source buffer at 0x425440000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 2972, copy 3579; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=64,tiling=tiles

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 20.7 GB/s over the touched lines; buffer at 0x469700000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 0.3965 ms, kernel 25.6529 ms, copy-out 0.3190 ms; source buffer at 0x469840000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4.173e+04, copy 3.572e+04; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=none

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 8 passes per interval, 194.9 GB/s over the touched lines; buffer at 0x54c200000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 0.3882 ms, kernel 2.7388 ms, copy-out 0.3210 ms; source buffer at 0x54c300000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 9419, copy 5464; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 7 passes per interval, 164.7 GB/s over the touched lines; buffer at 0x561cc0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 6 calls per interval; first call of an interval: copy-in 0.3896 ms, kernel 3.2374 ms, copy-out 0.3227 ms; source buffer at 0x561dc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 6005, copy 5438; multiplexed rows voided: 0

### route/footprint-mib=64,kernel=k6,placement=cpu,update=atomic

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 14 passes per interval, 44.5 GB/s over the touched lines; buffer at 0x4d4b80000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 34 calls per interval; first call of an interval: copy-in 0.2112 ms, kernel 0.1604 ms, copy-out 0.2376 ms; source buffer at 0x4d4c40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 6.711e+07; SMMU translation requests per repetition: direct 81.82, copy 2053; multiplexed rows voided: 0

### route/footprint-mib=64,kernel=k6,placement=hbm,update=atomic

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 122 passes per interval, 408.9 GB/s over the touched lines; buffer at 0x532e40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 79 calls per interval; first call of an interval: copy-in 0.0759 ms, kernel 0.1717 ms, copy-out 0.0426 ms; source buffer at 0x532f00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 22.91, copy 27.74; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1,placement=cpu

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x49d580000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 0.0412 ms, kernel 12.2938 ms, copy-out 0.0388 ms; source buffer at 0x49d640000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1,placement=hbm

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x405800000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 0.0358 ms, kernel 12.2937 ms, copy-out 0.0385 ms; source buffer at 0x4058c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1024,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x451200000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 24 calls per interval; first call of an interval: copy-in 0.0404 ms, kernel 0.7688 ms, copy-out 0.0411 ms; source buffer at 0x4512c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1024,placement=hbm

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 27 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x4aa440000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 25 calls per interval; first call of an interval: copy-in 0.0357 ms, kernel 0.7697 ms, copy-out 0.0367 ms; source buffer at 0x4aa4c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1048576,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 1.0 GB/s over the touched lines; buffer at 0x527dc0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 81 calls per interval; first call of an interval: copy-in 0.0392 ms, kernel 0.1811 ms, copy-out 0.0399 ms; source buffer at 0x527e80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1048576,placement=hbm

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 111 passes per interval, 44.1 GB/s over the touched lines; buffer at 0x476e40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 83 calls per interval; first call of an interval: copy-in 0.0357 ms, kernel 0.1818 ms, copy-out 0.0381 ms; source buffer at 0x476ec0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=16,placement=cpu

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x4f3bc0000000 (offset in its 16 GiB window: 16106127360 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 0.0410 ms, kernel 5.0415 ms, copy-out 0.0415 ms; source buffer at 0x4f3c80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=16,placement=hbm

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x4cf200000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 0.0145 ms, kernel 5.0303 ms, copy-out 0.0078 ms; source buffer at 0x4cf2c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=256,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x40f940000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 8 calls per interval; first call of an interval: copy-in 0.0401 ms, kernel 2.6964 ms, copy-out 0.0399 ms; source buffer at 0x40fa00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=256,placement=hbm

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 8 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x4c3040000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 8 calls per interval; first call of an interval: copy-in 0.0136 ms, kernel 2.6899 ms, copy-out 0.0080 ms; source buffer at 0x4c3100000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=4096,placement=cpu

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 0.0 GB/s over the touched lines; buffer at 0x5e7ec0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 59 calls per interval; first call of an interval: copy-in 0.0404 ms, kernel 0.2703 ms, copy-out 0.0391 ms; source buffer at 0x5e7f80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=4096,placement=hbm

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 76 passes per interval, 0.1 GB/s over the touched lines; buffer at 0x5c30c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 72 calls per interval; first call of an interval: copy-in 0.0145 ms, kernel 0.2676 ms, copy-out 0.0079 ms; source buffer at 0x5c3140000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=65536,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 5 passes per interval, 0.1 GB/s over the touched lines; buffer at 0x50da80000000 (offset in its 16 GiB window: 10737418240 bytes)
- copy route: 76 calls per interval; first call of an interval: copy-in 0.0390 ms, kernel 0.1952 ms, copy-out 0.0375 ms; source buffer at 0x50db00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.389e+06; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=65536,placement=hbm

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 104 passes per interval, 2.7 GB/s over the touched lines; buffer at 0x5e09c0000000 (offset in its 16 GiB window: 7516192768 bytes)
- copy route: 97 calls per interval; first call of an interval: copy-in 0.0139 ms, kernel 0.1946 ms, copy-out 0.0078 ms; source buffer at 0x5e0a80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 0, copy 0; multiplexed rows voided: 0

### route/footprint-mib=8192,generator=rmat,kernel=k4,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 8.6 GB/s over the touched lines; buffer at 0x548ac0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 22.6103 ms, kernel 391.9802 ms, copy-out 0.6776 ms; source buffer at 0x548f00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.415e+10 (359.8 per touched line), copy 8.607e+09; SMMU translation requests per repetition: direct 1.631e+05, copy 1.356e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,generator=rmat,kernel=k4,placement=hbm

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 21.7 GB/s over the touched lines; buffer at 0x46aa40000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 5.3297 ms, kernel 392.3209 ms, copy-out 0.1477 ms; source buffer at 0x46ae80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.633e+05, copy 4.022e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,generator=uniform,kernel=k4,placement=cpu

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 34.7 GB/s over the touched lines; buffer at 0x5a8ac0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 23.7446 ms, kernel 0.4793 ms, copy-out 0.6755 ms; source buffer at 0x5a8dc0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 2.553e+10 (380.4 per touched line), copy 8.59e+09; SMMU translation requests per repetition: direct 1.365e+05, copy 1.386e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,generator=uniform,kernel=k4,placement=hbm

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 2 passes per interval, 569.0 GB/s over the touched lines; buffer at 0x47b100000000 (offset in its 16 GiB window: 4294967296 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 5.0981 ms, kernel 14.9776 ms, copy-out 0.1487 ms; source buffer at 0x47b380000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.447e+05, copy 3.295e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=0.01

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 234.2 GB/s over the touched lines; buffer at 0x55b0c0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 17 calls per interval; first call of an interval: copy-in 0.7760 ms, kernel 0.4904 ms, copy-out 0.0153 ms; source buffer at 0x55b380000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.328e+05, copy 2.062e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=0.1

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 234.7 GB/s over the touched lines; buffer at 0x419cc0000000 (offset in its 16 GiB window: 3221225472 bytes)
- copy route: 13 calls per interval; first call of an interval: copy-in 1.3024 ms, kernel 0.4872 ms, copy-out 0.0162 ms; source buffer at 0x419f40000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.327e+05, copy 3.089e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,sharing=shared,w=1

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 234.7 GB/s over the touched lines; buffer at 0x553000000000 (offset in its 16 GiB window: 0 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 5.2435 ms, kernel 0.4890 ms, copy-out 0.0168 ms; source buffer at 0x553280000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.327e+05, copy 2.957e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=0.01

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 234.5 GB/s over the touched lines; buffer at 0x47a180000000 (offset in its 16 GiB window: 6442450944 bytes)
- copy route: 8 calls per interval; first call of an interval: copy-in 2.5441 ms, kernel 0.5001 ms, copy-out 0.0154 ms; source buffer at 0x47a440000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.328e+05, copy 5.219e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=0.1

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 234.6 GB/s over the touched lines; buffer at 0x443d40000000 (offset in its 16 GiB window: 5368709120 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 5.2723 ms, kernel 0.5013 ms, copy-out 0.0151 ms; source buffer at 0x444000000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.328e+05, copy 3.568e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,sharing=shared,w=1

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 234.0 GB/s over the touched lines; buffer at 0x463640000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 23.8946 ms, kernel 0.5070 ms, copy-out 0.0153 ms; source buffer at 0x463900000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.327e+05, copy 1.311e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=runs,sharing=shared,w=1

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 234.2 GB/s over the touched lines; buffer at 0x59db00000000 (offset in its 16 GiB window: 12884901888 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 20.4405 ms, kernel 0.5054 ms, copy-out 0.0148 ms; source buffer at 0x59dd80000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.327e+05, copy 1.326e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,sharing=shared,w=0.01

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 234.5 GB/s over the touched lines; buffer at 0x547c40000000 (offset in its 16 GiB window: 1073741824 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 5.1212 ms, kernel 0.4887 ms, copy-out 0.0174 ms; source buffer at 0x547f00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.33e+05, copy 2.869e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,sharing=shared,w=0.1

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 234.8 GB/s over the touched lines; buffer at 0x416b40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 5.1097 ms, kernel 0.4906 ms, copy-out 0.0163 ms; source buffer at 0x416e00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.328e+05, copy 2.877e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,sharing=shared,w=1

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 234.3 GB/s over the touched lines; buffer at 0x5d7f40000000 (offset in its 16 GiB window: 13958643712 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 5.2600 ms, kernel 0.4910 ms, copy-out 0.0179 ms; source buffer at 0x5d8200000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 1.328e+05, copy 2.787e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 245.3 GB/s over the touched lines; buffer at 0x5ec240000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 22.9814 ms, kernel 0.4981 ms, copy-out 0.0146 ms; source buffer at 0x5ec4c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (36.2 per touched line), copy 8.607e+09; SMMU translation requests per repetition: direct 4162, copy 1.311e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=hbm

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 3 passes per interval, 243.1 GB/s over the touched lines; buffer at 0x4546c0000000 (offset in its 16 GiB window: 11811160064 bytes)
- copy route: 4 calls per interval; first call of an interval: copy-in 5.0621 ms, kernel 0.4895 ms, copy-out 0.0139 ms; source buffer at 0x454940000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 4.427e+04, copy 1.154e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k6,placement=cpu,update=atomic

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 178.9 GB/s over the touched lines; buffer at 0x4ae600000000 (offset in its 16 GiB window: 8589934592 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 23.1891 ms, kernel 6.5943 ms, copy-out 28.9583 ms; source buffer at 0x4ae8c0000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 8.607e+09; SMMU translation requests per repetition: direct 1.319e+05, copy 2.622e+05; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k6,placement=hbm,update=atomic

- first variant A, seed 73; repeats alternated as drawn: yes
- direct route: 4 passes per interval, 1307.3 GB/s over the touched lines; buffer at 0x4fc780000000 (offset in its 16 GiB window: 15032385536 bytes)
- copy route: 2 calls per interval; first call of an interval: copy-in 5.1861 ms, kernel 6.5714 ms, copy-out 5.0753 ms; source buffer at 0x4fca00000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 0 (0.0 per touched line), copy 0; SMMU translation requests per repetition: direct 6.381e+04, copy 2.092e+05; multiplexed rows voided: 0

### route/footprint-mib=9728,kernel=k3,placement=cpu

- first variant B, seed 73; repeats alternated as drawn: yes
- direct route: 1 passes per interval, 15.1 GB/s over the touched lines; buffer at 0x590640000000 (offset in its 16 GiB window: 9663676416 bytes)
- copy route: 1 calls per interval; first call of an interval: copy-in 26.8063 ms, kernel 0.4926 ms, copy-out 0.0154 ms; source buffer at 0x590940000000
- AnonHugePages after population (kB): direct 0, copy 0; after the series: direct 0, copy 0
- link read bytes per repetition: direct 5.369e+08 (35.5 per touched line), copy 1.02e+10; SMMU translation requests per repetition: direct 3.597e+07, copy 1.628e+05; multiplexed rows voided: 0

