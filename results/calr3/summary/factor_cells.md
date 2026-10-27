# Factor cells: the direct route at a level of one factor against its home level, recomputed from raw rows

Times are per pass in ms. The factor effect on direct access is level minus home within a repeat, as median with its 95 % rank interval; a positive value means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | level | home ms | level ms | effect ms [interval] | relative to home | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0393 | 0.3748 | 0.3354 [0.3352, 0.3357] | +852.6 % | 10 | yes | pass |
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0162 | 0.0302 | 0.0141 [0.0140, 0.0141] | +86.8 % | 10 | yes | pass |
| at=1024,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=working-set,working-set-mib=32 | working-set | 1024 | 1.5040 | 47.1624 | 45.6584 [45.6483, 45.6740] | +3035.8 % | 10 | yes | pass |
| at=1024,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=working-set,working-set-mib=32 | working-set | 1024 | 0.0977 | 5.1554 | 5.0577 [5.0556, 5.0649] | +5179.3 % | 10 | yes | pass |
| at=1024,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint | footprint | 1024 | 0.0757 | 0.8150 | 0.7393 [0.7387, 0.7397] | +976.9 % | 10 | yes | pass |
| at=1024,footprint-mib=256,kernel=k6,placement=cpu,type=factor,update=atomic,vary=footprint | footprint | 1024 | 1.5073 | 6.0366 | 4.5293 [4.5237, 4.5345] | +300.5 % | 10 | yes | pass |
| at=1024,footprint-mib=256,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint | footprint | 1024 | 0.2044 | 0.8164 | 0.6120 [0.6111, 0.6126] | +299.4 % | 10 | yes | pass |
| at=1024,footprint-mib=4096,kernel=k6,placement=cpu,type=factor,update=atomic,vary=footprint | footprint | 1024 | 24.1600 | 5.8297 | -18.3270 [-18.3418, -18.3126] | -75.9 % | 10 | yes | pass |
| at=1024,footprint-mib=4096,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint | footprint | 1024 | 3.2754 | 0.8178 | -2.4575 [-2.4600, -2.4562] | -75.0 % | 10 | yes | pass |
| at=1024,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=factor,vary=keys | keys | 1024 | 191.3073 | 12.4924 | -178.8172 [-178.8267, -178.8059] | -93.5 % | 10 | yes | pass |
| at=1024,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=factor,vary=keys | keys | 1024 | 12.3095 | 0.7670 | -11.5424 [-11.5444, -11.5422] | -93.8 % | 10 | yes | pass |
| at=1024,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,type=factor,vary=keys | keys | 1024 | 7.7492 | 12.5027 | 4.7539 [4.7449, 4.7568] | +61.3 % | 10 | yes | pass |
| at=1024,footprint-mib=8,kernel=k6,keys=1048576,placement=hbm,type=factor,vary=keys | keys | 1024 | 0.1883 | 0.7668 | 0.5785 [0.5783, 0.5786] | +307.1 % | 10 | yes | pass |
| at=4,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=repeat | repeat | 4 | 6.0576 | 18.0753 | 12.0187 [12.0024, 12.0263] | +198.4 % | 10 | yes | pass |
| at=4,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=repeat | repeat | 4 | 0.8185 | 1.6423 | 0.8237 [0.8226, 0.8262] | +100.6 % | 10 | yes | pass |
| at=8,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=working-set,working-set-mib=32 | working-set | 8 | 1.4851 | 0.0394 | -1.4457 [-1.4463, -1.4455] | -97.3 % | 10 | yes | pass |
| at=8,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=working-set,working-set-mib=32 | working-set | 8 | 0.0962 | 0.0161 | -0.0801 [-0.0801, -0.0800] | -83.3 % | 10 | yes | pass |
| at=hbm,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=placement | placement | hbm | 10.0619 | 10.0610 | -0.0011 [-0.0044, 0.0026] | -0.0 % | 100 | no | pass |
| at=hbm,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=plain,vary=placement | placement | hbm | 2.2773 | 2.2629 | -0.0002 [-0.0018, 0.0015] | -0.0 % | 100 | no | pass |
| at=hbm,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=placement | placement | hbm | 13.0661 | 18.3959 | 5.3007 [5.1225, 5.4546] | +40.6 % | 100 | yes | pass |
| at=hbm,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=plain,vary=placement | placement | hbm | 2.3922 | 2.7348 | 0.3465 [0.3200, 0.3568] | +14.5 % | 10 | yes | pass |
| at=line,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=layout | layout | line | 6.0576 | 3.5342 | -2.5218 [-2.5318, -2.5177] | -41.6 % | 10 | yes | pass |
| at=line,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=layout | layout | line | 0.8171 | 0.3398 | -0.4773 [-0.4777, -0.4765] | -58.4 % | 10 | yes | pass |
| at=none,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=tiling | tiling | none | 26.5637 | 37.8297 | 11.2740 [11.1596, 11.3532] | +42.4 % | 10 | yes | pass |
| at=none,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=tiling | tiling | none | 3.2884 | 2.7545 | -0.5361 [-0.5639, -0.5285] | -16.3 % | 10 | yes | pass |
| at=plain,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | plain | 10.0677 | 2.3520 | -7.7189 [-7.7319, -7.7033] | -76.7 % | 10 | yes | pass |
| at=plain,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | plain | 10.0692 | 2.3333 | -7.7420 [-7.7531, -7.7206] | -76.9 % | 10 | yes | pass |
| at=plain,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | plain | 6.0632 | 6.0107 | -0.0517 [-0.0559, -0.0484] | -0.9 % | 20 | yes | pass |
| at=plain,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | plain | 0.8161 | 0.7678 | -0.0480 [-0.0487, -0.0473] | -5.9 % | 10 | yes | pass |
| at=plain,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | plain | 0.0737 | 0.0786 | 0.0050 [0.0049, 0.0050] | +6.8 % | 10 | yes | pass |
| at=plain,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | plain | 12.9899 | 2.3911 | -10.5956 [-10.6928, -10.4426] | -81.6 % | 30 | yes | pass |
| at=plain,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | plain | 17.7915 | 2.7305 | -15.0581 [-15.1792, -15.0354] | -84.6 % | 10 | yes | pass |
| at=returned,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | returned | 10.0544 | 40.5828 | 30.5249 [30.3435, 31.2096] | +303.6 % | 100 | yes | pass |
| at=returned,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | returned | 10.0611 | 41.4531 | 31.3915 [30.9007, 31.6046] | +312.0 % | 10 | yes | pass |
| at=returned,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | returned | 6.0513 | 6.0828 | 0.0308 [0.0272, 0.0324] | +0.5 % | 30 | yes | pass |
| at=returned,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | returned | 0.8144 | 0.8974 | 0.0829 [0.0823, 0.0834] | +10.2 % | 10 | yes | pass |
| at=returned,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | returned | 0.0760 | 0.1365 | 0.0605 [0.0605, 0.0606] | +79.6 % | 10 | yes | pass |
| at=returned,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | returned | 12.9230 | 47.8773 | 35.0935 [34.3649, 35.3553] | +271.6 % | 20 | yes | pass |
| at=returned,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | returned | 17.7601 | 48.0905 | 30.1958 [29.6604, 30.5782] | +170.0 % | 20 | yes | pass |
| at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=generator | generator | rmat | 30.7879 | 190.1682 | 159.3829 [159.3489, 159.4245] | +517.7 % | 10 | yes | pass |
| at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=generator | generator | rmat | 1.2711 | 65.4664 | 64.1954 [63.7057, 64.6945] | +5050.5 % | 10 | yes | pass |
| at=rmat,footprint-mib=8192,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=generator | generator | rmat | 247.8517 | 991.6169 | 743.7649 [743.6042, 743.8686] | +300.1 % | 10 | yes | pass |
| at=rmat,footprint-mib=8192,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=generator | generator | rmat | 15.1278 | 395.8022 | 380.6765 [378.1159, 383.1449] | +2516.4 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing | sharing | shared | 0.0203 | 0.0211 | 0.0009 [0.0008, 0.0009] | +4.2 % | 40 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0202 | 0.0210 | 0.0008 [0.0008, 0.0009] | +4.0 % | 40 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0205 | 0.0208 | 0.0004 [0.0003, 0.0004] | +1.8 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing | sharing | shared | 0.0202 | 0.0210 | 0.0009 [0.0008, 0.0009] | +4.3 % | 40 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0203 | 0.0209 | 0.0007 [0.0006, 0.0007] | +3.2 % | 40 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0203 | 0.0202 | -0.0001 [-0.0001, -0.0000] | -0.4 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing | sharing | shared | 0.1942 | 0.1933 | -0.0008 [-0.0010, -0.0007] | -0.4 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 0.1930 | 0.3782 | 0.1853 [0.1846, 0.1856] | +96.0 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing | sharing | shared | 0.1931 | 0.1925 | -0.0007 [-0.0008, -0.0006] | -0.3 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0383 | 0.1584 | 0.1201 [0.1182, 0.1212] | +313.3 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0357 | 0.1815 | 0.1459 [0.1455, 0.1461] | +409.3 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0382 | 0.0368 | -0.0015 [-0.0016, -0.0014] | -3.9 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing | sharing | shared | 0.1934 | 0.1931 | -0.0004 [-0.0005, -0.0002] | -0.2 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 0.1929 | 0.3805 | 0.1875 [0.1871, 0.1879] | +97.2 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing | sharing | shared | 0.1925 | 0.1919 | -0.0006 [-0.0006, -0.0005] | -0.3 % | 90 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0374 | 0.1667 | 0.1292 [0.1285, 0.1302] | +345.2 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0360 | 0.1796 | 0.1434 [0.1431, 0.1443] | +398.4 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0380 | 0.0370 | -0.0009 [-0.0011, -0.0009] | -2.4 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0150 | 0.0593 | 0.0444 [0.0443, 0.0446] | +294.9 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0153 | 0.0501 | 0.0347 [0.0344, 0.0351] | +226.4 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0155 | 0.0159 | 0.0004 [0.0003, 0.0004] | +2.4 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0151 | 0.0605 | 0.0454 [0.0452, 0.0457] | +300.4 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0156 | 0.0425 | 0.0269 [0.0266, 0.0275] | +172.6 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0151 | 0.0157 | 0.0005 [0.0005, 0.0006] | +3.4 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0562 | 0.2219 | 0.1654 [0.1647, 0.1666] | +294.5 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0507 | 0.2625 | 0.2118 [0.2113, 0.2122] | +417.4 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0505 | 0.0501 | -0.0005 [-0.0007, -0.0004] | -1.1 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0556 | 0.2360 | 0.1804 [0.1797, 0.1811] | +324.4 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0507 | 0.2636 | 0.2129 [0.2124, 0.2131] | +420.1 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0496 | 0.0492 | -0.0005 [-0.0005, -0.0004] | -0.9 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=factor,vary=sharing | sharing | shared | 30.8307 | 30.4717 | -0.3620 [-0.3972, -0.3406] | -1.2 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=factor,vary=sharing | sharing | shared | 1.2770 | 1.2769 | -0.0004 [-0.0016, 0.0013] | -0.0 % | 100 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0472 | 0.0643 | 0.0172 [0.0165, 0.0177] | +36.4 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0467 | 0.0674 | 0.0206 [0.0204, 0.0209] | +44.1 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0459 | 0.0458 | -0.0001 [-0.0001, -0.0000] | -0.2 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0461 | 0.0650 | 0.0188 [0.0185, 0.0195] | +40.9 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0468 | 0.0681 | 0.0213 [0.0209, 0.0215] | +45.4 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0456 | 0.0456 | 0.0000 [-0.0000, 0.0001] | +0.1 % | 100 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32 | sharing | shared | 1.5105 | 1.5003 | -0.0104 [-0.0112, -0.0100] | -0.7 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8 | sharing | shared | 0.0456 | 0.0456 | -0.0000 [-0.0000, 0.0001] | -0.0 % | 100 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 1.5121 | 1.5201 | 0.0082 [0.0075, 0.0089] | +0.5 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0523 | 0.0534 | 0.0011 [0.0010, 0.0012] | +2.1 % | 20 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 1.5068 | 1.4996 | -0.0071 [-0.0080, -0.0068] | -0.5 % | 30 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8 | sharing | shared | 0.0550 | 0.0560 | 0.0009 [0.0007, 0.0012] | +1.7 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32 | sharing | shared | 0.1052 | 0.1069 | 0.0017 [0.0016, 0.0019] | +1.6 % | 70 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.1149 | 0.1154 | 0.0005 [0.0003, 0.0007] | +0.4 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.1307 | 0.1312 | 0.0005 [0.0001, 0.0010] | +0.4 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32 | sharing | shared | 1.5062 | 1.5050 | -0.0013 [-0.0014, -0.0012] | -0.1 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8 | sharing | shared | 0.0455 | 0.0454 | -0.0001 [-0.0001, -0.0000] | -0.2 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 1.5024 | 1.5227 | 0.0199 [0.0194, 0.0208] | +1.3 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0522 | 0.0537 | 0.0015 [0.0014, 0.0015] | +2.8 % | 30 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 1.5070 | 1.5061 | -0.0010 [-0.0014, -0.0005] | -0.1 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8 | sharing | shared | 0.0527 | 0.0534 | 0.0008 [0.0005, 0.0011] | +1.4 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32 | sharing | shared | 0.1067 | 0.1067 | 0.0002 [-0.0000, 0.0002] | +0.2 % | 100 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.1141 | 0.1146 | 0.0006 [0.0003, 0.0010] | +0.6 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.1288 | 0.1309 | 0.0020 [0.0016, 0.0024] | +1.6 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01 | sharing | shared | 5.4351 | 5.4343 | -0.0009 [-0.0010, -0.0004] | -0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1 | sharing | shared | 5.4231 | 5.4200 | -0.0033 [-0.0158, -0.0024] | -0.1 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1 | sharing | shared | 5.3955 | 5.3949 | -0.0005 [-0.0011, -0.0000] | -0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01 | sharing | shared | 5.4352 | 5.4334 | -0.0017 [-0.0021, -0.0015] | -0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1 | sharing | shared | 5.4363 | 5.4340 | -0.0025 [-0.0032, -0.0018] | -0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1 | sharing | shared | 5.4262 | 5.4083 | -0.0057 [-0.0190, -0.0043] | -0.1 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 7.2601 | 7.2227 | -0.0359 [-0.0393, -0.0322] | -0.5 % | 70 | yes | pass |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 7.2613 | 7.2256 | -0.0350 [-0.0396, -0.0302] | -0.5 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01 | sharing | shared | 433.5770 | 433.6147 | 0.0722 [0.0105, 0.1024] | +0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1 | sharing | shared | 433.5967 | 433.6034 | 0.0150 [-0.0190, 0.0550] | +0.0 % | 100 | no | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1 | sharing | shared | 433.6085 | 433.5884 | -0.0029 [-0.0520, 0.0412] | -0.0 % | 100 | no | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01 | sharing | shared | 433.5892 | 433.6264 | 0.0463 [0.0111, 0.0913] | +0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1 | sharing | shared | 433.5717 | 433.6039 | 0.0035 [-0.0241, 0.0467] | +0.0 % | 100 | no | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1 | sharing | shared | 433.5535 | 433.5377 | -0.0204 [-0.0714, 0.0186] | -0.0 % | 100 | no | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing | sharing | shared | 26.3965 | 23.5109 | -2.8877 [-2.9119, -2.8732] | -10.9 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing | sharing | shared | 3.2721 | 3.2833 | 0.0116 [0.0107, 0.0129] | +0.4 % | 100 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | sharing | shared | 26.7847 | 23.5206 | -3.2631 [-3.2956, -3.2197] | -12.2 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | sharing | shared | 26.5886 | 23.5292 | -3.0689 [-3.1119, -3.0363] | -11.5 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | sharing | shared | 26.7283 | 23.6020 | -3.1242 [-3.1595, -3.0844] | -11.7 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | sharing | shared | 3.5782 | 3.5015 | -0.0736 [-0.0820, -0.0724] | -2.1 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | sharing | shared | 3.5401 | 3.5892 | 0.0486 [0.0459, 0.0514] | +1.4 % | 30 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | sharing | shared | 3.4843 | 3.5910 | 0.1065 [0.0987, 0.1123] | +3.1 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | sharing | shared | 26.5076 | 23.4204 | -3.0860 [-3.1247, -3.0577] | -11.6 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | sharing | shared | 26.2211 | 23.4325 | -2.7872 [-2.8187, -2.7706] | -10.6 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | sharing | shared | 26.7875 | 23.6565 | -3.1393 [-3.1462, -3.1051] | -11.7 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | sharing | shared | 3.4572 | 3.6050 | 0.1451 [0.1383, 0.1566] | +4.2 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | sharing | shared | 3.4655 | 3.5978 | 0.1333 [0.1236, 0.1380] | +3.8 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | sharing | shared | 3.5688 | 3.5105 | -0.0592 [-0.0634, -0.0545] | -1.7 % | 10 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01 | sharing | shared | 8.0805 | 8.0998 | 0.0199 [0.0179, 0.0218] | +0.2 % | 70 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1 | sharing | shared | 8.0884 | 8.0946 | 0.0063 [0.0043, 0.0085] | +0.1 % | 100 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=1 | sharing | shared | 8.1009 | 8.1267 | 0.0257 [0.0231, 0.0279] | +0.3 % | 60 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01 | sharing | shared | 8.0732 | 8.0991 | 0.0251 [0.0228, 0.0272] | +0.3 % | 70 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1 | sharing | shared | 8.0780 | 8.0955 | 0.0162 [0.0147, 0.0175] | +0.2 % | 90 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=1 | sharing | shared | 8.0851 | 8.1052 | 0.0211 [0.0184, 0.0232] | +0.3 % | 100 | yes | pass |
| at=stadd,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | stadd | 10.0566 | 7.9529 | -2.1028 [-2.1101, -2.0898] | -20.9 % | 10 | yes | pass |
| at=stadd,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | stadd | 10.0553 | 7.9691 | -2.0878 [-2.1227, -2.0775] | -20.8 % | 10 | yes | pass |
| at=stadd,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | stadd | 13.0097 | 9.1555 | -3.8580 [-3.9878, -3.7423] | -29.7 % | 20 | yes | pass |
| at=stadd,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | stadd | 17.3333 | 11.4074 | -5.9142 [-5.9554, -5.8744] | -34.1 % | 20 | yes | pass |
| at=tiles,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=tiling,working-set-mib=8 | tiling | tiles | 0.0395 | 0.0368 | -0.0026 [-0.0026, -0.0026] | -6.7 % | 10 | yes | pass |
| at=tiles,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=tiling,working-set-mib=8 | tiling | tiles | 0.0162 | 0.0155 | -0.0008 [-0.0008, -0.0007] | -4.7 % | 10 | yes | pass |
| at=warp,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,type=factor,vary=strategy | strategy | warp | 8.1687 | 8.1206 | -0.0478 [-0.0505, -0.0461] | -0.6 % | 20 | yes | pass |
| at=warp,footprint-mib=8,kernel=k6,keys=1048576,placement=hbm,type=factor,vary=strategy | strategy | warp | 0.1790 | 0.2862 | 0.1072 [0.1070, 0.1073] | +59.9 % | 10 | yes | pass |

