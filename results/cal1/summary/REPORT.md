# Route experiments: results

Campaign `results/cal1`, replicate `results/cal2`. Every contrast in absolute ms with its 95 % rank interval; a contrast is resolvable when its interval excludes zero, its size exceeds the floor of its family and mechanism group, and the replicate agrees on the sign. Relative values are given against the cell's normaliser (the copy route's call at home where the cell has one, else the home variant) and are never summed.

## Floors

| family | group | calibration floor ms | n | replicate floor ms | n |
|---|---|---|---|---|---|
| aa | route_axes | 0.0628 | 20 | 0.0628 | 20 |
| cross | translation | 0.6056 | 4 | 0.6056 | 4 |
| factor | route_axes | 0.0886 | 36 | 0.0886 | 36 |
| factor | translation | 0.2335 | 45 | 0.2335 | 45 |
| four | route_axes | 1.0568 | 15 | 1.0568 | 15 |
| four | translation | 0.3765 | 12 | 0.3765 | 12 |
| route | route_axes | 0.7997 | 46 | 0.7997 | 46 |

## route cells

### route, route_axes (calibration floor 0.7997 ms, replicate floor 0.7997 ms)

| cell | contrast | ms [interval] | route difference at the setting ms | relative to normaliser | verdict | checks |
|---|---|---|---|---|---|---|
| alignment=off512m,footprint-mib=8192,kernel=k3,placement=cpu | route difference (direct - copy) | 26.6250 [26.5316, 26.6742] | same | +123.4 % | resolvable | pass |
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | route difference (direct - copy) | -1.5764 [-1.5855, -1.5701] | same | -35.0 % | resolvable | pass |
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | route difference (direct - copy) | -2.5463 [-2.5486, -2.5452] | same | -83.3 % | resolvable | pass |
| f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=cpu | route difference (direct - copy) | -5.3266 [-5.3683, -5.2974] | same | -10.6 % | resolvable | pass |
| f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=hbm | route difference (direct - copy) | -36.3814 [-36.4083, -36.3591] | same | -74.2 % | resolvable | pass |
| f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=cpu | route difference (direct - copy) | -8.7542 [-8.7865, -8.7321] | same | -11.6 % | resolvable | pass |
| f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=hbm | route difference (direct - copy) | -54.5864 [-54.6311, -54.5613] | same | -74.2 % | resolvable | pass |
| f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu | route difference (direct - copy) | -0.3130 [-0.3160, -0.2861] | same | -29.8 % | below the floor (0.7997 ms); replicate agrees | pass |
| f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm | route difference (direct - copy) | -0.6558 [-0.6564, -0.6542] | same | -83.4 % | below the floor (0.7997 ms); replicate agrees | pass |
| f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=cpu | route difference (direct - copy) | -12.1358 [-12.1757, -12.1066] | same | -12.1 % | resolvable | pass |
| f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu | route difference (direct - copy) | -0.8874 [-0.8923, -0.8842] | same | -7.0 % | resolvable | pass |
| f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=hbm | route difference (direct - copy) | -10.1079 [-10.1102, -10.1057] | same | -83.3 % | resolvable | pass |
| f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=cpu | route difference (direct - copy) | -2.0800 [-2.0919, -2.0675] | same | -8.3 % | resolvable | pass |
| f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=hbm | route difference (direct - copy) | -20.3323 [-20.3380, -20.3250] | same | -83.2 % | resolvable | pass |
| f-den=10,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | route difference (direct - copy) | -2.7166 [-2.7173, -2.7160] | same | -90.0 % | resolvable | pass |
| f-den=10,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | route difference (direct - copy) | -2.5473 [-2.5482, -2.5464] | same | -97.7 % | resolvable | pass |
| f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=cpu | route difference (direct - copy) | -2.3829 [-2.3855, -1.9845] | same | -47.2 % | resolvable | pass |
| f-den=10,f-num=9,footprint-mib=1024,kernel=k1,placement=hbm | route difference (direct - copy) | -2.5499 [-2.5511, -2.5485] | same | -84.4 % | resolvable | pass |
| f-den=100,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | route difference (direct - copy) | -2.8925 [-2.8939, -2.8914] | same | -98.8 % | resolvable | pass |
| f-den=100,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | route difference (direct - copy) | -2.5508 [-2.5511, -2.5494] | same | -99.6 % | resolvable | pass |
| f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | route difference (direct - copy) | -3.2530 [-3.2535, -3.2505] | same | -99.8 % | resolvable | pass |
| f-den=1000,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | route difference (direct - copy) | -2.5557 [-2.5561, -2.5554] | same | -99.8 % | resolvable | pass |
| f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu | route difference (direct - copy) | -1.6970 [-1.6975, -1.6955] | same | -53.4 % | resolvable | pass |
| f-den=2,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm | route difference (direct - copy) | -2.5459 [-2.5469, -2.5450] | same | -90.7 % | resolvable | pass |
| f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=cpu | route difference (direct - copy) | -1.4522 [-1.4581, -1.4476] | same | -39.4 % | resolvable | pass |
| f-den=4,f-num=3,footprint-mib=1024,kernel=k1,placement=hbm | route difference (direct - copy) | -2.5424 [-2.5440, -2.5406] | same | -86.6 % | resolvable | pass |
| footprint-mib=1024,kernel=k3,placement=cpu | route difference (direct - copy) | 1.1592 [1.1548, 1.1670] | same | +27.5 % | resolvable | pass |
| footprint-mib=1024,kernel=k3,placement=hbm | route difference (direct - copy) | -2.5484 [-2.5492, -2.5471] | same | -84.3 % | resolvable | pass |
| footprint-mib=16384,kernel=k3,page-order=2m,placement=cpu | route difference (direct - copy) | -37.2369 [-37.2421, -37.2342] | same | -87.4 % | resolvable | pass |
| footprint-mib=16384,kernel=k3,page-order=2m,placement=hbm | route difference (direct - copy) | -39.0208 [-39.0286, -39.0129] | same | -94.1 % | resolvable | pass |
| footprint-mib=16384,kernel=k3,page-order=64k,placement=cpu | route difference (direct - copy) | -37.4345 [-37.4446, -37.4256] | same | -87.9 % | resolvable | pass |
| footprint-mib=16384,kernel=k3,page-order=64k,placement=hbm | route difference (direct - copy) | -40.2091 [-40.2235, -40.2026] | same | -97.0 % | resolvable | pass |
| footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu | route difference (direct - copy) | -37.2454 [-37.2513, -37.2423] | same | -87.4 % | resolvable | pass |
| footprint-mib=16384,kernel=k3,page-size=512m,placement=hbm | route difference (direct - copy) | -40.9092 [-40.9214, -40.8983] | same | -98.8 % | resolvable | pass |
| footprint-mib=16384,kernel=k3,partition=2g,placement=cpu | route difference (direct - copy) | -37.1243 [-37.1354, -37.1077] | same | -86.7 % | resolvable | pass |
| footprint-mib=16384,kernel=k3,placement=cpu | route difference (direct - copy) | 389.9693 [389.9182, 390.0602] | same | +914.5 % | resolvable | pass |
| footprint-mib=16384,kernel=k3,placement=hbm | route difference (direct - copy) | 385.7750 [385.4554, 386.0049] | same | +929.6 % | resolvable | pass |
| footprint-mib=24576,kernel=k3,placement=cpu | route difference (direct - copy) | 534.4671 [534.2727, 534.5441] | same | +839.1 % | resolvable | pass |
| footprint-mib=24576,kernel=k3,placement=hbm | route difference (direct - copy) | 529.3634 [529.2630, 529.5434] | same | +853.1 % | resolvable | pass |
| footprint-mib=256,kernel=k3,placement=cpu | route difference (direct - copy) | 3.6957 [3.6924, 3.7294] | same | +221.1 % | resolvable | pass |
| footprint-mib=256,kernel=k3,placement=hbm | route difference (direct - copy) | -0.6407 [-0.6419, -0.6403] | same | -59.2 % | below the floor (0.7997 ms); replicate agrees | pass |
| footprint-mib=32768,kernel=k3,placement=cpu | route difference (direct - copy) | 600.0745 [599.9847, 600.2344] | same | +708.0 % | resolvable | pass |
| footprint-mib=4096,kernel=k3,placement=cpu | route difference (direct - copy) | -5.5048 [-5.5238, -5.4908] | same | -49.8 % | resolvable | pass |
| footprint-mib=4096,kernel=k3,placement=hbm | route difference (direct - copy) | -5.4551 [-5.4574, -5.4540] | same | -51.4 % | resolvable | pass |
| footprint-mib=8192,kernel=k3,placement=cpu | route difference (direct - copy) | -13.8395 [-13.8429, -13.8361] | same | -64.1 % | resolvable | pass |
| footprint-mib=8192,kernel=k3,placement=hbm | route difference (direct - copy) | -13.1658 [-13.1696, -13.1627] | same | -62.9 % | resolvable | pass |

