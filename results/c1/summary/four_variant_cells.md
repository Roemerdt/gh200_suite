# Four-variant cells: direct and copy route at home and at a level of one factor, recomputed from raw rows

Times are per repetition in ms (one pass for the direct route, one complete call for the copy route). Each round runs the four variants once in the order the seed drew; the route difference at home (A - B) and at the level (C - D) and the change of the route difference, (C - D) - (A - B), are formed within each round and given as median with 95 % rank interval. A negative route difference means direct access is faster; a negative change means the level moved the comparison towards direct access. The relative change is the change over the route difference at home, given only where that difference excludes zero. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | level | direct home ms | copy home ms | direct level ms | copy level ms | route difference home ms [interval] | route difference level ms [interval] | change ms [interval] | relative change | rounds | change excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| at=1,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0303 | 0.0534 | 0.0301 | 0.0527 | -0.0231 [-0.0233, -0.0229] | -0.0226 [-0.0227, -0.0223] | 0.0006 [0.0004, 0.0009] | -2.5 % | 10 | yes | pass |
| at=1,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=four,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0088 | 0.0498 | 0.0089 | 0.0498 | -0.0410 [-0.0413, -0.0407] | -0.0409 [-0.0411, -0.0407] | 0.0001 [-0.0004, 0.0004] | -0.1 % | 10 | no | pass |
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=k,working-set-mib=32 | k | 1 | 1.5036 | 0.1902 | 0.1005 | 0.1246 | 1.3137 [1.3128, 1.3143] | -0.0241 [-0.0242, -0.0240] | -1.3378 [-1.3383, -1.3368] | -101.8 % | 10 | yes | pass |
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0377 | 0.0612 | 0.3726 | 0.0760 | -0.0235 [-0.0236, -0.0233] | 0.2966 [0.2959, 0.2972] | 0.3201 [0.3195, 0.3205] | -1361.7 % | 10 | yes | pass |
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=four,vary=k,working-set-mib=32 | k | 1 | 0.0977 | 0.1819 | 0.0174 | 0.1177 | -0.0841 [-0.0847, -0.0839] | -0.1003 [-0.1005, -0.1002] | -0.0162 [-0.0165, -0.0157] | +19.2 % | 10 | yes | pass |
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=four,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0161 | 0.0591 | 0.0299 | 0.0748 | -0.0430 [-0.0431, -0.0429] | -0.0449 [-0.0451, -0.0447] | -0.0019 [-0.0021, -0.0015] | +4.5 % | 20 | yes | pass |
| at=1,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0309 | 0.0539 | 0.0533 | 0.0542 | -0.0230 [-0.0232, -0.0228] | -0.0009 [-0.0014, -0.0007] | 0.0220 [0.0217, 0.0224] | -95.4 % | 10 | yes | pass |
| at=1,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=four,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0093 | 0.0500 | 0.0103 | 0.0501 | -0.0407 [-0.0408, -0.0403] | -0.0399 [-0.0400, -0.0395] | 0.0007 [0.0005, 0.0012] | -1.7 % | 10 | yes | pass |
| at=1,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0320 | 0.0555 | 0.0992 | 0.0584 | -0.0235 [-0.0236, -0.0233] | 0.0409 [0.0406, 0.0409] | 0.0643 [0.0640, 0.0644] | -274.1 % | 10 | yes | pass |
| at=1,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=four,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0104 | 0.0504 | 0.0132 | 0.0583 | -0.0399 [-0.0400, -0.0398] | -0.0451 [-0.0453, -0.0450] | -0.0053 [-0.0054, -0.0050] | +13.2 % | 20 | yes | pass |
| at=1,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0608 | 0.0857 | 1.4513 | 0.1361 | -0.0249 [-0.0250, -0.0246] | 1.3150 [1.3116, 1.3167] | 1.3396 [1.3365, 1.3419] | -5388.0 % | 10 | yes | pass |
| at=1,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=four,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0388 | 0.0836 | 0.0899 | 0.1339 | -0.0447 [-0.0449, -0.0446] | -0.0440 [-0.0443, -0.0435] | 0.0009 [0.0004, 0.0014] | -2.0 % | 10 | yes | pass |
| at=1,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sweeps | sweeps | 1 | 26.3551 | 6.4934 | 3.0252 | 3.6226 | 19.8621 [19.8056, 19.8824] | -0.5974 [-0.6006, -0.5924] | -20.4620 [-20.4748, -20.4019] | -103.0 % | 10 | yes | pass |
| at=1,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sweeps | sweeps | 1 | 3.2651 | 3.8599 | 0.3989 | 1.0446 | -0.5941 [-0.6013, -0.5927] | -0.6455 [-0.6471, -0.6450] | -0.0517 [-0.0536, -0.0451] | +8.7 % | 10 | yes | pass |
| at=16384,footprint-mib=1024,kernel=k3,placement=cpu,type=four,vary=footprint | footprint | 16384 | 5.3865 | 3.4511 | 432.7955 | 45.8292 | 1.9353 [1.9217, 1.9372] | 386.9730 [386.8176, 387.0564] | 385.0389 [384.8820, 385.1222] | +19895.5 % | 10 | yes | pass |
| at=16384,footprint-mib=1024,kernel=k3,placement=hbm,type=four,vary=footprint | footprint | 16384 | 0.4675 | 1.1201 | 425.0160 | 10.6519 | -0.6527 [-0.6531, -0.6516] | 414.3683 [414.2524, 414.4326] | 415.0214 [414.9042, 415.0848] | -63586.1 % | 10 | yes | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=f | f | 1of100 | 2.9100 | 3.2867 | 0.0384 | 0.0524 | -0.3772 [-0.3786, -0.3747] | -0.0140 [-0.0140, -0.0139] | 0.3631 [0.3607, 0.3646] | -96.3 % | 30 | yes | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=four,vary=f | f | 1of100 | 0.2989 | 0.9450 | 0.0101 | 0.0317 | -0.6461 [-0.6483, -0.6454] | -0.0216 [-0.0217, -0.0215] | 0.6246 [0.6237, 0.6266] | -96.7 % | 10 | yes | pass |
| at=2g,footprint-mib=11520,kernel=k3,placement=cpu,type=four,vary=partition | partition | 2g | 240.0462 | 32.6673 | 5.6751 | 30.9312 | 207.3394 [206.9133, 207.4587] | -25.2579 [-25.2626, -25.2503] | -232.6016 [-232.7085, -232.1708] | -112.2 % | 10 | yes | pass |
| at=2g,footprint-mib=12288,kernel=k3,placement=cpu,type=four,vary=partition | partition | 2g | 279.3405 | 34.7808 | 5.6701 | 32.8846 | 244.5561 [244.2469, 244.7791] | -27.2148 [-27.2242, -27.1974] | -271.7709 [-271.9766, -271.4600] | -111.1 % | 10 | yes | pass |
| at=2g,footprint-mib=12288,kernel=k3,placement=hbm,type=four,vary=partition | partition | 2g | 274.5325 | 8.1350 | 166.4868 | 8.2846 | 266.3838 [266.2450, 266.4803] | 158.1776 [156.3016, 158.8900] | -108.1474 [-110.0191, -107.3706] | -40.6 % | 30 | yes | pass |
| at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=partition | partition | 2g | 432.8546 | 46.1833 | 5.7733 | 43.1115 | 386.6672 [386.5988, 386.7327] | -37.3461 [-37.3952, -37.2926] | -423.9884 [-424.0784, -423.8951] | -109.7 % | 30 | yes | pass |
| at=2g,footprint-mib=24576,kernel=k3,placement=cpu,type=four,vary=partition | partition | 2g | 597.4420 | 65.8227 | 6.3143 | 63.9360 | 531.6122 [531.5802, 531.6682] | -57.6324 [-57.7433, -57.5232] | -589.2049 [-589.3857, -589.0393] | -110.8 % | 20 | yes | pass |
| at=2g,footprint-mib=32768,kernel=k3,placement=cpu,type=four,vary=partition | partition | 2g | 683.9687 | 86.0079 | 12.5016 | 84.9940 | 597.9587 [597.9315, 597.9869] | -72.4895 [-72.9568, -72.0423] | -670.4078 [-670.9029, -670.0055] | -112.1 % | 100 | yes | pass |
| at=2g,footprint-mib=4096,kernel=k3,placement=cpu,type=four,vary=partition | partition | 2g | 5.5366 | 11.9792 | 5.5457 | 12.1348 | -6.4448 [-6.5001, -6.4268] | -6.5891 [-6.5911, -6.5858] | -0.1521 [-0.1673, -0.0981] | +2.4 % | 20 | yes | pass |
| at=2g,footprint-mib=4096,kernel=k3,placement=hbm,type=four,vary=partition | partition | 2g | 5.1794 | 3.0244 | 3.7326 | 3.2041 | 2.1554 [2.1491, 2.1573] | 0.5315 [0.5169, 0.5483] | -1.6076 [-1.6355, -1.5881] | -74.6 % | 20 | yes | pass |
| at=2g,footprint-mib=8192,kernel=k3,placement=cpu,type=four,vary=partition | partition | 2g | 7.8887 | 23.5532 | 5.5804 | 22.8000 | -15.6700 [-15.8051, -15.6577] | -17.2258 [-17.2472, -17.2161] | -1.5531 [-1.5849, -1.4103] | +9.9 % | 10 | yes | pass |
| at=2g,footprint-mib=8192,kernel=k3,placement=hbm,type=four,vary=partition | partition | 2g | 7.8209 | 5.5610 | 5.7945 | 5.7424 | 2.2579 [2.2505, 2.2640] | 0.0510 [0.0299, 0.1218] | -2.2067 [-2.2262, -2.1336] | -97.7 % | 10 | yes | pass |
| at=2g,footprint-mib=9728,kernel=k3,placement=cpu,type=four,vary=partition | partition | 2g | 128.2484 | 27.3464 | 5.6567 | 27.5304 | 100.8861 [100.8165, 100.9798] | -21.8734 [-21.8963, -21.8497] | -122.7804 [-122.8296, -122.7110] | -121.7 % | 10 | yes | pass |
| at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-order | page-order | 2m | 433.4581 | 45.8139 | 5.3775 | 42.8407 | 387.6412 [387.3612, 387.7942] | -37.4625 [-37.4902, -37.4621] | -425.1013 [-425.2610, -424.8311] | -109.7 % | 10 | yes | pass |
| at=512m,footprint-mib=1024,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 5.3696 | 3.4131 | 5.3300 | 3.1232 | 1.9564 [1.9554, 1.9588] | 2.2069 [2.2023, 2.2083] | 0.2497 [0.2455, 0.2516] | +12.8 % | 10 | yes | pass |
| at=512m,footprint-mib=1024,kernel=k3,placement=hbm,type=four,vary=page-size | page-size | 512m | 0.4654 | 1.1179 | 0.4653 | 1.1164 | -0.6525 [-0.6530, -0.6515] | -0.6512 [-0.6522, -0.6501] | 0.0015 [0.0001, 0.0025] | -0.2 % | 10 | yes | pass |
| at=512m,footprint-mib=11520,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 240.1618 | 32.6362 | 5.3823 | 30.1355 | 207.5246 [207.4976, 207.5758] | -24.7551 [-24.7629, -24.7483] | -232.2832 [-232.3251, -232.2459] | -111.9 % | 10 | yes | pass |
| at=512m,footprint-mib=12288,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 279.0861 | 34.7691 | 5.3826 | 32.1132 | 244.3124 [244.1273, 244.4096] | -26.7310 [-26.7334, -26.7190] | -271.0447 [-271.1401, -270.8607] | -110.9 % | 10 | yes | pass |
| at=512m,footprint-mib=1536,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 5.3712 | 4.8114 | 5.3482 | 4.4436 | 0.5596 [0.5574, 0.5618] | 0.9047 [0.9027, 0.9056] | 0.3449 [0.3410, 0.3476] | +61.6 % | 10 | yes | pass |
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 432.7428 | 46.1570 | 5.3850 | 42.6422 | 386.5824 [386.4902, 386.6373] | -37.2571 [-37.4365, -37.2487] | -423.8719 [-423.9914, -423.8280] | -109.6 % | 20 | yes | pass |
| at=512m,footprint-mib=16384,kernel=k3p,placement=cpu,type=four,vary=page-size | page-size | 512m | 7.0316 | 45.1568 | 0.0992 | 42.2065 | -38.1267 [-38.1449, -38.1095] | -42.1073 [-42.1156, -42.0988] | -3.9760 [-4.0088, -3.9619] | +10.4 % | 10 | yes | pass |
| at=512m,footprint-mib=2048,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 5.3719 | 6.2067 | 5.3572 | 5.7640 | -0.8350 [-0.8363, -0.8326] | -0.4072 [-0.4087, -0.4062] | 0.4277 [0.4251, 0.4290] | -51.2 % | 20 | yes | pass |
| at=512m,footprint-mib=24576,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 598.3186 | 65.5936 | 5.3878 | 63.6907 | 532.7058 [532.6691, 532.7962] | -58.3039 [-58.3125, -58.2867] | -591.0446 [-591.2371, -590.9558] | -111.0 % | 20 | yes | pass |
| at=512m,footprint-mib=256,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 5.3594 | 1.2025 | 5.1755 | 1.1064 | 4.1570 [4.1562, 4.1582] | 4.0692 [4.0684, 4.0699] | -0.0882 [-0.0890, -0.0861] | -2.1 % | 10 | yes | pass |
| at=512m,footprint-mib=256,kernel=k3,placement=hbm,type=four,vary=page-size | page-size | 512m | 0.4256 | 1.0805 | 0.4242 | 1.0804 | -0.6550 [-0.6564, -0.6543] | -0.6561 [-0.6571, -0.6550] | -0.0008 [-0.0023, 0.0001] | +0.1 % | 10 | no | pass |
| at=512m,footprint-mib=32768,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 683.9093 | 85.9075 | 5.3896 | 84.7365 | 598.0039 [597.9113, 598.0804] | -79.3503 [-79.3675, -79.3296] | -677.3458 [-677.4250, -677.2794] | -113.3 % | 10 | yes | pass |
| at=512m,footprint-mib=4096,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 5.4968 | 11.9593 | 5.3703 | 11.0362 | -6.4754 [-6.5245, -6.4459] | -5.6659 [-5.6708, -5.6642] | 0.7638 [0.7100, 0.8133] | -11.8 % | 30 | yes | pass |
| at=512m,footprint-mib=4096,kernel=k3,placement=hbm,type=four,vary=page-size | page-size | 512m | 5.1211 | 3.0385 | 0.4765 | 3.0306 | 2.0847 [2.0676, 2.0920] | -2.5542 [-2.5568, -2.5511] | -4.6387 [-4.6476, -4.6218] | -222.5 % | 10 | yes | pass |
| at=512m,footprint-mib=8192,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 7.7557 | 23.5881 | 5.3789 | 21.5782 | -15.8310 [-15.8360, -15.8256] | -16.2001 [-16.2030, -16.1959] | -0.3712 [-0.3739, -0.3598] | +2.3 % | 10 | yes | pass |
| at=512m,footprint-mib=8192,kernel=k3,placement=hbm,type=four,vary=page-size | page-size | 512m | 7.8110 | 5.5625 | 0.4771 | 5.5640 | 2.2484 [2.1149, 2.2579] | -5.0869 [-5.0943, -5.0796] | -7.3300 [-7.3490, -7.2056] | -326.0 % | 10 | yes | pass |
| at=512m,footprint-mib=9728,kernel=k3,placement=cpu,type=four,vary=page-size | page-size | 512m | 128.2463 | 27.3497 | 5.3809 | 26.4298 | 100.8930 [100.7070, 100.9556] | -21.0487 [-21.0809, -21.0379] | -121.9396 [-122.0065, -121.7491] | -120.9 % | 10 | yes | pass |
| at=8,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 0.0997 | 0.1309 | 0.0299 | 0.0531 | -0.0312 [-0.0316, -0.0310] | -0.0232 [-0.0234, -0.0231] | 0.0080 [0.0079, 0.0082] | -25.5 % | 10 | yes | pass |
| at=8,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 0.0175 | 0.1197 | 0.0090 | 0.0506 | -0.1021 [-0.1024, -0.1020] | -0.0417 [-0.0417, -0.0416] | 0.0605 [0.0602, 0.0608] | -59.3 % | 50 | yes | pass |
| at=8,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 1.4930 | 0.1902 | 0.0374 | 0.0610 | 1.3029 [1.3023, 1.3033] | -0.0236 [-0.0241, -0.0234] | -1.3264 [-1.3272, -1.3259] | -101.8 % | 10 | yes | pass |
| at=8,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 0.0969 | 0.1812 | 0.0160 | 0.0582 | -0.0843 [-0.0851, -0.0838] | -0.0422 [-0.0423, -0.0416] | 0.0422 [0.0415, 0.0437] | -50.0 % | 10 | yes | pass |
| at=8,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 0.1918 | 0.1352 | 0.0307 | 0.0535 | 0.0567 [0.0562, 0.0570] | -0.0229 [-0.0230, -0.0227] | -0.0795 [-0.0797, -0.0790] | -140.3 % | 10 | yes | pass |
| at=8,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 0.0235 | 0.1254 | 0.0093 | 0.0502 | -0.1019 [-0.1023, -0.1018] | -0.0409 [-0.0412, -0.0408] | 0.0609 [0.0607, 0.0616] | -59.8 % | 20 | yes | pass |
| at=8,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 0.3768 | 0.1406 | 0.0317 | 0.0543 | 0.2362 [0.2361, 0.2365] | -0.0225 [-0.0228, -0.0222] | -0.2588 [-0.2590, -0.2584] | -109.6 % | 10 | yes | pass |
| at=8,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 0.0350 | 0.1307 | 0.0104 | 0.0506 | -0.0956 [-0.0963, -0.0951] | -0.0402 [-0.0403, -0.0400] | 0.0553 [0.0549, 0.0558] | -57.9 % | 20 | yes | pass |
| at=8,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 5.9615 | 0.3846 | 0.0606 | 0.0844 | 5.5768 [5.5735, 5.5809] | -0.0239 [-0.0241, -0.0235] | -5.6005 [-5.6050, -5.5977] | -100.4 % | 10 | yes | pass |
| at=8,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32 | working-set | 8 | 0.3458 | 0.3739 | 0.0388 | 0.0836 | -0.0281 [-0.0291, -0.0272] | -0.0448 [-0.0448, -0.0447] | -0.0167 [-0.0177, -0.0156] | +59.2 % | 10 | yes | pass |
| at=hbm,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=placement | placement | hbm | 2.9105 | 3.2543 | 0.2970 | 0.9468 | -0.3437 [-0.3454, -0.3420] | -0.6498 [-0.6505, -0.6485] | -0.3058 [-0.3079, -0.3034] | +89.0 % | 10 | yes | pass |
| at=none,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=tiling | tiling | none | 26.8547 | 6.4896 | 36.3077 | 5.9804 | 20.3676 [20.3504, 20.3918] | 30.3307 [29.9986, 30.5299] | 9.9462 [9.6068, 10.1764] | +48.8 % | 10 | yes | pass |
| at=none,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=tiling | tiling | none | 3.2517 | 3.8713 | 2.7529 | 3.3912 | -0.6218 [-0.6262, -0.6156] | -0.6378 [-0.6395, -0.6345] | -0.0162 [-0.0236, -0.0093] | +2.6 % | 10 | yes | pass |
| at=off512m,footprint-mib=8192,kernel=k3,placement=cpu,type=four,vary=alignment | alignment | off512m | 7.8863 | 23.6089 | 48.5632 | 22.8959 | -15.7229 [-15.8406, -15.7097] | 25.6735 [25.5715, 25.7258] | 41.4087 [41.3312, 41.4880] | -263.4 % | 10 | yes | pass |
| at=plain,footprint-mib=1024,kernel=k6,placement=cpu,type=four,update=atomic,vary=update | update | plain | 6.0592 | 7.3772 | 5.9759 | 7.2064 | -1.3184 [-1.3249, -1.3137] | -1.2302 [-1.2385, -1.2244] | 0.0892 [0.0818, 0.0929] | -6.8 % | 10 | yes | pass |
| at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,type=four,vary=generator | generator | rmat | 30.7620 | 4.1905 | 188.2987 | 67.7757 | 26.5718 [26.5618, 26.5843] | 121.0152 [119.9023, 122.1232] | 94.4435 [93.3206, 95.5594] | +355.4 % | 10 | yes | pass |
| at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,type=four,vary=generator | generator | rmat | 1.2720 | 1.7685 | 64.9943 | 64.9623 | -0.4964 [-0.4978, -0.4927] | -0.0037 [-0.0470, 0.0469] | 0.4929 [0.4458, 0.5433] | -99.3 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | sharing | shared | 0.0202 | 0.0346 | 0.0211 | 0.0364 | -0.0144 [-0.0147, -0.0140] | -0.0154 [-0.0159, -0.0152] | -0.0010 [-0.0015, -0.0007] | +7.2 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 0.0202 | 0.0348 | 0.0209 | 0.0362 | -0.0146 [-0.0149, -0.0144] | -0.0153 [-0.0155, -0.0150] | -0.0008 [-0.0010, -0.0003] | +5.6 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | sharing | shared | 0.0200 | 0.0344 | 0.0200 | 0.0343 | -0.0144 [-0.0146, -0.0142] | -0.0142 [-0.0146, -0.0141] | 0.0001 [-0.0000, 0.0003] | -0.5 % | 20 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | sharing | shared | 0.0120 | 0.0315 | 0.0121 | 0.0314 | -0.0194 [-0.0198, -0.0192] | -0.0194 [-0.0195, -0.0191] | 0.0002 [-0.0002, 0.0012] | -0.9 % | 20 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | sharing | shared | 0.0124 | 0.0319 | 0.0124 | 0.0321 | -0.0196 [-0.0197, -0.0193] | -0.0197 [-0.0200, -0.0195] | -0.0002 [-0.0007, 0.0002] | +1.0 % | 20 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | sharing | shared | 0.0121 | 0.0313 | 0.0121 | 0.0315 | -0.0192 [-0.0194, -0.0190] | -0.0195 [-0.0197, -0.0193] | -0.0002 [-0.0008, -0.0001] | +1.1 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | sharing | shared | 2.9332 | 3.3071 | 2.9206 | 3.1961 | -0.3734 [-0.3757, -0.3721] | -0.2756 [-0.2781, -0.2738] | 0.0978 [0.0940, 0.1009] | -26.2 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 2.9084 | 3.3100 | 3.0753 | 3.3225 | -0.4017 [-0.4024, -0.4009] | -0.2560 [-0.2820, -0.2161] | 0.1454 [0.1179, 0.1860] | -36.2 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | sharing | shared | 2.9204 | 3.2969 | 2.9112 | 3.1877 | -0.3765 [-0.3770, -0.3755] | -0.2767 [-0.2774, -0.2758] | 0.0996 [0.0990, 0.1011] | -26.5 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | sharing | shared | 0.3371 | 0.9787 | 0.3398 | 0.9792 | -0.6413 [-0.6435, -0.6397] | -0.6397 [-0.6407, -0.6360] | 0.0026 [0.0001, 0.0043] | -0.4 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | sharing | shared | 0.3907 | 1.0873 | 0.4116 | 1.0797 | -0.6971 [-0.6988, -0.6955] | -0.6679 [-0.6704, -0.6655] | 0.0284 [0.0271, 0.0321] | -4.1 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | sharing | shared | 0.3390 | 0.9759 | 0.3395 | 0.9763 | -0.6370 [-0.6381, -0.6350] | -0.6370 [-0.6382, -0.6363] | 0.0000 [-0.0020, 0.0011] | -0.0 % | 10 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | sharing | shared | 0.3786 | 0.4673 | 0.3714 | 0.4542 | -0.0885 [-0.0890, -0.0880] | -0.0827 [-0.0841, -0.0797] | 0.0055 [0.0038, 0.0084] | -6.3 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 0.3794 | 0.4628 | 0.6798 | 0.7245 | -0.0829 [-0.0850, -0.0818] | -0.0444 [-0.0460, -0.0414] | 0.0397 [0.0342, 0.0410] | -47.8 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | sharing | shared | 0.3703 | 0.4544 | 0.3717 | 0.4498 | -0.0839 [-0.0846, -0.0832] | -0.0784 [-0.0787, -0.0776] | 0.0061 [0.0048, 0.0068] | -7.2 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | sharing | shared | 0.0742 | 0.1923 | 0.2024 | 0.2760 | -0.1180 [-0.1184, -0.1177] | -0.0745 [-0.0766, -0.0727] | 0.0436 [0.0421, 0.0460] | -36.9 % | 70 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | sharing | shared | 0.0697 | 0.2073 | 0.2888 | 0.3590 | -0.1378 [-0.1385, -0.1364] | -0.0700 [-0.0704, -0.0688] | 0.0684 [0.0657, 0.0692] | -49.6 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | sharing | shared | 0.0590 | 0.1582 | 0.0595 | 0.1585 | -0.0990 [-0.0995, -0.0988] | -0.0988 [-0.1001, -0.0984] | 0.0001 [-0.0008, 0.0007] | -0.1 % | 10 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | sharing | shared | 0.0225 | 0.0412 | 0.0224 | 0.0413 | -0.0186 [-0.0188, -0.0182] | -0.0189 [-0.0192, -0.0185] | -0.0003 [-0.0006, 0.0000] | +1.5 % | 20 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 0.0225 | 0.0410 | 0.0246 | 0.0446 | -0.0185 [-0.0188, -0.0183] | -0.0199 [-0.0201, -0.0197] | -0.0013 [-0.0017, -0.0010] | +7.0 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | sharing | shared | 0.0227 | 0.0413 | 0.0229 | 0.0414 | -0.0185 [-0.0188, -0.0183] | -0.0184 [-0.0186, -0.0183] | 0.0002 [-0.0001, 0.0006] | -1.2 % | 20 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | sharing | shared | 0.0125 | 0.0318 | 0.0127 | 0.0323 | -0.0193 [-0.0195, -0.0192] | -0.0195 [-0.0198, -0.0194] | -0.0001 [-0.0004, 0.0001] | +0.5 % | 20 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | sharing | shared | 0.0124 | 0.0314 | 0.0135 | 0.0325 | -0.0190 [-0.0192, -0.0189] | -0.0190 [-0.0192, -0.0188] | 0.0002 [-0.0003, 0.0004] | -1.0 % | 20 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | sharing | shared | 0.0126 | 0.0319 | 0.0127 | 0.0319 | -0.0192 [-0.0195, -0.0191] | -0.0191 [-0.0194, -0.0188] | 0.0001 [-0.0004, 0.0005] | -0.4 % | 10 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | sharing | shared | 0.7457 | 0.8901 | 0.7378 | 0.8590 | -0.1446 [-0.1475, -0.1417] | -0.1217 [-0.1225, -0.1203] | 0.0234 [0.0188, 0.0271] | -16.2 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 0.7405 | 0.8761 | 0.8624 | 0.9555 | -0.1356 [-0.1359, -0.1353] | -0.0895 [-0.0960, -0.0860] | 0.0457 [0.0402, 0.0492] | -33.7 % | 70 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | sharing | shared | 0.7332 | 0.8639 | 0.7353 | 0.8538 | -0.1307 [-0.1311, -0.1302] | -0.1183 [-0.1186, -0.1180] | 0.0126 [0.0118, 0.0129] | -9.6 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | sharing | shared | 0.1069 | 0.7651 | 0.1665 | 0.7512 | -0.6581 [-0.6589, -0.6573] | -0.5845 [-0.5862, -0.5835] | 0.0735 [0.0725, 0.0749] | -11.2 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | sharing | shared | 0.1226 | 0.7933 | 0.2088 | 0.7669 | -0.6706 [-0.6724, -0.6688] | -0.5582 [-0.5595, -0.5572] | 0.1121 [0.1099, 0.1161] | -16.7 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | sharing | shared | 0.0985 | 0.7501 | 0.1003 | 0.7505 | -0.6516 [-0.6523, -0.6510] | -0.6500 [-0.6505, -0.6495] | 0.0016 [0.0010, 0.0025] | -0.2 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | sharing | shared | 0.0996 | 0.1330 | 0.1010 | 0.1349 | -0.0334 [-0.0339, -0.0332] | -0.0339 [-0.0343, -0.0334] | -0.0006 [-0.0011, -0.0001] | +1.8 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 0.0996 | 0.1334 | 0.1932 | 0.2144 | -0.0338 [-0.0343, -0.0332] | -0.0210 [-0.0217, -0.0201] | 0.0128 [0.0120, 0.0138] | -37.9 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | sharing | shared | 0.1004 | 0.1330 | 0.1009 | 0.1338 | -0.0325 [-0.0331, -0.0317] | -0.0329 [-0.0332, -0.0327] | -0.0006 [-0.0013, 0.0002] | +1.7 % | 10 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | sharing | shared | 0.0239 | 0.0560 | 0.0580 | 0.0883 | -0.0321 [-0.0329, -0.0315] | -0.0302 [-0.0308, -0.0296] | 0.0019 [0.0008, 0.0030] | -6.0 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | sharing | shared | 0.0225 | 0.0524 | 0.0928 | 0.1228 | -0.0298 [-0.0304, -0.0293] | -0.0300 [-0.0307, -0.0295] | -0.0000 [-0.0011, 0.0005] | +0.0 % | 10 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | sharing | shared | 0.0234 | 0.0566 | 0.0226 | 0.0554 | -0.0331 [-0.0336, -0.0327] | -0.0328 [-0.0330, -0.0327] | 0.0000 [-0.0005, 0.0010] | -0.0 % | 20 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | sharing | shared | 0.1938 | 0.2428 | 0.1917 | 0.2437 | -0.0492 [-0.0493, -0.0488] | -0.0522 [-0.0526, -0.0513] | -0.0027 [-0.0038, -0.0021] | +5.6 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 0.1919 | 0.2374 | 0.3754 | 0.4069 | -0.0454 [-0.0459, -0.0452] | -0.0317 [-0.0325, -0.0313] | 0.0138 [0.0122, 0.0148] | -30.5 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | sharing | shared | 0.1900 | 0.2399 | 0.1910 | 0.2404 | -0.0499 [-0.0504, -0.0488] | -0.0493 [-0.0496, -0.0490] | 0.0006 [-0.0005, 0.0015] | -1.3 % | 10 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | sharing | shared | 0.0382 | 0.0941 | 0.1733 | 0.2216 | -0.0558 [-0.0562, -0.0555] | -0.0479 [-0.0485, -0.0464] | 0.0081 [0.0069, 0.0093] | -14.5 % | 30 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | sharing | shared | 0.0357 | 0.0899 | 0.1851 | 0.2340 | -0.0542 [-0.0545, -0.0537] | -0.0488 [-0.0501, -0.0483] | 0.0051 [0.0044, 0.0062] | -9.5 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | sharing | shared | 0.0366 | 0.0911 | 0.0347 | 0.0917 | -0.0545 [-0.0550, -0.0540] | -0.0569 [-0.0572, -0.0565] | -0.0023 [-0.0027, -0.0022] | +4.3 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | sharing | shared | 0.0358 | 0.0588 | 0.0354 | 0.0589 | -0.0229 [-0.0233, -0.0226] | -0.0235 [-0.0237, -0.0234] | -0.0006 [-0.0008, -0.0002] | +2.7 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 0.0359 | 0.0583 | 0.0554 | 0.0774 | -0.0224 [-0.0227, -0.0222] | -0.0220 [-0.0226, -0.0217] | 0.0005 [-0.0003, 0.0006] | -2.3 % | 10 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | sharing | shared | 0.0358 | 0.0596 | 0.0360 | 0.0600 | -0.0238 [-0.0240, -0.0234] | -0.0240 [-0.0243, -0.0238] | -0.0003 [-0.0006, -0.0000] | +1.1 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | sharing | shared | 0.0146 | 0.0327 | 0.0229 | 0.0470 | -0.0181 [-0.0182, -0.0179] | -0.0241 [-0.0243, -0.0240] | -0.0060 [-0.0062, -0.0057] | +33.4 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | sharing | shared | 0.0142 | 0.0317 | 0.0291 | 0.0505 | -0.0175 [-0.0176, -0.0173] | -0.0213 [-0.0220, -0.0211] | -0.0040 [-0.0047, -0.0035] | +22.7 % | 40 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | sharing | shared | 0.0142 | 0.0319 | 0.0145 | 0.0318 | -0.0177 [-0.0178, -0.0174] | -0.0172 [-0.0176, -0.0171] | 0.0003 [-0.0000, 0.0005] | -1.9 % | 20 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | sharing | shared | 0.2856 | 0.3554 | 0.2817 | 0.3517 | -0.0692 [-0.0704, -0.0679] | -0.0699 [-0.0707, -0.0685] | -0.0007 [-0.0022, 0.0019] | +1.0 % | 10 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 0.2847 | 0.3536 | 0.5450 | 0.5855 | -0.0689 [-0.0717, -0.0660] | -0.0387 [-0.0449, -0.0355] | 0.0292 [0.0249, 0.0362] | -42.4 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | sharing | shared | 0.2819 | 0.3508 | 0.2801 | 0.3480 | -0.0690 [-0.0694, -0.0683] | -0.0679 [-0.0683, -0.0677] | 0.0012 [0.0004, 0.0014] | -1.7 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | sharing | shared | 0.0561 | 0.1403 | 0.1882 | 0.2410 | -0.0843 [-0.0857, -0.0837] | -0.0524 [-0.0545, -0.0514] | 0.0324 [0.0284, 0.0335] | -38.4 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | sharing | shared | 0.0524 | 0.1425 | 0.2528 | 0.3061 | -0.0902 [-0.0909, -0.0893] | -0.0533 [-0.0546, -0.0528] | 0.0368 [0.0357, 0.0372] | -40.8 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | sharing | shared | 0.0486 | 0.1257 | 0.0485 | 0.1271 | -0.0770 [-0.0781, -0.0766] | -0.0787 [-0.0797, -0.0775] | -0.0011 [-0.0030, -0.0004] | +1.4 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | sharing | shared | 30.8695 | 4.7096 | 29.7185 | 4.0649 | 26.1476 [26.1154, 26.1764] | 25.6547 [25.6501, 25.6571] | -0.4959 [-0.5501, -0.4426] | -1.9 % | 90 | yes | pass |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing | sharing | shared | 1.2805 | 1.7675 | 1.2781 | 1.7734 | -0.4876 [-0.4905, -0.4835] | -0.4951 [-0.4974, -0.4935] | -0.0077 [-0.0118, -0.0041] | +1.6 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=1,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0371 | 0.0549 | 0.0360 | 0.0534 | -0.0179 [-0.0182, -0.0172] | -0.0175 [-0.0177, -0.0170] | 0.0005 [-0.0004, 0.0009] | -2.8 % | 10 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=1,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0372 | 0.0553 | 0.0542 | 0.0719 | -0.0180 [-0.0188, -0.0174] | -0.0178 [-0.0184, -0.0171] | 0.0001 [-0.0006, 0.0012] | -0.5 % | 10 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=1,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0362 | 0.0538 | 0.0359 | 0.0535 | -0.0173 [-0.0177, -0.0171] | -0.0173 [-0.0180, -0.0171] | 0.0000 [-0.0002, 0.0003] | -0.2 % | 10 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0443 | 0.0622 | 0.0435 | 0.0609 | -0.0179 [-0.0188, -0.0176] | -0.0173 [-0.0177, -0.0170] | 0.0005 [-0.0001, 0.0012] | -3.0 % | 10 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0446 | 0.0627 | 0.0607 | 0.0782 | -0.0181 [-0.0188, -0.0178] | -0.0176 [-0.0181, -0.0174] | 0.0007 [0.0000, 0.0014] | -3.8 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0439 | 0.0615 | 0.0437 | 0.0613 | -0.0176 [-0.0177, -0.0173] | -0.0175 [-0.0178, -0.0173] | -0.0000 [-0.0002, 0.0003] | +0.2 % | 10 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=2,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0376 | 0.0550 | 0.0368 | 0.0539 | -0.0174 [-0.0178, -0.0170] | -0.0172 [-0.0174, -0.0169] | 0.0005 [-0.0002, 0.0008] | -2.7 % | 20 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=2,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0378 | 0.0553 | 0.0553 | 0.0722 | -0.0175 [-0.0180, -0.0172] | -0.0168 [-0.0175, -0.0163] | 0.0006 [-0.0003, 0.0014] | -3.3 % | 10 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=2,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0369 | 0.0532 | 0.0366 | 0.0528 | -0.0164 [-0.0169, -0.0162] | -0.0163 [-0.0166, -0.0160] | 0.0001 [-0.0003, 0.0005] | -0.8 % | 20 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=4,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0388 | 0.0565 | 0.0380 | 0.0553 | -0.0179 [-0.0183, -0.0171] | -0.0174 [-0.0178, -0.0169] | 0.0004 [0.0000, 0.0007] | -2.2 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=4,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0385 | 0.0559 | 0.0572 | 0.0740 | -0.0173 [-0.0176, -0.0171] | -0.0165 [-0.0169, -0.0161] | 0.0007 [0.0005, 0.0011] | -3.8 % | 30 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=4,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0380 | 0.0549 | 0.0378 | 0.0546 | -0.0170 [-0.0172, -0.0168] | -0.0168 [-0.0171, -0.0164] | 0.0003 [-0.0002, 0.0007] | -1.9 % | 20 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=64,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0676 | 0.0871 | 0.0666 | 0.0859 | -0.0194 [-0.0201, -0.0188] | -0.0193 [-0.0195, -0.0191] | 0.0001 [-0.0003, 0.0008] | -0.6 % | 10 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=64,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0673 | 0.0874 | 0.0872 | 0.1056 | -0.0200 [-0.0203, -0.0195] | -0.0184 [-0.0187, -0.0180] | 0.0014 [0.0008, 0.0019] | -7.2 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=64,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8 | sharing | shared | 0.0666 | 0.0858 | 0.0665 | 0.0853 | -0.0192 [-0.0194, -0.0186] | -0.0190 [-0.0194, -0.0188] | 0.0000 [-0.0003, 0.0007] | -0.3 % | 10 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.1139 | 0.0407 | 0.1142 | 0.6160 | 0.0731 [0.0729, 0.0740] | -0.5020 [-0.5022, -0.5016] | -0.5755 [-0.5761, -0.5750] | -787.2 % | 70 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0435 | 0.0392 | 0.0424 | 0.6098 | 0.0042 [0.0038, 0.0047] | -0.5673 [-0.5679, -0.5669] | -0.5721 [-0.5742, -0.5710] | -13707.9 % | 60 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.1161 | 0.1415 | 0.1189 | 0.1393 | -0.0254 [-0.0259, -0.0244] | -0.0203 [-0.0208, -0.0195] | 0.0050 [0.0039, 0.0062] | -19.8 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | sharing | shared | 0.0468 | 0.0689 | 0.0478 | 0.0700 | -0.0223 [-0.0226, -0.0218] | -0.0219 [-0.0226, -0.0211] | 0.0003 [-0.0004, 0.0008] | -1.2 % | 40 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.0302 | 0.0424 | 0.0306 | 0.2046 | -0.0121 [-0.0125, -0.0119] | -0.1741 [-0.1765, -0.1729] | -0.1624 [-0.1653, -0.1598] | +1344.0 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.0456 | 0.5629 | 0.0495 | 0.4908 | -0.5169 [-0.6102, -0.4183] | -0.4416 [-0.5327, -0.4303] | 0.0679 [-0.0181, 0.1597] | -13.1 % | 100 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 1.5208 | 0.0995 | 1.4873 | 0.6785 | 1.4210 [1.4196, 1.4218] | 0.8088 [0.8085, 0.8093] | -0.6125 [-0.6137, -0.6099] | -43.1 % | 50 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0507 | 0.0438 | 0.0502 | 0.6113 | 0.0068 [0.0060, 0.0071] | -0.5612 [-0.5618, -0.5610] | -0.5683 [-0.5698, -0.5671] | -8390.1 % | 90 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 1.5119 | 0.0973 | 1.5144 | 0.7476 | 1.4146 [1.4097, 1.4160] | 0.7665 [0.7660, 0.7673] | -0.6477 [-0.6495, -0.6443] | -45.8 % | 30 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0501 | 0.0439 | 0.0500 | 0.6911 | 0.0063 [0.0057, 0.0065] | -0.6414 [-0.6423, -0.6410] | -0.6500 [-0.6506, -0.6481] | -10391.3 % | 80 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 1.5069 | 0.2073 | 1.5097 | 0.2025 | 1.2994 [1.2986, 1.3022] | 1.3069 [1.3058, 1.3083] | 0.0071 [0.0058, 0.0083] | +0.5 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | sharing | shared | 0.0560 | 0.0788 | 0.0570 | 0.0794 | -0.0228 [-0.0231, -0.0222] | -0.0225 [-0.0232, -0.0220] | 0.0003 [-0.0004, 0.0008] | -1.4 % | 50 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.1143 | 0.1114 | 0.1155 | 0.2825 | 0.0029 [0.0022, 0.0038] | -0.1670 [-0.1682, -0.1666] | -0.1698 [-0.1713, -0.1692] | -5915.3 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.1139 | 0.1111 | 0.1151 | 0.7330 | 0.0028 [0.0023, 0.0038] | -0.6185 [-0.6188, -0.6171] | -0.6214 [-0.6223, -0.6187] | -22320.1 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.1300 | 0.2239 | 0.1301 | 0.2235 | -0.0942 [-0.0955, -0.0919] | -0.0933 [-0.0944, -0.0921] | 0.0013 [-0.0008, 0.0022] | -1.3 % | 10 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.2061 | 0.0402 | 0.2060 | 0.6223 | 0.1657 [0.1648, 0.1666] | -0.4163 [-0.4168, -0.4161] | -0.5820 [-0.5828, -0.5806] | -351.1 % | 40 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0438 | 0.0393 | 0.0420 | 0.6018 | 0.0044 [0.0041, 0.0048] | -0.5601 [-0.5608, -0.5594] | -0.5657 [-0.5665, -0.5638] | -12732.5 % | 60 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.2083 | 0.1511 | 0.2114 | 0.1452 | 0.0572 [0.0561, 0.0580] | 0.0662 [0.0648, 0.0681] | 0.0095 [0.0078, 0.0111] | +16.6 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | sharing | shared | 0.0475 | 0.0693 | 0.0478 | 0.0694 | -0.0220 [-0.0221, -0.0216] | -0.0210 [-0.0215, -0.0208] | 0.0006 [0.0002, 0.0010] | -2.6 % | 50 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.0407 | 0.0549 | 0.0405 | 0.2153 | -0.0141 [-0.0148, -0.0139] | -0.1746 [-0.1761, -0.1717] | -0.1599 [-0.1617, -0.1582] | +1133.8 % | 30 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.0545 | 0.6982 | 0.0567 | 0.6031 | -0.6437 [-0.7379, -0.6289] | -0.5467 [-0.6462, -0.4539] | 0.1155 [0.0496, 0.2069] | -17.9 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.3910 | 0.0492 | 0.3902 | 0.6298 | 0.3417 [0.3399, 0.3422] | -0.2398 [-0.2401, -0.2394] | -0.5813 [-0.5821, -0.5802] | -170.1 % | 30 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0451 | 0.0401 | 0.0446 | 0.6055 | 0.0049 [0.0045, 0.0054] | -0.5613 [-0.5620, -0.5606] | -0.5675 [-0.5686, -0.5656] | -11591.7 % | 70 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.3935 | 0.1620 | 0.3986 | 0.1552 | 0.2316 [0.2305, 0.2323] | 0.2435 [0.2426, 0.2444] | 0.0121 [0.0106, 0.0127] | +5.2 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | sharing | shared | 0.0486 | 0.0699 | 0.0496 | 0.0702 | -0.0213 [-0.0216, -0.0210] | -0.0204 [-0.0208, -0.0201] | 0.0009 [0.0002, 0.0013] | -4.2 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.0518 | 0.0625 | 0.0516 | 0.2192 | -0.0105 [-0.0109, -0.0103] | -0.1674 [-0.1688, -0.1641] | -0.1568 [-0.1583, -0.1542] | +1500.6 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.0650 | 1.0710 | 0.0673 | 0.7101 | -1.0063 [-1.1070, -0.9207] | -0.6428 [-0.6641, -0.5514] | 0.3899 [0.2888, 0.4803] | -38.7 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 5.9782 | 0.2946 | 5.9600 | 0.8739 | 5.6846 [5.6814, 5.6910] | 5.0859 [5.0815, 5.0915] | -0.5994 [-0.6066, -0.5952] | -10.5 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0739 | 0.0661 | 0.0733 | 0.6364 | 0.0077 [0.0074, 0.0079] | -0.5637 [-0.5644, -0.5631] | -0.5719 [-0.5724, -0.5708] | -7474.2 % | 70 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 5.9766 | 0.4017 | 5.9914 | 0.3943 | 5.5751 [5.5726, 5.5777] | 5.5967 [5.5940, 5.5998] | 0.0223 [0.0195, 0.0242] | +0.4 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | sharing | shared | 0.0780 | 0.1013 | 0.0782 | 0.1010 | -0.0232 [-0.0238, -0.0228] | -0.0227 [-0.0232, -0.0221] | 0.0006 [-0.0002, 0.0011] | -2.7 % | 30 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.3708 | 0.3032 | 0.3620 | 0.4467 | 0.0674 [0.0660, 0.0687] | -0.0847 [-0.0889, -0.0819] | -0.1526 [-0.1563, -0.1480] | -226.6 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.3786 | 0.6446 | 0.3779 | 0.4225 | -0.2661 [-0.2880, -0.1698] | -0.0450 [-0.0454, -0.0447] | 0.1393 [0.1246, 0.2383] | -52.4 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 5.4343 | 0.4908 | 5.4221 | 1.0722 | 4.9433 [4.9413, 4.9490] | 4.3505 [4.3323, 4.3635] | -0.5952 [-0.6101, -0.5715] | -12.0 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 5.3930 | 3.4792 | 5.3870 | 3.4759 | 1.9143 [1.9047, 1.9235] | 1.9145 [1.9002, 1.9359] | -0.0036 [-0.0069, 0.0151] | -0.2 % | 10 | no | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 0.6007 | 0.5550 | 0.6019 | 0.6444 | 0.0451 [0.0423, 0.0473] | -0.0423 [-0.0512, -0.0397] | -0.0860 [-0.0966, -0.0835] | -191.0 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | sharing | shared | 0.6972 | 1.3082 | 0.6951 | 1.2937 | -0.6106 [-0.6133, -0.6084] | -0.5992 [-0.6001, -0.5940] | 0.0119 [0.0096, 0.0153] | -2.0 % | 10 | yes | pass |
| at=shared,footprint-mib=11520,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 240.3338 | 0.5057 | 240.3393 | 3.7050 | 239.8287 [239.7554, 239.8891] | 236.6100 [236.5360, 236.7146] | -3.1709 [-3.2713, -3.1098] | -1.3 % | 20 | yes | pass |
| at=shared,footprint-mib=11520,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 240.3958 | 32.9735 | 240.4518 | 31.1406 | 207.4208 [207.3588, 207.5111] | 209.3113 [209.1351, 209.3787] | 1.8768 [1.6211, 2.0161] | +0.9 % | 30 | yes | pass |
| at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 279.7832 | 0.5114 | 279.7278 | 4.0958 | 279.2714 [279.1682, 279.3595] | 275.6672 [275.5064, 275.7089] | -3.6472 [-3.7440, -3.4970] | -1.3 % | 10 | yes | pass |
| at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 279.3384 | 35.0354 | 279.3900 | 33.0403 | 244.2969 [244.1414, 244.3543] | 246.3412 [246.2703, 246.4072] | 2.0961 [1.8675, 2.2378] | +0.9 % | 20 | yes | pass |
| at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 283.0134 | 0.5701 | 283.2826 | 2.4750 | 282.4403 [282.3271, 282.5173] | 280.8011 [280.6222, 280.9573] | -1.6259 [-1.8159, -1.3889] | -0.6 % | 10 | yes | pass |
| at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | sharing | shared | 284.4394 | 8.2976 | 285.1582 | 8.2942 | 276.1273 [275.8195, 276.2546] | 276.8664 [276.5384, 276.9895] | 0.7753 [0.5623, 0.8681] | +0.3 % | 10 | yes | pass |
| at=shared,footprint-mib=1536,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 5.4553 | 0.5025 | 5.4472 | 1.2206 | 4.9545 [4.9490, 4.9731] | 4.2284 [4.2218, 4.2472] | -0.7253 [-0.7422, -0.7201] | -14.6 % | 20 | yes | pass |
| at=shared,footprint-mib=1536,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 5.3841 | 4.9042 | 5.3787 | 4.8857 | 0.4800 [0.4780, 0.4813] | 0.4930 [0.4839, 0.4951] | 0.0138 [0.0031, 0.0151] | +2.9 % | 10 | yes | pass |
| at=shared,footprint-mib=16384,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | sharing | shared | 483.3420 | 47.8844 | 483.2173 | 45.2298 | 435.4648 [435.3396, 435.5500] | 437.9905 [437.8091, 438.1021] | 2.5679 [2.2940, 2.6668] | +0.6 % | 10 | yes | pass |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | sharing | shared | 7.2622 | 45.1678 | 7.2371 | 42.4107 | -37.9062 [-37.9108, -37.9038] | -35.1790 [-35.1907, -35.1663] | 2.7278 [2.7135, 2.7384] | -7.2 % | 10 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 433.5353 | 0.5129 | 433.6202 | 5.1916 | 433.0227 [432.7894, 433.1783] | 428.4287 [428.2674, 428.5694] | -4.5525 [-4.7731, -4.3558] | -1.1 % | 10 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1 | sharing | shared | 433.5680 | 0.5151 | 433.6678 | 10.7210 | 433.0523 [432.8738, 433.1566] | 422.9429 [422.7368, 423.0270] | -10.1174 [-10.3508, -9.9853] | -2.3 % | 10 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 433.4350 | 45.6413 | 433.5549 | 43.1546 | 387.8024 [387.6723, 387.8600] | 390.4045 [390.2580, 390.5087] | 2.5387 [2.4170, 2.7623] | +0.7 % | 20 | yes | pass |
| at=shared,footprint-mib=2048,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 5.4715 | 0.5027 | 5.4449 | 1.2466 | 4.9686 [4.9118, 4.9724] | 4.1993 [4.1523, 4.2444] | -0.7478 [-0.8157, -0.7186] | -15.1 % | 10 | yes | pass |
| at=shared,footprint-mib=2048,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 5.3863 | 6.2395 | 5.3736 | 6.2872 | -0.8530 [-0.8568, -0.8273] | -0.9071 [-0.9214, -0.8857] | -0.0568 [-0.0684, -0.0499] | +6.7 % | 10 | yes | pass |
| at=shared,footprint-mib=24576,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | sharing | shared | 752.0880 | 74.3968 | 751.8985 | 73.0848 | 677.6916 [677.6161, 677.7831] | 678.8587 [678.7762, 678.9200] | 1.1388 [1.0422, 1.3433] | +0.2 % | 20 | yes | pass |
| at=shared,footprint-mib=24576,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 598.3405 | 0.5167 | 598.4344 | 7.5696 | 597.8246 [597.6125, 597.9674] | 590.8628 [590.7653, 590.9522] | -6.9544 [-7.1521, -6.8072] | -1.2 % | 10 | yes | pass |
| at=shared,footprint-mib=24576,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 598.3330 | 65.8371 | 598.3472 | 64.0766 | 532.5055 [532.4121, 532.7358] | 534.2651 [534.1428, 534.3752] | 1.7634 [1.4937, 1.9197] | +0.3 % | 10 | yes | pass |
| at=shared,footprint-mib=256,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | sharing | shared | 7.3967 | 1.0142 | 7.3497 | 1.0102 | 6.3790 [6.3721, 6.3811] | 6.3393 [6.3369, 6.3405] | -0.0392 [-0.0416, -0.0330] | -0.6 % | 90 | yes | pass |
| at=shared,footprint-mib=256,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing | sharing | shared | 0.2151 | 0.8890 | 0.2154 | 0.8891 | -0.6740 [-0.6750, -0.6733] | -0.6739 [-0.6744, -0.6729] | 0.0001 [-0.0006, 0.0021] | -0.0 % | 10 | no | pass |
| at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 5.4034 | 0.4449 | 5.3987 | 0.6055 | 4.9582 [4.9545, 4.9596] | 4.7925 [4.7863, 4.7969] | -0.1643 [-0.1716, -0.1614] | -3.3 % | 10 | yes | pass |
| at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 5.3749 | 1.2173 | 5.3698 | 1.2692 | 4.1581 [4.1564, 4.1589] | 4.1009 [4.0990, 4.1086] | -0.0563 [-0.0597, -0.0517] | -1.4 % | 10 | yes | pass |
| at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 0.5058 | 0.5016 | 0.4979 | 0.5472 | 0.0044 [0.0012, 0.0055] | -0.0499 [-0.0546, -0.0481] | -0.0531 [-0.0606, -0.0485] | -1204.4 % | 10 | yes | pass |
| at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | sharing | shared | 0.5871 | 1.2447 | 0.5769 | 1.1132 | -0.6566 [-0.7209, -0.6552] | -0.5362 [-0.5370, -0.5357] | 0.1214 [0.1190, 0.1282] | -18.5 % | 100 | yes | pass |
| at=shared,footprint-mib=32768,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | sharing | shared | 971.4187 | 91.6280 | 971.1054 | 89.8134 | 879.7754 [879.7397, 879.8109] | 881.2689 [881.2240, 881.3869] | 1.5189 [1.3976, 1.5966] | +0.2 % | 20 | yes | pass |
| at=shared,footprint-mib=32768,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 685.0247 | 0.5188 | 685.0969 | 9.8536 | 684.5048 [684.3688, 684.7627] | 675.2726 [675.1675, 675.4667] | -9.2548 [-9.5063, -9.0740] | -1.4 % | 10 | yes | pass |
| at=shared,footprint-mib=32768,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 683.9226 | 86.6193 | 684.1630 | 85.2337 | 597.2590 [597.0972, 597.5362] | 598.9383 [598.9091, 598.9803] | 1.6793 [1.3866, 1.8481] | +0.3 % | 10 | yes | pass |
| at=shared,footprint-mib=4096,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | sharing | shared | 123.7892 | 12.5058 | 121.5583 | 12.5922 | 111.2865 [111.2275, 111.3055] | 108.9657 [108.9205, 108.9897] | -2.3095 [-2.3684, -2.2824] | -2.1 % | 10 | yes | pass |
| at=shared,footprint-mib=4096,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing | sharing | shared | 7.0823 | 9.6036 | 7.0647 | 9.5940 | -2.5199 [-2.5315, -2.5127] | -2.5272 [-2.5339, -2.5069] | -0.0089 [-0.0159, 0.0068] | +0.4 % | 10 | no | pass |
| at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 5.7277 | 0.5049 | 5.6946 | 1.7624 | 5.2217 [5.2090, 5.2375] | 3.9285 [3.8985, 3.9762] | -1.2959 [-1.3275, -1.2514] | -24.8 % | 20 | yes | pass |
| at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 5.4764 | 12.0044 | 5.4764 | 12.1916 | -6.5247 [-6.5404, -6.5001] | -6.7169 [-6.7497, -6.6799] | -0.1995 [-0.2315, -0.1411] | +3.1 % | 10 | yes | pass |
| at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 5.3190 | 0.5599 | 5.3329 | 1.1207 | 4.7604 [4.7559, 4.7641] | 4.2144 [4.2064, 4.2180] | -0.5477 [-0.5561, -0.5407] | -11.5 % | 10 | yes | pass |
| at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | sharing | shared | 5.3278 | 3.2153 | 5.3338 | 3.2227 | 2.1125 [2.1086, 2.1189] | 2.1124 [2.1009, 2.1164] | -0.0025 [-0.0145, 0.0029] | -0.1 % | 10 | no | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=1,tiling=tiles,type=four,vary=sharing | sharing | shared | 3.8039 | 3.7327 | 3.0537 | 3.6916 | 0.0719 [0.0669, 0.0764] | -0.6371 [-0.6413, -0.6313] | -0.7082 [-0.7122, -0.7034] | -985.1 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=16,tiling=tiles,type=four,vary=sharing | sharing | shared | 53.5649 | 9.7347 | 45.8734 | 9.7017 | 43.8345 [43.7690, 43.8630] | 36.1802 [36.1693, 36.2017] | -7.6533 [-7.6962, -7.5887] | -17.5 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=2,tiling=tiles,type=four,vary=sharing | sharing | shared | 6.8959 | 4.1121 | 5.8844 | 4.0657 | 2.7862 [2.7618, 2.7959] | 1.8173 [1.8128, 1.8222] | -0.9661 [-0.9753, -0.9489] | -34.7 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=4,tiling=tiles,type=four,vary=sharing | sharing | shared | 13.5520 | 4.9198 | 11.6371 | 4.8664 | 8.6337 [8.6236, 8.6391] | 6.7718 [6.7626, 6.7778] | -1.8592 [-1.8772, -1.8526] | -21.5 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=64,tiling=tiles,type=four,vary=sharing | sharing | shared | 214.0406 | 29.0900 | 182.6629 | 29.0285 | 184.9607 [184.9040, 185.0177] | 153.6320 [153.6005, 153.7176] | -31.3393 [-31.4016, -31.2076] | -16.9 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing | sharing | shared | 26.7419 | 6.5251 | 23.1417 | 6.4988 | 20.2163 [20.1784, 20.2376] | 16.6431 [16.6193, 16.6554] | -3.5687 [-3.6009, -3.5260] | -17.7 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=1,tiling=tiles,type=four,vary=sharing | sharing | shared | 0.4137 | 1.0568 | 0.4115 | 1.0553 | -0.6431 [-0.6437, -0.6424] | -0.6443 [-0.6451, -0.6428] | -0.0008 [-0.0032, 0.0016] | +0.1 % | 10 | no | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=16,tiling=tiles,type=four,vary=sharing | sharing | shared | 6.4972 | 7.0895 | 6.5217 | 7.0885 | -0.5961 [-0.6019, -0.5821] | -0.5685 [-0.5738, -0.5497] | 0.0306 [0.0083, 0.0455] | -5.1 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=2,tiling=tiles,type=four,vary=sharing | sharing | shared | 0.8250 | 1.4647 | 0.8215 | 1.4613 | -0.6402 [-0.6450, -0.6390] | -0.6403 [-0.6430, -0.6386] | 0.0004 [-0.0029, 0.0055] | -0.1 % | 10 | no | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=4,tiling=tiles,type=four,vary=sharing | sharing | shared | 1.6466 | 2.2641 | 1.6409 | 2.2626 | -0.6161 [-0.6213, -0.6114] | -0.6213 [-0.6250, -0.6180] | -0.0047 [-0.0128, -0.0013] | +0.8 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=64,tiling=tiles,type=four,vary=sharing | sharing | shared | 26.0799 | 26.3598 | 26.0503 | 26.3513 | -0.2687 [-0.3307, -0.2491] | -0.2839 [-0.3588, -0.2416] | -0.0088 [-0.0676, 0.0288] | +3.3 % | 10 | no | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing | sharing | shared | 3.2855 | 3.8708 | 3.2731 | 3.8694 | -0.5873 [-0.5918, -0.5808] | -0.5944 [-0.6015, -0.5908] | -0.0079 [-0.0140, -0.0039] | +1.3 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=1,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 3.7746 | 2.2306 | 3.0761 | 2.5278 | 1.5440 [1.5398, 1.5477] | 0.5482 [0.5432, 0.5521] | -0.9952 [-1.0025, -0.9911] | -64.5 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=16,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 53.7654 | 8.2701 | 45.8691 | 8.5533 | 45.4953 [45.4607, 45.5481] | 37.3160 [37.3031, 37.3271] | -8.1787 [-8.2345, -8.1441] | -18.0 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=2,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 6.7758 | 2.6329 | 5.9474 | 2.9272 | 4.1430 [4.1330, 4.1473] | 3.0203 [3.0164, 3.0232] | -1.1244 [-1.1267, -1.1087] | -27.1 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=4,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 13.4896 | 3.4373 | 11.6645 | 3.7318 | 10.0524 [10.0354, 10.0619] | 7.9334 [7.9295, 7.9358] | -2.1242 [-2.1268, -2.1011] | -21.1 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=64,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 220.4204 | 27.5904 | 183.0641 | 27.8745 | 192.8465 [192.7946, 192.9333] | 155.1937 [155.1381, 155.2345] | -37.6573 [-37.7208, -37.5613] | -19.5 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 26.4794 | 5.0372 | 23.1512 | 5.3370 | 21.4448 [21.4163, 21.4583] | 17.8124 [17.8048, 17.8236] | -3.6343 [-3.6450, -3.6115] | -16.9 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 26.6136 | 5.0292 | 22.9619 | 5.3692 | 21.5832 [21.5733, 21.6167] | 17.5942 [17.5829, 17.5968] | -3.9911 [-4.0357, -3.9767] | -18.5 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=1,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 3.7567 | 3.7255 | 3.1263 | 3.7750 | 0.0315 [0.0234, 0.0380] | -0.6508 [-0.6536, -0.6438] | -0.6812 [-0.6878, -0.6748] | -2162.4 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=16,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 53.0318 | 9.7420 | 46.0464 | 9.8216 | 43.2980 [43.2707, 43.3334] | 36.2305 [36.2157, 36.2412] | -7.0713 [-7.1016, -7.0549] | -16.3 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=2,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 6.8521 | 4.1071 | 5.9610 | 4.1347 | 2.7451 [2.7339, 2.7495] | 1.8317 [1.8176, 1.8360] | -0.9124 [-0.9324, -0.9072] | -33.2 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=4,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 13.5696 | 4.9292 | 11.6740 | 4.9849 | 8.6378 [8.6295, 8.6594] | 6.6883 [6.6809, 6.6926] | -1.9501 [-1.9699, -1.9390] | -22.6 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=64,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 213.3524 | 29.0952 | 182.9612 | 29.1674 | 184.2653 [184.2131, 184.3364] | 153.7961 [153.7533, 153.8214] | -30.4768 [-30.5699, -30.3746] | -16.5 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 26.5388 | 6.5170 | 23.0223 | 6.5753 | 20.0247 [19.9958, 20.0520] | 16.4412 [16.4251, 16.4520] | -3.5829 [-3.6185, -3.5541] | -17.9 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=1,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 0.5630 | 0.7512 | 0.5854 | 0.8402 | -0.1877 [-0.1901, -0.1866] | -0.2549 [-0.2560, -0.2536] | -0.0671 [-0.0689, -0.0640] | +35.7 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=16,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 6.7115 | 6.7841 | 6.8436 | 6.8770 | -0.0713 [-0.0901, -0.0544] | -0.0358 [-0.0422, -0.0280] | 0.0346 [0.0182, 0.0568] | -48.5 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=2,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 1.0485 | 1.1541 | 1.1741 | 1.2484 | -0.1062 [-0.1078, -0.1028] | -0.0722 [-0.0757, -0.0690] | 0.0333 [0.0287, 0.0392] | -31.4 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=4,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 1.8506 | 1.9574 | 1.8755 | 2.0483 | -0.1070 [-0.1097, -0.1040] | -0.1727 [-0.1751, -0.1694] | -0.0671 [-0.0701, -0.0608] | +62.7 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=64,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 25.9478 | 26.1346 | 26.0973 | 26.2180 | -0.1835 [-0.2252, -0.1399] | -0.1290 [-0.1773, -0.0570] | 0.0524 [-0.0556, 0.1065] | -28.5 % | 10 | no | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 3.4603 | 3.5632 | 3.4872 | 3.6482 | -0.1000 [-0.1087, -0.0941] | -0.1607 [-0.1673, -0.1515] | -0.0577 [-0.0722, -0.0438] | +57.7 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | sharing | shared | 3.5431 | 3.5489 | 3.5896 | 3.8480 | -0.0078 [-0.0136, 0.0061] | -0.2604 [-0.2696, -0.2502] | -0.2533 [-0.2637, -0.2510] | - | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=1,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 0.5789 | 1.2034 | 0.6583 | 1.1754 | -0.6234 [-0.6280, -0.6226] | -0.5176 [-0.5204, -0.5149] | 0.1081 [0.1027, 0.1099] | -17.3 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=16,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 6.7816 | 7.2478 | 6.7614 | 7.2297 | -0.4673 [-0.4743, -0.4534] | -0.4698 [-0.4769, -0.4530] | 0.0024 [-0.0154, 0.0149] | -0.5 % | 10 | no | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=2,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 1.0589 | 1.6036 | 1.0740 | 1.5762 | -0.5449 [-0.5490, -0.5418] | -0.5040 [-0.5059, -0.4965] | 0.0438 [0.0385, 0.0472] | -8.0 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=4,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 1.8510 | 2.4044 | 1.8735 | 2.3838 | -0.5528 [-0.5595, -0.5507] | -0.5087 [-0.5124, -0.5039] | 0.0438 [0.0384, 0.0499] | -7.9 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=64,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 26.1924 | 26.4264 | 26.0400 | 26.4148 | -0.2347 [-0.2778, -0.1631] | -0.3671 [-0.4211, -0.2720] | -0.1401 [-0.2180, -0.0086] | +59.7 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1 | sharing | shared | 3.5822 | 3.9989 | 3.5233 | 3.9775 | -0.4175 [-0.4322, -0.4098] | -0.4559 [-0.4614, -0.4519] | -0.0384 [-0.0480, -0.0178] | +9.2 % | 10 | yes | pass |
| at=shared,footprint-mib=8192,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | sharing | shared | 247.2523 | 24.9478 | 247.4941 | 24.6946 | 222.3104 [222.2629, 222.4397] | 222.7988 [222.7639, 222.8523] | 0.4931 [0.3633, 0.5874] | +0.2 % | 10 | yes | pass |
| at=shared,footprint-mib=8192,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing | sharing | shared | 15.1260 | 20.2347 | 15.1035 | 20.2246 | -5.1113 [-5.1214, -5.0925] | -5.1153 [-5.1442, -5.0800] | -0.0148 [-0.0488, 0.0078] | +0.3 % | 10 | no | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 7.8992 | 0.5078 | 8.0058 | 2.9208 | 7.3908 [7.3899, 7.3941] | 5.0393 [5.0097, 5.0835] | -2.4177 [-2.4713, -2.3561] | -32.7 % | 70 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 7.9005 | 23.4447 | 7.8550 | 23.1025 | -15.5538 [-15.6736, -15.5361] | -15.2543 [-15.3677, -15.2298] | 0.3074 [0.1833, 0.3983] | -2.0 % | 10 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 8.0705 | 0.5657 | 8.0941 | 1.7269 | 7.5050 [7.5000, 7.5104] | 6.3743 [6.3597, 6.3885] | -1.1307 [-1.1426, -1.1231] | -15.1 % | 10 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1 | sharing | shared | 8.0837 | 0.5653 | 8.0930 | 5.4437 | 7.5187 [7.5140, 7.5210] | 2.6493 [2.6462, 2.6897] | -4.8665 [-4.8720, -4.8223] | -64.7 % | 10 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | sharing | shared | 8.0927 | 5.6664 | 8.1201 | 5.6977 | 2.4263 [2.4033, 2.4363] | 2.4231 [2.3724, 2.4395] | -0.0084 [-0.0332, 0.0253] | -0.3 % | 10 | no | pass |
| at=shared,footprint-mib=9728,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | sharing | shared | 128.4142 | 0.5054 | 128.4781 | 3.2275 | 127.9085 [127.8464, 127.9526] | 125.2214 [125.1759, 125.2624] | -2.6765 [-2.7910, -2.6205] | -2.1 % | 20 | yes | pass |
| at=shared,footprint-mib=9728,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | sharing | shared | 128.2687 | 27.3524 | 128.2782 | 27.4506 | 100.9180 [100.7928, 100.9818] | 100.8250 [100.4855, 100.9122] | -0.0923 [-0.3717, 0.0344] | -0.1 % | 10 | no | pass |
| at=sys,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8 | scope | sys | 0.0301 | 0.0537 | 0.0308 | 0.0534 | -0.0236 [-0.0237, -0.0234] | -0.0226 [-0.0228, -0.0224] | 0.0010 [0.0008, 0.0012] | -4.2 % | 10 | yes | pass |
| at=sys,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=four,vary=scope,working-set-mib=8 | scope | sys | 0.0090 | 0.0505 | 0.0097 | 0.0507 | -0.0416 [-0.0417, -0.0415] | -0.0409 [-0.0410, -0.0409] | 0.0006 [0.0004, 0.0008] | -1.5 % | 40 | yes | pass |
| at=sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8 | scope | sys | 0.0380 | 0.0609 | 0.4018 | 0.0828 | -0.0230 [-0.0233, -0.0228] | 0.3190 [0.3180, 0.3205] | 0.3420 [0.3408, 0.3434] | -1489.0 % | 10 | yes | pass |
| at=sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=four,vary=scope,working-set-mib=8 | scope | sys | 0.0162 | 0.0590 | 0.0384 | 0.0837 | -0.0429 [-0.0431, -0.0423] | -0.0452 [-0.0454, -0.0439] | -0.0022 [-0.0027, -0.0016] | +5.2 % | 10 | yes | pass |
| at=sys,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8 | scope | sys | 0.0309 | 0.0536 | 0.0559 | 0.0560 | -0.0227 [-0.0228, -0.0225] | -0.0001 [-0.0002, 0.0002] | 0.0226 [0.0224, 0.0228] | -99.5 % | 10 | yes | pass |
| at=sys,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=four,vary=scope,working-set-mib=8 | scope | sys | 0.0093 | 0.0502 | 0.0115 | 0.0516 | -0.0409 [-0.0409, -0.0408] | -0.0401 [-0.0409, -0.0399] | 0.0009 [-0.0001, 0.0009] | -2.1 % | 30 | no | pass |
| at=sys,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8 | scope | sys | 0.0320 | 0.0554 | 0.1060 | 0.0601 | -0.0233 [-0.0234, -0.0232] | 0.0458 [0.0456, 0.0462] | 0.0692 [0.0689, 0.0695] | -296.6 % | 10 | yes | pass |
| at=sys,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=four,vary=scope,working-set-mib=8 | scope | sys | 0.0104 | 0.0504 | 0.0155 | 0.0591 | -0.0400 [-0.0403, -0.0399] | -0.0436 [-0.0438, -0.0433] | -0.0034 [-0.0038, -0.0032] | +8.6 % | 10 | yes | pass |
| at=sys,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8 | scope | sys | 0.0610 | 0.0856 | 1.5919 | 0.1717 | -0.0246 [-0.0249, -0.0244] | 1.4201 [1.4113, 1.4251] | 1.4447 [1.4360, 1.4501] | -5874.1 % | 10 | yes | pass |
| at=sys,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=four,vary=scope,working-set-mib=8 | scope | sys | 0.0387 | 0.0834 | 0.1280 | 0.1702 | -0.0447 [-0.0448, -0.0446] | -0.0422 [-0.0425, -0.0420] | 0.0027 [0.0022, 0.0028] | -5.9 % | 20 | yes | pass |

