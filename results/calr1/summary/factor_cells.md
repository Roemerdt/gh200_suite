# Factor cells: the direct route at a level of one factor against its home level, recomputed from raw rows

Times are per pass in ms. The factor effect on direct access is level minus home within a repeat, as median with its 95 % rank interval; a positive value means the level is slower. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | factor | level | home ms | level ms | effect ms [interval] | relative to home | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|---|---|
| at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=rotated,working-set-mib=8 | rotated | 1 | 0.0376 | 0.3751 | 0.3375 [0.3369, 0.3377] | +896.8 % | 10 | yes | pass |
| at=1024,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=working-set,working-set-mib=32 | working-set | 1024 | 1.4997 | 47.1392 | 45.6398 [45.6210, 45.6625] | +3043.3 % | 10 | yes | pass |
| at=1024,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint | footprint | 1024 | 0.0748 | 0.8148 | 0.7399 [0.7389, 0.7406] | +989.1 % | 10 | yes | pass |
| at=1024,footprint-mib=256,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint | footprint | 1024 | 0.2046 | 0.8156 | 0.6109 [0.6102, 0.6120] | +298.6 % | 10 | yes | pass |
| at=1024,footprint-mib=4096,kernel=k6,placement=cpu,type=factor,update=atomic,vary=footprint | footprint | 1024 | 24.0312 | 5.8266 | -18.2009 [-18.2536, -18.1866] | -75.7 % | 10 | yes | pass |
| at=1024,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=factor,vary=keys | keys | 1024 | 12.3045 | 0.7670 | -11.5375 [-11.5390, -11.5362] | -93.8 % | 10 | yes | pass |
| at=1024,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,type=factor,vary=keys | keys | 1024 | 8.7550 | 12.4984 | 3.7425 [3.7413, 3.7460] | +42.7 % | 10 | yes | pass |
| at=1024,footprint-mib=8,kernel=k6,keys=1048576,placement=hbm,type=factor,vary=keys | keys | 1024 | 0.1790 | 0.7665 | 0.5876 [0.5874, 0.5877] | +328.3 % | 10 | yes | pass |
| at=4,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=repeat | repeat | 4 | 6.0269 | 18.0477 | 12.0207 [12.0173, 12.0402] | +199.5 % | 10 | yes | pass |
| at=4,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=repeat | repeat | 4 | 0.8178 | 1.6390 | 0.8211 [0.8168, 0.8243] | +100.4 % | 10 | yes | pass |
| at=hbm,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=placement | placement | hbm | 10.0578 | 10.0582 | -0.0006 [-0.0022, 0.0026] | -0.0 % | 100 | no | pass |
| at=hbm,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=plain,vary=placement | placement | hbm | 2.3759 | 2.3771 | 0.0008 [-0.0009, 0.0024] | +0.0 % | 100 | no | pass |
| at=hbm,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=placement | placement | hbm | 13.0794 | 18.4544 | 5.3665 [5.1750, 5.5513] | +41.0 % | 90 | yes | pass |
| at=line,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=layout | layout | line | 6.0283 | 3.5399 | -2.4869 [-2.4991, -2.4829] | -41.3 % | 10 | yes | pass |
| at=line,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=layout | layout | line | 0.8172 | 0.3403 | -0.4770 [-0.4777, -0.4761] | -58.4 % | 10 | yes | pass |
| at=none,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=tiling | tiling | none | 26.8523 | 37.6668 | 10.8124 [10.6848, 10.9593] | +40.3 % | 10 | yes | pass |
| at=none,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=tiling | tiling | none | 3.2832 | 2.7461 | -0.5378 [-0.5900, -0.5329] | -16.4 % | 10 | yes | pass |
| at=plain,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | plain | 10.1859 | 2.3072 | -7.8739 [-7.8963, -7.8530] | -77.3 % | 10 | yes | pass |
| at=plain,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | plain | 6.0330 | 5.9977 | -0.0353 [-0.0387, -0.0338] | -0.6 % | 20 | yes | pass |
| at=plain,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | plain | 0.8158 | 0.7677 | -0.0481 [-0.0494, -0.0468] | -5.9 % | 10 | yes | pass |
| at=plain,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | plain | 0.0761 | 0.0790 | 0.0029 [0.0028, 0.0029] | +3.8 % | 10 | yes | pass |
| at=returned,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | returned | 10.0540 | 41.7553 | 31.7068 [31.4454, 31.7859] | +315.4 % | 20 | yes | pass |
| at=returned,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | returned | 6.0485 | 6.0802 | 0.0339 [0.0309, 0.0368] | +0.6 % | 30 | yes | pass |
| at=returned,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | returned | 0.8163 | 0.8976 | 0.0815 [0.0806, 0.0820] | +10.0 % | 10 | yes | pass |
| at=returned,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | returned | 0.0783 | 0.1323 | 0.0541 [0.0540, 0.0541] | +69.1 % | 10 | yes | pass |
| at=returned,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | returned | 13.0291 | 46.2082 | 33.1399 [32.4198, 34.0202] | +254.4 % | 100 | yes | pass |
| at=returned,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | returned | 17.8877 | 48.6094 | 30.9340 [28.3627, 31.2625] | +172.9 % | 100 | yes | pass |
| at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=generator | generator | rmat | 30.7673 | 189.9588 | 159.1872 [159.1414, 159.2716] | +517.4 % | 10 | yes | pass |
| at=rmat,footprint-mib=8192,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=generator | generator | rmat | 247.2547 | 996.7033 | 749.4589 [749.2977, 749.5100] | +303.1 % | 10 | yes | pass |
| at=rmat,footprint-mib=8192,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=generator | generator | rmat | 15.1369 | 395.7373 | 380.6017 [378.1096, 383.0412] | +2514.4 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0202 | 0.0211 | 0.0009 [0.0009, 0.0010] | +4.4 % | 40 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing | sharing | shared | 0.0201 | 0.0208 | 0.0007 [0.0007, 0.0008] | +3.6 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0203 | 0.0204 | 0.0001 [0.0000, 0.0001] | +0.4 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing | sharing | shared | 0.1928 | 0.1919 | -0.0010 [-0.0011, -0.0009] | -0.5 % | 80 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 0.1934 | 0.3778 | 0.1843 [0.1839, 0.1847] | +95.3 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing | sharing | shared | 0.1922 | 0.1920 | -0.0002 [-0.0002, -0.0001] | -0.1 % | 100 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0372 | 0.1619 | 0.1244 [0.1223, 0.1251] | +334.5 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0349 | 0.1815 | 0.1465 [0.1443, 0.1469] | +419.2 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0373 | 0.0360 | -0.0013 [-0.0014, -0.0012] | -3.5 % | 30 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing | sharing | shared | 0.1921 | 0.1938 | 0.0016 [0.0015, 0.0018] | +0.8 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing | sharing | shared | 0.1936 | 0.1920 | -0.0015 [-0.0017, -0.0014] | -0.8 % | 50 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0378 | 0.1642 | 0.1265 [0.1255, 0.1279] | +334.4 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0353 | 0.1801 | 0.1449 [0.1448, 0.1452] | +410.4 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0149 | 0.0571 | 0.0420 [0.0419, 0.0425] | +282.4 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0150 | 0.0513 | 0.0363 [0.0358, 0.0367] | +242.0 % | 40 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0151 | 0.0161 | 0.0010 [0.0009, 0.0011] | +6.8 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0557 | 0.2256 | 0.1699 [0.1691, 0.1710] | +305.1 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0498 | 0.0490 | -0.0008 [-0.0009, -0.0007] | -1.6 % | 90 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | sharing | shared | 0.0563 | 0.2346 | 0.1783 [0.1773, 0.1792] | +316.7 % | 10 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | sharing | shared | 0.0498 | 0.2643 | 0.2143 [0.2139, 0.2148] | +430.4 % | 20 | yes | pass |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | sharing | shared | 0.0496 | 0.0493 | -0.0003 [-0.0004, -0.0003] | -0.6 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=factor,vary=sharing | sharing | shared | 30.7309 | 30.4304 | -0.3009 [-0.3087, -0.2929] | -1.0 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=factor,vary=sharing | sharing | shared | 1.2774 | 1.2771 | -0.0008 [-0.0018, 0.0007] | -0.1 % | 100 | no | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0448 | 0.0620 | 0.0171 [0.0168, 0.0174] | +38.2 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0450 | 0.0656 | 0.0207 [0.0203, 0.0211] | +45.9 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0450 | 0.0450 | -0.0001 [-0.0001, -0.0000] | -0.2 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0445 | 0.0636 | 0.0192 [0.0190, 0.0193] | +43.2 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8 | sharing | shared | 0.0445 | 0.0660 | 0.0215 [0.0212, 0.0216] | +48.3 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32 | sharing | shared | 1.4830 | 1.5075 | 0.0244 [0.0237, 0.0252] | +1.6 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8 | sharing | shared | 0.0445 | 0.0444 | -0.0000 [-0.0001, 0.0000] | -0.1 % | 100 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 1.5021 | 1.5147 | 0.0128 [0.0117, 0.0139] | +0.9 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0506 | 0.0515 | 0.0009 [0.0008, 0.0010] | +1.7 % | 50 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32 | sharing | shared | 0.1073 | 0.1060 | -0.0012 [-0.0013, -0.0010] | -1.1 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.1143 | 0.1139 | -0.0003 [-0.0005, -0.0001] | -0.3 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.1289 | 0.1310 | 0.0020 [0.0016, 0.0026] | +1.6 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32 | sharing | shared | 1.5126 | 1.4993 | -0.0136 [-0.0145, -0.0126] | -0.9 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8 | sharing | shared | 0.0441 | 0.0442 | 0.0000 [-0.0000, 0.0001] | +0.1 % | 100 | no | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 1.5100 | 1.4866 | -0.0232 [-0.0248, -0.0219] | -1.5 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8 | sharing | shared | 0.0501 | 0.0489 | -0.0012 [-0.0014, -0.0011] | -2.4 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 1.5206 | 1.5043 | -0.0165 [-0.0169, -0.0161] | -1.1 % | 10 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8 | sharing | shared | 0.0516 | 0.0520 | 0.0005 [0.0003, 0.0010] | +1.0 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32 | sharing | shared | 0.1129 | 0.1144 | 0.0014 [0.0013, 0.0016] | +1.3 % | 40 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32 | sharing | shared | 0.1269 | 0.1280 | 0.0012 [0.0009, 0.0015] | +0.9 % | 100 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01 | sharing | shared | 5.4232 | 5.4353 | 0.0120 [0.0110, 0.0130] | +0.2 % | 90 | yes | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01 | sharing | shared | 5.4338 | 5.4328 | -0.0008 [-0.0013, 0.0036] | -0.0 % | 100 | no | pass |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1 | sharing | shared | 5.4214 | 5.4136 | -0.0045 [-0.0099, -0.0028] | -0.1 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | sharing | shared | 7.2552 | 7.2361 | -0.0196 [-0.0231, 0.0002] | -0.3 % | 100 | no | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01 | sharing | shared | 433.3733 | 433.4312 | 0.0594 [0.0463, 0.0712] | +0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1 | sharing | shared | 433.4082 | 433.4435 | 0.0360 [0.0148, 0.0585] | +0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1 | sharing | shared | 433.2943 | 433.3365 | 0.0399 [0.0254, 0.0501] | +0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1 | sharing | shared | 433.3113 | 433.3560 | 0.0453 [0.0183, 0.0665] | +0.0 % | 100 | yes | pass |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing | sharing | shared | 26.5291 | 23.5064 | -3.0223 [-3.0277, -3.0167] | -11.4 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | sharing | shared | 26.9457 | 23.3055 | -3.6417 [-3.6489, -3.6282] | -13.5 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | sharing | shared | 26.6195 | 23.4914 | -3.1306 [-3.1374, -3.1230] | -11.8 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | sharing | shared | 26.5372 | 23.2786 | -3.2559 [-3.2618, -3.2492] | -12.3 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | sharing | shared | 3.5595 | 3.6031 | 0.0433 [0.0406, 0.0462] | +1.2 % | 30 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | sharing | shared | 3.5420 | 3.5666 | 0.0247 [0.0222, 0.0269] | +0.7 % | 70 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | sharing | shared | 3.4707 | 3.5989 | 0.1267 [0.1235, 0.1336] | +3.7 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | sharing | shared | 26.6629 | 23.2126 | -3.4520 [-3.4613, -3.4420] | -12.9 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | sharing | shared | 26.5454 | 23.2582 | -3.2861 [-3.2983, -3.2670] | -12.4 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | sharing | shared | 26.8133 | 23.3819 | -3.4307 [-3.4430, -3.4238] | -12.8 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | sharing | shared | 3.4658 | 3.5920 | 0.1267 [0.1204, 0.1292] | +3.7 % | 10 | yes | pass |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | sharing | shared | 3.5637 | 3.5892 | 0.0247 [0.0225, 0.0269] | +0.7 % | 30 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=1 | sharing | shared | 8.0828 | 8.1070 | 0.0244 [0.0220, 0.0265] | +0.3 % | 40 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01 | sharing | shared | 8.0619 | 8.0984 | 0.0358 [0.0342, 0.0407] | +0.4 % | 10 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1 | sharing | shared | 8.0596 | 8.0968 | 0.0373 [0.0337, 0.0388] | +0.5 % | 10 | yes | pass |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=1 | sharing | shared | 8.1120 | 8.1027 | -0.0090 [-0.0105, -0.0077] | -0.1 % | 100 | yes | pass |
| at=stadd,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update | update | stadd | 13.0290 | 9.1442 | -3.8691 [-4.0005, -3.6588] | -29.7 % | 20 | yes | pass |
| at=stadd,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update | update | stadd | 17.3648 | 11.3897 | -5.9886 [-6.1915, -5.7973] | -34.5 % | 10 | yes | pass |
| at=tiles,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=tiling,working-set-mib=8 | tiling | tiles | 0.0378 | 0.0367 | -0.0011 [-0.0011, -0.0010] | -2.9 % | 10 | yes | pass |
| at=tiles,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=tiling,working-set-mib=8 | tiling | tiles | 0.0161 | 0.0154 | -0.0007 [-0.0007, -0.0007] | -4.2 % | 10 | yes | pass |
| at=warp,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,type=factor,vary=strategy | strategy | warp | 8.5464 | 8.3375 | -0.2098 [-0.2142, -0.2053] | -2.5 % | 10 | yes | pass |

