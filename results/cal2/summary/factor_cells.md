# Factor cells: the direct route at a level of one factor against its home level, recomputed from raw rows

Times are per pass in ms. The factor effect on direct access is level minus home within a repeat, as median with its 95 % rank interval; a positive value means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | level | home ms | level ms | effect ms [interval] | relative to home | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|
| at=1024,f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 44.8057 | 2.6753 | -42.1299 [-42.1483, -42.1066] | -94.0 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 12.6637 | 0.5175 | -12.1462 [-12.1483, -12.1324] | -95.9 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 66.4946 | 2.6759 | -63.8182 [-63.8358, -63.8018] | -96.0 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 18.9684 | 0.5169 | -18.4517 [-18.4675, -18.4395] | -97.3 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 0.7367 | 2.9314 | 2.1946 [2.1942, 2.1950] | +297.9 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 0.1316 | 0.5086 | 0.3771 [0.3766, 0.3775] | +286.6 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 88.0803 | 2.6751 | -85.4041 [-85.4469, -85.3894] | -97.0 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 25.3506 | 0.5165 | -24.8342 [-24.8502, -24.8005] | -98.0 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 11.7218 | 2.7479 | -8.9740 [-8.9821, -8.9691] | -76.6 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 2.0212 | 0.5093 | -1.5118 [-1.5139, -1.5105] | -74.8 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 23.0135 | 2.6800 | -20.3335 [-20.3438, -20.3210] | -88.4 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 4.3247 | 0.5136 | -3.8110 [-3.8167, -3.8098] | -88.1 % | 10 | yes | pass |
| at=1024,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 433.4265 | 5.3638 | -428.0609 [-428.1460, -427.9443] | -98.8 % | 10 | yes | pass |
| at=1024,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 427.2812 | 0.4748 | -426.8065 [-426.8508, -426.5746] | -99.9 % | 10 | yes | pass |
| at=1024,footprint-mib=24576,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 598.0740 | 5.3507 | -592.7230 [-592.8022, -592.6368] | -99.1 % | 10 | yes | pass |
| at=1024,footprint-mib=24576,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 592.3876 | 0.4747 | -591.9129 [-592.0323, -591.8330] | -99.9 % | 10 | yes | pass |
| at=1024,footprint-mib=256,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 5.3681 | 5.3727 | 0.0046 [0.0044, 0.0052] | +0.1 % | 50 | yes | pass |
| at=1024,footprint-mib=256,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 0.4389 | 0.4725 | 0.0336 [0.0333, 0.0340] | +7.7 % | 10 | yes | pass |
| at=1024,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 684.7791 | 5.3488 | -679.4296 [-679.6145, -679.2677] | -99.2 % | 10 | yes | pass |
| at=1024,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 680.8077 | 0.4742 | -680.3335 [-680.3885, -680.1807] | -99.9 % | 10 | yes | pass |
| at=1024,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 5.5274 | 5.3470 | -0.1808 [-0.1929, -0.1625] | -3.3 % | 20 | yes | pass |
| at=1024,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 5.1617 | 0.4742 | -4.6878 [-4.6891, -4.6853] | -90.8 % | 10 | yes | pass |
| at=1024,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 7.7846 | 5.3506 | -2.4339 [-2.4357, -2.4326] | -31.3 % | 10 | yes | pass |
| at=1024,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 7.7780 | 0.4751 | -7.3029 [-7.3055, -7.3017] | -93.9 % | 10 | yes | pass |
| at=1of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 1of10 | 2.9288 | 0.3032 | -2.6256 [-2.6272, -2.6243] | -89.6 % | 10 | yes | pass |
| at=1of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 1of10 | 0.5089 | 0.0594 | -0.4495 [-0.4497, -0.4493] | -88.3 % | 10 | yes | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 1of100 | 2.9297 | 0.0350 | -2.8947 [-2.8955, -2.8940] | -98.8 % | 10 | yes | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 1of100 | 0.5101 | 0.0096 | -0.5005 [-0.5007, -0.5002] | -98.1 % | 10 | yes | pass |
| at=1of1000,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 1of1000 | 2.9250 | 0.0076 | -2.9174 [-2.9181, -2.9160] | -99.7 % | 10 | yes | pass |
| at=1of1000,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 1of1000 | 0.5099 | 0.0040 | -0.5059 [-0.5068, -0.5056] | -99.2 % | 10 | yes | pass |
| at=1of2,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 1of2 | 2.9333 | 1.4865 | -1.4463 [-1.4485, -1.4459] | -49.3 % | 10 | yes | pass |
| at=1of2,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 1of2 | 0.5106 | 0.2598 | -0.2508 [-0.2510, -0.2506] | -49.1 % | 10 | yes | pass |
| at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=partition | partition | 2g | 433.4160 | 5.7041 | -427.7096 [-427.7945, -427.6593] | -98.7 % | 10 | yes | pass |
| at=2m,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=page-order | page-order | 2m | 5.3829 | 5.2602 | -0.1229 [-0.1259, -0.1139] | -2.3 % | 10 | yes | pass |
| at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 433.4948 | 5.3665 | -428.1287 [-428.1804, -428.0286] | -98.8 % | 10 | yes | pass |
| at=2m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 427.5381 | 2.4942 | -425.0453 [-425.2674, -424.8296] | -99.4 % | 10 | yes | pass |
| at=2m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 684.8036 | 5.3843 | -679.4186 [-679.6194, -679.2945] | -99.2 % | 10 | yes | pass |
| at=2m,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 680.6835 | 4.2715 | -676.4103 [-676.5864, -676.3164] | -99.4 % | 10 | yes | pass |
| at=2m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 5.4971 | 5.3391 | -0.1565 [-0.1738, -0.1463] | -2.8 % | 30 | yes | pass |
| at=2m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 5.1692 | 0.4471 | -4.7219 [-4.7231, -4.7204] | -91.3 % | 10 | yes | pass |
| at=2m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 7.8877 | 5.3540 | -2.5336 [-2.5364, -2.5328] | -32.1 % | 10 | yes | pass |
| at=2m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 7.8884 | 0.4892 | -7.3991 [-7.4028, -7.3977] | -93.8 % | 10 | yes | pass |
| at=3of4,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 3of4 | 2.9285 | 2.2411 | -0.6874 [-0.6889, -0.6864] | -23.5 % | 10 | yes | pass |
| at=3of4,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 3of4 | 0.5094 | 0.3915 | -0.1181 [-0.1184, -0.1176] | -23.2 % | 10 | yes | pass |
| at=512m,footprint-mib=1024,kernel=k3,placement=cpu,type=factor,vary=page-size | page-size | 512m | 5.3723 | 5.3334 | -0.0393 [-0.0412, -0.0375] | -0.7 % | 10 | yes | pass |
| at=512m,footprint-mib=1024,kernel=k3,placement=hbm,type=factor,vary=page-size | page-size | 512m | 0.4738 | 0.4698 | -0.0039 [-0.0042, -0.0036] | -0.8 % | 10 | yes | pass |
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-size | page-size | 512m | 433.2958 | 5.3885 | -427.9066 [-428.0177, -427.7682] | -98.8 % | 10 | yes | pass |
| at=512m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-size | page-size | 512m | 427.2216 | 0.4831 | -426.7385 [-426.7909, -426.6540] | -99.9 % | 10 | yes | pass |
| at=512m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-size | page-size | 512m | 684.9198 | 5.4072 | -679.5128 [-679.5784, -679.3422] | -99.2 % | 10 | yes | pass |
| at=512m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-size | page-size | 512m | 5.4807 | 5.3727 | -0.1084 [-0.1220, -0.1007] | -2.0 % | 40 | yes | pass |
| at=512m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-size | page-size | 512m | 5.1671 | 0.4795 | -4.6876 [-4.6886, -4.6862] | -90.7 % | 10 | yes | pass |
| at=512m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-size | page-size | 512m | 7.7440 | 5.3827 | -2.3612 [-2.3620, -2.3600] | -30.5 % | 10 | yes | pass |
| at=512m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-size | page-size | 512m | 7.7541 | 0.4825 | -7.2714 [-7.2742, -7.2702] | -93.8 % | 10 | yes | pass |
| at=64k,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=page-order | page-order | 64k | 5.3837 | 5.1407 | -0.2433 [-0.2487, -0.2375] | -4.5 % | 10 | yes | pass |
| at=64k,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 432.7954 | 5.1542 | -427.6415 [-427.8167, -427.5530] | -98.8 % | 10 | yes | pass |
| at=64k,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 427.5022 | 1.2799 | -426.2220 [-426.3333, -425.9190] | -99.7 % | 10 | yes | pass |
| at=64k,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 685.1268 | 5.2438 | -679.8878 [-679.9501, -679.7245] | -99.2 % | 10 | yes | pass |
| at=64k,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 680.9299 | 3.5595 | -677.3710 [-677.4470, -677.2123] | -99.5 % | 10 | yes | pass |
| at=64k,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 5.5137 | 5.0778 | -0.4364 [-0.4561, -0.4075] | -7.9 % | 10 | yes | pass |
| at=64k,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 5.1683 | 0.4258 | -4.7422 [-4.7433, -4.7402] | -91.8 % | 10 | yes | pass |
| at=64k,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 7.8900 | 5.1430 | -2.7485 [-2.7568, -2.7395] | -34.8 % | 10 | yes | pass |
| at=64k,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 7.8966 | 0.4564 | -7.4400 [-7.4428, -7.4387] | -94.2 % | 10 | yes | pass |
| at=9of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 9of10 | 2.9301 | 2.6742 | -0.2555 [-0.2561, -0.2547] | -8.7 % | 10 | yes | pass |
| at=9of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 9of10 | 0.5094 | 0.4731 | -0.0363 [-0.0366, -0.0361] | -7.1 % | 10 | yes | pass |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3821 | 5.3825 | 0.0004 [0.0002, 0.0007] | +0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4824 | 0.4827 | 0.0003 [0.0002, 0.0004] | +0.1 % | 100 | yes | pass |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 279.7330 | 279.6686 | -0.0646 [-0.0987, -0.0259] | -0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | alignment | off512m | 286.1319 | 276.6811 | -9.4336 [-9.5964, -9.0494] | -3.3 % | 10 | yes | pass |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3830 | 5.3839 | 0.0008 [0.0006, 0.0011] | +0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4830 | 0.4841 | 0.0010 [0.0010, 0.0011] | +0.2 % | 40 | yes | pass |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 433.4123 | 433.3342 | -0.0647 [-0.1162, -0.0244] | -0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | alignment | off512m | 427.3695 | 427.3816 | 0.0087 [-0.0291, 0.0713] | +0.0 % | 100 | no | pass |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3734 | 5.3733 | 0.0000 [-0.0003, 0.0004] | +0.0 % | 100 | no | pass |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4815 | 0.4798 | -0.0018 [-0.0019, -0.0016] | -0.4 % | 20 | yes | pass |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.5826 | 5.4593 | -0.1232 [-0.1344, -0.1166] | -2.2 % | 30 | yes | pass |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | alignment | off512m | 5.1667 | 5.1598 | -0.0071 [-0.0075, -0.0067] | -0.1 % | 70 | yes | pass |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3801 | 5.3805 | 0.0003 [0.0001, 0.0007] | +0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4813 | 0.4818 | 0.0005 [0.0004, 0.0006] | +0.1 % | 100 | yes | pass |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 7.8888 | 48.5658 | 40.6754 [40.6149, 40.7050] | +515.6 % | 10 | yes | pass |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | alignment | off512m | 7.8990 | 43.5850 | 35.6845 [35.6571, 35.7297] | +451.8 % | 10 | yes | pass |
| at=sorted,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=index-order | index-order | sorted | 433.4920 | 4.9906 | -428.5012 [-428.6561, -428.3378] | -98.8 % | 10 | yes | pass |

