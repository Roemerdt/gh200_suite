# Factor cells: the direct route at a level of one factor against its home level, recomputed from raw rows

Times are per pass in ms. The factor effect on direct access is level minus home within a repeat, as median with its 95 % rank interval; a positive value means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | level | home ms | level ms | effect ms [interval] | relative to home | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0394 | 0.3751 | 0.3357 [0.3354, 0.3359] | +853.2 % | 10 | yes | pass |
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0161 | 0.0301 | 0.0141 [0.0141, 0.0141] | +87.6 % | 10 | yes | pass |
| at=1024,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=working-set,working-set-mib=32 | working-set | 1024 | 1.4842 | 47.0197 | 45.5355 [45.5161, 45.5683] | +3068.0 % | 10 | yes | pass |
| at=1024,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=working-set,working-set-mib=32 | working-set | 1024 | 0.0968 | 5.1628 | 5.0660 [5.0624, 5.0683] | +5233.0 % | 10 | yes | pass |
| at=1024,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint | footprint | 1024 | 0.0758 | 0.8147 | 0.7389 [0.7377, 0.7394] | +974.8 % | 10 | yes | pass |
| at=1024,footprint-mib=256,kernel=k6,placement=cpu,type=factor,update=atomic,vary=footprint | footprint | 1024 | 1.5161 | 6.0359 | 4.5195 [4.5154, 4.5261] | +298.1 % | 10 | yes | pass |
| at=1024,footprint-mib=256,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint | footprint | 1024 | 0.2039 | 0.8166 | 0.6126 [0.6119, 0.6137] | +300.5 % | 10 | yes | pass |
| at=1024,footprint-mib=4096,kernel=k6,placement=cpu,type=factor,update=atomic,vary=footprint | footprint | 1024 | 24.1211 | 5.8624 | -18.2577 [-18.2965, -18.2424] | -75.7 % | 10 | yes | pass |
| at=1024,footprint-mib=4096,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint | footprint | 1024 | 3.2766 | 0.8140 | -2.4625 [-2.4656, -2.4588] | -75.2 % | 10 | yes | pass |
| at=1024,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=factor,vary=keys | keys | 1024 | 191.3091 | 12.4952 | -178.8141 [-178.8182, -178.8069] | -93.5 % | 10 | yes | pass |
| at=1024,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=factor,vary=keys | keys | 1024 | 12.5380 | 0.7660 | -11.7720 [-11.7723, -11.7712] | -93.9 % | 10 | yes | pass |
| at=1024,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,type=factor,vary=keys | keys | 1024 | 8.3276 | 12.4865 | 4.1612 [4.1510, 4.1643] | +50.0 % | 10 | yes | pass |
| at=1024,footprint-mib=8,kernel=k6,keys=1048576,placement=hbm,type=factor,vary=keys | keys | 1024 | 0.1790 | 0.7659 | 0.5869 [0.5867, 0.5870] | +327.8 % | 10 | yes | pass |
| at=4,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=repeat | repeat | 4 | 6.0536 | 18.0357 | 11.9811 [11.9641, 11.9973] | +197.9 % | 10 | yes | pass |
| at=4,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=repeat | repeat | 4 | 0.8150 | 1.6389 | 0.8236 [0.8231, 0.8264] | +101.1 % | 10 | yes | pass |
| at=8,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=working-set,working-set-mib=32 | working-set | 8 | 1.4944 | 0.0393 | -1.4552 [-1.4560, -1.4543] | -97.4 % | 10 | yes | pass |
| at=8,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=working-set,working-set-mib=32 | working-set | 8 | 0.0981 | 0.0161 | -0.0820 [-0.0822, -0.0820] | -83.6 % | 10 | yes | pass |
| at=hbm,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=placement | placement | hbm | 10.0580 | 10.0574 | -0.0020 [-0.0042, 0.0004] | -0.0 % | 100 | no | pass |
| at=hbm,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=plain,vary=placement | placement | hbm | 2.4001 | 2.3985 | -0.0017 [-0.0036, -0.0002] | -0.1 % | 100 | yes | pass |
| at=hbm,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=placement | placement | hbm | 12.9864 | 18.1656 | 5.2796 [5.1774, 5.4324] | +40.7 % | 90 | yes | pass |
| at=hbm,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=plain,vary=placement | placement | hbm | 2.3497 | 2.7292 | 0.3785 [0.3667, 0.3858] | +16.1 % | 10 | yes | pass |
| at=line,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=layout | layout | line | 6.0509 | 3.4976 | -2.5550 [-2.5612, -2.5426] | -42.2 % | 10 | yes | pass |
| at=line,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=layout | layout | line | 0.8177 | 0.3396 | -0.4782 [-0.4795, -0.4771] | -58.5 % | 10 | yes | pass |
| at=none,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=tiling | tiling | none | 26.2998 | 37.7425 | 11.4553 [11.3652, 11.5939] | +43.6 % | 10 | yes | pass |
| at=none,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=tiling | tiling | none | 3.2590 | 2.7478 | -0.5109 [-0.5416, -0.5070] | -15.7 % | 10 | yes | pass |
| at=plain,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | plain | 10.0751 | 2.3782 | -7.6973 [-7.7315, -7.6922] | -76.4 % | 10 | yes | pass |
| at=plain,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | plain | 10.0742 | 2.3444 | -7.7326 [-7.7578, -7.7168] | -76.8 % | 20 | yes | pass |
| at=plain,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | plain | 6.0418 | 6.0176 | -0.0248 [-0.0273, -0.0218] | -0.4 % | 100 | yes | pass |
| at=plain,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | plain | 0.8170 | 0.7683 | -0.0487 [-0.0499, -0.0472] | -6.0 % | 10 | yes | pass |
| at=plain,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | plain | 0.0747 | 0.0792 | 0.0045 [0.0045, 0.0046] | +6.1 % | 10 | yes | pass |
| at=plain,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | plain | 12.6660 | 2.3262 | -10.3425 [-10.4336, -10.2887] | -81.7 % | 10 | yes | pass |
| at=plain,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | plain | 17.7261 | 2.7364 | -14.9909 [-15.0449, -14.9394] | -84.6 % | 10 | yes | pass |
| at=returned,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | returned | 10.0678 | 40.9943 | 30.9288 [30.7393, 31.3740] | +307.2 % | 10 | yes | pass |
| at=returned,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | returned | 10.0607 | 41.0693 | 31.0173 [30.7976, 31.1065] | +308.3 % | 10 | yes | pass |
| at=returned,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | returned | 6.0407 | 6.0850 | 0.0443 [0.0422, 0.0474] | +0.7 % | 10 | yes | pass |
| at=returned,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | returned | 0.8167 | 0.8977 | 0.0810 [0.0798, 0.0815] | +9.9 % | 10 | yes | pass |
| at=returned,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | returned | 0.0743 | 0.1363 | 0.0620 [0.0619, 0.0620] | +83.4 % | 10 | yes | pass |
| at=returned,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | returned | 12.9670 | 45.6662 | 32.7325 [32.1295, 33.0667] | +252.4 % | 20 | yes | pass |
| at=returned,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | returned | 17.7325 | 49.0994 | 30.9992 [30.1320, 31.4743] | +174.8 % | 100 | yes | pass |
| at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=generator | generator | rmat | 30.8132 | 188.6881 | 157.8644 [157.8322, 157.9262] | +512.3 % | 10 | yes | pass |
| at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=generator | generator | rmat | 1.2712 | 65.5157 | 64.2449 [63.6955, 64.7560] | +5053.8 % | 10 | yes | pass |
| at=rmat,footprint-mib=8192,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=generator | generator | rmat | 247.2807 | 993.5360 | 746.2649 [746.1018, 746.4386] | +301.8 % | 10 | yes | pass |
| at=rmat,footprint-mib=8192,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=generator | generator | rmat | 15.1111 | 395.8313 | 380.7208 [378.2312, 383.2824] | +2519.5 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing | sharing | shared | 0.0201 | 0.0210 | 0.0008 [0.0008, 0.0009] | +4.2 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0202 | 0.0212 | 0.0010 [0.0009, 0.0010] | +4.9 % | 30 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0204 | 0.0207 | 0.0003 [0.0003, 0.0004] | +1.5 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing | sharing | shared | 0.0201 | 0.0208 | 0.0006 [0.0006, 0.0007] | +3.2 % | 80 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0203 | 0.0210 | 0.0008 [0.0007, 0.0009] | +3.9 % | 50 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0202 | 0.0202 | 0.0000 [-0.0000, 0.0001] | +0.1 % | 100 | no | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing | sharing | shared | 0.1923 | 0.1922 | -0.0001 [-0.0002, -0.0001] | -0.1 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 0.1925 | 0.3795 | 0.1870 [0.1854, 0.1873] | +97.2 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing | sharing | shared | 0.1924 | 0.1930 | 0.0006 [0.0005, 0.0007] | +0.3 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0377 | 0.1633 | 0.1256 [0.1251, 0.1265] | +333.5 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0347 | 0.1836 | 0.1490 [0.1485, 0.1494] | +429.7 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0382 | 0.0366 | -0.0015 [-0.0017, -0.0014] | -3.9 % | 60 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing | sharing | shared | 0.1924 | 0.1937 | 0.0014 [0.0012, 0.0014] | +0.7 % | 50 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 0.1912 | 0.3760 | 0.1847 [0.1846, 0.1850] | +96.6 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing | sharing | shared | 0.1927 | 0.1930 | 0.0003 [0.0001, 0.0004] | +0.2 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0373 | 0.1689 | 0.1316 [0.1311, 0.1319] | +352.4 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0356 | 0.1808 | 0.1450 [0.1447, 0.1458] | +407.6 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0374 | 0.0364 | -0.0009 [-0.0010, -0.0009] | -2.5 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0150 | 0.0597 | 0.0448 [0.0444, 0.0451] | +299.3 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0150 | 0.0557 | 0.0405 [0.0400, 0.0408] | +269.1 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0150 | 0.0155 | 0.0005 [0.0004, 0.0005] | +3.1 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0152 | 0.0571 | 0.0421 [0.0417, 0.0422] | +277.7 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0150 | 0.0540 | 0.0390 [0.0384, 0.0394] | +260.9 % | 90 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0152 | 0.0156 | 0.0005 [0.0004, 0.0005] | +3.2 % | 40 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0547 | 0.2264 | 0.1716 [0.1703, 0.1738] | +313.7 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0494 | 0.2646 | 0.2152 [0.2143, 0.2155] | +435.4 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0506 | 0.0504 | -0.0002 [-0.0003, -0.0000] | -0.4 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0548 | 0.2329 | 0.1779 [0.1774, 0.1784] | +324.7 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0490 | 0.2639 | 0.2148 [0.2145, 0.2151] | +438.7 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0501 | 0.0499 | -0.0003 [-0.0004, -0.0002] | -0.5 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=factor,vary=sharing | sharing | shared | 30.8176 | 30.3520 | -0.4603 [-0.4761, -0.4489] | -1.5 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=factor,vary=sharing | sharing | shared | 1.2749 | 1.2739 | -0.0012 [-0.0015, -0.0009] | -0.1 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0468 | 0.0642 | 0.0173 [0.0172, 0.0176] | +37.0 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0474 | 0.0669 | 0.0196 [0.0189, 0.0202] | +41.3 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0461 | 0.0460 | -0.0001 [-0.0001, -0.0000] | -0.2 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0459 | 0.0655 | 0.0194 [0.0192, 0.0199] | +42.3 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0457 | 0.0669 | 0.0212 [0.0211, 0.0215] | +46.4 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0464 | 0.0463 | -0.0000 [-0.0001, 0.0001] | -0.1 % | 100 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32 | sharing | shared | 1.4958 | 1.4993 | 0.0034 [0.0031, 0.0038] | +0.2 % | 40 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8 | sharing | shared | 0.0457 | 0.0458 | 0.0001 [0.0000, 0.0001] | +0.2 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 1.5140 | 1.5089 | -0.0050 [-0.0055, -0.0046] | -0.3 % | 60 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0521 | 0.0535 | 0.0014 [0.0013, 0.0016] | +2.7 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 1.5206 | 1.5076 | -0.0150 [-0.0155, -0.0128] | -1.0 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8 | sharing | shared | 0.0542 | 0.0549 | 0.0008 [0.0006, 0.0011] | +1.4 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32 | sharing | shared | 0.1053 | 0.1089 | 0.0036 [0.0032, 0.0038] | +3.4 % | 30 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.1151 | 0.1158 | 0.0008 [0.0004, 0.0010] | +0.7 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.1329 | 0.1335 | 0.0006 [0.0003, 0.0011] | +0.5 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32 | sharing | shared | 1.4912 | 1.5156 | 0.0244 [0.0228, 0.0252] | +1.6 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8 | sharing | shared | 0.0463 | 0.0466 | 0.0003 [0.0002, 0.0004] | +0.5 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 1.5062 | 1.5087 | 0.0027 [0.0024, 0.0029] | +0.2 % | 50 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0525 | 0.0528 | 0.0003 [0.0000, 0.0005] | +0.5 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 1.5130 | 1.5325 | 0.0197 [0.0181, 0.0202] | +1.3 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8 | sharing | shared | 0.0524 | 0.0531 | 0.0008 [0.0007, 0.0010] | +1.5 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32 | sharing | shared | 0.1053 | 0.1093 | 0.0039 [0.0036, 0.0042] | +3.7 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.1154 | 0.1137 | -0.0017 [-0.0019, -0.0016] | -1.5 % | 60 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.1286 | 0.1316 | 0.0031 [0.0028, 0.0034] | +2.4 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01 | sharing | shared | 5.4347 | 5.4305 | -0.0043 [-0.0049, -0.0040] | -0.1 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1 | sharing | shared | 5.4244 | 5.4207 | -0.0037 [-0.0157, -0.0029] | -0.1 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1 | sharing | shared | 5.3969 | 5.3946 | -0.0026 [-0.0036, -0.0021] | -0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01 | sharing | shared | 5.4344 | 5.4342 | -0.0001 [-0.0006, 0.0002] | -0.0 % | 100 | no | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1 | sharing | shared | 5.4354 | 5.4259 | -0.0025 [-0.0036, -0.0021] | -0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1 | sharing | shared | 5.4140 | 5.4241 | -0.0028 [-0.0042, -0.0021] | -0.1 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 7.2598 | 7.2244 | -0.0348 [-0.0388, -0.0314] | -0.5 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 7.2621 | 7.2325 | -0.0289 [-0.0308, -0.0254] | -0.4 % | 90 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01 | sharing | shared | 433.5659 | 433.5986 | 0.0454 [0.0034, 0.0886] | +0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1 | sharing | shared | 433.5674 | 433.5937 | 0.0370 [-0.0060, 0.0692] | +0.0 % | 100 | no | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1 | sharing | shared | 433.5646 | 433.6366 | 0.0569 [0.0148, 0.0964] | +0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01 | sharing | shared | 433.5638 | 433.5466 | -0.0008 [-0.0636, 0.0335] | -0.0 % | 100 | no | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1 | sharing | shared | 433.5513 | 433.5736 | 0.0258 [-0.0141, 0.0612] | +0.0 % | 100 | no | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1 | sharing | shared | 433.5995 | 433.5998 | -0.0104 [-0.0457, 0.0446] | -0.0 % | 100 | no | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing | sharing | shared | 26.4284 | 23.4764 | -2.9473 [-2.9982, -2.8626] | -11.2 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing | sharing | shared | 3.2654 | 3.2458 | -0.0188 [-0.0216, -0.0179] | -0.6 % | 50 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | sharing | shared | 26.5597 | 23.5357 | -3.0118 [-3.0419, -2.9410] | -11.3 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | sharing | shared | 26.6628 | 23.4693 | -3.1856 [-3.2158, -3.1467] | -11.9 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | sharing | shared | 26.1390 | 23.6074 | -2.5375 [-2.5463, -2.4957] | -9.7 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | sharing | shared | 3.4752 | 3.6098 | 0.1348 [0.1282, 0.1389] | +3.9 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | sharing | shared | 3.4790 | 3.6014 | 0.1215 [0.1115, 0.1332] | +3.5 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | sharing | shared | 3.4819 | 3.5773 | 0.0938 [0.0902, 0.1025] | +2.7 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | sharing | shared | 26.5339 | 23.6009 | -2.9335 [-2.9731, -2.9021] | -11.1 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | sharing | shared | 26.5775 | 23.5442 | -3.0278 [-3.0677, -3.0209] | -11.4 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | sharing | shared | 26.7131 | 23.5686 | -3.1435 [-3.1654, -3.0975] | -11.8 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | sharing | shared | 3.4886 | 3.6185 | 0.1287 [0.1228, 0.1342] | +3.7 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | sharing | shared | 3.4633 | 3.5926 | 0.1296 [0.1245, 0.1324] | +3.7 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | sharing | shared | 3.4734 | 3.5104 | 0.0365 [0.0347, 0.0399] | +1.1 % | 30 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01 | sharing | shared | 8.0734 | 8.0996 | 0.0261 [0.0247, 0.0293] | +0.3 % | 30 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1 | sharing | shared | 8.0839 | 8.1022 | 0.0182 [0.0162, 0.0203] | +0.2 % | 100 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=1 | sharing | shared | 8.0957 | 8.1182 | 0.0225 [0.0207, 0.0249] | +0.3 % | 70 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01 | sharing | shared | 8.0876 | 8.1024 | 0.0145 [0.0128, 0.0160] | +0.2 % | 100 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1 | sharing | shared | 8.0846 | 8.1007 | 0.0158 [0.0146, 0.0185] | +0.2 % | 100 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=1 | sharing | shared | 8.0820 | 8.1024 | 0.0191 [0.0173, 0.0210] | +0.2 % | 30 | yes | pass |
| at=stadd,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | stadd | 10.0560 | 8.0847 | -1.9710 [-1.9840, -1.9615] | -19.6 % | 10 | yes | pass |
| at=stadd,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | stadd | 10.0949 | 8.0908 | -2.0009 [-2.0202, -1.9824] | -19.8 % | 10 | yes | pass |
| at=stadd,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | stadd | 12.9971 | 9.0720 | -3.8776 [-3.9782, -3.6923] | -29.8 % | 30 | yes | pass |
| at=stadd,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | stadd | 17.3065 | 11.4375 | -5.8715 [-5.9728, -5.6427] | -33.9 % | 10 | yes | pass |
| at=tiles,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=tiling,working-set-mib=8 | tiling | tiles | 0.0393 | 0.0367 | -0.0026 [-0.0027, -0.0026] | -6.6 % | 10 | yes | pass |
| at=tiles,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=tiling,working-set-mib=8 | tiling | tiles | 0.0162 | 0.0155 | -0.0007 [-0.0007, -0.0007] | -4.5 % | 10 | yes | pass |
| at=warp,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,type=factor,vary=strategy | strategy | warp | 8.2423 | 9.6251 | 1.3826 [1.3762, 1.3909] | +16.8 % | 10 | yes | pass |
| at=warp,footprint-mib=8,kernel=k6,keys=1048576,placement=hbm,type=factor,vary=strategy | strategy | warp | 0.1791 | 0.2863 | 0.1072 [0.1070, 0.1075] | +59.8 % | 10 | yes | pass |

