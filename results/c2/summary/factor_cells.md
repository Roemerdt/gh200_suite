# Factor cells: the direct route at a level of one factor against its home level, recomputed from raw rows

Times are per pass in ms. The factor effect on direct access is level minus home within a repeat, as median with its 95 % rank interval; a positive value means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | level | home ms | level ms | effect ms [interval] | relative to home | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=k,working-set-mib=32 | k | 1 | 1.5112 | 0.0990 | -1.4122 [-1.4127, -1.4113] | -93.4 % | 10 | yes | pass |
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0377 | 0.3738 | 0.3362 [0.3357, 0.3363] | +892.1 % | 10 | yes | pass |
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=k,working-set-mib=32 | k | 1 | 0.0980 | 0.0175 | -0.0805 [-0.0806, -0.0804] | -82.2 % | 10 | yes | pass |
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0160 | 0.0301 | 0.0141 [0.0141, 0.0141] | +88.2 % | 10 | yes | pass |
| at=1,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sweeps | sweeps | 1 | 26.5282 | 3.2745 | -23.2503 [-23.2830, -23.2085] | -87.6 % | 10 | yes | pass |
| at=1,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sweeps | sweeps | 1 | 3.2712 | 0.3956 | -2.8755 [-2.8814, -2.8697] | -87.9 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 45.9228 | 2.7503 | -43.1714 [-43.2051, -43.1548] | -94.0 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 5.6897 | 0.2986 | -5.3913 [-5.4042, -5.3778] | -94.8 % | 20 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 68.3240 | 2.7756 | -65.5481 [-65.5606, -65.5299] | -95.9 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 9.4734 | 0.2979 | -9.1756 [-9.3030, -9.1162] | -96.9 % | 30 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 0.7307 | 2.9131 | 2.1823 [2.1820, 2.1827] | +298.7 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 0.0788 | 0.2980 | 0.2192 [0.2191, 0.2193] | +278.2 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 90.5113 | 2.7470 | -87.7644 [-87.8025, -87.7404] | -97.0 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 15.0108 | 0.2990 | -14.7118 [-14.8415, -14.6357] | -98.0 % | 70 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 11.6975 | 2.8135 | -8.8840 [-8.8876, -8.8809] | -75.9 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 1.1770 | 0.2975 | -0.8795 [-0.8797, -0.8788] | -74.7 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 23.2423 | 2.7523 | -20.4879 [-20.5212, -20.4850] | -88.1 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 2.3413 | 0.2997 | -2.0415 [-2.0433, -2.0399] | -87.2 % | 10 | yes | pass |
| at=1024,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=working-set,working-set-mib=32 | working-set | 1024 | 1.4963 | 47.1032 | 45.6068 [45.5960, 45.6289] | +3048.0 % | 10 | yes | pass |
| at=1024,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=working-set,working-set-mib=32 | working-set | 1024 | 0.0995 | 5.1635 | 5.0639 [5.0625, 5.0684] | +5089.8 % | 10 | yes | pass |
| at=1024,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint | footprint | 1024 | 0.0804 | 0.8185 | 0.7381 [0.7366, 0.7391] | +917.7 % | 10 | yes | pass |
| at=1024,footprint-mib=16384,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 483.2291 | 28.3830 | -454.8380 [-454.9842, -454.7666] | -94.1 % | 10 | yes | pass |
| at=1024,footprint-mib=16384,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 32.0719 | 1.2748 | -30.7970 [-30.8048, -30.7890] | -96.0 % | 10 | yes | pass |
| at=1024,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 432.8426 | 5.3606 | -427.4893 [-427.5759, -427.3311] | -98.8 % | 10 | yes | pass |
| at=1024,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 425.8689 | 0.4675 | -425.4015 [-425.5225, -425.2677] | -99.9 % | 10 | yes | pass |
| at=1024,footprint-mib=24576,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 752.0916 | 28.2632 | -723.8073 [-723.8702, -723.7401] | -96.2 % | 10 | yes | pass |
| at=1024,footprint-mib=24576,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 597.4012 | 5.3481 | -592.0537 [-592.1607, -591.9746] | -99.1 % | 10 | yes | pass |
| at=1024,footprint-mib=24576,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 590.1942 | 0.4672 | -589.7270 [-589.8229, -589.5818] | -99.9 % | 10 | yes | pass |
| at=1024,footprint-mib=256,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 7.3354 | 30.8397 | 23.5031 [23.4778, 23.5246] | +320.4 % | 10 | yes | pass |
| at=1024,footprint-mib=256,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 0.2119 | 1.2718 | 1.0600 [1.0587, 1.0617] | +500.3 % | 10 | yes | pass |
| at=1024,footprint-mib=256,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 5.3635 | 5.3694 | 0.0061 [0.0056, 0.0064] | +0.1 % | 20 | yes | pass |
| at=1024,footprint-mib=256,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 0.4276 | 0.4655 | 0.0380 [0.0377, 0.0382] | +8.9 % | 10 | yes | pass |
| at=1024,footprint-mib=256,kernel=k6,placement=cpu,type=factor,update=atomic,vary=footprint | footprint | 1024 | 1.5030 | 6.0195 | 4.5167 [4.5119, 4.5220] | +300.5 % | 10 | yes | pass |
| at=1024,footprint-mib=256,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint | footprint | 1024 | 0.2046 | 0.8149 | 0.6103 [0.6095, 0.6117] | +298.3 % | 10 | yes | pass |
| at=1024,footprint-mib=32768,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 971.5930 | 28.4066 | -943.1878 [-943.2278, -942.8709] | -97.1 % | 10 | yes | pass |
| at=1024,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 683.8642 | 5.3467 | -678.5180 [-678.7459, -678.4279] | -99.2 % | 10 | yes | pass |
| at=1024,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 678.5163 | 0.4678 | -678.0484 [-678.2497, -677.9310] | -99.9 % | 10 | yes | pass |
| at=1024,footprint-mib=4096,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 124.0021 | 28.5103 | -95.4969 [-95.5725, -95.4340] | -77.0 % | 10 | yes | pass |
| at=1024,footprint-mib=4096,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 7.0813 | 1.2705 | -5.8096 [-5.8136, -5.8057] | -82.0 % | 10 | yes | pass |
| at=1024,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 5.5749 | 5.3445 | -0.2306 [-0.2454, -0.2057] | -4.1 % | 10 | yes | pass |
| at=1024,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 5.1215 | 0.4654 | -4.6559 [-4.6586, -4.6540] | -90.9 % | 10 | yes | pass |
| at=1024,footprint-mib=4096,kernel=k6,placement=cpu,type=factor,update=atomic,vary=footprint | footprint | 1024 | 24.1309 | 5.8858 | -18.2460 [-18.2760, -18.2158] | -75.6 % | 10 | yes | pass |
| at=1024,footprint-mib=4096,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint | footprint | 1024 | 3.2688 | 0.8181 | -2.4511 [-2.4529, -2.4493] | -75.0 % | 10 | yes | pass |
| at=1024,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=factor,vary=keys | keys | 1024 | 191.3116 | 12.4767 | -178.8342 [-178.8405, -178.8312] | -93.5 % | 10 | yes | pass |
| at=1024,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=factor,vary=keys | keys | 1024 | 12.2943 | 0.7660 | -11.5282 [-11.5289, -11.5275] | -93.8 % | 10 | yes | pass |
| at=1024,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,type=factor,vary=keys | keys | 1024 | 7.8437 | 12.5068 | 4.6625 [4.6576, 4.6672] | +59.4 % | 10 | yes | pass |
| at=1024,footprint-mib=8,kernel=k6,keys=1048576,placement=hbm,type=factor,vary=keys | keys | 1024 | 0.1888 | 0.7663 | 0.5776 [0.5774, 0.5777] | +305.9 % | 10 | yes | pass |
| at=1024,footprint-mib=8192,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 247.6706 | 28.3555 | -219.3062 [-219.3882, -219.2266] | -88.5 % | 10 | yes | pass |
| at=1024,footprint-mib=8192,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 15.0587 | 1.2715 | -13.7862 [-13.7978, -13.7759] | -91.5 % | 10 | yes | pass |
| at=1024,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 7.7831 | 5.3497 | -2.4336 [-2.4360, -2.4314] | -31.3 % | 10 | yes | pass |
| at=1024,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 7.7192 | 0.4672 | -7.2517 [-7.2615, -7.2445] | -93.9 % | 10 | yes | pass |
| at=16,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sweeps | sweeps | 16 | 26.5080 | 46.6631 | 20.1546 [20.1375, 20.2252] | +76.0 % | 10 | yes | pass |
| at=16,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sweeps | sweeps | 16 | 3.2569 | 6.5358 | 3.2792 [3.2697, 3.2865] | +100.7 % | 10 | yes | pass |
| at=1of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 1of10 | 2.9083 | 0.3017 | -2.6065 [-2.6071, -2.6059] | -89.6 % | 10 | yes | pass |
| at=1of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 1of10 | 0.2975 | 0.0379 | -0.2596 [-0.2597, -0.2595] | -87.3 % | 10 | yes | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 1of100 | 2.9050 | 0.0383 | -2.8668 [-2.8672, -2.8663] | -98.7 % | 10 | yes | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 1of100 | 0.2969 | 0.0101 | -0.2868 [-0.2869, -0.2868] | -96.6 % | 10 | yes | pass |
| at=1of1000,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 1of1000 | 2.9061 | 0.0158 | -2.8903 [-2.8907, -2.8897] | -99.5 % | 10 | yes | pass |
| at=1of1000,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 1of1000 | 0.2976 | 0.0079 | -0.2897 [-0.2898, -0.2897] | -97.4 % | 10 | yes | pass |
| at=1of2,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 1of2 | 2.9099 | 1.4687 | -1.4410 [-1.4424, -1.4403] | -49.5 % | 10 | yes | pass |
| at=1of2,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 1of2 | 0.2971 | 0.1593 | -0.1378 [-0.1379, -0.1377] | -46.4 % | 10 | yes | pass |
| at=2,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=k,working-set-mib=32 | k | 2 | 1.4892 | 0.1931 | -1.2961 [-1.2963, -1.2959] | -87.0 % | 10 | yes | pass |
| at=2,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=k,working-set-mib=32 | k | 2 | 0.0971 | 0.0235 | -0.0736 [-0.0737, -0.0734] | -75.8 % | 10 | yes | pass |
| at=2,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sweeps | sweeps | 2 | 26.5641 | 6.1741 | -20.3908 [-20.4119, -20.3174] | -76.8 % | 10 | yes | pass |
| at=2,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sweeps | sweeps | 2 | 3.2649 | 0.8096 | -2.4557 [-2.4576, -2.4527] | -75.2 % | 10 | yes | pass |
| at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=partition | partition | 2g | 432.8668 | 5.8764 | -426.9960 [-427.0524, -426.8647] | -98.6 % | 20 | yes | pass |
| at=2m,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=page-order | page-order | 2m | 5.3805 | 5.3121 | -0.0684 [-0.0701, -0.0678] | -1.3 % | 10 | yes | pass |
| at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 432.8612 | 5.3784 | -427.4830 [-427.6632, -427.3497] | -98.8 % | 10 | yes | pass |
| at=2m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 425.2064 | 2.5106 | -422.6944 [-422.8505, -422.6255] | -99.4 % | 10 | yes | pass |
| at=2m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 685.1075 | 5.4365 | -679.6720 [-679.7424, -679.5933] | -99.2 % | 10 | yes | pass |
| at=2m,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 678.8255 | 4.1745 | -674.6510 [-674.7186, -674.5091] | -99.4 % | 10 | yes | pass |
| at=2m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 5.5317 | 5.3495 | -0.1823 [-0.2034, -0.1682] | -3.3 % | 20 | yes | pass |
| at=2m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 5.1087 | 0.4275 | -4.6813 [-4.6871, -4.6761] | -91.6 % | 10 | yes | pass |
| at=2m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 7.8751 | 5.3592 | -2.5160 [-2.5167, -2.5147] | -31.9 % | 10 | yes | pass |
| at=2m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 7.8235 | 0.4756 | -7.3479 [-7.3528, -7.3453] | -93.9 % | 10 | yes | pass |
| at=3of4,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 3of4 | 2.9047 | 2.2088 | -0.6957 [-0.6968, -0.6951] | -24.0 % | 10 | yes | pass |
| at=3of4,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 3of4 | 0.2984 | 0.2335 | -0.0649 [-0.0651, -0.0647] | -21.8 % | 10 | yes | pass |
| at=4,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=k,working-set-mib=32 | k | 4 | 1.4954 | 0.3774 | -1.1180 [-1.1184, -1.1172] | -74.8 % | 10 | yes | pass |
| at=4,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=k,working-set-mib=32 | k | 4 | 0.0982 | 0.0345 | -0.0637 [-0.0638, -0.0636] | -64.9 % | 10 | yes | pass |
| at=4,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=repeat | repeat | 4 | 6.0447 | 18.0401 | 11.9933 [11.9799, 12.0038] | +198.4 % | 10 | yes | pass |
| at=4,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=repeat | repeat | 4 | 0.8185 | 1.6431 | 0.8247 [0.8213, 0.8261] | +100.8 % | 10 | yes | pass |
| at=4,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sweeps | sweeps | 4 | 26.7343 | 11.9624 | -14.7780 [-14.7870, -14.7529] | -55.3 % | 10 | yes | pass |
| at=4,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sweeps | sweeps | 4 | 3.2383 | 1.6253 | -1.6113 [-1.6190, -1.6083] | -49.8 % | 10 | yes | pass |
| at=512m,footprint-mib=1024,kernel=k3,placement=cpu,type=factor,vary=page-size | page-size | 512m | 5.3699 | 5.3304 | -0.0394 [-0.0404, -0.0386] | -0.7 % | 10 | yes | pass |
| at=512m,footprint-mib=1024,kernel=k3,placement=hbm,type=factor,vary=page-size | page-size | 512m | 0.4657 | 0.4649 | -0.0008 [-0.0009, -0.0008] | -0.2 % | 60 | yes | pass |
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-size | page-size | 512m | 433.3806 | 5.3851 | -427.9956 [-428.1049, -427.9031] | -98.8 % | 10 | yes | pass |
| at=512m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-size | page-size | 512m | 425.2879 | 0.4783 | -424.8096 [-424.9069, -424.5954] | -99.9 % | 10 | yes | pass |
| at=512m,footprint-mib=16384,kernel=k3p,placement=cpu,type=factor,vary=page-size | page-size | 512m | 7.0189 | 0.0992 | -6.9198 [-6.9268, -6.9137] | -98.6 % | 10 | yes | pass |
| at=512m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-size | page-size | 512m | 683.9485 | 5.3904 | -678.5578 [-678.6398, -678.3864] | -99.2 % | 10 | yes | pass |
| at=512m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-size | page-size | 512m | 5.5560 | 5.3701 | -0.1863 [-0.2001, -0.1716] | -3.4 % | 10 | yes | pass |
| at=512m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-size | page-size | 512m | 5.1159 | 0.4753 | -4.6407 [-4.6424, -4.6368] | -90.7 % | 10 | yes | pass |
| at=512m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-size | page-size | 512m | 7.7436 | 5.3794 | -2.3640 [-2.3654, -2.3629] | -30.5 % | 10 | yes | pass |
| at=512m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-size | page-size | 512m | 7.6752 | 0.4772 | -7.1979 [-7.2082, -7.1910] | -93.8 % | 10 | yes | pass |
| at=64,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=k,working-set-mib=32 | k | 64 | 1.4898 | 5.9726 | 4.4821 [4.4793, 4.4848] | +300.9 % | 10 | yes | pass |
| at=64,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=k,working-set-mib=32 | k | 64 | 0.0953 | 0.3440 | 0.2487 [0.2481, 0.2493] | +260.9 % | 10 | yes | pass |
| at=64,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sweeps | sweeps | 64 | 26.0995 | 184.5186 | 158.4187 [158.3946, 158.4598] | +607.0 % | 10 | yes | pass |
| at=64,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sweeps | sweeps | 64 | 3.2580 | 26.2013 | 22.9383 [22.9125, 23.0028] | +704.1 % | 10 | yes | pass |
| at=64k,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=page-order | page-order | 64k | 5.3806 | 5.1737 | -0.2070 [-0.2091, -0.2046] | -3.8 % | 10 | yes | pass |
| at=64k,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 433.5340 | 5.2147 | -428.3222 [-428.6335, -428.2792] | -98.8 % | 10 | yes | pass |
| at=64k,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 426.1056 | 1.6198 | -424.4851 [-424.6058, -424.3293] | -99.6 % | 10 | yes | pass |
| at=64k,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 684.0404 | 5.2654 | -678.7756 [-678.8150, -678.6408] | -99.2 % | 10 | yes | pass |
| at=64k,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 679.7478 | 3.3252 | -676.4185 [-676.5800, -676.2445] | -99.5 % | 10 | yes | pass |
| at=64k,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 5.5691 | 5.1468 | -0.4217 [-0.4348, -0.4049] | -7.6 % | 10 | yes | pass |
| at=64k,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 5.1191 | 0.4125 | -4.7065 [-4.7103, -4.7044] | -91.9 % | 10 | yes | pass |
| at=64k,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 7.8862 | 5.1772 | -2.7085 [-2.7097, -2.7065] | -34.3 % | 10 | yes | pass |
| at=64k,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 7.8244 | 0.4445 | -7.3798 [-7.3910, -7.3731] | -94.3 % | 10 | yes | pass |
| at=8,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=working-set,working-set-mib=32 | working-set | 8 | 1.4989 | 0.0378 | -1.4611 [-1.4617, -1.4607] | -97.5 % | 10 | yes | pass |
| at=8,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=working-set,working-set-mib=32 | working-set | 8 | 0.0970 | 0.0162 | -0.0808 [-0.0809, -0.0808] | -83.3 % | 10 | yes | pass |
| at=9of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 9of10 | 2.9059 | 2.6589 | -0.2471 [-0.2477, -0.2460] | -8.5 % | 10 | yes | pass |
| at=9of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 9of10 | 0.2990 | 0.2751 | -0.0240 [-0.0242, -0.0239] | -8.0 % | 10 | yes | pass |
| at=hbm,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=placement | placement | hbm | 10.2133 | 10.2144 | 0.0009 [-0.0044, 0.0039] | +0.0 % | 100 | no | pass |
| at=hbm,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=plain,vary=placement | placement | hbm | 2.3752 | 2.3747 | -0.0003 [-0.0013, 0.0011] | -0.0 % | 100 | no | pass |
| at=hbm,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=placement | placement | hbm | 12.9165 | 18.0113 | 5.1069 [5.0032, 5.2286] | +39.5 % | 10 | yes | pass |
| at=hbm,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=plain,vary=placement | placement | hbm | 2.3774 | 2.7269 | 0.3447 [0.3393, 0.3614] | +14.5 % | 10 | yes | pass |
| at=line,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=layout | layout | line | 6.0398 | 3.4956 | -2.5438 [-2.5532, -2.5374] | -42.1 % | 10 | yes | pass |
| at=line,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=layout | layout | line | 0.8157 | 0.3388 | -0.4768 [-0.4776, -0.4761] | -58.5 % | 10 | yes | pass |
| at=none,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=tiling | tiling | none | 26.0780 | 37.6053 | 11.5316 [11.3715, 11.6199] | +44.2 % | 10 | yes | pass |
| at=none,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=tiling | tiling | none | 3.2508 | 2.7490 | -0.5019 [-0.5078, -0.4996] | -15.4 % | 10 | yes | pass |
| at=off512m,footprint-mib=1024,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3297 | 5.3299 | 0.0000 [-0.0001, 0.0003] | +0.0 % | 100 | no | pass |
| at=off512m,footprint-mib=1024,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4647 | 0.4647 | 0.0000 [-0.0001, 0.0001] | +0.0 % | 100 | no | pass |
| at=off512m,footprint-mib=1024,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3685 | 5.3691 | 0.0007 [0.0006, 0.0009] | +0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=1024,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4649 | 0.4652 | 0.0003 [0.0003, 0.0004] | +0.1 % | 100 | yes | pass |
| at=off512m,footprint-mib=11520,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3781 | 5.3778 | -0.0003 [-0.0004, -0.0001] | -0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=11520,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 240.4119 | 240.2866 | -0.1261 [-0.1637, -0.1093] | -0.1 % | 100 | yes | pass |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3791 | 5.3790 | -0.0002 [-0.0003, 0.0000] | -0.0 % | 100 | no | pass |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4772 | 0.4775 | 0.0003 [0.0002, 0.0003] | +0.1 % | 100 | yes | pass |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 279.3716 | 279.4509 | 0.0755 [0.0417, 0.1201] | +0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | alignment | off512m | 282.8738 | 284.9382 | 2.0747 [2.0073, 2.1277] | +0.7 % | 20 | yes | pass |
| at=off512m,footprint-mib=1536,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3482 | 5.3482 | -0.0001 [-0.0003, 0.0002] | -0.0 % | 100 | no | pass |
| at=off512m,footprint-mib=1536,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3710 | 5.3695 | -0.0015 [-0.0017, -0.0014] | -0.0 % | 70 | yes | pass |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3802 | 5.3796 | -0.0007 [-0.0008, -0.0004] | -0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4777 | 0.4776 | -0.0000 [-0.0002, 0.0001] | -0.0 % | 100 | no | pass |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 433.5923 | 433.5391 | -0.0535 [-0.0923, -0.0111] | -0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | alignment | off512m | 425.2457 | 425.1764 | -0.0663 [-0.1514, -0.0105] | -0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=2048,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3572 | 5.3566 | -0.0006 [-0.0007, -0.0005] | -0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=2048,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3720 | 5.3688 | -0.0032 [-0.0036, -0.0029] | -0.1 % | 20 | yes | pass |
| at=off512m,footprint-mib=24576,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3812 | 5.3810 | -0.0002 [-0.0003, -0.0000] | -0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=24576,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 598.6233 | 598.6570 | 0.0515 [0.0180, 0.0764] | +0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=256,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.1755 | 5.1753 | -0.0000 [-0.0002, 0.0001] | -0.0 % | 100 | no | pass |
| at=off512m,footprint-mib=256,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4243 | 0.4246 | 0.0003 [0.0003, 0.0003] | +0.1 % | 100 | yes | pass |
| at=off512m,footprint-mib=256,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3655 | 5.3627 | -0.0028 [-0.0030, -0.0025] | -0.1 % | 40 | yes | pass |
| at=off512m,footprint-mib=256,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4261 | 0.4255 | -0.0006 [-0.0006, -0.0005] | -0.1 % | 90 | yes | pass |
| at=off512m,footprint-mib=32768,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3819 | 5.3819 | -0.0000 [-0.0002, 0.0003] | -0.0 % | 100 | no | pass |
| at=off512m,footprint-mib=32768,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 685.2659 | 685.3791 | 0.0994 [0.0646, 0.1301] | +0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3695 | 5.3702 | 0.0007 [0.0005, 0.0010] | +0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4759 | 0.4751 | -0.0008 [-0.0008, -0.0007] | -0.2 % | 60 | yes | pass |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.5393 | 5.5272 | -0.0105 [-0.0167, -0.0049] | -0.2 % | 100 | yes | pass |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | alignment | off512m | 5.1171 | 5.1128 | -0.0051 [-0.0060, -0.0040] | -0.1 % | 100 | yes | pass |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3769 | 5.3763 | -0.0005 [-0.0006, -0.0003] | -0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4765 | 0.4776 | 0.0011 [0.0009, 0.0011] | +0.2 % | 40 | yes | pass |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 7.8862 | 48.5821 | 40.6971 [40.6554, 40.7575] | +516.1 % | 10 | yes | pass |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | alignment | off512m | 7.8246 | 43.1573 | 35.3338 [35.2887, 35.3994] | +451.6 % | 10 | yes | pass |
| at=off512m,footprint-mib=9728,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3780 | 5.3780 | 0.0000 [-0.0002, 0.0001] | +0.0 % | 100 | no | pass |
| at=off512m,footprint-mib=9728,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 128.4634 | 128.4987 | 0.0349 [0.0033, 0.0587] | +0.0 % | 100 | yes | pass |
| at=plain,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | plain | 10.2147 | 2.3679 | -7.8427 [-7.8609, -7.8269] | -76.8 % | 10 | yes | pass |
| at=plain,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | plain | 10.0406 | 2.3545 | -7.6887 [-7.7180, -7.6709] | -76.6 % | 10 | yes | pass |
| at=plain,footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | plain | 10.1449 | 2.3740 | -7.7706 [-7.7924, -7.7466] | -76.6 % | 10 | yes | pass |
| at=plain,footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | plain | 10.0567 | 2.3645 | -7.6969 [-7.7299, -7.6810] | -76.5 % | 10 | yes | pass |
| at=plain,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | plain | 6.0361 | 6.0170 | -0.0199 [-0.0213, -0.0175] | -0.3 % | 80 | yes | pass |
| at=plain,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | plain | 0.8161 | 0.7682 | -0.0476 [-0.0490, -0.0469] | -5.8 % | 10 | yes | pass |
| at=plain,footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | plain | 10.5892 | 2.3660 | -8.2214 [-8.2919, -8.1864] | -77.6 % | 10 | yes | pass |
| at=plain,footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | plain | 10.6576 | 2.3300 | -8.3182 [-8.3936, -8.2967] | -78.0 % | 10 | yes | pass |
| at=plain,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | plain | 0.0783 | 0.0786 | 0.0003 [0.0002, 0.0003] | +0.3 % | 20 | yes | pass |
| at=plain,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | plain | 12.8390 | 2.3468 | -10.4987 [-10.5985, -10.3842] | -81.8 % | 40 | yes | pass |
| at=plain,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | plain | 17.8030 | 2.7360 | -15.0681 [-15.1962, -14.9522] | -84.6 % | 10 | yes | pass |
| at=returned,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | returned | 10.2417 | 42.1104 | 31.8707 [31.6526, 31.9904] | +311.2 % | 10 | yes | pass |
| at=returned,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | returned | 10.2814 | 40.5368 | 30.2532 [30.1101, 30.4959] | +294.3 % | 40 | yes | pass |
| at=returned,footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | returned | 10.2579 | 43.6254 | 33.3624 [32.9740, 33.6720] | +325.2 % | 10 | yes | pass |
| at=returned,footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | returned | 10.2060 | 41.5240 | 31.3219 [31.1790, 31.5131] | +306.9 % | 40 | yes | pass |
| at=returned,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | returned | 6.0413 | 6.0528 | 0.0143 [0.0125, 0.0151] | +0.2 % | 50 | yes | pass |
| at=returned,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | returned | 0.8175 | 0.8977 | 0.0802 [0.0792, 0.0806] | +9.8 % | 10 | yes | pass |
| at=returned,footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | returned | 10.6495 | 41.4240 | 30.8085 [30.5801, 30.9459] | +289.3 % | 20 | yes | pass |
| at=returned,footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | returned | 10.6121 | 40.4595 | 29.8199 [27.9037, 30.0313] | +281.0 % | 100 | yes | pass |
| at=returned,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | returned | 0.0760 | 0.1349 | 0.0589 [0.0588, 0.0589] | +77.4 % | 10 | yes | pass |
| at=returned,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | returned | 13.0504 | 47.1562 | 34.0103 [33.7551, 34.2694] | +260.6 % | 20 | yes | pass |
| at=returned,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | returned | 17.7223 | 46.6223 | 29.0365 [28.6692, 29.8301] | +163.8 % | 100 | yes | pass |
| at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=generator | generator | rmat | 30.9488 | 190.0891 | 159.1483 [159.0533, 159.2026] | +514.2 % | 10 | yes | pass |
| at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=generator | generator | rmat | 1.2725 | 65.4251 | 64.1530 [63.6451, 64.6688] | +5041.3 % | 10 | yes | pass |
| at=rmat,footprint-mib=8192,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=generator | generator | rmat | 248.3019 | 993.2997 | 744.9576 [744.8272, 745.0730] | +300.0 % | 10 | yes | pass |
| at=rmat,footprint-mib=8192,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=generator | generator | rmat | 15.1198 | 395.8281 | 380.7045 [378.1939, 383.3713] | +2517.9 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing | sharing | shared | 0.0202 | 0.0210 | 0.0008 [0.0007, 0.0008] | +3.8 % | 30 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0204 | 0.0204 | -0.0000 [-0.0001, -0.0000] | -0.2 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0203 | 0.0203 | 0.0000 [-0.0000, 0.0001] | +0.1 % | 100 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing | sharing | shared | 0.0201 | 0.0206 | 0.0006 [0.0005, 0.0006] | +2.7 % | 30 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0200 | 0.0206 | 0.0005 [0.0005, 0.0005] | +2.5 % | 30 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0200 | 0.0201 | 0.0001 [0.0000, 0.0001] | +0.3 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing | sharing | shared | 0.1919 | 0.1913 | -0.0006 [-0.0007, -0.0005] | -0.3 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 0.1909 | 0.1908 | -0.0001 [-0.0002, -0.0001] | -0.1 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing | sharing | shared | 0.1897 | 0.1885 | -0.0012 [-0.0013, -0.0011] | -0.6 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0341 | 0.1003 | 0.0663 [0.0652, 0.0667] | +194.3 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0338 | 0.0349 | 0.0011 [0.0010, 0.0012] | +3.3 % | 40 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0336 | 0.0335 | -0.0001 [-0.0002, -0.0000] | -0.3 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing | sharing | shared | 0.1912 | 0.1917 | 0.0005 [0.0004, 0.0006] | +0.3 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 0.1904 | 0.3820 | 0.1916 [0.1914, 0.1918] | +100.7 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing | sharing | shared | 0.1905 | 0.1912 | 0.0007 [0.0006, 0.0007] | +0.3 % | 70 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0382 | 0.1077 | 0.0695 [0.0694, 0.0700] | +182.0 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0351 | 0.1776 | 0.1425 [0.1422, 0.1427] | +405.7 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0367 | 0.0354 | -0.0014 [-0.0015, -0.0013] | -3.9 % | 30 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0143 | 0.0224 | 0.0080 [0.0080, 0.0081] | +56.2 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0143 | 0.0147 | 0.0004 [0.0003, 0.0004] | +2.6 % | 90 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0143 | 0.0144 | 0.0001 [0.0001, 0.0002] | +0.9 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0145 | 0.0231 | 0.0087 [0.0085, 0.0090] | +59.7 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0146 | 0.0291 | 0.0146 [0.0143, 0.0146] | +100.2 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0144 | 0.0147 | 0.0003 [0.0003, 0.0003] | +2.1 % | 70 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0509 | 0.1856 | 0.1348 [0.1342, 0.1353] | +264.7 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0453 | 0.0456 | 0.0003 [0.0002, 0.0004] | +0.6 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0444 | 0.0454 | 0.0010 [0.0009, 0.0011] | +2.3 % | 60 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0539 | 0.1886 | 0.1346 [0.1336, 0.1353] | +249.8 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0492 | 0.2596 | 0.2102 [0.2096, 0.2107] | +427.1 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0490 | 0.0483 | -0.0007 [-0.0008, -0.0007] | -1.5 % | 90 | yes | pass |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=factor,vary=sharing | sharing | shared | 30.6976 | 30.4807 | -0.2205 [-0.2341, -0.1959] | -0.7 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=factor,vary=sharing | sharing | shared | 1.2773 | 1.2763 | -0.0017 [-0.0025, -0.0011] | -0.1 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0441 | 0.0436 | -0.0005 [-0.0005, -0.0005] | -1.2 % | 90 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0441 | 0.0438 | -0.0002 [-0.0003, -0.0001] | -0.5 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0437 | 0.0435 | -0.0002 [-0.0002, -0.0001] | -0.4 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0445 | 0.0439 | -0.0005 [-0.0006, -0.0004] | -1.2 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0444 | 0.0634 | 0.0191 [0.0190, 0.0192] | +43.1 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0437 | 0.0436 | -0.0001 [-0.0002, -0.0001] | -0.2 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32 | sharing | shared | 1.4939 | 1.5062 | 0.0124 [0.0114, 0.0132] | +0.8 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8 | sharing | shared | 0.0446 | 0.0446 | 0.0000 [-0.0000, 0.0001] | +0.1 % | 100 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 1.5118 | 1.5203 | 0.0086 [0.0081, 0.0091] | +0.6 % | 30 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0512 | 0.0517 | 0.0005 [0.0003, 0.0006] | +0.9 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 1.5203 | 1.5183 | -0.0019 [-0.0021, -0.0016] | -0.1 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8 | sharing | shared | 0.0549 | 0.0548 | -0.0001 [-0.0004, 0.0001] | -0.3 % | 100 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32 | sharing | shared | 0.1046 | 0.1053 | 0.0008 [0.0006, 0.0010] | +0.8 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.1171 | 0.1130 | -0.0041 [-0.0044, -0.0037] | -3.5 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.1082 | 0.1058 | -0.0025 [-0.0028, -0.0024] | -2.3 % | 90 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32 | sharing | shared | 1.4919 | 1.5115 | 0.0200 [0.0190, 0.0207] | +1.3 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8 | sharing | shared | 0.0445 | 0.0445 | 0.0000 [-0.0000, 0.0001] | +0.1 % | 100 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 1.4990 | 1.5097 | 0.0104 [0.0094, 0.0110] | +0.7 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0518 | 0.0514 | -0.0005 [-0.0007, -0.0003] | -1.0 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 1.5210 | 1.5201 | -0.0009 [-0.0012, -0.0007] | -0.1 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8 | sharing | shared | 0.0538 | 0.0546 | 0.0008 [0.0006, 0.0012] | +1.4 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32 | sharing | shared | 0.1067 | 0.1071 | 0.0003 [0.0003, 0.0004] | +0.3 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.1152 | 0.1146 | -0.0006 [-0.0009, -0.0003] | -0.5 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.1288 | 0.1337 | 0.0052 [0.0046, 0.0056] | +4.0 % | 90 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01 | sharing | shared | 5.4362 | 5.4338 | -0.0025 [-0.0030, -0.0019] | -0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1 | sharing | shared | 5.4215 | 5.4182 | -0.0092 [-0.0171, -0.0024] | -0.2 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1 | sharing | shared | 5.3987 | 5.3924 | -0.0062 [-0.0069, -0.0057] | -0.1 % | 70 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01 | sharing | shared | 5.4201 | 5.4355 | 0.0149 [0.0018, 0.0157] | +0.3 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1 | sharing | shared | 5.4382 | 5.4340 | -0.0041 [-0.0048, -0.0036] | -0.1 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1 | sharing | shared | 5.3827 | 5.3797 | -0.0030 [-0.0034, -0.0026] | -0.1 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 7.2582 | 7.2224 | -0.0363 [-0.0389, -0.0292] | -0.5 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 7.2496 | 7.2118 | -0.0373 [-0.0417, -0.0324] | -0.5 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01 | sharing | shared | 432.9060 | 432.9482 | 0.0417 [-0.0072, 0.0855] | +0.0 % | 100 | no | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1 | sharing | shared | 433.4805 | 433.5502 | 0.0829 [0.0042, 0.1224] | +0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1 | sharing | shared | 433.5500 | 433.5645 | 0.0267 [-0.0121, 0.0799] | +0.0 % | 100 | no | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01 | sharing | shared | 432.8690 | 432.9127 | 0.0288 [-0.0026, 0.0733] | +0.0 % | 100 | no | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1 | sharing | shared | 433.5258 | 433.5504 | 0.0189 [-0.0212, 0.0749] | +0.0 % | 100 | no | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1 | sharing | shared | 433.5016 | 433.5430 | 0.0308 [0.0021, 0.0676] | +0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing | sharing | shared | 26.6560 | 23.6032 | -3.0624 [-3.0808, -3.0296] | -11.5 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing | sharing | shared | 3.2723 | 3.2762 | 0.0035 [0.0019, 0.0058] | +0.1 % | 100 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | sharing | shared | 26.3396 | 23.3332 | -3.0071 [-3.0263, -2.9767] | -11.4 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | sharing | shared | 26.6105 | 23.5614 | -3.0473 [-3.0938, -3.0229] | -11.5 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | sharing | shared | 26.5217 | 23.4339 | -3.0872 [-3.1154, -3.0468] | -11.6 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | sharing | shared | 3.5440 | 3.5714 | 0.0272 [0.0258, 0.0310] | +0.8 % | 50 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | sharing | shared | 3.5393 | 3.4800 | -0.0603 [-0.0674, -0.0566] | -1.7 % | 20 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | sharing | shared | 3.4468 | 3.5563 | 0.1092 [0.1040, 0.1133] | +3.2 % | 20 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | sharing | shared | 26.6423 | 23.4367 | -3.2065 [-3.2089, -3.1757] | -12.0 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | sharing | shared | 26.6101 | 23.5558 | -3.0541 [-3.0827, -3.0307] | -11.5 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | sharing | shared | 26.1811 | 23.4506 | -2.7319 [-2.7725, -2.6800] | -10.4 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | sharing | shared | 3.5635 | 3.6009 | 0.0370 [0.0349, 0.0413] | +1.0 % | 50 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | sharing | shared | 3.4473 | 3.5877 | 0.1406 [0.1321, 0.1477] | +4.1 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | sharing | shared | 3.5470 | 3.4959 | -0.0523 [-0.0560, -0.0481] | -1.5 % | 20 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01 | sharing | shared | 8.0910 | 8.1022 | 0.0120 [0.0095, 0.0136] | +0.1 % | 100 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1 | sharing | shared | 8.0811 | 8.1008 | 0.0187 [0.0178, 0.0208] | +0.2 % | 70 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=1 | sharing | shared | 8.0881 | 8.0841 | -0.0040 [-0.0076, -0.0021] | -0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01 | sharing | shared | 8.0740 | 8.0963 | 0.0228 [0.0201, 0.0246] | +0.3 % | 60 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1 | sharing | shared | 8.0803 | 8.0940 | 0.0132 [0.0116, 0.0154] | +0.2 % | 100 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=1 | sharing | shared | 8.0879 | 8.1055 | 0.0165 [0.0137, 0.0182] | +0.2 % | 100 | yes | pass |
| at=sorted,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=index-order | index-order | sorted | 433.4936 | 5.0492 | -428.4383 [-428.5497, -428.3564] | -98.8 % | 10 | yes | pass |
| at=stadd,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | stadd | 10.2305 | 7.9177 | -2.3094 [-2.3215, -2.3008] | -22.6 % | 10 | yes | pass |
| at=stadd,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | stadd | 10.1889 | 7.9886 | -2.2005 [-2.2160, -2.1845] | -21.6 % | 10 | yes | pass |
| at=stadd,footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | stadd | 10.0891 | 7.9568 | -2.1322 [-2.1520, -2.0832] | -21.1 % | 10 | yes | pass |
| at=stadd,footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | stadd | 10.2195 | 8.0819 | -2.1407 [-2.1499, -2.1279] | -20.9 % | 10 | yes | pass |
| at=stadd,footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | stadd | 10.7787 | 7.9929 | -2.7920 [-2.8673, -2.6605] | -25.9 % | 10 | yes | pass |
| at=stadd,footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | stadd | 10.8488 | 8.0540 | -2.7877 [-2.8791, -2.7543] | -25.7 % | 10 | yes | pass |
| at=stadd,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | stadd | 13.2259 | 9.1945 | -4.0431 [-4.1359, -3.9367] | -30.6 % | 20 | yes | pass |
| at=stadd,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | stadd | 17.4227 | 11.4801 | -5.8906 [-5.9540, -5.8282] | -33.8 % | 30 | yes | pass |
| at=tiles,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=tiling,working-set-mib=8 | tiling | tiles | 0.0378 | 0.0367 | -0.0011 [-0.0011, -0.0011] | -2.8 % | 10 | yes | pass |
| at=tiles,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=tiling,working-set-mib=8 | tiling | tiles | 0.0161 | 0.0155 | -0.0007 [-0.0007, -0.0007] | -4.1 % | 10 | yes | pass |
| at=warp,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,type=factor,vary=strategy | strategy | warp | 8.7266 | 8.5838 | -0.1440 [-0.1518, -0.1374] | -1.7 % | 10 | yes | pass |
| at=warp,footprint-mib=8,kernel=k6,keys=1048576,placement=hbm,type=factor,vary=strategy | strategy | warp | 0.1787 | 0.2862 | 0.1075 [0.1074, 0.1078] | +60.2 % | 10 | yes | pass |
| at=warp,footprint-mib=8,kernel=k6,keys=4096,placement=cpu,type=factor,vary=strategy | strategy | warp | 6.2072 | 6.1841 | -0.0222 [-0.0251, -0.0192] | -0.4 % | 100 | yes | pass |
| at=warp,footprint-mib=8,kernel=k6,keys=4096,placement=hbm,type=factor,vary=strategy | strategy | warp | 0.2663 | 0.2821 | 0.0158 [0.0158, 0.0159] | +5.9 % | 10 | yes | pass |
| at=warp,footprint-mib=8,kernel=k6,keys=65536,placement=cpu,type=factor,vary=strategy | strategy | warp | 4.0309 | 4.0268 | -0.0041 [-0.0045, -0.0038] | -0.1 % | 30 | yes | pass |
| at=warp,footprint-mib=8,kernel=k6,keys=65536,placement=hbm,type=factor,vary=strategy | strategy | warp | 0.2067 | 0.2860 | 0.0792 [0.0792, 0.0798] | +38.3 % | 10 | yes | pass |