## Host phases

The CPU phase before every pass, timed on the CPU clock (ms per pass), and the state check's median load latency on the preparing core after the phase (ns per sampled load), per variant.

| cell | home CPU ms | home state ns | level CPU ms | level state ns |
|---|---|---|---|---|
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing | 0.2838 | 63.2 | 0.2791 | 62.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | 0.2447 | 62.0 | 0.2472 | 61.6 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing | 0.2703 | 179.6 | 0.2638 | 74.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing | 0.2814 | 63.1 | 0.2684 | 65.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | 0.2419 | 63.2 | 0.2425 | 62.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing | 0.2482 | 189.8 | 0.2452 | 69.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing | 5.2813 | 60.8 | 5.9151 | 94.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | 2.7727 | 58.6 | 3.3440 | 79.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing | 3.9865 | 214.2 | 3.9564 | 198.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | 5.0290 | 118.9 | 5.9410 | 202.6 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | 2.8688 | 56.9 | 3.6001 | 91.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | 3.9702 | 466.2 | 3.9029 | 422.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing | 5.2514 | 80.1 | 5.4115 | 186.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | 2.7437 | 67.1 | 2.6684 | 70.8 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing | 3.4452 | 197.6 | 3.4409 | 217.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | 5.0088 | 128.1 | 5.1073 | 205.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | 2.8798 | 90.0 | 3.0224 | 124.8 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | 3.2242 | 465.5 | 3.2364 | 421.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | 1.1822 | 69.2 | 1.2614 | 78.8 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | 0.9439 | 71.4 | 1.0352 | 72.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | 1.0457 | 370.2 | 1.0433 | 401.9 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | 1.1742 | 71.0 | 1.2033 | 86.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | 0.9025 | 62.4 | 0.9494 | 63.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | 0.9710 | 380.2 | 0.9754 | 381.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | 7.8107 | 239.1 | 8.1288 | 295.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | 4.2155 | 297.0 | 5.1725 | 300.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | 5.6783 | 485.4 | 5.5406 | 458.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | 7.2220 | 90.4 | 7.3495 | 146.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | 3.8970 | 329.6 | 4.0354 | 351.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | 4.5423 | 485.6 | 4.6122 | 459.6 |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=factor,vary=sharing | 1.5571 | - | 1.6515 | - |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=factor,vary=sharing | 2.4736 | - | 3.6947 | - |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8 | 0.9328 | 75.8 | 0.9275 | 77.6 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8 | 0.6554 | 61.2 | 0.6512 | 65.4 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8 | 0.7076 | 196.2 | 0.7074 | 200.1 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8 | 0.8804 | 70.9 | 0.8720 | 75.0 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8 | 0.5272 | 78.8 | 0.5206 | 74.1 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8 | 0.6393 | 207.5 | 0.6369 | 195.2 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32 | 0.5721 | 67.4 | 0.5912 | 102.9 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8 | 0.5841 | 76.4 | 0.5871 | 112.4 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32 | 4.2842 | 94.5 | 4.3124 | 151.4 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8 | 4.2018 | 140.6 | 4.1849 | 179.8 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32 | 29.2959 | 246.9 | 29.3159 | 257.5 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8 | 27.9226 | 288.2 | 27.9121 | 311.0 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32 | 0.9837 | 79.8 | 0.9962 | 112.4 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32 | 5.3785 | 351.5 | 5.3854 | 379.8 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32 | 32.0681 | 538.1 | 32.4612 | 569.4 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32 | 0.5563 | 75.1 | 0.5589 | 116.4 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8 | 0.5520 | 75.2 | 0.5506 | 122.0 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32 | 3.5605 | 97.5 | 3.5806 | 158.2 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8 | 3.5519 | 104.2 | 3.5619 | 148.2 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32 | 22.4307 | 259.0 | 22.4316 | 277.2 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8 | 20.0018 | 277.6 | 20.0011 | 312.8 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32 | 0.9651 | 70.4 | 0.9517 | 121.1 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32 | 4.5804 | 372.2 | 4.5481 | 409.5 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32 | 27.7517 | 526.1 | 27.5267 | 563.4 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01 | 0.6190 | 74.6 | 0.7639 | 103.6 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1 | 4.5873 | 127.8 | 5.1665 | 196.5 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1 | 27.2570 | 281.8 | 26.6196 | 316.2 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01 | 0.5688 | 67.4 | 0.6314 | 94.2 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1 | 3.9483 | 161.1 | 4.2807 | 204.5 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1 | 22.4228 | 256.6 | 22.4315 | 273.4 |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | 1.8783 | 105.2 | 2.7976 | 109.8 |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | 1.8763 | 97.6 | 2.9010 | 109.2 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01 | 8.4214 | 168.4 | 8.5088 | 207.6 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1 | 45.8293 | 316.9 | 45.7673 | 321.0 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1 | 344.5282 | 376.5 | 342.9759 | 363.1 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01 | 6.8438 | 190.9 | 7.6659 | 217.1 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1 | 33.6500 | 282.1 | 33.5864 | 287.2 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1 | 266.0235 | 372.5 | 265.8468 | 354.5 |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing | 27.6288 | - | 28.1334 | - |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing | 62.8796 | - | 62.5119 | - |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | 0.4422 | 55.4 | 0.5047 | 79.5 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | 2.4424 | 65.6 | 2.6568 | 115.1 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | 15.3336 | 238.1 | 14.9412 | 274.6 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | 0.8532 | 66.4 | 0.9029 | 86.8 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | 3.1125 | 257.1 | 3.0981 | 307.6 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | 16.7781 | 473.5 | 17.5544 | 529.5 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | 0.3768 | 55.6 | 0.4029 | 92.5 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | 1.8779 | 79.2 | 1.9555 | 158.4 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | 12.3276 | 253.6 | 13.1462 | 271.5 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | 0.7941 | 64.6 | 0.8071 | 82.5 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | 2.4527 | 216.4 | 2.4072 | 261.4 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | 16.8476 | 491.4 | 16.9101 | 546.9 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01 | 4.7943 | 302.5 | 4.8486 | 311.8 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1 | 25.0229 | 548.2 | 25.1438 | 567.9 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=1 | 193.2843 | 615.9 | 202.6591 | 618.0 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01 | 3.9548 | 344.4 | 3.9719 | 364.5 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1 | 23.6045 | 550.1 | 23.6536 | 570.0 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=1 | 164.8344 | 613.5 | 164.7182 | 608.2 |