## Host phases

The CPU phase before every pass, timed on the CPU clock (ms per pass), and the state check's median load latency on the preparing core after the phase (ns per sampled load), per variant.

| cell | home CPU ms | home state ns | level CPU ms | level state ns |
|---|---|---|---|---|
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing | 0.2827 | 62.8 | 0.2749 | 65.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | 0.2428 | 63.9 | 0.2454 | 65.6 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing | 0.2671 | 194.2 | 0.2601 | 69.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing | 0.2626 | 63.9 | 0.2604 | 64.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | 0.2406 | 63.1 | 0.2421 | 63.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing | 0.2473 | 187.6 | 0.2451 | 71.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing | 5.3053 | 62.4 | 5.9204 | 107.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | 2.7747 | 74.6 | 3.3405 | 79.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing | 3.9575 | 210.4 | 3.9424 | 219.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | 5.0550 | 77.6 | 5.9148 | 129.8 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | 2.8401 | 116.9 | 3.5694 | 155.8 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | 3.9714 | 457.4 | 3.8999 | 419.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing | 5.2357 | 70.2 | 5.3904 | 76.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | 2.7345 | 99.6 | 2.6676 | 116.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing | 3.4441 | 194.2 | 3.4424 | 207.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | 4.9602 | 61.2 | 5.1761 | 103.8 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | 2.8782 | 281.2 | 3.1501 | 301.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | 3.2459 | 459.1 | 3.2556 | 420.6 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | 1.1875 | 70.6 | 1.2662 | 79.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | 0.9267 | 70.0 | 1.0190 | 75.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | 1.0427 | 357.1 | 1.0430 | 375.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | 1.1777 | 67.1 | 1.1996 | 80.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | 0.9106 | 66.1 | 0.9330 | 73.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | 0.9843 | 379.1 | 0.9838 | 382.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | 7.4124 | 172.2 | 8.0824 | 223.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | 4.1072 | 88.6 | 5.1590 | 153.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | 5.6938 | 481.4 | 5.5500 | 462.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | 7.2090 | 297.1 | 7.4976 | 370.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | 3.9742 | 203.6 | 4.2821 | 247.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | 4.4500 | 485.4 | 4.4938 | 469.4 |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=factor,vary=sharing | 1.6723 | - | 1.6505 | - |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=factor,vary=sharing | 2.3158 | - | 3.6943 | - |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8 | 0.9290 | 73.0 | 0.9241 | 78.0 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8 | 0.6602 | 68.5 | 0.6560 | 71.0 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8 | 0.7107 | 207.4 | 0.7093 | 196.1 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8 | 0.8743 | 69.8 | 0.8676 | 78.1 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8 | 0.5212 | 70.4 | 0.5238 | 73.1 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8 | 0.6446 | 194.0 | 0.6451 | 194.9 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32 | 0.5812 | 73.6 | 0.5959 | 108.9 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8 | 0.5856 | 96.2 | 0.5891 | 150.0 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32 | 4.2879 | 153.4 | 4.3103 | 202.0 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8 | 4.1295 | 71.1 | 4.1326 | 130.2 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32 | 29.2008 | 260.2 | 29.6141 | 263.6 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8 | 27.9164 | 279.6 | 27.9191 | 284.6 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32 | 0.9886 | 71.6 | 0.9929 | 110.6 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32 | 5.3710 | 359.9 | 5.4018 | 416.6 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32 | 31.9161 | 527.0 | 32.1966 | 570.2 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32 | 0.5484 | 63.2 | 0.5526 | 100.5 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8 | 0.5592 | 73.5 | 0.5598 | 121.4 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32 | 3.5740 | 141.0 | 3.5771 | 214.2 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8 | 3.5325 | 109.5 | 3.5348 | 152.1 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32 | 22.4265 | 267.2 | 22.4087 | 272.1 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8 | 20.0023 | 266.4 | 20.0017 | 301.6 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32 | 0.9741 | 73.0 | 0.9589 | 111.2 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32 | 4.4806 | 321.9 | 4.4737 | 347.1 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32 | 27.9107 | 551.1 | 30.1490 | 576.0 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01 | 0.5987 | 66.4 | 0.7399 | 99.6 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1 | 4.5654 | 88.2 | 5.1324 | 140.2 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1 | 27.1876 | 255.5 | 26.6720 | 275.5 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01 | 0.5661 | 69.4 | 0.6577 | 98.5 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1 | 3.6825 | 124.0 | 3.8583 | 160.4 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1 | 22.4444 | 244.5 | 22.4113 | 274.4 |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | 1.8662 | 88.9 | 2.8180 | 101.9 |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | 1.8627 | 116.5 | 2.8689 | 135.6 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01 | 8.3585 | 185.0 | 8.7199 | 216.4 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1 | 46.3860 | 310.1 | 46.3328 | 325.5 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1 | 342.8436 | 373.8 | 342.2000 | 365.8 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01 | 6.7369 | 191.2 | 7.6348 | 223.0 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1 | 29.9591 | 287.6 | 30.0125 | 292.5 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1 | 265.6709 | 382.4 | 265.7687 | 364.0 |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing | 27.6540 | - | 28.1438 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing | 62.8182 | - | 62.4452 | - |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | 0.4603 | 65.9 | 0.5070 | 74.5 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | 2.4308 | 115.6 | 2.6516 | 162.4 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | 15.3581 | 256.6 | 13.7008 | 279.2 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | 0.8811 | 75.2 | 0.9276 | 114.4 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | 3.0645 | 228.5 | 3.0313 | 278.4 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | 19.3626 | 494.0 | 19.3968 | 518.9 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | 0.3921 | 68.4 | 0.4102 | 90.9 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | 1.8953 | 108.8 | 2.0137 | 187.5 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | 12.4113 | 261.4 | 13.1744 | 271.8 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | 0.8023 | 89.5 | 0.8245 | 113.4 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | 2.5713 | 231.5 | 2.5869 | 283.6 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | 16.2296 | 497.6 | 16.2304 | 543.6 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01 | 4.8055 | 334.4 | 4.8563 | 326.8 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1 | 26.2410 | 554.4 | 26.1119 | 582.4 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=1 | 192.8750 | 640.2 | 197.6020 | 627.9 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01 | 3.9295 | 350.4 | 3.9270 | 372.4 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1 | 23.5781 | 549.5 | 23.6546 | 576.9 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=1 | 163.6507 | 593.4 | 163.5209 | 615.4 |