## Host phases

The CPU phase before every pass, timed on the CPU clock (ms per pass), and the state check's median load latency on the preparing core after the phase (ns per sampled load), per variant.

| cell | home CPU ms | home state ns | level CPU ms | level state ns |
|---|---|---|---|---|
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing | 0.3350 | 7.5 | 0.3307 | 13.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | 0.2798 | 16.2 | 0.2799 | 35.6 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing | 0.3099 | 188.8 | 0.3113 | 71.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing | 0.3287 | 6.5 | 0.3276 | 15.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | 0.2885 | 8.8 | 0.2809 | 26.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing | 0.3160 | 200.6 | 0.3044 | 76.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing | 15.5102 | 69.4 | 15.2334 | 108.8 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | 7.7839 | 75.2 | 6.9834 | 218.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing | 11.0174 | 205.2 | 11.0420 | 213.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | 16.1095 | 138.2 | 19.8539 | 190.6 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | 7.9112 | 104.9 | 8.5059 | 402.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | 12.1600 | 520.4 | 11.8915 | 423.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing | 14.4821 | 43.6 | 14.7239 | 46.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | 7.2286 | 47.5 | 6.9806 | 67.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing | 10.6533 | 222.0 | 10.6628 | 212.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | 15.6057 | 83.6 | 19.6305 | 120.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | 8.5359 | 95.2 | 8.5319 | 113.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | 12.2334 | 455.2 | 11.8538 | 402.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | 2.3299 | 64.0 | 2.7680 | 69.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | 1.5075 | 61.2 | 1.4941 | 344.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | 1.9889 | 378.8 | 1.9763 | 378.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | 2.2916 | 87.1 | 2.7366 | 91.8 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | 1.7369 | 73.2 | 1.5020 | 69.8 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | 1.9143 | 367.1 | 1.9233 | 363.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | 29.3138 | 300.0 | 30.2323 | 277.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | 12.7240 | 297.9 | 12.9061 | 445.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | 17.9313 | 520.9 | 17.6944 | 460.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | 26.8983 | 132.8 | 30.1169 | 132.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | 12.4530 | 218.4 | 12.9634 | 233.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | 18.0869 | 485.9 | 17.7910 | 447.5 |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=factor,vary=sharing | 1.8410 | - | 1.6576 | - |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=factor,vary=sharing | 2.6219 | - | 3.6954 | - |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8 | 2.0570 | 45.6 | 2.0607 | 48.2 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8 | 1.0706 | 179.8 | 1.0653 | 182.5 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8 | 1.5659 | 196.6 | 1.5646 | 194.9 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8 | 2.0184 | 67.1 | 2.0192 | 63.0 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8 | 1.0773 | 68.0 | 1.0741 | 69.1 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8 | 1.5164 | 196.0 | 1.5163 | 192.8 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32 | 0.6368 | 72.0 | 0.6470 | 116.0 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8 | 0.6344 | 58.8 | 0.6373 | 101.4 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32 | 4.8599 | 121.2 | 4.9054 | 165.6 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8 | 4.6211 | 150.0 | 4.6385 | 192.2 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32 | 70.9795 | 199.2 | 71.1009 | 329.1 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8 | 71.5348 | 216.8 | 71.1764 | 288.9 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32 | 1.0146 | 72.6 | 1.0177 | 125.6 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32 | 5.9013 | 327.9 | 5.8788 | 357.5 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32 | 136.6041 | 556.5 | 135.9058 | 582.5 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32 | 0.6036 | 81.0 | 0.6086 | 119.9 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8 | 0.5920 | 60.0 | 0.5911 | 99.1 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32 | 3.9757 | 155.5 | 3.9693 | 170.9 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8 | 3.9877 | 126.6 | 3.9843 | 174.2 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32 | 67.6373 | 202.0 | 67.6370 | 322.8 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8 | 67.5668 | 202.8 | 67.6645 | 327.1 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32 | 0.9829 | 70.8 | 0.9829 | 104.0 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32 | 4.9983 | 336.6 | 4.9995 | 370.2 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32 | 137.4215 | 614.1 | 136.9044 | 579.0 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01 | 0.6518 | 65.6 | 0.7905 | 99.6 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1 | 5.1658 | 118.6 | 5.7724 | 171.6 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1 | 71.0998 | 214.4 | 71.2461 | 289.0 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01 | 0.5981 | 57.2 | 0.6938 | 99.6 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1 | 4.1727 | 96.4 | 4.4871 | 140.9 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1 | 67.5590 | 202.4 | 67.7716 | 299.9 |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | 1.9847 | 97.2 | 2.9336 | 102.9 |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | 1.9742 | 94.5 | 2.9645 | 105.0 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01 | 9.4453 | 168.1 | 9.7696 | 204.0 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1 | 52.6350 | 313.2 | 51.0413 | 320.1 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1 | 1136.0300 | 380.9 | 1135.8885 | 371.8 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01 | 7.4734 | 179.6 | 8.0528 | 209.4 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1 | 33.9388 | 321.5 | 33.9426 | 333.1 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1 | 1078.7370 | 373.1 | 1078.0022 | 376.5 |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing | 27.5173 | - | 28.1921 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing | 62.9473 | - | 62.5403 | - |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | 0.4635 | 56.8 | 0.5085 | 73.8 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | 2.6694 | 101.8 | 2.9446 | 151.9 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | 35.6817 | 187.5 | 35.7943 | 241.2 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | 0.8998 | 78.5 | 0.9462 | 104.4 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | 3.3754 | 186.9 | 3.3732 | 205.6 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | 68.6234 | 552.9 | 68.6373 | 577.4 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | 0.4321 | 69.1 | 0.4461 | 91.1 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | 2.1118 | 113.6 | 2.2553 | 182.6 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | 33.9866 | 180.8 | 34.0759 | 274.2 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | 0.7871 | 66.4 | 0.8094 | 101.1 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | 2.5898 | 216.4 | 2.6112 | 255.5 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | 68.9790 | 516.5 | 68.9435 | 527.8 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01 | 5.3853 | 328.5 | 5.3959 | 335.5 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1 | 30.1699 | 552.4 | 30.8068 | 571.4 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=1 | 1087.5052 | 733.6 | 1087.5680 | 633.0 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01 | 4.5985 | 313.2 | 4.6062 | 320.5 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1 | 23.7467 | 540.6 | 23.7718 | 575.4 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=1 | 1092.6633 | 729.4 | 1093.1301 | 633.8 |