## Per cell

### route/at=1024,f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x418d00000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x419180000000
- per repetition: home 1.718e+10 link read bytes and 5.898e+05 SMMU translation requests; level 1.074e+09 link read bytes and 4880 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x50c440000000; level: placement hbm, 39 passes per interval, cursor 0, buffer at 0x50c8c0000000
- per repetition: home 0 link read bytes and 8.31e+05 SMMU translation requests; level 0 link read bytes and 1362 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x584b80000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x585240000000
- per repetition: home 2.577e+10 link read bytes and 8.629e+05 SMMU translation requests; level 1.074e+09 link read bytes and 4878 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x501b80000000; level: placement hbm, 39 passes per interval, cursor 0, buffer at 0x502200000000
- per repetition: home 0 link read bytes and 1.248e+06 SMMU translation requests; level 0 link read bytes and 1343 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 28 passes per interval, cursor 0, buffer at 0x4ec940000000; level: placement cpu, 7 passes per interval, cursor 0, buffer at 0x4eca00000000
- per repetition: home 2.684e+08 link read bytes and 0 SMMU translation requests; level 1.074e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 153 passes per interval, cursor 0, buffer at 0x57a040000000; level: placement hbm, 40 passes per interval, cursor 0, buffer at 0x57a100000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5ec540000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x5ece00000000
- per repetition: home 3.436e+10 link read bytes and 1.131e+06 SMMU translation requests; level 1.074e+09 link read bytes and 4808 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x551680000000; level: placement hbm, 39 passes per interval, cursor 0, buffer at 0x551f40000000
- per repetition: home 0 link read bytes and 1.659e+06 SMMU translation requests; level 0 link read bytes and 1356 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x5dda80000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x5ddc40000000
- per repetition: home 4.295e+09 link read bytes and 0 SMMU translation requests; level 1.074e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 10 passes per interval, cursor 0, buffer at 0x457e40000000; level: placement hbm, 40 passes per interval, cursor 0, buffer at 0x458000000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x48a3c0000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x48a640000000
- per repetition: home 8.59e+09 link read bytes and 3.033e+05 SMMU translation requests; level 1.074e+09 link read bytes and 4875 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 5 passes per interval, cursor 0, buffer at 0x4dc5c0000000; level: placement hbm, 39 passes per interval, cursor 0, buffer at 0x4dc880000000
- per repetition: home 0 link read bytes and 9.761e+04 SMMU translation requests; level 0 link read bytes and 1560 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x48ab80000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x48b040000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.368e+08 link read bytes and 4353 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x4fe040000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x4fe500000000
- per repetition: home 0 link read bytes and 1.211e+08 SMMU translation requests; level 0 link read bytes and 404.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=24576,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x50a780000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x50ae00000000
- per repetition: home 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; level 5.369e+08 link read bytes and 4363 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=24576,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5227c0000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x522e40000000
- per repetition: home 0 link read bytes and 1.671e+08 SMMU translation requests; level 0 link read bytes and 414.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=256,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x535bc0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x535cc0000000
- per repetition: home 5.368e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=256,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 46 passes per interval, cursor 0, buffer at 0x41e340000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x41e3c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4b5e00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4b66c0000000
- per repetition: home 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; level 5.368e+08 link read bytes and 4359 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x403a00000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x404280000000
- per repetition: home 0 link read bytes and 1.913e+08 SMMU translation requests; level 0 link read bytes and 406.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x49f8c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x49fa40000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x4c93c0000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x4c9580000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x406d80000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x407000000000
- per repetition: home 5.369e+08 link read bytes and 1.527e+04 SMMU translation requests; level 5.368e+08 link read bytes and 4355 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x4ad0c0000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x4ad380000000
- per repetition: home 0 link read bytes and 1.53e+04 SMMU translation requests; level 0 link read bytes and 403.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 7 passes per interval, cursor 0, buffer at 0x5bdf80000000; level: placement cpu, 67 passes per interval, cursor 0, buffer at 0x5be040000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 1.074e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 40 passes per interval, cursor 0, buffer at 0x5e7cc0000000; level: placement hbm, 337 passes per interval, cursor 1, buffer at 0x5e7d80000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 8 passes per interval, cursor 0, buffer at 0x406b80000000; level: placement cpu, 632 passes per interval, cursor 0, buffer at 0x406c80000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 1.074e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 40 passes per interval, cursor 0, buffer at 0x418880000000; level: placement hbm, 2061 passes per interval, cursor 1, buffer at 0x418980000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of1000,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 7 passes per interval, cursor 0, buffer at 0x559c00000000; level: placement cpu, 2637 passes per interval, cursor 1, buffer at 0x559d00000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 1.074e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of1000,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 40 passes per interval, cursor 0, buffer at 0x5e4c00000000; level: placement hbm, 4885 passes per interval, cursor 1, buffer at 0x5e4d00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of2,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 7 passes per interval, cursor 0, buffer at 0x402780000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x4028c0000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of2,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 40 passes per interval, cursor 0, buffer at 0x42f080000000; level: placement hbm, 77 passes per interval, cursor 0, buffer at 0x42f140000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=partition

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x447900000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x447d80000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 2.729e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=page-order

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x54a380000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x54a800000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.366e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x400880000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x400d00000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.366e+08 link read bytes and 6.13e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5d2140000000; level: placement hbm, 9 passes per interval, cursor 0, buffer at 0x5d25c0000000
- per repetition: home 0 link read bytes and 1.211e+08 SMMU translation requests; level 0 link read bytes and 5.702e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x59dd80000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x59e640000000
- per repetition: home 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; level 5.366e+08 link read bytes and 1.367e+06 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x40c200000000; level: placement hbm, 5 passes per interval, cursor 0, buffer at 0x40cac0000000
- per repetition: home 0 link read bytes and 1.913e+08 SMMU translation requests; level 0 link read bytes and 1.065e+06 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x53bb00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x53bcc0000000
- per repetition: home 5.369e+08 link read bytes and 68 SMMU translation requests; level 5.366e+08 link read bytes and 241.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x5870c0000000; level: placement hbm, 45 passes per interval, cursor 0, buffer at 0x587280000000
- per repetition: home 0 link read bytes and 68.25 SMMU translation requests; level 0 link read bytes and 26.72 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x4443c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x444680000000
- per repetition: home 5.369e+08 link read bytes and 4.423e+04 SMMU translation requests; level 5.366e+08 link read bytes and 6.398e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x4550c0000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x455380000000
- per repetition: home 0 link read bytes and 4.427e+04 SMMU translation requests; level 0 link read bytes and 7092 SMMU translation requests; multiplexed rows voided: 0