## Per cell

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=rotated,working-set-mib=8

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 509 passes per interval, cursor 1, buffer at 0x5fcec0000000; level: placement cpu, 54 passes per interval, cursor 1, buffer at 0x5fcfc0000000
- per repetition: home 8.43e+06 link read bytes and 0 SMMU translation requests; level 1.341e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=rotated,working-set-mib=8

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 1247 passes per interval, cursor 1, buffer at 0x5c3f00000000; level: placement hbm, 666 passes per interval, cursor 1, buffer at 0x5c4040000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=working-set,working-set-mib=32

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x4bea40000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4beb00000000
- per repetition: home 5.366e+08 link read bytes and 0 SMMU translation requests; level 1.718e+10 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=working-set,working-set-mib=32

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 208 passes per interval, cursor 1, buffer at 0x4f1000000000; level: placement hbm, 4 passes per interval, cursor 0, buffer at 0x4f1140000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 264 passes per interval, cursor 0, buffer at 0x5789c0000000; level: placement hbm, 25 passes per interval, cursor 0, buffer at 0x578a40000000
- per repetition: home 0 link read bytes and 2.773 SMMU translation requests; level 0 link read bytes and 1493 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=256,kernel=k6,placement=cpu,type=factor,update=atomic,vary=footprint

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x4f9300000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4f9400000000
- per repetition: home 0 link read bytes and 313.9 SMMU translation requests; level 0 link read bytes and 4193 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=256,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 99 passes per interval, cursor 0, buffer at 0x5659c0000000; level: placement hbm, 25 passes per interval, cursor 0, buffer at 0x565a80000000
- per repetition: home 0 link read bytes and 107.2 SMMU translation requests; level 0 link read bytes and 1234 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=4096,kernel=k6,placement=cpu,type=factor,update=atomic,vary=footprint

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x533ac0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x533c40000000
- per repetition: home 0 link read bytes and 6.645e+04 SMMU translation requests; level 0 link read bytes and 4216 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=4096,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 7 passes per interval, cursor 0, buffer at 0x538a00000000; level: placement hbm, 25 passes per interval, cursor 0, buffer at 0x538b80000000
- per repetition: home 0 link read bytes and 1.753e+04 SMMU translation requests; level 0 link read bytes and 1267 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=factor,vary=keys

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5ca000000000; level: placement cpu, 2 passes per interval, cursor 0, buffer at 0x5ca080000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=factor,vary=keys

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x53ff80000000; level: placement hbm, 27 passes per interval, cursor 0, buffer at 0x540000000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,type=factor,vary=keys

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x452600000000; level: placement cpu, 2 passes per interval, cursor 0, buffer at 0x452680000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8,kernel=k6,keys=1048576,placement=hbm,type=factor,vary=keys

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 112 passes per interval, cursor 0, buffer at 0x401d80000000; level: placement hbm, 27 passes per interval, cursor 0, buffer at 0x401e40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=4,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=repeat

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5527c0000000; level: placement cpu, 2 passes per interval, cursor 0, buffer at 0x5528c0000000
- per repetition: home 0 link read bytes and 4187 SMMU translation requests; level 0 link read bytes and 8290 SMMU translation requests; multiplexed rows voided: 0