## factor cells

### factor, route_axes (calibration floor 0.0886 ms, replicate floor 0.0886 ms)

| cell | contrast | ms [interval] | route difference at the setting ms | relative to normaliser | verdict | checks |
|---|---|---|---|---|---|---|
| at=1024,f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=cpu,type=factor,vary=footprint | factor effect on direct access (level - home) | -42.1059 [-42.1157, -42.0881] | - | -94.0 % | resolvable | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=16384,kernel=k1,placement=hbm,type=factor,vary=footprint | factor effect on direct access (level - home) | -12.1583 [-12.1707, -12.1348] | - | -95.9 % | resolvable | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=cpu,type=factor,vary=footprint | factor effect on direct access (level - home) | -63.7679 [-63.7832, -63.7462] | - | -96.0 % | resolvable | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=24576,kernel=k1,placement=hbm,type=factor,vary=footprint | factor effect on direct access (level - home) | -18.4630 [-18.4766, -18.4435] | - | -97.3 % | resolvable | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=cpu,type=factor,vary=footprint | factor effect on direct access (level - home) | 2.1924 [2.1913, 2.1931] | - | +296.4 % | resolvable | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm,type=factor,vary=footprint | factor effect on direct access (level - home) | 0.3781 [0.3778, 0.3786] | - | +288.4 % | resolvable | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=cpu,type=factor,vary=footprint | factor effect on direct access (level - home) | -85.4261 [-85.4618, -85.3981] | - | -97.0 % | resolvable | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=32768,kernel=k1,placement=hbm,type=factor,vary=footprint | factor effect on direct access (level - home) | -24.7535 [-24.7783, -24.7005] | - | -98.0 % | resolvable | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=cpu,type=factor,vary=footprint | factor effect on direct access (level - home) | -8.9590 [-8.9641, -8.9559] | - | -76.4 % | resolvable | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=4096,kernel=k1,placement=hbm,type=factor,vary=footprint | factor effect on direct access (level - home) | -1.5103 [-1.5121, -1.5089] | - | -74.8 % | resolvable | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=cpu,type=factor,vary=footprint | factor effect on direct access (level - home) | -20.3203 [-20.3295, -20.3120] | - | -88.4 % | resolvable | pass |
| at=1024,f-den=1,f-num=1,footprint-mib=8192,kernel=k1,placement=hbm,type=factor,vary=footprint | factor effect on direct access (level - home) | -3.8717 [-3.8766, -3.8624] | - | -88.2 % | resolvable | pass |
| at=1024,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=footprint | factor effect on direct access (level - home) | -427.9723 [-428.0079, -427.8230] | - | -98.8 % | resolvable | pass |
| at=1024,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=footprint | factor effect on direct access (level - home) | -427.2430 [-427.3155, -427.1360] | - | -99.9 % | resolvable | pass |
| at=1024,footprint-mib=24576,kernel=k3,placement=cpu,type=factor,vary=footprint | factor effect on direct access (level - home) | -592.8144 [-592.8833, -592.7299] | - | -99.1 % | resolvable | pass |
| at=1024,footprint-mib=24576,kernel=k3,placement=hbm,type=factor,vary=footprint | factor effect on direct access (level - home) | -591.9959 [-592.0365, -591.8027] | - | -99.9 % | resolvable | pass |
| at=1024,footprint-mib=256,kernel=k3,placement=cpu,type=factor,vary=footprint | factor effect on direct access (level - home) | 0.0038 [0.0034, 0.0041] | - | +0.1 % | below the floor (0.0886 ms); replicate agrees | pass |
| at=1024,footprint-mib=256,kernel=k3,placement=hbm,type=factor,vary=footprint | factor effect on direct access (level - home) | 0.0320 [0.0315, 0.0322] | - | +7.2 % | below the floor (0.0886 ms); replicate agrees | pass |
| at=1024,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=footprint | factor effect on direct access (level - home) | -678.4305 [-678.5266, -678.3122] | - | -99.2 % | resolvable | pass |
| at=1024,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=footprint | factor effect on direct access (level - home) | -680.3936 [-680.5600, -680.2604] | - | -99.9 % | resolvable | pass |
| at=1024,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=footprint | factor effect on direct access (level - home) | -0.2142 [-0.2237, -0.2024] | - | -3.9 % | resolvable | pass |
| at=1024,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=footprint | factor effect on direct access (level - home) | -4.6937 [-4.6948, -4.6924] | - | -90.8 % | resolvable | pass |
| at=1024,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=footprint | factor effect on direct access (level - home) | -2.4369 [-2.4386, -2.4363] | - | -31.3 % | resolvable | pass |
| at=1024,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=footprint | factor effect on direct access (level - home) | -7.3160 [-7.3181, -7.3138] | - | -93.9 % | resolvable | pass |
| at=1of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | factor effect on direct access (level - home) | -2.6225 [-2.6240, -2.6218] | - | -89.7 % | resolvable | pass |
| at=1of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | factor effect on direct access (level - home) | -0.4509 [-0.4515, -0.4504] | - | -88.3 % | resolvable | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | factor effect on direct access (level - home) | -2.8935 [-2.8941, -2.8918] | - | -98.8 % | resolvable | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | factor effect on direct access (level - home) | -0.5008 [-0.5015, -0.5004] | - | -98.1 % | resolvable | pass |
| at=1of1000,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | factor effect on direct access (level - home) | -2.9190 [-2.9192, -2.9175] | - | -99.7 % | resolvable | pass |
| at=1of1000,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | factor effect on direct access (level - home) | -0.5059 [-0.5062, -0.5055] | - | -99.2 % | resolvable | pass |
| at=1of2,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | factor effect on direct access (level - home) | -1.4459 [-1.4481, -1.4449] | - | -49.3 % | resolvable | pass |
| at=1of2,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | factor effect on direct access (level - home) | -0.2486 [-0.2490, -0.2484] | - | -48.8 % | resolvable | pass |
| at=3of4,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | factor effect on direct access (level - home) | -0.6865 [-0.6880, -0.6856] | - | -23.4 % | resolvable | pass |
| at=3of4,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | factor effect on direct access (level - home) | -0.1185 [-0.1186, -0.1181] | - | -23.2 % | resolvable | pass |
| at=9of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=factor,vary=f | factor effect on direct access (level - home) | -0.2522 [-0.2537, -0.2511] | - | -8.6 % | resolvable | pass |
| at=9of10,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=factor,vary=f | factor effect on direct access (level - home) | -0.0359 [-0.0362, -0.0356] | - | -7.0 % | below the floor (0.0886 ms); replicate agrees | pass |