## Host phases

The CPU phase before every pass, timed on the CPU clock (ms per pass), and the state check's median load latency on the preparing core after the phase (ns per sampled load), per variant.

| cell | home CPU ms | home state ns | level CPU ms | level state ns |
|---|---|---|---|---|
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | 0.2467 | 61.6 | 0.2445 | 62.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing | 0.2610 | 63.9 | 0.2576 | 61.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing | 0.2518 | 189.5 | 0.2478 | 69.6 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing | 5.2827 | 58.4 | 5.9269 | 151.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing | 2.7803 | 56.0 | 3.3529 | 87.0 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing | 3.9452 | 219.9 | 3.9420 | 216.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | 5.0217 | 62.6 | 5.7633 | 126.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | 2.8696 | 103.6 | 3.4491 | 149.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | 3.9741 | 461.1 | 3.8878 | 427.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing | 5.2325 | 68.4 | 5.4670 | 189.8 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing | 3.4871 | 203.9 | 3.4752 | 220.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | 4.9993 | 127.8 | 5.0745 | 190.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | 2.8939 | 105.0 | 2.9393 | 159.5 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | 1.1916 | 69.8 | 1.2673 | 88.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing | 0.9260 | 67.8 | 1.0118 | 75.1 |
| at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | 0.9746 | 379.5 | 1.0257 | 373.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing | 7.4070 | 170.4 | 7.8337 | 226.2 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing | 5.5245 | 481.8 | 5.5001 | 458.4 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing | 7.2178 | 82.9 | 7.2610 | 162.6 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing | 3.8980 | 312.6 | 4.0899 | 371.6 |
| at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing | 4.3677 | 481.4 | 4.4372 | 465.6 |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=factor,vary=sharing | 1.2299 | - | 1.6569 | - |
| at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=factor,vary=sharing | 2.2093 | - | 3.6949 | - |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8 | 0.9448 | 72.2 | 0.9308 | 81.8 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8 | 0.6584 | 61.2 | 0.6501 | 67.1 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8 | 0.7092 | 199.2 | 0.7100 | 199.1 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8 | 0.8829 | 78.4 | 0.8736 | 73.6 |
| at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8 | 0.5262 | 65.0 | 0.5255 | 64.6 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32 | 0.5768 | 64.2 | 0.5877 | 100.6 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8 | 0.5885 | 73.6 | 0.5920 | 113.8 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32 | 4.2399 | 90.6 | 4.3006 | 158.5 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8 | 4.0913 | 112.9 | 4.0922 | 172.0 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32 | 0.9834 | 73.1 | 0.9826 | 115.6 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32 | 5.3213 | 337.2 | 5.3296 | 347.1 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32 | 31.4948 | 532.4 | 31.6648 | 564.1 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32 | 0.5661 | 75.6 | 0.5680 | 114.8 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8 | 0.5449 | 84.8 | 0.5437 | 122.9 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32 | 3.6995 | 97.0 | 3.7202 | 151.6 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8 | 3.6149 | 119.1 | 3.6189 | 145.0 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32 | 22.4224 | 270.2 | 22.4324 | 280.5 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8 | 20.4425 | 268.0 | 20.2017 | 288.1 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32 | 5.0314 | 363.6 | 5.0392 | 402.8 |
| at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32 | 27.8496 | 554.0 | 27.8302 | 565.1 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01 | 0.6012 | 68.0 | 0.7422 | 106.6 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01 | 0.5623 | 66.5 | 0.6622 | 99.5 |
| at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1 | 22.5059 | 264.8 | 22.5118 | 269.0 |
| at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing | 1.8539 | 97.2 | 2.9498 | 103.4 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01 | 8.0530 | 170.4 | 8.4408 | 184.2 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1 | 42.2037 | 323.0 | 41.6788 | 327.9 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1 | 350.1539 | 364.4 | 349.3088 | 365.4 |
| at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1 | 33.4073 | 287.2 | 32.9969 | 305.4 |
| at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing | 27.1973 | - | 28.2038 | - |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | 0.4207 | 63.1 | 0.4919 | 83.6 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | 2.1104 | 79.9 | 2.5938 | 125.1 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | 17.2430 | 283.5 | 16.7047 | 283.8 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | 0.8569 | 67.0 | 0.9112 | 100.9 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | 3.0618 | 246.1 | 3.0745 | 304.6 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | 16.2039 | 496.2 | 16.2382 | 522.9 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | 0.3793 | 58.8 | 0.4042 | 80.6 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | 1.9019 | 85.1 | 2.0300 | 155.0 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1 | 12.7158 | 260.4 | 12.2365 | 269.0 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01 | 0.7818 | 73.0 | 0.8057 | 96.8 |
| at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1 | 2.6045 | 241.8 | 2.6201 | 296.2 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=1 | 190.1871 | 621.5 | 193.1954 | 619.5 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01 | 4.5888 | 336.2 | 4.6230 | 352.1 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1 | 23.8135 | 549.5 | 23.8126 | 577.5 |
| at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=1 | 166.5888 | 622.2 | 167.7675 | 627.6 |

