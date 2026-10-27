# A/A' cells: two identically prepared direct variants, recomputed from raw rows

Times are per pass in ms. The difference B - A within a repeat is the noise between identically prepared buffers, as median with its 95 % rank interval; its spread over the A/A' cells of a footprint is the floor for translation contrasts there. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | A ms | B ms | B - A ms [interval] | relative to A | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,replicate=1,type=aa | 2.9168 | 2.8880 | -0.0287 [-0.0293, -0.0280] | -1.0 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,replicate=2,type=aa | 2.9128 | 2.8899 | -0.0226 [-0.0238, -0.0207] | -0.8 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,replicate=3,type=aa | 2.9057 | 2.8847 | -0.0209 [-0.0215, -0.0186] | -0.7 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,replicate=1,type=aa | 0.2974 | 0.2967 | -0.0007 [-0.0007, -0.0006] | -0.2 % | 20 | yes | pass |
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,replicate=2,type=aa | 0.2984 | 0.2994 | 0.0009 [0.0009, 0.0010] | +0.3 % | 20 | yes | pass |
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,replicate=3,type=aa | 0.2978 | 0.2989 | 0.0012 [0.0011, 0.0013] | +0.4 % | 30 | yes | pass |
| f-den=1,f-num=1,footprint-mib=64,kernel=k1,placement=cpu,replicate=1,type=aa | 0.1851 | 0.1841 | -0.0010 [-0.0010, -0.0009] | -0.5 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=64,kernel=k1,placement=cpu,replicate=2,type=aa | 0.1830 | 0.1808 | -0.0022 [-0.0022, -0.0021] | -1.2 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=64,kernel=k1,placement=cpu,replicate=3,type=aa | 0.1855 | 0.1860 | 0.0004 [0.0004, 0.0005] | +0.2 % | 20 | yes | pass |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,replicate=1,sharing=shared,type=aa | 31.0980 | 31.0516 | -0.0439 [-0.0523, -0.0362] | -0.1 % | 100 | yes | pass |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,replicate=2,sharing=shared,type=aa | 31.0313 | 31.0464 | 0.0138 [0.0107, 0.0230] | +0.0 % | 100 | yes | pass |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,replicate=3,sharing=shared,type=aa | 31.1160 | 30.9063 | -0.2118 [-0.2192, -0.1925] | -0.7 % | 30 | yes | pass |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,replicate=1,sharing=shared,type=aa | 1.2779 | 1.2770 | -0.0011 [-0.0019, 0.0003] | -0.1 % | 100 | no | pass |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,replicate=2,sharing=shared,type=aa | 1.2751 | 1.2746 | -0.0004 [-0.0009, 0.0000] | -0.0 % | 100 | no | pass |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,replicate=3,sharing=shared,type=aa | 1.2754 | 1.2745 | -0.0012 [-0.0017, -0.0007] | -0.1 % | 100 | yes | pass |
| footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,replicate=1,type=aa | 31.1582 | 31.0169 | -0.1361 [-0.1524, -0.1280] | -0.4 % | 30 | yes | pass |
| footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,replicate=2,type=aa | 31.0505 | 30.9924 | -0.0576 [-0.0639, -0.0521] | -0.2 % | 100 | yes | pass |
| footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,replicate=3,type=aa | 31.0678 | 30.9833 | -0.0833 [-0.0901, -0.0735] | -0.3 % | 80 | yes | pass |
| footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,replicate=1,type=aa | 1.2701 | 1.2699 | -0.0001 [-0.0003, 0.0002] | -0.0 % | 100 | no | pass |
| footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,replicate=2,type=aa | 1.2700 | 1.2695 | -0.0006 [-0.0009, -0.0003] | -0.0 % | 100 | yes | pass |
| footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,replicate=3,type=aa | 1.2703 | 1.2697 | -0.0008 [-0.0011, -0.0006] | -0.1 % | 100 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=1,type=aa,working-set-mib=32 | 1.4933 | 1.4941 | 0.0008 [0.0005, 0.0012] | +0.1 % | 100 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=1,type=aa,working-set-mib=8 | 0.0375 | 0.0372 | -0.0003 [-0.0003, -0.0002] | -0.7 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=2,type=aa,working-set-mib=32 | 1.5031 | 1.4944 | -0.0087 [-0.0091, -0.0081] | -0.6 % | 20 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=2,type=aa,working-set-mib=8 | 0.0377 | 0.0373 | -0.0004 [-0.0004, -0.0003] | -1.0 % | 20 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=3,type=aa,working-set-mib=32 | 1.4808 | 1.4936 | 0.0126 [0.0121, 0.0135] | +0.9 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=3,type=aa,working-set-mib=8 | 0.0377 | 0.0373 | -0.0004 [-0.0004, -0.0003] | -1.0 % | 20 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=1,type=aa,working-set-mib=32 | 0.0969 | 0.0978 | 0.0009 [0.0008, 0.0010] | +0.9 % | 30 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=1,type=aa,working-set-mib=8 | 0.0160 | 0.0160 | 0.0000 [0.0000, 0.0000] | +0.1 % | 100 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=2,type=aa,working-set-mib=32 | 0.0962 | 0.0990 | 0.0029 [0.0028, 0.0031] | +3.0 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=2,type=aa,working-set-mib=8 | 0.0161 | 0.0161 | -0.0000 [-0.0000, 0.0000] | -0.0 % | 100 | no | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=3,type=aa,working-set-mib=32 | 0.0975 | 0.0972 | -0.0004 [-0.0004, -0.0003] | -0.4 % | 100 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=3,type=aa,working-set-mib=8 | 0.0162 | 0.0161 | -0.0000 [-0.0000, -0.0000] | -0.1 % | 100 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=cpu,replicate=1,type=aa,update=atomic | 6.0350 | 6.0114 | -0.0224 [-0.0245, -0.0205] | -0.4 % | 40 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=cpu,replicate=2,type=aa,update=atomic | 6.0423 | 5.9996 | -0.0446 [-0.0456, -0.0393] | -0.7 % | 20 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=cpu,replicate=3,type=aa,update=atomic | 6.0404 | 6.0117 | -0.0297 [-0.0324, -0.0263] | -0.5 % | 100 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=hbm,replicate=1,type=aa,update=atomic | 0.8157 | 0.8158 | 0.0002 [-0.0001, 0.0005] | +0.0 % | 100 | no | pass |
| footprint-mib=1024,kernel=k6,placement=hbm,replicate=2,type=aa,update=atomic | 0.8166 | 0.8153 | -0.0011 [-0.0017, -0.0008] | -0.1 % | 100 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=hbm,replicate=3,type=aa,update=atomic | 0.8152 | 0.8161 | 0.0010 [0.0007, 0.0013] | +0.1 % | 100 | yes | pass |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,replicate=1,type=aa,update=atomic | 12.6291 | 12.6457 | 0.0366 [0.0103, 0.0775] | +0.3 % | 100 | yes | pass |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,replicate=2,type=aa,update=atomic | 12.6680 | 12.7163 | 0.0275 [0.0134, 0.0741] | +0.2 % | 100 | yes | pass |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,replicate=3,type=aa,update=atomic | 12.5714 | 12.5817 | 0.0144 [-0.0026, 0.0407] | +0.1 % | 100 | no | pass |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,replicate=1,type=aa,update=atomic | 17.2227 | 17.4944 | 0.2719 [0.2137, 0.3110] | +1.6 % | 100 | yes | pass |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,replicate=2,type=aa,update=atomic | 17.3631 | 17.3626 | 0.0487 [-0.1868, 0.1998] | +0.3 % | 100 | no | pass |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,replicate=3,type=aa,update=atomic | 17.4498 | 17.3419 | -0.1428 [-0.2252, 0.1201] | -0.8 % | 100 | no | pass |
| footprint-mib=512,host=reads,kernel=k5,placement=cpu,replicate=1,sharing=shared,sweeps=8,tiling=tiles,type=aa | 30.7528 | 28.1165 | -2.6357 [-2.6819, -2.5884] | -8.6 % | 10 | yes | pass |
| footprint-mib=512,host=reads,kernel=k5,placement=cpu,replicate=2,sharing=shared,sweeps=8,tiling=tiles,type=aa | 30.9355 | 28.1624 | -2.7620 [-2.8135, -2.7425] | -8.9 % | 10 | yes | pass |
| footprint-mib=512,host=reads,kernel=k5,placement=cpu,replicate=3,sharing=shared,sweeps=8,tiling=tiles,type=aa | 30.8322 | 28.2334 | -2.5894 [-2.6247, -2.5578] | -8.4 % | 10 | yes | pass |
| footprint-mib=512,host=reads,kernel=k5,placement=hbm,replicate=1,sharing=shared,sweeps=8,tiling=tiles,type=aa | 3.2599 | 3.2496 | -0.0102 [-0.0121, -0.0087] | -0.3 % | 100 | yes | pass |
| footprint-mib=512,host=reads,kernel=k5,placement=hbm,replicate=2,sharing=shared,sweeps=8,tiling=tiles,type=aa | 3.2695 | 3.2845 | 0.0162 [0.0147, 0.0177] | +0.5 % | 50 | yes | pass |
| footprint-mib=512,host=reads,kernel=k5,placement=hbm,replicate=3,sharing=shared,sweeps=8,tiling=tiles,type=aa | 3.2432 | 3.2556 | 0.0127 [0.0115, 0.0133] | +0.4 % | 90 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,replicate=1,sweeps=8,tiling=tiles,type=aa | 30.7406 | 28.0526 | -2.6968 [-2.7237, -2.6458] | -8.8 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,replicate=2,sweeps=8,tiling=tiles,type=aa | 30.6107 | 27.9908 | -2.6368 [-2.6675, -2.5603] | -8.6 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,replicate=3,sweeps=8,tiling=tiles,type=aa | 30.9201 | 28.0281 | -2.8868 [-2.9217, -2.8550] | -9.3 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=hbm,replicate=1,sweeps=8,tiling=tiles,type=aa | 3.2634 | 3.2595 | -0.0033 [-0.0049, -0.0015] | -0.1 % | 100 | yes | pass |
| footprint-mib=512,kernel=k5,placement=hbm,replicate=2,sweeps=8,tiling=tiles,type=aa | 3.2412 | 3.2749 | 0.0349 [0.0325, 0.0378] | +1.1 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=hbm,replicate=3,sweeps=8,tiling=tiles,type=aa | 3.2654 | 3.2532 | -0.0120 [-0.0137, -0.0107] | -0.4 % | 100 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1024,placement=cpu,replicate=1,type=aa | 12.4807 | 12.4791 | -0.0012 [-0.0025, 0.0006] | -0.0 % | 100 | no | pass |
| footprint-mib=8,kernel=k6,keys=1024,placement=cpu,replicate=2,type=aa | 12.4820 | 12.4893 | 0.0080 [0.0068, 0.0095] | +0.1 % | 100 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1024,placement=cpu,replicate=3,type=aa | 12.4742 | 12.4899 | 0.0149 [0.0126, 0.0156] | +0.1 % | 80 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1024,placement=hbm,replicate=1,type=aa | 0.7663 | 0.7664 | 0.0002 [0.0001, 0.0002] | +0.0 % | 100 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1024,placement=hbm,replicate=2,type=aa | 0.7669 | 0.7667 | -0.0002 [-0.0002, -0.0002] | -0.0 % | 100 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1024,placement=hbm,replicate=3,type=aa | 0.7672 | 0.7670 | -0.0002 [-0.0003, -0.0002] | -0.0 % | 100 | yes | pass |

