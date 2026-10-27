# Four-variant cells: direct and copy route at home and at a level of one factor, recomputed from raw rows

Times are per repetition in ms (one pass for the direct route, one complete call for the copy route). Each round runs the four variants once in the order the seed drew; the route difference at home (A - B) and at the level (C - D) and the change of the route difference, (C - D) - (A - B), are formed within each round and given as median with 95 % rank interval. A negative route difference means direct access is faster; a negative change means the level moved the comparison towards direct access. The relative change is the change over the route difference at home, given only where that difference excludes zero. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | level | direct home ms | copy home ms | direct level ms | copy level ms | route difference home ms [interval] | route difference level ms [interval] | change ms [interval] | relative change | rounds | change excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0378 | 0.1090 | 0.3713 | 0.1467 | -0.0712 [-0.0778, -0.0702] | 0.2243 [0.2155, 0.2258] | 0.2961 [0.2875, 0.3038] | -415.6 % | 100 | yes | pass |
| at=8,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 1.4848 | 0.1851 | 0.0375 | 0.1303 | 1.2995 [1.2991, 1.2999] | -0.0927 [-0.1007, -0.0855] | -1.3923 [-1.3994, -1.3791] | -107.1 % | 100 | yes | pass |
| at=8,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 0.0957 | 0.1811 | 0.0160 | 0.0583 | -0.0854 [-0.0861, -0.0851] | -0.0423 [-0.0424, -0.0422] | 0.0430 [0.0426, 0.0443] | -50.3 % | 30 | yes | pass |
| at=none,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=tiling | tiling | none | 26.0992 | 6.4875 | 35.3229 | 5.9932 | 19.6066 [19.5923, 19.6329] | 29.3241 [29.2092, 29.5653] | 9.7176 [9.6169, 9.9176] | +49.6 % | 10 | yes | pass |
| at=none,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=tiling | tiling | none | 3.2760 | 3.8873 | 2.7529 | 3.3858 | -0.6099 [-0.6136, -0.6077] | -0.6329 [-0.6342, -0.6315] | -0.0225 [-0.0253, -0.0176] | +3.7 % | 100 | yes | pass |
| at=plain,footprint-mib=1024,kernel=k6,placement=cpu,type=four,update=atomic,vary=update | update | plain | 6.0346 | 7.3593 | 5.9338 | 7.2092 | -1.3256 [-1.3292, -1.3194] | -1.2749 [-1.2800, -1.2696] | 0.0533 [0.0461, 0.0550] | -4.0 % | 20 | yes | pass |
| at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,type=four,vary=generator | generator | rmat | 1.2735 | 1.7691 | 66.0143 | 65.9924 | -0.4952 [-0.4958, -0.4939] | 0.0258 [0.0167, 0.0435] | 0.5189 [0.5091, 0.5369] | -104.8 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | sharing | shared | 0.1934 | 0.2420 | 0.1920 | 0.2430 | -0.0487 [-0.0488, -0.0485] | -0.0510 [-0.0511, -0.0509] | -0.0024 [-0.0026, -0.0022] | +4.9 % | 80 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 0.1924 | 0.2416 | 0.3760 | 0.4068 | -0.0492 [-0.0495, -0.0484] | -0.0307 [-0.0321, -0.0304] | 0.0181 [0.0172, 0.0190] | -36.7 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | sharing | shared | 0.0381 | 0.0943 | 0.1646 | 0.2189 | -0.0563 [-0.0565, -0.0561] | -0.0540 [-0.0547, -0.0535] | 0.0023 [0.0013, 0.0030] | -4.1 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | sharing | shared | 0.0355 | 0.0910 | 0.1784 | 0.2313 | -0.0556 [-0.0557, -0.0555] | -0.0526 [-0.0529, -0.0519] | 0.0034 [0.0028, 0.0042] | -6.0 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | sharing | shared | 30.7927 | 4.2034 | 30.4523 | 4.0819 | 26.5885 [26.5834, 26.5956] | 26.3700 [26.3638, 26.3777] | -0.2191 [-0.2314, -0.2078] | -0.8 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing | sharing | shared | 1.2759 | 1.7636 | 1.2751 | 1.7628 | -0.4875 [-0.4882, -0.4870] | -0.4876 [-0.4880, -0.4870] | -0.0002 [-0.0008, 0.0004] | +0.0 % | 100 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 1.5144 | 0.0987 | 1.5156 | 0.7581 | 1.4154 [1.4149, 1.4162] | 0.7570 [0.7565, 0.7577] | -0.6587 [-0.6598, -0.6578] | -46.5 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0503 | 0.0434 | 0.0483 | 0.7013 | 0.0067 [0.0062, 0.0072] | -0.6534 [-0.6540, -0.6528] | -0.6608 [-0.6616, -0.6598] | -9865.3 % | 80 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=runs,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 1.5089 | 0.0972 | 1.5085 | 741.7749 | 1.4117 [1.4107, 1.4124] | -740.2667 [-741.6268, -739.9386] | -741.6782 [-743.0389, -741.3494] | -52538.5 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=runs,type=four,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0501 | 0.0431 | 0.0492 | 735.8944 | 0.0070 [0.0065, 0.0073] | -735.8450 [-738.2893, -732.5505] | -735.8513 [-738.2966, -732.5577] | -10542524.5 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | sharing | shared | 0.0510 | 0.0861 | 0.0516 | 0.0867 | -0.0350 [-0.0352, -0.0348] | -0.0348 [-0.0352, -0.0344] | 0.0004 [-0.0001, 0.0008] | -1.1 % | 100 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.1166 | 0.1099 | 0.1167 | 0.7344 | 0.0067 [0.0064, 0.0072] | -0.6176 [-0.6183, -0.6165] | -0.6241 [-0.6252, -0.6233] | -9346.2 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=runs,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.1134 | 0.1109 | 0.1159 | 706.9846 | 0.0025 [0.0022, 0.0027] | -706.8691 [-708.0348, -705.4991] | -706.8712 [-708.0379, -705.5005] | -28236898.8 % | 80 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.1260 | 0.2220 | 0.1261 | 0.2211 | -0.0960 [-0.0966, -0.0955] | -0.0944 [-0.0948, -0.0942] | 0.0017 [0.0012, 0.0023] | -1.8 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 7.2598 | 42.4863 | 7.2346 | 42.3788 | -35.2268 [-35.2287, -35.2255] | -35.1447 [-35.1475, -35.1408] | 0.0840 [0.0793, 0.0907] | -0.2 % | 80 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1 | sharing | shared | 433.2522 | 0.5134 | 433.4681 | 10.7053 | 432.7390 [432.7041, 432.8025] | 422.7654 [422.7053, 422.8708] | -9.9757 [-10.0597, -9.8569] | -2.3 % | 10 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 433.3125 | 43.8591 | 433.4542 | 43.0426 | 389.4566 [389.4273, 389.4771] | 390.4048 [390.3700, 390.4582] | 0.9641 [0.9138, 1.0010] | +0.2 % | 20 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing | sharing | shared | 26.2095 | 6.5082 | 22.8106 | 6.4692 | 19.7027 [19.6942, 19.7084] | 16.3412 [16.3295, 16.3503] | -3.3600 [-3.3688, -3.3508] | -17.1 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing | sharing | shared | 3.2400 | 3.8589 | 3.2643 | 3.8611 | -0.6198 [-0.6205, -0.6178] | -0.5969 [-0.5980, -0.5961] | 0.0232 [0.0209, 0.0239] | -3.7 % | 90 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=runs,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 27.0198 | 5.0447 | 23.0583 | 369.2012 | 21.9728 [21.9650, 21.9817] | -346.1422 [-346.7013, -345.6215] | -368.1159 [-368.6662, -367.6025] | -1675.3 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 26.9432 | 6.4915 | 22.8283 | 6.5545 | 20.4523 [20.4439, 20.4596] | 16.2712 [16.2587, 16.3033] | -4.1837 [-4.1977, -4.1461] | -20.5 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 3.5613 | 3.5544 | 3.6051 | 3.8609 | 0.0070 [0.0060, 0.0077] | -0.2560 [-0.2572, -0.2549] | -0.2635 [-0.2655, -0.2617] | -3784.7 % | 100 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=runs,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 3.4683 | 3.5681 | 3.4953 | 702.7302 | -0.0986 [-0.1040, -0.0950] | -699.2352 [-699.6158, -698.7370] | -699.1357 [-699.5167, -698.6412] | +709292.7 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 3.4831 | 4.0058 | 3.5887 | 3.9828 | -0.5230 [-0.5274, -0.5185] | -0.3931 [-0.3976, -0.3905] | 0.1303 [0.1211, 0.1328] | -24.9 % | 10 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=runs,type=four,vary=sharing,w=0.1 | sharing | shared | 8.0609 | 0.5661 | 8.0857 | 5751.3102 | 7.4942 [7.4920, 7.4969] | -5743.2226 [-5761.6804, -5711.7273] | -5750.7150 [-5769.1768, -5719.2210] | -76735.7 % | 10 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | sharing | shared | 8.0857 | 5.6646 | 8.0988 | 5.6472 | 2.4213 [2.4179, 2.4229] | 2.4526 [2.4493, 2.4557] | 0.0283 [0.0256, 0.0343] | +1.2 % | 100 | yes | pass |
| at=sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8 | scope | sys | 0.0380 | 0.1093 | 0.3995 | 0.1379 | -0.0714 [-0.0775, -0.0704] | 0.2621 [0.2536, 0.2633] | 0.3362 [0.3309, 0.3427] | -471.0 % | 100 | yes | pass |