### route/at=3of4,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 7 passes per interval, cursor 0, buffer at 0x527ec0000000; level: placement cpu, 9 passes per interval, cursor 0, buffer at 0x527fc0000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 8.053e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=3of4,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 40 passes per interval, cursor 0, buffer at 0x5506c0000000; level: placement hbm, 52 passes per interval, cursor 0, buffer at 0x5507c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=1024,kernel=k3,placement=cpu,type=factor,vary=page-size

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x501fc0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5020c0000000
- per repetition: home 5.368e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=1024,kernel=k3,placement=hbm,type=factor,vary=page-size

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 43 passes per interval, cursor 0, buffer at 0x421200000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x421300000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-size

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x49e680000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x49eb40000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 149.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-size

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5f3c00000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x5f4080000000
- per repetition: home 0 link read bytes and 1.211e+08 SMMU translation requests; level 0 link read bytes and 14.24 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-size

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4c3440000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4c3cc0000000
- per repetition: home 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; level 5.369e+08 link read bytes and 279.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-size

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x55a900000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x55aac0000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-size

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x4e2100000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x4e22c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-size

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x552380000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x552600000000
- per repetition: home 5.369e+08 link read bytes and 4159 SMMU translation requests; level 5.369e+08 link read bytes and 83.25 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-size

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x4fa8c0000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x4fab80000000
- per repetition: home 0 link read bytes and 4096 SMMU translation requests; level 0 link read bytes and 7.988 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=page-order

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4e86c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4e8b40000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.384e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5f5e40000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5f62c0000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.383e+08 link read bytes and 2.307e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x525b80000000; level: placement hbm, 16 passes per interval, cursor 0, buffer at 0x526000000000
- per repetition: home 0 link read bytes and 1.211e+08 SMMU translation requests; level 0 link read bytes and 3.253e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4dea80000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4df300000000
- per repetition: home 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; level 5.388e+08 link read bytes and 6.282e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x53ab00000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x53b380000000
- per repetition: home 0 link read bytes and 1.913e+08 SMMU translation requests; level 0 link read bytes and 9.649e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x47fd00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x47fec0000000
- per repetition: home 5.369e+08 link read bytes and 58 SMMU translation requests; level 5.331e+08 link read bytes and 185.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x4755c0000000; level: placement hbm, 47 passes per interval, cursor 0, buffer at 0x475780000000
- per repetition: home 0 link read bytes and 62 SMMU translation requests; level 0 link read bytes and 22.16 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x57e480000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x57e700000000
- per repetition: home 5.369e+08 link read bytes and 4.426e+04 SMMU translation requests; level 5.362e+08 link read bytes and 3.428e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x54cc40000000; level: placement hbm, 45 passes per interval, cursor 0, buffer at 0x54cf00000000
- per repetition: home 0 link read bytes and 4.424e+04 SMMU translation requests; level 0 link read bytes and 5156 SMMU translation requests; multiplexed rows voided: 0