## Per cell

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,replicate=1,type=aa

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x50aac0000000, B at 0x50abc0000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 1.074e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,replicate=2,type=aa

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x4dbb80000000, B at 0x4dbc80000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 1.074e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,replicate=3,type=aa

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x545300000000, B at 0x545400000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 1.074e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,replicate=1,type=aa

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x40b400000000, B at 0x40b500000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,replicate=2,type=aa

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x528600000000, B at 0x528700000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,replicate=3,type=aa

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x4751c0000000, B at 0x4752c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=64,kernel=k1,placement=cpu,replicate=1,type=aa

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x4bccc0000000, B at 0x4bcd40000000
- per repetition: home 6.711e+07 link read bytes and 0 SMMU translation requests; level 6.711e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=64,kernel=k1,placement=cpu,replicate=2,type=aa

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x48ae40000000, B at 0x48af00000000
- per repetition: home 6.711e+07 link read bytes and 0 SMMU translation requests; level 6.711e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=64,kernel=k1,placement=cpu,replicate=3,type=aa

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x4d1040000000, B at 0x4d10c0000000
- per repetition: home 6.711e+07 link read bytes and 0 SMMU translation requests; level 6.711e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,replicate=1,sharing=shared,type=aa

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x5c43c0000000, B at 0x5c4480000000
- per repetition: home 3.196e+09 link read bytes and 0 SMMU translation requests; level 3.198e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,replicate=2,sharing=shared,type=aa

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x480e00000000, B at 0x480f00000000
- per repetition: home 3.203e+09 link read bytes and 0 SMMU translation requests; level 3.194e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,replicate=3,sharing=shared,type=aa

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x5f7540000000, B at 0x5f7680000000
- per repetition: home 3.195e+09 link read bytes and 0 SMMU translation requests; level 3.2e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,replicate=1,sharing=shared,type=aa

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x49d2c0000000, B at 0x49d3c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,replicate=2,sharing=shared,type=aa

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x4057c0000000, B at 0x4058c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,replicate=3,sharing=shared,type=aa

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x582240000000, B at 0x582340000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,replicate=1,type=aa

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x4639c0000000, B at 0x463b00000000
- per repetition: home 3.196e+09 link read bytes and 0 SMMU translation requests; level 3.194e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,replicate=2,type=aa

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x5331c0000000, B at 0x533280000000
- per repetition: home 3.2e+09 link read bytes and 0 SMMU translation requests; level 3.199e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,replicate=3,type=aa

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x4f1440000000, B at 0x4f1540000000
- per repetition: home 3.201e+09 link read bytes and 0 SMMU translation requests; level 3.199e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,replicate=1,type=aa

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x529b40000000, B at 0x529c80000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,replicate=2,type=aa

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x530080000000, B at 0x530180000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,replicate=3,type=aa

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x5a4e00000000, B at 0x5a4f40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=1,type=aa,working-set-mib=32

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x49ca80000000, B at 0x49cb40000000
- per repetition: home 5.365e+08 link read bytes and 0 SMMU translation requests; level 5.365e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=1,type=aa,working-set-mib=8

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x4a0600000000, B at 0x4a0700000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 8.382e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=2,type=aa,working-set-mib=32

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x49c140000000, B at 0x49c200000000
- per repetition: home 5.365e+08 link read bytes and 0 SMMU translation requests; level 5.365e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=2,type=aa,working-set-mib=8

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x4bb440000000, B at 0x4bb500000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 8.382e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=3,type=aa,working-set-mib=32

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x555980000000, B at 0x555a80000000
- per repetition: home 5.366e+08 link read bytes and 0 SMMU translation requests; level 5.365e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=3,type=aa,working-set-mib=8

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x5fbd00000000, B at 0x5fbdc0000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 8.382e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=1,type=aa,working-set-mib=32

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x50c740000000, B at 0x50c840000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=1,type=aa,working-set-mib=8

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x524a00000000, B at 0x524ac0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=2,type=aa,working-set-mib=32

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x441480000000, B at 0x441540000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=2,type=aa,working-set-mib=8

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x4daa80000000, B at 0x4dab40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=3,type=aa,working-set-mib=32

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x50a7c0000000, B at 0x50a8c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=3,type=aa,working-set-mib=8

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x5a4a80000000, B at 0x5a4b80000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=cpu,replicate=1,type=aa,update=atomic

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x4d8c40000000, B at 0x4d8d40000000
- per repetition: home 0 link read bytes and 4215 SMMU translation requests; level 0 link read bytes and 4206 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=cpu,replicate=2,type=aa,update=atomic

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x41ab00000000, B at 0x41abc0000000
- per repetition: home 0 link read bytes and 4187 SMMU translation requests; level 0 link read bytes and 4193 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=cpu,replicate=3,type=aa,update=atomic

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x5f2cc0000000, B at 0x5f2dc0000000
- per repetition: home 0 link read bytes and 4188 SMMU translation requests; level 0 link read bytes and 4227 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=hbm,replicate=1,type=aa,update=atomic

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x45c8c0000000, B at 0x45c9c0000000
- per repetition: home 0 link read bytes and 1257 SMMU translation requests; level 0 link read bytes and 1322 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=hbm,replicate=2,type=aa,update=atomic

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x474580000000, B at 0x474680000000
- per repetition: home 0 link read bytes and 1337 SMMU translation requests; level 0 link read bytes and 1240 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=hbm,replicate=3,type=aa,update=atomic

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x4c5100000000, B at 0x4c5200000000
- per repetition: home 0 link read bytes and 1324 SMMU translation requests; level 0 link read bytes and 1252 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,replicate=1,type=aa,update=atomic

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x4d7dc0000000, B at 0x4d7e80000000
- no hardware counters in this cell