### factor, translation (calibration floor 0.2335 ms, replicate floor 0.2335 ms)

| cell | contrast | ms [interval] | route difference at the setting ms | relative to normaliser | verdict | checks |
|---|---|---|---|---|---|---|
| at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=partition | factor effect on direct access (level - home) | -427.9110 [-428.0050, -427.8355] | - | -98.7 % | resolvable | pass |
| at=2m,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=page-order | factor effect on direct access (level - home) | -0.1268 [-0.1333, -0.1163] | - | -2.4 % | below the floor (0.2335 ms); replicate agrees | pass |
| at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order | factor effect on direct access (level - home) | -428.0661 [-428.1798, -427.9520] | - | -98.8 % | resolvable | pass |
| at=2m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order | factor effect on direct access (level - home) | -425.2788 [-425.4349, -425.1549] | - | -99.4 % | resolvable | pass |
| at=2m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order | factor effect on direct access (level - home) | -679.4826 [-679.6670, -679.3630] | - | -99.2 % | resolvable | pass |
| at=2m,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=page-order | factor effect on direct access (level - home) | -675.5686 [-675.6942, -675.4845] | - | -99.4 % | resolvable | pass |
| at=2m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order | factor effect on direct access (level - home) | -0.1051 [-0.1169, -0.0976] | - | -1.9 % | below the floor (0.2335 ms); replicate agrees | pass |
| at=2m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order | factor effect on direct access (level - home) | -4.7130 [-4.7136, -4.7107] | - | -91.3 % | resolvable | pass |
| at=2m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order | factor effect on direct access (level - home) | -2.5360 [-2.5371, -2.5346] | - | -32.1 % | resolvable | pass |
| at=2m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order | factor effect on direct access (level - home) | -7.3966 [-7.3983, -7.3948] | - | -93.8 % | resolvable | pass |
| at=512m,footprint-mib=1024,kernel=k3,placement=cpu,type=factor,vary=page-size | factor effect on direct access (level - home) | -0.0421 [-0.0428, -0.0401] | - | -0.8 % | below the floor (0.2335 ms); replicate agrees | pass |
| at=512m,footprint-mib=1024,kernel=k3,placement=hbm,type=factor,vary=page-size | factor effect on direct access (level - home) | -0.0029 [-0.0030, -0.0024] | - | -0.6 % | below the floor (0.2335 ms); replicate agrees | pass |
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-size | factor effect on direct access (level - home) | -428.0118 [-428.2342, -427.8596] | - | -98.8 % | resolvable | pass |
| at=512m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-size | factor effect on direct access (level - home) | -426.1402 [-426.2864, -426.0598] | - | -99.9 % | resolvable | pass |
| at=512m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-size | factor effect on direct access (level - home) | -679.4150 [-679.5816, -679.3045] | - | -99.2 % | resolvable | pass |
| at=512m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-size | factor effect on direct access (level - home) | -0.1659 [-0.1794, -0.1509] | - | -3.0 % | below the floor (0.2335 ms); replicate agrees | pass |
| at=512m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-size | factor effect on direct access (level - home) | -4.6777 [-4.6811, -4.6764] | - | -90.7 % | resolvable | pass |
| at=512m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-size | factor effect on direct access (level - home) | -2.3638 [-2.3657, -2.3634] | - | -30.5 % | resolvable | pass |
| at=512m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-size | factor effect on direct access (level - home) | -7.2722 [-7.2734, -7.2703] | - | -93.8 % | resolvable | pass |
| at=64k,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=page-order | factor effect on direct access (level - home) | -0.2412 [-0.2434, -0.2375] | - | -4.5 % | resolvable | pass |
| at=64k,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order | factor effect on direct access (level - home) | -428.3271 [-428.5190, -428.2962] | - | -98.8 % | resolvable | pass |
| at=64k,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order | factor effect on direct access (level - home) | -426.1198 [-426.2460, -426.0039] | - | -99.7 % | resolvable | pass |
| at=64k,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order | factor effect on direct access (level - home) | -679.7631 [-679.9215, -679.6749] | - | -99.2 % | resolvable | pass |
| at=64k,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=page-order | factor effect on direct access (level - home) | -677.3791 [-677.5463, -677.2268] | - | -99.5 % | resolvable | pass |
| at=64k,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order | factor effect on direct access (level - home) | -0.4566 [-0.4820, -0.4440] | - | -8.2 % | resolvable | pass |
| at=64k,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order | factor effect on direct access (level - home) | -4.7422 [-4.7434, -4.7409] | - | -91.8 % | resolvable | pass |
| at=64k,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order | factor effect on direct access (level - home) | -2.7996 [-2.8035, -2.7927] | - | -35.5 % | resolvable | pass |
| at=64k,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order | factor effect on direct access (level - home) | -7.4381 [-7.4392, -7.4368] | - | -94.2 % | resolvable | pass |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | factor effect on direct access (level - home) | 0.0023 [0.0019, 0.0025] | - | +0.0 % | below the floor (0.2335 ms); replicate agrees | pass |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | factor effect on direct access (level - home) | -0.0005 [-0.0006, -0.0004] | - | -0.1 % | below the floor (0.2335 ms); replicate disagrees (0.0003 ms) | pass |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | factor effect on direct access (level - home) | -0.0239 [-0.0679, 0.0171] | - | -0.0 % | interval includes zero | pass |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | factor effect on direct access (level - home) | -3.1290 [-3.2594, -3.0320] | - | -1.1 % | resolvable | pass |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | factor effect on direct access (level - home) | 0.0009 [0.0007, 0.0012] | - | +0.0 % | below the floor (0.2335 ms); replicate agrees | pass |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | factor effect on direct access (level - home) | 0.0006 [0.0005, 0.0007] | - | +0.1 % | below the floor (0.2335 ms); replicate agrees | pass |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | factor effect on direct access (level - home) | -0.0506 [-0.0911, -0.0215] | - | -0.0 % | below the floor (0.2335 ms); replicate agrees | pass |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | factor effect on direct access (level - home) | -0.1343 [-0.1775, -0.0881] | - | -0.0 % | below the floor (0.2335 ms); replicate disagrees (0.0087 ms) | pass |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | factor effect on direct access (level - home) | 0.0007 [0.0003, 0.0009] | - | +0.0 % | below the floor (0.2335 ms); replicate agrees | pass |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | factor effect on direct access (level - home) | 0.0005 [0.0004, 0.0006] | - | +0.1 % | below the floor (0.2335 ms); replicate disagrees (-0.0018 ms) | pass |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | factor effect on direct access (level - home) | 0.0356 [0.0248, 0.0433] | - | +0.6 % | below the floor (0.2335 ms); replicate disagrees (-0.1232 ms) | pass |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | factor effect on direct access (level - home) | -0.0026 [-0.0029, -0.0022] | - | -0.0 % | below the floor (0.2335 ms); replicate agrees | pass |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | factor effect on direct access (level - home) | -0.0001 [-0.0003, 0.0002] | - | -0.0 % | interval includes zero | pass |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | factor effect on direct access (level - home) | 0.0015 [0.0014, 0.0016] | - | +0.3 % | below the floor (0.2335 ms); replicate agrees | pass |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | factor effect on direct access (level - home) | 40.7110 [40.6767, 40.7800] | - | +516.1 % | resolvable | pass |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | factor effect on direct access (level - home) | 35.5935 [35.5498, 35.6293] | - | +450.8 % | resolvable | pass |
| at=sorted,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=index-order | factor effect on direct access (level - home) | -428.4331 [-428.5756, -428.3906] | - | -98.8 % | resolvable | pass |