## Host phases

The CPU phase before every pass, timed on the CPU clock (ms per pass), and the state check's median load latency on the preparing core after the phase (ns per sampled load), per variant.

| cell | direct home CPU ms | direct home state ns | copy home CPU ms | copy home state ns | direct level CPU ms | direct level state ns | copy level CPU ms | copy level state ns |
|---|---|---|---|---|---|---|---|---|
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | 0.3283 | 6.5 | 0.3330 | 13.1 | 0.3286 | 12.5 | 0.3256 | 14.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 0.2805 | 9.0 | 0.2833 | 28.9 | 0.2758 | 23.6 | 0.2800 | 23.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | 0.3049 | 192.0 | 0.3095 | 168.4 | 0.3075 | 69.0 | 0.3088 | 70.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | 0.7155 | 6.8 | 0.7148 | 20.4 | 0.7370 | 15.2 | 0.7380 | 19.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | 0.7234 | 7.2 | 0.7222 | 38.5 | 0.6742 | 43.4 | 0.6795 | 37.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | 0.6999 | 362.9 | 0.6982 | 339.4 | 0.7002 | 354.4 | 0.6992 | 346.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | 228.5895 | 193.9 | 228.7059 | 296.5 | 233.8663 | 275.0 | 230.9020 | 340.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 109.0359 | 197.9 | 108.4993 | 299.2 | 108.5667 | 290.2 | 109.3467 | 353.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | 176.2984 | 206.1 | 170.2261 | 258.9 | 167.0687 | 260.2 | 167.1211 | 267.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | 316.0400 | 550.5 | 316.3056 | 558.1 | 316.8435 | 568.1 | 316.1518 | 570.6 |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | 142.3665 | 637.4 | 142.3700 | 646.4 | 142.1033 | 681.9 | 142.3589 | 700.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | 187.4037 | 545.9 | 187.8845 | 557.4 | 187.3568 | 556.9 | 187.5011 | 571.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | 27.6621 | 91.9 | 27.6654 | 113.5 | 29.2667 | 160.4 | 29.0555 | 135.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 13.7775 | 125.8 | 13.9191 | 149.0 | 13.7474 | 162.2 | 13.7516 | 154.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | 21.2535 | 200.0 | 21.4017 | 219.6 | 21.0806 | 226.9 | 21.0768 | 215.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | 35.8612 | 239.6 | 36.1113 | 207.5 | 40.1123 | 203.0 | 39.5361 | 214.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | 17.8552 | 305.5 | 17.9743 | 344.6 | 17.4285 | 320.8 | 18.3207 | 338.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | 23.8323 | 489.5 | 23.9939 | 507.0 | 23.6730 | 495.2 | 24.0049 | 520.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | 0.6365 | 32.4 | 0.6312 | 40.4 | 0.6509 | 40.8 | 0.6519 | 42.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 0.4677 | 28.6 | 0.4722 | 41.4 | 0.4342 | 40.0 | 0.4361 | 42.8 |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | 0.5543 | 210.8 | 0.5573 | 188.9 | 0.5458 | 112.9 | 0.5477 | 120.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | 1.0321 | 35.6 | 1.0328 | 41.9 | 1.1348 | 48.0 | 1.1405 | 44.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | 0.8543 | 49.9 | 0.8823 | 57.1 | 0.8361 | 52.1 | 0.8408 | 54.8 |
| at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | 0.9339 | 367.2 | 0.9356 | 367.8 | 0.9356 | 365.0 | 0.9360 | 370.6 |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | 57.1550 | 147.8 | 56.1467 | 206.5 | 58.2706 | 211.5 | 57.8583 | 255.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 27.3787 | 181.2 | 27.2935 | 222.4 | 27.3064 | 234.6 | 27.2898 | 241.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | 41.9339 | 203.0 | 41.9341 | 241.8 | 41.9335 | 248.1 | 43.0395 | 232.6 |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | 77.6640 | 345.1 | 77.7364 | 409.6 | 79.7719 | 411.1 | 79.0544 | 401.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | 36.1039 | 458.4 | 36.0915 | 479.6 | 35.7472 | 473.8 | 36.0275 | 475.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | 47.1065 | 505.5 | 47.1587 | 542.5 | 47.1137 | 530.6 | 47.3285 | 545.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | 6.8672 | 42.9 | 6.8394 | 43.4 | 7.9000 | 51.8 | 7.6313 | 49.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 4.1742 | 72.0 | 4.1664 | 71.8 | 3.6011 | 87.4 | 3.6310 | 83.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | 5.5602 | 203.8 | 5.5288 | 213.0 | 5.4620 | 194.6 | 5.6542 | 202.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | 7.5723 | 83.8 | 7.6421 | 67.1 | 9.1783 | 98.2 | 10.1989 | 94.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | 5.4914 | 138.1 | 5.7712 | 154.0 | 4.1670 | 174.2 | 4.9411 | 178.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | 6.4543 | 394.9 | 6.4630 | 435.6 | 5.9348 | 372.4 | 6.4624 | 421.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | 5.2688 | 65.0 | 5.2499 | 83.2 | 5.3811 | 181.0 | 5.3789 | 184.8 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 2.7298 | 78.9 | 2.7270 | 100.6 | 2.6695 | 104.5 | 2.6692 | 103.8 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | 10.6664 | 211.8 | 10.9295 | 210.1 | 11.0189 | 235.4 | 10.6594 | 228.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | 4.9229 | 88.8 | 5.1024 | 96.4 | 5.0538 | 146.0 | 5.0385 | 112.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | 2.8551 | 194.5 | 3.0257 | 196.4 | 2.8739 | 234.2 | 2.9529 | 222.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | 12.3007 | 466.9 | 12.2784 | 450.5 | 11.8895 | 412.4 | 12.3308 | 462.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | 1.8563 | 40.0 | 1.8725 | 42.0 | 1.9938 | 60.0 | 1.9968 | 52.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 1.1021 | 61.6 | 1.0963 | 61.5 | 1.0747 | 62.5 | 1.0700 | 66.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | 1.5352 | 212.2 | 1.5565 | 204.4 | 1.5329 | 176.6 | 1.5341 | 180.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | 2.2913 | 48.9 | 2.2952 | 49.6 | 2.7352 | 58.5 | 2.7416 | 52.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | 1.5226 | 95.8 | 1.5419 | 84.8 | 1.4958 | 114.6 | 1.4951 | 99.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | 1.9696 | 368.5 | 1.9807 | 363.9 | 1.9332 | 369.8 | 1.9337 | 365.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing | 21.9695 | 80.5 | 21.9992 | 82.6 | 21.8469 | 141.9 | 22.0694 | 132.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 10.3708 | 119.2 | 10.4071 | 129.8 | 10.4830 | 136.9 | 10.5073 | 148.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing | 15.8564 | 199.2 | 16.1814 | 207.5 | 15.8649 | 232.5 | 16.0237 | 223.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing | 27.8785 | 178.0 | 28.3652 | 179.0 | 30.2600 | 199.2 | 29.6221 | 198.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing | 12.5417 | 393.2 | 12.9171 | 447.8 | 13.0018 | 419.6 | 13.9064 | 475.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing | 18.1313 | 483.0 | 18.0887 | 493.4 | 17.8350 | 449.5 | 18.1916 | 498.2 |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | 1.2484 | - | 1.2203 | - | 1.6473 | - | 1.6562 | - |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing | 2.3951 | - | 3.7253 | - | 3.6932 | - | 3.1261 | - |
| at=shared,footprint-mib=1024,host=state,k=1,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8 | 2.0359 | 47.4 | 2.0652 | 48.2 | 2.0489 | 49.4 | 2.0534 | 44.2 |
| at=shared,footprint-mib=1024,host=state,k=1,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | 1.0842 | 75.8 | 1.0819 | 82.5 | 1.1129 | 87.1 | 1.0809 | 75.4 |
| at=shared,footprint-mib=1024,host=state,k=1,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8 | 1.5167 | 197.6 | 1.5391 | 196.1 | 1.5551 | 197.0 | 1.5193 | 191.9 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8 | 2.0212 | 75.9 | 2.0064 | 67.1 | 2.0187 | 79.6 | 2.0396 | 79.9 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | 1.0810 | 87.1 | 1.0790 | 90.2 | 1.0772 | 89.6 | 1.0834 | 82.4 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8 | 1.5516 | 205.0 | 1.5252 | 190.5 | 1.5185 | 192.9 | 1.5268 | 195.2 |
| at=shared,footprint-mib=1024,host=state,k=2,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8 | 2.0234 | 54.0 | 2.0211 | 56.0 | 2.0175 | 62.4 | 2.0189 | 59.0 |
| at=shared,footprint-mib=1024,host=state,k=2,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | 1.0899 | 71.9 | 1.0829 | 81.2 | 1.1022 | 78.2 | 1.0761 | 71.5 |
| at=shared,footprint-mib=1024,host=state,k=2,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8 | 1.5179 | 215.8 | 1.5173 | 205.1 | 1.5231 | 218.2 | 1.5217 | 224.4 |
| at=shared,footprint-mib=1024,host=state,k=4,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8 | 2.0208 | 69.0 | 2.0223 | 58.5 | 2.0611 | 65.4 | 2.0177 | 70.2 |
| at=shared,footprint-mib=1024,host=state,k=4,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | 1.0811 | 44.6 | 1.0787 | 42.9 | 1.0773 | 44.4 | 1.0730 | 42.0 |
| at=shared,footprint-mib=1024,host=state,k=4,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8 | 1.5187 | 199.1 | 1.5247 | 200.5 | 1.5204 | 194.2 | 1.5223 | 196.2 |
| at=shared,footprint-mib=1024,host=state,k=64,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8 | 2.0188 | 43.9 | 2.0262 | 41.5 | 2.0282 | 43.6 | 2.0182 | 44.2 |
| at=shared,footprint-mib=1024,host=state,k=64,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8 | 1.0765 | 44.2 | 1.0905 | 42.4 | 1.0840 | 43.6 | 1.0815 | 43.8 |
| at=shared,footprint-mib=1024,host=state,k=64,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8 | 1.5443 | 199.0 | 1.5165 | 200.9 | 1.5148 | 204.5 | 1.5200 | 197.1 |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 3.9752 | 131.6 | 4.0346 | 169.9 | 3.9846 | 191.0 | 4.4480 | 186.9 |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | 4.0729 | 144.9 | 4.0242 | 169.8 | 4.0711 | 177.1 | 4.5819 | 198.2 |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | 67.7937 | 200.6 | 67.8298 | 295.8 | 67.8786 | 321.2 | 67.7985 | 308.2 |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | 67.7549 | 213.5 | 67.7685 | 307.9 | 67.8816 | 308.1 | 67.8699 | 324.0 |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 4.4856 | 368.6 | 4.4943 | 401.0 | 4.4668 | 422.5 | 4.4187 | 449.0 |
| at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | 137.2347 | 662.8 | 137.2489 | 658.9 | 137.0049 | 601.8 | 137.3087 | 577.9 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 4.0511 | 78.2 | 4.0425 | 133.4 | 4.0627 | 132.8 | 4.5021 | 126.6 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | 4.0083 | 119.9 | 4.0013 | 163.9 | 4.0000 | 173.5 | 4.4190 | 171.0 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32 | 4.0315 | 127.6 | 4.0209 | 176.6 | 4.0807 | 194.9 | 4.6632 | 191.4 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=8 | 3.9608 | 83.0 | 3.9658 | 120.1 | 3.9513 | 132.4 | 4.3907 | 141.6 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | 67.6316 | 198.0 | 67.6890 | 303.5 | 67.9725 | 343.2 | 67.7580 | 326.8 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | 67.5321 | 196.4 | 67.5716 | 291.6 | 67.7948 | 334.2 | 67.7376 | 349.4 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 4.4966 | 338.9 | 4.5428 | 396.1 | 4.4951 | 425.1 | 4.5693 | 415.2 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32 | 4.5061 | 337.8 | 4.5272 | 374.8 | 4.5234 | 412.1 | 4.5293 | 381.8 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | 23.8389 | 552.4 | 23.6653 | 578.9 | 23.7846 | 587.1 | 23.6753 | 573.2 |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 4.0054 | 79.9 | 4.0036 | 126.5 | 4.0204 | 129.8 | 4.5214 | 129.8 |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | 4.0313 | 104.5 | 4.0285 | 147.8 | 4.0219 | 155.4 | 4.4552 | 165.0 |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | 67.7385 | 197.5 | 67.8177 | 286.6 | 67.8365 | 335.4 | 67.8438 | 320.0 |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | 67.7626 | 197.8 | 67.7965 | 299.5 | 67.8802 | 314.9 | 67.8887 | 338.1 |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 5.0512 | 368.4 | 4.9466 | 422.1 | 4.9771 | 456.6 | 4.9943 | 468.5 |
| at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | 137.3521 | 686.0 | 137.3708 | 686.9 | 136.9775 | 576.6 | 137.4531 | 566.4 |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 4.0355 | 108.4 | 4.0398 | 139.2 | 4.0491 | 151.0 | 4.5369 | 145.8 |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | 3.9915 | 89.9 | 4.0103 | 130.6 | 3.9834 | 124.9 | 4.4663 | 144.8 |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | 67.8132 | 196.2 | 67.8549 | 298.9 | 67.8855 | 318.6 | 67.7660 | 312.5 |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | 67.7658 | 199.2 | 67.7933 | 294.5 | 67.8652 | 316.9 | 67.8635 | 343.6 |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 4.9728 | 358.2 | 4.9918 | 437.6 | 4.8740 | 442.4 | 4.9271 | 417.8 |
| at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | 137.2224 | 660.6 | 137.2440 | 648.6 | 137.0582 | 595.9 | 137.2645 | 578.9 |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 4.0393 | 130.6 | 4.0556 | 162.8 | 3.9710 | 185.2 | 4.4743 | 183.1 |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8 | 4.0760 | 85.6 | 4.0867 | 124.2 | 4.0884 | 120.1 | 4.6347 | 133.4 |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32 | 67.8695 | 204.9 | 67.8158 | 293.2 | 67.9677 | 318.6 | 67.7983 | 302.8 |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8 | 67.7643 | 197.1 | 67.7960 | 311.9 | 67.8434 | 331.9 | 67.9002 | 325.6 |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32 | 5.0679 | 346.8 | 5.1536 | 368.8 | 5.0583 | 405.5 | 5.0626 | 390.0 |
| at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32 | 137.2441 | 653.0 | 137.2608 | 657.4 | 136.9161 | 562.4 | 137.2741 | 581.5 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 4.0921 | 126.0 | 4.0773 | 170.2 | 4.1068 | 185.0 | 4.4627 | 184.5 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 67.6270 | 204.8 | 67.6039 | 279.5 | 68.0046 | 312.4 | 67.9063 | 348.6 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | 4.5032 | 351.1 | 4.4524 | 362.2 | 4.4485 | 416.5 | 4.4679 | 396.1 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | 136.9016 | 692.5 | 136.9104 | 738.4 | 137.0223 | 596.8 | 136.9854 | 577.9 |
| at=shared,footprint-mib=11520,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 29.5722 | 287.2 | 31.0104 | 307.0 | 29.5780 | 302.6 | 28.8308 | 286.9 |
| at=shared,footprint-mib=11520,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 759.4192 | 344.6 | 759.1463 | 396.5 | 760.6380 | 369.6 | 759.6154 | 391.4 |
| at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 27.0633 | 283.1 | 27.4774 | 315.9 | 30.9467 | 320.6 | 27.8285 | 284.6 |
| at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 810.1589 | 354.6 | 809.8605 | 378.6 | 811.1008 | 392.8 | 809.9562 | 390.4 |
| at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | 36.4011 | 600.1 | 36.5142 | 599.5 | 38.2286 | 586.0 | 38.0606 | 586.1 |
| at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | 1638.7069 | 745.5 | 1638.9680 | 730.9 | 1638.6551 | 673.4 | 1638.5852 | 673.9 |
| at=shared,footprint-mib=1536,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 6.4016 | 163.1 | 6.4152 | 208.0 | 6.0677 | 215.8 | 6.5548 | 212.2 |
| at=shared,footprint-mib=1536,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 101.4336 | 219.6 | 101.3977 | 322.6 | 101.9083 | 348.2 | 101.6182 | 374.9 |
| at=shared,footprint-mib=16384,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | 25.9624 | - | 25.9812 | - | 26.6024 | - | 26.6042 | - |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing | 1.8432 | 164.4 | 1.8456 | 150.6 | 2.8968 | 164.1 | 2.9518 | 170.4 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 33.8516 | 277.9 | 31.6476 | 333.1 | 33.7407 | 302.5 | 31.5890 | 286.8 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1 | 32.8713 | 282.6 | 31.5900 | 324.6 | 32.5108 | 320.5 | 33.1493 | 284.9 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 266.6058 | 340.1 | 265.8495 | 347.8 | 266.6597 | 325.4 | 265.6663 | 347.6 |
| at=shared,footprint-mib=2048,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 8.2564 | 151.1 | 7.6568 | 210.9 | 7.9302 | 218.2 | 8.3445 | 215.8 |
| at=shared,footprint-mib=2048,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 134.9936 | 219.5 | 134.9400 | 330.1 | 135.5337 | 365.1 | 135.2147 | 373.6 |
| at=shared,footprint-mib=24576,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | 39.3387 | - | 39.3314 | - | 39.9415 | - | 39.9722 | - |
| at=shared,footprint-mib=24576,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 50.8524 | 362.9 | 51.3557 | 356.9 | 50.8419 | 361.4 | 51.2333 | 267.6 |
| at=shared,footprint-mib=24576,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 1625.0879 | 373.9 | 1624.3729 | 387.2 | 1626.5301 | 392.5 | 1626.0215 | 395.4 |
| at=shared,footprint-mib=256,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | 0.3030 | - | 0.3027 | - | 0.4142 | - | 0.4150 | - |
| at=shared,footprint-mib=256,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing | 0.3367 | - | 0.3163 | - | 0.9029 | - | 0.8930 | - |
| at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 1.1824 | 65.1 | 1.1642 | 104.1 | 1.2752 | 125.5 | 1.2917 | 145.6 |
| at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 16.9128 | 161.5 | 16.9047 | 218.5 | 17.1475 | 240.8 | 17.1219 | 225.5 |
| at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | 1.7430 | 68.4 | 1.7454 | 96.4 | 1.7407 | 99.8 | 1.7427 | 100.6 |
| at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | 34.6395 | 509.6 | 34.6472 | 502.6 | 34.6313 | 497.1 | 34.6475 | 505.6 |
| at=shared,footprint-mib=32768,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | 52.6244 | - | 52.6689 | - | 53.1080 | - | 53.1262 | - |
| at=shared,footprint-mib=32768,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 65.8478 | 377.9 | 67.4357 | 362.1 | 66.3345 | 363.8 | 66.1241 | 271.0 |
| at=shared,footprint-mib=32768,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 2169.6927 | 381.8 | 2169.0534 | 392.9 | 2169.6572 | 387.8 | 2166.3810 | 395.2 |
| at=shared,footprint-mib=4096,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | 5.8992 | - | 5.8222 | - | 6.6222 | - | 6.6413 | - |
| at=shared,footprint-mib=4096,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing | 14.8255 | - | 14.8453 | - | 14.8137 | - | 14.4205 | - |
| at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 14.1901 | 204.8 | 14.3567 | 251.6 | 14.0346 | 262.0 | 14.2439 | 253.9 |
| at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 270.0961 | 275.8 | 269.9974 | 363.1 | 270.3415 | 378.1 | 269.9662 | 386.0 |
| at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | 14.5363 | 502.1 | 15.2874 | 560.0 | 14.6838 | 573.2 | 14.8455 | 552.2 |
| at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | 546.6215 | 698.6 | 546.6686 | 695.4 | 546.6728 | 673.9 | 546.5545 | 678.2 |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=1,tiling=tiles,type=four,vary=sharing | 27.2126 | - | 27.2175 | - | 28.2751 | - | 28.2939 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=16,tiling=tiles,type=four,vary=sharing | 27.3216 | - | 27.3237 | - | 28.2605 | - | 28.3114 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=2,tiling=tiles,type=four,vary=sharing | 27.2559 | - | 27.2399 | - | 28.2781 | - | 28.2875 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=4,tiling=tiles,type=four,vary=sharing | 27.1693 | - | 27.1473 | - | 28.2162 | - | 28.2379 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=64,tiling=tiles,type=four,vary=sharing | 27.6561 | - | 27.6570 | - | 28.2676 | - | 28.2975 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing | 27.3103 | - | 27.2577 | - | 28.2255 | - | 28.2377 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=1,tiling=tiles,type=four,vary=sharing | 62.8495 | - | 62.9717 | - | 62.3981 | - | 62.4634 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=16,tiling=tiles,type=four,vary=sharing | 62.9287 | - | 62.9873 | - | 62.5396 | - | 62.6541 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=2,tiling=tiles,type=four,vary=sharing | 62.8196 | - | 62.9328 | - | 62.4074 | - | 62.4833 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=4,tiling=tiles,type=four,vary=sharing | 62.8662 | - | 62.9776 | - | 62.4397 | - | 62.4917 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=64,tiling=tiles,type=four,vary=sharing | 63.0565 | - | 63.0607 | - | 63.0391 | - | 63.0337 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing | 62.8489 | - | 62.9462 | - | 62.4797 | - | 62.5187 | - |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=1,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.1303 | 65.2 | 2.1251 | 105.9 | 2.3029 | 120.4 | 2.2809 | 108.5 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=16,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.2002 | 90.4 | 2.1432 | 108.8 | 2.2190 | 135.0 | 2.3400 | 124.0 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=2,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.1521 | 92.5 | 2.1373 | 133.2 | 2.2943 | 155.8 | 2.2636 | 146.8 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=4,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.2001 | 100.2 | 2.1514 | 142.0 | 2.2266 | 154.1 | 2.3349 | 148.4 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=64,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.2182 | 74.4 | 2.2139 | 126.1 | 2.3291 | 141.8 | 2.2554 | 125.6 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | 1.9555 | 64.2 | 1.9785 | 108.2 | 1.9986 | 129.4 | 2.0266 | 116.2 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | 1.9752 | 79.8 | 1.9654 | 119.4 | 2.0392 | 133.4 | 2.2080 | 125.6 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=1,tiling=tiles,type=four,vary=sharing,w=1 | 33.8626 | 184.6 | 33.7979 | 271.5 | 34.0930 | 251.5 | 34.3451 | 261.0 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=16,tiling=tiles,type=four,vary=sharing,w=1 | 33.9113 | 181.5 | 33.8636 | 300.0 | 34.1449 | 304.9 | 34.3853 | 320.9 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=2,tiling=tiles,type=four,vary=sharing,w=1 | 33.8459 | 189.6 | 33.7733 | 243.5 | 34.1206 | 260.8 | 34.3893 | 300.9 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=4,tiling=tiles,type=four,vary=sharing,w=1 | 33.8885 | 201.9 | 33.8074 | 297.6 | 34.1001 | 269.0 | 34.2896 | 312.9 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=64,tiling=tiles,type=four,vary=sharing,w=1 | 33.9567 | 186.1 | 33.9130 | 295.2 | 34.1037 | 284.2 | 34.3683 | 298.8 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1 | 13.2909 | 252.4 | 13.4422 | 280.1 | 13.2994 | 270.6 | 13.2714 | 278.9 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=1,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.5843 | 194.5 | 2.5649 | 231.9 | 2.5610 | 238.0 | 2.5304 | 266.6 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=16,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.9844 | 212.5 | 2.9540 | 273.1 | 2.8783 | 264.0 | 2.8856 | 263.8 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=2,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.5858 | 216.0 | 2.5852 | 265.9 | 2.5647 | 290.0 | 2.5520 | 278.6 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=4,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.9186 | 198.6 | 2.9384 | 218.9 | 2.8372 | 229.6 | 2.8733 | 274.1 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=64,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.6867 | 240.9 | 2.6840 | 267.8 | 2.6584 | 270.8 | 2.6522 | 293.8 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.5846 | 240.1 | 2.5664 | 317.6 | 2.5554 | 319.0 | 2.5631 | 319.6 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1 | 2.5934 | 205.8 | 2.5925 | 220.5 | 2.5865 | 232.6 | 2.5926 | 247.2 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=1,tiling=tiles,type=four,vary=sharing,w=1 | 68.8936 | 477.1 | 68.8637 | 521.8 | 68.7789 | 522.6 | 68.8982 | 541.4 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=16,tiling=tiles,type=four,vary=sharing,w=1 | 68.9943 | 538.5 | 68.9717 | 581.6 | 68.9890 | 532.2 | 68.9719 | 562.5 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=2,tiling=tiles,type=four,vary=sharing,w=1 | 68.9202 | 557.4 | 68.8755 | 566.4 | 68.8536 | 592.2 | 68.8730 | 571.0 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=4,tiling=tiles,type=four,vary=sharing,w=1 | 68.9355 | 531.1 | 68.9222 | 567.2 | 68.8682 | 552.6 | 68.9003 | 573.0 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=64,tiling=tiles,type=four,vary=sharing,w=1 | 68.9872 | 554.2 | 69.0245 | 613.9 | 68.9798 | 622.0 | 68.9734 | 625.5 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1 | 16.1766 | 475.9 | 15.7931 | 538.6 | 16.1487 | 538.5 | 15.7177 | 548.4 |
| at=shared,footprint-mib=8192,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing | 12.4522 | - | 12.4921 | - | 13.2512 | - | 13.2499 | - |
| at=shared,footprint-mib=8192,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing | 29.6702 | - | 29.6739 | - | 29.6589 | - | 29.6668 | - |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 19.9366 | 248.9 | 19.9080 | 277.8 | 19.9971 | 277.6 | 20.9943 | 265.1 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 539.9119 | 337.6 | 539.8006 | 379.8 | 540.5299 | 390.1 | 539.7581 | 392.4 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1 | 24.0949 | 547.9 | 23.7790 | 570.4 | 23.7646 | 582.0 | 24.8057 | 574.0 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1 | 23.5130 | 550.0 | 23.4450 | 575.6 | 23.1620 | 573.2 | 22.6338 | 571.5 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1 | 164.4103 | 625.8 | 165.4447 | 629.0 | 164.4000 | 625.0 | 165.7518 | 626.6 |
| at=shared,footprint-mib=9728,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1 | 23.1486 | 257.1 | 25.8432 | 272.9 | 25.2791 | 277.6 | 24.7454 | 285.5 |
| at=shared,footprint-mib=9728,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1 | 641.3779 | 347.5 | 641.1816 | 370.1 | 642.2722 | 377.6 | 641.1819 | 387.5 |

