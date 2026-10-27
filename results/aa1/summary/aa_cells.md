# A/A' cells: two identically prepared direct variants, recomputed from raw rows

Times are per pass in ms. The difference B - A within a repeat is the noise between identically prepared buffers, as median with its 95 % rank interval; its spread over the A/A' cells of a footprint is the floor for translation contrasts there. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | A ms | B ms | B - A ms [interval] | relative to A | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,replicate=1,type=aa | 2.8987 | 2.8896 | -0.0089 [-0.0093, -0.0079] | -0.3 % | 30 | yes | pass |
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,replicate=2,type=aa | 2.9045 | 2.8852 | -0.0191 [-0.0204, -0.0189] | -0.7 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,replicate=3,type=aa | 2.9050 | 2.8965 | -0.0090 [-0.0093, -0.0078] | -0.3 % | 20 | yes | pass |
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,replicate=1,type=aa | 0.2989 | 0.2989 | -0.0000 [-0.0001, 0.0000] | -0.0 % | 100 | no | pass |
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,replicate=2,type=aa | 0.2991 | 0.2975 | -0.0016 [-0.0017, -0.0014] | -0.5 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,replicate=3,type=aa | 0.2987 | 0.2987 | -0.0000 [-0.0000, 0.0000] | -0.0 % | 100 | no | pass |
| f-den=1,f-num=1,footprint-mib=64,kernel=k1,placement=cpu,replicate=1,type=aa | 0.1862 | 0.1845 | -0.0017 [-0.0019, -0.0016] | -0.9 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=64,kernel=k1,placement=cpu,replicate=2,type=aa | 0.1860 | 0.1840 | -0.0021 [-0.0021, -0.0019] | -1.1 % | 10 | yes | pass |
| f-den=1,f-num=1,footprint-mib=64,kernel=k1,placement=cpu,replicate=3,type=aa | 0.1835 | 0.1839 | 0.0003 [0.0003, 0.0003] | +0.2 % | 20 | yes | pass |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,replicate=1,sharing=shared,type=aa | 31.1076 | 31.0055 | -0.0992 [-0.1105, -0.0918] | -0.3 % | 90 | yes | pass |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,replicate=2,sharing=shared,type=aa | 31.0654 | 31.0721 | 0.0054 [-0.0003, 0.0143] | +0.0 % | 100 | no | pass |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,replicate=3,sharing=shared,type=aa | 31.1904 | 31.0182 | -0.1766 [-0.1888, -0.1542] | -0.6 % | 20 | yes | pass |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,replicate=1,sharing=shared,type=aa | 1.2773 | 1.2770 | -0.0005 [-0.0021, 0.0003] | -0.0 % | 100 | no | pass |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,replicate=2,sharing=shared,type=aa | 1.2755 | 1.2748 | -0.0010 [-0.0017, -0.0006] | -0.1 % | 100 | yes | pass |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,replicate=3,sharing=shared,type=aa | 1.2764 | 1.2756 | -0.0008 [-0.0018, 0.0001] | -0.1 % | 100 | no | pass |
| footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,replicate=1,type=aa | 31.0993 | 31.0307 | -0.0719 [-0.0772, -0.0631] | -0.2 % | 90 | yes | pass |
| footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,replicate=2,type=aa | 31.0689 | 30.8822 | -0.1771 [-0.2015, -0.1680] | -0.6 % | 40 | yes | pass |
| footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,replicate=3,type=aa | 31.1497 | 30.9383 | -0.2134 [-0.2223, -0.1859] | -0.7 % | 30 | yes | pass |
| footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,replicate=1,type=aa | 1.2713 | 1.2703 | -0.0010 [-0.0012, -0.0008] | -0.1 % | 100 | yes | pass |
| footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,replicate=2,type=aa | 1.2702 | 1.2696 | -0.0007 [-0.0009, -0.0005] | -0.1 % | 100 | yes | pass |
| footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,replicate=3,type=aa | 1.2707 | 1.2699 | -0.0007 [-0.0011, -0.0003] | -0.1 % | 100 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=1,type=aa,working-set-mib=32 | 1.4983 | 1.4655 | -0.0332 [-0.0340, -0.0320] | -2.2 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=1,type=aa,working-set-mib=8 | 0.0375 | 0.0372 | -0.0002 [-0.0003, -0.0002] | -0.6 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=2,type=aa,working-set-mib=32 | 1.4961 | 1.4958 | -0.0004 [-0.0007, -0.0001] | -0.0 % | 100 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=2,type=aa,working-set-mib=8 | 0.0376 | 0.0375 | -0.0001 [-0.0001, -0.0001] | -0.2 % | 70 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=3,type=aa,working-set-mib=32 | 1.5036 | 1.4851 | -0.0187 [-0.0196, -0.0173] | -1.2 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=3,type=aa,working-set-mib=8 | 0.0376 | 0.0373 | -0.0003 [-0.0003, -0.0002] | -0.8 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=1,type=aa,working-set-mib=32 | 0.0986 | 0.0960 | -0.0026 [-0.0027, -0.0025] | -2.6 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=1,type=aa,working-set-mib=8 | 0.0161 | 0.0161 | 0.0000 [0.0000, 0.0000] | +0.1 % | 100 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=2,type=aa,working-set-mib=32 | 0.0962 | 0.0967 | 0.0005 [0.0005, 0.0006] | +0.6 % | 50 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=2,type=aa,working-set-mib=8 | 0.0161 | 0.0161 | 0.0000 [-0.0000, 0.0000] | +0.0 % | 100 | no | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=3,type=aa,working-set-mib=32 | 0.0975 | 0.0989 | 0.0014 [0.0013, 0.0015] | +1.4 % | 10 | yes | pass |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=3,type=aa,working-set-mib=8 | 0.0161 | 0.0161 | -0.0000 [-0.0000, -0.0000] | -0.1 % | 70 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=cpu,replicate=1,type=aa,update=atomic | 6.0449 | 6.0050 | -0.0383 [-0.0409, -0.0360] | -0.6 % | 40 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=cpu,replicate=2,type=aa,update=atomic | 6.0329 | 6.0100 | -0.0230 [-0.0252, -0.0210] | -0.4 % | 100 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=cpu,replicate=3,type=aa,update=atomic | 6.0426 | 5.9900 | -0.0518 [-0.0543, -0.0458] | -0.9 % | 20 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=hbm,replicate=1,type=aa,update=atomic | 0.8161 | 0.8160 | -0.0001 [-0.0003, 0.0001] | -0.0 % | 100 | no | pass |
| footprint-mib=1024,kernel=k6,placement=hbm,replicate=2,type=aa,update=atomic | 0.8142 | 0.8153 | 0.0011 [0.0008, 0.0015] | +0.1 % | 100 | yes | pass |
| footprint-mib=1024,kernel=k6,placement=hbm,replicate=3,type=aa,update=atomic | 0.8148 | 0.8158 | 0.0010 [0.0008, 0.0013] | +0.1 % | 100 | yes | pass |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,replicate=1,type=aa,update=atomic | 12.7469 | 12.7989 | 0.0544 [0.0100, 0.0939] | +0.4 % | 100 | yes | pass |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,replicate=2,type=aa,update=atomic | 12.5717 | 12.5671 | -0.0069 [-0.0344, 0.0165] | -0.1 % | 100 | no | pass |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,replicate=3,type=aa,update=atomic | 12.7534 | 12.7372 | -0.0596 [-0.0805, -0.0209] | -0.5 % | 100 | yes | pass |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,replicate=1,type=aa,update=atomic | 17.4147 | 17.3354 | -0.1313 [-0.1803, 0.1182] | -0.8 % | 100 | no | pass |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,replicate=2,type=aa,update=atomic | 17.6158 | 17.7109 | 0.2067 [0.1271, 0.2859] | +1.2 % | 100 | yes | pass |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,replicate=3,type=aa,update=atomic | 17.3036 | 17.4592 | 0.2035 [0.1515, 0.2563] | +1.2 % | 100 | yes | pass |
| footprint-mib=512,host=reads,kernel=k5,placement=cpu,replicate=1,sharing=shared,sweeps=8,tiling=tiles,type=aa | 30.8266 | 28.1130 | -2.7157 [-2.7257, -2.6765] | -8.8 % | 10 | yes | pass |
| footprint-mib=512,host=reads,kernel=k5,placement=cpu,replicate=2,sharing=shared,sweeps=8,tiling=tiles,type=aa | 30.8628 | 28.1442 | -2.7052 [-2.7784, -2.6869] | -8.8 % | 10 | yes | pass |
| footprint-mib=512,host=reads,kernel=k5,placement=cpu,replicate=3,sharing=shared,sweeps=8,tiling=tiles,type=aa | 30.8797 | 28.2833 | -2.6053 [-2.6271, -2.5625] | -8.4 % | 10 | yes | pass |
| footprint-mib=512,host=reads,kernel=k5,placement=hbm,replicate=1,sharing=shared,sweeps=8,tiling=tiles,type=aa | 3.2820 | 3.2776 | -0.0044 [-0.0049, -0.0035] | -0.1 % | 100 | yes | pass |
| footprint-mib=512,host=reads,kernel=k5,placement=hbm,replicate=2,sharing=shared,sweeps=8,tiling=tiles,type=aa | 3.2627 | 3.2669 | 0.0040 [0.0027, 0.0047] | +0.1 % | 100 | yes | pass |
| footprint-mib=512,host=reads,kernel=k5,placement=hbm,replicate=3,sharing=shared,sweeps=8,tiling=tiles,type=aa | 3.2645 | 3.2606 | -0.0037 [-0.0043, -0.0026] | -0.1 % | 100 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,replicate=1,sweeps=8,tiling=tiles,type=aa | 30.8338 | 28.0311 | -2.7991 [-2.8256, -2.7637] | -9.1 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,replicate=2,sweeps=8,tiling=tiles,type=aa | 30.9944 | 28.1993 | -2.7876 [-2.8274, -2.7639] | -9.0 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=cpu,replicate=3,sweeps=8,tiling=tiles,type=aa | 30.9038 | 28.2228 | -2.6762 [-2.7088, -2.6316] | -8.7 % | 10 | yes | pass |
| footprint-mib=512,kernel=k5,placement=hbm,replicate=1,sweeps=8,tiling=tiles,type=aa | 3.2536 | 3.2712 | 0.0164 [0.0154, 0.0186] | +0.5 % | 90 | yes | pass |
| footprint-mib=512,kernel=k5,placement=hbm,replicate=2,sweeps=8,tiling=tiles,type=aa | 3.2661 | 3.2641 | -0.0020 [-0.0030, -0.0012] | -0.1 % | 100 | yes | pass |
| footprint-mib=512,kernel=k5,placement=hbm,replicate=3,sweeps=8,tiling=tiles,type=aa | 3.2433 | 3.2516 | 0.0083 [0.0073, 0.0093] | +0.3 % | 100 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1024,placement=cpu,replicate=1,type=aa | 12.5058 | 12.4821 | -0.0225 [-0.0256, -0.0204] | -0.2 % | 100 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1024,placement=cpu,replicate=2,type=aa | 12.5037 | 12.4776 | -0.0263 [-0.0279, -0.0237] | -0.2 % | 70 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1024,placement=cpu,replicate=3,type=aa | 12.4971 | 12.4776 | -0.0193 [-0.0217, -0.0179] | -0.2 % | 90 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1024,placement=hbm,replicate=1,type=aa | 0.7670 | 0.7672 | 0.0003 [0.0002, 0.0003] | +0.0 % | 100 | yes | pass |
| footprint-mib=8,kernel=k6,keys=1024,placement=hbm,replicate=2,type=aa | 0.7657 | 0.7657 | 0.0000 [-0.0000, 0.0001] | +0.0 % | 100 | no | pass |
| footprint-mib=8,kernel=k6,keys=1024,placement=hbm,replicate=3,type=aa | 0.7662 | 0.7662 | 0.0000 [-0.0000, 0.0001] | +0.0 % | 100 | no | pass |