### route/at=4,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=repeat

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 25 passes per interval, cursor 0, buffer at 0x551880000000; level: placement hbm, 13 passes per interval, cursor 0, buffer at 0x551940000000
- per repetition: home 0 link read bytes and 1299 SMMU translation requests; level 0 link read bytes and 1944 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=working-set,working-set-mib=32

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x58bd00000000; level: placement cpu, 511 passes per interval, cursor 1, buffer at 0x58be00000000
- per repetition: home 5.366e+08 link read bytes and 0 SMMU translation requests; level 8.43e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=working-set,working-set-mib=32

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 205 passes per interval, cursor 1, buffer at 0x5dbf00000000; level: placement hbm, 1246 passes per interval, cursor 1, buffer at 0x5dc040000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=hbm,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=placement

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x46b080000000; level: placement hbm, 2 passes per interval, cursor 0, buffer at 0x46b100000000
- no hardware counters in this cell

### route/at=hbm,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=plain,vary=placement

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 9 passes per interval, cursor 0, buffer at 0x5a4bc0000000; level: placement hbm, 9 passes per interval, cursor 0, buffer at 0x5a4c80000000
- no hardware counters in this cell

### route/at=hbm,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=placement

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x5eddc0000000; level: placement hbm, 2 passes per interval, cursor 0, buffer at 0x5ede80000000
- no hardware counters in this cell