## Per cell

### route/at=1,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=rotated,working-set-mib=8

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 532 passes per interval, cursor 1, buffer at 0x4fd0c0000000; level: placement cpu, 54 passes per interval, cursor 1, buffer at 0x4fd180000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 1.341e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=working-set,working-set-mib=32

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5b1bc0000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5b1c80000000
- per repetition: home 5.365e+08 link read bytes and 0 SMMU translation requests; level 1.718e+10 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 268 passes per interval, cursor 0, buffer at 0x425380000000; level: placement hbm, 25 passes per interval, cursor 0, buffer at 0x425400000000
- per repetition: home 0 link read bytes and 3.14 SMMU translation requests; level 0 link read bytes and 1571 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=256,kernel=k6,placement=hbm,type=factor,update=atomic,vary=footprint

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 98 passes per interval, cursor 0, buffer at 0x428200000000; level: placement hbm, 25 passes per interval, cursor 0, buffer at 0x4282c0000000
- per repetition: home 0 link read bytes and 102.5 SMMU translation requests; level 0 link read bytes and 1288 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=4096,kernel=k6,placement=cpu,type=factor,update=atomic,vary=footprint

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x438cc0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x438e80000000
- per repetition: home 0 link read bytes and 6.634e+04 SMMU translation requests; level 0 link read bytes and 4195 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8,kernel=k6,keys=1,placement=hbm,type=factor,vary=keys

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x4776c0000000; level: placement hbm, 27 passes per interval, cursor 0, buffer at 0x477780000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,type=factor,vary=keys

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x502800000000; level: placement cpu, 2 passes per interval, cursor 0, buffer at 0x502880000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=1024,footprint-mib=8,kernel=k6,keys=1048576,placement=hbm,type=factor,vary=keys

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 112 passes per interval, cursor 0, buffer at 0x5f7dc0000000; level: placement hbm, 27 passes per interval, cursor 0, buffer at 0x5f7e40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=4,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=repeat

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5e8bc0000000; level: placement cpu, 2 passes per interval, cursor 0, buffer at 0x5e8cc0000000
- per repetition: home 0 link read bytes and 4226 SMMU translation requests; level 0 link read bytes and 8276 SMMU translation requests; multiplexed rows voided: 0