## Per cell

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,replicate=1,type=aa

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x44d8c0000000, B at 0x44d9c0000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 1.074e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,replicate=2,type=aa

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x50c2c0000000, B at 0x50c380000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 1.074e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,replicate=3,type=aa

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x40b8c0000000, B at 0x40b9c0000000
- per repetition: home 1.074e+09 link read bytes and 0 SMMU translation requests; level 1.074e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,replicate=1,type=aa

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x4d2980000000, B at 0x4d2a40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,replicate=2,type=aa

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x5e4700000000, B at 0x5e4840000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,replicate=3,type=aa

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x582300000000, B at 0x5823c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=64,kernel=k1,placement=cpu,replicate=1,type=aa

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x5ebcc0000000, B at 0x5ebd40000000
- per repetition: home 6.711e+07 link read bytes and 0 SMMU translation requests; level 6.711e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=64,kernel=k1,placement=cpu,replicate=2,type=aa

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x43fec0000000, B at 0x43ff40000000
- per repetition: home 6.711e+07 link read bytes and 0 SMMU translation requests; level 6.711e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/f-den=1,f-num=1,footprint-mib=64,kernel=k1,placement=cpu,replicate=3,type=aa

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x5645c0000000, B at 0x564680000000
- per repetition: home 6.711e+07 link read bytes and 0 SMMU translation requests; level 6.711e+07 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,replicate=1,sharing=shared,type=aa

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x559140000000, B at 0x559240000000
- per repetition: home 3.201e+09 link read bytes and 0 SMMU translation requests; level 3.198e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,replicate=2,sharing=shared,type=aa

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x475140000000, B at 0x475280000000
- per repetition: home 3.202e+09 link read bytes and 0 SMMU translation requests; level 3.197e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,replicate=3,sharing=shared,type=aa

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x51de40000000, B at 0x51df40000000
- per repetition: home 3.194e+09 link read bytes and 0 SMMU translation requests; level 3.198e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,replicate=1,sharing=shared,type=aa

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x56dfc0000000, B at 0x56e0c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,replicate=2,sharing=shared,type=aa

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x4eccc0000000, B at 0x4ece00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,replicate=3,sharing=shared,type=aa

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x44f1c0000000, B at 0x44f300000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,replicate=1,type=aa

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x4a8080000000, B at 0x4a8180000000
- per repetition: home 3.196e+09 link read bytes and 0 SMMU translation requests; level 3.195e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,replicate=2,type=aa

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x453600000000, B at 0x4536c0000000
- per repetition: home 3.201e+09 link read bytes and 0 SMMU translation requests; level 3.2e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,replicate=3,type=aa

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x5450c0000000, B at 0x5451c0000000
- per repetition: home 3.196e+09 link read bytes and 0 SMMU translation requests; level 3.199e+09 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,replicate=1,type=aa

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x540540000000, B at 0x540600000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,replicate=2,type=aa

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x43b580000000, B at 0x43b640000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,replicate=3,type=aa

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x4af540000000, B at 0x4af600000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=1,type=aa,working-set-mib=32

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x51e200000000, B at 0x51e300000000
- per repetition: home 5.365e+08 link read bytes and 0 SMMU translation requests; level 5.366e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=1,type=aa,working-set-mib=8

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x55ca40000000, B at 0x55cb40000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 8.382e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=2,type=aa,working-set-mib=32

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x4426c0000000, B at 0x4427c0000000
- per repetition: home 5.365e+08 link read bytes and 0 SMMU translation requests; level 5.365e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=2,type=aa,working-set-mib=8

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x593800000000, B at 0x5938c0000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 8.382e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=3,type=aa,working-set-mib=32

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x52e240000000, B at 0x52e340000000
- per repetition: home 5.365e+08 link read bytes and 0 SMMU translation requests; level 5.365e+08 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=3,type=aa,working-set-mib=8

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x4498c0000000, B at 0x4499c0000000
- per repetition: home 8.382e+06 link read bytes and 0 SMMU translation requests; level 8.382e+06 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=1,type=aa,working-set-mib=32

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x4ef500000000, B at 0x4ef600000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=1,type=aa,working-set-mib=8

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x434e00000000, B at 0x434f00000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=2,type=aa,working-set-mib=32

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x4901c0000000, B at 0x490280000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=2,type=aa,working-set-mib=8

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x5c8040000000, B at 0x5c8140000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=3,type=aa,working-set-mib=32

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x49fbc0000000, B at 0x49fcc0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=3,type=aa,working-set-mib=8

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x4d60c0000000, B at 0x4d61c0000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=cpu,replicate=1,type=aa,update=atomic

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x4be540000000, B at 0x4be640000000
- per repetition: home 0 link read bytes and 4200 SMMU translation requests; level 0 link read bytes and 4211 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=cpu,replicate=2,type=aa,update=atomic

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x5e3500000000, B at 0x5e3600000000
- per repetition: home 0 link read bytes and 4230 SMMU translation requests; level 0 link read bytes and 4189 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=cpu,replicate=3,type=aa,update=atomic

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x53f440000000, B at 0x53f540000000
- per repetition: home 0 link read bytes and 4217 SMMU translation requests; level 0 link read bytes and 4215 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=hbm,replicate=1,type=aa,update=atomic

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x422700000000, B at 0x422840000000
- per repetition: home 0 link read bytes and 1323 SMMU translation requests; level 0 link read bytes and 1263 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=hbm,replicate=2,type=aa,update=atomic

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x4cd980000000, B at 0x4cda80000000
- per repetition: home 0 link read bytes and 1334 SMMU translation requests; level 0 link read bytes and 1286 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=1024,kernel=k6,placement=hbm,replicate=3,type=aa,update=atomic

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x558400000000, B at 0x558500000000
- per repetition: home 0 link read bytes and 1271 SMMU translation requests; level 0 link read bytes and 1331 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,replicate=1,type=aa,update=atomic

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x584600000000, B at 0x5846c0000000
- no hardware counters in this cell