## Per cell

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=rotated,working-set-mib=8

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 510 passes per interval, cursor 1, buffer at 0x4c3300000000; level: placement cpu, 54 passes per interval, cursor 1, buffer at 0x4c3400000000
- per repetition: home 8.43e+06 link read bytes and 0 SMMU translation requests; level 1.341e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=rotated,working-set-mib=8

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 1237 passes per interval, cursor 1, buffer at 0x535080000000; level: placement hbm, 662 passes per interval, cursor 1, buffer at 0x535140000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=working-set,working-set-mib=32

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x556300000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5563c0000000
- per repetition: home 5.366e+08 link read bytes and 0 SMMU translation requests; level 1.718e+10 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=working-set,working-set-mib=32

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 205 passes per interval, cursor 1, buffer at 0x5c6980000000; level: placement hbm, 4 passes per interval, cursor 0, buffer at 0x5c6a40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 265 passes per interval, cursor 0, buffer at 0x59dcc0000000; level: placement hbm, 25 passes per interval, cursor 0, buffer at 0x59dd80000000
- per repetition: home 0 link read bytes and 2.549 SMMU translation requests; level 0 link read bytes and 1463 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=256,kernel=k6,placement=cpu,type=factor,update=atomic,vary=footprint

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x545500000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5455c0000000
- per repetition: home 0 link read bytes and 319.3 SMMU translation requests; level 0 link read bytes and 4212 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=256,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 99 passes per interval, cursor 0, buffer at 0x41a840000000; level: placement hbm, 25 passes per interval, cursor 0, buffer at 0x41a940000000
- per repetition: home 0 link read bytes and 100.6 SMMU translation requests; level 0 link read bytes and 1279 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=4096,kernel=k6,placement=cpu,type=factor,update=atomic,vary=footprint

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4ffc40000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4ffe00000000
- per repetition: home 0 link read bytes and 6.62e+04 SMMU translation requests; level 0 link read bytes and 4223 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=4096,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 7 passes per interval, cursor 0, buffer at 0x5e32c0000000; level: placement hbm, 25 passes per interval, cursor 0, buffer at 0x5e3480000000
- per repetition: home 0 link read bytes and 1.76e+04 SMMU translation requests; level 0 link read bytes and 1279 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8,kernel=k6,keys=1,placement=cpu,type=factor,vary=keys

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x44c3c0000000; level: placement cpu, 2 passes per interval, cursor 0, buffer at 0x44c480000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=factor,vary=keys

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x515c80000000; level: placement hbm, 27 passes per interval, cursor 0, buffer at 0x515d00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,type=factor,vary=keys

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x467440000000; level: placement cpu, 2 passes per interval, cursor 0, buffer at 0x4674c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8,kernel=k6,keys=1048576,placement=hbm,type=factor,vary=keys

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 107 passes per interval, cursor 0, buffer at 0x46ef80000000; level: placement hbm, 27 passes per interval, cursor 0, buffer at 0x46f040000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=4,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=repeat

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x539e80000000; level: placement cpu, 2 passes per interval, cursor 0, buffer at 0x539f40000000
- per repetition: home 0 link read bytes and 4205 SMMU translation requests; level 0 link read bytes and 8271 SMMU translation requests; multiplexed rows voided: 0