## Per cell

### route/at=1,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x417a80000000, copy home 0x417b40000000, direct level 0x417c00000000, copy level 0x417cc0000000
- factor effect within the cell: on the direct route -0.0001 [-0.0001, -0.0001] ms, on the copy route -0.0007 [-0.0011, -0.0005] ms; change relative to the copy call at home: +1.1 %
- per repetition: direct home 8.38e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.7 SMMU translation requests; direct level 8.38e+06 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=four,vary=rotated,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x58f840000000, copy home 0x58f940000000, direct level 0x58fa00000000, copy level 0x58fac0000000
- factor effect within the cell: on the direct route 0.0001 [0.0001, 0.0001] ms, on the copy route 0.0001 [-0.0002, 0.0005] ms; change relative to the copy call at home: +0.1 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 134.4 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=k,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 1.0568 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5a7280000000, copy home 0x5a7340000000, direct level 0x5a7400000000, copy level 0x5a74c0000000
- factor effect within the cell: on the direct route -1.4031 [-1.4041, -1.4027] ms, on the copy route -0.0656 [-0.0658, -0.0651] ms; change relative to the copy call at home: -703.5 %
- per repetition: direct home 5.365e+08 link read bytes and 0 SMMU translation requests; copy home 3.354e+07 link read bytes and 533 SMMU translation requests; direct level 3.354e+07 link read bytes and 0 SMMU translation requests; copy level 3.354e+07 link read bytes and 533 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x56f600000000, copy home 0x56f700000000, direct level 0x56f7c0000000, copy level 0x56f880000000
- factor effect within the cell: on the direct route 0.3349 [0.3343, 0.3354] ms, on the copy route 0.0148 [0.0146, 0.0150] ms; change relative to the copy call at home: +523.1 %
- per repetition: direct home 8.382e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.7 SMMU translation requests; direct level 1.341e+08 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=four,vary=k,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 1.0568 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x424640000000, copy home 0x4247c0000000, direct level 0x424880000000, copy level 0x424940000000
- factor effect within the cell: on the direct route -0.0803 [-0.0804, -0.0802] ms, on the copy route -0.0641 [-0.0647, -0.0637] ms; change relative to the copy call at home: -8.9 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 520.4 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 518.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=four,vary=rotated,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x430480000000, copy home 0x430580000000, direct level 0x430640000000, copy level 0x430700000000
- factor effect within the cell: on the direct route 0.0138 [0.0138, 0.0138] ms, on the copy route 0.0157 [0.0153, 0.0159] ms; change relative to the copy call at home: -3.3 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 134.4 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 135 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4e6940000000, copy home 0x4e6a40000000, direct level 0x4e6b00000000, copy level 0x4e6bc0000000
- factor effect within the cell: on the direct route 0.0224 [0.0223, 0.0224] ms, on the copy route 0.0004 [-0.0000, 0.0007] ms; change relative to the copy call at home: +40.7 %
- per repetition: direct home 8.382e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.7 SMMU translation requests; direct level 1.676e+07 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=four,vary=rotated,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4e5f80000000, copy home 0x4e6080000000, direct level 0x4e6140000000, copy level 0x4e6200000000
- factor effect within the cell: on the direct route 0.0009 [0.0009, 0.0009] ms, on the copy route 0.0002 [-0.0002, 0.0004] ms; change relative to the copy call at home: +1.4 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 134.2 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x526fc0000000, copy home 0x5270c0000000, direct level 0x527180000000, copy level 0x527240000000
- factor effect within the cell: on the direct route 0.0672 [0.0671, 0.0672] ms, on the copy route 0.0029 [0.0027, 0.0032] ms; change relative to the copy call at home: +116.0 %
- per repetition: direct home 8.382e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.7 SMMU translation requests; direct level 3.352e+07 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=four,vary=rotated,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x41c8c0000000, copy home 0x41c9c0000000, direct level 0x41ca80000000, copy level 0x41cb40000000
- factor effect within the cell: on the direct route 0.0027 [0.0027, 0.0028] ms, on the copy route 0.0080 [0.0078, 0.0082] ms; change relative to the copy call at home: -10.5 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 134.3 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=four,vary=rotated,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x48f500000000, copy home 0x48f640000000, direct level 0x48f700000000, copy level 0x48f7c0000000
- factor effect within the cell: on the direct route 1.3904 [1.3864, 1.3920] ms, on the copy route 0.0504 [0.0501, 0.0508] ms; change relative to the copy call at home: +1562.6 %
- per repetition: direct home 8.382e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.7 SMMU translation requests; direct level 5.363e+08 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=four,vary=rotated,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x415200000000, copy home 0x4152c0000000, direct level 0x415380000000, copy level 0x415440000000
- factor effect within the cell: on the direct route 0.0511 [0.0510, 0.0512] ms, on the copy route 0.0502 [0.0496, 0.0506] ms; change relative to the copy call at home: +1.1 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 134.5 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 136.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sweeps