### route/at=4,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=repeat

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 25 passes per interval, cursor 0, buffer at 0x4dbec0000000; level: placement hbm, 13 passes per interval, cursor 0, buffer at 0x4dc000000000
- per repetition: home 0 link read bytes and 1275 SMMU translation requests; level 0 link read bytes and 2039 SMMU translation requests; multiplexed rows voided: 0

### route/at=hbm,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=placement

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x4febc0000000; level: placement hbm, 2 passes per interval, cursor 0, buffer at 0x4fec80000000
- no hardware counters in this cell

### route/at=hbm,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=plain,vary=placement

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 9 passes per interval, cursor 0, buffer at 0x446640000000; level: placement hbm, 9 passes per interval, cursor 0, buffer at 0x446700000000
- no hardware counters in this cell

### route/at=hbm,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=placement

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x511340000000; level: placement hbm, 2 passes per interval, cursor 0, buffer at 0x5113c0000000
- no hardware counters in this cell

### route/at=line,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=layout

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x450b80000000; level: placement cpu, 6 passes per interval, cursor 0, buffer at 0x450c80000000
- per repetition: home 0 link read bytes and 4226 SMMU translation requests; level 0 link read bytes and 2881 SMMU translation requests; multiplexed rows voided: 0

### route/at=line,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=layout

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 25 passes per interval, cursor 0, buffer at 0x434500000000; level: placement hbm, 59 passes per interval, cursor 0, buffer at 0x434600000000
- per repetition: home 0 link read bytes and 1275 SMMU translation requests; level 0 link read bytes and 409.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=none,footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=tiling

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x55df00000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x55e000000000
- per repetition: home 6.422e+09 link read bytes and 3.633e+04 SMMU translation requests; level 1.307e+10 link read bytes and 3.498e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=none,footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=tiling

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 7 passes per interval, cursor 0, buffer at 0x501380000000; level: placement hbm, 8 passes per interval, cursor 0, buffer at 0x501480000000
- per repetition: home 0 link read bytes and 5972 SMMU translation requests; level 0 link read bytes and 9864 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x514e00000000; level: placement hbm, 9 passes per interval, cursor 0, buffer at 0x514ec0000000
- no hardware counters in this cell