### route/at=hbm,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=plain,vary=placement

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 9 passes per interval, cursor 0, buffer at 0x42a680000000; level: placement hbm, 8 passes per interval, cursor 0, buffer at 0x42a740000000
- no hardware counters in this cell

### route/at=line,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=layout

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x536980000000; level: placement cpu, 6 passes per interval, cursor 0, buffer at 0x536a80000000
- per repetition: home 0 link read bytes and 4243 SMMU translation requests; level 0 link read bytes and 2886 SMMU translation requests; multiplexed rows voided: 0

### route/at=line,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=layout

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 25 passes per interval, cursor 0, buffer at 0x5b6f80000000; level: placement hbm, 59 passes per interval, cursor 0, buffer at 0x5b70c0000000
- per repetition: home 0 link read bytes and 1236 SMMU translation requests; level 0 link read bytes and 421.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=none,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=tiling

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x406780000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4068c0000000
- per repetition: home 6.422e+09 link read bytes and 3.606e+04 SMMU translation requests; level 1.311e+10 link read bytes and 3.506e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=none,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=tiling

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 7 passes per interval, cursor 0, buffer at 0x555380000000; level: placement hbm, 8 passes per interval, cursor 0, buffer at 0x555480000000
- per repetition: home 0 link read bytes and 6032 SMMU translation requests; level 0 link read bytes and 9437 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x477700000000; level: placement cpu, 9 passes per interval, cursor 0, buffer at 0x477780000000
- no hardware counters in this cell