## Per cell

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=k,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x4b0a40000000; level: placement cpu, 199 passes per interval, cursor 0, buffer at 0x4b0b40000000
- per repetition: home 5.365e+08 link read bytes and 0 SMMU translation requests; level 3.354e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=rotated,working-set-mib=8

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 528 passes per interval, cursor 1, buffer at 0x530f00000000; level: placement cpu, 54 passes per interval, cursor 1, buffer at 0x531000000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 1.341e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=k,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 206 passes per interval, cursor 1, buffer at 0x575bc0000000; level: placement hbm, 1151 passes per interval, cursor 1, buffer at 0x575cc0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=rotated,working-set-mib=8

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 1253 passes per interval, cursor 1, buffer at 0x456600000000; level: placement hbm, 666 passes per interval, cursor 1, buffer at 0x456780000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sweeps

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5c5d00000000; level: placement cpu, 7 passes per interval, cursor 0, buffer at 0x5c5e00000000
- per repetition: home 6.422e+09 link read bytes and 3.606e+04 SMMU translation requests; level 8.028e+08 link read bytes and 3169 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sweeps

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 7 passes per interval, cursor 0, buffer at 0x4a5940000000; level: placement hbm, 51 passes per interval, cursor 0, buffer at 0x4a5a40000000
- per repetition: home 0 link read bytes and 5528 SMMU translation requests; level 0 link read bytes and 568.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x40ebc0000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x40f040000000
- per repetition: home 1.718e+10 link read bytes and 2.717e+05 SMMU translation requests; level 1.074e+09 link read bytes and 2755 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x43ccc0000000; level: placement hbm, 67 passes per interval, cursor 0, buffer at 0x43d140000000
- per repetition: home 0 link read bytes and 7.067e+05 SMMU translation requests; level 0 link read bytes and 660.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x552f00000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x5535c0000000
- per repetition: home 2.577e+10 link read bytes and 4.07e+05 SMMU translation requests; level 1.074e+09 link read bytes and 2650 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x4548c0000000; level: placement hbm, 67 passes per interval, cursor 0, buffer at 0x454f80000000
- per repetition: home 0 link read bytes and 1.14e+06 SMMU translation requests; level 0 link read bytes and 657.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 28 passes per interval, cursor 0, buffer at 0x5e3600000000; level: placement cpu, 7 passes per interval, cursor 0, buffer at 0x5e3680000000
- per repetition: home 2.684e+08 link read bytes and 0 SMMU translation requests; level 1.074e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 255 passes per interval, cursor 0, buffer at 0x5665c0000000; level: placement hbm, 68 passes per interval, cursor 0, buffer at 0x566680000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x536600000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x536e80000000
- per repetition: home 3.436e+10 link read bytes and 5.447e+05 SMMU translation requests; level 1.074e+09 link read bytes and 2726 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x4df880000000; level: placement hbm, 67 passes per interval, cursor 0, buffer at 0x4e0100000000
- per repetition: home 0 link read bytes and 1.609e+06 SMMU translation requests; level 0 link read bytes and 664.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x442400000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x442580000000
- per repetition: home 4.295e+09 link read bytes and 0 SMMU translation requests; level 1.074e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 18 passes per interval, cursor 0, buffer at 0x4d7080000000; level: placement hbm, 68 passes per interval, cursor 0, buffer at 0x4d7200000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x515140000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x515400000000
- per repetition: home 8.59e+09 link read bytes and 1.127e+05 SMMU translation requests; level 1.074e+09 link read bytes and 2760 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 9 passes per interval, cursor 0, buffer at 0x4d01c0000000; level: placement hbm, 67 passes per interval, cursor 0, buffer at 0x4d0480000000
- per repetition: home 0 link read bytes and 4.044e+04 SMMU translation requests; level 0 link read bytes and 714.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=working-set,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x4b9880000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4b9a00000000
- per repetition: home 5.365e+08 link read bytes and 0 SMMU translation requests; level 1.718e+10 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=working-set,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 223 passes per interval, cursor 1, buffer at 0x590c40000000; level: placement hbm, 4 passes per interval, cursor 0, buffer at 0x590d40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 253 passes per interval, cursor 0, buffer at 0x525600000000; level: placement hbm, 25 passes per interval, cursor 0, buffer at 0x5256c0000000
- per repetition: home 0 link read bytes and 3.03 SMMU translation requests; level 0 link read bytes and 1380 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=16384,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x549a40000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x549f00000000
- per repetition: home 4.962e+10 link read bytes and 2.772e+05 SMMU translation requests; level 3.197e+09 link read bytes and 1.759e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=16384,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=footprint

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x4a31c0000000; level: placement hbm, 16 passes per interval, cursor 0, buffer at 0x4a3680000000
- per repetition: home 0 link read bytes and 5.064e+05 SMMU translation requests; level 0 link read bytes and 2023 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5d5c80000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5d6140000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 4360 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5de5c0000000; level: placement hbm, 44 passes per interval, cursor 0, buffer at 0x5dea80000000
- per repetition: home 0 link read bytes and 1.207e+08 SMMU translation requests; level 0 link read bytes and 396.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=24576,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x47e980000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x47f040000000
- per repetition: home 7.685e+10 link read bytes and 5.048e+05 SMMU translation requests; level 3.2e+09 link read bytes and 1.756e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=24576,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x473fc0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x474680000000
- per repetition: home 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; level 5.368e+08 link read bytes and 4374 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=24576,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x52a4c0000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x52ab80000000
- per repetition: home 0 link read bytes and 1.667e+08 SMMU translation requests; level 0 link read bytes and 403.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=256,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x436740000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x436800000000
- per repetition: home 7.684e+08 link read bytes and 0 SMMU translation requests; level 3.197e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=256,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=footprint

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 95 passes per interval, cursor 0, buffer at 0x4b1300000000; level: placement hbm, 16 passes per interval, cursor 0, buffer at 0x4b13c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=256,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x427740000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x427800000000
- per repetition: home 5.368e+08 link read bytes and 0 SMMU translation requests; level 5.368e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=256,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 47 passes per interval, cursor 0, buffer at 0x584840000000; level: placement hbm, 44 passes per interval, cursor 0, buffer at 0x584940000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=256,kernel=k6,placement=cpu,type=factor,update=atomic,vary=footprint

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x577c00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x577d00000000
- per repetition: home 0 link read bytes and 309.9 SMMU translation requests; level 0 link read bytes and 4198 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=256,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 98 passes per interval, cursor 0, buffer at 0x4d7b00000000; level: placement hbm, 25 passes per interval, cursor 0, buffer at 0x4d7bc0000000
- per repetition: home 0 link read bytes and 98.58 SMMU translation requests; level 0 link read bytes and 1292 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=32768,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x52b380000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x52bc40000000
- per repetition: home 9.936e+10 link read bytes and 7.609e+05 SMMU translation requests; level 3.195e+09 link read bytes and 1.761e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4f6900000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4f71c0000000
- per repetition: home 5.369e+08 link read bytes and 1.912e+08 SMMU translation requests; level 5.368e+08 link read bytes and 4351 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x4fc240000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x4fcac0000000
- per repetition: home 0 link read bytes and 1.909e+08 SMMU translation requests; level 0 link read bytes and 405.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=4096,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x598f40000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x599100000000
- per repetition: home 1.286e+10 link read bytes and 6.869e+04 SMMU translation requests; level 3.199e+09 link read bytes and 1.762e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=4096,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=footprint

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x42dcc0000000; level: placement hbm, 16 passes per interval, cursor 0, buffer at 0x42de40000000
- per repetition: home 0 link read bytes and 3.985e+04 SMMU translation requests; level 0 link read bytes and 2179 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x53aec0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x53b080000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x5fac40000000; level: placement hbm, 44 passes per interval, cursor 0, buffer at 0x5fae00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=4096,kernel=k6,placement=cpu,type=factor,update=atomic,vary=footprint

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x42bac0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x42bc80000000
- per repetition: home 0 link read bytes and 6.626e+04 SMMU translation requests; level 0 link read bytes and 4236 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=4096,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 7 passes per interval, cursor 0, buffer at 0x4251c0000000; level: placement hbm, 25 passes per interval, cursor 0, buffer at 0x425340000000
- per repetition: home 0 link read bytes and 1.733e+04 SMMU translation requests; level 0 link read bytes and 1316 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=factor,vary=keys

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5c9800000000; level: placement cpu, 2 passes per interval, cursor 0, buffer at 0x5c98c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=factor,vary=keys

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x41b980000000; level: placement hbm, 27 passes per interval, cursor 0, buffer at 0x41ba40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,type=factor,vary=keys

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x5f4d00000000; level: placement cpu, 2 passes per interval, cursor 0, buffer at 0x5f4dc0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8,kernel=k6,keys=1048576,placement=hbm,type=factor,vary=keys

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 113 passes per interval, cursor 0, buffer at 0x432180000000; level: placement hbm, 27 passes per interval, cursor 0, buffer at 0x432240000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8192,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=footprint

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x494600000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4948c0000000
- per repetition: home 2.556e+10 link read bytes and 1.367e+05 SMMU translation requests; level 3.196e+09 link read bytes and 1.759e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8192,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=footprint

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x5af140000000; level: placement hbm, 16 passes per interval, cursor 0, buffer at 0x5af400000000
- per repetition: home 0 link read bytes and 1.227e+05 SMMU translation requests; level 0 link read bytes and 2091 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x423ec0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x424140000000
- per repetition: home 5.369e+08 link read bytes and 1.535e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4349 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x4def80000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x4df200000000
- per repetition: home 0 link read bytes and 1.542e+04 SMMU translation requests; level 0 link read bytes and 405.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=16,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sweeps

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5c04c0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5c0600000000
- per repetition: home 6.422e+09 link read bytes and 3.6e+04 SMMU translation requests; level 1.285e+10 link read bytes and 3.619e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=16,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sweeps

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 7 passes per interval, cursor 0, buffer at 0x452980000000; level: placement hbm, 4 passes per interval, cursor 0, buffer at 0x452ac0000000
- per repetition: home 0 link read bytes and 5942 SMMU translation requests; level 0 link read bytes and 9672 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 7 passes per interval, cursor 0, buffer at 0x4ce300000000; level: placement cpu, 67 passes per interval, cursor 0, buffer at 0x4ce400000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 1.074e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 68 passes per interval, cursor 0, buffer at 0x5368c0000000; level: placement hbm, 530 passes per interval, cursor 1, buffer at 0x536980000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 7 passes per interval, cursor 0, buffer at 0x4d0440000000; level: placement cpu, 525 passes per interval, cursor 0, buffer at 0x4d0540000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 1.074e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 68 passes per interval, cursor 0, buffer at 0x42fc80000000; level: placement hbm, 1990 passes per interval, cursor 1, buffer at 0x42fe00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of1000,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 7 passes per interval, cursor 0, buffer at 0x5ffd40000000; level: placement cpu, 1264 passes per interval, cursor 1, buffer at 0x5ffe40000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 1.074e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of1000,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 68 passes per interval, cursor 0, buffer at 0x4e1480000000; level: placement hbm, 2533 passes per interval, cursor 1, buffer at 0x4e1540000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of2,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 7 passes per interval, cursor 0, buffer at 0x550a40000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x550b40000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of2,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 68 passes per interval, cursor 0, buffer at 0x42a4c0000000; level: placement hbm, 125 passes per interval, cursor 0, buffer at 0x42a5c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=k,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x4d6140000000; level: placement cpu, 104 passes per interval, cursor 0, buffer at 0x4d6240000000
- per repetition: home 5.365e+08 link read bytes and 0 SMMU translation requests; level 6.708e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=k,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 203 passes per interval, cursor 1, buffer at 0x489e80000000; level: placement hbm, 853 passes per interval, cursor 1, buffer at 0x489f80000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sweeps

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x530a00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x530b00000000
- per repetition: home 6.422e+09 link read bytes and 3.629e+04 SMMU translation requests; level 1.606e+09 link read bytes and 9000 SMMU translation requests; multiplexed rows voided: 0