### route/footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,replicate=2,type=aa,update=atomic

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x53ea00000000, B at 0x53eac0000000
- no hardware counters in this cell

### route/footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,replicate=3,type=aa,update=atomic

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x440080000000, B at 0x440140000000
- no hardware counters in this cell

### route/footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,replicate=1,type=aa,update=atomic

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x4d3a80000000, B at 0x4d3b80000000
- no hardware counters in this cell

### route/footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,replicate=2,type=aa,update=atomic

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x420680000000, B at 0x420740000000
- no hardware counters in this cell

### route/footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,replicate=3,type=aa,update=atomic

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x507600000000, B at 0x5076c0000000
- no hardware counters in this cell

### route/footprint-mib=512,host=reads,kernel=k5,placement=cpu,replicate=1,sharing=shared,sweeps=8,tiling=tiles,type=aa

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x581e80000000, B at 0x581fc0000000
- per repetition: home 6.422e+09 link read bytes and 3.622e+04 SMMU translation requests; level 6.422e+09 link read bytes and 3.628e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=512,host=reads,kernel=k5,placement=cpu,replicate=2,sharing=shared,sweeps=8,tiling=tiles,type=aa

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x587d80000000, B at 0x587ec0000000
- per repetition: home 6.422e+09 link read bytes and 3.614e+04 SMMU translation requests; level 6.422e+09 link read bytes and 3.623e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=512,host=reads,kernel=k5,placement=cpu,replicate=3,sharing=shared,sweeps=8,tiling=tiles,type=aa

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x441cc0000000, B at 0x441e40000000
- per repetition: home 6.422e+09 link read bytes and 3.601e+04 SMMU translation requests; level 6.422e+09 link read bytes and 3.629e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=512,host=reads,kernel=k5,placement=hbm,replicate=1,sharing=shared,sweeps=8,tiling=tiles,type=aa

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x4549c0000000, B at 0x454ac0000000
- per repetition: home 0 link read bytes and 5483 SMMU translation requests; level 0 link read bytes and 5980 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=512,host=reads,kernel=k5,placement=hbm,replicate=2,sharing=shared,sweeps=8,tiling=tiles,type=aa

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x4b1f00000000, B at 0x4b2040000000
- per repetition: home 0 link read bytes and 5943 SMMU translation requests; level 0 link read bytes and 5471 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=512,host=reads,kernel=k5,placement=hbm,replicate=3,sharing=shared,sweeps=8,tiling=tiles,type=aa

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x5b48c0000000, B at 0x5b49c0000000
- per repetition: home 0 link read bytes and 6009 SMMU translation requests; level 0 link read bytes and 5988 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,replicate=1,sweeps=8,tiling=tiles,type=aa

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x4ddd00000000, B at 0x4dde00000000
- per repetition: home 6.422e+09 link read bytes and 3.595e+04 SMMU translation requests; level 6.422e+09 link read bytes and 3.622e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,replicate=2,sweeps=8,tiling=tiles,type=aa

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x5b2f40000000, B at 0x5b3040000000
- per repetition: home 6.422e+09 link read bytes and 3.605e+04 SMMU translation requests; level 6.422e+09 link read bytes and 3.614e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,replicate=3,sweeps=8,tiling=tiles,type=aa

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x489540000000, B at 0x489640000000
- per repetition: home 6.422e+09 link read bytes and 3.598e+04 SMMU translation requests; level 6.422e+09 link read bytes and 3.637e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=hbm,replicate=1,sweeps=8,tiling=tiles,type=aa

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x412500000000, B at 0x412600000000
- per repetition: home 0 link read bytes and 5493 SMMU translation requests; level 0 link read bytes and 5508 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=hbm,replicate=2,sweeps=8,tiling=tiles,type=aa

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x4f0700000000, B at 0x4f0800000000
- per repetition: home 0 link read bytes and 5506 SMMU translation requests; level 0 link read bytes and 5522 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=hbm,replicate=3,sweeps=8,tiling=tiles,type=aa

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x53c780000000, B at 0x53c880000000
- per repetition: home 0 link read bytes and 5528 SMMU translation requests; level 0 link read bytes and 5508 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1024,placement=cpu,replicate=1,type=aa

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x453980000000, B at 0x453a00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1024,placement=cpu,replicate=2,type=aa

- first variant B, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x526e00000000, B at 0x526ec0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1024,placement=cpu,replicate=3,type=aa

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x5eccc0000000, B at 0x5ecd80000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1024,placement=hbm,replicate=1,type=aa

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x47d180000000, B at 0x47d240000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1024,placement=hbm,replicate=2,type=aa

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x4464c0000000, B at 0x446580000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1024,placement=hbm,replicate=3,type=aa

- first variant A, seed 113; repeats alternated as drawn: yes
- buffers: A at 0x564ac0000000, B at 0x564b80000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

