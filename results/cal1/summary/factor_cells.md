# Factor cells: the direct route at a level of one factor against its home level, recomputed from raw rows

Times are per pass in ms. The factor effect on direct access is level minus home within a repeat, as median with its 95 % rank interval; a positive value means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | level | home ms | level ms | effect ms [interval] | relative to home | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|
| at=1024,f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 44.7800 | 2.6749 | -42.1059 [-42.1157, -42.0881] | -94.0 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 12.6757 | 0.5172 | -12.1583 [-12.1707, -12.1348] | -95.9 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 66.4462 | 2.6781 | -63.7679 [-63.7832, -63.7462] | -96.0 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 18.9811 | 0.5181 | -18.4630 [-18.4766, -18.4435] | -97.3 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 0.7396 | 2.9318 | 2.1924 [2.1913, 2.1931] | +296.4 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 0.1311 | 0.5094 | 0.3781 [0.3778, 0.3786] | +288.4 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 88.1024 | 2.6757 | -85.4261 [-85.4618, -85.3981] | -97.0 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 25.2705 | 0.5173 | -24.7535 [-24.7783, -24.7005] | -98.0 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 11.7199 | 2.7610 | -8.9590 [-8.9641, -8.9559] | -76.4 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 2.0203 | 0.5098 | -1.5103 [-1.5121, -1.5089] | -74.8 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 22.9966 | 2.6760 | -20.3203 [-20.3295, -20.3120] | -88.4 % | 10 | yes | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 4.3872 | 0.5158 | -3.8717 [-3.8766, -3.8624] | -88.2 % | 10 | yes | pass |
| at=1024,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 433.3228 | 5.3502 | -427.9723 [-428.0079, -427.8230] | -98.8 % | 10 | yes | pass |
| at=1024,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 427.7188 | 0.4759 | -427.2430 [-427.3155, -427.1360] | -99.9 % | 10 | yes | pass |
| at=1024,footprint-mib=24576,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 598.1653 | 5.3495 | -592.8144 [-592.8833, -592.7299] | -99.1 % | 10 | yes | pass |
| at=1024,footprint-mib=24576,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 592.4734 | 0.4776 | -591.9959 [-592.0365, -591.8027] | -99.9 % | 10 | yes | pass |
| at=1024,footprint-mib=256,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 5.3687 | 5.3724 | 0.0038 [0.0034, 0.0041] | +0.1 % | 30 | yes | pass |
| at=1024,footprint-mib=256,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 0.4418 | 0.4736 | 0.0320 [0.0315, 0.0322] | +7.2 % | 10 | yes | pass |
| at=1024,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 683.7798 | 5.3492 | -678.4305 [-678.5266, -678.3122] | -99.2 % | 10 | yes | pass |
| at=1024,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 680.8684 | 0.4749 | -680.3936 [-680.5600, -680.2604] | -99.9 % | 10 | yes | pass |
| at=1024,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 5.5598 | 5.3452 | -0.2142 [-0.2237, -0.2024] | -3.9 % | 10 | yes | pass |
| at=1024,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 5.1666 | 0.4731 | -4.6937 [-4.6948, -4.6924] | -90.8 % | 10 | yes | pass |
| at=1024,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=footprint | footprint | 1024 | 7.7862 | 5.3491 | -2.4369 [-2.4386, -2.4363] | -31.3 % | 10 | yes | pass |
| at=1024,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=footprint | footprint | 1024 | 7.7925 | 0.4763 | -7.3160 [-7.3181, -7.3138] | -93.9 % | 10 | yes | pass |
| at=1of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 1of10 | 2.9247 | 0.3023 | -2.6225 [-2.6240, -2.6218] | -89.7 % | 10 | yes | pass |
| at=1of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 1of10 | 0.5105 | 0.0596 | -0.4509 [-0.4515, -0.4504] | -88.3 % | 10 | yes | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 1of100 | 2.9287 | 0.0352 | -2.8935 [-2.8941, -2.8918] | -98.8 % | 10 | yes | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 1of100 | 0.5105 | 0.0097 | -0.5008 [-0.5015, -0.5004] | -98.1 % | 10 | yes | pass |
| at=1of1000,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 1of1000 | 2.9266 | 0.0076 | -2.9190 [-2.9192, -2.9175] | -99.7 % | 10 | yes | pass |
| at=1of1000,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 1of1000 | 0.5100 | 0.0041 | -0.5059 [-0.5062, -0.5055] | -99.2 % | 10 | yes | pass |
| at=1of2,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 1of2 | 2.9318 | 1.4856 | -1.4459 [-1.4481, -1.4449] | -49.3 % | 10 | yes | pass |
| at=1of2,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 1of2 | 0.5089 | 0.2603 | -0.2486 [-0.2490, -0.2484] | -48.8 % | 10 | yes | pass |
| at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=partition | partition | 2g | 433.5908 | 5.6915 | -427.9110 [-428.0050, -427.8355] | -98.7 % | 10 | yes | pass |
| at=2m,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=page-order | page-order | 2m | 5.3842 | 5.2570 | -0.1268 [-0.1333, -0.1163] | -2.4 % | 10 | yes | pass |
| at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 433.4337 | 5.3680 | -428.0661 [-428.1798, -427.9520] | -98.8 % | 10 | yes | pass |
| at=2m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 427.7780 | 2.4986 | -425.2788 [-425.4349, -425.1549] | -99.4 % | 10 | yes | pass |
| at=2m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 684.8718 | 5.3825 | -679.4826 [-679.6670, -679.3630] | -99.2 % | 10 | yes | pass |
| at=2m,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 679.8450 | 4.2713 | -675.5686 [-675.6942, -675.4845] | -99.4 % | 10 | yes | pass |
| at=2m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 5.4491 | 5.3441 | -0.1051 [-0.1169, -0.0976] | -1.9 % | 30 | yes | pass |
| at=2m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 5.1609 | 0.4481 | -4.7130 [-4.7136, -4.7107] | -91.3 % | 10 | yes | pass |
| at=2m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 2m | 7.8895 | 5.3535 | -2.5360 [-2.5371, -2.5346] | -32.1 % | 10 | yes | pass |
| at=2m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 2m | 7.8856 | 0.4889 | -7.3966 [-7.3983, -7.3948] | -93.8 % | 10 | yes | pass |
| at=3of4,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 3of4 | 2.9308 | 2.2439 | -0.6865 [-0.6880, -0.6856] | -23.4 % | 10 | yes | pass |
| at=3of4,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 3of4 | 0.5104 | 0.3919 | -0.1185 [-0.1186, -0.1181] | -23.2 % | 10 | yes | pass |
| at=512m,footprint-mib=1024,kernel=k3,placement=cpu,type=factor,vary=page-size | page-size | 512m | 5.3743 | 5.3325 | -0.0421 [-0.0428, -0.0401] | -0.8 % | 10 | yes | pass |
| at=512m,footprint-mib=1024,kernel=k3,placement=hbm,type=factor,vary=page-size | page-size | 512m | 0.4724 | 0.4696 | -0.0029 [-0.0030, -0.0024] | -0.6 % | 10 | yes | pass |
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-size | page-size | 512m | 433.4161 | 5.4040 | -428.0118 [-428.2342, -427.8596] | -98.8 % | 10 | yes | pass |
| at=512m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-size | page-size | 512m | 426.6235 | 0.4832 | -426.1402 [-426.2864, -426.0598] | -99.9 % | 10 | yes | pass |
| at=512m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-size | page-size | 512m | 684.8082 | 5.3937 | -679.4150 [-679.5816, -679.3045] | -99.2 % | 10 | yes | pass |
| at=512m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-size | page-size | 512m | 5.5379 | 5.3724 | -0.1659 [-0.1794, -0.1509] | -3.0 % | 10 | yes | pass |
| at=512m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-size | page-size | 512m | 5.1569 | 0.4792 | -4.6777 [-4.6811, -4.6764] | -90.7 % | 10 | yes | pass |
| at=512m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-size | page-size | 512m | 7.7460 | 5.3820 | -2.3638 [-2.3657, -2.3634] | -30.5 % | 10 | yes | pass |
| at=512m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-size | page-size | 512m | 7.7551 | 0.4829 | -7.2722 [-7.2734, -7.2703] | -93.8 % | 10 | yes | pass |
| at=64k,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=page-order | page-order | 64k | 5.3845 | 5.1431 | -0.2412 [-0.2434, -0.2375] | -4.5 % | 10 | yes | pass |
| at=64k,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 433.5134 | 5.1812 | -428.3271 [-428.5190, -428.2962] | -98.8 % | 10 | yes | pass |
| at=64k,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 427.4076 | 1.2873 | -426.1198 [-426.2460, -426.0039] | -99.7 % | 10 | yes | pass |
| at=64k,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 685.0120 | 5.2478 | -679.7631 [-679.9215, -679.6749] | -99.2 % | 10 | yes | pass |
| at=64k,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 680.9127 | 3.5355 | -677.3791 [-677.5463, -677.2268] | -99.5 % | 10 | yes | pass |
| at=64k,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 5.5411 | 5.0867 | -0.4566 [-0.4820, -0.4440] | -8.2 % | 10 | yes | pass |
| at=64k,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 5.1680 | 0.4260 | -4.7422 [-4.7434, -4.7409] | -91.8 % | 10 | yes | pass |
| at=64k,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order | page-order | 64k | 7.8896 | 5.0891 | -2.7996 [-2.8035, -2.7927] | -35.5 % | 10 | yes | pass |
| at=64k,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order | page-order | 64k | 7.8946 | 0.4565 | -7.4381 [-7.4392, -7.4368] | -94.2 % | 10 | yes | pass |
| at=9of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | f | 9of10 | 2.9255 | 2.6735 | -0.2522 [-0.2537, -0.2511] | -8.6 % | 10 | yes | pass |
| at=9of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | f | 9of10 | 0.5096 | 0.4737 | -0.0359 [-0.0362, -0.0356] | -7.0 % | 10 | yes | pass |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3807 | 5.3830 | 0.0023 [0.0019, 0.0025] | +0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4826 | 0.4822 | -0.0005 [-0.0006, -0.0004] | -0.1 % | 100 | yes | pass |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 279.6234 | 279.6191 | -0.0239 [-0.0679, 0.0171] | -0.0 % | 100 | no | pass |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | alignment | off512m | 286.1076 | 282.9866 | -3.1290 [-3.2594, -3.0320] | -1.1 % | 10 | yes | pass |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3823 | 5.3831 | 0.0009 [0.0007, 0.0012] | +0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4830 | 0.4836 | 0.0006 [0.0005, 0.0007] | +0.1 % | 100 | yes | pass |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 433.5432 | 433.4630 | -0.0506 [-0.0911, -0.0215] | -0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | alignment | off512m | 427.6154 | 427.4768 | -0.1343 [-0.1775, -0.0881] | -0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3723 | 5.3729 | 0.0007 [0.0003, 0.0009] | +0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4795 | 0.4800 | 0.0005 [0.0004, 0.0006] | +0.1 % | 100 | yes | pass |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.5274 | 5.5606 | 0.0356 [0.0248, 0.0433] | +0.6 % | 100 | yes | pass |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | alignment | off512m | 5.1585 | 5.1560 | -0.0026 [-0.0029, -0.0022] | -0.0 % | 100 | yes | pass |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | alignment | off512m | 5.3798 | 5.3797 | -0.0001 [-0.0003, 0.0002] | -0.0 % | 100 | no | pass |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | alignment | off512m | 0.4816 | 0.4832 | 0.0015 [0.0014, 0.0016] | +0.3 % | 50 | yes | pass |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | alignment | off512m | 7.8884 | 48.6000 | 40.7110 [40.6767, 40.7800] | +516.1 % | 10 | yes | pass |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | alignment | off512m | 7.8955 | 43.4884 | 35.5935 [35.5498, 35.6293] | +450.8 % | 10 | yes | pass |
| at=sorted,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=index-order | index-order | sorted | 433.4415 | 5.0109 | -428.4331 [-428.5756, -428.3906] | -98.8 % | 10 | yes | pass |

