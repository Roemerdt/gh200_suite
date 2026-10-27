# Four-variant cells: direct and copy route at home and at a level of one factor, recomputed from raw rows

Times are per repetition in ms (one pass for the direct route, one complete call for the copy route). Each round runs the four variants once in the order the seed drew; the route difference at home (A - B) and at the level (C - D) and the change of the route difference, (C - D) - (A - B), are formed within each round and given as median with 95 % rank interval. A negative route difference means direct access is faster; a negative change means the level moved the comparison towards direct access. The relative change is the change over the route difference at home, given only where that difference excludes zero. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | level | direct home ms | copy home ms | direct level ms | copy level ms | route difference home ms [interval] | route difference level ms [interval] | change ms [interval] | relative change | rounds | change excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0392 | 0.1032 | 0.3720 | 0.1185 | -0.0640 [-0.0718, -0.0638] | 0.2535 [0.2443, 0.2540] | 0.3157 [0.3112, 0.3216] | -493.1 % | 100 | yes | pass |
| at=8,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 1.4838 | 0.1904 | 0.0389 | 0.1239 | 1.2933 [1.2930, 1.2936] | -0.0850 [-0.0917, -0.0834] | -1.3782 [-1.3854, -1.3708] | -106.6 % | 100 | yes | pass |
| at=8,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 0.0959 | 0.1781 | 0.0162 | 0.0589 | -0.0822 [-0.0824, -0.0820] | -0.0426 [-0.0427, -0.0424] | 0.0396 [0.0393, 0.0399] | -48.2 % | 10 | yes | pass |
| at=none,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=tiling | tiling | none | 26.5404 | 6.5082 | 36.4422 | 5.9753 | 20.0367 [19.9918, 20.0654] | 30.4656 [30.1687, 30.4959] | 10.4360 [10.1110, 10.4667] | +52.1 % | 10 | yes | pass |
| at=none,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=tiling | tiling | none | 3.2757 | 3.8657 | 2.7512 | 3.3917 | -0.5903 [-0.5949, -0.5887] | -0.6392 [-0.6438, -0.6371] | -0.0477 [-0.0498, -0.0428] | +8.1 % | 30 | yes | pass |
| at=plain,footprint-mib=1024,kernel=k6,placement=cpu,type=four,update=atomic,vary=update | update | plain | 6.0594 | 7.4043 | 5.9798 | 7.2413 | -1.3449 [-1.3494, -1.3421] | -1.2632 [-1.2692, -1.2558] | 0.0814 [0.0729, 0.0889] | -6.1 % | 10 | yes | pass |
| at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,type=four,vary=generator | generator | rmat | 30.8079 | 4.1778 | 188.6884 | 68.2019 | 26.6320 [26.6000, 26.6555] | 120.9701 [120.4279, 122.5880] | 94.3375 [93.7819, 95.9740] | +354.2 % | 10 | yes | pass |
| at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,type=four,vary=generator | generator | rmat | 1.2726 | 1.7639 | 65.8752 | 65.9459 | -0.4907 [-0.4913, -0.4902] | -0.0584 [-0.0692, -0.0444] | 0.4334 [0.4213, 0.4467] | -88.3 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | sharing | shared | 0.1930 | 0.2426 | 0.1915 | 0.2422 | -0.0496 [-0.0498, -0.0494] | -0.0508 [-0.0510, -0.0505] | -0.0011 [-0.0014, -0.0008] | +2.3 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 0.1925 | 0.2415 | 0.3765 | 0.4099 | -0.0489 [-0.0491, -0.0484] | -0.0334 [-0.0342, -0.0320] | 0.0155 [0.0148, 0.0169] | -31.8 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | sharing | shared | 0.0375 | 0.0937 | 0.1646 | 0.2158 | -0.0562 [-0.0566, -0.0560] | -0.0510 [-0.0522, -0.0493] | 0.0053 [0.0045, 0.0071] | -9.4 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | sharing | shared | 0.0354 | 0.0898 | 0.1816 | 0.2331 | -0.0545 [-0.0547, -0.0543] | -0.0516 [-0.0520, -0.0513] | 0.0030 [0.0026, 0.0033] | -5.5 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | sharing | shared | 30.8002 | 4.7385 | 30.5349 | 4.1168 | 26.0266 [25.6073, 26.0860] | 26.4183 [26.4150, 26.4236] | 0.3917 [0.3444, 0.8054] | +1.5 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing | sharing | shared | 1.2791 | 1.7738 | 1.2790 | 1.7635 | -0.4951 [-0.4964, -0.4939] | -0.4845 [-0.4852, -0.4837] | 0.0106 [0.0088, 0.0121] | -2.1 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0462 | 0.0713 | 0.0669 | 0.0897 | -0.0251 [-0.0252, -0.0250] | -0.0229 [-0.0230, -0.0227] | 0.0022 [0.0020, 0.0024] | -8.9 % | 90 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 1.5030 | 0.0979 | 1.5059 | 0.6853 | 1.4051 [1.4044, 1.4056] | 0.8207 [0.8203, 0.8212] | -0.5850 [-0.5858, -0.5837] | -41.6 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0520 | 0.0436 | 0.0526 | 0.6124 | 0.0081 [0.0078, 0.0088] | -0.5599 [-0.5603, -0.5596] | -0.5687 [-0.5713, -0.5679] | -7062.2 % | 70 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 1.5103 | 0.0982 | 1.5179 | 0.7575 | 1.4120 [1.4109, 1.4125] | 0.7605 [0.7600, 0.7609] | -0.6518 [-0.6526, -0.6504] | -46.2 % | 90 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0514 | 0.0439 | 0.0524 | 0.6994 | 0.0070 [0.0066, 0.0079] | -0.6476 [-0.6482, -0.6471] | -0.6579 [-0.6590, -0.6556] | -9376.9 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 1.4974 | 0.2186 | 1.5196 | 0.2210 | 1.2792 [1.2782, 1.2802] | 1.2988 [1.2978, 1.3000] | 0.0203 [0.0181, 0.0217] | +1.6 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | sharing | shared | 0.0542 | 0.0904 | 0.0553 | 0.0904 | -0.0362 [-0.0368, -0.0359] | -0.0351 [-0.0357, -0.0347] | 0.0008 [0.0002, 0.0018] | -2.1 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.1142 | 0.1096 | 0.1176 | 0.2804 | 0.0045 [0.0041, 0.0049] | -0.1630 [-0.1639, -0.1620] | -0.1676 [-0.1683, -0.1663] | -3723.1 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.1160 | 0.1098 | 0.1138 | 0.7315 | 0.0063 [0.0058, 0.0068] | -0.6177 [-0.6186, -0.6170] | -0.6239 [-0.6253, -0.6233] | -9974.3 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.1255 | 0.2200 | 0.1274 | 0.2203 | -0.0947 [-0.0949, -0.0942] | -0.0928 [-0.0930, -0.0926] | 0.0020 [0.0013, 0.0026] | -2.2 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 7.2606 | 45.0168 | 7.2305 | 42.5667 | -37.7571 [-37.7590, -37.7544] | -35.3393 [-35.3594, -35.3223] | 2.4186 [2.3989, 2.4340] | -6.4 % | 10 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 433.5190 | 0.5131 | 433.5136 | 5.1532 | 433.0064 [432.9327, 433.1353] | 428.3459 [428.2444, 428.5572] | -4.6619 [-4.7039, -4.5271] | -1.1 % | 10 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1 | sharing | shared | 433.5118 | 0.5130 | 433.6031 | 10.6646 | 432.9966 [432.8926, 433.1864] | 422.9583 [422.7400, 422.9846] | -10.1132 [-10.3380, -9.9558] | -2.3 % | 10 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 433.5799 | 45.5574 | 433.5650 | 43.0186 | 388.0184 [387.7256, 388.2363] | 390.5395 [390.3768, 390.6854] | 2.5129 [2.3360, 2.8353] | +0.6 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing | sharing | shared | 26.7048 | 6.5111 | 23.1673 | 6.4638 | 20.1931 [20.1652, 20.2120] | 16.7051 [16.6888, 16.7113] | -3.4923 [-3.5231, -3.4539] | -17.3 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing | sharing | shared | 3.2782 | 3.8814 | 3.2549 | 3.8841 | -0.6030 [-0.6039, -0.6013] | -0.6290 [-0.6308, -0.6267] | -0.0273 [-0.0287, -0.0228] | +4.5 % | 100 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 26.4409 | 5.0380 | 23.0303 | 5.3361 | 21.4005 [21.3689, 21.4108] | 17.6921 [17.6774, 17.6985] | -3.7099 [-3.7209, -3.6725] | -17.3 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 26.6707 | 5.0339 | 23.0976 | 5.3739 | 21.6343 [21.5803, 21.6754] | 17.7218 [17.7143, 17.7343] | -3.9192 [-3.9539, -3.8596] | -18.1 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 26.6237 | 6.5223 | 23.2116 | 6.5957 | 20.0996 [20.0674, 20.1186] | 16.6169 [16.6021, 16.6377] | -3.4813 [-3.4938, -3.4614] | -17.3 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 3.4778 | 3.5756 | 3.4905 | 3.6640 | -0.0983 [-0.0996, -0.0926] | -0.1741 [-0.1780, -0.1707] | -0.0768 [-0.0829, -0.0703] | +78.1 % | 30 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 3.5709 | 3.5697 | 3.6075 | 3.8771 | 0.0009 [-0.0011, 0.0024] | -0.2699 [-0.2711, -0.2679] | -0.2711 [-0.2730, -0.2681] | - | 100 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 3.5110 | 4.0244 | 3.6000 | 4.0082 | -0.5133 [-0.5198, -0.5106] | -0.4097 [-0.4175, -0.4054] | 0.1026 [0.0957, 0.1122] | -20.0 % | 10 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 8.0737 | 0.5588 | 8.0914 | 1.7223 | 7.5151 [7.5138, 7.5244] | 6.3683 [6.3602, 6.3838] | -1.1505 [-1.1536, -1.1312] | -15.3 % | 10 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1 | sharing | shared | 8.0861 | 0.5624 | 8.1085 | 5.4269 | 7.5240 [7.5187, 7.5262] | 2.6831 [2.6786, 2.7010] | -4.8370 [-4.8438, -4.8205] | -64.3 % | 20 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | sharing | shared | 8.0890 | 5.6394 | 8.1070 | 5.6259 | 2.4497 [2.4462, 2.4528] | 2.4807 [2.4772, 2.4831] | 0.0292 [0.0253, 0.0343] | +1.2 % | 100 | yes | pass |
| at=sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8 | scope | sys | 0.0393 | 0.1100 | 0.4049 | 0.1337 | -0.0708 [-0.0711, -0.0629] | 0.2705 [0.2651, 0.2766] | 0.3366 [0.3290, 0.3471] | -475.7 % | 100 | yes | pass |