### route/at=plain,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x4252c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x425380000000
- per repetition: home 0 link read bytes and 4175 SMMU translation requests; level 1.074e+09 link read bytes and 4538 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 25 passes per interval, cursor 0, buffer at 0x565780000000; level: placement hbm, 27 passes per interval, cursor 0, buffer at 0x5658c0000000
- per repetition: home 0 link read bytes and 1223 SMMU translation requests; level 0 link read bytes and 2773 SMMU translation requests; multiplexed rows voided: 0

### route/at=plain,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 263 passes per interval, cursor 0, buffer at 0x5f4640000000; level: placement hbm, 254 passes per interval, cursor 0, buffer at 0x5f4700000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=returned,footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x5f8200000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5f82c0000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=1024,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5916c0000000; level: placement cpu, 4 passes per interval, cursor 0, buffer at 0x5917c0000000
- per repetition: home 0 link read bytes and 4190 SMMU translation requests; level 1.074e+09 link read bytes and 4500 SMMU translation requests; multiplexed rows voided: 0

### route/at=returned,footprint-mib=1024,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 25 passes per interval, cursor 0, buffer at 0x5cbc40000000; level: placement hbm, 23 passes per interval, cursor 0, buffer at 0x5cbd40000000
- per repetition: home 0 link read bytes and 1268 SMMU translation requests; level 0 link read bytes and 3002 SMMU translation requests; multiplexed rows voided: 0

### route/at=returned,footprint-mib=16,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 256 passes per interval, cursor 0, buffer at 0x5e0280000000; level: placement hbm, 152 passes per interval, cursor 0, buffer at 0x5e0340000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=returned,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x5b7f40000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x5b8000000000
- no hardware counters in this cell

### route/at=returned,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x5767c0000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x576840000000
- no hardware counters in this cell