### route/at=4,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=repeat

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 25 passes per interval, cursor 0, buffer at 0x4b0d80000000; level: placement hbm, 13 passes per interval, cursor 0, buffer at 0x4b0e80000000
- per repetition: home 0 link read bytes and 1236 SMMU translation requests; level 0 link read bytes and 2098 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=working-set,working-set-mib=32

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x419fc0000000; level: placement cpu, 508 passes per interval, cursor 1, buffer at 0x41a0c0000000
- per repetition: home 5.366e+08 link read bytes and 0 SMMU translation requests; level 8.43e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=8,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=working-set,working-set-mib=32

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 209 passes per interval, cursor 1, buffer at 0x47fa00000000; level: placement hbm, 1245 passes per interval, cursor 1, buffer at 0x47fac0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=hbm,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=placement

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x54b0c0000000; level: placement hbm, 2 passes per interval, cursor 0, buffer at 0x54b180000000
- no hardware counters in this cell

### route/at=hbm,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=plain,vary=placement

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 10 passes per interval, cursor 0, buffer at 0x502040000000; level: placement hbm, 9 passes per interval, cursor 0, buffer at 0x5020c0000000
- no hardware counters in this cell

### route/at=hbm,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=placement

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x4eb740000000; level: placement hbm, 2 passes per interval, cursor 0, buffer at 0x4eb800000000
- no hardware counters in this cell