## Per cell

### route/at=1024,f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x425240000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x425700000000
- per repetition: home 1.718e+10 link read bytes and 5.91e+05 SMMU translation requests; level 1.074e+09 link read bytes and 4962 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x578580000000; level: placement hbm, 40 passes per interval, cursor 0, buffer at 0x578a40000000
- per repetition: home 0 link read bytes and 8.309e+05 SMMU translation requests; level 0 link read bytes and 1326 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x423800000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x423e80000000
- per repetition: home 2.577e+10 link read bytes and 8.652e+05 SMMU translation requests; level 1.074e+09 link read bytes and 4897 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x56cdc0000000; level: placement hbm, 40 passes per interval, cursor 0, buffer at 0x56d480000000
- per repetition: home 0 link read bytes and 1.247e+06 SMMU translation requests; level 0 link read bytes and 1295 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 28 passes per interval, cursor 0, buffer at 0x5af880000000; level: placement cpu, 7 passes per interval, cursor 0, buffer at 0x5af980000000
- per repetition: home 2.684e+08 link read bytes and 0 SMMU translation requests; level 1.074e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 153 passes per interval, cursor 0, buffer at 0x4913c0000000; level: placement hbm, 40 passes per interval, cursor 0, buffer at 0x491480000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5ba4c0000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x5bad80000000
- per repetition: home 3.436e+10 link read bytes and 1.132e+06 SMMU translation requests; level 1.074e+09 link read bytes and 4889 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x499f40000000; level: placement hbm, 40 passes per interval, cursor 0, buffer at 0x49a800000000
- per repetition: home 0 link read bytes and 1.66e+06 SMMU translation requests; level 0 link read bytes and 1333 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x4a5040000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x4a51c0000000
- per repetition: home 4.295e+09 link read bytes and 0 SMMU translation requests; level 1.074e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 10 passes per interval, cursor 0, buffer at 0x5e7980000000; level: placement hbm, 40 passes per interval, cursor 0, buffer at 0x5e7b00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=cpu,type=factor,vary=footprint

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x597940000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x597bc0000000
- per repetition: home 8.59e+09 link read bytes and 3.028e+05 SMMU translation requests; level 1.074e+09 link read bytes and 4894 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=hbm,type=factor,vary=footprint

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 5 passes per interval, cursor 0, buffer at 0x41e580000000; level: placement hbm, 40 passes per interval, cursor 0, buffer at 0x41e800000000
- per repetition: home 0 link read bytes and 9.104e+04 SMMU translation requests; level 0 link read bytes and 1399 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4b8680000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4b8b40000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 4351 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x57be00000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x57c280000000
- per repetition: home 0 link read bytes and 1.211e+08 SMMU translation requests; level 0 link read bytes and 404.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=24576,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x451600000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x451cc0000000
- per repetition: home 5.369e+08 link read bytes and 1.671e+08 SMMU translation requests; level 5.368e+08 link read bytes and 4367 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=24576,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x58d0c0000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x58d780000000
- per repetition: home 0 link read bytes and 1.671e+08 SMMU translation requests; level 0 link read bytes and 414.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=256,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4d1900000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4d19c0000000
- per repetition: home 5.368e+08 link read bytes and 0 SMMU translation requests; level 5.368e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=256,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 46 passes per interval, cursor 0, buffer at 0x40fb00000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x40fbc0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5819c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x582240000000
- per repetition: home 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; level 5.369e+08 link read bytes and 4352 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x4b2dc0000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x4b3640000000
- per repetition: home 0 link read bytes and 1.912e+08 SMMU translation requests; level 0 link read bytes and 405.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x533740000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5338c0000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x5677c0000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x567980000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=footprint

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x44ca00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x44ccc0000000
- per repetition: home 5.369e+08 link read bytes and 1.549e+04 SMMU translation requests; level 5.368e+08 link read bytes and 4358 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=footprint

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x4d8cc0000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x4d8f80000000
- per repetition: home 0 link read bytes and 1.519e+04 SMMU translation requests; level 0 link read bytes and 404.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 7 passes per interval, cursor 0, buffer at 0x5d1100000000; level: placement cpu, 67 passes per interval, cursor 0, buffer at 0x5d1200000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 1.074e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 40 passes per interval, cursor 0, buffer at 0x50db00000000; level: placement hbm, 337 passes per interval, cursor 1, buffer at 0x50dc40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 8 passes per interval, cursor 0, buffer at 0x541c00000000; level: placement cpu, 632 passes per interval, cursor 0, buffer at 0x541d00000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 1.074e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 40 passes per interval, cursor 0, buffer at 0x596fc0000000; level: placement hbm, 2061 passes per interval, cursor 1, buffer at 0x5970c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of1000,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 7 passes per interval, cursor 0, buffer at 0x4f5dc0000000; level: placement cpu, 2637 passes per interval, cursor 1, buffer at 0x4f5e80000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 1.074e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of1000,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 40 passes per interval, cursor 0, buffer at 0x4f4540000000; level: placement hbm, 4885 passes per interval, cursor 1, buffer at 0x4f4640000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of2,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 7 passes per interval, cursor 0, buffer at 0x47d340000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x47d440000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1of2,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 40 passes per interval, cursor 0, buffer at 0x506140000000; level: placement hbm, 77 passes per interval, cursor 0, buffer at 0x506240000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=partition

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x50f4c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x50f980000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 2.757e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=page-order

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4bd000000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4bd480000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.366e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4a2ac0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4a2f80000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.366e+08 link read bytes and 6.103e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x48d9c0000000; level: placement hbm, 9 passes per interval, cursor 0, buffer at 0x48de40000000
- per repetition: home 0 link read bytes and 1.211e+08 SMMU translation requests; level 0 link read bytes and 5.69e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5fd180000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5fda00000000
- per repetition: home 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; level 5.366e+08 link read bytes and 1.365e+06 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x402bc0000000; level: placement hbm, 5 passes per interval, cursor 0, buffer at 0x403480000000
- per repetition: home 0 link read bytes and 1.913e+08 SMMU translation requests; level 0 link read bytes and 1.069e+06 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5005c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x500780000000
- per repetition: home 5.369e+08 link read bytes and 62.12 SMMU translation requests; level 5.366e+08 link read bytes and 191.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x4bf880000000; level: placement hbm, 45 passes per interval, cursor 0, buffer at 0x4bfa00000000
- per repetition: home 0 link read bytes and 62 SMMU translation requests; level 0 link read bytes and 28.96 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x57a5c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x57a840000000
- per repetition: home 5.369e+08 link read bytes and 4.424e+04 SMMU translation requests; level 5.366e+08 link read bytes and 6.382e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=2m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x433780000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x433a00000000
- per repetition: home 0 link read bytes and 4.428e+04 SMMU translation requests; level 0 link read bytes and 6951 SMMU translation requests; multiplexed rows voided: 0