## four cells

### four, route_axes (calibration floor 1.0568 ms, replicate floor 1.0568 ms)

| cell | contrast | ms [interval] | route difference at the setting ms | relative to normaliser | verdict | checks |
|---|---|---|---|---|---|---|
| at=16384,footprint-mib=1024,kernel=k3,placement=cpu,type=four,vary=footprint | route difference at home | 1.9776 [1.9653, 1.9795] | same | +58.0 % | resolvable | pass |
| at=16384,footprint-mib=1024,kernel=k3,placement=cpu,type=four,vary=footprint | route difference at the level | 390.7082 [390.5477, 390.8451] | 1.9776 | +11457.9 % | resolvable | pass |
| at=16384,footprint-mib=1024,kernel=k3,placement=cpu,type=four,vary=footprint | change of the route difference | 388.7377 [388.5708, 388.8669] | 1.9776 | +19657.3 % of the route difference at home | resolvable | pass |
| at=16384,footprint-mib=1024,kernel=k3,placement=hbm,type=four,vary=footprint | route difference at home | -2.5490 [-2.5510, -2.5478] | same | -84.3 % | resolvable | pass |
| at=16384,footprint-mib=1024,kernel=k3,placement=hbm,type=four,vary=footprint | route difference at the level | 386.0234 [385.8484, 386.1097] | -2.5490 | +12763.8 % | resolvable | pass |
| at=16384,footprint-mib=1024,kernel=k3,placement=hbm,type=four,vary=footprint | change of the route difference | 388.5741 [388.4015, 388.6575] | -2.5490 | -15244.1 % of the route difference at home | resolvable | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=f | route difference at home | -1.5889 [-1.6029, -1.5836] | same | -35.2 % | resolvable | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=f | route difference at the level | -2.7303 [-2.7307, -2.7297] | -1.5889 | -60.4 % | resolvable | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=f | change of the route difference | -1.1413 [-1.1523, -1.1356] | -1.5889 | +71.8 % of the route difference at home | resolvable | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=four,vary=f | route difference at home | -2.5483 [-2.5486, -2.5481] | same | -83.3 % | resolvable | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=four,vary=f | route difference at the level | -2.5501 [-2.5504, -2.5498] | -2.5483 | -83.4 % | resolvable | pass |
| at=1of100,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=four,vary=f | change of the route difference | -0.0018 [-0.0022, -0.0016] | -2.5483 | +0.1 % of the route difference at home | below the floor (1.0568 ms); replicate disagrees (0.0050 ms) | pass |
| at=hbm,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=placement | route difference at home | -0.5130 [-0.5154, -0.5122] | same | -14.9 % | below the floor (1.0568 ms); replicate agrees | pass |
| at=hbm,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=placement | route difference at the level | -2.5443 [-2.5457, -2.5434] | -0.5130 | -73.9 % | resolvable | pass |
| at=hbm,f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=four,vary=placement | change of the route difference | -2.0312 [-2.0322, -2.0299] | -0.5130 | +395.9 % of the route difference at home | resolvable | pass |