### route/at=9of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 7 passes per interval, cursor 0, buffer at 0x5c2940000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x5c2a00000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 9.664e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=9of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 40 passes per interval, cursor 0, buffer at 0x5db0c0000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x5db1c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=12288,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x553640000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x553c20000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=12288,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 42 passes per interval, cursor 0, buffer at 0x484500000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x484c20000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=12288,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x42e680000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x42ec20000000
- per repetition: home 5.369e+08 link read bytes and 7.821e+07 SMMU translation requests; level 5.369e+08 link read bytes and 7.819e+07 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=12288,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x478040000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x478420000000
- per repetition: home 0 link read bytes and 7.818e+07 SMMU translation requests; level 0 link read bytes and 7.82e+07 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x56fe40000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x570420000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=16384,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 42 passes per interval, cursor 0, buffer at 0x57fb40000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x580020000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=16384,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x473b00000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x474020000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=16384,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x564140000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x564820000000
- per repetition: home 0 link read bytes and 1.211e+08 SMMU translation requests; level 0 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=4096,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5d3540000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5d3820000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=4096,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 42 passes per interval, cursor 0, buffer at 0x560e80000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x561420000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=4096,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x522c00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x523020000000
- per repetition: home 5.369e+08 link read bytes and 4451 SMMU translation requests; level 5.369e+08 link read bytes and 4866 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=4096,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x537080000000; level: placement hbm, 4 passes per interval, cursor 0, buffer at 0x537420000000
- per repetition: home 0 link read bytes and 4425 SMMU translation requests; level 0 link read bytes and 4787 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=8192,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5ef440000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5ef820000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=8192,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 42 passes per interval, cursor 0, buffer at 0x539b80000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x53a020000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=8192,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x511180000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x511420000000
- per repetition: home 5.369e+08 link read bytes and 4.393e+04 SMMU translation requests; level 5.369e+08 link read bytes and 1.368e+07 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=8192,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment

- first variant A, seed 37; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x59aa40000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x59b020000000
- per repetition: home 0 link read bytes and 4.391e+04 SMMU translation requests; level 0 link read bytes and 1.369e+07 SMMU translation requests; multiplexed rows voided: 0

### route/at=sorted,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=index-order

- first variant B, seed 37; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x444e00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x445280000000
- per repetition: home 5.369e+08 link read bytes and 1.212e+08 SMMU translation requests; level 5.438e+08 link read bytes and 2.289e+05 SMMU translation requests; multiplexed rows voided: 0