### route/at=3of4,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 7 passes per interval, cursor 0, buffer at 0x5b5f80000000; level: placement cpu, 9 passes per interval, cursor 0, buffer at 0x5b60c0000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 8.053e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=3of4,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 40 passes per interval, cursor 0, buffer at 0x48d540000000; level: placement hbm, 52 passes per interval, cursor 0, buffer at 0x48d640000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=1024,kernel=k3,placement=cpu,type=factor,vary=page-size

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4db340000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4db400000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.368e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=1024,kernel=k3,placement=hbm,type=factor,vary=page-size

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 43 passes per interval, cursor 0, buffer at 0x49a8c0000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x49a980000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-size

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x475f40000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4763c0000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 149.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-size

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x583740000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x583c00000000
- per repetition: home 0 link read bytes and 1.211e+08 SMMU translation requests; level 0 link read bytes and 14.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-size

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5f3700000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5f3fc0000000
- per repetition: home 5.369e+08 link read bytes and 1.912e+08 SMMU translation requests; level 5.369e+08 link read bytes and 279.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-size

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x422840000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4229c0000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-size

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x5fa540000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x5fa700000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-size

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x4712c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x471540000000
- per repetition: home 5.369e+08 link read bytes and 4076 SMMU translation requests; level 5.369e+08 link read bytes and 84.62 SMMU translation requests; multiplexed rows voided: 0

