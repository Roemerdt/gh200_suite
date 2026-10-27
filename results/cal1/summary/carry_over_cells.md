# Carry-over cells: two variants run in a fixed sequence, recomputed from raw rows

Times are per repetition in ms. For each variant: its median over all its intervals, and by the variant that ran just before it. In a pattern that has a variant after itself and after the other (AABB), the carry-over is the paired difference per repeat, after the other minus after itself, as median with 95 % rank interval; a positive value means the variant is slower after the other. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | sequence | variant | route | level | ms | after A ms | after B ms | carry-over ms [interval] | relative | repeats | excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-size | AAAA | A | direct | home | 432.5579 | 432.5579 | - | - [-, -] | - | 0 | no | pass |
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-size | AABB | A | direct | home | 433.2484 | 433.2073 | 433.2951 | 0.0876 [0.0495, 0.1240] | +0.0 % | 100 | yes | pass |
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-size | AABB | B | direct | 512m | 5.3862 | 5.3874 | 5.3829 | 0.0044 [0.0041, 0.0048] | +0.1 % | 100 | yes | pass |
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-size | ABAB | A | direct | home | 433.2688 | - | 433.2688 | - [-, -] | - | 0 | no | pass |
| at=512m,footprint-mib=16384,kernel=k3,placement=cpu,type=factor,vary=page-size | ABAB | B | direct | 512m | 5.3876 | 5.3876 | - | - [-, -] | - | 0 | no | pass |
| at=512m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-size | AAAA | A | direct | home | 5.5073 | 5.5073 | - | - [-, -] | - | 0 | no | pass |
| at=512m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-size | AABB | A | direct | home | 5.5715 | 5.5727 | 5.5694 | -0.0035 [-0.0107, 0.0045] | -0.1 % | 100 | no | pass |
| at=512m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-size | AABB | B | direct | 512m | 5.3724 | 5.3724 | 5.3723 | 0.0001 [-0.0001, 0.0003] | +0.0 % | 100 | no | pass |
| at=512m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-size | ABAB | A | direct | home | 5.4720 | - | 5.4720 | - [-, -] | - | 0 | no | pass |
| at=512m,footprint-mib=4096,kernel=k3,placement=cpu,type=factor,vary=page-size | ABAB | B | direct | 512m | 5.3732 | 5.3732 | - | - [-, -] | - | 0 | no | pass |
| at=512m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-size | AAAA | A | direct | home | 7.7292 | 7.7292 | - | - [-, -] | - | 0 | no | pass |
| at=512m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-size | AABB | A | direct | home | 7.7329 | 7.7288 | 7.7356 | 0.0069 [0.0064, 0.0071] | +0.1 % | 100 | yes | pass |
| at=512m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-size | AABB | B | direct | 512m | 5.3805 | 5.3815 | 5.3793 | 0.0024 [0.0022, 0.0025] | +0.0 % | 100 | yes | pass |
| at=512m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-size | ABAB | A | direct | home | 7.7391 | - | 7.7391 | - [-, -] | - | 0 | no | pass |
| at=512m,footprint-mib=8192,kernel=k3,placement=cpu,type=factor,vary=page-size | ABAB | B | direct | 512m | 5.3822 | 5.3822 | - | - [-, -] | - | 0 | no | pass |
| f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm | AAAA | A | direct | home | 0.1313 | 0.1313 | - | - [-, -] | - | 0 | no | pass |
| f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm | AABB | A | direct | home | 0.1312 | 0.1312 | 0.1312 | 0.0000 [0.0000, 0.0000] | +0.0 % | 100 | yes | pass |
| f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm | AABB | B | copy | home | 0.7847 | 0.7846 | 0.7847 | -0.0001 [-0.0003, 0.0002] | -0.0 % | 100 | no | pass |
| f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm | ABAB | A | direct | home | 0.1312 | - | 0.1312 | - [-, -] | - | 0 | no | pass |
| f-den=1,f-num=1,footprint-mib=256,kernel=k1,placement=hbm | ABAB | B | copy | home | 0.7874 | 0.7874 | - | - [-, -] | - | 0 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu | AAAA | A | direct | home | 433.1699 | 433.1699 | - | - [-, -] | - | 0 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu | AABB | A | direct | home | 433.2129 | 433.1878 | 433.2638 | 0.0686 [0.0294, 0.1122] | +0.0 % | 100 | yes | pass |
| footprint-mib=16384,kernel=k3,placement=cpu | AABB | B | copy | home | 42.6324 | 42.6384 | 42.6209 | 0.0179 [0.0165, 0.0199] | +0.0 % | 100 | yes | pass |
| footprint-mib=16384,kernel=k3,placement=cpu | ABAB | A | direct | home | 433.2868 | - | 433.2868 | - [-, -] | - | 0 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu | ABAB | B | copy | home | 42.6387 | 42.6387 | - | - [-, -] | - | 0 | no | pass |
| footprint-mib=4096,kernel=k3,placement=cpu | AAAA | A | direct | home | 5.4869 | 5.4869 | - | - [-, -] | - | 0 | no | pass |
| footprint-mib=4096,kernel=k3,placement=cpu | AABB | A | direct | home | 5.5320 | 5.5293 | 5.5339 | 0.0050 [-0.0045, 0.0107] | +0.1 % | 100 | no | pass |
| footprint-mib=4096,kernel=k3,placement=cpu | AABB | B | copy | home | 11.0480 | 11.0487 | 11.0472 | 0.0013 [0.0003, 0.0020] | +0.0 % | 100 | yes | pass |
| footprint-mib=4096,kernel=k3,placement=cpu | ABAB | A | direct | home | 5.5629 | - | 5.5629 | - [-, -] | - | 0 | no | pass |
| footprint-mib=4096,kernel=k3,placement=cpu | ABAB | B | copy | home | 11.0467 | 11.0467 | - | - [-, -] | - | 0 | no | pass |
| footprint-mib=8192,kernel=k3,page-size=512m,placement=cpu | AAAA | A | direct | home | 5.3791 | 5.3791 | - | - [-, -] | - | 0 | no | pass |
| footprint-mib=8192,kernel=k3,page-size=512m,placement=cpu | AABB | A | direct | home | 5.3792 | 5.3791 | 5.3794 | 0.0004 [0.0001, 0.0006] | +0.0 % | 100 | yes | pass |
| footprint-mib=8192,kernel=k3,page-size=512m,placement=cpu | AABB | B | copy | home | 21.5866 | 21.5861 | 21.6027 | 0.0017 [-0.0410, 0.0046] | +0.0 % | 100 | no | pass |
| footprint-mib=8192,kernel=k3,page-size=512m,placement=cpu | ABAB | A | direct | home | 5.3796 | - | 5.3796 | - [-, -] | - | 0 | no | pass |
| footprint-mib=8192,kernel=k3,page-size=512m,placement=cpu | ABAB | B | copy | home | 21.5777 | 21.5777 | - | - [-, -] | - | 0 | no | pass |
| footprint-mib=8192,kernel=k3,placement=cpu | AAAA | A | direct | home | 7.7387 | 7.7387 | - | - [-, -] | - | 0 | no | pass |
| footprint-mib=8192,kernel=k3,placement=cpu | AABB | A | direct | home | 7.7434 | 7.7389 | 7.7464 | 0.0077 [0.0072, 0.0084] | +0.1 % | 100 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu | AABB | B | copy | home | 21.5815 | 21.5864 | 21.5754 | 0.0108 [0.0098, 0.0125] | +0.0 % | 100 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu | ABAB | A | direct | home | 7.7474 | - | 7.7474 | - [-, -] | - | 0 | no | pass |
| footprint-mib=8192,kernel=k3,placement=cpu | ABAB | B | copy | home | 21.5872 | 21.5872 | - | - [-, -] | - | 0 | no | pass |