- seed 71; every round ran in the drawn order: yes; floor 1.0568 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4ed880000000, copy home 0x4ed9c0000000, direct level 0x4edac0000000, copy level 0x4edb80000000
- factor effect within the cell: on the direct route -23.3333 [-23.3457, -23.2872] ms, on the copy route -2.8711 [-2.8749, -2.8653] ms; change relative to the copy call at home: -315.1 %
- per repetition: direct home 6.422e+09 link read bytes and 3.608e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 8.028e+08 link read bytes and 3189 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sweeps

- seed 71; every round ran in the drawn order: yes; floor 1.0568 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5384c0000000, copy home 0x5385c0000000, direct level 0x538680000000, copy level 0x538780000000
- factor effect within the cell: on the direct route -2.8661 [-2.8678, -2.8615] ms, on the copy route -2.8151 [-2.8180, -2.8103] ms; change relative to the copy call at home: -1.3 %
- per repetition: direct home 0 link read bytes and 5986 SMMU translation requests; copy home 0 link read bytes and 5334 SMMU translation requests; direct level 0 link read bytes and 513.2 SMMU translation requests; copy level 0 link read bytes and 1628 SMMU translation requests; multiplexed rows voided: 0

### route/at=16384,footprint-mib=1024,kernel=k3,placement=cpu,type=four,vary=footprint

- seed 71; every round ran in the drawn order: yes; floor 1.0568 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x433c00000000, copy home 0x433cc0000000, direct level 0x433d80000000, copy level 0x434280000000
- factor effect within the cell: on the direct route 427.4092 [427.2772, 427.5142] ms, on the copy route 42.3790 [42.3705, 42.3952] ms; change relative to the copy call at home: +11156.8 %
- per repetition: direct home 5.369e+08 link read bytes and 4314 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.64e+04 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy level 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=16384,footprint-mib=1024,kernel=k3,placement=hbm,type=four,vary=footprint

- seed 71; every round ran in the drawn order: yes; floor 1.0568 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5d0f80000000, copy home 0x5d1040000000, direct level 0x5d1100000000, copy level 0x5d15c0000000
- factor effect within the cell: on the direct route 424.5483 [424.4175, 424.6743] ms, on the copy route 9.5317 [9.5075, 9.5495] ms; change relative to the copy call at home: +37053.3 %
- per repetition: direct home 0 link read bytes and 404.5 SMMU translation requests; copy home 0 link read bytes and 2721 SMMU translation requests; direct level 0 link read bytes and 1.207e+08 SMMU translation requests; copy level 0 link read bytes and 6.495e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=f

- seed 71; every round ran in the drawn order: yes; floor 1.0568 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x471100000000, copy home 0x471200000000, direct level 0x4712c0000000, copy level 0x471380000000
- factor effect within the cell: on the direct route -2.8717 [-2.8723, -2.8712] ms, on the copy route -3.2343 [-3.2358, -3.2329] ms; change relative to the copy call at home: +11.0 %
- per repetition: direct home 1.074e+09 link read bytes and 0 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.64e+04 SMMU translation requests; direct level 1.074e+07 link read bytes and 0 SMMU translation requests; copy level 1.074e+07 link read bytes and 0.04178 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=four,vary=f

- seed 71; every round ran in the drawn order: yes; floor 1.0568 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x463580000000, copy home 0x463680000000, direct level 0x463740000000, copy level 0x463800000000
- factor effect within the cell: on the direct route -0.2888 [-0.2890, -0.2887] ms, on the copy route -0.9132 [-0.9154, -0.9127] ms; change relative to the copy call at home: +66.1 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 0 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=11520,kernel=k3,placement=cpu,type=four,vary=partition

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x47bec0000000, copy home 0x47c240000000, direct level 0x47c580000000, copy level 0x47c940000000
- factor effect within the cell: on the direct route -234.3761 [-234.4771, -234.0021] ms, on the copy route -1.7366 [-1.7469, -1.7203] ms; change relative to the copy call at home: -712.0 %
- per repetition: direct home 5.369e+08 link read bytes and 6.723e+07 SMMU translation requests; copy home 1.211e+10 link read bytes and 1.843e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.886e+05 SMMU translation requests; copy level 1.211e+10 link read bytes and 1.843e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=12288,kernel=k3,placement=cpu,type=four,vary=partition

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x505780000000, copy home 0x505b40000000, direct level 0x505ec0000000, copy level 0x506280000000
- factor effect within the cell: on the direct route -273.6705 [-273.8889, -273.3596] ms, on the copy route -1.9044 [-1.9124, -1.8794] ms; change relative to the copy call at home: -781.4 %
- per repetition: direct home 5.369e+08 link read bytes and 7.821e+07 SMMU translation requests; copy home 1.292e+10 link read bytes and 1.966e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 2.011e+05 SMMU translation requests; copy level 1.292e+10 link read bytes and 1.966e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=12288,kernel=k3,placement=hbm,type=four,vary=partition

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5b0fc0000000, copy home 0x5b1380000000, direct level 0x5b1700000000, copy level 0x5b1ac0000000
- factor effect within the cell: on the direct route -108.0250 [-109.8249, -107.1850] ms, on the copy route 0.1503 [0.1432, 0.1706] ms; change relative to the copy call at home: -1329.4 %
- per repetition: direct home 0 link read bytes and 7.777e+07 SMMU translation requests; copy home 0 link read bytes and 4.733e+05 SMMU translation requests; direct level 0 link read bytes and 4.566e+07 SMMU translation requests; copy level 0 link read bytes and 4.526e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=partition

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4c4440000000, copy home 0x4c4900000000, direct level 0x4c4d80000000, copy level 0x4c5240000000
- factor effect within the cell: on the direct route -427.0380 [-427.1389, -426.9216] ms, on the copy route -3.0706 [-3.0758, -3.0667] ms; change relative to the copy call at home: -918.1 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 3.483e+05 SMMU translation requests; copy level 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=24576,kernel=k3,placement=cpu,type=four,vary=partition

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x544340000000, copy home 0x5449c0000000, direct level 0x545040000000, copy level 0x545700000000
- factor effect within the cell: on the direct route -591.1060 [-591.1469, -591.0410] ms, on the copy route -1.8874 [-1.8968, -1.8808] ms; change relative to the copy call at home: -895.1 %
- per repetition: direct home 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; copy home 2.585e+10 link read bytes and 3.933e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 7.314e+05 SMMU translation requests; copy level 2.585e+10 link read bytes and 3.932e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=32768,kernel=k3,placement=cpu,type=four,vary=partition

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: no, cap hit: yes
- home at placement cpu, level at placement cpu; buffers: direct home 0x45aec0000000, copy home 0x45b740000000, direct level 0x45bfc0000000, copy level 0x45c880000000
- factor effect within the cell: on the direct route -671.5212 [-671.9329, -671.1704] ms, on the copy route -1.0138 [-1.0206, -1.0066] ms; change relative to the copy call at home: -779.5 %
- per repetition: direct home 5.369e+08 link read bytes and 1.912e+08 SMMU translation requests; copy home 3.448e+10 link read bytes and 5.244e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 2.813e+06 SMMU translation requests; copy level 3.448e+10 link read bytes and 5.245e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=4096,kernel=k3,placement=cpu,type=four,vary=partition

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x596c80000000, copy home 0x596e40000000, direct level 0x596fc0000000, copy level 0x597180000000
- factor effect within the cell: on the direct route 0.0084 [-0.0090, 0.0681] ms, on the copy route 0.1564 [0.1540, 0.1595] ms; change relative to the copy call at home: -1.3 %
- per repetition: direct home 5.369e+08 link read bytes and 1311 SMMU translation requests; copy home 4.295e+09 link read bytes and 6.556e+04 SMMU translation requests; direct level 5.369e+08 link read bytes and 1794 SMMU translation requests; copy level 4.295e+09 link read bytes and 6.556e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=4096,kernel=k3,placement=hbm,type=four,vary=partition

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x569b00000000, copy home 0x569cc0000000, direct level 0x569e40000000, copy level 0x56a000000000
- factor effect within the cell: on the direct route -1.4301 [-1.4545, -1.4100] ms, on the copy route 0.1794 [0.1766, 0.1819] ms; change relative to the copy call at home: -53.2 %
- per repetition: direct home 0 link read bytes and 1.664e+04 SMMU translation requests; copy home 0 link read bytes and 2.485e+04 SMMU translation requests; direct level 0 link read bytes and 1.125e+04 SMMU translation requests; copy level 0 link read bytes and 2.484e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=8192,kernel=k3,placement=cpu,type=four,vary=partition

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x549140000000, copy home 0x549400000000, direct level 0x549680000000, copy level 0x549940000000
- factor effect within the cell: on the direct route -2.3085 [-2.3382, -2.1655] ms, on the copy route -0.7553 [-0.7685, -0.7399] ms; change relative to the copy call at home: -6.6 %
- per repetition: direct home 5.369e+08 link read bytes and 4.416e+04 SMMU translation requests; copy home 8.607e+09 link read bytes and 1.311e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 3.415e+04 SMMU translation requests; copy level 8.607e+09 link read bytes and 1.311e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=8192,kernel=k3,placement=hbm,type=four,vary=partition

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x530480000000, copy home 0x530740000000, direct level 0x5309c0000000, copy level 0x530c80000000
- factor effect within the cell: on the direct route -2.0268 [-2.0395, -1.9526] ms, on the copy route 0.1807 [0.1714, 0.1974] ms; change relative to the copy call at home: -39.7 %
- per repetition: direct home 0 link read bytes and 4.428e+04 SMMU translation requests; copy home 0 link read bytes and 1.162e+05 SMMU translation requests; direct level 0 link read bytes and 3.488e+04 SMMU translation requests; copy level 0 link read bytes and 1.141e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=9728,kernel=k3,placement=cpu,type=four,vary=partition

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4f5240000000, copy home 0x4f5540000000, direct level 0x4f5800000000, copy level 0x4f5b40000000
- factor effect within the cell: on the direct route -122.5913 [-122.6577, -122.5200] ms, on the copy route 0.1757 [0.1584, 0.2100] ms; change relative to the copy call at home: -449.0 %
- per repetition: direct home 5.369e+08 link read bytes and 3.597e+07 SMMU translation requests; copy home 1.02e+10 link read bytes and 1.626e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.313e+05 SMMU translation requests; copy level 1.02e+10 link read bytes and 1.622e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-order

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5d33c0000000, copy home 0x5d3840000000, direct level 0x5d3cc0000000, copy level 0x5d41c0000000
- factor effect within the cell: on the direct route -428.0804 [-428.2349, -427.8164] ms, on the copy route -2.9733 [-2.9853, -2.9560] ms; change relative to the copy call at home: -927.9 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; direct level 5.368e+08 link read bytes and 6.343e+05 SMMU translation requests; copy level 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=1024,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5b8f40000000, copy home 0x5b9000000000, direct level 0x5b90c0000000, copy level 0x5b91c0000000
- factor effect within the cell: on the direct route -0.0393 [-0.0402, -0.0384] ms, on the copy route -0.2886 [-0.2909, -0.2853] ms; change relative to the copy call at home: +7.3 %
- per repetition: direct home 5.369e+08 link read bytes and 0 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.641e+04 SMMU translation requests; direct level 5.369e+08 link read bytes and 0 SMMU translation requests; copy level 1.074e+09 link read bytes and 51.14 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=1024,kernel=k3,placement=hbm,type=four,vary=page-size

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5f67c0000000, copy home 0x5f68c0000000, direct level 0x5f6980000000, copy level 0x5f6a80000000
- factor effect within the cell: on the direct route -0.0001 [-0.0004, 0.0000] ms, on the copy route -0.0017 [-0.0027, -0.0003] ms; change relative to the copy call at home: +0.1 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 0 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=11520,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4bde00000000, copy home 0x4be140000000, direct level 0x4be4c0000000, copy level 0x4be840000000
- factor effect within the cell: on the direct route -234.7808 [-234.8440, -234.7433] ms, on the copy route -2.4979 [-2.5258, -2.4856] ms; change relative to the copy call at home: -711.7 %
- per repetition: direct home 5.369e+08 link read bytes and 6.716e+07 SMMU translation requests; copy home 1.211e+10 link read bytes and 1.843e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 109 SMMU translation requests; copy level 1.211e+10 link read bytes and 379 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=12288,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5afa00000000, copy home 0x5afd80000000, direct level 0x5b0100000000, copy level 0x5b04c0000000
- factor effect within the cell: on the direct route -273.7032 [-273.7949, -273.5122] ms, on the copy route -2.6609 [-2.6712, -2.6454] ms; change relative to the copy call at home: -779.6 %
- per repetition: direct home 5.369e+08 link read bytes and 7.814e+07 SMMU translation requests; copy home 1.292e+10 link read bytes and 1.966e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 117.2 SMMU translation requests; copy level 1.292e+10 link read bytes and 404 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=1536,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x52a980000000, copy home 0x52aa80000000, direct level 0x52ab80000000, copy level 0x52acc0000000
- factor effect within the cell: on the direct route -0.0231 [-0.0235, -0.0225] ms, on the copy route -0.3680 [-0.3699, -0.3644] ms; change relative to the copy call at home: +7.2 %
- per repetition: direct home 5.369e+08 link read bytes and 0 SMMU translation requests; copy home 1.611e+09 link read bytes and 2.46e+04 SMMU translation requests; direct level 5.369e+08 link read bytes and 0 SMMU translation requests; copy level 1.611e+09 link read bytes and 66.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x50d900000000, copy home 0x50ddc0000000, direct level 0x50e240000000, copy level 0x50e700000000
- factor effect within the cell: on the direct route -427.3599 [-427.4033, -427.2693] ms, on the copy route -3.5071 [-3.5297, -3.3432] ms; change relative to the copy call at home: -918.3 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 148.1 SMMU translation requests; copy level 1.723e+10 link read bytes and 532 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=16384,kernel=k3p,placement=cpu,type=four,vary=page-size

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x57c9c0000000, copy home 0x57ce40000000, direct level 0x57d2c0000000, copy level 0x57d740000000
- factor effect within the cell: on the direct route -6.9325 [-6.9422, -6.9236] ms, on the copy route -2.9512 [-2.9689, -2.9334] ms; change relative to the copy call at home: -8.8 %
- per repetition: direct home 3.355e+07 link read bytes and 1.962e+06 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; direct level 3.355e+07 link read bytes and 2.965 SMMU translation requests; copy level 1.723e+10 link read bytes and 531 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=2048,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x484bc0000000, copy home 0x484d00000000, direct level 0x484e00000000, copy level 0x484f40000000
- factor effect within the cell: on the direct route -0.0150 [-0.0154, -0.0144] ms, on the copy route -0.4417 [-0.4436, -0.4402] ms; change relative to the copy call at home: +6.9 %
- per repetition: direct home 5.369e+08 link read bytes and 0 SMMU translation requests; copy home 2.147e+09 link read bytes and 3.279e+04 SMMU translation requests; direct level 5.369e+08 link read bytes and 0 SMMU translation requests; copy level 2.147e+09 link read bytes and 83 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=24576,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x503c80000000, copy home 0x504340000000, direct level 0x5049c0000000, copy level 0x505080000000
- factor effect within the cell: on the direct route -592.9330 [-593.0028, -592.8582] ms, on the copy route -1.9027 [-1.9195, -1.8854] ms; change relative to the copy call at home: -901.1 %
- per repetition: direct home 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; copy home 2.585e+10 link read bytes and 3.932e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 214.6 SMMU translation requests; copy level 2.585e+10 link read bytes and 788 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=256,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x53f800000000, copy home 0x53f900000000, direct level 0x53f980000000, copy level 0x53fa40000000
- factor effect within the cell: on the direct route -0.1839 [-0.1845, -0.1834] ms, on the copy route -0.0957 [-0.0973, -0.0951] ms; change relative to the copy call at home: -7.3 %
- per repetition: direct home 5.368e+08 link read bytes and 0 SMMU translation requests; copy home 2.684e+08 link read bytes and 4117 SMMU translation requests; direct level 5.368e+08 link read bytes and 0 SMMU translation requests; copy level 2.684e+08 link read bytes and 27.74 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=256,kernel=k3,placement=hbm,type=four,vary=page-size

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5a33c0000000, copy home 0x5a3480000000, direct level 0x5a3500000000, copy level 0x5a3600000000
- factor effect within the cell: on the direct route -0.0013 [-0.0016, -0.0011] ms, on the copy route -0.0005 [-0.0012, 0.0010] ms; change relative to the copy call at home: -0.1 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 4130 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 41.34 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=32768,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4af700000000, copy home 0x4aff80000000, direct level 0x4b0800000000, copy level 0x4b10c0000000
- factor effect within the cell: on the direct route -678.5190 [-678.5886, -678.4274] ms, on the copy route -1.1710 [-1.2014, -1.1476] ms; change relative to the copy call at home: -788.5 %
- per repetition: direct home 5.369e+08 link read bytes and 1.912e+08 SMMU translation requests; copy home 3.448e+10 link read bytes and 5.244e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 277.4 SMMU translation requests; copy level 3.448e+10 link read bytes and 1044 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=4096,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5f9800000000, copy home 0x5f99c0000000, direct level 0x5f9b40000000, copy level 0x5f9d00000000
- factor effect within the cell: on the direct route -0.1263 [-0.1878, -0.1030] ms, on the copy route -0.9240 [-0.9259, -0.9169] ms; change relative to the copy call at home: +6.4 %
- per repetition: direct home 5.369e+08 link read bytes and 0 SMMU translation requests; copy home 4.295e+09 link read bytes and 6.556e+04 SMMU translation requests; direct level 5.369e+08 link read bytes and 0 SMMU translation requests; copy level 4.295e+09 link read bytes and 148 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=4096,kernel=k3,placement=hbm,type=four,vary=page-size

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5b7500000000, copy home 0x5b76c0000000, direct level 0x5b7840000000, copy level 0x5b7a00000000
- factor effect within the cell: on the direct route -4.6446 [-4.6520, -4.6405] ms, on the copy route -0.0064 [-0.0139, -0.0034] ms; change relative to the copy call at home: -152.7 %
- per repetition: direct home 0 link read bytes and 2794 SMMU translation requests; copy home 0 link read bytes and 5079 SMMU translation requests; direct level 0 link read bytes and 4.75 SMMU translation requests; copy level 0 link read bytes and 22.36 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=8192,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4aac80000000, copy home 0x4aaf40000000, direct level 0x4ab1c0000000, copy level 0x4ab480000000
- factor effect within the cell: on the direct route -2.3777 [-2.3810, -2.3742] ms, on the copy route -2.0086 [-2.0207, -1.9983] ms; change relative to the copy call at home: -1.6 %
- per repetition: direct home 5.369e+08 link read bytes and 7955 SMMU translation requests; copy home 8.607e+09 link read bytes and 1.311e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 82.88 SMMU translation requests; copy level 8.607e+09 link read bytes and 276 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=8192,kernel=k3,placement=hbm,type=four,vary=page-size

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5c8000000000, copy home 0x5c82c0000000, direct level 0x5c8540000000, copy level 0x5c8800000000
- factor effect within the cell: on the direct route -7.3338 [-7.3422, -7.2018] ms, on the copy route 0.0077 [-0.0115, 0.0130] ms; change relative to the copy call at home: -131.8 %
- per repetition: direct home 0 link read bytes and 4.423e+04 SMMU translation requests; copy home 0 link read bytes and 9.135e+04 SMMU translation requests; direct level 0 link read bytes and 7.869 SMMU translation requests; copy level 0 link read bytes and 75.25 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=9728,kernel=k3,placement=cpu,type=four,vary=page-size

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x49d0c0000000, copy home 0x49d3c0000000, direct level 0x49d6c0000000, copy level 0x49d9c0000000
- factor effect within the cell: on the direct route -122.8652 [-122.9290, -122.6545] ms, on the copy route -0.9084 [-0.9345, -0.8871] ms; change relative to the copy call at home: -445.9 %
- per repetition: direct home 5.369e+08 link read bytes and 3.598e+07 SMMU translation requests; copy home 1.02e+10 link read bytes and 1.629e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 96.62 SMMU translation requests; copy level 1.02e+10 link read bytes and 321.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x444700000000, copy home 0x444800000000, direct level 0x4448c0000000, copy level 0x444980000000
- factor effect within the cell: on the direct route -0.0698 [-0.0699, -0.0698] ms, on the copy route -0.0778 [-0.0780, -0.0777] ms; change relative to the copy call at home: +6.1 %
- per repetition: direct home 3.354e+07 link read bytes and 0 SMMU translation requests; copy home 3.354e+07 link read bytes and 533 SMMU translation requests; direct level 8.38e+06 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x521100000000, copy home 0x521200000000, direct level 0x5212c0000000, copy level 0x521380000000
- factor effect within the cell: on the direct route -0.0086 [-0.0086, -0.0086] ms, on the copy route -0.0691 [-0.0694, -0.0688] ms; change relative to the copy call at home: +50.6 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 519.1 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x523a40000000, copy home 0x523b40000000, direct level 0x523c00000000, copy level 0x523cc0000000
- factor effect within the cell: on the direct route -1.4556 [-1.4561, -1.4553] ms, on the copy route -0.1292 [-0.1298, -0.1287] ms; change relative to the copy call at home: -697.5 %
- per repetition: direct home 5.366e+08 link read bytes and 0 SMMU translation requests; copy home 3.354e+07 link read bytes and 533.1 SMMU translation requests; direct level 8.382e+06 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x435b40000000, copy home 0x435c00000000, direct level 0x435cc0000000, copy level 0x435d80000000
- factor effect within the cell: on the direct route -0.0809 [-0.0810, -0.0808] ms, on the copy route -0.1231 [-0.1245, -0.1223] ms; change relative to the copy call at home: +23.3 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 519.9 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x583a40000000, copy home 0x583b00000000, direct level 0x583bc0000000, copy level 0x583c80000000
- factor effect within the cell: on the direct route -0.1612 [-0.1612, -0.1611] ms, on the copy route -0.0816 [-0.0822, -0.0814] ms; change relative to the copy call at home: -58.8 %
- per repetition: direct home 6.708e+07 link read bytes and 0 SMMU translation requests; copy home 3.354e+07 link read bytes and 533 SMMU translation requests; direct level 8.382e+06 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x546800000000, copy home 0x546900000000, direct level 0x5469c0000000, copy level 0x546a80000000
- factor effect within the cell: on the direct route -0.0141 [-0.0141, -0.0141] ms, on the copy route -0.0751 [-0.0758, -0.0748] ms; change relative to the copy call at home: +48.6 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 519.9 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x57f8c0000000, copy home 0x57f980000000, direct level 0x57fa40000000, copy level 0x57fb00000000
- factor effect within the cell: on the direct route -0.3451 [-0.3452, -0.3450] ms, on the copy route -0.0863 [-0.0866, -0.0861] ms; change relative to the copy call at home: -184.0 %
- per repetition: direct home 1.342e+08 link read bytes and 0 SMMU translation requests; copy home 3.354e+07 link read bytes and 533 SMMU translation requests; direct level 8.382e+06 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4c8ec0000000, copy home 0x4c8fc0000000, direct level 0x4c9080000000, copy level 0x4c9140000000
- factor effect within the cell: on the direct route -0.0246 [-0.0246, -0.0246] ms, on the copy route -0.0800 [-0.0804, -0.0794] ms; change relative to the copy call at home: +42.4 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 519.5 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=four,vary=working-set,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x45f140000000, copy home 0x45f200000000, direct level 0x45f2c0000000, copy level 0x45f380000000
- factor effect within the cell: on the direct route -5.9009 [-5.9045, -5.8985] ms, on the copy route -0.3004 [-0.3009, -0.2992] ms; change relative to the copy call at home: -1456.2 %
- per repetition: direct home 2.145e+09 link read bytes and 0 SMMU translation requests; copy home 3.354e+07 link read bytes and 533.2 SMMU translation requests; direct level 8.382e+06 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=four,vary=working-set,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x542ac0000000, copy home 0x542b80000000, direct level 0x542c40000000, copy level 0x542d00000000
- factor effect within the cell: on the direct route -0.3070 [-0.3079, -0.3064] ms, on the copy route -0.2904 [-0.2910, -0.2898] ms; change relative to the copy call at home: -4.5 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 522.4 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=hbm,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=placement