### route/at=2,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sweeps

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 7 passes per interval, cursor 0, buffer at 0x5c9b00000000; level: placement hbm, 26 passes per interval, cursor 0, buffer at 0x5c9c00000000
- per repetition: home 0 link read bytes and 5493 SMMU translation requests; level 0 link read bytes and 1480 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=partition

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4183c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x418840000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 3.879e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=page-order

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4cc9c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4cce40000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.368e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x514680000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x514b40000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.368e+08 link read bytes and 6.297e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x57ba80000000; level: placement hbm, 9 passes per interval, cursor 0, buffer at 0x57bf40000000
- per repetition: home 0 link read bytes and 1.207e+08 SMMU translation requests; level 0 link read bytes and 5.722e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x480240000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x480ac0000000
- per repetition: home 5.369e+08 link read bytes and 1.912e+08 SMMU translation requests; level 5.368e+08 link read bytes and 1.302e+06 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x4c23c0000000; level: placement hbm, 5 passes per interval, cursor 0, buffer at 0x4c2c80000000
- per repetition: home 0 link read bytes and 1.91e+08 SMMU translation requests; level 0 link read bytes and 1.058e+06 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x59ce40000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x59d000000000
- per repetition: home 5.369e+08 link read bytes and 68 SMMU translation requests; level 5.368e+08 link read bytes and 323 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x51f580000000; level: placement hbm, 47 passes per interval, cursor 0, buffer at 0x51f740000000
- per repetition: home 0 link read bytes and 78 SMMU translation requests; level 0 link read bytes and 34.44 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x545000000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5452c0000000
- per repetition: home 5.369e+08 link read bytes and 4.425e+04 SMMU translation requests; level 5.368e+08 link read bytes and 6.653e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x404080000000; level: placement hbm, 45 passes per interval, cursor 0, buffer at 0x404340000000
- per repetition: home 0 link read bytes and 4.426e+04 SMMU translation requests; level 0 link read bytes and 6829 SMMU translation requests; multiplexed rows voided: 0