### route/at=hbm,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=plain,vary=placement

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 9 passes per interval, cursor 0, buffer at 0x51a3c0000000; level: placement hbm, 8 passes per interval, cursor 0, buffer at 0x51a4c0000000
- no hardware counters in this cell

### route/at=line,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=layout

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x404ec0000000; level: placement cpu, 6 passes per interval, cursor 0, buffer at 0x404fc0000000
- per repetition: home 0 link read bytes and 4228 SMMU translation requests; level 0 link read bytes and 2881 SMMU translation requests; multiplexed rows voided: 0

### route/at=line,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=layout

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 25 passes per interval, cursor 0, buffer at 0x491180000000; level: placement hbm, 59 passes per interval, cursor 0, buffer at 0x491280000000
- per repetition: home 0 link read bytes and 1299 SMMU translation requests; level 0 link read bytes and 422.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=none,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=tiling

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x550c80000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x550d80000000
- per repetition: home 6.422e+09 link read bytes and 3.606e+04 SMMU translation requests; level 1.311e+10 link read bytes and 3.469e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=none,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=tiling

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 7 passes per interval, cursor 0, buffer at 0x5f3700000000; level: placement hbm, 8 passes per interval, cursor 0, buffer at 0x5f3840000000
- per repetition: home 0 link read bytes and 6014 SMMU translation requests; level 0 link read bytes and 9797 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x4e0080000000; level: placement cpu, 9 passes per interval, cursor 0, buffer at 0x4e0140000000
- no hardware counters in this cell