- seed 71; every round ran in the drawn order: yes; floor 1.0568 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement hbm; buffers: direct home 0x5ba700000000, copy home 0x5ba800000000, direct level 0x5ba8c0000000, copy level 0x5ba980000000
- factor effect within the cell: on the direct route -2.6136 [-2.6143, -2.6130] ms, on the copy route -2.3079 [-2.3093, -2.3062] ms; change relative to the copy call at home: -9.4 %
- per repetition: direct home 1.074e+09 link read bytes and 0 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.64e+04 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 0.7273 SMMU translation requests; multiplexed rows voided: 0

### route/at=none,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=tiling

- seed 71; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x50a8c0000000, copy home 0x50a9c0000000, direct level 0x50aac0000000, copy level 0x50ab80000000
- factor effect within the cell: on the direct route 9.4332 [9.1029, 9.6656] ms, on the copy route -0.5068 [-0.5123, -0.5024] ms; change relative to the copy call at home: +153.3 %
- per repetition: direct home 6.422e+09 link read bytes and 3.622e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 1.307e+10 link read bytes and 3.606e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=none,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=tiling

- seed 71; every round ran in the drawn order: yes; floor 0.3714 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x533b80000000, copy home 0x533c80000000, direct level 0x533d80000000, copy level 0x533e40000000
- factor effect within the cell: on the direct route -0.4972 [-0.5044, -0.4866] ms, on the copy route -0.4809 [-0.4868, -0.4734] ms; change relative to the copy call at home: -0.4 %
- per repetition: direct home 0 link read bytes and 5927 SMMU translation requests; copy home 0 link read bytes and 5458 SMMU translation requests; direct level 0 link read bytes and 8832 SMMU translation requests; copy level 0 link read bytes and 5524 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=8192,kernel=k3,placement=cpu,type=four,vary=alignment

- seed 71; every round ran in the drawn order: yes; floor 0.3765 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4d4b40000000, copy home 0x4d4dc0000000, direct level 0x4d5420000000, copy level 0x4d5820000000
- factor effect within the cell: on the direct route 40.6981 [40.6476, 40.7852] ms, on the copy route -0.7056 [-0.7244, -0.6903] ms; change relative to the copy call at home: +175.4 %
- per repetition: direct home 5.369e+08 link read bytes and 4.396e+04 SMMU translation requests; copy home 8.607e+09 link read bytes and 1.311e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.369e+07 SMMU translation requests; copy level 8.607e+09 link read bytes and 1.311e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=1024,kernel=k6,placement=cpu,type=four,update=atomic,vary=update

- seed 71; every round ran in the drawn order: yes; floor 0.2722 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x522ec0000000, copy home 0x522fc0000000, direct level 0x523080000000, copy level 0x523140000000
- factor effect within the cell: on the direct route -0.0829 [-0.0897, -0.0786] ms, on the copy route -0.1722 [-0.1769, -0.1666] ms; change relative to the copy call at home: +1.2 %
- per repetition: direct home 0 link read bytes and 4222 SMMU translation requests; copy home 1.074e+09 link read bytes and 3.278e+04 SMMU translation requests; direct level 1.074e+09 link read bytes and 4558 SMMU translation requests; copy level 1.074e+09 link read bytes and 3.278e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,type=four,vary=generator

- seed 71; every round ran in the drawn order: yes; floor 0.5037 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4b7400000000, copy home 0x4b7540000000, direct level 0x4b7600000000, copy level 0x4b76c0000000
- factor effect within the cell: on the direct route 157.5357 [157.4545, 158.6417] ms, on the copy route 63.5845 [63.0841, 64.1252] ms; change relative to the copy call at home: +2253.8 %
- per repetition: direct home 3.204e+09 link read bytes and 0 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.689e+04 SMMU translation requests; direct level 2.853e+09 link read bytes and 0 SMMU translation requests; copy level 1.074e+09 link read bytes and 1.689e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,type=four,vary=generator