### route/at=3of4,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 7 passes per interval, cursor 0, buffer at 0x59ec40000000; level: placement cpu, 10 passes per interval, cursor 0, buffer at 0x59ed40000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 8.053e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=3of4,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 68 passes per interval, cursor 0, buffer at 0x4d04c0000000; level: placement hbm, 86 passes per interval, cursor 0, buffer at 0x4d05c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=4,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=k,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x4219c0000000; level: placement cpu, 53 passes per interval, cursor 0, buffer at 0x421a80000000
- per repetition: home 5.365e+08 link read bytes and 0 SMMU translation requests; level 1.342e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=4,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=k,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 209 passes per interval, cursor 1, buffer at 0x4567c0000000; level: placement hbm, 575 passes per interval, cursor 1, buffer at 0x456880000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=4,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=repeat

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5d8d80000000; level: placement cpu, 2 passes per interval, cursor 0, buffer at 0x5d8e40000000
- per repetition: home 0 link read bytes and 4225 SMMU translation requests; level 0 link read bytes and 8282 SMMU translation requests; multiplexed rows voided: 0

### route/at=4,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=repeat

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 25 passes per interval, cursor 0, buffer at 0x440ec0000000; level: placement hbm, 13 passes per interval, cursor 0, buffer at 0x440f80000000
- per repetition: home 0 link read bytes and 1230 SMMU translation requests; level 0 link read bytes and 1957 SMMU translation requests; multiplexed rows voided: 0