## Host phases

The CPU phase before every pass, timed on the CPU clock (ms per pass), and the state check's median load latency on the preparing core after the phase (ns per sampled load), per variant.

| cell | direct home CPU ms | direct home state ns | copy home CPU ms | copy home state ns | direct level CPU ms | direct level state ns | copy level CPU ms | copy level state ns |
|---|---|---|---|---|---|---|---|---|
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | 5.2366 | 60.1 | 5.2403 | 74.4 | 5.4227 | 176.2 | 5.4214 | 179.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 2.7530 | 92.4 | 2.7527 | 145.5 | 2.6641 | 108.0 | 2.6636 | 117.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | 4.9548 | 168.6 | 5.1694 | 139.6 | 5.1016 | 270.8 | 5.1194 | 181.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | 2.8955 | 97.2 | 3.0368 | 101.8 | 2.9189 | 131.6 | 2.9794 | 111.2 |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | 1.2377 | - | 1.2186 | - | 1.6491 | - | 1.6548 | - |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing | 2.4163 | - | 3.7336 | - | 3.6970 | - | 3.1220 | - |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | 0.5227 | 62.2 | 0.5296 | 60.5 | 0.5217 | 56.8 | 0.5246 | 56.1 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 3.6478 | 119.2 | 3.6403 | 167.0 | 3.6205 | 194.1 | 4.0905 | 183.9 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | 3.6312 | 69.1 | 3.6276 | 122.4 | 3.6208 | 127.0 | 4.0933 | 127.6 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32 | 3.6316 | 74.1 | 3.6264 | 128.9 | 3.6150 | 134.0 | 4.0945 | 140.9 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=8 | 3.6498 | 98.0 | 3.6608 | 129.1 | 3.6336 | 143.8 | 4.0957 | 144.4 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | 22.5239 | 248.4 | 19.8096 | 263.5 | 22.4611 | 253.9 | 19.8062 | 255.8 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | 19.9988 | 263.4 | 19.9642 | 284.1 | 19.9982 | 295.5 | 19.9636 | 302.5 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 4.5938 | 371.4 | 4.6043 | 422.8 | 4.5858 | 449.9 | 4.6037 | 424.8 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32 | 4.5954 | 344.8 | 4.5981 | 369.1 | 4.5765 | 402.8 | 4.6122 | 377.5 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | 26.8572 | 524.6 | 24.6265 | 592.2 | 25.6799 | 565.1 | 27.7079 | 579.1 |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 1.8070 | 166.9 | 1.9106 | 170.2 | 2.8747 | 183.9 | 2.9247 | 190.2 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 33.7603 | 313.0 | 31.6363 | 308.8 | 33.8344 | 310.2 | 32.7599 | 295.5 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1 | 31.8712 | 305.4 | 31.5361 | 323.4 | 32.7169 | 302.2 | 32.1633 | 299.2 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 266.4829 | 376.8 | 265.6037 | 373.1 | 265.7763 | 367.2 | 265.7277 | 389.9 |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing | 27.1770 | - | 27.1591 | - | 28.2068 | - | 28.2121 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing | 62.9096 | - | 62.9904 | - | 62.5168 | - | 62.5695 | - |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.0148 | 60.5 | 1.9764 | 105.5 | 2.0096 | 122.8 | 2.0600 | 107.9 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | 1.9466 | 82.6 | 1.9857 | 122.9 | 1.9766 | 145.0 | 2.0153 | 128.6 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1 | 13.1257 | 253.0 | 13.4204 | 271.8 | 13.2788 | 263.5 | 13.3613 | 275.2 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.5968 | 223.2 | 2.6108 | 276.6 | 2.5882 | 286.4 | 2.5960 | 273.4 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.5447 | 185.9 | 2.5566 | 212.8 | 2.5237 | 225.2 | 2.5375 | 208.2 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1 | 16.1257 | 452.4 | 15.7265 | 497.6 | 15.9902 | 508.8 | 15.6050 | 539.9 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | 23.8886 | 554.1 | 23.4448 | 567.2 | 23.9759 | 567.8 | 24.2670 | 571.8 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1 | 23.9472 | 556.1 | 23.5687 | 585.8 | 23.6675 | 596.4 | 23.4754 | 588.0 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | 178.9139 | 613.1 | 178.2723 | 614.1 | 179.2626 | 615.2 | 178.1298 | 632.5 |