### route/at=512m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-size

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x41f880000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x41fb00000000
- per repetition: home 0 link read bytes and 4087 SMMU translation requests; level 0 link read bytes and 7.94 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=page-order

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4ecb00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4ecfc0000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.383e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x496840000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x496cc0000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.383e+08 link read bytes and 2.255e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x43d3c0000000; level: placement hbm, 16 passes per interval, cursor 0, buffer at 0x43d880000000
- per repetition: home 0 link read bytes and 1.211e+08 SMMU translation requests; level 0 link read bytes and 3.263e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x562b00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5633c0000000
- per repetition: home 5.369e+08 link read bytes and 1.913e+08 SMMU translation requests; level 5.389e+08 link read bytes and 6.3e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x522b40000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x5233c0000000
- per repetition: home 0 link read bytes and 1.913e+08 SMMU translation requests; level 0 link read bytes and 9.577e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5b1800000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5b1980000000
- per repetition: home 5.369e+08 link read bytes and 62 SMMU translation requests; level 5.333e+08 link read bytes and 191.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x45fb40000000; level: placement hbm, 47 passes per interval, cursor 0, buffer at 0x45fcc0000000
- per repetition: home 0 link read bytes and 70 SMMU translation requests; level 0 link read bytes and 20.28 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x5cb7c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5cba40000000
- per repetition: home 5.369e+08 link read bytes and 4.43e+04 SMMU translation requests; level 5.364e+08 link read bytes and 3.437e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=64k,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x57b8c0000000; level: placement hbm, 45 passes per interval, cursor 0, buffer at 0x57bb40000000
- per repetition: home 0 link read bytes and 4.424e+04 SMMU translation requests; level 0 link read bytes and 5153 SMMU translation requests; multiplexed rows voided: 0