### route/at=plain,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x4a6ec0000000; level: placement hbm, 9 passes per interval, cursor 0, buffer at 0x4a6f80000000
- no hardware counters in this cell

### route/at=plain,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x411dc0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x411ec0000000
- per repetition: home 0 link read bytes and 4208 SMMU translation requests; level 1.074e+09 link read bytes and 4556 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 25 passes per interval, cursor 0, buffer at 0x4b5100000000; level: placement hbm, 27 passes per interval, cursor 0, buffer at 0x4b5200000000
- per repetition: home 0 link read bytes and 1294 SMMU translation requests; level 0 link read bytes and 2766 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 268 passes per interval, cursor 0, buffer at 0x5f99c0000000; level: placement hbm, 253 passes per interval, cursor 0, buffer at 0x5f9a40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x46f180000000; level: placement cpu, 9 passes per interval, cursor 0, buffer at 0x46f240000000
- no hardware counters in this cell

### route/at=plain,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x55c640000000; level: placement hbm, 8 passes per interval, cursor 0, buffer at 0x55c700000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x5ca4c0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5ca540000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x529400000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5294c0000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4d4d40000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4d4e40000000
- per repetition: home 0 link read bytes and 4238 SMMU translation requests; level 1.074e+09 link read bytes and 4510 SMMU translation requests; multiplexed rows voided: 0

### route/at=returned,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 25 passes per interval, cursor 0, buffer at 0x55a9c0000000; level: placement hbm, 23 passes per interval, cursor 0, buffer at 0x55aa80000000
- per repetition: home 0 link read bytes and 1285 SMMU translation requests; level 0 link read bytes and 2998 SMMU translation requests; multiplexed rows voided: 0

### route/at=returned,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 270 passes per interval, cursor 0, buffer at 0x5daa00000000; level: placement hbm, 147 passes per interval, cursor 0, buffer at 0x5daac0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=returned,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x404680000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x404740000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x534b00000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x534b80000000
- no hardware counters in this cell