### route/footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,replicate=2,type=aa,update=atomic

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x40f400000000, B at 0x40f4c0000000
- no hardware counters in this cell

### route/footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,replicate=3,type=aa,update=atomic

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x443d40000000, B at 0x443dc0000000
- no hardware counters in this cell

### route/footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,replicate=1,type=aa,update=atomic

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x4ddc80000000, B at 0x4ddd40000000
- no hardware counters in this cell

### route/footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,replicate=2,type=aa,update=atomic

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x5bb0c0000000, B at 0x5bb180000000
- no hardware counters in this cell

### route/footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,replicate=3,type=aa,update=atomic

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x58bc80000000, B at 0x58bd40000000
- no hardware counters in this cell

### route/footprint-mib=512,host=reads,kernel=k5,placement=cpu,replicate=1,sharing=shared,sweeps=8,tiling=tiles,type=aa

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x4b1540000000, B at 0x4b1640000000
- per repetition: home 6.422e+09 link read bytes and 3.606e+04 SMMU translation requests; level 6.422e+09 link read bytes and 3.63e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=512,host=reads,kernel=k5,placement=cpu,replicate=2,sharing=shared,sweeps=8,tiling=tiles,type=aa

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x5a5e00000000, B at 0x5a5f40000000
- per repetition: home 6.422e+09 link read bytes and 3.611e+04 SMMU translation requests; level 6.422e+09 link read bytes and 3.631e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=512,host=reads,kernel=k5,placement=cpu,replicate=3,sharing=shared,sweeps=8,tiling=tiles,type=aa

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x57eb80000000, B at 0x57ecc0000000
- per repetition: home 6.422e+09 link read bytes and 3.604e+04 SMMU translation requests; level 6.422e+09 link read bytes and 3.61e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=512,host=reads,kernel=k5,placement=hbm,replicate=1,sharing=shared,sweeps=8,tiling=tiles,type=aa

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x538680000000, B at 0x538740000000
- per repetition: home 0 link read bytes and 5484 SMMU translation requests; level 0 link read bytes and 5488 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=512,host=reads,kernel=k5,placement=hbm,replicate=2,sharing=shared,sweeps=8,tiling=tiles,type=aa

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x491700000000, B at 0x491800000000
- per repetition: home 0 link read bytes and 5472 SMMU translation requests; level 0 link read bytes and 5490 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=512,host=reads,kernel=k5,placement=hbm,replicate=3,sharing=shared,sweeps=8,tiling=tiles,type=aa

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x42a900000000, B at 0x42aa40000000
- per repetition: home 0 link read bytes and 5955 SMMU translation requests; level 0 link read bytes and 5978 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,replicate=1,sweeps=8,tiling=tiles,type=aa

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x4458c0000000, B at 0x445a00000000
- per repetition: home 6.422e+09 link read bytes and 3.592e+04 SMMU translation requests; level 6.422e+09 link read bytes and 3.621e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,replicate=2,sweeps=8,tiling=tiles,type=aa

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x5f7100000000, B at 0x5f7200000000
- per repetition: home 6.422e+09 link read bytes and 3.596e+04 SMMU translation requests; level 6.422e+09 link read bytes and 3.625e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=cpu,replicate=3,sweeps=8,tiling=tiles,type=aa

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x58df40000000, B at 0x58e040000000
- per repetition: home 6.422e+09 link read bytes and 3.611e+04 SMMU translation requests; level 6.422e+09 link read bytes and 3.608e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=hbm,replicate=1,sweeps=8,tiling=tiles,type=aa

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x498880000000, B at 0x498980000000
- per repetition: home 0 link read bytes and 5963 SMMU translation requests; level 0 link read bytes and 5498 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=hbm,replicate=2,sweeps=8,tiling=tiles,type=aa

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x53f140000000, B at 0x53f240000000
- per repetition: home 0 link read bytes and 5523 SMMU translation requests; level 0 link read bytes and 5985 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=512,kernel=k5,placement=hbm,replicate=3,sweeps=8,tiling=tiles,type=aa

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x5f48c0000000, B at 0x5f49c0000000
- per repetition: home 0 link read bytes and 5956 SMMU translation requests; level 0 link read bytes and 5985 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1024,placement=cpu,replicate=1,type=aa

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x40a280000000, B at 0x40a300000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1024,placement=cpu,replicate=2,type=aa

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x540b80000000, B at 0x540c40000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1024,placement=cpu,replicate=3,type=aa

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x491300000000, B at 0x491380000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1024,placement=hbm,replicate=1,type=aa

- first variant B, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x48e480000000, B at 0x48e500000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1024,placement=hbm,replicate=2,type=aa

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x5394c0000000, B at 0x539540000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8,kernel=k6,keys=1024,placement=hbm,replicate=3,type=aa

- first variant A, seed 109; repeats alternated as drawn: yes
- buffers: A at 0x50b580000000, B at 0x50b640000000
- per repetition: home 0 link read bytes and 0 SMMU translation requests; level 0 link read bytes and 0 SMMU translation requests; multiplexed rows voided: 0