### route/at=4,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sweeps

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x58ab00000000; level: placement cpu, 2 passes per interval, cursor 0, buffer at 0x58ac00000000
- per repetition: home 6.422e+09 link read bytes and 3.609e+04 SMMU translation requests; level 3.211e+09 link read bytes and 1.801e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=4,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sweeps

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 7 passes per interval, cursor 0, buffer at 0x563080000000; level: placement hbm, 13 passes per interval, cursor 0, buffer at 0x563180000000
- per repetition: home 0 link read bytes and 5982 SMMU translation requests; level 0 link read bytes and 2979 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=1024,kernel=k3,placement=cpu,type=factor,vary=page-size

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x416100000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x416200000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=1024,kernel=k3,placement=hbm,type=factor,vary=page-size

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 44 passes per interval, cursor 0, buffer at 0x520fc0000000; level: placement hbm, 44 passes per interval, cursor 0, buffer at 0x521080000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-size

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4d3400000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4d38c0000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 149.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-size

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5c9a80000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x5c9f40000000
- per repetition: home 0 link read bytes and 1.206e+08 SMMU translation requests; level 0 link read bytes and 14.27 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=16384,kernel=k3p,placement=cpu,type=factor,vary=page-size

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x507880000000; level: placement cpu, 201 passes per interval, cursor 0, buffer at 0x507d40000000
- per repetition: home 3.355e+07 link read bytes and 1.959e+06 SMMU translation requests; level 3.355e+07 link read bytes and 2.993 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-size

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5ed800000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5ee080000000
- per repetition: home 5.369e+08 link read bytes and 1.912e+08 SMMU translation requests; level 5.369e+08 link read bytes and 278.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-size

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x432ec0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x433080000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-size

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x4c4940000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x4c4b00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-size

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x494740000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4949c0000000
- per repetition: home 5.369e+08 link read bytes and 4097 SMMU translation requests; level 5.369e+08 link read bytes and 83.75 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-size

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x50f780000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x50fa00000000
- per repetition: home 0 link read bytes and 4054 SMMU translation requests; level 0 link read bytes and 8.036 SMMU translation requests; multiplexed rows voided: 0

### route/at=64,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=k,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x59c440000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x59c540000000
- per repetition: home 5.365e+08 link read bytes and 0 SMMU translation requests; level 2.145e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=64,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=k,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 206 passes per interval, cursor 1, buffer at 0x532100000000; level: placement hbm, 61 passes per interval, cursor 1, buffer at 0x532200000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=64,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sweeps

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4a8a00000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4a8b80000000
- per repetition: home 6.422e+09 link read bytes and 3.615e+04 SMMU translation requests; level 5.138e+10 link read bytes and 3.595e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=64,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sweeps

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 7 passes per interval, cursor 0, buffer at 0x585540000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x585680000000
- per repetition: home 0 link read bytes and 5536 SMMU translation requests; level 0 link read bytes and 3.871e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x50ce80000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x50d300000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.387e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x538100000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x538580000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.386e+08 link read bytes and 2.769e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5fe980000000; level: placement hbm, 13 passes per interval, cursor 0, buffer at 0x5fee40000000
- per repetition: home 0 link read bytes and 1.207e+08 SMMU translation requests; level 0 link read bytes and 3.968e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4a8040000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4a88c0000000
- per repetition: home 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; level 5.39e+08 link read bytes and 8.3e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5f9040000000; level: placement hbm, 7 passes per interval, cursor 0, buffer at 0x5f98c0000000
- per repetition: home 0 link read bytes and 1.91e+08 SMMU translation requests; level 0 link read bytes and 8.678e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5cec00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5cedc0000000
- per repetition: home 5.369e+08 link read bytes and 52.12 SMMU translation requests; level 5.363e+08 link read bytes and 96.75 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x4abd80000000; level: placement hbm, 49 passes per interval, cursor 0, buffer at 0x4abf00000000
- per repetition: home 0 link read bytes and 72.12 SMMU translation requests; level 0 link read bytes and 26.39 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x435c00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x435ec0000000
- per repetition: home 5.369e+08 link read bytes and 4.427e+04 SMMU translation requests; level 5.373e+08 link read bytes and 3.436e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x5e1ac0000000; level: placement hbm, 46 passes per interval, cursor 0, buffer at 0x5e1d40000000
- per repetition: home 0 link read bytes and 4.424e+04 SMMU translation requests; level 0 link read bytes and 4357 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=working-set,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x516540000000; level: placement cpu, 531 passes per interval, cursor 1, buffer at 0x516640000000
- per repetition: home 5.365e+08 link read bytes and 0 SMMU translation requests; level 8.382e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=working-set,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 206 passes per interval, cursor 1, buffer at 0x480440000000; level: placement hbm, 1239 passes per interval, cursor 1, buffer at 0x480540000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=9of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 7 passes per interval, cursor 0, buffer at 0x44f1c0000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x44f2c0000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 9.664e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=9of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 68 passes per interval, cursor 0, buffer at 0x527600000000; level: placement hbm, 73 passes per interval, cursor 0, buffer at 0x527740000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=hbm,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=placement

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x4e4f00000000; level: placement hbm, 2 passes per interval, cursor 0, buffer at 0x4e4fc0000000
- no hardware counters in this cell

### route/at=hbm,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=plain,vary=placement

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 9 passes per interval, cursor 0, buffer at 0x41d440000000; level: placement hbm, 9 passes per interval, cursor 0, buffer at 0x41d4c0000000
- no hardware counters in this cell

### route/at=hbm,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=placement

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x5ff1c0000000; level: placement hbm, 2 passes per interval, cursor 0, buffer at 0x5ff280000000
- no hardware counters in this cell

### route/at=hbm,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=plain,vary=placement

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 9 passes per interval, cursor 0, buffer at 0x47ff00000000; level: placement hbm, 8 passes per interval, cursor 0, buffer at 0x47ffc0000000
- no hardware counters in this cell

### route/at=line,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=layout

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x50b4c0000000; level: placement cpu, 6 passes per interval, cursor 0, buffer at 0x50b5c0000000
- per repetition: home 0 link read bytes and 4236 SMMU translation requests; level 0 link read bytes and 2884 SMMU translation requests; multiplexed rows voided: 0