- seed 71; every round ran in the drawn order: yes; floor 0.5037 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x408180000000, copy home 0x408240000000, direct level 0x408300000000, copy level 0x4083c0000000
- factor effect within the cell: on the direct route 63.7218 [63.6656, 64.6621] ms, on the copy route 63.1946 [63.1674, 64.2344] ms; change relative to the copy call at home: +27.9 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 0 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5c2680000000, copy home 0x5c2740000000, direct level 0x5c27c0000000, copy level 0x5c2840000000
- factor effect within the cell: on the direct route 0.0009 [0.0008, 0.0011] ms, on the copy route 0.0019 [0.0015, 0.0024] ms; change relative to the copy call at home: -3.0 %
- per repetition: direct home 5.243e+05 link read bytes and 0.78 SMMU translation requests; copy home 5.243e+05 link read bytes and 0.34 SMMU translation requests; direct level 5.243e+05 link read bytes and 0.78 SMMU translation requests; copy level 5.243e+05 link read bytes and 0.67 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5d3380000000, copy home 0x5d3440000000, direct level 0x5d34c0000000, copy level 0x5d3540000000
- factor effect within the cell: on the direct route 0.0007 [0.0006, 0.0007] ms, on the copy route 0.0014 [0.0011, 0.0017] ms; change relative to the copy call at home: -2.3 %
- per repetition: direct home 5.243e+05 link read bytes and 0.78 SMMU translation requests; copy home 5.243e+05 link read bytes and 0.67 SMMU translation requests; direct level 5.243e+05 link read bytes and 0.78 SMMU translation requests; copy level 5.243e+05 link read bytes and 0.66 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5ff7c0000000, copy home 0x5ff840000000, direct level 0x5ff8c0000000, copy level 0x5ff940000000
- factor effect within the cell: on the direct route -0.0000 [-0.0001, 0.0000] ms, on the copy route -0.0001 [-0.0004, 0.0001] ms; change relative to the copy call at home: +0.2 %
- per repetition: direct home 5.243e+05 link read bytes and 0.78 SMMU translation requests; copy home 5.243e+05 link read bytes and 0.68 SMMU translation requests; direct level 5.243e+05 link read bytes and 0.78 SMMU translation requests; copy level 5.243e+05 link read bytes and 0.67 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4c5600000000, copy home 0x4c5680000000, direct level 0x4c5700000000, copy level 0x4c5780000000
- factor effect within the cell: on the direct route 0.0001 [-0.0000, 0.0001] ms, on the copy route -0.0001 [-0.0007, 0.0003] ms; change relative to the copy call at home: +0.6 %
- per repetition: direct home 0 link read bytes and 39 SMMU translation requests; copy home 0 link read bytes and 39 SMMU translation requests; direct level 0 link read bytes and 39 SMMU translation requests; copy level 0 link read bytes and 39 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x41f680000000, copy home 0x41f740000000, direct level 0x41f7c0000000, copy level 0x41f840000000
- factor effect within the cell: on the direct route 0.0000 [-0.0001, 0.0001] ms, on the copy route 0.0004 [-0.0001, 0.0007] ms; change relative to the copy call at home: -0.6 %
- per repetition: direct home 0 link read bytes and 39 SMMU translation requests; copy home 0 link read bytes and 39 SMMU translation requests; direct level 0 link read bytes and 39 SMMU translation requests; copy level 0 link read bytes and 39 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5b1240000000, copy home 0x5b12c0000000, direct level 0x5b1340000000, copy level 0x5b13c0000000
- factor effect within the cell: on the direct route 0.0000 [-0.0000, 0.0001] ms, on the copy route 0.0002 [-0.0000, 0.0008] ms; change relative to the copy call at home: -0.7 %
- per repetition: direct home 0 link read bytes and 39 SMMU translation requests; copy home 0 link read bytes and 39 SMMU translation requests; direct level 0 link read bytes and 39 SMMU translation requests; copy level 0 link read bytes and 39 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x53dfc0000000, copy home 0x53e080000000, direct level 0x53e140000000, copy level 0x53e200000000
- factor effect within the cell: on the direct route -0.0129 [-0.0136, -0.0102] ms, on the copy route -0.1098 [-0.1122, -0.1075] ms; change relative to the copy call at home: +3.0 %
- per repetition: direct home 1.074e+09 link read bytes and 409.9 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.64e+04 SMMU translation requests; direct level 1.074e+09 link read bytes and 626.2 SMMU translation requests; copy level 1.074e+09 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x508500000000, copy home 0x508600000000, direct level 0x5086c0000000, copy level 0x508780000000
- factor effect within the cell: on the direct route 0.1673 [0.1494, 0.1865] ms, on the copy route 0.0134 [0.0004, 0.0416] ms; change relative to the copy call at home: +4.4 %
- per repetition: direct home 1.074e+09 link read bytes and 416.1 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.64e+04 SMMU translation requests; direct level 1.074e+09 link read bytes and 391.9 SMMU translation requests; copy level 1.074e+09 link read bytes and 1.65e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4c09c0000000, copy home 0x4c0a80000000, direct level 0x4c0b40000000, copy level 0x4c0c00000000
- factor effect within the cell: on the direct route -0.0093 [-0.0098, -0.0086] ms, on the copy route -0.1090 [-0.1097, -0.1081] ms; change relative to the copy call at home: +3.0 %
- per repetition: direct home 1.074e+09 link read bytes and 399.3 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.64e+04 SMMU translation requests; direct level 1.074e+09 link read bytes and 448.5 SMMU translation requests; copy level 1.074e+09 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x42a300000000, copy home 0x42a400000000, direct level 0x42a4c0000000, copy level 0x42a580000000
- factor effect within the cell: on the direct route 0.0027 [0.0017, 0.0038] ms, on the copy route 0.0003 [-0.0005, 0.0014] ms; change relative to the copy call at home: +0.3 %
- per repetition: direct home 0 link read bytes and 5.072e+04 SMMU translation requests; copy home 0 link read bytes and 4.52e+04 SMMU translation requests; direct level 0 link read bytes and 4.973e+04 SMMU translation requests; copy level 0 link read bytes and 4.478e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4d6100000000, copy home 0x4d61c0000000, direct level 0x4d6280000000, copy level 0x4d6340000000
- factor effect within the cell: on the direct route 0.0208 [0.0181, 0.0232] ms, on the copy route -0.0081 [-0.0101, -0.0066] ms; change relative to the copy call at home: +2.6 %
- per repetition: direct home 0 link read bytes and 4.764e+04 SMMU translation requests; copy home 0 link read bytes and 4.976e+04 SMMU translation requests; direct level 0 link read bytes and 5.194e+04 SMMU translation requests; copy level 0 link read bytes and 4.749e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=1024,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5ab100000000, copy home 0x5ab1c0000000, direct level 0x5ab280000000, copy level 0x5ab340000000
- factor effect within the cell: on the direct route 0.0005 [-0.0021, 0.0018] ms, on the copy route 0.0008 [-0.0009, 0.0018] ms; change relative to the copy call at home: +0.0 %
- per repetition: direct home 0 link read bytes and 5.165e+04 SMMU translation requests; copy home 0 link read bytes and 4.501e+04 SMMU translation requests; direct level 0 link read bytes and 4.992e+04 SMMU translation requests; copy level 0 link read bytes and 4.498e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x426740000000, copy home 0x426800000000, direct level 0x426880000000, copy level 0x426900000000
- factor effect within the cell: on the direct route -0.0070 [-0.0082, -0.0054] ms, on the copy route -0.0130 [-0.0140, -0.0119] ms; change relative to the copy call at home: +1.2 %
- per repetition: direct home 1.342e+08 link read bytes and 0 SMMU translation requests; copy home 1.342e+08 link read bytes and 2060 SMMU translation requests; direct level 1.342e+08 link read bytes and 0 SMMU translation requests; copy level 1.342e+08 link read bytes and 2060 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x41a9c0000000, copy home 0x41aa80000000, direct level 0x41ab00000000, copy level 0x41ab80000000
- factor effect within the cell: on the direct route 0.2999 [0.2944, 0.3011] ms, on the copy route 0.2609 [0.2535, 0.2642] ms; change relative to the copy call at home: +8.6 %
- per repetition: direct home 1.342e+08 link read bytes and 88.74 SMMU translation requests; copy home 1.342e+08 link read bytes and 2060 SMMU translation requests; direct level 1.342e+08 link read bytes and 62.14 SMMU translation requests; copy level 1.342e+08 link read bytes and 2061 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4d3e00000000, copy home 0x4d3e80000000, direct level 0x4d3f00000000, copy level 0x4d3f80000000
- factor effect within the cell: on the direct route 0.0013 [0.0009, 0.0016] ms, on the copy route -0.0049 [-0.0053, -0.0034] ms; change relative to the copy call at home: +1.3 %
- per repetition: direct home 1.342e+08 link read bytes and 0 SMMU translation requests; copy home 1.342e+08 link read bytes and 2060 SMMU translation requests; direct level 1.342e+08 link read bytes and 0 SMMU translation requests; copy level 1.342e+08 link read bytes and 2060 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5a0840000000, copy home 0x5a0900000000, direct level 0x5a0980000000, copy level 0x5a0a00000000
- factor effect within the cell: on the direct route 0.1274 [0.1245, 0.1300] ms, on the copy route 0.0839 [0.0822, 0.0858] ms; change relative to the copy call at home: +22.7 %
- per repetition: direct home 0 link read bytes and 6487 SMMU translation requests; copy home 0 link read bytes and 6506 SMMU translation requests; direct level 0 link read bytes and 3704 SMMU translation requests; copy level 0 link read bytes and 3587 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x56c100000000, copy home 0x56c1c0000000, direct level 0x56c240000000, copy level 0x56c2c0000000
- factor effect within the cell: on the direct route 0.2192 [0.2184, 0.2195] ms, on the copy route 0.1506 [0.1499, 0.1537] ms; change relative to the copy call at home: +33.0 %
- per repetition: direct home 0 link read bytes and 7231 SMMU translation requests; copy home 0 link read bytes and 6907 SMMU translation requests; direct level 0 link read bytes and 3472 SMMU translation requests; copy level 0 link read bytes and 3389 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=128,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5c1700000000, copy home 0x5c17c0000000, direct level 0x5c1840000000, copy level 0x5c18c0000000
- factor effect within the cell: on the direct route 0.0004 [0.0001, 0.0008] ms, on the copy route 0.0006 [-0.0004, 0.0013] ms; change relative to the copy call at home: +0.1 %
- per repetition: direct home 0 link read bytes and 6267 SMMU translation requests; copy home 0 link read bytes and 7463 SMMU translation requests; direct level 0 link read bytes and 5917 SMMU translation requests; copy level 0 link read bytes and 7648 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x52e380000000, copy home 0x52e440000000, direct level 0x52e4c0000000, copy level 0x52e540000000
- factor effect within the cell: on the direct route -0.0002 [-0.0003, 0.0000] ms, on the copy route 0.0002 [-0.0002, 0.0004] ms; change relative to the copy call at home: -0.7 %
- per repetition: direct home 2.097e+06 link read bytes and 1.63 SMMU translation requests; copy home 2.097e+06 link read bytes and 1 SMMU translation requests; direct level 2.097e+06 link read bytes and 2 SMMU translation requests; copy level 2.097e+06 link read bytes and 1 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5f9340000000, copy home 0x5f9400000000, direct level 0x5f9480000000, copy level 0x5f9500000000
- factor effect within the cell: on the direct route 0.0023 [0.0020, 0.0023] ms, on the copy route 0.0036 [0.0033, 0.0039] ms; change relative to the copy call at home: -3.1 %
- per repetition: direct home 2.097e+06 link read bytes and 1.64 SMMU translation requests; copy home 2.097e+06 link read bytes and 1 SMMU translation requests; direct level 2.097e+06 link read bytes and 2.01 SMMU translation requests; copy level 2.097e+06 link read bytes and 1.17 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5737c0000000, copy home 0x573840000000, direct level 0x5738c0000000, copy level 0x573940000000
- factor effect within the cell: on the direct route 0.0002 [0.0001, 0.0003] ms, on the copy route 0.0001 [-0.0004, 0.0003] ms; change relative to the copy call at home: +0.5 %
- per repetition: direct home 2.097e+06 link read bytes and 1.48 SMMU translation requests; copy home 2.097e+06 link read bytes and 1 SMMU translation requests; direct level 2.097e+06 link read bytes and 1.73 SMMU translation requests; copy level 2.097e+06 link read bytes and 1 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4d8f00000000, copy home 0x4d8f80000000, direct level 0x4d9000000000, copy level 0x4d9080000000
- factor effect within the cell: on the direct route 0.0003 [0.0002, 0.0003] ms, on the copy route 0.0004 [0.0001, 0.0007] ms; change relative to the copy call at home: -0.3 %
- per repetition: direct home 0 link read bytes and 93.58 SMMU translation requests; copy home 0 link read bytes and 105.3 SMMU translation requests; direct level 0 link read bytes and 88.66 SMMU translation requests; copy level 0 link read bytes and 91.43 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4e13c0000000, copy home 0x4e1480000000, direct level 0x4e1500000000, copy level 0x4e1580000000
- factor effect within the cell: on the direct route 0.0011 [0.0010, 0.0012] ms, on the copy route 0.0009 [0.0007, 0.0014] ms; change relative to the copy call at home: +0.6 %
- per repetition: direct home 0 link read bytes and 94.51 SMMU translation requests; copy home 0 link read bytes and 103.5 SMMU translation requests; direct level 0 link read bytes and 89.31 SMMU translation requests; copy level 0 link read bytes and 90.67 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=2,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x506a40000000, copy home 0x506ac0000000, direct level 0x506b40000000, copy level 0x506bc0000000
- factor effect within the cell: on the direct route 0.0001 [-0.0000, 0.0002] ms, on the copy route 0.0001 [-0.0002, 0.0003] ms; change relative to the copy call at home: +0.2 %
- per repetition: direct home 0 link read bytes and 93.97 SMMU translation requests; copy home 0 link read bytes and 99.04 SMMU translation requests; direct level 0 link read bytes and 82.96 SMMU translation requests; copy level 0 link read bytes and 93.17 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x44d880000000, copy home 0x44d940000000, direct level 0x44da00000000, copy level 0x44da80000000
- factor effect within the cell: on the direct route -0.0073 [-0.0096, -0.0069] ms, on the copy route -0.0304 [-0.0343, -0.0277] ms; change relative to the copy call at home: +2.6 %
- per repetition: direct home 2.684e+08 link read bytes and 75.25 SMMU translation requests; copy home 2.684e+08 link read bytes and 4110 SMMU translation requests; direct level 2.684e+08 link read bytes and 73.82 SMMU translation requests; copy level 2.684e+08 link read bytes and 4110 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x555740000000, copy home 0x555800000000, direct level 0x555880000000, copy level 0x555900000000
- factor effect within the cell: on the direct route 0.1222 [0.1211, 0.1282] ms, on the copy route 0.0792 [0.0755, 0.0898] ms; change relative to the copy call at home: +5.2 %
- per repetition: direct home 2.684e+08 link read bytes and 0 SMMU translation requests; copy home 2.684e+08 link read bytes and 4110 SMMU translation requests; direct level 2.684e+08 link read bytes and 0 SMMU translation requests; copy level 2.684e+08 link read bytes and 4109 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4cf9c0000000, copy home 0x4cfa80000000, direct level 0x4cfb00000000, copy level 0x4cfbc0000000
- factor effect within the cell: on the direct route 0.0022 [0.0015, 0.0028] ms, on the copy route -0.0103 [-0.0105, -0.0099] ms; change relative to the copy call at home: +1.5 %
- per repetition: direct home 2.684e+08 link read bytes and 77.49 SMMU translation requests; copy home 2.684e+08 link read bytes and 4111 SMMU translation requests; direct level 2.684e+08 link read bytes and 67.89 SMMU translation requests; copy level 2.684e+08 link read bytes and 4110 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x57e240000000, copy home 0x57e300000000, direct level 0x57e380000000, copy level 0x57e400000000
- factor effect within the cell: on the direct route 0.0596 [0.0583, 0.0608] ms, on the copy route -0.0139 [-0.0147, -0.0130] ms; change relative to the copy call at home: +9.6 %
- per repetition: direct home 0 link read bytes and 1.285e+04 SMMU translation requests; copy home 0 link read bytes and 4118 SMMU translation requests; direct level 0 link read bytes and 8849 SMMU translation requests; copy level 0 link read bytes and 4120 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x555ac0000000, copy home 0x555b80000000, direct level 0x555c00000000, copy level 0x555c80000000
- factor effect within the cell: on the direct route 0.0863 [0.0850, 0.0872] ms, on the copy route -0.0254 [-0.0279, -0.0238] ms; change relative to the copy call at home: +14.1 %
- per repetition: direct home 0 link read bytes and 1.406e+04 SMMU translation requests; copy home 0 link read bytes and 4115 SMMU translation requests; direct level 0 link read bytes and 1.116e+04 SMMU translation requests; copy level 0 link read bytes and 4118 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=256,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x499000000000, copy home 0x4990c0000000, direct level 0x499140000000, copy level 0x4991c0000000
- factor effect within the cell: on the direct route 0.0019 [0.0016, 0.0023] ms, on the copy route 0.0003 [-0.0005, 0.0011] ms; change relative to the copy call at home: +0.2 %
- per repetition: direct home 0 link read bytes and 1.222e+04 SMMU translation requests; copy home 0 link read bytes and 4117 SMMU translation requests; direct level 0 link read bytes and 1.196e+04 SMMU translation requests; copy level 0 link read bytes and 4115 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x581fc0000000, copy home 0x582080000000, direct level 0x582100000000, copy level 0x582180000000
- factor effect within the cell: on the direct route 0.0013 [0.0010, 0.0015] ms, on the copy route 0.0021 [0.0012, 0.0023] ms; change relative to the copy call at home: -0.4 %
- per repetition: direct home 3.355e+07 link read bytes and 39.16 SMMU translation requests; copy home 3.355e+07 link read bytes and 523.7 SMMU translation requests; direct level 3.355e+07 link read bytes and 26.04 SMMU translation requests; copy level 3.355e+07 link read bytes and 523.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4f5240000000, copy home 0x4f52c0000000, direct level 0x4f5340000000, copy level 0x4f53c0000000
- factor effect within the cell: on the direct route 0.0937 [0.0930, 0.0942] ms, on the copy route 0.0808 [0.0800, 0.0819] ms; change relative to the copy call at home: +9.6 %
- per repetition: direct home 3.355e+07 link read bytes and 53.85 SMMU translation requests; copy home 3.355e+07 link read bytes and 523.7 SMMU translation requests; direct level 3.355e+07 link read bytes and 19.77 SMMU translation requests; copy level 3.355e+07 link read bytes and 524.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4753c0000000, copy home 0x475440000000, direct level 0x4754c0000000, copy level 0x475540000000
- factor effect within the cell: on the direct route 0.0004 [0.0003, 0.0005] ms, on the copy route 0.0010 [0.0002, 0.0016] ms; change relative to the copy call at home: -0.4 %
- per repetition: direct home 3.355e+07 link read bytes and 51.79 SMMU translation requests; copy home 3.355e+07 link read bytes and 524 SMMU translation requests; direct level 3.355e+07 link read bytes and 37.26 SMMU translation requests; copy level 3.355e+07 link read bytes and 523.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x431a40000000, copy home 0x431b00000000, direct level 0x431b80000000, copy level 0x431c00000000
- factor effect within the cell: on the direct route 0.0342 [0.0338, 0.0345] ms, on the copy route 0.0323 [0.0312, 0.0327] ms; change relative to the copy call at home: +3.4 %
- per repetition: direct home 0 link read bytes and 1447 SMMU translation requests; copy home 0 link read bytes and 2008 SMMU translation requests; direct level 0 link read bytes and 1517 SMMU translation requests; copy level 0 link read bytes and 1252 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x472700000000, copy home 0x472780000000, direct level 0x472800000000, copy level 0x472880000000
- factor effect within the cell: on the direct route 0.0703 [0.0701, 0.0706] ms, on the copy route 0.0701 [0.0698, 0.0715] ms; change relative to the copy call at home: -0.0 %
- per repetition: direct home 0 link read bytes and 1584 SMMU translation requests; copy home 0 link read bytes and 1854 SMMU translation requests; direct level 0 link read bytes and 1449 SMMU translation requests; copy level 0 link read bytes and 994.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=32,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5351c0000000, copy home 0x535280000000, direct level 0x535300000000, copy level 0x535380000000
- factor effect within the cell: on the direct route -0.0008 [-0.0009, -0.0006] ms, on the copy route -0.0011 [-0.0019, -0.0003] ms; change relative to the copy call at home: +0.0 %
- per repetition: direct home 0 link read bytes and 1488 SMMU translation requests; copy home 0 link read bytes and 2028 SMMU translation requests; direct level 0 link read bytes and 1477 SMMU translation requests; copy level 0 link read bytes and 1769 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5e80c0000000, copy home 0x5e8180000000, direct level 0x5e8200000000, copy level 0x5e8280000000
- factor effect within the cell: on the direct route -0.0022 [-0.0024, -0.0018] ms, on the copy route 0.0008 [-0.0003, 0.0013] ms; change relative to the copy call at home: -1.1 %
- per repetition: direct home 6.711e+07 link read bytes and 2141 SMMU translation requests; copy home 6.711e+07 link read bytes and 1043 SMMU translation requests; direct level 6.711e+07 link read bytes and 1720 SMMU translation requests; copy level 6.711e+07 link read bytes and 1047 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x459a80000000, copy home 0x459b00000000, direct level 0x459b80000000, copy level 0x459c00000000
- factor effect within the cell: on the direct route 0.1835 [0.1827, 0.1838] ms, on the copy route 0.1694 [0.1681, 0.1703] ms; change relative to the copy call at home: +5.8 %
- per repetition: direct home 6.711e+07 link read bytes and 2229 SMMU translation requests; copy home 6.711e+07 link read bytes and 1043 SMMU translation requests; direct level 6.711e+07 link read bytes and 1689 SMMU translation requests; copy level 6.711e+07 link read bytes and 1070 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4d6000000000, copy home 0x4d60c0000000, direct level 0x4d6140000000, copy level 0x4d61c0000000
- factor effect within the cell: on the direct route 0.0010 [0.0008, 0.0011] ms, on the copy route 0.0004 [-0.0006, 0.0015] ms; change relative to the copy call at home: +0.3 %
- per repetition: direct home 6.711e+07 link read bytes and 44.66 SMMU translation requests; copy home 6.711e+07 link read bytes and 1036 SMMU translation requests; direct level 6.711e+07 link read bytes and 46.33 SMMU translation requests; copy level 6.711e+07 link read bytes and 1036 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4f9280000000, copy home 0x4f9340000000, direct level 0x4f93c0000000, copy level 0x4f9440000000
- factor effect within the cell: on the direct route 0.1350 [0.1348, 0.1371] ms, on the copy route 0.1274 [0.1271, 0.1276] ms; change relative to the copy call at home: +8.6 %
- per repetition: direct home 0 link read bytes and 2916 SMMU translation requests; copy home 0 link read bytes and 3889 SMMU translation requests; direct level 0 link read bytes and 2011 SMMU translation requests; copy level 0 link read bytes and 1533 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x49ee00000000, copy home 0x49ee80000000, direct level 0x49ef00000000, copy level 0x49efc0000000
- factor effect within the cell: on the direct route 0.1492 [0.1485, 0.1500] ms, on the copy route 0.1436 [0.1432, 0.1444] ms; change relative to the copy call at home: +5.7 %
- per repetition: direct home 0 link read bytes and 2933 SMMU translation requests; copy home 0 link read bytes and 3847 SMMU translation requests; direct level 0 link read bytes and 2108 SMMU translation requests; copy level 0 link read bytes and 1609 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x484800000000, copy home 0x4848c0000000, direct level 0x484940000000, copy level 0x4849c0000000
- factor effect within the cell: on the direct route -0.0019 [-0.0020, -0.0016] ms, on the copy route 0.0004 [0.0002, 0.0008] ms; change relative to the copy call at home: -2.5 %
- per repetition: direct home 0 link read bytes and 2909 SMMU translation requests; copy home 0 link read bytes and 3887 SMMU translation requests; direct level 0 link read bytes and 2868 SMMU translation requests; copy level 0 link read bytes and 3909 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x410c80000000, copy home 0x410d00000000, direct level 0x410d80000000, copy level 0x410e00000000
- factor effect within the cell: on the direct route -0.0005 [-0.0007, -0.0003] ms, on the copy route 0.0002 [-0.0003, 0.0005] ms; change relative to the copy call at home: -1.0 %
- per repetition: direct home 8.389e+06 link read bytes and 7.3 SMMU translation requests; copy home 8.389e+06 link read bytes and 5.87 SMMU translation requests; direct level 8.389e+06 link read bytes and 8.09 SMMU translation requests; copy level 8.389e+06 link read bytes and 2.95 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4929c0000000, copy home 0x492a40000000, direct level 0x492ac0000000, copy level 0x492b40000000
- factor effect within the cell: on the direct route 0.0195 [0.0194, 0.0197] ms, on the copy route 0.0190 [0.0188, 0.0198] ms; change relative to the copy call at home: +0.9 %
- per repetition: direct home 8.389e+06 link read bytes and 7.6 SMMU translation requests; copy home 8.389e+06 link read bytes and 2.94 SMMU translation requests; direct level 8.389e+06 link read bytes and 4.43 SMMU translation requests; copy level 8.389e+06 link read bytes and 2.94 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5cd680000000, copy home 0x5cd740000000, direct level 0x5cd7c0000000, copy level 0x5cd840000000
- factor effect within the cell: on the direct route 0.0002 [-0.0000, 0.0004] ms, on the copy route 0.0006 [0.0000, 0.0009] ms; change relative to the copy call at home: -0.4 %
- per repetition: direct home 8.389e+06 link read bytes and 8.6 SMMU translation requests; copy home 8.389e+06 link read bytes and 2.94 SMMU translation requests; direct level 8.389e+06 link read bytes and 7.68 SMMU translation requests; copy level 8.389e+06 link read bytes and 2.94 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5ee1c0000000, copy home 0x5ee280000000, direct level 0x5ee300000000, copy level 0x5ee380000000
- factor effect within the cell: on the direct route 0.0083 [0.0082, 0.0084] ms, on the copy route 0.0142 [0.0140, 0.0147] ms; change relative to the copy call at home: -18.5 %
- per repetition: direct home 0 link read bytes and 421.8 SMMU translation requests; copy home 0 link read bytes and 425.6 SMMU translation requests; direct level 0 link read bytes and 383.1 SMMU translation requests; copy level 0 link read bytes and 364.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x599480000000, copy home 0x599500000000, direct level 0x599580000000, copy level 0x599600000000
- factor effect within the cell: on the direct route 0.0149 [0.0149, 0.0150] ms, on the copy route 0.0188 [0.0185, 0.0195] ms; change relative to the copy call at home: -12.5 %
- per repetition: direct home 0 link read bytes and 408.9 SMMU translation requests; copy home 0 link read bytes and 439.3 SMMU translation requests; direct level 0 link read bytes and 408.2 SMMU translation requests; copy level 0 link read bytes and 386.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x504b00000000, copy home 0x504bc0000000, direct level 0x504c40000000, copy level 0x504cc0000000
- factor effect within the cell: on the direct route 0.0003 [0.0002, 0.0004] ms, on the copy route -0.0000 [-0.0003, 0.0005] ms; change relative to the copy call at home: +1.1 %
- per repetition: direct home 0 link read bytes and 414.1 SMMU translation requests; copy home 0 link read bytes and 437.8 SMMU translation requests; direct level 0 link read bytes and 369.6 SMMU translation requests; copy level 0 link read bytes and 376.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x533600000000, copy home 0x5336c0000000, direct level 0x533740000000, copy level 0x5337c0000000
- factor effect within the cell: on the direct route -0.0043 [-0.0047, -0.0030] ms, on the copy route -0.0039 [-0.0051, -0.0016] ms; change relative to the copy call at home: -0.2 %
- per repetition: direct home 1.007e+08 link read bytes and 0 SMMU translation requests; copy home 1.007e+08 link read bytes and 1564 SMMU translation requests; direct level 1.007e+08 link read bytes and 0 SMMU translation requests; copy level 1.007e+08 link read bytes and 1564 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x550d00000000, copy home 0x550dc0000000, direct level 0x550e40000000, copy level 0x550ec0000000
- factor effect within the cell: on the direct route 0.2613 [0.2565, 0.2654] ms, on the copy route 0.2317 [0.2297, 0.2341] ms; change relative to the copy call at home: +8.2 %
- per repetition: direct home 1.007e+08 link read bytes and 68.95 SMMU translation requests; copy home 1.007e+08 link read bytes and 1564 SMMU translation requests; direct level 1.007e+08 link read bytes and 47.35 SMMU translation requests; copy level 1.007e+08 link read bytes and 1565 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x491c00000000, copy home 0x491cc0000000, direct level 0x491d40000000, copy level 0x491dc0000000
- factor effect within the cell: on the direct route -0.0017 [-0.0022, -0.0014] ms, on the copy route -0.0027 [-0.0032, -0.0024] ms; change relative to the copy call at home: +0.3 %
- per repetition: direct home 1.007e+08 link read bytes and 64.67 SMMU translation requests; copy home 1.007e+08 link read bytes and 1564 SMMU translation requests; direct level 1.007e+08 link read bytes and 68.15 SMMU translation requests; copy level 1.007e+08 link read bytes and 1564 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x516c40000000, copy home 0x516d00000000, direct level 0x516d80000000, copy level 0x516e00000000
- factor effect within the cell: on the direct route 0.1324 [0.1311, 0.1333] ms, on the copy route 0.0999 [0.0988, 0.1019] ms; change relative to the copy call at home: +23.1 %
- per repetition: direct home 0 link read bytes and 4626 SMMU translation requests; copy home 0 link read bytes and 5326 SMMU translation requests; direct level 0 link read bytes and 2937 SMMU translation requests; copy level 0 link read bytes and 2855 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5bc6c0000000, copy home 0x5bc780000000, direct level 0x5bc800000000, copy level 0x5bc880000000
- factor effect within the cell: on the direct route 0.2004 [0.2001, 0.2006] ms, on the copy route 0.1635 [0.1628, 0.1647] ms; change relative to the copy call at home: +25.8 %
- per repetition: direct home 0 link read bytes and 4941 SMMU translation requests; copy home 0 link read bytes and 5534 SMMU translation requests; direct level 0 link read bytes and 2790 SMMU translation requests; copy level 0 link read bytes and 2665 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5cdfc0000000, copy home 0x5ce080000000, direct level 0x5ce100000000, copy level 0x5ce180000000
- factor effect within the cell: on the direct route -0.0001 [-0.0006, 0.0002] ms, on the copy route 0.0009 [0.0005, 0.0029] ms; change relative to the copy call at home: -0.9 %
- per repetition: direct home 0 link read bytes and 4618 SMMU translation requests; copy home 0 link read bytes and 5606 SMMU translation requests; direct level 0 link read bytes and 4319 SMMU translation requests; copy level 0 link read bytes and 5680 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x58b040000000, copy home 0x58b1c0000000, direct level 0x58b280000000, copy level 0x58b340000000
- factor effect within the cell: on the direct route -1.1502 [-1.1565, -1.1448] ms, on the copy route -0.6457 [-0.6735, -0.6183] ms; change relative to the copy call at home: -10.5 %
- per repetition: direct home 3.197e+09 link read bytes and 0 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.689e+04 SMMU translation requests; direct level 3.194e+09 link read bytes and 0 SMMU translation requests; copy level 1.074e+09 link read bytes and 1.689e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x57ea80000000, copy home 0x57eb40000000, direct level 0x57ec00000000, copy level 0x57ed00000000
- factor effect within the cell: on the direct route -0.0011 [-0.0059, 0.0022] ms, on the copy route 0.0058 [0.0027, 0.0090] ms; change relative to the copy call at home: -0.4 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 0 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=1,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4e1580000000, copy home 0x4e1680000000, direct level 0x4e1740000000, copy level 0x4e1800000000
- factor effect within the cell: on the direct route -0.0011 [-0.0012, -0.0008] ms, on the copy route -0.0016 [-0.0019, -0.0008] ms; change relative to the copy call at home: +0.9 %
- per repetition: direct home 8.38e+06 link read bytes and 320.4 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.38e+06 link read bytes and 319.5 SMMU translation requests; copy level 8.38e+06 link read bytes and 131 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=1,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4b4040000000, copy home 0x4b4140000000, direct level 0x4b4200000000, copy level 0x4b42c0000000
- factor effect within the cell: on the direct route 0.0170 [0.0167, 0.0173] ms, on the copy route 0.0170 [0.0161, 0.0175] ms; change relative to the copy call at home: +0.2 %
- per repetition: direct home 8.38e+06 link read bytes and 316.5 SMMU translation requests; copy home 8.38e+06 link read bytes and 131 SMMU translation requests; direct level 8.38e+06 link read bytes and 308.2 SMMU translation requests; copy level 8.38e+06 link read bytes and 144.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=1,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5f9f80000000, copy home 0x5fa080000000, direct level 0x5fa140000000, copy level 0x5fa200000000
- factor effect within the cell: on the direct route -0.0003 [-0.0005, -0.0001] ms, on the copy route -0.0002 [-0.0007, 0.0001] ms; change relative to the copy call at home: +0.1 %
- per repetition: direct home 8.38e+06 link read bytes and 330.3 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.38e+06 link read bytes and 330.2 SMMU translation requests; copy level 8.38e+06 link read bytes and 130.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4b9c40000000, copy home 0x4b9d00000000, direct level 0x4b9dc0000000, copy level 0x4b9e80000000
- factor effect within the cell: on the direct route -0.0008 [-0.0010, -0.0007] ms, on the copy route -0.0015 [-0.0018, -0.0007] ms; change relative to the copy call at home: +0.9 %
- per repetition: direct home 8.382e+06 link read bytes and 324.1 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 327 SMMU translation requests; copy level 8.38e+06 link read bytes and 131.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x403280000000, copy home 0x403380000000, direct level 0x403440000000, copy level 0x403500000000
- factor effect within the cell: on the direct route 0.0160 [0.0156, 0.0164] ms, on the copy route 0.0154 [0.0147, 0.0161] ms; change relative to the copy call at home: +1.1 %
- per repetition: direct home 8.382e+06 link read bytes and 315.5 SMMU translation requests; copy home 8.38e+06 link read bytes and 131 SMMU translation requests; direct level 8.382e+06 link read bytes and 310.1 SMMU translation requests; copy level 8.38e+06 link read bytes and 147.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x416500000000, copy home 0x416640000000, direct level 0x416700000000, copy level 0x4167c0000000
- factor effect within the cell: on the direct route -0.0001 [-0.0004, -0.0000] ms, on the copy route -0.0001 [-0.0004, 0.0000] ms; change relative to the copy call at home: -0.1 %
- per repetition: direct home 8.382e+06 link read bytes and 321.5 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 322.5 SMMU translation requests; copy level 8.38e+06 link read bytes and 131 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=2,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5ea6c0000000, copy home 0x5ea7c0000000, direct level 0x5ea880000000, copy level 0x5ea940000000
- factor effect within the cell: on the direct route -0.0008 [-0.0009, -0.0008] ms, on the copy route -0.0012 [-0.0016, -0.0008] ms; change relative to the copy call at home: +0.9 %
- per repetition: direct home 8.382e+06 link read bytes and 318.6 SMMU translation requests; copy home 8.38e+06 link read bytes and 131 SMMU translation requests; direct level 8.382e+06 link read bytes and 319.5 SMMU translation requests; copy level 8.38e+06 link read bytes and 131 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=2,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x560080000000, copy home 0x560140000000, direct level 0x560200000000, copy level 0x5602c0000000
- factor effect within the cell: on the direct route 0.0176 [0.0173, 0.0179] ms, on the copy route 0.0169 [0.0159, 0.0179] ms; change relative to the copy call at home: +1.1 %
- per repetition: direct home 8.382e+06 link read bytes and 302 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 293.3 SMMU translation requests; copy level 8.38e+06 link read bytes and 143.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=2,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5840c0000000, copy home 0x5841c0000000, direct level 0x584280000000, copy level 0x584340000000
- factor effect within the cell: on the direct route -0.0002 [-0.0003, -0.0001] ms, on the copy route -0.0003 [-0.0008, 0.0001] ms; change relative to the copy call at home: +0.2 %
- per repetition: direct home 8.382e+06 link read bytes and 299.9 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 302 SMMU translation requests; copy level 8.38e+06 link read bytes and 130.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=4,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x54c040000000, copy home 0x54c100000000, direct level 0x54c1c0000000, copy level 0x54c280000000
- factor effect within the cell: on the direct route -0.0008 [-0.0010, -0.0005] ms, on the copy route -0.0012 [-0.0015, -0.0006] ms; change relative to the copy call at home: +0.7 %
- per repetition: direct home 8.382e+06 link read bytes and 321.1 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 317.4 SMMU translation requests; copy level 8.38e+06 link read bytes and 130.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=4,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5f6ac0000000, copy home 0x5f6bc0000000, direct level 0x5f6c80000000, copy level 0x5f6d40000000
- factor effect within the cell: on the direct route 0.0186 [0.0185, 0.0192] ms, on the copy route 0.0180 [0.0179, 0.0184] ms; change relative to the copy call at home: +1.2 %
- per repetition: direct home 8.382e+06 link read bytes and 315.6 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 305.8 SMMU translation requests; copy level 8.38e+06 link read bytes and 141.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=4,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x42cf80000000, copy home 0x42d040000000, direct level 0x42d100000000, copy level 0x42d1c0000000
- factor effect within the cell: on the direct route -0.0002 [-0.0003, -0.0001] ms, on the copy route -0.0005 [-0.0009, -0.0001] ms; change relative to the copy call at home: +0.6 %
- per repetition: direct home 8.382e+06 link read bytes and 318.3 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 321.9 SMMU translation requests; copy level 8.38e+06 link read bytes and 130.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=64,kernel=k2,pattern=word,placement=cpu,state=clean,type=four,vary=sharing,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4e0940000000, copy home 0x4e0a40000000, direct level 0x4e0b00000000, copy level 0x4e0bc0000000
- factor effect within the cell: on the direct route -0.0010 [-0.0013, -0.0007] ms, on the copy route -0.0013 [-0.0015, -0.0006] ms; change relative to the copy call at home: +0.1 %
- per repetition: direct home 8.382e+06 link read bytes and 320.7 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 323.6 SMMU translation requests; copy level 8.38e+06 link read bytes and 130.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=64,kernel=k2,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x48ccc0000000, copy home 0x48cdc0000000, direct level 0x48ce80000000, copy level 0x48cf40000000
- factor effect within the cell: on the direct route 0.0200 [0.0192, 0.0203] ms, on the copy route 0.0184 [0.0176, 0.0188] ms; change relative to the copy call at home: +1.6 %
- per repetition: direct home 8.382e+06 link read bytes and 298.1 SMMU translation requests; copy home 8.38e+06 link read bytes and 131 SMMU translation requests; direct level 8.382e+06 link read bytes and 290.8 SMMU translation requests; copy level 8.38e+06 link read bytes and 139.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=64,kernel=k2,pattern=word,placement=cpu,state=evicted,type=four,vary=sharing,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4a7b40000000, copy home 0x4a7c40000000, direct level 0x4a7d00000000, copy level 0x4a7dc0000000
- factor effect within the cell: on the direct route -0.0001 [-0.0003, 0.0000] ms, on the copy route -0.0002 [-0.0007, 0.0004] ms; change relative to the copy call at home: +0.1 %
- per repetition: direct home 8.382e+06 link read bytes and 318 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 318 SMMU translation requests; copy level 8.38e+06 link read bytes and 130.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x419340000000, copy home 0x419400000000, direct level 0x4194c0000000, copy level 0x419580000000
- factor effect within the cell: on the direct route 0.0003 [-0.0003, 0.0007] ms, on the copy route 0.5755 [0.5753, 0.5759] ms; change relative to the copy call at home: -1413.9 %
- per repetition: direct home 3.354e+07 link read bytes and 835.5 SMMU translation requests; copy home 0 link read bytes and 14.72 SMMU translation requests; direct level 3.354e+07 link read bytes and 826.5 SMMU translation requests; copy level 1.074e+08 link read bytes and 2.311e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x499940000000, copy home 0x499a00000000, direct level 0x499ac0000000, copy level 0x499b80000000
- factor effect within the cell: on the direct route -0.0009 [-0.0013, -0.0002] ms, on the copy route 0.5705 [0.5704, 0.5717] ms; change relative to the copy call at home: -1458.8 %
- per repetition: direct home 8.38e+06 link read bytes and 329.5 SMMU translation requests; copy home 0 link read bytes and 14.72 SMMU translation requests; direct level 8.38e+06 link read bytes and 330.9 SMMU translation requests; copy level 1.074e+08 link read bytes and 2.149e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x50d1c0000000, copy home 0x50d2c0000000, direct level 0x50d380000000, copy level 0x50d440000000
- factor effect within the cell: on the direct route 0.0027 [0.0024, 0.0033] ms, on the copy route -0.0020 [-0.0028, -0.0011] ms; change relative to the copy call at home: +3.6 %
- per repetition: direct home 3.354e+07 link read bytes and 0 SMMU translation requests; copy home 3.354e+07 link read bytes and 533.1 SMMU translation requests; direct level 3.354e+07 link read bytes and 0 SMMU translation requests; copy level 3.354e+07 link read bytes and 533.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x429c80000000, copy home 0x429d80000000, direct level 0x429e40000000, copy level 0x429f00000000
- factor effect within the cell: on the direct route 0.0009 [0.0003, 0.0016] ms, on the copy route 0.0011 [0.0001, 0.0015] ms; change relative to the copy call at home: +0.4 %
- per repetition: direct home 8.38e+06 link read bytes and 326.2 SMMU translation requests; copy home 8.38e+06 link read bytes and 131 SMMU translation requests; direct level 8.38e+06 link read bytes and 325.8 SMMU translation requests; copy level 8.38e+06 link read bytes and 131.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5b3140000000, copy home 0x5b3200000000, direct level 0x5b32c0000000, copy level 0x5b3380000000
- factor effect within the cell: on the direct route 0.0004 [0.0003, 0.0005] ms, on the copy route 0.1626 [0.1607, 0.1655] ms; change relative to the copy call at home: -383.3 %
- per repetition: direct home 0 link read bytes and 946.5 SMMU translation requests; copy home 0 link read bytes and 16 SMMU translation requests; direct level 0 link read bytes and 947.7 SMMU translation requests; copy level 0 link read bytes and 3.666e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=1,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x4fb5c0000000, copy home 0x4fb6c0000000, direct level 0x4fb780000000, copy level 0x4fb840000000
- factor effect within the cell: on the direct route 0.0038 [0.0033, 0.0042] ms, on the copy route -0.0660 [-0.1582, 0.0231] ms; change relative to the copy call at home: +12.1 %
- per repetition: direct home 0 link read bytes and 959 SMMU translation requests; copy home 0 link read bytes and 549.1 SMMU translation requests; direct level 0 link read bytes and 959.4 SMMU translation requests; copy level 0 link read bytes and 552.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4b1a00000000, copy home 0x4b1b00000000, direct level 0x4b1bc0000000, copy level 0x4b1c80000000
- factor effect within the cell: on the direct route -0.0332 [-0.0342, -0.0306] ms, on the copy route 0.5788 [0.5783, 0.5803] ms; change relative to the copy call at home: -615.6 %
- per repetition: direct home 5.365e+08 link read bytes and 788.3 SMMU translation requests; copy home 0 link read bytes and 14.4 SMMU translation requests; direct level 5.366e+08 link read bytes and 765.1 SMMU translation requests; copy level 1.074e+08 link read bytes and 2.229e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x484100000000, copy home 0x484200000000, direct level 0x4842c0000000, copy level 0x484380000000
- factor effect within the cell: on the direct route -0.0002 [-0.0007, 0.0002] ms, on the copy route 0.5677 [0.5671, 0.5682] ms; change relative to the copy call at home: -1297.0 %
- per repetition: direct home 8.382e+06 link read bytes and 329.7 SMMU translation requests; copy home 0 link read bytes and 14.56 SMMU translation requests; direct level 8.382e+06 link read bytes and 331.2 SMMU translation requests; copy level 1.074e+08 link read bytes and 2.219e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x45a400000000, copy home 0x45a500000000, direct level 0x45a5c0000000, copy level 0x45a680000000
- factor effect within the cell: on the direct route 0.0033 [0.0016, 0.0068] ms, on the copy route 0.6502 [0.6494, 0.6512] ms; change relative to the copy call at home: -665.7 %
- per repetition: direct home 5.365e+08 link read bytes and 754.7 SMMU translation requests; copy home 0 link read bytes and 12.48 SMMU translation requests; direct level 5.365e+08 link read bytes and 700.2 SMMU translation requests; copy level 1.074e+08 link read bytes and 5.095e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x462140000000, copy home 0x462240000000, direct level 0x462300000000, copy level 0x4623c0000000
- factor effect within the cell: on the direct route -0.0000 [-0.0004, 0.0003] ms, on the copy route 0.6475 [0.6469, 0.6484] ms; change relative to the copy call at home: -1480.2 %
- per repetition: direct home 8.382e+06 link read bytes and 333.6 SMMU translation requests; copy home 0 link read bytes and 14.72 SMMU translation requests; direct level 8.382e+06 link read bytes and 331.8 SMMU translation requests; copy level 1.074e+08 link read bytes and 5.027e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5e2040000000, copy home 0x5e2140000000, direct level 0x5e2200000000, copy level 0x5e22c0000000
- factor effect within the cell: on the direct route 0.0023 [0.0018, 0.0031] ms, on the copy route -0.0047 [-0.0054, -0.0037] ms; change relative to the copy call at home: +3.4 %
- per repetition: direct home 5.365e+08 link read bytes and 59.71 SMMU translation requests; copy home 3.354e+07 link read bytes and 533.2 SMMU translation requests; direct level 5.366e+08 link read bytes and 62 SMMU translation requests; copy level 3.354e+07 link read bytes and 532.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x47eec0000000, copy home 0x47efc0000000, direct level 0x47f080000000, copy level 0x47f140000000
- factor effect within the cell: on the direct route 0.0006 [0.0002, 0.0013] ms, on the copy route 0.0005 [-0.0001, 0.0009] ms; change relative to the copy call at home: +0.4 %
- per repetition: direct home 8.382e+06 link read bytes and 308.3 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 315.8 SMMU translation requests; copy level 8.38e+06 link read bytes and 131.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x404380000000, copy home 0x404440000000, direct level 0x404500000000, copy level 0x4045c0000000
- factor effect within the cell: on the direct route 0.0012 [0.0008, 0.0016] ms, on the copy route 0.1711 [0.1704, 0.1725] ms; change relative to the copy call at home: -152.3 %
- per repetition: direct home 0 link read bytes and 950.5 SMMU translation requests; copy home 0 link read bytes and 16 SMMU translation requests; direct level 0 link read bytes and 951.8 SMMU translation requests; copy level 0 link read bytes and 3.988e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5b6940000000, copy home 0x5b6a80000000, direct level 0x5b6b40000000, copy level 0x5b6c00000000
- factor effect within the cell: on the direct route 0.0013 [0.0003, 0.0020] ms, on the copy route 0.6221 [0.6202, 0.6236] ms; change relative to the copy call at home: -559.5 %
- per repetition: direct home 0 link read bytes and 955.9 SMMU translation requests; copy home 0 link read bytes and 16 SMMU translation requests; direct level 0 link read bytes and 954 SMMU translation requests; copy level 0 link read bytes and 4.8e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5cc300000000, copy home 0x5cc400000000, direct level 0x5cc4c0000000, copy level 0x5cc580000000
- factor effect within the cell: on the direct route 0.0001 [-0.0018, 0.0014] ms, on the copy route -0.0006 [-0.0016, 0.0001] ms; change relative to the copy call at home: +0.6 %
- per repetition: direct home 0 link read bytes and 948.5 SMMU translation requests; copy home 0 link read bytes and 549.2 SMMU translation requests; direct level 0 link read bytes and 943.3 SMMU translation requests; copy level 0 link read bytes and 549.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5e24c0000000, copy home 0x5e25c0000000, direct level 0x5e2680000000, copy level 0x5e2740000000
- factor effect within the cell: on the direct route -0.0002 [-0.0005, 0.0007] ms, on the copy route 0.5821 [0.5818, 0.5825] ms; change relative to the copy call at home: -1448.4 %
- per repetition: direct home 6.708e+07 link read bytes and 862.6 SMMU translation requests; copy home 0 link read bytes and 15.04 SMMU translation requests; direct level 6.708e+07 link read bytes and 875.7 SMMU translation requests; copy level 1.074e+08 link read bytes and 2.336e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x435e80000000, copy home 0x435f40000000, direct level 0x436000000000, copy level 0x4360c0000000
- factor effect within the cell: on the direct route -0.0017 [-0.0019, -0.0011] ms, on the copy route 0.5628 [0.5623, 0.5634] ms; change relative to the copy call at home: -1440.4 %
- per repetition: direct home 8.382e+06 link read bytes and 329.4 SMMU translation requests; copy home 0 link read bytes and 14.08 SMMU translation requests; direct level 8.382e+06 link read bytes and 329 SMMU translation requests; copy level 1.074e+08 link read bytes and 2.073e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x469200000000, copy home 0x469300000000, direct level 0x4693c0000000, copy level 0x469480000000
- factor effect within the cell: on the direct route 0.0031 [0.0028, 0.0039] ms, on the copy route -0.0061 [-0.0076, -0.0049] ms; change relative to the copy call at home: +6.3 %
- per repetition: direct home 6.708e+07 link read bytes and 17.18 SMMU translation requests; copy home 3.354e+07 link read bytes and 533.2 SMMU translation requests; direct level 6.708e+07 link read bytes and 16.68 SMMU translation requests; copy level 3.354e+07 link read bytes and 533.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x442100000000, copy home 0x442200000000, direct level 0x4422c0000000, copy level 0x442380000000
- factor effect within the cell: on the direct route 0.0003 [0.0000, 0.0011] ms, on the copy route -0.0002 [-0.0006, 0.0004] ms; change relative to the copy call at home: +0.8 %
- per repetition: direct home 8.382e+06 link read bytes and 299.5 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 300.7 SMMU translation requests; copy level 8.38e+06 link read bytes and 131.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4c9fc0000000, copy home 0x4ca100000000, direct level 0x4ca1c0000000, copy level 0x4ca280000000
- factor effect within the cell: on the direct route -0.0002 [-0.0005, -0.0001] ms, on the copy route 0.1596 [0.1574, 0.1611] ms; change relative to the copy call at home: -291.3 %
- per repetition: direct home 0 link read bytes and 950.8 SMMU translation requests; copy home 0 link read bytes and 16 SMMU translation requests; direct level 0 link read bytes and 954.2 SMMU translation requests; copy level 0 link read bytes and 3.805e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=2,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x43d4c0000000, copy home 0x43d5c0000000, direct level 0x43d680000000, copy level 0x43d740000000
- factor effect within the cell: on the direct route 0.0020 [0.0018, 0.0023] ms, on the copy route -0.1127 [-0.2054, -0.0484] ms; change relative to the copy call at home: +16.5 %
- per repetition: direct home 0 link read bytes and 943.2 SMMU translation requests; copy home 0 link read bytes and 551.7 SMMU translation requests; direct level 0 link read bytes and 943 SMMU translation requests; copy level 0 link read bytes and 549.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x56efc0000000, copy home 0x56f0c0000000, direct level 0x56f180000000, copy level 0x56f240000000
- factor effect within the cell: on the direct route -0.0006 [-0.0009, 0.0007] ms, on the copy route 0.5808 [0.5804, 0.5816] ms; change relative to the copy call at home: -1182.0 %
- per repetition: direct home 1.342e+08 link read bytes and 861.3 SMMU translation requests; copy home 0 link read bytes and 14.88 SMMU translation requests; direct level 1.342e+08 link read bytes and 836.5 SMMU translation requests; copy level 1.074e+08 link read bytes and 2.184e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x54e140000000, copy home 0x54e200000000, direct level 0x54e2c0000000, copy level 0x54e380000000
- factor effect within the cell: on the direct route -0.0003 [-0.0011, 0.0003] ms, on the copy route 0.5660 [0.5654, 0.5666] ms; change relative to the copy call at home: -1414.0 %
- per repetition: direct home 8.382e+06 link read bytes and 329.2 SMMU translation requests; copy home 0 link read bytes and 14.72 SMMU translation requests; direct level 8.382e+06 link read bytes and 329.2 SMMU translation requests; copy level 1.074e+08 link read bytes and 2.187e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5c4780000000, copy home 0x5c4840000000, direct level 0x5c4900000000, copy level 0x5c49c0000000
- factor effect within the cell: on the direct route 0.0049 [0.0040, 0.0056] ms, on the copy route -0.0068 [-0.0082, -0.0062] ms; change relative to the copy call at home: +7.5 %
- per repetition: direct home 1.342e+08 link read bytes and 18.73 SMMU translation requests; copy home 3.354e+07 link read bytes and 533.2 SMMU translation requests; direct level 1.342e+08 link read bytes and 16.69 SMMU translation requests; copy level 3.354e+07 link read bytes and 533.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4eba00000000, copy home 0x4ebb00000000, direct level 0x4ebbc0000000, copy level 0x4ebc80000000
- factor effect within the cell: on the direct route 0.0009 [0.0003, 0.0016] ms, on the copy route 0.0003 [-0.0001, 0.0007] ms; change relative to the copy call at home: +1.3 %
- per repetition: direct home 8.382e+06 link read bytes and 299.5 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 301.4 SMMU translation requests; copy level 8.38e+06 link read bytes and 131.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x5bf480000000, copy home 0x5bf540000000, direct level 0x5bf600000000, copy level 0x5bf6c0000000
- factor effect within the cell: on the direct route -0.0002 [-0.0003, -0.0001] ms, on the copy route 0.1565 [0.1540, 0.1583] ms; change relative to the copy call at home: -250.8 %
- per repetition: direct home 0 link read bytes and 942.1 SMMU translation requests; copy home 0 link read bytes and 16 SMMU translation requests; direct level 0 link read bytes and 945 SMMU translation requests; copy level 0 link read bytes and 3.699e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=4,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x580380000000, copy home 0x580440000000, direct level 0x580500000000, copy level 0x5805c0000000
- factor effect within the cell: on the direct route 0.0021 [0.0018, 0.0025] ms, on the copy route -0.3882 [-0.4788, -0.2875] ms; change relative to the copy call at home: +36.4 %
- per repetition: direct home 0 link read bytes and 950.9 SMMU translation requests; copy home 0 link read bytes and 550.2 SMMU translation requests; direct level 0 link read bytes and 955.3 SMMU translation requests; copy level 0 link read bytes and 552.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4b17c0000000, copy home 0x4b1900000000, direct level 0x4b19c0000000, copy level 0x4b1a80000000
- factor effect within the cell: on the direct route -0.0185 [-0.0228, -0.0137] ms, on the copy route 0.5800 [0.5779, 0.5846] ms; change relative to the copy call at home: -203.5 %
- per repetition: direct home 2.145e+09 link read bytes and 923.8 SMMU translation requests; copy home 0 link read bytes and 12.96 SMMU translation requests; direct level 2.146e+09 link read bytes and 915.1 SMMU translation requests; copy level 1.074e+08 link read bytes and 1.875e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5365c0000000, copy home 0x536680000000, direct level 0x536740000000, copy level 0x536800000000
- factor effect within the cell: on the direct route -0.0004 [-0.0011, 0.0000] ms, on the copy route 0.5703 [0.5700, 0.5707] ms; change relative to the copy call at home: -865.8 %
- per repetition: direct home 8.382e+06 link read bytes and 327.9 SMMU translation requests; copy home 0 link read bytes and 14.72 SMMU translation requests; direct level 8.382e+06 link read bytes and 327.6 SMMU translation requests; copy level 1.074e+08 link read bytes and 2.224e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x435540000000, copy home 0x435640000000, direct level 0x435700000000, copy level 0x4357c0000000
- factor effect within the cell: on the direct route 0.0148 [0.0111, 0.0180] ms, on the copy route -0.0072 [-0.0085, -0.0063] ms; change relative to the copy call at home: +5.5 %
- per repetition: direct home 2.145e+09 link read bytes and 0 SMMU translation requests; copy home 3.354e+07 link read bytes and 532.9 SMMU translation requests; direct level 2.145e+09 link read bytes and 0 SMMU translation requests; copy level 3.354e+07 link read bytes and 533.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=cpu,type=four,vary=sharing,w=1,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x576ac0000000, copy home 0x576bc0000000, direct level 0x576c80000000, copy level 0x576d40000000
- factor effect within the cell: on the direct route 0.0003 [-0.0003, 0.0007] ms, on the copy route -0.0001 [-0.0012, 0.0006] ms; change relative to the copy call at home: +0.6 %
- per repetition: direct home 8.382e+06 link read bytes and 326.6 SMMU translation requests; copy home 8.38e+06 link read bytes and 130.9 SMMU translation requests; direct level 8.382e+06 link read bytes and 328.3 SMMU translation requests; copy level 8.38e+06 link read bytes and 130.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x507d80000000, copy home 0x507e40000000, direct level 0x507f00000000, copy level 0x507fc0000000
- factor effect within the cell: on the direct route -0.0086 [-0.0094, -0.0077] ms, on the copy route 0.1435 [0.1414, 0.1473] ms; change relative to the copy call at home: -50.3 %
- per repetition: direct home 0 link read bytes and 948.2 SMMU translation requests; copy home 0 link read bytes and 16 SMMU translation requests; direct level 0 link read bytes and 948.2 SMMU translation requests; copy level 0 link read bytes and 3.236e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=64,kernel=k2,pattern=word,placement=hbm,type=four,vary=sharing,w=1,working-set-mib=32

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x408740000000, copy home 0x408840000000, direct level 0x408900000000, copy level 0x4089c0000000
- factor effect within the cell: on the direct route -0.0010 [-0.0017, -0.0001] ms, on the copy route -0.1368 [-0.2407, -0.1253] ms; change relative to the copy call at home: +21.6 %
- per repetition: direct home 0 link read bytes and 952.3 SMMU translation requests; copy home 0 link read bytes and 550 SMMU translation requests; direct level 0 link read bytes and 957.1 SMMU translation requests; copy level 0 link read bytes and 552.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5bf6c0000000, copy home 0x5bf780000000, direct level 0x5bf840000000, copy level 0x5bf940000000
- factor effect within the cell: on the direct route -0.0141 [-0.0308, 0.0026] ms, on the copy route 0.5822 [0.5793, 0.5831] ms; change relative to the copy call at home: -121.3 %
- per repetition: direct home 5.369e+08 link read bytes and 1.741e+04 SMMU translation requests; copy home 0 link read bytes and 13.89 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.308e+04 SMMU translation requests; copy level 1.074e+08 link read bytes and 2.158e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x56b140000000, copy home 0x56b200000000, direct level 0x56b2c0000000, copy level 0x56b3c0000000
- factor effect within the cell: on the direct route -0.0056 [-0.0063, -0.0049] ms, on the copy route -0.0027 [-0.0203, -0.0001] ms; change relative to the copy call at home: -0.1 %
- per repetition: direct home 5.369e+08 link read bytes and 0 SMMU translation requests; copy home 1.074e+09 link read bytes and 1.641e+04 SMMU translation requests; direct level 5.369e+08 link read bytes and 0 SMMU translation requests; copy level 1.074e+09 link read bytes and 1.645e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4e2bc0000000, copy home 0x4e2cc0000000, direct level 0x4e2d80000000, copy level 0x4e2e80000000
- factor effect within the cell: on the direct route 0.0017 [-0.0009, 0.0039] ms, on the copy route 0.0885 [0.0848, 0.0976] ms; change relative to the copy call at home: -15.5 %
- per repetition: direct home 0 link read bytes and 1.739e+04 SMMU translation requests; copy home 0 link read bytes and 16.78 SMMU translation requests; direct level 0 link read bytes and 1.742e+04 SMMU translation requests; copy level 0 link read bytes and 3.307e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4ef8c0000000, copy home 0x4efa00000000, direct level 0x4efac0000000, copy level 0x4efbc0000000
- factor effect within the cell: on the direct route -0.0016 [-0.0040, -0.0006] ms, on the copy route -0.0142 [-0.0194, -0.0116] ms; change relative to the copy call at home: +0.9 %
- per repetition: direct home 0 link read bytes and 1.741e+04 SMMU translation requests; copy home 0 link read bytes and 3.717e+04 SMMU translation requests; direct level 0 link read bytes and 1.741e+04 SMMU translation requests; copy level 0 link read bytes and 3.703e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=11520,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4015c0000000, copy home 0x401940000000, direct level 0x401c80000000, copy level 0x402000000000
- factor effect within the cell: on the direct route 0.0598 [-0.0745, 0.1075] ms, on the copy route 3.1994 [3.1954, 3.2473] ms; change relative to the copy call at home: -627.0 %
- per repetition: direct home 5.369e+08 link read bytes and 6.722e+07 SMMU translation requests; copy home 0 link read bytes and 2.562 SMMU translation requests; direct level 5.369e+08 link read bytes and 6.72e+07 SMMU translation requests; copy level 1.208e+09 link read bytes and 2.108e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=11520,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5f3980000000, copy home 0x5f3cc0000000, direct level 0x5f4040000000, copy level 0x5f43c0000000
- factor effect within the cell: on the direct route 0.0491 [-0.2054, 0.1848] ms, on the copy route -1.8311 [-1.8487, -1.8136] ms; change relative to the copy call at home: +5.7 %
- per repetition: direct home 5.369e+08 link read bytes and 6.721e+07 SMMU translation requests; copy home 1.211e+10 link read bytes and 1.843e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 6.721e+07 SMMU translation requests; copy level 1.211e+10 link read bytes and 1.844e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4325c0000000, copy home 0x432980000000, direct level 0x432d00000000, copy level 0x4330c0000000
- factor effect within the cell: on the direct route -0.0685 [-0.1703, 0.1221] ms, on the copy route 3.5839 [3.5495, 3.6313] ms; change relative to the copy call at home: -713.1 %
- per repetition: direct home 5.369e+08 link read bytes and 7.822e+07 SMMU translation requests; copy home 0 link read bytes and 2.725 SMMU translation requests; direct level 5.369e+08 link read bytes and 7.818e+07 SMMU translation requests; copy level 1.288e+09 link read bytes and 2.209e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x41c9c0000000, copy home 0x41cd40000000, direct level 0x41d0c0000000, copy level 0x41d480000000
- factor effect within the cell: on the direct route 0.1225 [-0.1267, 0.2010] ms, on the copy route -1.9933 [-2.0073, -1.9807] ms; change relative to the copy call at home: +6.0 %
- per repetition: direct home 5.369e+08 link read bytes and 7.822e+07 SMMU translation requests; copy home 1.292e+10 link read bytes and 1.966e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 7.82e+07 SMMU translation requests; copy level 1.292e+10 link read bytes and 1.966e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5e2a40000000, copy home 0x5e2e00000000, direct level 0x5e3180000000, copy level 0x5e3540000000
- factor effect within the cell: on the direct route 0.2887 [0.0883, 0.4814] ms, on the copy route 1.9050 [1.8781, 1.9148] ms; change relative to the copy call at home: -285.2 %
- per repetition: direct home 0 link read bytes and 7.776e+07 SMMU translation requests; copy home 0 link read bytes and 16.75 SMMU translation requests; direct level 0 link read bytes and 7.776e+07 SMMU translation requests; copy level 0 link read bytes and 4.511e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=12288,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4596c0000000, copy home 0x459a80000000, direct level 0x459e00000000, copy level 0x45a1c0000000
- factor effect within the cell: on the direct route 0.7785 [0.5335, 0.8694] ms, on the copy route -0.0096 [-0.0452, 0.0387] ms; change relative to the copy call at home: +9.3 %
- per repetition: direct home 0 link read bytes and 7.779e+07 SMMU translation requests; copy home 0 link read bytes and 4.489e+05 SMMU translation requests; direct level 0 link read bytes and 7.773e+07 SMMU translation requests; copy level 0 link read bytes and 4.566e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1536,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x480200000000, copy home 0x480300000000, direct level 0x4803c0000000, copy level 0x480500000000
- factor effect within the cell: on the direct route -0.0074 [-0.0258, -0.0037] ms, on the copy route 0.7186 [0.7127, 0.7211] ms; change relative to the copy call at home: -144.3 %
- per repetition: direct home 5.369e+08 link read bytes and 1.931e+04 SMMU translation requests; copy home 0 link read bytes and 12.1 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.923e+04 SMMU translation requests; copy level 1.611e+08 link read bytes and 1.965e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1536,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5993c0000000, copy home 0x5994c0000000, direct level 0x5995c0000000, copy level 0x5996c0000000
- factor effect within the cell: on the direct route -0.0059 [-0.0068, -0.0045] ms, on the copy route -0.0188 [-0.0220, -0.0081] ms; change relative to the copy call at home: +0.3 %
- per repetition: direct home 5.369e+08 link read bytes and 0 SMMU translation requests; copy home 1.611e+09 link read bytes and 2.46e+04 SMMU translation requests; direct level 5.369e+08 link read bytes and 0 SMMU translation requests; copy level 1.611e+09 link read bytes and 2.464e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x57ad40000000, copy home 0x57b200000000, direct level 0x57b680000000, copy level 0x57bb40000000
- factor effect within the cell: on the direct route -0.0865 [-0.3475, 0.0204] ms, on the copy route -2.6490 [-2.6864, -2.6397] ms; change relative to the copy call at home: +5.4 %
- per repetition: direct home 4.961e+10 link read bytes and 2.724e+05 SMMU translation requests; copy home 1.718e+10 link read bytes and 2.766e+05 SMMU translation requests; direct level 4.962e+10 link read bytes and 2.745e+05 SMMU translation requests; copy level 1.718e+10 link read bytes and 2.765e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5151c0000000, copy home 0x515680000000, direct level 0x515b00000000, copy level 0x515f80000000
- factor effect within the cell: on the direct route -0.0242 [-0.0421, -0.0175] ms, on the copy route -2.7557 [-2.7570, -2.7478] ms; change relative to the copy call at home: +6.0 %
- per repetition: direct home 3.355e+07 link read bytes and 2.026e+06 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; direct level 3.355e+07 link read bytes and 2.018e+06 SMMU translation requests; copy level 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4c5640000000, copy home 0x4c5b00000000, direct level 0x4c5f80000000, copy level 0x4c6440000000
- factor effect within the cell: on the direct route 0.1260 [-0.0968, 0.3212] ms, on the copy route 4.6793 [4.6751, 4.6830] ms; change relative to the copy call at home: -887.5 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 0 link read bytes and 2.312 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy level 1.718e+09 link read bytes and 2.915e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=pitched,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5366c0000000, copy home 0x536b40000000, direct level 0x536fc0000000, copy level 0x537480000000
- factor effect within the cell: on the direct route 0.0854 [-0.1305, 0.2207] ms, on the copy route 10.2055 [10.1997, 10.2128] ms; change relative to the copy call at home: -1964.3 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 0 link read bytes and 3.846 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.212e+08 SMMU translation requests; copy level 1.718e+09 link read bytes and 6.39e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x44b680000000, copy home 0x44bb40000000, direct level 0x44bfc0000000, copy level 0x44c480000000
- factor effect within the cell: on the direct route 0.0419 [-0.0437, 0.2767] ms, on the copy route -2.4949 [-2.5049, -2.4791] ms; change relative to the copy call at home: +5.6 %
- per repetition: direct home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy home 1.723e+10 link read bytes and 2.622e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; copy level 1.723e+10 link read bytes and 2.623e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=2048,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5138c0000000, copy home 0x513a00000000, direct level 0x513b00000000, copy level 0x513c40000000
- factor effect within the cell: on the direct route 0.0006 [-0.0723, 0.0186] ms, on the copy route 0.7429 [0.7356, 0.7476] ms; change relative to the copy call at home: -148.8 %
- per repetition: direct home 5.369e+08 link read bytes and 2.536e+04 SMMU translation requests; copy home 0 link read bytes and 9.262 SMMU translation requests; direct level 5.369e+08 link read bytes and 2.115e+04 SMMU translation requests; copy level 2.147e+08 link read bytes and 1.986e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=2048,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5f19c0000000, copy home 0x5f1ac0000000, direct level 0x5f1bc0000000, copy level 0x5f1d00000000
- factor effect within the cell: on the direct route -0.0119 [-0.0139, -0.0107] ms, on the copy route 0.0437 [0.0420, 0.0569] ms; change relative to the copy call at home: -0.9 %
- per repetition: direct home 5.369e+08 link read bytes and 0 SMMU translation requests; copy home 2.147e+09 link read bytes and 3.279e+04 SMMU translation requests; direct level 5.369e+08 link read bytes and 0 SMMU translation requests; copy level 2.147e+09 link read bytes and 3.283e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=24576,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5dda40000000, copy home 0x5de100000000, direct level 0x5de780000000, copy level 0x5dee40000000
- factor effect within the cell: on the direct route -0.1735 [-0.3033, 0.0164] ms, on the copy route -1.2753 [-1.3603, -1.2317] ms; change relative to the copy call at home: +1.5 %
- per repetition: direct home 7.684e+10 link read bytes and 5.025e+05 SMMU translation requests; copy home 2.577e+10 link read bytes and 4.145e+05 SMMU translation requests; direct level 7.684e+10 link read bytes and 5.07e+05 SMMU translation requests; copy level 2.577e+10 link read bytes and 4.147e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=24576,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x46ff40000000, copy home 0x4705c0000000, direct level 0x470c40000000, copy level 0x471300000000
- factor effect within the cell: on the direct route 0.0813 [-0.1175, 0.2512] ms, on the copy route 7.0491 [7.0273, 7.0772] ms; change relative to the copy call at home: -1346.0 %
- per repetition: direct home 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; copy home 0 link read bytes and 2.154 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; copy level 2.577e+09 link read bytes and 5.057e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=24576,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x42c680000000, copy home 0x42cd00000000, direct level 0x42d380000000, copy level 0x42da40000000
- factor effect within the cell: on the direct route -0.0010 [-0.2744, 0.1859] ms, on the copy route -1.7666 [-1.8123, -1.7081] ms; change relative to the copy call at home: +2.7 %
- per repetition: direct home 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; copy home 2.585e+10 link read bytes and 3.933e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; copy level 2.585e+10 link read bytes and 3.934e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=256,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4d9c80000000, copy home 0x4d9d40000000, direct level 0x4d9dc0000000, copy level 0x4d9e40000000
- factor effect within the cell: on the direct route -0.0464 [-0.0480, -0.0443] ms, on the copy route -0.0042 [-0.0054, -0.0039] ms; change relative to the copy call at home: -3.9 %
- per repetition: direct home 7.685e+08 link read bytes and 0 SMMU translation requests; copy home 2.684e+08 link read bytes and 4229 SMMU translation requests; direct level 7.684e+08 link read bytes and 0 SMMU translation requests; copy level 2.684e+08 link read bytes and 4229 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=256,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4f33c0000000, copy home 0x4f3480000000, direct level 0x4f3500000000, copy level 0x4f35c0000000
- factor effect within the cell: on the direct route 0.0001 [-0.0006, 0.0007] ms, on the copy route -0.0000 [-0.0012, 0.0004] ms; change relative to the copy call at home: +0.0 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 4229 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 4227 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4fc680000000, copy home 0x4fc740000000, direct level 0x4fc7c0000000, copy level 0x4fc8c0000000
- factor effect within the cell: on the direct route -0.0033 [-0.0107, -0.0010] ms, on the copy route 0.1608 [0.1593, 0.1617] ms; change relative to the copy call at home: -36.9 %
- per repetition: direct home 5.368e+08 link read bytes and 4950 SMMU translation requests; copy home 0 link read bytes and 14.85 SMMU translation requests; direct level 5.368e+08 link read bytes and 4939 SMMU translation requests; copy level 2.684e+07 link read bytes and 8084 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5cdf00000000, copy home 0x5cdfc0000000, direct level 0x5ce040000000, copy level 0x5ce100000000
- factor effect within the cell: on the direct route -0.0055 [-0.0069, -0.0037] ms, on the copy route 0.0517 [0.0446, 0.0548] ms; change relative to the copy call at home: -4.6 %
- per repetition: direct home 5.368e+08 link read bytes and 0 SMMU translation requests; copy home 2.684e+08 link read bytes and 4117 SMMU translation requests; direct level 5.368e+08 link read bytes and 0 SMMU translation requests; copy level 2.684e+08 link read bytes and 4117 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x464c00000000, copy home 0x464cc0000000, direct level 0x464d40000000, copy level 0x464e40000000
- factor effect within the cell: on the direct route -0.0068 [-0.0098, -0.0051] ms, on the copy route 0.0468 [0.0415, 0.0513] ms; change relative to the copy call at home: -10.6 %
- per repetition: direct home 0 link read bytes and 4980 SMMU translation requests; copy home 0 link read bytes and 16.8 SMMU translation requests; direct level 0 link read bytes and 4985 SMMU translation requests; copy level 0 link read bytes and 9254 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=256,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: no, cap hit: yes
- home at placement hbm, level at placement hbm; buffers: direct home 0x550580000000, copy home 0x550640000000, direct level 0x5506c0000000, copy level 0x5507c0000000
- factor effect within the cell: on the direct route -0.0103 [-0.0105, -0.0101] ms, on the copy route -0.1305 [-0.1379, -0.1290] ms; change relative to the copy call at home: +9.8 %
- per repetition: direct home 0 link read bytes and 4974 SMMU translation requests; copy home 0 link read bytes and 4140 SMMU translation requests; direct level 0 link read bytes and 4964 SMMU translation requests; copy level 0 link read bytes and 4132 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=32768,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x45b700000000, copy home 0x45bfc0000000, direct level 0x45c880000000, copy level 0x45d140000000
- factor effect within the cell: on the direct route -0.2956 [-0.4267, -0.1891] ms, on the copy route -1.8169 [-1.8316, -1.7766] ms; change relative to the copy call at home: +1.7 %
- per repetition: direct home 9.934e+10 link read bytes and 7.465e+05 SMMU translation requests; copy home 3.436e+10 link read bytes and 5.526e+05 SMMU translation requests; direct level 9.934e+10 link read bytes and 7.662e+05 SMMU translation requests; copy level 3.436e+10 link read bytes and 5.525e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=32768,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4e3280000000, copy home 0x4e3b00000000, direct level 0x4e4380000000, copy level 0x4e4c40000000
- factor effect within the cell: on the direct route 0.0874 [-0.1969, 0.1693] ms, on the copy route 9.3347 [9.2877, 9.3492] ms; change relative to the copy call at home: -1784.0 %
- per repetition: direct home 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; copy home 0 link read bytes and 1.308 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.912e+08 SMMU translation requests; copy level 3.436e+09 link read bytes and 8.539e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=32768,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x492000000000, copy home 0x4928c0000000, direct level 0x493140000000, copy level 0x493a00000000
- factor effect within the cell: on the direct route 0.2277 [0.0186, 0.3811] ms, on the copy route -1.4006 [-1.4554, -1.3484] ms; change relative to the copy call at home: +1.9 %
- per repetition: direct home 5.369e+08 link read bytes and 1.912e+08 SMMU translation requests; copy home 3.448e+10 link read bytes and 5.244e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; copy level 3.448e+10 link read bytes and 5.245e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=4096,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5be100000000, copy home 0x5be300000000, direct level 0x5be480000000, copy level 0x5be600000000
- factor effect within the cell: on the direct route -2.2254 [-2.2786, -2.1914] ms, on the copy route 0.0855 [0.0792, 0.0899] ms; change relative to the copy call at home: -18.5 %
- per repetition: direct home 1.287e+10 link read bytes and 6.866e+04 SMMU translation requests; copy home 4.295e+09 link read bytes and 6.831e+04 SMMU translation requests; direct level 1.285e+10 link read bytes and 6.878e+04 SMMU translation requests; copy level 4.295e+09 link read bytes and 6.827e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=4096,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5f7400000000, copy home 0x5f7600000000, direct level 0x5f77c0000000, copy level 0x5f7940000000
- factor effect within the cell: on the direct route -0.0158 [-0.0219, -0.0021] ms, on the copy route -0.0069 [-0.0239, -0.0021] ms; change relative to the copy call at home: -0.1 %
- per repetition: direct home 0 link read bytes and 4.946e+04 SMMU translation requests; copy home 0 link read bytes and 5.44e+04 SMMU translation requests; direct level 0 link read bytes and 4.907e+04 SMMU translation requests; copy level 0 link read bytes and 5.614e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4df6c0000000, copy home 0x4df880000000, direct level 0x4dfa00000000, copy level 0x4dfbc0000000
- factor effect within the cell: on the direct route -0.0450 [-0.0726, 0.0098] ms, on the copy route 1.2571 [1.2461, 1.2654] ms; change relative to the copy call at home: -256.6 %
- per repetition: direct home 5.369e+08 link read bytes and 3.332e+04 SMMU translation requests; copy home 0 link read bytes and 6.688 SMMU translation requests; direct level 5.369e+08 link read bytes and 3.329e+04 SMMU translation requests; copy level 4.295e+08 link read bytes and 3.336e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5773c0000000, copy home 0x577540000000, direct level 0x5776c0000000, copy level 0x577880000000
- factor effect within the cell: on the direct route -0.0152 [-0.0485, 0.0525] ms, on the copy route 0.1905 [0.1646, 0.1973] ms; change relative to the copy call at home: -1.7 %
- per repetition: direct home 5.369e+08 link read bytes and 1198 SMMU translation requests; copy home 4.295e+09 link read bytes and 6.556e+04 SMMU translation requests; direct level 5.369e+08 link read bytes and 1236 SMMU translation requests; copy level 4.295e+09 link read bytes and 6.561e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4a0d80000000, copy home 0x4a0f40000000, direct level 0x4a10c0000000, copy level 0x4a1280000000
- factor effect within the cell: on the direct route 0.0142 [0.0101, 0.0157] ms, on the copy route 0.5622 [0.5535, 0.5699] ms; change relative to the copy call at home: -97.8 %
- per repetition: direct home 0 link read bytes and 6.665e+04 SMMU translation requests; copy home 0 link read bytes and 16.81 SMMU translation requests; direct level 0 link read bytes and 6.668e+04 SMMU translation requests; copy level 0 link read bytes and 1.557e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=4096,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4dfc00000000, copy home 0x4dfdc0000000, direct level 0x4dff40000000, copy level 0x4e0100000000
- factor effect within the cell: on the direct route 0.0059 [0.0024, 0.0090] ms, on the copy route 0.0093 [0.0015, 0.0180] ms; change relative to the copy call at home: -0.1 %
- per repetition: direct home 0 link read bytes and 6.662e+04 SMMU translation requests; copy home 0 link read bytes and 1.386e+05 SMMU translation requests; direct level 0 link read bytes and 6.658e+04 SMMU translation requests; copy level 0 link read bytes and 1.384e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=1,tiling=tiles,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x427bc0000000, copy home 0x427d00000000, direct level 0x427dc0000000, copy level 0x427ec0000000
- factor effect within the cell: on the direct route -0.7477 [-0.7547, -0.7440] ms, on the copy route -0.0404 [-0.0432, -0.0372] ms; change relative to the copy call at home: -19.0 %
- per repetition: direct home 8.028e+08 link read bytes and 3700 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 8.028e+08 link read bytes and 3186 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=16,tiling=tiles,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x468200000000, copy home 0x468300000000, direct level 0x4683c0000000, copy level 0x4684c0000000
- factor effect within the cell: on the direct route -7.6922 [-7.7264, -7.6197] ms, on the copy route -0.0343 [-0.0566, -0.0144] ms; change relative to the copy call at home: -78.6 %
- per repetition: direct home 1.284e+10 link read bytes and 3.606e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 1.285e+10 link read bytes and 3.591e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=2,tiling=tiles,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5b6840000000, copy home 0x5b6980000000, direct level 0x5b6a40000000, copy level 0x5b6b40000000
- factor effect within the cell: on the direct route -1.0108 [-1.0243, -0.9923] ms, on the copy route -0.0456 [-0.0489, -0.0410] ms; change relative to the copy call at home: -23.5 %
- per repetition: direct home 1.606e+09 link read bytes and 1.201e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 1.606e+09 link read bytes and 9086 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=4,tiling=tiles,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4e49c0000000, copy home 0x4e4b00000000, direct level 0x4e4bc0000000, copy level 0x4e4cc0000000
- factor effect within the cell: on the direct route -1.9089 [-1.9331, -1.9035] ms, on the copy route -0.0527 [-0.0565, -0.0466] ms; change relative to the copy call at home: -37.8 %
- per repetition: direct home 3.211e+09 link read bytes and 1.805e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.641e+04 SMMU translation requests; direct level 3.211e+09 link read bytes and 1.8e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.641e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=64,tiling=tiles,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5d3c40000000, copy home 0x5d3d40000000, direct level 0x5d3e40000000, copy level 0x5d3f00000000
- factor effect within the cell: on the direct route -31.3641 [-31.4427, -31.3211] ms, on the copy route -0.0538 [-0.0967, -0.0158] ms; change relative to the copy call at home: -107.7 %
- per repetition: direct home 5.138e+10 link read bytes and 3.625e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 5.138e+10 link read bytes and 3.631e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4b2840000000, copy home 0x4b2980000000, direct level 0x4b2a40000000, copy level 0x4b2b40000000
- factor effect within the cell: on the direct route -3.5954 [-3.6285, -3.5518] ms, on the copy route -0.0255 [-0.0322, -0.0166] ms; change relative to the copy call at home: -54.7 %
- per repetition: direct home 6.422e+09 link read bytes and 3.6e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 6.423e+09 link read bytes and 3.582e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=1,tiling=tiles,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x41fec0000000, copy home 0x420000000000, direct level 0x4200c0000000, copy level 0x4201c0000000
- factor effect within the cell: on the direct route -0.0023 [-0.0034, -0.0014] ms, on the copy route -0.0020 [-0.0031, 0.0007] ms; change relative to the copy call at home: -0.1 %
- per repetition: direct home 0 link read bytes and 539.6 SMMU translation requests; copy home 0 link read bytes and 1945 SMMU translation requests; direct level 0 link read bytes and 528.3 SMMU translation requests; copy level 0 link read bytes and 1822 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=16,tiling=tiles,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4f5e80000000, copy home 0x4f5f80000000, direct level 0x4f6080000000, copy level 0x4f6140000000
- factor effect within the cell: on the direct route 0.0304 [0.0159, 0.0433] ms, on the copy route 0.0015 [-0.0093, 0.0076] ms; change relative to the copy call at home: +0.4 %
- per repetition: direct home 0 link read bytes and 1.038e+04 SMMU translation requests; copy home 0 link read bytes and 1.22e+04 SMMU translation requests; direct level 0 link read bytes and 9597 SMMU translation requests; copy level 0 link read bytes and 1.205e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=2,tiling=tiles,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x524780000000, copy home 0x524880000000, direct level 0x524940000000, copy level 0x524a40000000
- factor effect within the cell: on the direct route -0.0035 [-0.0073, -0.0012] ms, on the copy route -0.0040 [-0.0065, -0.0024] ms; change relative to the copy call at home: +0.0 %
- per repetition: direct home 0 link read bytes and 1535 SMMU translation requests; copy home 0 link read bytes and 2622 SMMU translation requests; direct level 0 link read bytes and 1538 SMMU translation requests; copy level 0 link read bytes and 2627 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=4,tiling=tiles,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4e5600000000, copy home 0x4e5700000000, direct level 0x4e5800000000, copy level 0x4e58c0000000
- factor effect within the cell: on the direct route -0.0062 [-0.0130, -0.0016] ms, on the copy route -0.0012 [-0.0033, 0.0007] ms; change relative to the copy call at home: -0.2 %
- per repetition: direct home 0 link read bytes and 2983 SMMU translation requests; copy home 0 link read bytes and 4256 SMMU translation requests; direct level 0 link read bytes and 2931 SMMU translation requests; copy level 0 link read bytes and 4030 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=64,tiling=tiles,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5ae200000000, copy home 0x5ae300000000, direct level 0x5ae400000000, copy level 0x5ae500000000
- factor effect within the cell: on the direct route -0.0275 [-0.0955, 0.0485] ms, on the copy route -0.0071 [-0.0890, 0.0888] ms; change relative to the copy call at home: -0.0 %
- per repetition: direct home 0 link read bytes and 3.819e+04 SMMU translation requests; copy home 0 link read bytes and 3.861e+04 SMMU translation requests; direct level 0 link read bytes and 3.809e+04 SMMU translation requests; copy level 0 link read bytes and 3.898e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x539080000000, copy home 0x539200000000, direct level 0x5392c0000000, copy level 0x5393c0000000
- factor effect within the cell: on the direct route -0.0096 [-0.0153, -0.0070] ms, on the copy route -0.0009 [-0.0088, 0.0039] ms; change relative to the copy call at home: -0.2 %
- per repetition: direct home 0 link read bytes and 5460 SMMU translation requests; copy home 0 link read bytes and 5997 SMMU translation requests; direct level 0 link read bytes and 5856 SMMU translation requests; copy level 0 link read bytes and 6220 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=1,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x412000000000, copy home 0x412180000000, direct level 0x412240000000, copy level 0x412340000000
- factor effect within the cell: on the direct route -0.6986 [-0.7019, -0.6926] ms, on the copy route 0.2977 [0.2946, 0.3006] ms; change relative to the copy call at home: -44.6 %
- per repetition: direct home 8.028e+08 link read bytes and 2.214e+04 SMMU translation requests; copy home 0 link read bytes and 8209 SMMU translation requests; direct level 8.028e+08 link read bytes and 2.214e+04 SMMU translation requests; copy level 5.369e+07 link read bytes and 2.572e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=16,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4dd840000000, copy home 0x4dd940000000, direct level 0x4dda00000000, copy level 0x4ddb00000000
- factor effect within the cell: on the direct route -7.8924 [-7.9405, -7.8601] ms, on the copy route 0.2835 [0.2763, 0.3044] ms; change relative to the copy call at home: -98.9 %
- per repetition: direct home 1.284e+10 link read bytes and 3.612e+04 SMMU translation requests; copy home 0 link read bytes and 8209 SMMU translation requests; direct level 1.285e+10 link read bytes and 3.595e+04 SMMU translation requests; copy level 5.369e+07 link read bytes and 2.25e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=2,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4befc0000000, copy home 0x4bf0c0000000, direct level 0x4bf1c0000000, copy level 0x4bf280000000
- factor effect within the cell: on the direct route -0.8293 [-0.8333, -0.8176] ms, on the copy route 0.2936 [0.2910, 0.2969] ms; change relative to the copy call at home: -42.7 %
- per repetition: direct home 1.606e+09 link read bytes and 3.608e+04 SMMU translation requests; copy home 0 link read bytes and 8209 SMMU translation requests; direct level 1.606e+09 link read bytes and 3.58e+04 SMMU translation requests; copy level 5.369e+07 link read bytes and 2.494e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=4,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x567080000000, copy home 0x567180000000, direct level 0x567280000000, copy level 0x567340000000
- factor effect within the cell: on the direct route -1.8264 [-1.8328, -1.8090] ms, on the copy route 0.2947 [0.2919, 0.2976] ms; change relative to the copy call at home: -61.8 %
- per repetition: direct home 3.211e+09 link read bytes and 3.607e+04 SMMU translation requests; copy home 0 link read bytes and 8209 SMMU translation requests; direct level 3.211e+09 link read bytes and 3.613e+04 SMMU translation requests; copy level 5.369e+07 link read bytes and 2.567e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=64,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4723c0000000, copy home 0x4724c0000000, direct level 0x4725c0000000, copy level 0x472680000000
- factor effect within the cell: on the direct route -37.3660 [-37.4563, -37.3300] ms, on the copy route 0.2947 [0.2486, 0.3043] ms; change relative to the copy call at home: -136.5 %
- per repetition: direct home 5.138e+10 link read bytes and 3.621e+04 SMMU translation requests; copy home 0 link read bytes and 8208 SMMU translation requests; direct level 5.138e+10 link read bytes and 3.591e+04 SMMU translation requests; copy level 5.369e+07 link read bytes and 2.394e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5ae400000000, copy home 0x5ae500000000, direct level 0x5ae600000000, copy level 0x5ae6c0000000
- factor effect within the cell: on the direct route -3.3296 [-3.3500, -3.3107] ms, on the copy route 0.2995 [0.2929, 0.3043] ms; change relative to the copy call at home: -72.1 %
- per repetition: direct home 6.422e+09 link read bytes and 3.625e+04 SMMU translation requests; copy home 0 link read bytes and 8209 SMMU translation requests; direct level 6.423e+09 link read bytes and 3.604e+04 SMMU translation requests; copy level 5.369e+07 link read bytes and 2.523e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x529440000000, copy home 0x529540000000, direct level 0x529640000000, copy level 0x529700000000
- factor effect within the cell: on the direct route -3.6543 [-3.6839, -3.6387] ms, on the copy route 0.3376 [0.3343, 0.3473] ms; change relative to the copy call at home: -79.4 %
- per repetition: direct home 6.422e+09 link read bytes and 3.614e+04 SMMU translation requests; copy home 0 link read bytes and 8209 SMMU translation requests; direct level 6.423e+09 link read bytes and 3.599e+04 SMMU translation requests; copy level 5.369e+07 link read bytes and 3.315e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=1,tiling=tiles,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x587b00000000, copy home 0x587c00000000, direct level 0x587d00000000, copy level 0x587dc0000000
- factor effect within the cell: on the direct route -0.6298 [-0.6361, -0.6276] ms, on the copy route 0.0506 [0.0448, 0.0545] ms; change relative to the copy call at home: -18.3 %
- per repetition: direct home 8.028e+08 link read bytes and 3711 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 8.028e+08 link read bytes and 3166 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.647e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=16,tiling=tiles,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5ea7c0000000, copy home 0x5ea8c0000000, direct level 0x5ea980000000, copy level 0x5eaa80000000
- factor effect within the cell: on the direct route -6.9907 [-7.0233, -6.9757] ms, on the copy route 0.0788 [0.0649, 0.0835] ms; change relative to the copy call at home: -72.6 %
- per repetition: direct home 1.284e+10 link read bytes and 3.612e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 1.285e+10 link read bytes and 3.598e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.644e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=2,tiling=tiles,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x558340000000, copy home 0x558440000000, direct level 0x558540000000, copy level 0x558600000000
- factor effect within the cell: on the direct route -0.8877 [-0.8995, -0.8796] ms, on the copy route 0.0278 [0.0227, 0.0318] ms; change relative to the copy call at home: -22.2 %
- per repetition: direct home 1.606e+09 link read bytes and 1.202e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 1.606e+09 link read bytes and 8993 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.644e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=4,tiling=tiles,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5f3400000000, copy home 0x5f3580000000, direct level 0x5f3640000000, copy level 0x5f3740000000
- factor effect within the cell: on the direct route -1.8961 [-1.9114, -1.8880] ms, on the copy route 0.0552 [0.0498, 0.0617] ms; change relative to the copy call at home: -39.6 %
- per repetition: direct home 3.211e+09 link read bytes and 1.809e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 3.211e+09 link read bytes and 1.798e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.646e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=64,tiling=tiles,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5f6140000000, copy home 0x5f6240000000, direct level 0x5f6300000000, copy level 0x5f6400000000
- factor effect within the cell: on the direct route -30.3769 [-30.4733, -30.3346] ms, on the copy route 0.0712 [0.0491, 0.1257] ms; change relative to the copy call at home: -104.7 %
- per repetition: direct home 5.138e+10 link read bytes and 3.608e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 5.138e+10 link read bytes and 3.594e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.65e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x558e00000000, copy home 0x558f00000000, direct level 0x558fc0000000, copy level 0x5590c0000000
- factor effect within the cell: on the direct route -3.5187 [-3.5712, -3.4914] ms, on the copy route 0.0592 [0.0486, 0.0700] ms; change relative to the copy call at home: -55.0 %
- per repetition: direct home 6.422e+09 link read bytes and 3.606e+04 SMMU translation requests; copy home 5.369e+08 link read bytes and 1.64e+04 SMMU translation requests; direct level 6.423e+09 link read bytes and 3.584e+04 SMMU translation requests; copy level 5.369e+08 link read bytes and 1.646e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=1,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x511980000000, copy home 0x511a80000000, direct level 0x511b40000000, copy level 0x511c40000000
- factor effect within the cell: on the direct route 0.0223 [0.0208, 0.0230] ms, on the copy route 0.0891 [0.0869, 0.0903] ms; change relative to the copy call at home: -8.9 %
- per repetition: direct home 0 link read bytes and 3.046e+04 SMMU translation requests; copy home 0 link read bytes and 1.288e+04 SMMU translation requests; direct level 0 link read bytes and 3.271e+04 SMMU translation requests; copy level 0 link read bytes and 2.961e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=16,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x523380000000, copy home 0x523480000000, direct level 0x523540000000, copy level 0x523640000000
- factor effect within the cell: on the direct route 0.1330 [0.1129, 0.1492] ms, on the copy route 0.0945 [0.0916, 0.0988] ms; change relative to the copy call at home: +0.5 %
- per repetition: direct home 0 link read bytes and 4.25e+04 SMMU translation requests; copy home 0 link read bytes and 1.29e+04 SMMU translation requests; direct level 0 link read bytes and 4.127e+04 SMMU translation requests; copy level 0 link read bytes and 2.894e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=2,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5ed880000000, copy home 0x5ed980000000, direct level 0x5eda80000000, copy level 0x5edb40000000
- factor effect within the cell: on the direct route 0.1270 [0.1237, 0.1283] ms, on the copy route 0.0947 [0.0903, 0.0954] ms; change relative to the copy call at home: +2.9 %
- per repetition: direct home 0 link read bytes and 4.299e+04 SMMU translation requests; copy home 0 link read bytes and 1.287e+04 SMMU translation requests; direct level 0 link read bytes and 4.17e+04 SMMU translation requests; copy level 0 link read bytes and 2.988e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=4,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5bc8c0000000, copy home 0x5bc9c0000000, direct level 0x5bca80000000, copy level 0x5bcb80000000
- factor effect within the cell: on the direct route 0.0235 [0.0216, 0.0287] ms, on the copy route 0.0915 [0.0873, 0.0951] ms; change relative to the copy call at home: -3.4 %
- per repetition: direct home 0 link read bytes and 4.274e+04 SMMU translation requests; copy home 0 link read bytes and 1.26e+04 SMMU translation requests; direct level 0 link read bytes and 4.515e+04 SMMU translation requests; copy level 0 link read bytes and 2.917e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=64,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5a5b40000000, copy home 0x5a5c80000000, direct level 0x5a5d80000000, copy level 0x5a5e40000000
- factor effect within the cell: on the direct route 0.1448 [0.1035, 0.1690] ms, on the copy route 0.0759 [0.0607, 0.1596] ms; change relative to the copy call at home: +0.2 %
- per repetition: direct home 0 link read bytes and 4.172e+04 SMMU translation requests; copy home 0 link read bytes and 1.3e+04 SMMU translation requests; direct level 0 link read bytes and 4.017e+04 SMMU translation requests; copy level 0 link read bytes and 2.874e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=gather,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x52bd00000000, copy home 0x52be40000000, direct level 0x52bf40000000, copy level 0x52c000000000
- factor effect within the cell: on the direct route 0.0266 [0.0147, 0.0378] ms, on the copy route 0.0863 [0.0802, 0.0915] ms; change relative to the copy call at home: -1.6 %
- per repetition: direct home 0 link read bytes and 4.249e+04 SMMU translation requests; copy home 0 link read bytes and 1.289e+04 SMMU translation requests; direct level 0 link read bytes and 4.466e+04 SMMU translation requests; copy level 0 link read bytes and 3.056e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,recopy=pitched,sweeps=8,tiling=tiles,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x44d800000000, copy home 0x44d900000000, direct level 0x44d9c0000000, copy level 0x44dac0000000
- factor effect within the cell: on the direct route 0.0464 [0.0400, 0.0529] ms, on the copy route 0.3010 [0.2979, 0.3100] ms; change relative to the copy call at home: -7.1 %
- per repetition: direct home 0 link read bytes and 3.853e+04 SMMU translation requests; copy home 0 link read bytes and 1.283e+04 SMMU translation requests; direct level 0 link read bytes and 4.165e+04 SMMU translation requests; copy level 0 link read bytes and 3.626e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=1,tiling=tiles,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x53e5c0000000, copy home 0x53e6c0000000, direct level 0x53e7c0000000, copy level 0x53e880000000
- factor effect within the cell: on the direct route 0.0786 [0.0763, 0.0818] ms, on the copy route -0.0276 [-0.0323, -0.0232] ms; change relative to the copy call at home: +9.0 %
- per repetition: direct home 0 link read bytes and 3.062e+04 SMMU translation requests; copy home 0 link read bytes and 3.108e+04 SMMU translation requests; direct level 0 link read bytes and 2.594e+04 SMMU translation requests; copy level 0 link read bytes and 3.068e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=16,tiling=tiles,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x47fa80000000, copy home 0x47fbc0000000, direct level 0x47fcc0000000, copy level 0x47fd80000000
- factor effect within the cell: on the direct route -0.0161 [-0.0288, -0.0048] ms, on the copy route -0.0163 [-0.0437, -0.0108] ms; change relative to the copy call at home: +0.0 %
- per repetition: direct home 0 link read bytes and 3.854e+04 SMMU translation requests; copy home 0 link read bytes and 3.151e+04 SMMU translation requests; direct level 0 link read bytes and 3.84e+04 SMMU translation requests; copy level 0 link read bytes and 3.092e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=2,tiling=tiles,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x406ac0000000, copy home 0x406bc0000000, direct level 0x406cc0000000, copy level 0x406dc0000000
- factor effect within the cell: on the direct route 0.0168 [0.0120, 0.0185] ms, on the copy route -0.0274 [-0.0285, -0.0252] ms; change relative to the copy call at home: +2.7 %
- per repetition: direct home 0 link read bytes and 4.299e+04 SMMU translation requests; copy home 0 link read bytes and 3.175e+04 SMMU translation requests; direct level 0 link read bytes and 4.276e+04 SMMU translation requests; copy level 0 link read bytes and 3.129e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=4,tiling=tiles,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x478080000000, copy home 0x478180000000, direct level 0x478280000000, copy level 0x478380000000
- factor effect within the cell: on the direct route 0.0237 [0.0216, 0.0275] ms, on the copy route -0.0206 [-0.0224, -0.0167] ms; change relative to the copy call at home: +1.8 %
- per repetition: direct home 0 link read bytes and 4.289e+04 SMMU translation requests; copy home 0 link read bytes and 3.092e+04 SMMU translation requests; direct level 0 link read bytes and 4.257e+04 SMMU translation requests; copy level 0 link read bytes and 3.072e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=64,tiling=tiles,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5bb440000000, copy home 0x5bb540000000, direct level 0x5bb600000000, copy level 0x5bb700000000
- factor effect within the cell: on the direct route -0.1376 [-0.2098, -0.0828] ms, on the copy route -0.0035 [-0.0796, 0.0247] ms; change relative to the copy call at home: -0.5 %
- per repetition: direct home 0 link read bytes and 3.792e+04 SMMU translation requests; copy home 0 link read bytes and 3.701e+04 SMMU translation requests; direct level 0 link read bytes and 3.812e+04 SMMU translation requests; copy level 0 link read bytes and 3.561e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x499740000000, copy home 0x499840000000, direct level 0x499940000000, copy level 0x499a00000000
- factor effect within the cell: on the direct route -0.0602 [-0.0642, -0.0519] ms, on the copy route -0.0211 [-0.0315, -0.0160] ms; change relative to the copy call at home: -1.0 %
- per repetition: direct home 0 link read bytes and 3.879e+04 SMMU translation requests; copy home 0 link read bytes and 3.134e+04 SMMU translation requests; direct level 0 link read bytes and 4.449e+04 SMMU translation requests; copy level 0 link read bytes and 3.172e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,generator=uniform,host=reads,kernel=k4,placement=cpu,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x489980000000, copy home 0x489c40000000, direct level 0x489ec0000000, copy level 0x48a180000000
- factor effect within the cell: on the direct route 0.2374 [0.1350, 0.2896] ms, on the copy route -0.2649 [-0.2798, -0.2188] ms; change relative to the copy call at home: +2.0 %
- per repetition: direct home 2.553e+10 link read bytes and 1.367e+05 SMMU translation requests; copy home 8.59e+09 link read bytes and 1.385e+05 SMMU translation requests; direct level 2.558e+10 link read bytes and 1.365e+05 SMMU translation requests; copy level 8.59e+09 link read bytes and 1.386e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,generator=uniform,host=reads,kernel=k4,placement=hbm,type=four,vary=sharing

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x45b240000000, copy home 0x45b500000000, direct level 0x45b780000000, copy level 0x45ba40000000
- factor effect within the cell: on the direct route -0.0225 [-0.0321, -0.0078] ms, on the copy route -0.0023 [-0.0393, 0.0166] ms; change relative to the copy call at home: -0.1 %
- per repetition: direct home 0 link read bytes and 1.447e+05 SMMU translation requests; copy home 0 link read bytes and 3.349e+05 SMMU translation requests; direct level 0 link read bytes and 1.43e+05 SMMU translation requests; copy level 0 link read bytes and 3.262e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5d85c0000000, copy home 0x5d8880000000, direct level 0x5d8b00000000, copy level 0x5d8dc0000000
- factor effect within the cell: on the direct route -0.0355 [-0.0380, 0.1035] ms, on the copy route 2.4132 [2.3787, 2.4346] ms; change relative to the copy call at home: -476.1 %
- per repetition: direct home 5.369e+08 link read bytes and 4.426e+04 SMMU translation requests; copy home 0 link read bytes and 3.35 SMMU translation requests; direct level 5.369e+08 link read bytes and 8.833e+04 SMMU translation requests; copy level 8.59e+08 link read bytes and 6.067e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5d6d00000000, copy home 0x5d6fc0000000, direct level 0x5d7240000000, copy level 0x5d7500000000
- factor effect within the cell: on the direct route -0.0450 [-0.1883, 0.0939] ms, on the copy route -0.3421 [-0.3728, -0.3097] ms; change relative to the copy call at home: +1.3 %
- per repetition: direct home 5.369e+08 link read bytes and 4.418e+04 SMMU translation requests; copy home 8.607e+09 link read bytes and 1.311e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 4.418e+04 SMMU translation requests; copy level 8.607e+09 link read bytes and 1.311e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=gather,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4a69c0000000, copy home 0x4a6c40000000, direct level 0x4a6ec0000000, copy level 0x4a7180000000
- factor effect within the cell: on the direct route 0.0244 [0.0197, 0.0306] ms, on the copy route 1.1614 [1.1449, 1.1648] ms; change relative to the copy call at home: -199.9 %
- per repetition: direct home 0 link read bytes and 1.328e+05 SMMU translation requests; copy home 0 link read bytes and 16.81 SMMU translation requests; direct level 0 link read bytes and 1.326e+05 SMMU translation requests; copy level 0 link read bytes and 3.146e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,recopy=pitched,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4e97c0000000, copy home 0x4e9a80000000, direct level 0x4e9d00000000, copy level 0x4e9fc0000000
- factor effect within the cell: on the direct route 0.0127 [0.0060, 0.0154] ms, on the copy route 4.8788 [4.8435, 4.8842] ms; change relative to the copy call at home: -860.8 %
- per repetition: direct home 0 link read bytes and 1.328e+05 SMMU translation requests; copy home 0 link read bytes and 16.81 SMMU translation requests; direct level 0 link read bytes and 1.326e+05 SMMU translation requests; copy level 0 link read bytes and 3.457e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5a1c00000000, copy home 0x5a1ec0000000, direct level 0x5a2140000000, copy level 0x5a2400000000
- factor effect within the cell: on the direct route 0.0256 [0.0206, 0.0358] ms, on the copy route 0.0366 [-0.0012, 0.0624] ms; change relative to the copy call at home: -0.1 %
- per repetition: direct home 0 link read bytes and 1.329e+05 SMMU translation requests; copy home 0 link read bytes and 2.747e+05 SMMU translation requests; direct level 0 link read bytes and 1.326e+05 SMMU translation requests; copy level 0 link read bytes and 2.848e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=9728,host=writes,kernel=k3,pattern=word,placement=cpu,recopy=gather,type=four,vary=sharing,w=0.1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x5aa940000000, copy home 0x5aac40000000, direct level 0x5aaf40000000, copy level 0x5ab240000000
- factor effect within the cell: on the direct route 0.0582 [-0.0061, 0.1032] ms, on the copy route 2.7220 [2.7167, 2.7496] ms; change relative to the copy call at home: -529.6 %
- per repetition: direct home 5.369e+08 link read bytes and 3.597e+07 SMMU translation requests; copy home 0 link read bytes and 2.537 SMMU translation requests; direct level 5.369e+08 link read bytes and 3.598e+07 SMMU translation requests; copy level 1.02e+09 link read bytes and 1.739e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=9728,host=writes,kernel=k3,pattern=word,placement=cpu,type=four,vary=sharing,w=1