## Host phases

The CPU phase before every pass, timed on the CPU clock (ms per pass), and the state check's median load latency on the preparing core after the phase (ns per sampled load), per variant.

| cell | direct home CPU ms | direct home state ns | copy home CPU ms | copy home state ns | direct level CPU ms | direct level state ns | copy level CPU ms | copy level state ns |
|---|---|---|---|---|---|---|---|---|
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | 5.2318 | 57.4 | 5.2405 | 75.8 | 5.4245 | 82.5 | 5.4264 | 108.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 2.7234 | 67.9 | 2.7207 | 85.4 | 2.6722 | 88.6 | 2.6712 | 87.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | 4.9710 | 103.0 | 5.1455 | 91.1 | 5.0241 | 128.8 | 5.0227 | 112.6 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | 2.9503 | 61.9 | 3.0165 | 82.8 | 2.8838 | 90.8 | 2.9428 | 81.9 |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | 1.2246 | - | 1.2178 | - | 1.6579 | - | 1.6575 | - |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing | 2.3014 | - | 3.7195 | - | 3.6934 | - | 3.1387 | - |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32 | 3.6485 | 168.5 | 3.6452 | 183.0 | 3.6274 | 206.9 | 4.0936 | 215.9 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=8 | 3.6561 | 114.0 | 3.6497 | 159.8 | 3.6399 | 185.6 | 4.0896 | 182.2 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=runs,type=four,vary=sharing,w=0.1,working-set-mib=32 | 3.5950 | 168.0 | 3.5571 | 181.0 | 3.5593 | 202.4 | 3.5958 | 190.0 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=runs,type=four,vary=sharing,w=0.1,working-set-mib=8 | 3.5736 | 146.2 | 3.5891 | 164.6 | 3.5619 | 193.4 | 3.5899 | 165.8 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | 20.4425 | 262.9 | 20.4487 | 270.4 | 20.6037 | 264.6 | 20.2092 | 274.4 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32 | 4.8079 | 422.4 | 4.7842 | 432.4 | 4.7008 | 436.5 | 4.6391 | 446.2 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=runs,type=four,vary=sharing,w=0.1,working-set-mib=32 | 4.8197 | 415.4 | 4.7906 | 441.6 | 4.7745 | 471.9 | 4.5866 | 470.6 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | 27.7634 | 535.1 | 27.6408 | 579.2 | 27.8301 | 571.8 | 27.6926 | 566.0 |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 1.8343 | 142.4 | 1.8263 | 161.4 | 3.0507 | 177.9 | 3.1513 | 170.2 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1 | 31.8195 | 305.5 | 31.5135 | 317.2 | 31.6515 | 307.0 | 33.0310 | 277.4 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 266.9801 | 370.8 | 268.1826 | 356.5 | 267.6776 | 335.0 | 268.7837 | 312.2 |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing | 27.0990 | - | 27.1043 | - | 28.1799 | - | 28.1928 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing | 62.9101 | - | 63.0130 | - | 62.5023 | - | 62.5549 | - |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=runs,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | 1.9909 | 66.2 | 1.9841 | 107.1 | 1.9844 | 115.1 | 2.0284 | 95.9 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1 | 13.0432 | 249.2 | 13.4540 | 264.9 | 13.0827 | 266.8 | 13.3870 | 278.4 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.6626 | 200.1 | 2.6661 | 243.4 | 2.6131 | 236.4 | 2.5998 | 249.0 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=runs,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.7416 | 189.1 | 2.9671 | 226.9 | 2.6175 | 227.4 | 2.6300 | 229.5 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1 | 16.1070 | 453.9 | 15.8682 | 507.9 | 16.1881 | 513.0 | 15.8235 | 542.8 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=runs,type=four,vary=sharing,w=0.1 | 23.8206 | 549.9 | 23.3950 | 588.1 | 23.8044 | 574.8 | 23.2235 | 593.5 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | 167.7899 | 607.8 | 174.1386 | 618.9 | 167.6507 | 630.1 | 166.3453 | 619.8 |