### four, translation (calibration floor 0.3765 ms, replicate floor 0.3765 ms)

| cell | contrast | ms [interval] | route difference at the setting ms | relative to normaliser | verdict | checks |
|---|---|---|---|---|---|---|
| at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=partition | route difference at home | 390.7782 [390.6605, 390.9219] | same | +916.5 % | resolvable | pass |
| at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=partition | route difference at the level | -37.1171 [-37.1220, -37.1047] | 390.7782 | -87.0 % | resolvable | pass |
| at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=partition | change of the route difference | -427.8989 [-428.0380, -427.7727] | 390.7782 | -109.5 % of the route difference at home | resolvable | pass |
| at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-order | route difference at home | 390.7603 [390.5341, 390.8873] | same | +916.4 % | resolvable | pass |
| at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-order | route difference at the level | -37.2473 [-37.2529, -37.2404] | 390.7603 | -87.3 % | resolvable | pass |
| at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-order | change of the route difference | -428.0011 [-428.1306, -427.7870] | 390.7603 | -109.5 % of the route difference at home | resolvable | pass |
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-size | route difference at home | 390.6139 [390.5405, 390.8140] | same | +916.3 % | resolvable | pass |
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-size | route difference at the level | -37.2494 [-37.2606, -37.2385] | 390.6139 | -87.4 % | resolvable | pass |
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=four,vary=page-size | change of the route difference | -427.8886 [-428.0646, -427.7908] | 390.6139 | -109.5 % of the route difference at home | resolvable | pass |
| at=off512m,footprint-mib=8192,kernel=k3,placement=cpu,type=four,vary=alignment | route difference at home | -13.6907 [-13.7029, -13.6873] | same | -63.4 % | resolvable | pass |
| at=off512m,footprint-mib=8192,kernel=k3,placement=cpu,type=four,vary=alignment | route difference at the level | 26.9795 [26.5927, 27.0369] | -13.6907 | +125.0 % | resolvable | pass |
| at=off512m,footprint-mib=8192,kernel=k3,placement=cpu,type=four,vary=alignment | change of the route difference | 40.6758 [40.2949, 40.7549] | -13.6907 | -297.1 % of the route difference at home | resolvable | pass |

## cross cells

### cross, translation (calibration floor 0.6056 ms, replicate floor 0.6056 ms)

| cell | contrast | ms [interval] | route difference at the setting ms | relative to normaliser | verdict | checks |
|---|---|---|---|---|---|---|
| at=2m,at2=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=cross,vary=page-order,vary2=page-size | first factor's effect at the second's home | -428.0132 [-428.1289, -427.9168] | - | -98.8 % | resolvable | pass |
| at=2m,at2=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=cross,vary=page-order,vary2=page-size | first factor's effect at the second's level | -0.1111 [-0.1189, -0.1034] | - | -0.0 % | below the floor (0.6056 ms); replicate agrees | pass |
| at=2m,at2=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=cross,vary=page-order,vary2=page-size | change of the first factor's effect | 427.8965 [427.8126, 428.0257] | - | +98.7 % | resolvable | pass |
| at=2m,at2=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=cross,vary=page-order,vary2=page-size | second factor's effect at home | -427.9910 [-428.1133, -427.8965] | - | -98.8 % | interval includes zero | pass |

## aa cells

### aa, route_axes (calibration floor 0.0628 ms, replicate floor 0.0628 ms)

| cell | contrast | ms [interval] | route difference at the setting ms | relative to normaliser | verdict | checks |
|---|---|---|---|---|---|---|
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=1,type=aa | A' - A | 0.0137 [-0.0235, 0.0353] | - | +0.0 % | interval includes zero | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=10,type=aa | A' - A | 0.0338 [-0.0075, 0.0588] | - | +0.0 % | interval includes zero | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=2,type=aa | A' - A | -0.0107 [-0.0464, 0.0398] | - | -0.0 % | interval includes zero | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=3,type=aa | A' - A | -0.0733 [-0.1048, -0.0388] | - | -0.0 % | resolvable | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=4,type=aa | A' - A | 0.0441 [0.0013, 0.0986] | - | +0.0 % | below the floor (0.0628 ms); replicate disagrees (-0.0187 ms) | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=5,type=aa | A' - A | 0.0053 [-0.0532, 0.0576] | - | +0.0 % | interval includes zero | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=6,type=aa | A' - A | -0.0263 [-0.0732, 0.0019] | - | -0.0 % | interval includes zero | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=7,type=aa | A' - A | 0.0490 [0.0093, 0.0778] | - | +0.0 % | below the floor (0.0628 ms); replicate agrees | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=8,type=aa | A' - A | 0.0432 [-0.0278, 0.0795] | - | +0.0 % | interval includes zero | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=9,type=aa | A' - A | 0.0276 [-0.0014, 0.0871] | - | +0.0 % | interval includes zero | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=1,type=aa | A' - A | -0.0460 [-0.0490, -0.0419] | - | -0.6 % | below the floor (0.0628 ms); replicate agrees | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=10,type=aa | A' - A | -0.0381 [-0.0408, -0.0362] | - | -0.5 % | below the floor (0.0628 ms); replicate agrees | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=2,type=aa | A' - A | -0.0419 [-0.0440, -0.0397] | - | -0.5 % | below the floor (0.0628 ms); replicate agrees | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=3,type=aa | A' - A | -0.0417 [-0.0445, -0.0397] | - | -0.5 % | below the floor (0.0628 ms); replicate agrees | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=4,type=aa | A' - A | -0.0416 [-0.0437, -0.0407] | - | -0.5 % | below the floor (0.0628 ms); replicate agrees | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=5,type=aa | A' - A | -0.0461 [-0.0496, -0.0451] | - | -0.6 % | below the floor (0.0628 ms); replicate agrees | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=6,type=aa | A' - A | -0.0353 [-0.0370, -0.0331] | - | -0.4 % | below the floor (0.0628 ms); replicate agrees | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=7,type=aa | A' - A | -0.0475 [-0.0509, -0.0453] | - | -0.6 % | below the floor (0.0628 ms); replicate agrees | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=8,type=aa | A' - A | -0.0268 [-0.0283, -0.0232] | - | -0.3 % | below the floor (0.0628 ms); replicate agrees | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=9,type=aa | A' - A | -0.0587 [-0.0611, -0.0567] | - | -0.7 % | below the floor (0.0628 ms); replicate agrees | pass |