### route/at=rmat,footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=generator

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x539e80000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x539f80000000
- per repetition: home 3.198e+09 link read bytes and 0 SMMU translation requests; level 2.853e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=rmat,footprint-mib=8192,generator=uniform,kernel=k4,placement=cpu,type=factor,vary=generator

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 1 passes per interval, cursor 0, buffer at 0x53e340000000; level: placement cpu, 1 passes per interval, cursor 0, buffer at 0x53e600000000
- per repetition: home 2.553e+10 link read bytes and 1.365e+05 SMMU translation requests; level 2.415e+10 link read bytes and 1.501e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=rmat,footprint-mib=8192,generator=uniform,kernel=k4,placement=hbm,type=factor,vary=generator

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x51e9c0000000; level: placement hbm, 1 passes per interval, cursor 0, buffer at 0x51ec40000000
- per repetition: home 0 link read bytes and 1.434e+05 SMMU translation requests; level 0 link read bytes and 1.642e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5281c0000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x528240000000
- per repetition: home 5.243e+05 link read bytes and 0.78 SMMU translation requests; level 5.243e+05 link read bytes and 0.78 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5850c0000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x585140000000
- per repetition: home 5.243e+05 link read bytes and 0.78 SMMU translation requests; level 5.243e+05 link read bytes and 0.78 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=0.5,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5e9780000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x5e9800000000
- per repetition: home 5.243e+05 link read bytes and 0.78 SMMU translation requests; level 5.243e+05 link read bytes and 0.78 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x55b9c0000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x55ba80000000
- per repetition: home 6.711e+07 link read bytes and 2132 SMMU translation requests; level 6.711e+07 link read bytes and 1945 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x533780000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x533800000000
- per repetition: home 6.711e+07 link read bytes and 2115 SMMU translation requests; level 6.711e+07 link read bytes and 1698 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x41ed00000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x41ed80000000
- per repetition: home 6.711e+07 link read bytes and 1756 SMMU translation requests; level 6.711e+07 link read bytes and 1948 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x57ba40000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x57bb00000000
- per repetition: home 0 link read bytes and 2902 SMMU translation requests; level 0 link read bytes and 2065 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x523a80000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x523b00000000
- per repetition: home 0 link read bytes and 2937 SMMU translation requests; level 0 link read bytes and 2112 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4d34c0000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4d3540000000
- per repetition: home 0 link read bytes and 2940 SMMU translation requests; level 0 link read bytes and 2802 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x4ec8c0000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x4ec940000000
- per repetition: home 6.711e+07 link read bytes and 2176 SMMU translation requests; level 6.711e+07 link read bytes and 2047 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=cpu,state=evicted,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 0, buffer at 0x472e00000000; level: placement cpu, 50 passes per interval, cursor 0, buffer at 0x472e80000000
- per repetition: home 6.711e+07 link read bytes and 1663 SMMU translation requests; level 6.711e+07 link read bytes and 1900 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4f2340000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4f2400000000
- per repetition: home 0 link read bytes and 2892 SMMU translation requests; level 0 link read bytes and 2095 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=64,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x54b380000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x54b400000000
- per repetition: home 0 link read bytes and 2920 SMMU translation requests; level 0 link read bytes and 2092 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x484f80000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x485000000000
- per repetition: home 0 link read bytes and 387.7 SMMU translation requests; level 0 link read bytes and 308.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=line,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4b3d40000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4b3e00000000
- per repetition: home 0 link read bytes and 401.7 SMMU translation requests; level 0 link read bytes and 316.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=8,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x592900000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5929c0000000
- per repetition: home 0 link read bytes and 398.6 SMMU translation requests; level 0 link read bytes and 314.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=clean,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4c2140000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4c2240000000
- per repetition: home 0 link read bytes and 4520 SMMU translation requests; level 0 link read bytes and 2718 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=line,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5f4fc0000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x5f5080000000
- per repetition: home 0 link read bytes and 4547 SMMU translation requests; level 0 link read bytes and 4258 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=clean,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x42da40000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x42db00000000
- per repetition: home 0 link read bytes and 4476 SMMU translation requests; level 0 link read bytes and 2653 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=dirty,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4a57c0000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4a5880000000
- per repetition: home 0 link read bytes and 4415 SMMU translation requests; level 0 link read bytes and 2751 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,f-den=1,f-num=1,footprint-mib=96,host=state,kernel=k1,pattern=word,placement=hbm,state=evicted,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4e3900000000; level: placement hbm, 50 passes per interval, cursor 0, buffer at 0x4e39c0000000
- per repetition: home 0 link read bytes and 4538 SMMU translation requests; level 0 link read bytes and 4266 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,type=factor,vary=sharing

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 10 passes per interval, cursor 0, buffer at 0x45d600000000; level: placement cpu, 10 passes per interval, cursor 0, buffer at 0x45d700000000
- per repetition: home 3.198e+09 link read bytes and 0 SMMU translation requests; level 3.195e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 16 passes per interval, cursor 0, buffer at 0x58eb40000000; level: placement hbm, 16 passes per interval, cursor 0, buffer at 0x58ec00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x42b500000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x42b5c0000000
- per repetition: home 8.382e+06 link read bytes and 333.8 SMMU translation requests; level 8.382e+06 link read bytes and 317.7 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x506040000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x506140000000
- per repetition: home 8.382e+06 link read bytes and 327.7 SMMU translation requests; level 8.382e+06 link read bytes and 317 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=line,placement=cpu,state=evicted,type=factor,vary=sharing,working-set-mib=8

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x404200000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x404300000000
- per repetition: home 8.382e+06 link read bytes and 333.2 SMMU translation requests; level 8.382e+06 link read bytes and 333.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=clean,type=factor,vary=sharing,working-set-mib=8

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5fda80000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5fdb80000000
- per repetition: home 8.382e+06 link read bytes and 337 SMMU translation requests; level 8.382e+06 link read bytes and 317.1 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=state,k=16,kernel=k2,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing,working-set-mib=8

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x523c80000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x523d80000000
- per repetition: home 8.382e+06 link read bytes and 316.6 SMMU translation requests; level 8.382e+06 link read bytes and 302.8 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x40f6c0000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x40f7c0000000
- per repetition: home 5.366e+08 link read bytes and 621.4 SMMU translation requests; level 5.366e+08 link read bytes and 729.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x4ec980000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x4eca40000000
- per repetition: home 8.382e+06 link read bytes and 336.9 SMMU translation requests; level 8.382e+06 link read bytes and 335.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5406c0000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x540780000000
- per repetition: home 5.365e+08 link read bytes and 788.8 SMMU translation requests; level 5.365e+08 link read bytes and 755 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x4e6600000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x4e6700000000
- per repetition: home 8.382e+06 link read bytes and 331.5 SMMU translation requests; level 8.382e+06 link read bytes and 330.5 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.01,working-set-mib=32

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x490b80000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x490c40000000
- per repetition: home 0 link read bytes and 954.1 SMMU translation requests; level 0 link read bytes and 957.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x4d4f80000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x4d5080000000
- per repetition: home 0 link read bytes and 938.9 SMMU translation requests; level 0 link read bytes and 945.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=line,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x4f9000000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x4f9100000000
- per repetition: home 0 link read bytes and 950.6 SMMU translation requests; level 0 link read bytes and 957.3 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=32

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5dbb00000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5dbbc0000000
- per repetition: home 5.365e+08 link read bytes and 849.2 SMMU translation requests; level 5.366e+08 link read bytes and 865.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01,working-set-mib=8

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x536140000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x536240000000
- per repetition: home 8.382e+06 link read bytes and 321.3 SMMU translation requests; level 8.382e+06 link read bytes and 321.6 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=32

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5a5d80000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x5a5e40000000
- per repetition: home 5.365e+08 link read bytes and 840.1 SMMU translation requests; level 5.366e+08 link read bytes and 790 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1,working-set-mib=8

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x47bc80000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x47bd80000000
- per repetition: home 8.382e+06 link read bytes and 330.5 SMMU translation requests; level 8.382e+06 link read bytes and 333.4 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=32

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 14 passes per interval, cursor 0, buffer at 0x4af540000000; level: placement cpu, 14 passes per interval, cursor 0, buffer at 0x4af600000000
- per repetition: home 5.365e+08 link read bytes and 385.1 SMMU translation requests; level 5.366e+08 link read bytes and 330 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=cpu,type=factor,vary=sharing,w=1,working-set-mib=8

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5ec400000000; level: placement cpu, 50 passes per interval, cursor 1, buffer at 0x5ec4c0000000
- per repetition: home 8.382e+06 link read bytes and 322.4 SMMU translation requests; level 8.382e+06 link read bytes and 321 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1,working-set-mib=32

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x553840000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x553980000000
- per repetition: home 0 link read bytes and 948.9 SMMU translation requests; level 0 link read bytes and 950.9 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,k=16,kernel=k2,pattern=word,placement=hbm,type=factor,vary=sharing,w=1,working-set-mib=32

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 50 passes per interval, cursor 1, buffer at 0x55a0c0000000; level: placement hbm, 50 passes per interval, cursor 1, buffer at 0x55a1c0000000
- per repetition: home 0 link read bytes and 946.4 SMMU translation requests; level 0 link read bytes and 953.2 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 10 passes per interval, cursor 0, buffer at 0x5bf380000000; level: placement cpu, 10 passes per interval, cursor 0, buffer at 0x5bf480000000
- per repetition: home 5.369e+08 link read bytes and 1.56e+04 SMMU translation requests; level 5.369e+08 link read bytes and 1.736e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.01

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 10 passes per interval, cursor 0, buffer at 0x4d7ac0000000; level: placement cpu, 10 passes per interval, cursor 0, buffer at 0x4d7bc0000000
- per repetition: home 5.369e+08 link read bytes and 1.736e+04 SMMU translation requests; level 5.369e+08 link read bytes and 1.74e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=1024,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=1

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 10 passes per interval, cursor 0, buffer at 0x5a1180000000; level: placement cpu, 10 passes per interval, cursor 0, buffer at 0x5a1280000000
- per repetition: home 5.369e+08 link read bytes and 8680 SMMU translation requests; level 5.369e+08 link read bytes and 6962 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=state,kernel=k3p,pattern=word,placement=cpu,state=dirty,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 10 passes per interval, cursor 0, buffer at 0x514180000000; level: placement cpu, 10 passes per interval, cursor 0, buffer at 0x514600000000
- per repetition: home 3.355e+07 link read bytes and 2.024e+06 SMMU translation requests; level 3.355e+07 link read bytes and 2.018e+06 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.01

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 10 passes per interval, cursor 0, buffer at 0x448240000000; level: placement cpu, 10 passes per interval, cursor 0, buffer at 0x448700000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=0.1

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 10 passes per interval, cursor 0, buffer at 0x56d840000000; level: placement cpu, 10 passes per interval, cursor 0, buffer at 0x56dcc0000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=line,placement=cpu,type=factor,vary=sharing,w=1

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 10 passes per interval, cursor 0, buffer at 0x5cc0c0000000; level: placement cpu, 10 passes per interval, cursor 0, buffer at 0x5cc580000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=16384,host=writes,kernel=k3,pattern=word,placement=cpu,type=factor,vary=sharing,w=0.1

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 10 passes per interval, cursor 0, buffer at 0x586640000000; level: placement cpu, 10 passes per interval, cursor 0, buffer at 0x586ac0000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=reads,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 10 passes per interval, cursor 0, buffer at 0x5fdac0000000; level: placement cpu, 10 passes per interval, cursor 0, buffer at 0x5fdbc0000000
- per repetition: home 6.422e+09 link read bytes and 3612 SMMU translation requests; level 6.423e+09 link read bytes and 3600 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 10 passes per interval, cursor 0, buffer at 0x57cc40000000; level: placement cpu, 10 passes per interval, cursor 0, buffer at 0x57cd40000000
- per repetition: home 6.422e+09 link read bytes and 2.17e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.591e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 10 passes per interval, cursor 0, buffer at 0x52a500000000; level: placement cpu, 10 passes per interval, cursor 0, buffer at 0x52a600000000
- per repetition: home 6.422e+09 link read bytes and 3.61e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.236e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 10 passes per interval, cursor 0, buffer at 0x5e0000000000; level: placement cpu, 10 passes per interval, cursor 0, buffer at 0x5e0100000000
- per repetition: home 6.422e+09 link read bytes and 7252 SMMU translation requests; level 6.423e+09 link read bytes and 1.255e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 10 passes per interval, cursor 0, buffer at 0x43ca00000000; level: placement hbm, 10 passes per interval, cursor 0, buffer at 0x43cb00000000
- per repetition: home 0 link read bytes and 3.873e+04 SMMU translation requests; level 0 link read bytes and 4.183e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 10 passes per interval, cursor 0, buffer at 0x5f5dc0000000; level: placement hbm, 10 passes per interval, cursor 0, buffer at 0x5f5f00000000
- per repetition: home 0 link read bytes and 3.855e+04 SMMU translation requests; level 0 link read bytes and 4.179e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=line,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 10 passes per interval, cursor 0, buffer at 0x5ccec0000000; level: placement hbm, 10 passes per interval, cursor 0, buffer at 0x5ccfc0000000
- per repetition: home 0 link read bytes and 4.287e+04 SMMU translation requests; level 0 link read bytes and 4.156e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 10 passes per interval, cursor 0, buffer at 0x4d6000000000; level: placement cpu, 10 passes per interval, cursor 0, buffer at 0x4d6100000000
- per repetition: home 6.422e+09 link read bytes and 7250 SMMU translation requests; level 6.423e+09 link read bytes and 3.253e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 10 passes per interval, cursor 0, buffer at 0x59b500000000; level: placement cpu, 10 passes per interval, cursor 0, buffer at 0x59b600000000
- per repetition: home 6.422e+09 link read bytes and 3.597e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.406e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=cpu,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=1

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 10 passes per interval, cursor 0, buffer at 0x502d40000000; level: placement cpu, 10 passes per interval, cursor 0, buffer at 0x502e80000000
- per repetition: home 6.422e+09 link read bytes and 3.239e+04 SMMU translation requests; level 6.423e+09 link read bytes and 3.24e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.01

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 10 passes per interval, cursor 0, buffer at 0x5510c0000000; level: placement hbm, 10 passes per interval, cursor 0, buffer at 0x551200000000
- per repetition: home 0 link read bytes and 4.3e+04 SMMU translation requests; level 0 link read bytes and 4.185e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=512,host=writes,kernel=k5,pattern=word,placement=hbm,sweeps=8,tiling=tiles,type=factor,vary=sharing,w=0.1

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 10 passes per interval, cursor 0, buffer at 0x40ba00000000; level: placement hbm, 10 passes per interval, cursor 0, buffer at 0x40bb00000000
- per repetition: home 0 link read bytes and 3.871e+04 SMMU translation requests; level 0 link read bytes and 4.168e+04 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=line,placement=hbm,type=factor,vary=sharing,w=1

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 10 passes per interval, cursor 0, buffer at 0x52d080000000; level: placement hbm, 10 passes per interval, cursor 0, buffer at 0x52d340000000
- per repetition: home 0 link read bytes and 1.327e+05 SMMU translation requests; level 0 link read bytes and 1.344e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.01

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 10 passes per interval, cursor 0, buffer at 0x44edc0000000; level: placement hbm, 10 passes per interval, cursor 0, buffer at 0x44f040000000
- per repetition: home 0 link read bytes and 1.327e+05 SMMU translation requests; level 0 link read bytes and 1.329e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=0.1

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 10 passes per interval, cursor 0, buffer at 0x515180000000; level: placement hbm, 10 passes per interval, cursor 0, buffer at 0x515440000000
- per repetition: home 0 link read bytes and 1.33e+05 SMMU translation requests; level 0 link read bytes and 1.328e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=shared,footprint-mib=8192,host=writes,kernel=k3,pattern=word,placement=hbm,type=factor,vary=sharing,w=1

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 10 passes per interval, cursor 0, buffer at 0x443800000000; level: placement hbm, 10 passes per interval, cursor 0, buffer at 0x443a80000000
- per repetition: home 0 link read bytes and 1.328e+05 SMMU translation requests; level 0 link read bytes and 1.328e+05 SMMU translation requests; multiplexed rows voided: 0