### route/at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=generator

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4b93c0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4b9480000000
- per repetition: home 3.199e+09 link read bytes and 0 SMMU translation requests; level 2.853e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=generator

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 16 passes per interval, cursor 0, buffer at 0x58ba00000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x58bb00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=rmat,footprint-mib=8192,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=generator

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x46a580000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x46a880000000
- per repetition: home 2.553e+10 link read bytes and 1.367e+05 SMMU translation requests; level 2.415e+10 link read bytes and 1.638e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=rmat,footprint-mib=8192,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=generator

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x4aef40000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x4af200000000
- per repetition: home 0 link read bytes and 1.429e+05 SMMU translation requests; level 0 link read bytes and 1.631e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5e0e80000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5e0f00000000
- per repetition: home 5.243e+05 link read bytes and 28.86 SMMU translation requests; level 5.243e+05 link read bytes and 28.08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x49bfc0000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x49c040000000
- per repetition: home 5.243e+05 link read bytes and 0.78 SMMU translation requests; level 5.243e+05 link read bytes and 0.78 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x410ac0000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x410b80000000
- per repetition: home 5.243e+05 link read bytes and 24.18 SMMU translation requests; level 5.243e+05 link read bytes and 27.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x587ac0000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x587b80000000
- per repetition: home 5.243e+05 link read bytes and 1.56 SMMU translation requests; level 5.243e+05 link read bytes and 0.78 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5639c0000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x563a80000000
- per repetition: home 5.243e+05 link read bytes and 0.78 SMMU translation requests; level 5.243e+05 link read bytes and 0.78 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x500000000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5000c0000000
- per repetition: home 5.243e+05 link read bytes and 0.78 SMMU translation requests; level 5.243e+05 link read bytes and 0.78 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x4452c0000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x445380000000
- per repetition: home 6.711e+07 link read bytes and 2111 SMMU translation requests; level 6.711e+07 link read bytes and 1741 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x448800000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x448880000000
- per repetition: home 6.711e+07 link read bytes and 2057 SMMU translation requests; level 6.711e+07 link read bytes and 1678 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5a7700000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5a7780000000
- per repetition: home 6.711e+07 link read bytes and 1974 SMMU translation requests; level 6.711e+07 link read bytes and 2008 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x521dc0000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x521ec0000000
- per repetition: home 0 link read bytes and 2911 SMMU translation requests; level 0 link read bytes and 2085 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x55a140000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x55a200000000
- per repetition: home 0 link read bytes and 2917 SMMU translation requests; level 0 link read bytes and 2086 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x42cf00000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x42cf80000000
- per repetition: home 0 link read bytes and 2885 SMMU translation requests; level 0 link read bytes and 2833 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x4e2300000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x4e2380000000
- per repetition: home 6.711e+07 link read bytes and 2142 SMMU translation requests; level 6.711e+07 link read bytes and 1954 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x4608c0000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x460980000000
- per repetition: home 6.711e+07 link read bytes and 2155 SMMU translation requests; level 6.711e+07 link read bytes and 1782 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x540a40000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x540b00000000
- per repetition: home 6.711e+07 link read bytes and 2016 SMMU translation requests; level 6.711e+07 link read bytes and 2090 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x447d80000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x447e40000000
- per repetition: home 0 link read bytes and 2867 SMMU translation requests; level 0 link read bytes and 2026 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x572cc0000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x572d80000000
- per repetition: home 0 link read bytes and 2941 SMMU translation requests; level 0 link read bytes and 2102 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x42dd00000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x42ddc0000000
- per repetition: home 0 link read bytes and 2926 SMMU translation requests; level 0 link read bytes and 2846 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x40fdc0000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x40fe80000000
- per repetition: home 0 link read bytes and 396.9 SMMU translation requests; level 0 link read bytes and 300.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x46ebc0000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x46ec80000000
- per repetition: home 0 link read bytes and 373 SMMU translation requests; level 0 link read bytes and 312.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5316c0000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x531780000000
- per repetition: home 0 link read bytes and 382.4 SMMU translation requests; level 0 link read bytes and 330 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5e1500000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5e1580000000
- per repetition: home 0 link read bytes and 398.1 SMMU translation requests; level 0 link read bytes and 302.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4e3980000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4e3a00000000
- per repetition: home 0 link read bytes and 399.5 SMMU translation requests; level 0 link read bytes and 308.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x49cf00000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x49cfc0000000
- per repetition: home 0 link read bytes and 398.8 SMMU translation requests; level 0 link read bytes and 357.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x418f80000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x419040000000
- per repetition: home 0 link read bytes and 4562 SMMU translation requests; level 0 link read bytes and 2789 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5d6c00000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5d6cc0000000
- per repetition: home 0 link read bytes and 4398 SMMU translation requests; level 0 link read bytes and 2746 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4c8040000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4c8100000000
- per repetition: home 0 link read bytes and 4501 SMMU translation requests; level 0 link read bytes and 4229 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5eea00000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5eea80000000
- per repetition: home 0 link read bytes and 4571 SMMU translation requests; level 0 link read bytes and 2593 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x553900000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x553980000000
- per repetition: home 0 link read bytes and 4376 SMMU translation requests; level 0 link read bytes and 2709 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x56a040000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x56a100000000
- per repetition: home 0 link read bytes and 4599 SMMU translation requests; level 0 link read bytes and 4251 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=factor,vary=sharing

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x48b680000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x48b7c0000000
- per repetition: home 3.201e+09 link read bytes and 0 SMMU translation requests; level 3.198e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=factor,vary=sharing

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 16 passes per interval, cursor 0, buffer at 0x4d4c80000000; level: placement hbm, 16 passes per interval, cursor 0, buffer at 0x4d4d80000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x59cb00000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x59cc00000000
- per repetition: home 8.429e+06 link read bytes and 335.2 SMMU translation requests; level 8.428e+06 link read bytes and 315.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5b78c0000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5b79c0000000
- per repetition: home 8.429e+06 link read bytes and 330.9 SMMU translation requests; level 8.431e+06 link read bytes and 319.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5aaa80000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5aab80000000
- per repetition: home 8.43e+06 link read bytes and 334.1 SMMU translation requests; level 8.428e+06 link read bytes and 334.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x4821c0000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x482280000000
- per repetition: home 8.43e+06 link read bytes and 331.6 SMMU translation requests; level 8.429e+06 link read bytes and 315.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x4ae000000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x4ae100000000
- per repetition: home 8.432e+06 link read bytes and 314.6 SMMU translation requests; level 8.429e+06 link read bytes and 299.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5adc00000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5adcc0000000
- per repetition: home 8.429e+06 link read bytes and 327.6 SMMU translation requests; level 8.429e+06 link read bytes and 327.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5a1cc0000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5a1d80000000
- per repetition: home 5.366e+08 link read bytes and 733.5 SMMU translation requests; level 5.366e+08 link read bytes and 795.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x482280000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x482340000000
- per repetition: home 8.43e+06 link read bytes and 334 SMMU translation requests; level 8.429e+06 link read bytes and 333.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x45eac0000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x45ebc0000000
- per repetition: home 5.366e+08 link read bytes and 774.8 SMMU translation requests; level 5.366e+08 link read bytes and 768.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x40c240000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x40c380000000
- per repetition: home 8.429e+06 link read bytes and 329.6 SMMU translation requests; level 8.43e+06 link read bytes and 328.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x4c0c00000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x4c0cc0000000
- per repetition: home 5.366e+08 link read bytes and 260.1 SMMU translation requests; level 5.366e+08 link read bytes and 198.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x438e00000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x438ec0000000
- per repetition: home 8.428e+06 link read bytes and 319.9 SMMU translation requests; level 8.43e+06 link read bytes and 318.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x56af80000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x56b0c0000000
- per repetition: home 0 link read bytes and 951.8 SMMU translation requests; level 0 link read bytes and 948.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x4bb8c0000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x4bb980000000
- per repetition: home 0 link read bytes and 940.6 SMMU translation requests; level 0 link read bytes and 946.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x56d500000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x56d600000000
- per repetition: home 0 link read bytes and 952.1 SMMU translation requests; level 0 link read bytes and 960.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5b8040000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5b8140000000
- per repetition: home 5.366e+08 link read bytes and 325.7 SMMU translation requests; level 5.366e+08 link read bytes and 699.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x57f680000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x57f780000000
- per repetition: home 8.428e+06 link read bytes and 331.5 SMMU translation requests; level 8.43e+06 link read bytes and 331.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5e9900000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5e9a00000000
- per repetition: home 5.366e+08 link read bytes and 804 SMMU translation requests; level 5.366e+08 link read bytes and 803.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x50aa80000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x50ab80000000
- per repetition: home 8.429e+06 link read bytes and 330.7 SMMU translation requests; level 8.428e+06 link read bytes and 332.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5ed440000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5ed500000000
- per repetition: home 5.366e+08 link read bytes and 530.8 SMMU translation requests; level 5.366e+08 link read bytes and 441.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x453e40000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x453f40000000
- per repetition: home 8.429e+06 link read bytes and 324.3 SMMU translation requests; level 8.428e+06 link read bytes and 323.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x487180000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x487240000000
- per repetition: home 0 link read bytes and 951.5 SMMU translation requests; level 0 link read bytes and 946.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x49fc00000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x49fd00000000
- per repetition: home 0 link read bytes and 948.1 SMMU translation requests; level 0 link read bytes and 949 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x54a6c0000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x54a7c0000000
- per repetition: home 0 link read bytes and 954.7 SMMU translation requests; level 0 link read bytes and 955.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5a7a00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5a7b00000000
- per repetition: home 5.369e+08 link read bytes and 1.737e+04 SMMU translation requests; level 5.369e+08 link read bytes and 1.739e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4c7d40000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4c7e40000000
- per repetition: home 5.369e+08 link read bytes and 1.31e+04 SMMU translation requests; level 5.369e+08 link read bytes and 1.308e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x470c80000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x470d80000000
- per repetition: home 5.369e+08 link read bytes and 4365 SMMU translation requests; level 5.369e+08 link read bytes and 4347 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x459f40000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x45a000000000
- per repetition: home 5.369e+08 link read bytes and 1.737e+04 SMMU translation requests; level 5.369e+08 link read bytes and 1.739e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x42ca80000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x42cb80000000
- per repetition: home 5.369e+08 link read bytes and 1.732e+04 SMMU translation requests; level 5.369e+08 link read bytes and 1.524e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x55d440000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x55d500000000
- per repetition: home 5.369e+08 link read bytes and 8785 SMMU translation requests; level 5.369e+08 link read bytes and 1.3e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x45f380000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x45f800000000
- per repetition: home 3.355e+07 link read bytes and 2.025e+06 SMMU translation requests; level 3.355e+07 link read bytes and 2.015e+06 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x46f580000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x46fa40000000
- per repetition: home 3.355e+07 link read bytes and 2.026e+06 SMMU translation requests; level 3.355e+07 link read bytes and 2.017e+06 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x410f00000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x411380000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x588a00000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x588ec0000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5e38c0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5e3d80000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5f0880000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5f0d40000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4e1d80000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4e2200000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4ef280000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4ef700000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x58e540000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x58e640000000
- per repetition: home 6.422e+09 link read bytes and 3.616e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.607e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 7 passes per interval, cursor 0, buffer at 0x5c7380000000; level: placement hbm, 7 passes per interval, cursor 0, buffer at 0x5c7480000000
- per repetition: home 0 link read bytes and 5982 SMMU translation requests; level 0 link read bytes and 5965 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x557f00000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x558000000000
- per repetition: home 6.422e+09 link read bytes and 3.604e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.598e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x586400000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x586500000000
- per repetition: home 6.422e+09 link read bytes and 3.595e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.595e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4b76c0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4b77c0000000
- per repetition: home 6.423e+09 link read bytes and 3.617e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.59e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x4d2440000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x4d2580000000
- per repetition: home 0 link read bytes and 4.298e+04 SMMU translation requests; level 0 link read bytes and 4.175e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x535a80000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x535b80000000
- per repetition: home 0 link read bytes and 4.266e+04 SMMU translation requests; level 0 link read bytes and 4.179e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x445880000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x445980000000
- per repetition: home 0 link read bytes and 4.286e+04 SMMU translation requests; level 0 link read bytes and 4.127e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5771c0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5772c0000000
- per repetition: home 6.423e+09 link read bytes and 3.609e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.623e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x41eb80000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x41ec80000000
- per repetition: home 6.423e+09 link read bytes and 3.613e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.603e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x592880000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5929c0000000
- per repetition: home 6.422e+09 link read bytes and 3.596e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.589e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x5a7e80000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x5a7f80000000
- per repetition: home 0 link read bytes and 4.281e+04 SMMU translation requests; level 0 link read bytes and 4.157e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x4a4ac0000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x4a4c00000000
- per repetition: home 0 link read bytes and 4.267e+04 SMMU translation requests; level 0 link read bytes and 4.145e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x533c00000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x533d40000000
- per repetition: home 0 link read bytes and 4.289e+04 SMMU translation requests; level 0 link read bytes and 4.466e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x501780000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x501a40000000
- per repetition: home 0 link read bytes and 1.328e+05 SMMU translation requests; level 0 link read bytes and 1.328e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x5818c0000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x581b80000000
- per repetition: home 0 link read bytes and 1.329e+05 SMMU translation requests; level 0 link read bytes and 1.336e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=1

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x58c8c0000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x58cb40000000
- per repetition: home 0 link read bytes and 1.327e+05 SMMU translation requests; level 0 link read bytes and 1.339e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x4be300000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x4be580000000
- per repetition: home 0 link read bytes and 1.327e+05 SMMU translation requests; level 0 link read bytes and 1.328e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x5db4c0000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x5db780000000
- per repetition: home 0 link read bytes and 1.327e+05 SMMU translation requests; level 0 link read bytes and 1.328e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=1

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x57f040000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x57f300000000
- per repetition: home 0 link read bytes and 1.327e+05 SMMU translation requests; level 0 link read bytes and 1.329e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=stadd,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x40e4c0000000; level: placement cpu, 3 passes per interval, cursor 0, buffer at 0x40e540000000
- no hardware counters in this cell