### route/at=line,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=layout

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 25 passes per interval, cursor 0, buffer at 0x510a80000000; level: placement hbm, 59 passes per interval, cursor 0, buffer at 0x510b80000000
- per repetition: home 0 link read bytes and 1257 SMMU translation requests; level 0 link read bytes and 413.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=none,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=tiling

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x435540000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x435640000000
- per repetition: home 6.422e+09 link read bytes and 3.618e+04 SMMU translation requests; level 1.308e+10 link read bytes and 3.51e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=none,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=tiling

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 7 passes per interval, cursor 0, buffer at 0x453680000000; level: placement hbm, 8 passes per interval, cursor 0, buffer at 0x453780000000
- per repetition: home 0 link read bytes and 5952 SMMU translation requests; level 0 link read bytes and 9335 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=1024,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x544ac0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x544c20000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=1024,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 44 passes per interval, cursor 0, buffer at 0x5a5340000000; level: placement hbm, 44 passes per interval, cursor 0, buffer at 0x5a5420000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=1024,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5eb900000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5ebc20000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=1024,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 43 passes per interval, cursor 0, buffer at 0x583f80000000; level: placement hbm, 44 passes per interval, cursor 0, buffer at 0x584420000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=11520,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x556680000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x556c20000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=11520,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x432900000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x433020000000
- per repetition: home 5.369e+08 link read bytes and 6.722e+07 SMMU translation requests; level 5.369e+08 link read bytes and 6.718e+07 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=12288,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x491840000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x491c20000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=12288,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 42 passes per interval, cursor 0, buffer at 0x46cd40000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x46d420000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=12288,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x471b00000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x472020000000
- per repetition: home 5.369e+08 link read bytes and 7.82e+07 SMMU translation requests; level 5.369e+08 link read bytes and 7.82e+07 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=12288,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5afb40000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5b0020000000
- per repetition: home 0 link read bytes and 7.778e+07 SMMU translation requests; level 0 link read bytes and 7.776e+07 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=1536,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4abac0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4abc20000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=1536,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x510680000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x510820000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x512480000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x512c20000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=16384,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 42 passes per interval, cursor 0, buffer at 0x41e600000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x41ec20000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=16384,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x402680000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x402c20000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=16384,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x512d00000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x513420000000
- per repetition: home 0 link read bytes and 1.207e+08 SMMU translation requests; level 0 link read bytes and 1.207e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=2048,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5038c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x503c20000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=2048,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x48a2c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x48a420000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=24576,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5bd940000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5be020000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=24576,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5def80000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5df820000000
- per repetition: home 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=256,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x531400000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x531820000000
- per repetition: home 5.368e+08 link read bytes and 0 SMMU translation requests; level 5.368e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=256,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 48 passes per interval, cursor 0, buffer at 0x4983c0000000; level: placement hbm, 48 passes per interval, cursor 0, buffer at 0x498820000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=256,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4e3b80000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4e4020000000
- per repetition: home 5.368e+08 link read bytes and 0 SMMU translation requests; level 5.368e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=256,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 48 passes per interval, cursor 0, buffer at 0x47f600000000; level: placement hbm, 48 passes per interval, cursor 0, buffer at 0x47f820000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=32768,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4af800000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4b0420000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=32768,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x57a840000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x57b420000000
- per repetition: home 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=4096,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4798c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x479c20000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=4096,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 43 passes per interval, cursor 0, buffer at 0x51a980000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x51ac20000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=4096,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x414700000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x414c20000000
- per repetition: home 5.369e+08 link read bytes and 4422 SMMU translation requests; level 5.369e+08 link read bytes and 4784 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=4096,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x5c5340000000; level: placement hbm, 4 passes per interval, cursor 0, buffer at 0x5c5820000000
- per repetition: home 0 link read bytes and 4406 SMMU translation requests; level 0 link read bytes and 4805 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=8192,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5ca340000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5ca820000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=8192,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 42 passes per interval, cursor 0, buffer at 0x57da80000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x57e020000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=8192,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x5e98c0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5e9c20000000
- per repetition: home 5.369e+08 link read bytes and 4.392e+04 SMMU translation requests; level 5.369e+08 link read bytes and 1.369e+07 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=8192,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x4a1100000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x4a1420000000
- per repetition: home 0 link read bytes and 4.393e+04 SMMU translation requests; level 0 link read bytes and 1.356e+07 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=9728,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x547f00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x548420000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=9728,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x56e980000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x56f020000000
- per repetition: home 5.369e+08 link read bytes and 3.597e+07 SMMU translation requests; level 5.369e+08 link read bytes and 3.597e+07 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x45f500000000; level: placement cpu, 9 passes per interval, cursor 0, buffer at 0x45f580000000
- no hardware counters in this cell

### route/at=plain,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x4e0b80000000; level: placement hbm, 9 passes per interval, cursor 0, buffer at 0x4e0c40000000
- no hardware counters in this cell

### route/at=plain,footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x56e900000000; level: placement cpu, 9 passes per interval, cursor 0, buffer at 0x56e9c0000000
- no hardware counters in this cell

### route/at=plain,footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x57ad80000000; level: placement hbm, 9 passes per interval, cursor 0, buffer at 0x57ae00000000
- no hardware counters in this cell

### route/at=plain,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4334c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x433580000000
- per repetition: home 0 link read bytes and 4184 SMMU translation requests; level 1.074e+09 link read bytes and 4554 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 25 passes per interval, cursor 0, buffer at 0x554880000000; level: placement hbm, 27 passes per interval, cursor 0, buffer at 0x554940000000
- per repetition: home 0 link read bytes and 1338 SMMU translation requests; level 0 link read bytes and 2746 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x5afc80000000; level: placement cpu, 9 passes per interval, cursor 0, buffer at 0x5afd40000000
- no hardware counters in this cell

### route/at=plain,footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x4b7180000000; level: placement hbm, 9 passes per interval, cursor 0, buffer at 0x4b7240000000
- no hardware counters in this cell

### route/at=plain,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 264 passes per interval, cursor 0, buffer at 0x546e40000000; level: placement hbm, 253 passes per interval, cursor 0, buffer at 0x546f00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x51f500000000; level: placement cpu, 9 passes per interval, cursor 0, buffer at 0x51f5c0000000
- no hardware counters in this cell

### route/at=plain,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x5d7bc0000000; level: placement hbm, 8 passes per interval, cursor 0, buffer at 0x5d7cc0000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x5ed080000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5ed100000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x5db6c0000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5db780000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x4a9240000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4a92c0000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x541e00000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x541ec0000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x481580000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x481680000000
- per repetition: home 0 link read bytes and 4195 SMMU translation requests; level 1.074e+09 link read bytes and 4519 SMMU translation requests; multiplexed rows voided: 0

### route/at=returned,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 25 passes per interval, cursor 0, buffer at 0x5b0700000000; level: placement hbm, 23 passes per interval, cursor 0, buffer at 0x5b07c0000000
- per repetition: home 0 link read bytes and 1316 SMMU translation requests; level 0 link read bytes and 3005 SMMU translation requests; multiplexed rows voided: 0

### route/at=returned,footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x5af600000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5af6c0000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x584400000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5844c0000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 261 passes per interval, cursor 0, buffer at 0x5a6c80000000; level: placement hbm, 155 passes per interval, cursor 0, buffer at 0x5a6d40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=returned,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x4fdfc0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4fe040000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x5d8e80000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5d8f40000000
- no hardware counters in this cell