### route/at=plain,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x5adf00000000; level: placement hbm, 9 passes per interval, cursor 0, buffer at 0x5adfc0000000
- no hardware counters in this cell

### route/at=plain,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x587bc0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x587cc0000000
- per repetition: home 0 link read bytes and 4189 SMMU translation requests; level 1.074e+09 link read bytes and 4552 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 25 passes per interval, cursor 0, buffer at 0x5dc680000000; level: placement hbm, 27 passes per interval, cursor 0, buffer at 0x5dc740000000
- per repetition: home 0 link read bytes and 1241 SMMU translation requests; level 0 link read bytes and 2710 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 272 passes per interval, cursor 0, buffer at 0x51d540000000; level: placement hbm, 255 passes per interval, cursor 0, buffer at 0x51d600000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x4e04c0000000; level: placement cpu, 9 passes per interval, cursor 0, buffer at 0x4e05c0000000
- no hardware counters in this cell

### route/at=plain,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x512580000000; level: placement hbm, 8 passes per interval, cursor 0, buffer at 0x512640000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x5b3a40000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5b3b00000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x5d0740000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5d07c0000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x58a380000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x58a480000000
- per repetition: home 0 link read bytes and 4186 SMMU translation requests; level 1.074e+09 link read bytes and 4500 SMMU translation requests; multiplexed rows voided: 0

### route/at=returned,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 25 passes per interval, cursor 0, buffer at 0x505bc0000000; level: placement hbm, 23 passes per interval, cursor 0, buffer at 0x505cc0000000
- per repetition: home 0 link read bytes and 1278 SMMU translation requests; level 0 link read bytes and 3002 SMMU translation requests; multiplexed rows voided: 0

### route/at=returned,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 264 passes per interval, cursor 0, buffer at 0x557bc0000000; level: placement hbm, 147 passes per interval, cursor 0, buffer at 0x557c80000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=returned,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x513980000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x513a40000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x520280000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x520340000000
- no hardware counters in this cell