## Comparison points (P5.4)

### K3P at 16 GiB, CPU placement: translation against coherence

| cell | family | contrast | ms [interval] | verdict |
|---|---|---|---|---|

### K2 at 8 MiB, CPU placement: coherence against caching and scope

| cell | family | contrast | ms [interval] | verdict |
|---|---|---|---|---|


## Crossovers

See `summary/crossovers.md`:

| axis | kernel | placement | levels | route difference ms | signs | outcome | brackets | model crossover(s) |
|---|---|---|---|---|---|---|---|---|
| f | k1 | cpu | 1of1000 1of100 1of10 1of2 3of4 9of10 1of1 | -3.253 -2.893 -2.717 -1.697 -1.452 -2.383 -1.576 | - - - - - - - | no sign change on the grid |  |  |
| f | k1 | hbm | 1of1000 1of100 1of10 1of2 3of4 9of10 1of1 | -2.556 -2.551 -2.547 -2.546 -2.542 -2.550 -2.546 | - - - - - - - | no sign change on the grid |  |  |
| footprint | k1 | cpu | 256 1024 4096 8192 16384 24576 32768 | -0.313 -1.576 -0.887 -2.080 -5.327 -8.754 -12.136 | ? - - - - - - | no sign change on the grid |  |  |
| footprint | k1 | hbm | 256 1024 4096 8192 16384 24576 | -0.656 -2.546 -10.108 -20.332 -36.381 -54.586 | ? - - - - - | no sign change on the grid |  |  |
| footprint | k3 | cpu | 256 1024 4096 8192 16384 24576 32768 | 3.696 1.159 -5.505 -13.839 389.969 534.467 600.074 | + + - - + + + | 2 sign change(s) | [1024, 4096] width x4.00; model: no crossover; [8192, 16384] width x2.00; model: no crossover |  |
| footprint | k3 | hbm | 256 1024 4096 8192 16384 24576 | -0.641 -2.548 -5.455 -13.166 385.775 529.363 | ? - - - + + | 1 sign change(s) | [8192, 16384] width x2.00; model: no crossover |  |

## Per-unit costs (P11.4)

Per pair: the time difference over the counter difference, median with rank interval; given only where the counter difference excludes zero. Translation costs are per counted SMMU request, including uncounted GPU-internal translation, within one footprint and page-order level.