- seed 71; every round ran in the drawn order: yes; floor 0.2316 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x567cc0000000, copy home 0x567fc0000000, direct level 0x5682c0000000, copy level 0x5685c0000000
- factor effect within the cell: on the direct route 0.0313 [-0.2740, 0.0856] ms, on the copy route 0.0965 [0.0352, 0.1354] ms; change relative to the copy call at home: -0.3 %
- per repetition: direct home 5.369e+08 link read bytes and 3.598e+07 SMMU translation requests; copy home 1.02e+10 link read bytes and 1.62e+05 SMMU translation requests; direct level 5.369e+08 link read bytes and 3.597e+07 SMMU translation requests; copy level 1.02e+10 link read bytes and 1.621e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=sys,footprint-mib=1024,k=1,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2722 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x442e80000000, copy home 0x442f80000000, direct level 0x443040000000, copy level 0x443100000000
- factor effect within the cell: on the direct route 0.0007 [0.0007, 0.0007] ms, on the copy route -0.0003 [-0.0005, -0.0001] ms; change relative to the copy call at home: +1.8 %
- per repetition: direct home 8.38e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.7 SMMU translation requests; direct level 8.38e+06 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=sys,footprint-mib=1024,k=1,kernel=k2,placement=hbm,type=four,vary=scope,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2722 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x427ac0000000, copy home 0x427c00000000, direct level 0x427cc0000000, copy level 0x427d80000000
- factor effect within the cell: on the direct route 0.0008 [0.0008, 0.0008] ms, on the copy route 0.0001 [-0.0000, 0.0003] ms; change relative to the copy call at home: +1.2 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 134.4 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=sys,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2722 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x434bc0000000, copy home 0x434cc0000000, direct level 0x434d80000000, copy level 0x434e40000000
- factor effect within the cell: on the direct route 0.3638 [0.3629, 0.3650] ms, on the copy route 0.0219 [0.0212, 0.0223] ms; change relative to the copy call at home: +561.3 %
- per repetition: direct home 8.382e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.7 SMMU translation requests; direct level 1.341e+08 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=sys,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=four,vary=scope,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2722 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4be400000000, copy home 0x4be540000000, direct level 0x4be600000000, copy level 0x4be6c0000000
- factor effect within the cell: on the direct route 0.0223 [0.0222, 0.0223] ms, on the copy route 0.0245 [0.0239, 0.0250] ms; change relative to the copy call at home: -3.8 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 134.3 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 135 SMMU translation requests; multiplexed rows voided: 0