### route/at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=generator

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x44ebc0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x44ec80000000
- per repetition: home 3.197e+09 link read bytes and 0 SMMU translation requests; level 2.853e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=generator

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 16 passes per interval, cursor 0, buffer at 0x5be240000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x5be340000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=rmat,footprint-mib=8192,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=generator

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4f6ec0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4f7180000000
- per repetition: home 2.558e+10 link read bytes and 1.367e+05 SMMU translation requests; level 2.415e+10 link read bytes and 1.512e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=rmat,footprint-mib=8192,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=generator

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x48e800000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x48eac0000000
- per repetition: home 0 link read bytes and 1.358e+05 SMMU translation requests; level 0 link read bytes and 1.637e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x452340000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x452400000000
- per repetition: home 5.243e+05 link read bytes and 29.64 SMMU translation requests; level 5.243e+05 link read bytes and 29.64 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5a96c0000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5a9740000000
- per repetition: home 5.243e+05 link read bytes and 0.78 SMMU translation requests; level 5.243e+05 link read bytes and 0.78 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x56c000000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x56c080000000
- per repetition: home 5.243e+05 link read bytes and 24.18 SMMU translation requests; level 5.243e+05 link read bytes and 27.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x56f100000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x56f1c0000000
- per repetition: home 5.243e+05 link read bytes and 22.23 SMMU translation requests; level 5.243e+05 link read bytes and 15.21 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x51e740000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x51e7c0000000
- per repetition: home 5.243e+05 link read bytes and 0 SMMU translation requests; level 5.243e+05 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5615c0000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x561640000000
- per repetition: home 5.243e+05 link read bytes and 0.78 SMMU translation requests; level 5.243e+05 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x4eb700000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x4eb7c0000000
- per repetition: home 6.711e+07 link read bytes and 2116 SMMU translation requests; level 6.711e+07 link read bytes and 1710 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x49ae40000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x49af00000000
- per repetition: home 6.711e+07 link read bytes and 2049 SMMU translation requests; level 6.711e+07 link read bytes and 1647 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x490500000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x490580000000
- per repetition: home 6.711e+07 link read bytes and 2062 SMMU translation requests; level 6.711e+07 link read bytes and 1969 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x586540000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x586600000000
- per repetition: home 0 link read bytes and 2861 SMMU translation requests; level 0 link read bytes and 2099 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x473100000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x473180000000
- per repetition: home 0 link read bytes and 2938 SMMU translation requests; level 0 link read bytes and 2130 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x59e740000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x59e800000000
- per repetition: home 0 link read bytes and 2913 SMMU translation requests; level 0 link read bytes and 2781 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x562d40000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x562dc0000000
- per repetition: home 6.711e+07 link read bytes and 2087 SMMU translation requests; level 6.711e+07 link read bytes and 2007 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x516480000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x516540000000
- per repetition: home 6.711e+07 link read bytes and 2141 SMMU translation requests; level 6.711e+07 link read bytes and 1735 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x43d700000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x43d7c0000000
- per repetition: home 6.711e+07 link read bytes and 2079 SMMU translation requests; level 6.711e+07 link read bytes and 2084 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x52b580000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x52b640000000
- per repetition: home 0 link read bytes and 2864 SMMU translation requests; level 0 link read bytes and 2037 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x55c640000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x55c6c0000000
- per repetition: home 0 link read bytes and 2960 SMMU translation requests; level 0 link read bytes and 2139 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x59afc0000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x59b080000000
- per repetition: home 0 link read bytes and 2936 SMMU translation requests; level 0 link read bytes and 2814 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x548080000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x548140000000
- per repetition: home 0 link read bytes and 389 SMMU translation requests; level 0 link read bytes and 306.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x571880000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x571900000000
- per repetition: home 0 link read bytes and 394.1 SMMU translation requests; level 0 link read bytes and 320.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5b03c0000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5b0480000000
- per repetition: home 0 link read bytes and 379.9 SMMU translation requests; level 0 link read bytes and 334 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4f3180000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4f3240000000
- per repetition: home 0 link read bytes and 399.9 SMMU translation requests; level 0 link read bytes and 303.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4db940000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4dba00000000
- per repetition: home 0 link read bytes and 405.6 SMMU translation requests; level 0 link read bytes and 346.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x467d00000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x467dc0000000
- per repetition: home 0 link read bytes and 404.7 SMMU translation requests; level 0 link read bytes and 380.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5ead40000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5eae00000000
- per repetition: home 0 link read bytes and 4507 SMMU translation requests; level 0 link read bytes and 2767 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x483740000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x483800000000
- per repetition: home 0 link read bytes and 4537 SMMU translation requests; level 0 link read bytes and 2695 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4b64c0000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4b6580000000
- per repetition: home 0 link read bytes and 4512 SMMU translation requests; level 0 link read bytes and 4190 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x44e780000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x44e840000000
- per repetition: home 0 link read bytes and 4582 SMMU translation requests; level 0 link read bytes and 2678 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4acf80000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4ad000000000
- per repetition: home 0 link read bytes and 4640 SMMU translation requests; level 0 link read bytes and 2691 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5531c0000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x553240000000
- per repetition: home 0 link read bytes and 4636 SMMU translation requests; level 0 link read bytes and 4284 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x420b00000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x420c00000000
- per repetition: home 3.199e+09 link read bytes and 0 SMMU translation requests; level 3.195e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 16 passes per interval, cursor 0, buffer at 0x475380000000; level: placement hbm, 16 passes per interval, cursor 0, buffer at 0x4754c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5c3b80000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5c3c40000000
- per repetition: home 8.43e+06 link read bytes and 336.4 SMMU translation requests; level 8.429e+06 link read bytes and 318.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5e2040000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5e21c0000000
- per repetition: home 8.43e+06 link read bytes and 332.8 SMMU translation requests; level 8.429e+06 link read bytes and 321.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x52b940000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x52ba80000000
- per repetition: home 8.429e+06 link read bytes and 334.4 SMMU translation requests; level 8.428e+06 link read bytes and 335 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x471540000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x471680000000
- per repetition: home 8.429e+06 link read bytes and 329.4 SMMU translation requests; level 8.43e+06 link read bytes and 313.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x547340000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x547400000000
- per repetition: home 8.43e+06 link read bytes and 310.9 SMMU translation requests; level 8.429e+06 link read bytes and 299.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x561040000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x561100000000
- per repetition: home 8.429e+06 link read bytes and 333.7 SMMU translation requests; level 8.429e+06 link read bytes and 330.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x573680000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x573780000000
- per repetition: home 5.366e+08 link read bytes and 642.9 SMMU translation requests; level 5.366e+08 link read bytes and 778.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5ff880000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5ff940000000
- per repetition: home 8.43e+06 link read bytes and 330.3 SMMU translation requests; level 8.429e+06 link read bytes and 333.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x4688c0000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x468980000000
- per repetition: home 5.366e+08 link read bytes and 659.8 SMMU translation requests; level 5.366e+08 link read bytes and 697.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x572b40000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x572c40000000
- per repetition: home 8.429e+06 link read bytes and 330.6 SMMU translation requests; level 8.429e+06 link read bytes and 328.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x4b2680000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x4b2780000000
- per repetition: home 5.366e+08 link read bytes and 230 SMMU translation requests; level 5.366e+08 link read bytes and 202.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x53dac0000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x53dbc0000000
- per repetition: home 8.429e+06 link read bytes and 321.1 SMMU translation requests; level 8.429e+06 link read bytes and 322.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x5ff540000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x5ff600000000
- per repetition: home 0 link read bytes and 952.1 SMMU translation requests; level 0 link read bytes and 953.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x5c0500000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x5c0640000000
- per repetition: home 0 link read bytes and 942.6 SMMU translation requests; level 0 link read bytes and 950.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x517f00000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x518000000000
- per repetition: home 0 link read bytes and 951.9 SMMU translation requests; level 0 link read bytes and 956.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5cf100000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5cf200000000
- per repetition: home 5.366e+08 link read bytes and 816.4 SMMU translation requests; level 5.366e+08 link read bytes and 789 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x564bc0000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x564cc0000000
- per repetition: home 8.429e+06 link read bytes and 327.9 SMMU translation requests; level 8.428e+06 link read bytes and 326.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5c8780000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5c8880000000
- per repetition: home 5.366e+08 link read bytes and 795.9 SMMU translation requests; level 5.366e+08 link read bytes and 762.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x429b40000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x429c00000000
- per repetition: home 8.429e+06 link read bytes and 328.7 SMMU translation requests; level 8.429e+06 link read bytes and 329.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x4500c0000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x4501c0000000
- per repetition: home 5.366e+08 link read bytes and 577.5 SMMU translation requests; level 5.366e+08 link read bytes and 580.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x419980000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x419a40000000
- per repetition: home 8.429e+06 link read bytes and 322.8 SMMU translation requests; level 8.429e+06 link read bytes and 323.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x5eb780000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x5eb880000000
- per repetition: home 0 link read bytes and 948.9 SMMU translation requests; level 0 link read bytes and 947.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x4b8d40000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x4b8e40000000
- per repetition: home 0 link read bytes and 946.5 SMMU translation requests; level 0 link read bytes and 953.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x43fec0000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x43ffc0000000
- per repetition: home 0 link read bytes and 944.8 SMMU translation requests; level 0 link read bytes and 944.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4b38c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4b3980000000
- per repetition: home 5.369e+08 link read bytes and 1.738e+04 SMMU translation requests; level 5.369e+08 link read bytes and 1.739e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5fd600000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5fd700000000
- per repetition: home 5.369e+08 link read bytes and 1.309e+04 SMMU translation requests; level 5.369e+08 link read bytes and 1.307e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x506880000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x506980000000
- per repetition: home 5.369e+08 link read bytes and 4350 SMMU translation requests; level 5.369e+08 link read bytes and 4355 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5daa00000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5dab00000000
- per repetition: home 5.369e+08 link read bytes and 1.74e+04 SMMU translation requests; level 5.369e+08 link read bytes and 1.74e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x551e80000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x551f40000000
- per repetition: home 5.369e+08 link read bytes and 1.315e+04 SMMU translation requests; level 5.369e+08 link read bytes and 1.734e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x53b440000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x53b540000000
- per repetition: home 5.369e+08 link read bytes and 8760 SMMU translation requests; level 5.369e+08 link read bytes and 8714 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x582740000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x582c00000000
- per repetition: home 3.355e+07 link read bytes and 2.025e+06 SMMU translation requests; level 3.355e+07 link read bytes and 2.015e+06 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x4f73c0000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x4f7840000000
- per repetition: home 3.355e+07 link read bytes and 2.025e+06 SMMU translation requests; level 3.355e+07 link read bytes and 2.015e+06 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4bc740000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4bcc00000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4c4600000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4c4ac0000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x482f40000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4833c0000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x51a240000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x51a6c0000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x45b280000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x45b740000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x550500000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x550980000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x473a40000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x473b40000000
- per repetition: home 6.422e+09 link read bytes and 3.608e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.609e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 7 passes per interval, cursor 0, buffer at 0x5d5c00000000; level: placement hbm, 7 passes per interval, cursor 0, buffer at 0x5d5d00000000
- per repetition: home 0 link read bytes and 5519 SMMU translation requests; level 0 link read bytes and 5469 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5e78c0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5e79c0000000
- per repetition: home 6.422e+09 link read bytes and 3.612e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.606e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x592700000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x592800000000
- per repetition: home 6.422e+09 link read bytes and 3.599e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.601e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x433280000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x433380000000
- per repetition: home 6.422e+09 link read bytes and 3.607e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.594e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x59ddc0000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x59dec0000000
- per repetition: home 0 link read bytes and 3.87e+04 SMMU translation requests; level 0 link read bytes and 4.525e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x5249c0000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x524ac0000000
- per repetition: home 0 link read bytes and 3.855e+04 SMMU translation requests; level 0 link read bytes and 4.157e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x475080000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x475180000000
- per repetition: home 0 link read bytes and 4.29e+04 SMMU translation requests; level 0 link read bytes and 4.142e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x495e00000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x495f00000000
- per repetition: home 6.423e+09 link read bytes and 3.622e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.604e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4c5080000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x4c5200000000
- per repetition: home 6.423e+09 link read bytes and 3.616e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.594e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x590c80000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x590dc0000000
- per repetition: home 6.422e+09 link read bytes and 3.603e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.592e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x592380000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x592480000000
- per repetition: home 0 link read bytes and 4.305e+04 SMMU translation requests; level 0 link read bytes and 4.198e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x5d6600000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x5d6740000000
- per repetition: home 0 link read bytes and 4.266e+04 SMMU translation requests; level 0 link read bytes and 4.164e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 6 passes per interval, cursor 0, buffer at 0x5491c0000000; level: placement hbm, 6 passes per interval, cursor 0, buffer at 0x5492c0000000
- per repetition: home 0 link read bytes and 3.864e+04 SMMU translation requests; level 0 link read bytes and 4.471e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x59bc00000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x59be80000000
- per repetition: home 0 link read bytes and 1.328e+05 SMMU translation requests; level 0 link read bytes and 1.328e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x4c1bc0000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x4c1e80000000
- per repetition: home 0 link read bytes and 1.328e+05 SMMU translation requests; level 0 link read bytes and 1.328e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=1

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x51c6c0000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x51c980000000
- per repetition: home 0 link read bytes and 1.327e+05 SMMU translation requests; level 0 link read bytes and 1.328e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x481fc0000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x482240000000
- per repetition: home 0 link read bytes and 1.327e+05 SMMU translation requests; level 0 link read bytes and 1.338e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x5d1c00000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x5d1e80000000
- per repetition: home 0 link read bytes and 1.328e+05 SMMU translation requests; level 0 link read bytes and 1.328e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=1

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 3 passes per interval, cursor 0, buffer at 0x5a0200000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x5a04c0000000
- per repetition: home 0 link read bytes and 1.327e+05 SMMU translation requests; level 0 link read bytes and 1.337e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=stadd,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x56dec0000000; level: placement cpu, 3 passes per interval, cursor 0, buffer at 0x56df40000000
- no hardware counters in this cell