| cell | counter | counter difference per pass [interval] | ns per unit [interval] | pairs |
|---|---|---|---|---|
| at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=partition | SMMU translation requests | -1.21e+08 [-1.21e+08, -1.21e+08] | 3.5 [3.5, 3.5] | 10 |
| at=2g,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=partition | link read bytes | -7.68e+03 [-7.94e+03, -7.17e+03] | 55720.4 [53913.9, 59700.3] | 10 |
| at=2m,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=page-order | SMMU translation requests | 0 [0, 0] | - (counter difference includes zero) | 10 |
| at=2m,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=page-order | link read bytes | -2.3e+05 [-2.33e+05, -2.27e+05] | 0.6 [0.5, 0.6] | 10 |
| at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order | SMMU translation requests | -1.21e+08 [-1.21e+08, -1.2e+08] | 3.6 [3.6, 3.6] | 10 |
| at=2m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order | link read bytes | -2.51e+05 [-2.54e+05, -2.47e+05] | 1706.1 [1683.7, 1733.7] | 10 |
| at=2m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order | SMMU translation requests | -1.21e+08 [-1.21e+08, -1.21e+08] | 3.5 [3.5, 3.5] | 10 |
| at=2m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order | link read bytes | 0 [0, 0] | - (counter difference includes zero) | 10 |
| at=2m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order | SMMU translation requests | -1.9e+08 [-1.9e+08, -1.9e+08] | 3.6 [3.6, 3.6] | 10 |
| at=2m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order | link read bytes | -2.82e+05 [-2.85e+05, -2.78e+05] | 2407.8 [2383.5, 2448.5] | 10 |
| at=2m,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=page-order | SMMU translation requests | -1.9e+08 [-1.9e+08, -1.9e+08] | 3.6 [3.6, 3.6] | 10 |
| at=2m,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=page-order | link read bytes | 0 [0, 0] | - (counter difference includes zero) | 10 |
| at=2m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order | SMMU translation requests | 132 [128, 134] | -763.2 [-922.3, -729.4] | 30 |
| at=2m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order | link read bytes | -2.36e+05 [-2.38e+05, -2.34e+05] | 0.4 [0.4, 0.5] | 30 |
| at=2m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order | SMMU translation requests | -33 [-37.6, -27] | 143074.2 [125195.1, 174516.4] | 10 |
| at=2m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order | link read bytes | 0 [0, 0] | - (counter difference includes zero) | 10 |
| at=2m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order | SMMU translation requests | 1.96e+04 [1.89e+04, 2.04e+04] | -129.6 [-133.9, -124.5] | 10 |
| at=2m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order | link read bytes | -2.56e+05 [-2.6e+05, -2.53e+05] | 9.9 [9.7, 10.0] | 10 |
| at=2m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order | SMMU translation requests | -3.73e+04 [-3.74e+04, -3.72e+04] | 198.2 [197.8, 198.8] | 10 |
| at=2m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order | link read bytes | 0 [0, 0] | - (counter difference includes zero) | 10 |
| at=512m,footprint-mib=1024,kernel=k3,placement=cpu,type=factor,vary=page-size | SMMU translation requests | 0 [0, 0] | - (counter difference includes zero) | 10 |
| at=512m,footprint-mib=1024,kernel=k3,placement=cpu,type=factor,vary=page-size | link read bytes | -448 [-768, -256] | 84.5 [55.4, 163.1] | 9 |
| at=512m,footprint-mib=1024,kernel=k3,placement=hbm,type=factor,vary=page-size | SMMU translation requests | 0 [0, 0] | - (counter difference includes zero) | 10 |
| at=512m,footprint-mib=1024,kernel=k3,placement=hbm,type=factor,vary=page-size | link read bytes | 0 [0, 0] | - (counter difference includes zero) | 10 |
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,sequence=AABB,type=factor,vary=page-size | SMMU translation requests | -1.21e+08 [-1.21e+08, -1.21e+08] | 3.5 [3.5, 3.5] | 100 |
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,sequence=AABB,type=factor,vary=page-size | link read bytes | 256 [0, 256] | - (counter difference includes zero) | 100 |
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,sequence=ABAB,type=factor,vary=page-size | SMMU translation requests | -1.21e+08 [-1.21e+08, -1.21e+08] | 3.5 [3.5, 3.5] | 100 |
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,sequence=ABAB,type=factor,vary=page-size | link read bytes | -384 [-384, 0] | - (counter difference includes zero) | 100 |
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-size | SMMU translation requests | -1.21e+08 [-1.21e+08, -1.21e+08] | 3.5 [3.5, 3.5] | 10 |
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-size | link read bytes | 320 [-256, 384] | - (counter difference includes zero) | 10 |
| at=512m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-size | SMMU translation requests | -1.21e+08 [-1.21e+08, -1.21e+08] | 3.5 [3.5, 3.5] | 10 |
| at=512m,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-size | link read bytes | 0 [0, 0] | - (counter difference includes zero) | 10 |
| at=512m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-size | SMMU translation requests | -1.91e+08 [-1.91e+08, -1.91e+08] | 3.6 [3.6, 3.6] | 10 |
| at=512m,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-size | link read bytes | -256 [-256, 256] | - (counter difference includes zero) | 10 |
| at=512m,footprint-mib=4096,kernel=k3,placement=cpu,sequence=AABB,type=factor,vary=page-size | SMMU translation requests | 0 [0, 0] | - (counter difference includes zero) | 100 |
| at=512m,footprint-mib=4096,kernel=k3,placement=cpu,sequence=AABB,type=factor,vary=page-size | link read bytes | 0 [0, 128] | - (counter difference includes zero) | 100 |
| at=512m,footprint-mib=4096,kernel=k3,placement=cpu,sequence=ABAB,type=factor,vary=page-size | SMMU translation requests | 0 [0, 0] | - (counter difference includes zero) | 100 |
| at=512m,footprint-mib=4096,kernel=k3,placement=cpu,sequence=ABAB,type=factor,vary=page-size | link read bytes | 128 [128, 256] | -381.8 [-469.9, -284.0] | 80 |
| at=512m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-size | SMMU translation requests | 0 [0, 0] | - (counter difference includes zero) | 10 |
| at=512m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-size | link read bytes | 256 [0, 384] | - (counter difference includes zero) | 10 |
| at=512m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-size | SMMU translation requests | 0 [0, 0] | - (counter difference includes zero) | 10 |
| at=512m,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-size | link read bytes | 0 [0, 0] | - (counter difference includes zero) | 10 |
| at=512m,footprint-mib=8192,kernel=k3,placement=cpu,sequence=AABB,type=factor,vary=page-size | SMMU translation requests | 0 [0, 0] | - (counter difference includes zero) | 100 |
| at=512m,footprint-mib=8192,kernel=k3,placement=cpu,sequence=AABB,type=factor,vary=page-size | link read bytes | 256 [213, 299] | -6884.2 [-9174.0, -6119.5] | 96 |
| at=512m,footprint-mib=8192,kernel=k3,placement=cpu,sequence=ABAB,type=factor,vary=page-size | SMMU translation requests | -4.03e+03 [-4.06e+03, -3.99e+03] | 584.7 [580.2, 589.9] | 100 |
| at=512m,footprint-mib=8192,kernel=k3,placement=cpu,sequence=ABAB,type=factor,vary=page-size | link read bytes | 256 [128, 256] | -9199.8 [-9209.7, -7888.3] | 96 |
| at=512m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-size | SMMU translation requests | -3.99e+03 [-4.14e+03, -3.86e+03] | 591.6 [570.8, 612.5] | 10 |
| at=512m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-size | link read bytes | 405 [256, 555] | -5847.0 [-9241.0, -4261.2] | 10 |
| at=512m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-size | SMMU translation requests | -4.08e+03 [-4.23e+03, -3.98e+03] | 1783.1 [1718.4, 1825.5] | 10 |
| at=512m,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-size | link read bytes | 0 [0, 0] | - (counter difference includes zero) | 10 |
| at=64k,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=page-order | SMMU translation requests | 0 [0, 0] | - (counter difference includes zero) | 10 |
| at=64k,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=page-order | link read bytes | 1.46e+06 [1.46e+06, 1.48e+06] | -0.2 [-0.2, -0.2] | 10 |
| at=64k,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order | SMMU translation requests | -1.21e+08 [-1.21e+08, -1.21e+08] | 3.5 [3.5, 3.5] | 10 |
| at=64k,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-order | link read bytes | 1.46e+06 [1.44e+06, 1.47e+06] | -292.5 [-297.3, -290.4] | 10 |
| at=64k,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order | SMMU translation requests | -1.21e+08 [-1.21e+08, -1.21e+08] | 3.5 [3.5, 3.5] | 10 |
| at=64k,footprint-mib=16384,kernel=k3,placement=hbm,type=factor,vary=page-order | link read bytes | 0 [0, 0] | - (counter difference includes zero) | 10 |
| at=64k,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order | SMMU translation requests | -1.91e+08 [-1.91e+08, -1.91e+08] | 3.6 [3.6, 3.6] | 10 |
| at=64k,footprint-mib=32768,kernel=k3,placement=cpu,type=factor,vary=page-order | link read bytes | 1.98e+06 [1.98e+06, 1.99e+06] | -342.6 [-344.2, -341.2] | 10 |
| at=64k,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=page-order | SMMU translation requests | -1.9e+08 [-1.9e+08, -1.9e+08] | 3.6 [3.6, 3.6] | 10 |
| at=64k,footprint-mib=32768,kernel=k3,placement=hbm,type=factor,vary=page-order | link read bytes | 0 [0, 0] | - (counter difference includes zero) | 10 |
| at=64k,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order | SMMU translation requests | 135 [123, 144] | -3430.5 [-3725.7, -3031.2] | 10 |
| at=64k,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-order | link read bytes | -3.55e+06 [-3.63e+06, -3.53e+06] | 0.1 [0.1, 0.1] | 10 |
| at=64k,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order | SMMU translation requests | -50.5 [-63.4, -31.7] | 93942.9 [74802.6, 149326.9] | 10 |
| at=64k,footprint-mib=4096,kernel=k3,placement=hbm,type=factor,vary=page-order | link read bytes | 0 [0, 0] | - (counter difference includes zero) | 10 |
| at=64k,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order | SMMU translation requests | -9.95e+03 [-1e+04, -9.83e+03] | 281.5 [279.1, 283.8] | 10 |
| at=64k,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-order | link read bytes | -4.46e+05 [-4.63e+05, -4.12e+05] | 6.3 [6.0, 6.8] | 10 |
| at=64k,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order | SMMU translation requests | -3.91e+04 [-3.92e+04, -3.9e+04] | 190.3 [189.6, 190.6] | 10 |
| at=64k,footprint-mib=8192,kernel=k3,placement=hbm,type=factor,vary=page-order | link read bytes | 0 [0, 0] | - (counter difference includes zero) | 10 |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | SMMU translation requests | 0 [0, 0] | - (counter difference includes zero) | 100 |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | link read bytes | -128 [-128, -128] | -9.5 [-11.6, -7.3] | 75 |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | SMMU translation requests | 0 [0, 0] | - (counter difference includes zero) | 100 |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | link read bytes | 0 [0, 0] | - (counter difference includes zero) | 100 |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | SMMU translation requests | -748 [-1.19e+04, 1.16e+04] | - (counter difference includes zero) | 100 |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | link read bytes | 0 [0, 0] | - (counter difference includes zero) | 100 |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | SMMU translation requests | -1.69e+04 [-2.97e+04, 2.06e+04] | - (counter difference includes zero) | 10 |
| at=off512m,footprint-mib=12288,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | link read bytes | 0 [0, 0] | - (counter difference includes zero) | 10 |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | SMMU translation requests | 0 [0, 0] | - (counter difference includes zero) | 100 |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | link read bytes | 128 [0, 128] | - (counter difference includes zero) | 100 |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | SMMU translation requests | 0 [0, 0] | - (counter difference includes zero) | 100 |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | link read bytes | 0 [0, 0] | - (counter difference includes zero) | 100 |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | SMMU translation requests | -1.27e+04 [-1.76e+04, -3.81e+03] | 3.6 [3.4, 4.1] | 100 |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | link read bytes | 0 [0, 0] | - (counter difference includes zero) | 100 |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | SMMU translation requests | -2.72e+04 [-3.57e+04, -1.74e+04] | 4.2 [3.4, 5.0] | 100 |
| at=off512m,footprint-mib=16384,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | link read bytes | 0 [0, 0] | - (counter difference includes zero) | 100 |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | SMMU translation requests | 0 [0, 0] | - (counter difference includes zero) | 100 |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | link read bytes | 0 [0, 128] | - (counter difference includes zero) | 100 |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | SMMU translation requests | 0 [0, 0] | - (counter difference includes zero) | 100 |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | link read bytes | 0 [0, 0] | - (counter difference includes zero) | 100 |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | SMMU translation requests | 409 [367, 441] | 84.9 [62.3, 104.9] | 100 |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | link read bytes | 0 [-128, 0] | - (counter difference includes zero) | 100 |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | SMMU translation requests | 374 [343, 402] | -6.5 [-7.8, -5.3] | 100 |
| at=off512m,footprint-mib=4096,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | link read bytes | 0 [0, 0] | - (counter difference includes zero) | 100 |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | SMMU translation requests | 0 [0, 0] | - (counter difference includes zero) | 100 |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=512m,placement=cpu,type=factor,vary=alignment | link read bytes | 0 [-128, 0] | - (counter difference includes zero) | 100 |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | SMMU translation requests | 0 [0, 0] | - (counter difference includes zero) | 50 |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=512m,placement=hbm,type=factor,vary=alignment | link read bytes | 0 [0, 0] | - (counter difference includes zero) | 50 |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | SMMU translation requests | 1.36e+07 [1.36e+07, 1.37e+07] | 3.0 [3.0, 3.0] | 10 |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=64k,placement=cpu,type=factor,vary=alignment | link read bytes | -85.3 [-171, 512] | - (counter difference includes zero) | 10 |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | SMMU translation requests | 1.36e+07 [1.36e+07, 1.37e+07] | 2.6 [2.6, 2.6] | 10 |
| at=off512m,footprint-mib=8192,kernel=k3,page-size=64k,placement=hbm,type=factor,vary=alignment | link read bytes | 0 [0, 0] | - (counter difference includes zero) | 10 |
| at=sorted,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=index-order | SMMU translation requests | -1.21e+08 [-1.21e+08, -1.21e+08] | 3.5 [3.5, 3.5] | 10 |
| at=sorted,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=index-order | link read bytes | 6.9e+06 [6.9e+06, 6.9e+06] | -62.1 [-62.1, -62.1] | 10 |