## Per cell

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x4b46c0000000, copy home 0x4b4780000000, direct level 0x4b4840000000, copy level 0x4b4900000000
- factor effect within the cell: on the direct route 0.3335 [0.3333, 0.3336] ms, on the copy route 0.0368 [0.0297, 0.0456] ms; change relative to the copy call at home: +271.6 %
- per repetition: direct home 8.382e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.8 SMMU translation requests; direct level 1.341e+08 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x4d9b80000000, copy home 0x4d9c80000000, direct level 0x4d9d40000000, copy level 0x4d9e00000000
- factor effect within the cell: on the direct route -1.4473 [-1.4479, -1.4468] ms, on the copy route -0.0554 [-0.0670, -0.0473] ms; change relative to the copy call at home: -752.0 %
- per repetition: direct home 5.365e+08 link read bytes and 0 SMMU translation requests; copy home 3.354e+07 link read bytes and 533.1 SMMU translation requests; direct level 8.382e+06 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4c88c0000000, copy home 0x4c89c0000000, direct level 0x4c8a80000000, copy level 0x4c8b40000000
- factor effect within the cell: on the direct route -0.0798 [-0.0798, -0.0797] ms, on the copy route -0.1228 [-0.1240, -0.1224] ms; change relative to the copy call at home: +23.7 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 519.2 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=none,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=tiling

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x508ec0000000, copy home 0x508fc0000000, direct level 0x5090c0000000, copy level 0x509180000000
- factor effect within the cell: on the direct route 9.2262 [9.1246, 9.4156] ms, on the copy route -0.4955 [-0.5012, -0.4891] ms; change relative to the copy call at home: +149.8 %
- per repetition: direct home 6.422e+09 link read bytes and 3.624e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 1.306e+10 link read bytes and 3.647e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=none,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=tiling

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x54db40000000, copy home 0x54dc40000000, direct level 0x54dd00000000, copy level 0x54de00000000
- factor effect within the cell: on the direct route -0.5232 [-0.5262, -0.5200] ms, on the copy route -0.5014 [-0.5042, -0.4984] ms; change relative to the copy call at home: -0.6 %
- per repetition: direct home 0 link read bytes and 5515 SMMU translation requests; copy home 0 link read bytes and 5461 SMMU translation requests; direct level 0 link read bytes and 8996 SMMU translation requests; copy level 0 link read bytes and 5382 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=1024,kernel=k6,placement=cpu,type=four,update=atomic,vary=update

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x531880000000, copy home 0x531980000000, direct level 0x531a40000000, copy level 0x531b00000000
- factor effect within the cell: on the direct route -0.0991 [-0.1026, -0.0954] ms, on the copy route -0.1508 [-0.1529, -0.1480] ms; change relative to the copy call at home: +0.7 %
- per repetition: direct home 0 link read bytes and 4220 SMMU translation requests; copy home 1.074e+09 link read bytes and 3.278e+04 SMMU translation requests; direct level 1.074e+09 link read bytes and 4595 SMMU translation requests; copy level 1.074e+09 link read bytes and 3.278e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,type=four,vary=generator

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x44fe80000000, copy home 0x44ff80000000, direct level 0x450040000000, copy level 0x450100000000
- factor effect within the cell: on the direct route 64.7352 [63.8202, 64.7616] ms, on the copy route 64.2223 [63.2919, 64.2435] ms; change relative to the copy call at home: +29.3 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 0 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x47f780000000, copy home 0x47f840000000, direct level 0x47f8c0000000, copy level 0x47f940000000
- factor effect within the cell: on the direct route -0.0015 [-0.0016, -0.0014] ms, on the copy route 0.0008 [0.0006, 0.0011] ms; change relative to the copy call at home: -1.0 %
- per repetition: direct home 6.711e+07 link read bytes and 2024 SMMU translation requests; copy home 6.711e+07 link read bytes and 1043 SMMU translation requests; direct level 6.711e+07 link read bytes and 1875 SMMU translation requests; copy level 6.711e+07 link read bytes and 1043 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4da380000000, copy home 0x4da440000000, direct level 0x4da4c0000000, copy level 0x4da540000000
- factor effect within the cell: on the direct route 0.1835 [0.1833, 0.1841] ms, on the copy route 0.1655 [0.1647, 0.1669] ms; change relative to the copy call at home: +7.5 %
- per repetition: direct home 6.711e+07 link read bytes and 2159 SMMU translation requests; copy home 6.711e+07 link read bytes and 1042 SMMU translation requests; direct level 6.711e+07 link read bytes and 1766 SMMU translation requests; copy level 6.711e+07 link read bytes and 1061 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x5ed480000000, copy home 0x5ed540000000, direct level 0x5ed5c0000000, copy level 0x5ed640000000
- factor effect within the cell: on the direct route 0.1264 [0.1260, 0.1271] ms, on the copy route 0.1246 [0.1238, 0.1249] ms; change relative to the copy call at home: +2.4 %
- per repetition: direct home 0 link read bytes and 2857 SMMU translation requests; copy home 0 link read bytes and 3890 SMMU translation requests; direct level 0 link read bytes and 1998 SMMU translation requests; copy level 0 link read bytes and 1556 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x4eb4c0000000, copy home 0x4eb540000000, direct level 0x4eb5c0000000, copy level 0x4eb680000000
- factor effect within the cell: on the direct route 0.1430 [0.1428, 0.1433] ms, on the copy route 0.1402 [0.1398, 0.1404] ms; change relative to the copy call at home: +3.7 %
- per repetition: direct home 0 link read bytes and 2887 SMMU translation requests; copy home 0 link read bytes and 3848 SMMU translation requests; direct level 0 link read bytes and 2080 SMMU translation requests; copy level 0 link read bytes and 1559 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5c8040000000, copy home 0x5c8100000000, direct level 0x5c81c0000000, copy level 0x5c82c0000000
- factor effect within the cell: on the direct route -0.3420 [-0.3510, -0.3363] ms, on the copy route -0.1216 [-0.1245, -0.1192] ms; change relative to the copy call at home: -5.2 %
- per repetition: direct home 3.196e+09 link read bytes and 0 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.689e+04 SMMU translation requests; direct level 3.198e+09 link read bytes and 0 SMMU translation requests; copy level 1.074e+09 link read bytes and 1.689e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x5d67c0000000, copy home 0x5d68c0000000, direct level 0x5d6980000000, copy level 0x5d6a40000000
- factor effect within the cell: on the direct route -0.0009 [-0.0014, -0.0004] ms, on the copy route -0.0010 [-0.0013, -0.0005] ms; change relative to the copy call at home: -0.0 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 0 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x574700000000, copy home 0x574800000000, direct level 0x5748c0000000, copy level 0x574980000000
- factor effect within the cell: on the direct route 0.0017 [0.0010, 0.0024] ms, on the copy route 0.6596 [0.6591, 0.6603] ms; change relative to the copy call at home: -667.1 %
- per repetition: direct home 5.365e+08 link read bytes and 833.4 SMMU translation requests; copy home 0 link read bytes and 14.4 SMMU translation requests; direct level 5.365e+08 link read bytes and 827.7 SMMU translation requests; copy level 1.074e+08 link read bytes and 5.06e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=8

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5f0500000000, copy home 0x5f05c0000000, direct level 0x5f0680000000, copy level 0x5f0740000000
- factor effect within the cell: on the direct route -0.0016 [-0.0023, -0.0013] ms, on the copy route 0.6581 [0.6576, 0.6590] ms; change relative to the copy call at home: -1522.7 %
- per repetition: direct home 8.382e+06 link read bytes and 332.6 SMMU translation requests; copy home 0 link read bytes and 15.04 SMMU translation requests; direct level 8.382e+06 link read bytes and 335.5 SMMU translation requests; copy level 1.074e+08 link read bytes and 5.053e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=runs,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x529740000000, copy home 0x529800000000, direct level 0x5298c0000000, copy level 0x529980000000
- factor effect within the cell: on the direct route -0.0008 [-0.0023, 0.0007] ms, on the copy route 741.6779 [741.3508, 743.0370] ms; change relative to the copy call at home: -763091.1 %
- per repetition: direct home 5.365e+08 link read bytes and 815.9 SMMU translation requests; copy home 0 link read bytes and 14.56 SMMU translation requests; direct level 5.366e+08 link read bytes and 847.3 SMMU translation requests; copy level 0 link read bytes and 12.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=runs,type=four,vary=sharing,w=0.1,working-set-mib=8

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x54c9c0000000, copy home 0x54ca80000000, direct level 0x54cb40000000, copy level 0x54cc00000000
- factor effect within the cell: on the direct route -0.0007 [-0.0012, -0.0004] ms, on the copy route 735.8508 [732.5570, 738.2956] ms; change relative to the copy call at home: -1708447.0 %
- per repetition: direct home 8.382e+06 link read bytes and 328.6 SMMU translation requests; copy home 0 link read bytes and 14.4 SMMU translation requests; direct level 8.382e+06 link read bytes and 329.9 SMMU translation requests; copy level 0 link read bytes and 14.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x4a8840000000, copy home 0x4a8940000000, direct level 0x4a8a00000000, copy level 0x4a8ac0000000
- factor effect within the cell: on the direct route 0.0007 [0.0005, 0.0011] ms, on the copy route 0.0005 [0.0001, 0.0009] ms; change relative to the copy call at home: +0.5 %
- per repetition: direct home 8.382e+06 link read bytes and 319.1 SMMU translation requests; copy home 8.38e+06 link read bytes and 142.7 SMMU translation requests; direct level 8.382e+06 link read bytes and 318.3 SMMU translation requests; copy level 8.38e+06 link read bytes and 143.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5cc5c0000000, copy home 0x5cc6c0000000, direct level 0x5cc780000000, copy level 0x5cc840000000
- factor effect within the cell: on the direct route 0.0002 [-0.0005, 0.0004] ms, on the copy route 0.6242 [0.6236, 0.6252] ms; change relative to the copy call at home: -568.0 %
- per repetition: direct home 0 link read bytes and 945.4 SMMU translation requests; copy home 0 link read bytes and 16 SMMU translation requests; direct level 0 link read bytes and 952.3 SMMU translation requests; copy level 0 link read bytes and 4.774e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=runs,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x544ec0000000, copy home 0x545000000000, direct level 0x5450c0000000, copy level 0x545180000000
- factor effect within the cell: on the direct route 0.0026 [0.0023, 0.0029] ms, on the copy route 706.8734 [705.5035, 708.0404] ms; change relative to the copy call at home: -637611.3 %
- per repetition: direct home 0 link read bytes and 952.1 SMMU translation requests; copy home 0 link read bytes and 16 SMMU translation requests; direct level 0 link read bytes and 952.1 SMMU translation requests; copy level 0 link read bytes and 16 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x544300000000, copy home 0x544400000000, direct level 0x5444c0000000, copy level 0x544580000000
- factor effect within the cell: on the direct route 0.0005 [0.0003, 0.0008] ms, on the copy route -0.0012 [-0.0016, -0.0007] ms; change relative to the copy call at home: +0.8 %
- per repetition: direct home 0 link read bytes and 925.8 SMMU translation requests; copy home 0 link read bytes and 548.2 SMMU translation requests; direct level 0 link read bytes and 923.2 SMMU translation requests; copy level 0 link read bytes and 547.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x527fc0000000, copy home 0x528480000000, direct level 0x528900000000, copy level 0x528d80000000
- factor effect within the cell: on the direct route -0.0238 [-0.0279, -0.0184] ms, on the copy route -0.1076 [-0.1083, -0.1063] ms; change relative to the copy call at home: +0.2 %
- per repetition: direct home 3.355e+07 link read bytes and 2.026e+06 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; direct level 3.355e+07 link read bytes and 2.017e+06 SMMU translation requests; copy level 1.723e+10 link read bytes and 2.623e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x586740000000, copy home 0x586c00000000, direct level 0x587080000000, copy level 0x587540000000
- factor effect within the cell: on the direct route 0.2207 [0.1232, 0.3398] ms, on the copy route 10.1921 [10.1869, 10.1982] ms; change relative to the copy call at home: -1942.9 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 0 link read bytes and 3.375 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy level 1.718e+09 link read bytes and 6.497e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x413940000000, copy home 0x413dc0000000, direct level 0x414240000000, copy level 0x414700000000
- factor effect within the cell: on the direct route 0.1313 [0.0996, 0.1730] ms, on the copy route -0.8149 [-0.8244, -0.8106] ms; change relative to the copy call at home: +2.2 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy level 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x548d80000000, copy home 0x548ec0000000, direct level 0x548fc0000000, copy level 0x549080000000
- factor effect within the cell: on the direct route -3.4002 [-3.4096, -3.3916] ms, on the copy route -0.0388 [-0.0409, -0.0351] ms; change relative to the copy call at home: -51.6 %
- per repetition: direct home 6.422e+09 link read bytes and 3616 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 6.423e+09 link read bytes and 3604 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5b3f40000000, copy home 0x5b4040000000, direct level 0x5b4100000000, copy level 0x5b4200000000
- factor effect within the cell: on the direct route 0.0239 [0.0223, 0.0263] ms, on the copy route 0.0023 [0.0011, 0.0033] ms; change relative to the copy call at home: +0.6 %
- per repetition: direct home 0 link read bytes and 3866 SMMU translation requests; copy home 0 link read bytes and 3640 SMMU translation requests; direct level 0 link read bytes and 3848 SMMU translation requests; copy level 0 link read bytes and 3619 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=runs,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4e0f40000000, copy home 0x4e1040000000, direct level 0x4e1140000000, copy level 0x4e1200000000
- factor effect within the cell: on the direct route -3.9633 [-3.9681, -3.9560] ms, on the copy route 364.1572 [363.6376, 364.7024] ms; change relative to the copy call at home: -7297.1 %
- per repetition: direct home 6.422e+09 link read bytes and 3.256e+04 SMMU translation requests; copy home 0 link read bytes and 8209 SMMU translation requests; direct level 6.423e+09 link read bytes and 3.231e+04 SMMU translation requests; copy level 0 link read bytes and 8209 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x403a80000000, copy home 0x403bc0000000, direct level 0x403cc0000000, copy level 0x403d80000000
- factor effect within the cell: on the direct route -4.1098 [-4.1318, -4.0752] ms, on the copy route 0.0639 [0.0537, 0.0828] ms; change relative to the copy call at home: -64.4 %
- per repetition: direct home 6.422e+09 link read bytes and 3.061e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 6.423e+09 link read bytes and 2.875e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.648e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x400600000000, copy home 0x400700000000, direct level 0x400800000000, copy level 0x4008c0000000
- factor effect within the cell: on the direct route 0.0435 [0.0424, 0.0451] ms, on the copy route 0.3068 [0.3058, 0.3078] ms; change relative to the copy call at home: -7.4 %
- per repetition: direct home 0 link read bytes and 3.854e+04 SMMU translation requests; copy home 0 link read bytes and 1.287e+04 SMMU translation requests; direct level 0 link read bytes and 4.17e+04 SMMU translation requests; copy level 0 link read bytes and 3.62e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=runs,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5ecfc0000000, copy home 0x5ed0c0000000, direct level 0x5ed1c0000000, copy level 0x5ed280000000
- factor effect within the cell: on the direct route 0.0258 [0.0179, 0.0305] ms, on the copy route 699.1614 [698.6621, 699.5454] ms; change relative to the copy call at home: -19594.3 %
- per repetition: direct home 0 link read bytes and 4.273e+04 SMMU translation requests; copy home 0 link read bytes and 1.286e+04 SMMU translation requests; direct level 0 link read bytes and 4.478e+04 SMMU translation requests; copy level 0 link read bytes and 2.135e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x413e40000000, copy home 0x413f00000000, direct level 0x414000000000, copy level 0x4140c0000000
- factor effect within the cell: on the direct route 0.1053 [0.1007, 0.1089] ms, on the copy route -0.0236 [-0.0264, -0.0205] ms; change relative to the copy call at home: +3.3 %
- per repetition: direct home 0 link read bytes and 4.287e+04 SMMU translation requests; copy home 0 link read bytes and 3.157e+04 SMMU translation requests; direct level 0 link read bytes and 4.137e+04 SMMU translation requests; copy level 0 link read bytes and 3.183e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=runs,type=four,vary=sharing,w=0.1

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x56fdc0000000, copy home 0x570040000000, direct level 0x5702c0000000, copy level 0x570580000000
- factor effect within the cell: on the direct route 0.0253 [0.0216, 0.0269] ms, on the copy route 5750.7431 [5719.2479, 5769.2014] ms; change relative to the copy call at home: -1015862.2 %
- per repetition: direct home 0 link read bytes and 1.329e+05 SMMU translation requests; copy home 0 link read bytes and 16.83 SMMU translation requests; direct level 0 link read bytes and 1.326e+05 SMMU translation requests; copy level 0 link read bytes and 16.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x4a2b00000000, copy home 0x4a2d80000000, direct level 0x4a3000000000, copy level 0x4a32c0000000
- factor effect within the cell: on the direct route 0.0135 [0.0122, 0.0149] ms, on the copy route -0.0154 [-0.0224, -0.0122] ms; change relative to the copy call at home: +0.5 %
- per repetition: direct home 0 link read bytes and 1.327e+05 SMMU translation requests; copy home 0 link read bytes and 2.653e+05 SMMU translation requests; direct level 0 link read bytes and 1.326e+05 SMMU translation requests; copy level 0 link read bytes and 2.823e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8

- seed 61; every round ran in the drawn order: yes; floor 0.0000 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x4de640000000, copy home 0x4de700000000, direct level 0x4de7c0000000, copy level 0x4de880000000
- factor effect within the cell: on the direct route 0.3616 [0.3612, 0.3619] ms, on the copy route 0.0247 [0.0186, 0.0312] ms; change relative to the copy call at home: +307.5 %
- per repetition: direct home 8.382e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.8 SMMU translation requests; direct level 1.341e+08 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.8 SMMU translation requests; multiplexed rows voided: 0