### route/at=9of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 7 passes per interval, cursor 0, buffer at 0x4ba780000000; level: placement cpu, 8 passes per interval, cursor 0, buffer at 0x4ba8c0000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 9.664e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=9of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 40 passes per interval, cursor 0, buffer at 0x47b3c0000000; level: placement hbm, 43 passes per interval, cursor 0, buffer at 0x47b480000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=12288,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x45cdc0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x45d420000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=12288,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 42 passes per interval, cursor 0, buffer at 0x5f0280000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x5f0820000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=12288,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x47ed00000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x47f420000000
- per repetition: home 5.369e+08 link read bytes and 7.82e+07 SMMU translation requests; level 5.369e+08 link read bytes and 7.82e+07 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=12288,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x42ec80000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x42f420000000
- per repetition: home 0 link read bytes and 7.82e+07 SMMU translation requests; level 0 link read bytes and 7.819e+07 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5b3d80000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5b4420000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=16384,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 42 passes per interval, cursor 0, buffer at 0x4dfb00000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x4e0020000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=16384,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x406a80000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x407020000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=16384,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 1 passes per interval, cursor 0, buffer at 0x561f80000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x562820000000
- per repetition: home 0 link read bytes and 1.211e+08 SMMU translation requests; level 0 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=4096,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x58e080000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x58e420000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=4096,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 42 passes per interval, cursor 0, buffer at 0x4a3480000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x4a3820000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=4096,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4475c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x447820000000
- per repetition: home 5.369e+08 link read bytes and 4417 SMMU translation requests; level 5.369e+08 link read bytes and 4830 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=4096,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 4 passes per interval, cursor 0, buffer at 0x5ec540000000; level: placement hbm, 4 passes per interval, cursor 0, buffer at 0x5ec820000000
- per repetition: home 0 link read bytes and 4414 SMMU translation requests; level 0 link read bytes and 4793 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=8192,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5802c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x580820000000
- per repetition: home 5.369e+08 link read bytes and 0 SMMU translation requests; level 5.369e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=8192,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 42 passes per interval, cursor 0, buffer at 0x42c440000000; level: placement hbm, 42 passes per interval, cursor 0, buffer at 0x42c820000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=8192,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment

- first variant A, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x594980000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x595020000000
- per repetition: home 5.369e+08 link read bytes and 4.391e+04 SMMU translation requests; level 5.369e+08 link read bytes and 1.369e+07 SMMU translation requests; multiplexed rows voided: 0

### route/at=off512m,footprint-mib=8192,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x4b79c0000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x4b8020000000
- per repetition: home 0 link read bytes and 4.391e+04 SMMU translation requests; level 0 link read bytes and 1.369e+07 SMMU translation requests; multiplexed rows voided: 0

### route/at=sorted,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=index-order

- first variant B, seed 31; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5c2f80000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5c3400000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.438e+08 link read bytes and 2.301e+05 SMMU translation requests; multiplexed rows voided: 0