### route/at=sys,footprint-mib=1024,k=2,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2722 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x40df40000000, copy home 0x40e000000000, direct level 0x40e0c0000000, copy level 0x40e180000000
- factor effect within the cell: on the direct route 0.0250 [0.0250, 0.0251] ms, on the copy route 0.0024 [0.0023, 0.0026] ms; change relative to the copy call at home: +42.1 %
- per repetition: direct home 8.382e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.7 SMMU translation requests; direct level 1.676e+07 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=sys,footprint-mib=1024,k=2,kernel=k2,placement=hbm,type=four,vary=scope,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2722 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x59d0c0000000, copy home 0x59d180000000, direct level 0x59d240000000, copy level 0x59d300000000
- factor effect within the cell: on the direct route 0.0022 [0.0022, 0.0022] ms, on the copy route 0.0014 [0.0013, 0.0024] ms; change relative to the copy call at home: +1.7 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 134.2 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=sys,footprint-mib=1024,k=4,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2722 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x414100000000, copy home 0x414200000000, direct level 0x4142c0000000, copy level 0x414380000000
- factor effect within the cell: on the direct route 0.0740 [0.0739, 0.0741] ms, on the copy route 0.0048 [0.0045, 0.0051] ms; change relative to the copy call at home: +125.0 %
- per repetition: direct home 8.382e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.7 SMMU translation requests; direct level 3.352e+07 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=sys,footprint-mib=1024,k=4,kernel=k2,placement=hbm,type=four,vary=scope,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2722 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x4ff380000000, copy home 0x4ff480000000, direct level 0x4ff540000000, copy level 0x4ff600000000
- factor effect within the cell: on the direct route 0.0051 [0.0051, 0.0051] ms, on the copy route 0.0085 [0.0083, 0.0089] ms; change relative to the copy call at home: -6.8 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 134.3 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 134.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=sys,footprint-mib=1024,k=64,kernel=k2,placement=cpu,type=four,vary=scope,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2722 ms; stopped on target: yes, cap hit: no
- home at placement cpu, level at placement cpu; buffers: direct home 0x4614c0000000, copy home 0x461580000000, direct level 0x461640000000, copy level 0x461700000000
- factor effect within the cell: on the direct route 1.5310 [1.5226, 1.5357] ms, on the copy route 0.0862 [0.0855, 0.0866] ms; change relative to the copy call at home: +1687.9 %
- per repetition: direct home 8.382e+06 link read bytes and 0 SMMU translation requests; copy home 8.38e+06 link read bytes and 132.7 SMMU translation requests; direct level 5.363e+08 link read bytes and 0 SMMU translation requests; copy level 8.38e+06 link read bytes and 132.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=sys,footprint-mib=1024,k=64,kernel=k2,placement=hbm,type=four,vary=scope,working-set-mib=8

- seed 71; every round ran in the drawn order: yes; floor 0.2722 ms; stopped on target: yes, cap hit: no
- home at placement hbm, level at placement hbm; buffers: direct home 0x5ad740000000, copy home 0x5ad800000000, direct level 0x5ad8c0000000, copy level 0x5ad980000000
- factor effect within the cell: on the direct route 0.0893 [0.0893, 0.0894] ms, on the copy route 0.0866 [0.0865, 0.0871] ms; change relative to the copy call at home: +3.2 %
- per repetition: direct home 0 link read bytes and 0 SMMU translation requests; copy home 0 link read bytes and 135.1 SMMU translation requests; direct level 0 link read bytes and 0 SMMU translation requests; copy level 0 link read bytes and 137.6 SMMU translation requests; multiplexed rows voided: 0