### route/at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=generator

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4d8040000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4d8140000000
- per repetition: home 3.199e+09 link read bytes and 0 SMMU translation requests; level 2.853e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=generator

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 16 passes per interval, cursor 0, buffer at 0x4b4040000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x4b4140000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=rmat,footprint-mib=8192,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=generator

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x427380000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x427640000000
- per repetition: home 2.553e+10 link read bytes and 1.364e+05 SMMU translation requests; level 2.415e+10 link read bytes and 1.593e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=rmat,footprint-mib=8192,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=generator

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x4b7a80000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x4b7d40000000
- per repetition: home 0 link read bytes and 1.353e+05 SMMU translation requests; level 0 link read bytes and 1.67e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x541c40000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x541cc0000000
- per repetition: home 5.243e+05 link read bytes and 0.78 SMMU translation requests; level 5.243e+05 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5e0000000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5e0080000000
- per repetition: home 5.243e+05 link read bytes and 0.78 SMMU translation requests; level 5.243e+05 link read bytes and 0.78 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x537ac0000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x537b80000000
- per repetition: home 5.243e+05 link read bytes and 0 SMMU translation requests; level 5.243e+05 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x49aa40000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x49ab00000000
- per repetition: home 5.243e+05 link read bytes and 0.78 SMMU translation requests; level 5.243e+05 link read bytes and 0.78 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x441ec0000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x441f80000000
- per repetition: home 5.243e+05 link read bytes and 0.78 SMMU translation requests; level 5.243e+05 link read bytes and 0.78 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x4a1b00000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x4a1bc0000000
- per repetition: home 5.243e+05 link read bytes and 0.78 SMMU translation requests; level 5.243e+05 link read bytes and 0.78 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5f3e80000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5f3f40000000
- per repetition: home 6.711e+07 link read bytes and 0 SMMU translation requests; level 6.711e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x49d4c0000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x49d580000000
- per repetition: home 6.711e+07 link read bytes and 46.27 SMMU translation requests; level 6.711e+07 link read bytes and 47.58 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5b5800000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5b5880000000
- per repetition: home 6.711e+07 link read bytes and 22.51 SMMU translation requests; level 6.711e+07 link read bytes and 22.98 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x519a40000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x519ac0000000
- per repetition: home 0 link read bytes and 3009 SMMU translation requests; level 0 link read bytes and 2593 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x462b80000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x462c40000000
- per repetition: home 0 link read bytes and 3046 SMMU translation requests; level 0 link read bytes and 2996 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x523800000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x523880000000
- per repetition: home 0 link read bytes and 3024 SMMU translation requests; level 0 link read bytes and 3009 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x419f00000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x419f80000000
- per repetition: home 6.711e+07 link read bytes and 0 SMMU translation requests; level 6.711e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5b9cc0000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5b9d80000000
- per repetition: home 6.711e+07 link read bytes and 44 SMMU translation requests; level 6.711e+07 link read bytes and 35.67 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x4c6180000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x4c6200000000
- per repetition: home 6.711e+07 link read bytes and 42.23 SMMU translation requests; level 6.711e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x499580000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x499640000000
- per repetition: home 0 link read bytes and 2910 SMMU translation requests; level 0 link read bytes and 2534 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x452d00000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x452d80000000
- per repetition: home 0 link read bytes and 2947 SMMU translation requests; level 0 link read bytes and 2185 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4fac00000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4fac80000000
- per repetition: home 0 link read bytes and 2908 SMMU translation requests; level 0 link read bytes and 2893 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4d60c0000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4d6140000000
- per repetition: home 0 link read bytes and 419 SMMU translation requests; level 0 link read bytes and 392.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x45a600000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x45a680000000
- per repetition: home 0 link read bytes and 415.2 SMMU translation requests; level 0 link read bytes and 364.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4b91c0000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4b9240000000
- per repetition: home 0 link read bytes and 407.2 SMMU translation requests; level 0 link read bytes and 375.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x407d40000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x407dc0000000
- per repetition: home 0 link read bytes and 398.5 SMMU translation requests; level 0 link read bytes and 392.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x52f900000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x52f9c0000000
- per repetition: home 0 link read bytes and 417.6 SMMU translation requests; level 0 link read bytes and 425.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x45f240000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x45f300000000
- per repetition: home 0 link read bytes and 415.2 SMMU translation requests; level 0 link read bytes and 362.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4cccc0000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4ccd80000000
- per repetition: home 0 link read bytes and 4457 SMMU translation requests; level 0 link read bytes and 2984 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4ca140000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4ca200000000
- per repetition: home 0 link read bytes and 4417 SMMU translation requests; level 0 link read bytes and 4308 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x58f640000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x58f700000000
- per repetition: home 0 link read bytes and 4425 SMMU translation requests; level 0 link read bytes and 4312 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x42c740000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x42c7c0000000
- per repetition: home 0 link read bytes and 4592 SMMU translation requests; level 0 link read bytes and 2931 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4b5dc0000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4b5e80000000
- per repetition: home 0 link read bytes and 4643 SMMU translation requests; level 0 link read bytes and 2805 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5fd800000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5fd880000000
- per repetition: home 0 link read bytes and 4549 SMMU translation requests; level 0 link read bytes and 4307 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=factor,vary=sharing

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4b75c0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4b76c0000000
- per repetition: home 3.198e+09 link read bytes and 0 SMMU translation requests; level 3.193e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=factor,vary=sharing

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 16 passes per interval, cursor 0, buffer at 0x492400000000; level: placement hbm, 16 passes per interval, cursor 0, buffer at 0x492500000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x553080000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x553140000000
- per repetition: home 8.382e+06 link read bytes and 313.6 SMMU translation requests; level 8.382e+06 link read bytes and 312.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5c4980000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5c4a40000000
- per repetition: home 8.382e+06 link read bytes and 313.8 SMMU translation requests; level 8.382e+06 link read bytes and 312.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x45b380000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x45b480000000
- per repetition: home 8.382e+06 link read bytes and 312.7 SMMU translation requests; level 8.382e+06 link read bytes and 315.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x44db00000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x44dbc0000000
- per repetition: home 8.382e+06 link read bytes and 310.3 SMMU translation requests; level 8.382e+06 link read bytes and 315.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5a3ac0000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5a3bc0000000
- per repetition: home 8.382e+06 link read bytes and 305 SMMU translation requests; level 8.382e+06 link read bytes and 302.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x52af40000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x52b000000000
- per repetition: home 8.382e+06 link read bytes and 317 SMMU translation requests; level 8.382e+06 link read bytes and 313.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x529040000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x529140000000
- per repetition: home 5.366e+08 link read bytes and 717.7 SMMU translation requests; level 5.365e+08 link read bytes and 806 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5f6680000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5f6780000000
- per repetition: home 8.382e+06 link read bytes and 337.2 SMMU translation requests; level 8.382e+06 link read bytes and 337.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x50d900000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x50da00000000
- per repetition: home 5.365e+08 link read bytes and 785.3 SMMU translation requests; level 5.365e+08 link read bytes and 785.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x4edf00000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x4ee000000000
- per repetition: home 8.382e+06 link read bytes and 327.8 SMMU translation requests; level 8.382e+06 link read bytes and 327.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5334c0000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5335c0000000
- per repetition: home 5.365e+08 link read bytes and 0 SMMU translation requests; level 5.365e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5c1ec0000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5c1f80000000
- per repetition: home 8.382e+06 link read bytes and 310.7 SMMU translation requests; level 8.382e+06 link read bytes and 307 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x49b5c0000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x49b6c0000000
- per repetition: home 0 link read bytes and 953.5 SMMU translation requests; level 0 link read bytes and 952 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x54d340000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x54d440000000
- per repetition: home 0 link read bytes and 937 SMMU translation requests; level 0 link read bytes and 940.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x539d00000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x539e40000000
- per repetition: home 0 link read bytes and 949.5 SMMU translation requests; level 0 link read bytes and 950.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5849c0000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x584ac0000000
- per repetition: home 5.366e+08 link read bytes and 718.2 SMMU translation requests; level 5.365e+08 link read bytes and 757.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x4da900000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x4daa00000000
- per repetition: home 8.382e+06 link read bytes and 330.2 SMMU translation requests; level 8.382e+06 link read bytes and 329.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5aa240000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5aa300000000
- per repetition: home 5.366e+08 link read bytes and 828.2 SMMU translation requests; level 5.365e+08 link read bytes and 855 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x4dd6c0000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x4dd7c0000000
- per repetition: home 8.382e+06 link read bytes and 326.3 SMMU translation requests; level 8.382e+06 link read bytes and 326.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x57e1c0000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x57e2c0000000
- per repetition: home 5.365e+08 link read bytes and 0 SMMU translation requests; level 5.365e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x56a540000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x56a640000000
- per repetition: home 8.382e+06 link read bytes and 309.3 SMMU translation requests; level 8.382e+06 link read bytes and 309 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x57f180000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x57f240000000
- per repetition: home 0 link read bytes and 946.6 SMMU translation requests; level 0 link read bytes and 943.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x423740000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x423840000000
- per repetition: home 0 link read bytes and 940.9 SMMU translation requests; level 0 link read bytes and 945.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x56b880000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x56b9c0000000
- per repetition: home 0 link read bytes and 947.7 SMMU translation requests; level 0 link read bytes and 950.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5c3e80000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5c3f80000000
- per repetition: home 5.368e+08 link read bytes and 1.736e+04 SMMU translation requests; level 5.369e+08 link read bytes and 1.738e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x57ff80000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x580040000000
- per repetition: home 5.369e+08 link read bytes and 1.308e+04 SMMU translation requests; level 5.369e+08 link read bytes and 1.305e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x499440000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x499500000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.368e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x59c680000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x59c740000000
- per repetition: home 5.369e+08 link read bytes and 1.31e+04 SMMU translation requests; level 5.369e+08 link read bytes and 1.741e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x561200000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x561300000000
- per repetition: home 5.369e+08 link read bytes and 1.737e+04 SMMU translation requests; level 5.369e+08 link read bytes and 1.737e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4b7bc0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4b7c80000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x546500000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x546980000000
- per repetition: home 3.355e+07 link read bytes and 2.024e+06 SMMU translation requests; level 3.355e+07 link read bytes and 2.014e+06 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x560740000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x560c00000000
- per repetition: home 3.355e+07 link read bytes and 2.025e+06 SMMU translation requests; level 3.355e+07 link read bytes and 2.015e+06 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x54d1c0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x54d640000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4e8240000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4e86c0000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x43e8c0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x43ed80000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4b7cc0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4b8140000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5f74c0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5f7940000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5f0340000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5f07c0000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x464e00000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x464f40000000
- per repetition: home 6.422e+09 link read bytes and 3.632e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.622e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 7 passes per interval, cursor 0, buffer at 0x549940000000; level: placement hbm, 7 passes per interval, cursor 0, buffer at 0x549a40000000
- per repetition: home 0 link read bytes and 5503 SMMU translation requests; level 0 link read bytes and 5462 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4525c0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4526c0000000
- per repetition: home 6.422e+09 link read bytes and 3.617e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.603e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4e9cc0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4e9dc0000000
- per repetition: home 6.422e+09 link read bytes and 3.608e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.622e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x561d80000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x561e80000000
- per repetition: home 6.422e+09 link read bytes and 3.606e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.608e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x54d280000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x54d3c0000000
- per repetition: home 0 link read bytes and 3.863e+04 SMMU translation requests; level 0 link read bytes and 4.17e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x4ff940000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x4ffa40000000
- per repetition: home 0 link read bytes and 3.852e+04 SMMU translation requests; level 0 link read bytes and 4.498e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x5028c0000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x5029c0000000
- per repetition: home 0 link read bytes and 4.288e+04 SMMU translation requests; level 0 link read bytes and 3.876e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5042c0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5043c0000000
- per repetition: home 6.422e+09 link read bytes and 3.616e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.598e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x41abc0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x41acc0000000
- per repetition: home 6.422e+09 link read bytes and 3.602e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.58e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x407a40000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x407b40000000
- per repetition: home 6.422e+09 link read bytes and 3.606e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.566e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x4c5d80000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x4c5e80000000
- per repetition: home 0 link read bytes and 3.887e+04 SMMU translation requests; level 0 link read bytes and 4.173e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x5f6800000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x5f6940000000
- per repetition: home 0 link read bytes and 4.268e+04 SMMU translation requests; level 0 link read bytes and 4.172e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x599ac0000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x599b80000000
- per repetition: home 0 link read bytes and 3.859e+04 SMMU translation requests; level 0 link read bytes and 4.259e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x4a9940000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x4a9bc0000000
- per repetition: home 0 link read bytes and 1.329e+05 SMMU translation requests; level 0 link read bytes and 1.328e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x559180000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x559440000000
- per repetition: home 0 link read bytes and 1.328e+05 SMMU translation requests; level 0 link read bytes and 1.334e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=1

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x5a1700000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x5a1980000000
- per repetition: home 0 link read bytes and 1.327e+05 SMMU translation requests; level 0 link read bytes and 1.328e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x5a6800000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x5a6ac0000000
- per repetition: home 0 link read bytes and 1.327e+05 SMMU translation requests; level 0 link read bytes and 1.335e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x589a40000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x589d00000000
- per repetition: home 0 link read bytes and 1.329e+05 SMMU translation requests; level 0 link read bytes and 1.328e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=1

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x47bac0000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x47bd80000000
- per repetition: home 0 link read bytes and 1.329e+05 SMMU translation requests; level 0 link read bytes and 1.336e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=sorted,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=index-order

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x44e0c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x44e580000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.438e+08 link read bytes and 2.793e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=stadd,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x5c02c0000000; level: placement cpu, 3 passes per interval, cursor 0, buffer at 0x5c0380000000
- no hardware counters in this cell

### route/at=stadd,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x557200000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x5572c0000000
- no hardware counters in this cell

### route/at=stadd,footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x4206c0000000; level: placement cpu, 3 passes per interval, cursor 0, buffer at 0x420780000000
- no hardware counters in this cell

### route/at=stadd,footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x49ba80000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x49bb40000000
- no hardware counters in this cell

### route/at=stadd,footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x5fe8c0000000; level: placement cpu, 3 passes per interval, cursor 0, buffer at 0x5fe980000000
- no hardware counters in this cell

### route/at=stadd,footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x550f40000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x551000000000
- no hardware counters in this cell

### route/at=stadd,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x405940000000; level: placement cpu, 3 passes per interval, cursor 0, buffer at 0x405a00000000
- no hardware counters in this cell

### route/at=stadd,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x477980000000; level: placement hbm, 2 passes per interval, cursor 0, buffer at 0x477a00000000
- no hardware counters in this cell

### route/at=tiles,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=tiling,working-set-mib=8

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 529 passes per interval, cursor 1, buffer at 0x482780000000; level: placement cpu, 544 passes per interval, cursor 1, buffer at 0x482880000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 8.38e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=tiles,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=tiling,working-set-mib=8

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 1251 passes per interval, cursor 1, buffer at 0x541280000000; level: placement hbm, 1305 passes per interval, cursor 1, buffer at 0x541380000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,type=factor,vary=strategy

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x5e3f00000000; level: placement cpu, 3 passes per interval, cursor 0, buffer at 0x5e3fc0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp,footprint-mib=8,kernel=k6,keys=1048576,placement=hbm,type=factor,vary=strategy

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 113 passes per interval, cursor 0, buffer at 0x557fc0000000; level: placement hbm, 70 passes per interval, cursor 0, buffer at 0x558080000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp,footprint-mib=8,kernel=k6,keys=4096,placement=cpu,type=factor,vary=strategy

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5b7440000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5b74c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp,footprint-mib=8,kernel=k6,keys=4096,placement=hbm,type=factor,vary=strategy

- first variant A, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 76 passes per interval, cursor 0, buffer at 0x5b9600000000; level: placement hbm, 71 passes per interval, cursor 0, buffer at 0x5b9680000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp,footprint-mib=8,kernel=k6,keys=65536,placement=cpu,type=factor,vary=strategy

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement cpu, 5 passes per interval, cursor 0, buffer at 0x474bc0000000; level: placement cpu, 5 passes per interval, cursor 0, buffer at 0x474c40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp,footprint-mib=8,kernel=k6,keys=65536,placement=hbm,type=factor,vary=strategy

- first variant B, seed 73; repeats alternated as drawn: yes
- home: placement hbm, 104 passes per interval, cursor 0, buffer at 0x5c3900000000; level: placement hbm, 70 passes per interval, cursor 0, buffer at 0x5c39c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