### route/at=stadd,footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=factor,update=atomic,vary=update

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 2 passes per interval, cursor 0, buffer at 0x5693c0000000; level: placement cpu, 3 passes per interval, cursor 0, buffer at 0x569480000000
- no hardware counters in this cell

### route/at=stadd,footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=factor,update=atomic,vary=update

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 2 passes per interval, cursor 0, buffer at 0x4a40c0000000; level: placement hbm, 2 passes per interval, cursor 0, buffer at 0x4a4140000000
- no hardware counters in this cell

### route/at=tiles,footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=factor,vary=tiling,working-set-mib=8

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 531 passes per interval, cursor 1, buffer at 0x506980000000; level: placement cpu, 546 passes per interval, cursor 1, buffer at 0x506a80000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 8.38e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=tiles,footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=factor,vary=tiling,working-set-mib=8

- first variant B, seed 61; repeats alternated as drawn: yes
- home: placement hbm, 1242 passes per interval, cursor 1, buffer at 0x5d64c0000000; level: placement hbm, 1298 passes per interval, cursor 1, buffer at 0x5d65c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/at=warp,footprint-mib=8,kernel=k6,keys=1048576,placement=cpu,type=factor,vary=strategy

- first variant A, seed 61; repeats alternated as drawn: yes
- home: placement cpu, 3 passes per interval, cursor 0, buffer at 0x570400000000; level: placement cpu, 3 passes per interval, cursor 0, buffer at 0x570480000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