### route/at=stadd,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x53b300000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x53b3c0000000
- no hardware counters in this cell

### route/at=stadd,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x45d080000000; level: placement cpu, 3 passes per interval, cursor 0, buffer at 0x45d180000000
- no hardware counters in this cell

### route/at=stadd,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x4ae5c0000000; level: placement hbm, 2 passes per interval, cursor 0, buffer at 0x4ae6c0000000
- no hardware counters in this cell

### route/at=tiles,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=tiling,working-set-mib=8

- first variant A, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 510 passes per interval, cursor 1, buffer at 0x510600000000; level: placement cpu, 545 passes per interval, cursor 1, buffer at 0x5106c0000000
- per repetition: home 8.429e+06 link read bytes and 0 SMMU translation requests; level 8.38e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=tiles,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=tiling,working-set-mib=8

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 1236 passes per interval, cursor 1, buffer at 0x46f900000000; level: placement hbm, 1294 passes per interval, cursor 1, buffer at 0x46f9c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,type=factor,vary=strategy

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x43d8c0000000; level: placement cpu, 3 passes per interval, cursor 0, buffer at 0x43d980000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp,footprint-mib=8,kernel=k6,keys=1048576,placement=hbm,type=factor,vary=strategy

- first variant B, seed 67; repeats alternated as drawn: yes
- home: placement hbm, 112 passes per interval, cursor 0, buffer at 0x484740000000; level: placement hbm, 70 passes per interval, cursor 0, buffer at 0x484800000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