### route/at=stadd,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x52afc0000000; level: placement hbm, 3 passes per interval, cursor 0, buffer at 0x52b040000000
- no hardware counters in this cell

### route/at=stadd,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x449740000000; level: placement cpu, 3 passes per interval, cursor 0, buffer at 0x449800000000
- no hardware counters in this cell

### route/at=stadd,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x49a100000000; level: placement hbm, 2 passes per interval, cursor 0, buffer at 0x49a200000000
- no hardware counters in this cell

### route/at=tiles,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=tiling,working-set-mib=8

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 509 passes per interval, cursor 1, buffer at 0x5f6200000000; level: placement cpu, 544 passes per interval, cursor 1, buffer at 0x5f6300000000
- per repetition: home 8.43e+06 link read bytes and 0 SMMU translation requests; level 8.38e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=tiles,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=tiling,working-set-mib=8

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 1233 passes per interval, cursor 1, buffer at 0x492e40000000; level: placement hbm, 1294 passes per interval, cursor 1, buffer at 0x492f40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,type=factor,vary=strategy

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x5df640000000; level: placement cpu, 3 passes per interval, cursor 0, buffer at 0x5df6c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp,footprint-mib=8,kernel=k6,keys=1048576,placement=hbm,type=factor,vary=strategy

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 112 passes per interval, cursor 0, buffer at 0x5e9800000000; level: placement hbm, 70 passes per interval, cursor 0, buffer at 0x5e9880000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