## Per cell

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x444040000000, copy home 0x444140000000, direct level 0x444200000000, copy level 0x4442c0000000
- factor effect within the cell: on the direct route 0.3327 [0.3326, 0.3328] ms, on the copy route 0.0175 [0.0113, 0.0216] ms; change relative to the copy call at home: +305.8 %
- per repetition: direct home 8.43e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.8 SMMU translation requests; direct level 1.341e+08 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x4dfa80000000, copy home 0x4dfb40000000, direct level 0x4dfc00000000, copy level 0x4dfcc0000000
- factor effect within the cell: on the direct route -1.4449 [-1.4450, -1.4446] ms, on the copy route -0.0670 [-0.0744, -0.0598] ms; change relative to the copy call at home: -723.7 %
- per repetition: direct home 5.366e+08 link read bytes and 0 SMMU translation requests; copy home 3.354e+07 link read bytes and 533.1 SMMU translation requests; direct level 8.429e+06 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4bd980000000, copy home 0x4bda80000000, direct level 0x4bdb40000000, copy level 0x4bdc00000000
- factor effect within the cell: on the direct route -0.0797 [-0.0797, -0.0796] ms, on the copy route -0.1193 [-0.1196, -0.1190] ms; change relative to the copy call at home: +22.2 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 520.4 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=none,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=tiling

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x519000000000, copy home 0x519100000000, direct level 0x519200000000, copy level 0x5192c0000000
- factor effect within the cell: on the direct route 9.9058 [9.5743, 9.9296] ms, on the copy route -0.5334 [-0.5371, -0.5272] ms; change relative to the copy call at home: +160.4 %
- per repetition: direct home 6.422e+09 link read bytes and 3.625e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 1.309e+10 link read bytes and 3.578e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=none,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=tiling

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x482140000000, copy home 0x482240000000, direct level 0x482340000000, copy level 0x482400000000
- factor effect within the cell: on the direct route -0.5258 [-0.5271, -0.5218] ms, on the copy route -0.4784 [-0.4808, -0.4737] ms; change relative to the copy call at home: -1.2 %
- per repetition: direct home 0 link read bytes and 5474 SMMU translation requests; copy home 0 link read bytes and 5399 SMMU translation requests; direct level 0 link read bytes and 9240 SMMU translation requests; copy level 0 link read bytes and 5344 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=1024,kernel=k6,placement=cpu,type=four,update=atomic,vary=update

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x465d40000000, copy home 0x465e40000000, direct level 0x465f00000000, copy level 0x465fc0000000
- factor effect within the cell: on the direct route -0.0805 [-0.0910, -0.0752] ms, on the copy route -0.1615 [-0.1664, -0.1591] ms; change relative to the copy call at home: +1.1 %
- per repetition: direct home 0 link read bytes and 4193 SMMU translation requests; copy home 1.074e+09 link read bytes and 3.278e+04 SMMU translation requests; direct level 1.074e+09 link read bytes and 4554 SMMU translation requests; copy level 1.074e+09 link read bytes and 3.278e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,type=four,vary=generator

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x43de00000000, copy home 0x43df00000000, direct level 0x43dfc0000000, copy level 0x43e080000000
- factor effect within the cell: on the direct route 157.8782 [157.7968, 158.9847] ms, on the copy route 64.0234 [63.0107, 64.0484] ms; change relative to the copy call at home: +2258.1 %
- per repetition: direct home 3.199e+09 link read bytes and 0 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.689e+04 SMMU translation requests; direct level 2.853e+09 link read bytes and 0 SMMU translation requests; copy level 1.074e+09 link read bytes and 1.689e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,type=four,vary=generator

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x46a1c0000000, copy home 0x46a2c0000000, direct level 0x46a380000000, copy level 0x46a440000000
- factor effect within the cell: on the direct route 64.6016 [63.6866, 64.6248] ms, on the copy route 64.1821 [63.2587, 64.2006] ms; change relative to the copy call at home: +24.6 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 0 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x476e40000000, copy home 0x476ec0000000, direct level 0x476f40000000, copy level 0x476fc0000000
- factor effect within the cell: on the direct route -0.0015 [-0.0015, -0.0014] ms, on the copy route -0.0004 [-0.0006, -0.0001] ms; change relative to the copy call at home: -0.5 %
- per repetition: direct home 6.711e+07 link read bytes and 2133 SMMU translation requests; copy home 6.711e+07 link read bytes and 1043 SMMU translation requests; direct level 6.711e+07 link read bytes and 1878 SMMU translation requests; copy level 6.711e+07 link read bytes and 1044 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x567440000000, copy home 0x5674c0000000, direct level 0x567580000000, copy level 0x567600000000
- factor effect within the cell: on the direct route 0.1839 [0.1836, 0.1842] ms, on the copy route 0.1683 [0.1666, 0.1688] ms; change relative to the copy call at home: +6.4 %
- per repetition: direct home 6.711e+07 link read bytes and 2018 SMMU translation requests; copy home 6.711e+07 link read bytes and 1042 SMMU translation requests; direct level 6.711e+07 link read bytes and 1509 SMMU translation requests; copy level 6.711e+07 link read bytes and 1060 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x4f9000000000, copy home 0x4f9080000000, direct level 0x4f9100000000, copy level 0x4f9180000000
- factor effect within the cell: on the direct route 0.1271 [0.1266, 0.1275] ms, on the copy route 0.1219 [0.1215, 0.1224] ms; change relative to the copy call at home: +5.7 %
- per repetition: direct home 0 link read bytes and 2877 SMMU translation requests; copy home 0 link read bytes and 3865 SMMU translation requests; direct level 0 link read bytes and 2044 SMMU translation requests; copy level 0 link read bytes and 1540 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x439700000000, copy home 0x4397c0000000, direct level 0x439840000000, copy level 0x4398c0000000
- factor effect within the cell: on the direct route 0.1462 [0.1460, 0.1464] ms, on the copy route 0.1433 [0.1429, 0.1438] ms; change relative to the copy call at home: +3.3 %
- per repetition: direct home 0 link read bytes and 2977 SMMU translation requests; copy home 0 link read bytes and 3898 SMMU translation requests; direct level 0 link read bytes and 2103 SMMU translation requests; copy level 0 link read bytes and 1585 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x5f8e00000000, copy home 0x5f8f00000000, direct level 0x5f8fc0000000, copy level 0x5f9080000000
- factor effect within the cell: on the direct route -0.2622 [-0.2683, -0.2550] ms, on the copy route -0.6220 [-1.0870, -0.6012] ms; change relative to the copy call at home: +8.3 %
- per repetition: direct home 3.197e+09 link read bytes and 0 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.689e+04 SMMU translation requests; direct level 3.197e+09 link read bytes and 0 SMMU translation requests; copy level 1.074e+09 link read bytes and 1.689e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x54f9c0000000, copy home 0x54fa80000000, direct level 0x54fb40000000, copy level 0x54fc40000000
- factor effect within the cell: on the direct route 0.0000 [-0.0011, 0.0011] ms, on the copy route -0.0103 [-0.0107, -0.0095] ms; change relative to the copy call at home: +0.6 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 0 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4eafc0000000, copy home 0x4eb080000000, direct level 0x4eb140000000, copy level 0x4eb200000000
- factor effect within the cell: on the direct route 0.0207 [0.0206, 0.0208] ms, on the copy route 0.0185 [0.0182, 0.0186] ms; change relative to the copy call at home: +3.1 %
- per repetition: direct home 8.429e+06 link read bytes and 316.3 SMMU translation requests; copy home 8.38e+06 link read bytes and 131.3 SMMU translation requests; direct level 8.429e+06 link read bytes and 300.4 SMMU translation requests; copy level 8.38e+06 link read bytes and 142.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x5a0540000000, copy home 0x5a0640000000, direct level 0x5a0700000000, copy level 0x5a07c0000000
- factor effect within the cell: on the direct route 0.0034 [0.0026, 0.0042] ms, on the copy route 0.5877 [0.5873, 0.5888] ms; change relative to the copy call at home: -597.3 %
- per repetition: direct home 5.366e+08 link read bytes and 859.8 SMMU translation requests; copy home 0 link read bytes and 14.72 SMMU translation requests; direct level 5.366e+08 link read bytes and 845.9 SMMU translation requests; copy level 1.074e+08 link read bytes and 2.334e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5636c0000000, copy home 0x5637c0000000, direct level 0x563880000000, copy level 0x563940000000
- factor effect within the cell: on the direct route 0.0009 [0.0005, 0.0012] ms, on the copy route 0.5690 [0.5686, 0.5696] ms; change relative to the copy call at home: -1304.5 %
- per repetition: direct home 8.429e+06 link read bytes and 332.8 SMMU translation requests; copy home 0 link read bytes and 15.04 SMMU translation requests; direct level 8.429e+06 link read bytes and 326.4 SMMU translation requests; copy level 1.074e+08 link read bytes and 2.198e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x533500000000, copy home 0x5335c0000000, direct level 0x533680000000, copy level 0x533740000000
- factor effect within the cell: on the direct route 0.0083 [0.0076, 0.0095] ms, on the copy route 0.6596 [0.6588, 0.6604] ms; change relative to the copy call at home: -664.0 %
- per repetition: direct home 5.366e+08 link read bytes and 824.8 SMMU translation requests; copy home 0 link read bytes and 14.4 SMMU translation requests; direct level 5.366e+08 link read bytes and 808.1 SMMU translation requests; copy level 1.074e+08 link read bytes and 5.06e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=8

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x5166c0000000, copy home 0x5167c0000000, direct level 0x516880000000, copy level 0x516940000000
- factor effect within the cell: on the direct route 0.0010 [0.0008, 0.0012] ms, on the copy route 0.6557 [0.6550, 0.6562] ms; change relative to the copy call at home: -1497.1 %
- per repetition: direct home 8.428e+06 link read bytes and 329.2 SMMU translation requests; copy home 0 link read bytes and 14.72 SMMU translation requests; direct level 8.428e+06 link read bytes and 326.7 SMMU translation requests; copy level 1.074e+08 link read bytes and 5.06e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5cf6c0000000, copy home 0x5cf7c0000000, direct level 0x5cf880000000, copy level 0x5cf940000000
- factor effect within the cell: on the direct route 0.0225 [0.0207, 0.0239] ms, on the copy route 0.0020 [0.0015, 0.0032] ms; change relative to the copy call at home: +9.3 %
- per repetition: direct home 5.366e+08 link read bytes and 386.9 SMMU translation requests; copy home 3.354e+07 link read bytes and 538.6 SMMU translation requests; direct level 5.366e+08 link read bytes and 390.6 SMMU translation requests; copy level 3.354e+07 link read bytes and 539 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x591940000000, copy home 0x591a00000000, direct level 0x591ac0000000, copy level 0x591b80000000
- factor effect within the cell: on the direct route 0.0011 [0.0006, 0.0015] ms, on the copy route 0.0001 [-0.0006, 0.0008] ms; change relative to the copy call at home: +0.9 %
- per repetition: direct home 8.429e+06 link read bytes and 324.9 SMMU translation requests; copy home 8.38e+06 link read bytes and 150.6 SMMU translation requests; direct level 8.428e+06 link read bytes and 326.4 SMMU translation requests; copy level 8.38e+06 link read bytes and 151.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5ba8c0000000, copy home 0x5ba980000000, direct level 0x5baa40000000, copy level 0x5bab00000000
- factor effect within the cell: on the direct route 0.0035 [0.0030, 0.0037] ms, on the copy route 0.1710 [0.1700, 0.1714] ms; change relative to the copy call at home: -152.8 %
- per repetition: direct home 0 link read bytes and 946.3 SMMU translation requests; copy home 0 link read bytes and 16 SMMU translation requests; direct level 0 link read bytes and 949.8 SMMU translation requests; copy level 0 link read bytes and 3.906e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x475c80000000, copy home 0x475d40000000, direct level 0x475e00000000, copy level 0x475ec0000000
- factor effect within the cell: on the direct route -0.0022 [-0.0023, -0.0020] ms, on the copy route 0.6221 [0.6210, 0.6230] ms; change relative to the copy call at home: -568.4 %
- per repetition: direct home 0 link read bytes and 950.2 SMMU translation requests; copy home 0 link read bytes and 16 SMMU translation requests; direct level 0 link read bytes and 951.8 SMMU translation requests; copy level 0 link read bytes and 4.786e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x547680000000, copy home 0x5477c0000000, direct level 0x547880000000, copy level 0x547940000000
- factor effect within the cell: on the direct route 0.0020 [0.0016, 0.0024] ms, on the copy route -0.0001 [-0.0003, 0.0004] ms; change relative to the copy call at home: +0.9 %
- per repetition: direct home 0 link read bytes and 949.7 SMMU translation requests; copy home 0 link read bytes and 549.4 SMMU translation requests; direct level 0 link read bytes and 949.3 SMMU translation requests; copy level 0 link read bytes and 548.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5ab580000000, copy home 0x5aba40000000, direct level 0x5abec0000000, copy level 0x5ac340000000
- factor effect within the cell: on the direct route -0.0317 [-0.0428, -0.0151] ms, on the copy route -2.4512 [-2.4557, -2.4471] ms; change relative to the copy call at home: +5.4 %
- per repetition: direct home 3.355e+07 link read bytes and 2.025e+06 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; direct level 3.355e+07 link read bytes and 2.017e+06 SMMU translation requests; copy level 1.723e+10 link read bytes and 2.623e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5e5a00000000, copy home 0x5e5ec0000000, direct level 0x5e6340000000, copy level 0x5e6800000000
- factor effect within the cell: on the direct route 0.0051 [-0.0626, 0.1472] ms, on the copy route 4.6401 [4.6382, 4.7014] ms; change relative to the copy call at home: -908.6 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 0 link read bytes and 3.763 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy level 1.718e+09 link read bytes and 2.941e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x455a00000000, copy home 0x455e80000000, direct level 0x456300000000, copy level 0x4567c0000000
- factor effect within the cell: on the direct route 0.0410 [-0.1922, 0.1833] ms, on the copy route 10.1500 [10.1359, 10.1582] ms; change relative to the copy call at home: -1971.4 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 0 link read bytes and 2.95 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy level 1.718e+09 link read bytes and 6.669e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x55ae80000000, copy home 0x55b300000000, direct level 0x55b780000000, copy level 0x55bc40000000
- factor effect within the cell: on the direct route 0.0265 [-0.2124, 0.2692] ms, on the copy route -2.5437 [-2.5611, -2.4967] ms; change relative to the copy call at home: +5.5 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy level 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4d4e00000000, copy home 0x4d4f00000000, direct level 0x4d5000000000, copy level 0x4d5100000000
- factor effect within the cell: on the direct route -3.5379 [-3.5654, -3.5025] ms, on the copy route -0.0466 [-0.0550, -0.0413] ms; change relative to the copy call at home: -53.6 %
- per repetition: direct home 6.422e+09 link read bytes and 3.608e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.641e+04 SMMU translation requests; direct level 6.423e+09 link read bytes and 3.617e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.641e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x434c00000000, copy home 0x434d00000000, direct level 0x434dc0000000, copy level 0x434ec0000000
- factor effect within the cell: on the direct route -0.0237 [-0.0258, -0.0214] ms, on the copy route 0.0026 [0.0015, 0.0038] ms; change relative to the copy call at home: -0.7 %
- per repetition: direct home 0 link read bytes and 5517 SMMU translation requests; copy home 0 link read bytes and 6058 SMMU translation requests; direct level 0 link read bytes and 5481 SMMU translation requests; copy level 0 link read bytes and 6044 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4b8c40000000, copy home 0x4b8d80000000, direct level 0x4b8e40000000, copy level 0x4b8f40000000
- factor effect within the cell: on the direct route -3.4124 [-3.4320, -3.3756] ms, on the copy route 0.2984 [0.2939, 0.3019] ms; change relative to the copy call at home: -73.6 %
- per repetition: direct home 6.422e+09 link read bytes and 3.605e+04 SMMU translation requests; copy home 0 link read bytes and 8209 SMMU translation requests; direct level 6.423e+09 link read bytes and 3.581e+04 SMMU translation requests; copy level 5.369e+07 link read bytes and 2.437e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4e84c0000000, copy home 0x4e8600000000, direct level 0x4e86c0000000, copy level 0x4e87c0000000
- factor effect within the cell: on the direct route -3.5710 [-3.6135, -3.5166] ms, on the copy route 0.3408 [0.3333, 0.3478] ms; change relative to the copy call at home: -77.9 %
- per repetition: direct home 6.422e+09 link read bytes and 3.591e+04 SMMU translation requests; copy home 0 link read bytes and 8209 SMMU translation requests; direct level 6.423e+09 link read bytes and 3.597e+04 SMMU translation requests; copy level 5.369e+07 link read bytes and 3.312e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4c2c40000000, copy home 0x4c2d40000000, direct level 0x4c2e00000000, copy level 0x4c2f00000000
- factor effect within the cell: on the direct route -3.4057 [-3.4261, -3.3887] ms, on the copy route 0.0724 [0.0672, 0.0758] ms; change relative to the copy call at home: -53.4 %
- per repetition: direct home 6.422e+09 link read bytes and 3.617e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 6.423e+09 link read bytes and 3.591e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.647e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4360c0000000, copy home 0x436200000000, direct level 0x4362c0000000, copy level 0x4363c0000000
- factor effect within the cell: on the direct route 0.0127 [0.0065, 0.0152] ms, on the copy route 0.0892 [0.0861, 0.0912] ms; change relative to the copy call at home: -2.1 %
- per repetition: direct home 0 link read bytes and 4.277e+04 SMMU translation requests; copy home 0 link read bytes and 1.282e+04 SMMU translation requests; direct level 0 link read bytes and 4.482e+04 SMMU translation requests; copy level 0 link read bytes and 2.99e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x5bd340000000, copy home 0x5bd440000000, direct level 0x5bd500000000, copy level 0x5bd600000000
- factor effect within the cell: on the direct route 0.0375 [0.0348, 0.0408] ms, on the copy route 0.3081 [0.3069, 0.3100] ms; change relative to the copy call at home: -7.6 %
- per repetition: direct home 0 link read bytes and 3.845e+04 SMMU translation requests; copy home 0 link read bytes and 1.294e+04 SMMU translation requests; direct level 0 link read bytes and 4.162e+04 SMMU translation requests; copy level 0 link read bytes and 3.579e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x41c400000000, copy home 0x41c540000000, direct level 0x41c600000000, copy level 0x41c700000000
- factor effect within the cell: on the direct route 0.0877 [0.0811, 0.0919] ms, on the copy route -0.0165 [-0.0258, -0.0092] ms; change relative to the copy call at home: +2.5 %
- per repetition: direct home 0 link read bytes and 4.268e+04 SMMU translation requests; copy home 0 link read bytes and 3.117e+04 SMMU translation requests; direct level 0 link read bytes and 4.14e+04 SMMU translation requests; copy level 0 link read bytes and 3.071e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5fd0c0000000, copy home 0x5fd340000000, direct level 0x5fd5c0000000, copy level 0x5fd880000000
- factor effect within the cell: on the direct route 0.0159 [0.0087, 0.0224] ms, on the copy route 1.1637 [1.1511, 1.1703] ms; change relative to the copy call at home: -205.9 %
- per repetition: direct home 0 link read bytes and 1.33e+05 SMMU translation requests; copy home 0 link read bytes and 16.86 SMMU translation requests; direct level 0 link read bytes and 1.326e+05 SMMU translation requests; copy level 0 link read bytes and 3.144e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x44df40000000, copy home 0x44e200000000, direct level 0x44e480000000, copy level 0x44e740000000
- factor effect within the cell: on the direct route 0.0221 [0.0159, 0.0286] ms, on the copy route 4.8639 [4.8382, 4.8695] ms; change relative to the copy call at home: -860.0 %
- per repetition: direct home 0 link read bytes and 1.327e+05 SMMU translation requests; copy home 0 link read bytes and 16.76 SMMU translation requests; direct level 0 link read bytes and 1.327e+05 SMMU translation requests; copy level 0 link read bytes and 3.436e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x4eda40000000, copy home 0x4edd00000000, direct level 0x4edf80000000, copy level 0x4ee240000000
- factor effect within the cell: on the direct route 0.0184 [0.0169, 0.0202] ms, on the copy route -0.0121 [-0.0162, -0.0088] ms; change relative to the copy call at home: +0.5 %
- per repetition: direct home 0 link read bytes and 1.328e+05 SMMU translation requests; copy home 0 link read bytes and 2.733e+05 SMMU translation requests; direct level 0 link read bytes and 1.326e+05 SMMU translation requests; copy level 0 link read bytes and 2.898e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8

- seed 67; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x41a280000000, copy home 0x41a380000000, direct level 0x41a440000000, copy level 0x41a500000000
- factor effect within the cell: on the direct route 0.3656 [0.3654, 0.3657] ms, on the copy route 0.0292 [0.0185, 0.0366] ms; change relative to the copy call at home: +306.0 %
- per repetition: direct home 8.429e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.8 SMMU translation requests; direct level 1.341e+08 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.9 SMMU translation requests; multiplexed rows voided: 0

