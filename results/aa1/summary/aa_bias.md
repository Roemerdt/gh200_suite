# A/A' cells: what the allocation order alone does to a contrast

B - A between two identically prepared direct variants, B allocated after A as the level variant of a factor cell is allocated after its control. Per setting over all its cells (processes and campaigns): the median of B - A relative to A, its range, and the cells whose interval excludes zero with B faster or slower.

| setting | cells | median B - A | range | B faster | B slower |
|---|---|---|---|---|---|
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,type=aa | 6 | -0.7 % | -1.0 % to -0.3 % | 6 | 0 |
| f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,type=aa | 6 | -0.0 % | -0.5 % to +0.4 % | 2 | 2 |
| f-den=1,f-num=1,footprint-mib=64,kernel=k1,placement=cpu,type=aa | 6 | -0.7 % | -1.2 % to +0.2 % | 4 | 2 |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,sharing=shared,type=aa | 6 | -0.2 % | -0.7 % to +0.0 % | 4 | 1 |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,sharing=shared,type=aa | 6 | -0.1 % | -0.1 % to -0.0 % | 2 | 0 |
| footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,type=aa | 6 | -0.4 % | -0.7 % to -0.2 % | 6 | 0 |
| footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,type=aa | 6 | -0.1 % | -0.1 % to -0.0 % | 5 | 0 |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=aa,working-set-mib=32 | 6 | -0.3 % | -2.2 % to +0.9 % | 4 | 2 |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,type=aa,working-set-mib=8 | 6 | -0.7 % | -1.0 % to -0.2 % | 6 | 0 |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=aa,working-set-mib=32 | 6 | +0.8 % | -2.6 % to +3.0 % | 2 | 4 |
| footprint-mib=1024,k=16,kernel=k2,placement=hbm,type=aa,working-set-mib=8 | 6 | -0.0 % | -0.1 % to +0.1 % | 2 | 2 |
| footprint-mib=1024,kernel=k6,placement=cpu,type=aa,update=atomic | 6 | -0.6 % | -0.9 % to -0.4 % | 6 | 0 |
| footprint-mib=1024,kernel=k6,placement=hbm,type=aa,update=atomic | 6 | +0.1 % | -0.1 % to +0.1 % | 1 | 3 |
| footprint-mib=16384,kernel=k3,placement=cpu,type=aa | 20 | +0.0 % | -0.0 % to +0.0 % | 0 | 6 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=atomic | 6 | +0.2 % | -0.5 % to +0.4 % | 1 | 3 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=atomic | 6 | +0.7 % | -0.8 % to +1.6 % | 0 | 3 |
| footprint-mib=512,host=reads,kernel=k5,placement=cpu,sharing=shared,sweeps=8,tiling=tiles,type=aa | 6 | -8.7 % | -8.9 % to -8.4 % | 6 | 0 |
| footprint-mib=512,host=reads,kernel=k5,placement=hbm,sharing=shared,sweeps=8,tiling=tiles,type=aa | 6 | +0.0 % | -0.3 % to +0.5 % | 3 | 3 |
| footprint-mib=512,kernel=k5,placement=cpu,sweeps=8,tiling=tiles,type=aa | 6 | -8.9 % | -9.3 % to -8.6 % | 6 | 0 |
| footprint-mib=512,kernel=k5,placement=hbm,sweeps=8,tiling=tiles,type=aa | 6 | +0.1 % | -0.4 % to +1.1 % | 3 | 3 |
| footprint-mib=8,kernel=k6,keys=1024,placement=cpu,type=aa | 6 | -0.1 % | -0.2 % to +0.1 % | 3 | 2 |
| footprint-mib=8,kernel=k6,keys=1024,placement=hbm,type=aa | 6 | +0.0 % | -0.0 % to +0.0 % | 2 | 2 |
| footprint-mib=8192,kernel=k3,placement=cpu,type=aa | 20 | -0.5 % | -0.9 % to -0.3 % | 20 | 0 |

## Per cell

| campaign | cell | A ms | B ms | B - A ms [interval] | relative | pairs | first |
|---|---|---|---|---|---|---|---|
| aa1 | f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,replicate=1,type=aa | 2.8987 | 2.8896 | -0.0089 [-0.0093, -0.0079] | -0.3 % | 30 | A |
| aa1 | f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,replicate=2,type=aa | 2.9045 | 2.8852 | -0.0191 [-0.0204, -0.0189] | -0.7 % | 10 | B |
| aa1 | f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,replicate=3,type=aa | 2.9050 | 2.8965 | -0.0090 [-0.0093, -0.0078] | -0.3 % | 20 | A |
| aa1 | f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,replicate=1,type=aa | 0.2989 | 0.2989 | -0.0000 [-0.0001, 0.0000] | -0.0 % | 100 | B |
| aa1 | f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,replicate=2,type=aa | 0.2991 | 0.2975 | -0.0016 [-0.0017, -0.0014] | -0.5 % | 10 | A |
| aa1 | f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,replicate=3,type=aa | 0.2987 | 0.2987 | -0.0000 [-0.0000, 0.0000] | -0.0 % | 100 | A |
| aa1 | f-den=1,f-num=1,footprint-mib=64,kernel=k1,placement=cpu,replicate=1,type=aa | 0.1862 | 0.1845 | -0.0017 [-0.0019, -0.0016] | -0.9 % | 10 | B |
| aa1 | f-den=1,f-num=1,footprint-mib=64,kernel=k1,placement=cpu,replicate=2,type=aa | 0.1860 | 0.1840 | -0.0021 [-0.0021, -0.0019] | -1.1 % | 10 | A |
| aa1 | f-den=1,f-num=1,footprint-mib=64,kernel=k1,placement=cpu,replicate=3,type=aa | 0.1835 | 0.1839 | 0.0003 [0.0003, 0.0003] | +0.2 % | 20 | B |
| aa1 | footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,replicate=1,sharing=shared,type=aa | 31.1076 | 31.0055 | -0.0992 [-0.1105, -0.0918] | -0.3 % | 90 | B |
| aa1 | footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,replicate=2,sharing=shared,type=aa | 31.0654 | 31.0721 | 0.0054 [-0.0003, 0.0143] | +0.0 % | 100 | A |
| aa1 | footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,replicate=3,sharing=shared,type=aa | 31.1904 | 31.0182 | -0.1766 [-0.1888, -0.1542] | -0.6 % | 20 | A |
| aa1 | footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,replicate=1,sharing=shared,type=aa | 1.2773 | 1.2770 | -0.0005 [-0.0021, 0.0003] | -0.0 % | 100 | B |
| aa1 | footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,replicate=2,sharing=shared,type=aa | 1.2755 | 1.2748 | -0.0010 [-0.0017, -0.0006] | -0.1 % | 100 | A |
| aa1 | footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,replicate=3,sharing=shared,type=aa | 1.2764 | 1.2756 | -0.0008 [-0.0018, 0.0001] | -0.1 % | 100 | A |
| aa1 | footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,replicate=1,type=aa | 31.0993 | 31.0307 | -0.0719 [-0.0772, -0.0631] | -0.2 % | 90 | A |
| aa1 | footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,replicate=2,type=aa | 31.0689 | 30.8822 | -0.1771 [-0.2015, -0.1680] | -0.6 % | 40 | A |
| aa1 | footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,replicate=3,type=aa | 31.1497 | 30.9383 | -0.2134 [-0.2223, -0.1859] | -0.7 % | 30 | A |
| aa1 | footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,replicate=1,type=aa | 1.2713 | 1.2703 | -0.0010 [-0.0012, -0.0008] | -0.1 % | 100 | A |
| aa1 | footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,replicate=2,type=aa | 1.2702 | 1.2696 | -0.0007 [-0.0009, -0.0005] | -0.1 % | 100 | A |
| aa1 | footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,replicate=3,type=aa | 1.2707 | 1.2699 | -0.0007 [-0.0011, -0.0003] | -0.1 % | 100 | B |
| aa1 | footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=1,type=aa,working-set-mib=32 | 1.4983 | 1.4655 | -0.0332 [-0.0340, -0.0320] | -2.2 % | 10 | A |
| aa1 | footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=1,type=aa,working-set-mib=8 | 0.0375 | 0.0372 | -0.0002 [-0.0003, -0.0002] | -0.6 % | 10 | B |
| aa1 | footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=2,type=aa,working-set-mib=32 | 1.4961 | 1.4958 | -0.0004 [-0.0007, -0.0001] | -0.0 % | 100 | A |
| aa1 | footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=2,type=aa,working-set-mib=8 | 0.0376 | 0.0375 | -0.0001 [-0.0001, -0.0001] | -0.2 % | 70 | B |
| aa1 | footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=3,type=aa,working-set-mib=32 | 1.5036 | 1.4851 | -0.0187 [-0.0196, -0.0173] | -1.2 % | 10 | A |
| aa1 | footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=3,type=aa,working-set-mib=8 | 0.0376 | 0.0373 | -0.0003 [-0.0003, -0.0002] | -0.8 % | 10 | B |
| aa1 | footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=1,type=aa,working-set-mib=32 | 0.0986 | 0.0960 | -0.0026 [-0.0027, -0.0025] | -2.6 % | 10 | A |
| aa1 | footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=1,type=aa,working-set-mib=8 | 0.0161 | 0.0161 | 0.0000 [0.0000, 0.0000] | +0.1 % | 100 | A |
| aa1 | footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=2,type=aa,working-set-mib=32 | 0.0962 | 0.0967 | 0.0005 [0.0005, 0.0006] | +0.6 % | 50 | B |
| aa1 | footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=2,type=aa,working-set-mib=8 | 0.0161 | 0.0161 | 0.0000 [-0.0000, 0.0000] | +0.0 % | 100 | A |
| aa1 | footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=3,type=aa,working-set-mib=32 | 0.0975 | 0.0989 | 0.0014 [0.0013, 0.0015] | +1.4 % | 10 | B |
| aa1 | footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=3,type=aa,working-set-mib=8 | 0.0161 | 0.0161 | -0.0000 [-0.0000, -0.0000] | -0.1 % | 70 | A |
| aa1 | footprint-mib=1024,kernel=k6,placement=cpu,replicate=1,type=aa,update=atomic | 6.0449 | 6.0050 | -0.0383 [-0.0409, -0.0360] | -0.6 % | 40 | B |
| aa1 | footprint-mib=1024,kernel=k6,placement=cpu,replicate=2,type=aa,update=atomic | 6.0329 | 6.0100 | -0.0230 [-0.0252, -0.0210] | -0.4 % | 100 | A |
| aa1 | footprint-mib=1024,kernel=k6,placement=cpu,replicate=3,type=aa,update=atomic | 6.0426 | 5.9900 | -0.0518 [-0.0543, -0.0458] | -0.9 % | 20 | A |
| aa1 | footprint-mib=1024,kernel=k6,placement=hbm,replicate=1,type=aa,update=atomic | 0.8161 | 0.8160 | -0.0001 [-0.0003, 0.0001] | -0.0 % | 100 | A |
| aa1 | footprint-mib=1024,kernel=k6,placement=hbm,replicate=2,type=aa,update=atomic | 0.8142 | 0.8153 | 0.0011 [0.0008, 0.0015] | +0.1 % | 100 | A |
| aa1 | footprint-mib=1024,kernel=k6,placement=hbm,replicate=3,type=aa,update=atomic | 0.8148 | 0.8158 | 0.0010 [0.0008, 0.0013] | +0.1 % | 100 | B |
| aa1 | footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,replicate=1,type=aa,update=atomic | 12.7469 | 12.7989 | 0.0544 [0.0100, 0.0939] | +0.4 % | 100 | B |
| aa1 | footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,replicate=2,type=aa,update=atomic | 12.5717 | 12.5671 | -0.0069 [-0.0344, 0.0165] | -0.1 % | 100 | A |
| aa1 | footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,replicate=3,type=aa,update=atomic | 12.7534 | 12.7372 | -0.0596 [-0.0805, -0.0209] | -0.5 % | 100 | A |
| aa1 | footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,replicate=1,type=aa,update=atomic | 17.4147 | 17.3354 | -0.1313 [-0.1803, 0.1182] | -0.8 % | 100 | A |
| aa1 | footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,replicate=2,type=aa,update=atomic | 17.6158 | 17.7109 | 0.2067 [0.1271, 0.2859] | +1.2 % | 100 | B |
| aa1 | footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,replicate=3,type=aa,update=atomic | 17.3036 | 17.4592 | 0.2035 [0.1515, 0.2563] | +1.2 % | 100 | B |
| aa1 | footprint-mib=512,host=reads,kernel=k5,placement=cpu,replicate=1,sharing=shared,sweeps=8,tiling=tiles,type=aa | 30.8266 | 28.1130 | -2.7157 [-2.7257, -2.6765] | -8.8 % | 10 | A |
| aa1 | footprint-mib=512,host=reads,kernel=k5,placement=cpu,replicate=2,sharing=shared,sweeps=8,tiling=tiles,type=aa | 30.8628 | 28.1442 | -2.7052 [-2.7784, -2.6869] | -8.8 % | 10 | B |
| aa1 | footprint-mib=512,host=reads,kernel=k5,placement=cpu,replicate=3,sharing=shared,sweeps=8,tiling=tiles,type=aa | 30.8797 | 28.2833 | -2.6053 [-2.6271, -2.5625] | -8.4 % | 10 | B |
| aa1 | footprint-mib=512,host=reads,kernel=k5,placement=hbm,replicate=1,sharing=shared,sweeps=8,tiling=tiles,type=aa | 3.2820 | 3.2776 | -0.0044 [-0.0049, -0.0035] | -0.1 % | 100 | B |
| aa1 | footprint-mib=512,host=reads,kernel=k5,placement=hbm,replicate=2,sharing=shared,sweeps=8,tiling=tiles,type=aa | 3.2627 | 3.2669 | 0.0040 [0.0027, 0.0047] | +0.1 % | 100 | B |
| aa1 | footprint-mib=512,host=reads,kernel=k5,placement=hbm,replicate=3,sharing=shared,sweeps=8,tiling=tiles,type=aa | 3.2645 | 3.2606 | -0.0037 [-0.0043, -0.0026] | -0.1 % | 100 | A |
| aa1 | footprint-mib=512,kernel=k5,placement=cpu,replicate=1,sweeps=8,tiling=tiles,type=aa | 30.8338 | 28.0311 | -2.7991 [-2.8256, -2.7637] | -9.1 % | 10 | B |
| aa1 | footprint-mib=512,kernel=k5,placement=cpu,replicate=2,sweeps=8,tiling=tiles,type=aa | 30.9944 | 28.1993 | -2.7876 [-2.8274, -2.7639] | -9.0 % | 10 | B |
| aa1 | footprint-mib=512,kernel=k5,placement=cpu,replicate=3,sweeps=8,tiling=tiles,type=aa | 30.9038 | 28.2228 | -2.6762 [-2.7088, -2.6316] | -8.7 % | 10 | B |
| aa1 | footprint-mib=512,kernel=k5,placement=hbm,replicate=1,sweeps=8,tiling=tiles,type=aa | 3.2536 | 3.2712 | 0.0164 [0.0154, 0.0186] | +0.5 % | 90 | A |
| aa1 | footprint-mib=512,kernel=k5,placement=hbm,replicate=2,sweeps=8,tiling=tiles,type=aa | 3.2661 | 3.2641 | -0.0020 [-0.0030, -0.0012] | -0.1 % | 100 | A |
| aa1 | footprint-mib=512,kernel=k5,placement=hbm,replicate=3,sweeps=8,tiling=tiles,type=aa | 3.2433 | 3.2516 | 0.0083 [0.0073, 0.0093] | +0.3 % | 100 | A |
| aa1 | footprint-mib=8,kernel=k6,keys=1024,placement=cpu,replicate=1,type=aa | 12.5058 | 12.4821 | -0.0225 [-0.0256, -0.0204] | -0.2 % | 100 | A |
| aa1 | footprint-mib=8,kernel=k6,keys=1024,placement=cpu,replicate=2,type=aa | 12.5037 | 12.4776 | -0.0263 [-0.0279, -0.0237] | -0.2 % | 70 | B |
| aa1 | footprint-mib=8,kernel=k6,keys=1024,placement=cpu,replicate=3,type=aa | 12.4971 | 12.4776 | -0.0193 [-0.0217, -0.0179] | -0.2 % | 90 | A |
| aa1 | footprint-mib=8,kernel=k6,keys=1024,placement=hbm,replicate=1,type=aa | 0.7670 | 0.7672 | 0.0003 [0.0002, 0.0003] | +0.0 % | 100 | B |
| aa1 | footprint-mib=8,kernel=k6,keys=1024,placement=hbm,replicate=2,type=aa | 0.7657 | 0.7657 | 0.0000 [-0.0000, 0.0001] | +0.0 % | 100 | A |
| aa1 | footprint-mib=8,kernel=k6,keys=1024,placement=hbm,replicate=3,type=aa | 0.7662 | 0.7662 | 0.0000 [-0.0000, 0.0001] | +0.0 % | 100 | A |
| aa2 | f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,replicate=1,type=aa | 2.9168 | 2.8880 | -0.0287 [-0.0293, -0.0280] | -1.0 % | 10 | B |
| aa2 | f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,replicate=2,type=aa | 2.9128 | 2.8899 | -0.0226 [-0.0238, -0.0207] | -0.8 % | 10 | A |
| aa2 | f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=cpu,replicate=3,type=aa | 2.9057 | 2.8847 | -0.0209 [-0.0215, -0.0186] | -0.7 % | 10 | A |
| aa2 | f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,replicate=1,type=aa | 0.2974 | 0.2967 | -0.0007 [-0.0007, -0.0006] | -0.2 % | 20 | A |
| aa2 | f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,replicate=2,type=aa | 0.2984 | 0.2994 | 0.0009 [0.0009, 0.0010] | +0.3 % | 20 | B |
| aa2 | f-den=1,f-num=1,footprint-mib=1024,kernel=k1,placement=hbm,replicate=3,type=aa | 0.2978 | 0.2989 | 0.0012 [0.0011, 0.0013] | +0.4 % | 30 | A |
| aa2 | f-den=1,f-num=1,footprint-mib=64,kernel=k1,placement=cpu,replicate=1,type=aa | 0.1851 | 0.1841 | -0.0010 [-0.0010, -0.0009] | -0.5 % | 10 | B |
| aa2 | f-den=1,f-num=1,footprint-mib=64,kernel=k1,placement=cpu,replicate=2,type=aa | 0.1830 | 0.1808 | -0.0022 [-0.0022, -0.0021] | -1.2 % | 10 | B |
| aa2 | f-den=1,f-num=1,footprint-mib=64,kernel=k1,placement=cpu,replicate=3,type=aa | 0.1855 | 0.1860 | 0.0004 [0.0004, 0.0005] | +0.2 % | 20 | B |
| aa2 | footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,replicate=1,sharing=shared,type=aa | 31.0980 | 31.0516 | -0.0439 [-0.0523, -0.0362] | -0.1 % | 100 | B |
| aa2 | footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,replicate=2,sharing=shared,type=aa | 31.0313 | 31.0464 | 0.0138 [0.0107, 0.0230] | +0.0 % | 100 | B |
| aa2 | footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,replicate=3,sharing=shared,type=aa | 31.1160 | 30.9063 | -0.2118 [-0.2192, -0.1925] | -0.7 % | 30 | B |
| aa2 | footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,replicate=1,sharing=shared,type=aa | 1.2779 | 1.2770 | -0.0011 [-0.0019, 0.0003] | -0.1 % | 100 | A |
| aa2 | footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,replicate=2,sharing=shared,type=aa | 1.2751 | 1.2746 | -0.0004 [-0.0009, 0.0000] | -0.0 % | 100 | A |
| aa2 | footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,replicate=3,sharing=shared,type=aa | 1.2754 | 1.2745 | -0.0012 [-0.0017, -0.0007] | -0.1 % | 100 | A |
| aa2 | footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,replicate=1,type=aa | 31.1582 | 31.0169 | -0.1361 [-0.1524, -0.1280] | -0.4 % | 30 | A |
| aa2 | footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,replicate=2,type=aa | 31.0505 | 30.9924 | -0.0576 [-0.0639, -0.0521] | -0.2 % | 100 | A |
| aa2 | footprint-mib=1024,generator=uniform,kernel=k4,placement=cpu,replicate=3,type=aa | 31.0678 | 30.9833 | -0.0833 [-0.0901, -0.0735] | -0.3 % | 80 | A |
| aa2 | footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,replicate=1,type=aa | 1.2701 | 1.2699 | -0.0001 [-0.0003, 0.0002] | -0.0 % | 100 | B |
| aa2 | footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,replicate=2,type=aa | 1.2700 | 1.2695 | -0.0006 [-0.0009, -0.0003] | -0.0 % | 100 | A |
| aa2 | footprint-mib=1024,generator=uniform,kernel=k4,placement=hbm,replicate=3,type=aa | 1.2703 | 1.2697 | -0.0008 [-0.0011, -0.0006] | -0.1 % | 100 | B |
| aa2 | footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=1,type=aa,working-set-mib=32 | 1.4933 | 1.4941 | 0.0008 [0.0005, 0.0012] | +0.1 % | 100 | A |
| aa2 | footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=1,type=aa,working-set-mib=8 | 0.0375 | 0.0372 | -0.0003 [-0.0003, -0.0002] | -0.7 % | 10 | B |
| aa2 | footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=2,type=aa,working-set-mib=32 | 1.5031 | 1.4944 | -0.0087 [-0.0091, -0.0081] | -0.6 % | 20 | B |
| aa2 | footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=2,type=aa,working-set-mib=8 | 0.0377 | 0.0373 | -0.0004 [-0.0004, -0.0003] | -1.0 % | 20 | B |
| aa2 | footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=3,type=aa,working-set-mib=32 | 1.4808 | 1.4936 | 0.0126 [0.0121, 0.0135] | +0.9 % | 10 | B |
| aa2 | footprint-mib=1024,k=16,kernel=k2,placement=cpu,replicate=3,type=aa,working-set-mib=8 | 0.0377 | 0.0373 | -0.0004 [-0.0004, -0.0003] | -1.0 % | 20 | B |
| aa2 | footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=1,type=aa,working-set-mib=32 | 0.0969 | 0.0978 | 0.0009 [0.0008, 0.0010] | +0.9 % | 30 | A |
| aa2 | footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=1,type=aa,working-set-mib=8 | 0.0160 | 0.0160 | 0.0000 [0.0000, 0.0000] | +0.1 % | 100 | B |
| aa2 | footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=2,type=aa,working-set-mib=32 | 0.0962 | 0.0990 | 0.0029 [0.0028, 0.0031] | +3.0 % | 10 | A |
| aa2 | footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=2,type=aa,working-set-mib=8 | 0.0161 | 0.0161 | -0.0000 [-0.0000, 0.0000] | -0.0 % | 100 | B |
| aa2 | footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=3,type=aa,working-set-mib=32 | 0.0975 | 0.0972 | -0.0004 [-0.0004, -0.0003] | -0.4 % | 100 | A |
| aa2 | footprint-mib=1024,k=16,kernel=k2,placement=hbm,replicate=3,type=aa,working-set-mib=8 | 0.0162 | 0.0161 | -0.0000 [-0.0000, -0.0000] | -0.1 % | 100 | A |
| aa2 | footprint-mib=1024,kernel=k6,placement=cpu,replicate=1,type=aa,update=atomic | 6.0350 | 6.0114 | -0.0224 [-0.0245, -0.0205] | -0.4 % | 40 | A |
| aa2 | footprint-mib=1024,kernel=k6,placement=cpu,replicate=2,type=aa,update=atomic | 6.0423 | 5.9996 | -0.0446 [-0.0456, -0.0393] | -0.7 % | 20 | B |
| aa2 | footprint-mib=1024,kernel=k6,placement=cpu,replicate=3,type=aa,update=atomic | 6.0404 | 6.0117 | -0.0297 [-0.0324, -0.0263] | -0.5 % | 100 | A |
| aa2 | footprint-mib=1024,kernel=k6,placement=hbm,replicate=1,type=aa,update=atomic | 0.8157 | 0.8158 | 0.0002 [-0.0001, 0.0005] | +0.0 % | 100 | B |
| aa2 | footprint-mib=1024,kernel=k6,placement=hbm,replicate=2,type=aa,update=atomic | 0.8166 | 0.8153 | -0.0011 [-0.0017, -0.0008] | -0.1 % | 100 | A |
| aa2 | footprint-mib=1024,kernel=k6,placement=hbm,replicate=3,type=aa,update=atomic | 0.8152 | 0.8161 | 0.0010 [0.0007, 0.0013] | +0.1 % | 100 | A |
| aa2 | footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,replicate=1,type=aa,update=atomic | 12.6291 | 12.6457 | 0.0366 [0.0103, 0.0775] | +0.3 % | 100 | A |
| aa2 | footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,replicate=2,type=aa,update=atomic | 12.6680 | 12.7163 | 0.0275 [0.0134, 0.0741] | +0.2 % | 100 | B |
| aa2 | footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,replicate=3,type=aa,update=atomic | 12.5714 | 12.5817 | 0.0144 [-0.0026, 0.0407] | +0.1 % | 100 | B |
| aa2 | footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,replicate=1,type=aa,update=atomic | 17.2227 | 17.4944 | 0.2719 [0.2137, 0.3110] | +1.6 % | 100 | A |
| aa2 | footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,replicate=2,type=aa,update=atomic | 17.3631 | 17.3626 | 0.0487 [-0.1868, 0.1998] | +0.3 % | 100 | B |
| aa2 | footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,replicate=3,type=aa,update=atomic | 17.4498 | 17.3419 | -0.1428 [-0.2252, 0.1201] | -0.8 % | 100 | B |
| aa2 | footprint-mib=512,host=reads,kernel=k5,placement=cpu,replicate=1,sharing=shared,sweeps=8,tiling=tiles,type=aa | 30.7528 | 28.1165 | -2.6357 [-2.6819, -2.5884] | -8.6 % | 10 | A |
| aa2 | footprint-mib=512,host=reads,kernel=k5,placement=cpu,replicate=2,sharing=shared,sweeps=8,tiling=tiles,type=aa | 30.9355 | 28.1624 | -2.7620 [-2.8135, -2.7425] | -8.9 % | 10 | B |
| aa2 | footprint-mib=512,host=reads,kernel=k5,placement=cpu,replicate=3,sharing=shared,sweeps=8,tiling=tiles,type=aa | 30.8322 | 28.2334 | -2.5894 [-2.6247, -2.5578] | -8.4 % | 10 | B |
| aa2 | footprint-mib=512,host=reads,kernel=k5,placement=hbm,replicate=1,sharing=shared,sweeps=8,tiling=tiles,type=aa | 3.2599 | 3.2496 | -0.0102 [-0.0121, -0.0087] | -0.3 % | 100 | B |
| aa2 | footprint-mib=512,host=reads,kernel=k5,placement=hbm,replicate=2,sharing=shared,sweeps=8,tiling=tiles,type=aa | 3.2695 | 3.2845 | 0.0162 [0.0147, 0.0177] | +0.5 % | 50 | B |
| aa2 | footprint-mib=512,host=reads,kernel=k5,placement=hbm,replicate=3,sharing=shared,sweeps=8,tiling=tiles,type=aa | 3.2432 | 3.2556 | 0.0127 [0.0115, 0.0133] | +0.4 % | 90 | A |
| aa2 | footprint-mib=512,kernel=k5,placement=cpu,replicate=1,sweeps=8,tiling=tiles,type=aa | 30.7406 | 28.0526 | -2.6968 [-2.7237, -2.6458] | -8.8 % | 10 | B |
| aa2 | footprint-mib=512,kernel=k5,placement=cpu,replicate=2,sweeps=8,tiling=tiles,type=aa | 30.6107 | 27.9908 | -2.6368 [-2.6675, -2.5603] | -8.6 % | 10 | A |
| aa2 | footprint-mib=512,kernel=k5,placement=cpu,replicate=3,sweeps=8,tiling=tiles,type=aa | 30.9201 | 28.0281 | -2.8868 [-2.9217, -2.8550] | -9.3 % | 10 | B |
| aa2 | footprint-mib=512,kernel=k5,placement=hbm,replicate=1,sweeps=8,tiling=tiles,type=aa | 3.2634 | 3.2595 | -0.0033 [-0.0049, -0.0015] | -0.1 % | 100 | A |
| aa2 | footprint-mib=512,kernel=k5,placement=hbm,replicate=2,sweeps=8,tiling=tiles,type=aa | 3.2412 | 3.2749 | 0.0349 [0.0325, 0.0378] | +1.1 % | 10 | A |
| aa2 | footprint-mib=512,kernel=k5,placement=hbm,replicate=3,sweeps=8,tiling=tiles,type=aa | 3.2654 | 3.2532 | -0.0120 [-0.0137, -0.0107] | -0.4 % | 100 | A |
| aa2 | footprint-mib=8,kernel=k6,keys=1024,placement=cpu,replicate=1,type=aa | 12.4807 | 12.4791 | -0.0012 [-0.0025, 0.0006] | -0.0 % | 100 | A |
| aa2 | footprint-mib=8,kernel=k6,keys=1024,placement=cpu,replicate=2,type=aa | 12.4820 | 12.4893 | 0.0080 [0.0068, 0.0095] | +0.1 % | 100 | B |
| aa2 | footprint-mib=8,kernel=k6,keys=1024,placement=cpu,replicate=3,type=aa | 12.4742 | 12.4899 | 0.0149 [0.0126, 0.0156] | +0.1 % | 80 | A |
| aa2 | footprint-mib=8,kernel=k6,keys=1024,placement=hbm,replicate=1,type=aa | 0.7663 | 0.7664 | 0.0002 [0.0001, 0.0002] | +0.0 % | 100 | A |
| aa2 | footprint-mib=8,kernel=k6,keys=1024,placement=hbm,replicate=2,type=aa | 0.7669 | 0.7667 | -0.0002 [-0.0002, -0.0002] | -0.0 % | 100 | A |
| aa2 | footprint-mib=8,kernel=k6,keys=1024,placement=hbm,replicate=3,type=aa | 0.7672 | 0.7670 | -0.0002 [-0.0003, -0.0002] | -0.0 % | 100 | A |
| c1 | footprint-mib=16384,kernel=k3,placement=cpu,replicate=1,type=aa | 432.8821 | 432.9494 | 0.0552 [0.0196, 0.0838] | +0.0 % | 100 | B |
| c1 | footprint-mib=16384,kernel=k3,placement=cpu,replicate=10,type=aa | 433.5367 | 433.5509 | -0.0020 [-0.0380, 0.0379] | -0.0 % | 100 | A |
| c1 | footprint-mib=16384,kernel=k3,placement=cpu,replicate=2,type=aa | 432.9193 | 432.9364 | 0.0108 [-0.0126, 0.0554] | +0.0 % | 100 | B |
| c1 | footprint-mib=16384,kernel=k3,placement=cpu,replicate=3,type=aa | 432.9029 | 432.8996 | 0.0108 [-0.0387, 0.0499] | +0.0 % | 100 | B |
| c1 | footprint-mib=16384,kernel=k3,placement=cpu,replicate=4,type=aa | 432.9091 | 432.9223 | 0.0201 [-0.0187, 0.0521] | +0.0 % | 100 | A |
| c1 | footprint-mib=16384,kernel=k3,placement=cpu,replicate=5,type=aa | 432.9018 | 432.8703 | -0.0287 [-0.0556, 0.0168] | -0.0 % | 100 | A |
| c1 | footprint-mib=16384,kernel=k3,placement=cpu,replicate=6,type=aa | 432.9178 | 432.9101 | 0.0170 [-0.0192, 0.0493] | +0.0 % | 100 | B |
| c1 | footprint-mib=16384,kernel=k3,placement=cpu,replicate=7,type=aa | 432.9073 | 432.9092 | 0.0042 [-0.0229, 0.0591] | +0.0 % | 100 | A |
| c1 | footprint-mib=16384,kernel=k3,placement=cpu,replicate=8,type=aa | 433.5312 | 433.5955 | 0.0513 [0.0209, 0.1025] | +0.0 % | 100 | B |
| c1 | footprint-mib=16384,kernel=k3,placement=cpu,replicate=9,type=aa | 433.5160 | 433.5926 | 0.0360 [-0.0151, 0.0941] | +0.0 % | 100 | B |
| c1 | footprint-mib=8192,kernel=k3,placement=cpu,replicate=1,type=aa | 7.8827 | 7.8539 | -0.0288 [-0.0315, -0.0276] | -0.4 % | 10 | B |
| c1 | footprint-mib=8192,kernel=k3,placement=cpu,replicate=10,type=aa | 7.8867 | 7.8427 | -0.0444 [-0.0455, -0.0434] | -0.6 % | 10 | A |
| c1 | footprint-mib=8192,kernel=k3,placement=cpu,replicate=2,type=aa | 7.8891 | 7.8456 | -0.0431 [-0.0452, -0.0424] | -0.5 % | 10 | B |
| c1 | footprint-mib=8192,kernel=k3,placement=cpu,replicate=3,type=aa | 7.8778 | 7.8461 | -0.0317 [-0.0343, -0.0300] | -0.4 % | 10 | B |
| c1 | footprint-mib=8192,kernel=k3,placement=cpu,replicate=4,type=aa | 7.8890 | 7.8523 | -0.0372 [-0.0382, -0.0355] | -0.5 % | 10 | A |
| c1 | footprint-mib=8192,kernel=k3,placement=cpu,replicate=5,type=aa | 7.8880 | 7.8525 | -0.0356 [-0.0368, -0.0347] | -0.5 % | 10 | A |
| c1 | footprint-mib=8192,kernel=k3,placement=cpu,replicate=6,type=aa | 7.8901 | 7.8451 | -0.0449 [-0.0465, -0.0440] | -0.6 % | 10 | A |
| c1 | footprint-mib=8192,kernel=k3,placement=cpu,replicate=7,type=aa | 7.8864 | 7.8592 | -0.0267 [-0.0297, -0.0254] | -0.3 % | 10 | B |
| c1 | footprint-mib=8192,kernel=k3,placement=cpu,replicate=8,type=aa | 7.8877 | 7.8445 | -0.0429 [-0.0455, -0.0404] | -0.5 % | 10 | A |
| c1 | footprint-mib=8192,kernel=k3,placement=cpu,replicate=9,type=aa | 7.8871 | 7.8534 | -0.0338 [-0.0346, -0.0318] | -0.4 % | 10 | A |
| c2 | footprint-mib=16384,kernel=k3,placement=cpu,replicate=1,type=aa | 432.9270 | 432.9206 | -0.0198 [-0.0544, 0.0422] | -0.0 % | 100 | B |
| c2 | footprint-mib=16384,kernel=k3,placement=cpu,replicate=10,type=aa | 432.8881 | 432.9299 | -0.0117 [-0.0464, 0.0341] | -0.0 % | 100 | B |
| c2 | footprint-mib=16384,kernel=k3,placement=cpu,replicate=2,type=aa | 432.9246 | 432.9475 | 0.0235 [-0.0109, 0.0768] | +0.0 % | 100 | B |
| c2 | footprint-mib=16384,kernel=k3,placement=cpu,replicate=3,type=aa | 432.9406 | 432.9440 | 0.0022 [-0.0355, 0.0416] | +0.0 % | 100 | A |
| c2 | footprint-mib=16384,kernel=k3,placement=cpu,replicate=4,type=aa | 433.0094 | 433.0753 | 0.0758 [0.0269, 0.1160] | +0.0 % | 100 | A |
| c2 | footprint-mib=16384,kernel=k3,placement=cpu,replicate=5,type=aa | 433.5736 | 433.6315 | 0.0509 [0.0248, 0.0729] | +0.0 % | 100 | A |
| c2 | footprint-mib=16384,kernel=k3,placement=cpu,replicate=6,type=aa | 433.5999 | 433.6344 | 0.0672 [0.0133, 0.1177] | +0.0 % | 100 | B |
| c2 | footprint-mib=16384,kernel=k3,placement=cpu,replicate=7,type=aa | 433.6102 | 433.6183 | 0.0170 [-0.0176, 0.0718] | +0.0 % | 100 | B |
| c2 | footprint-mib=16384,kernel=k3,placement=cpu,replicate=8,type=aa | 432.9245 | 432.9910 | 0.0482 [0.0018, 0.0762] | +0.0 % | 100 | A |
| c2 | footprint-mib=16384,kernel=k3,placement=cpu,replicate=9,type=aa | 432.8981 | 432.9111 | -0.0012 [-0.0368, 0.0555] | -0.0 % | 100 | B |
| c2 | footprint-mib=8192,kernel=k3,placement=cpu,replicate=1,type=aa | 7.8874 | 7.8453 | -0.0419 [-0.0439, -0.0401] | -0.5 % | 10 | B |
| c2 | footprint-mib=8192,kernel=k3,placement=cpu,replicate=10,type=aa | 7.8877 | 7.8532 | -0.0351 [-0.0376, -0.0320] | -0.4 % | 10 | B |
| c2 | footprint-mib=8192,kernel=k3,placement=cpu,replicate=2,type=aa | 7.8868 | 7.8447 | -0.0414 [-0.0433, -0.0401] | -0.5 % | 10 | B |
| c2 | footprint-mib=8192,kernel=k3,placement=cpu,replicate=3,type=aa | 7.8874 | 7.8484 | -0.0391 [-0.0431, -0.0371] | -0.5 % | 10 | B |
| c2 | footprint-mib=8192,kernel=k3,placement=cpu,replicate=4,type=aa | 7.8886 | 7.8544 | -0.0345 [-0.0355, -0.0325] | -0.4 % | 10 | B |
| c2 | footprint-mib=8192,kernel=k3,placement=cpu,replicate=5,type=aa | 7.8892 | 7.8177 | -0.0712 [-0.0732, -0.0689] | -0.9 % | 10 | B |
| c2 | footprint-mib=8192,kernel=k3,placement=cpu,replicate=6,type=aa | 7.8872 | 7.8446 | -0.0421 [-0.0433, -0.0408] | -0.5 % | 10 | B |
| c2 | footprint-mib=8192,kernel=k3,placement=cpu,replicate=7,type=aa | 7.8887 | 7.8454 | -0.0424 [-0.0452, -0.0400] | -0.5 % | 10 | B |
| c2 | footprint-mib=8192,kernel=k3,placement=cpu,replicate=8,type=aa | 7.8862 | 7.8469 | -0.0397 [-0.0411, -0.0369] | -0.5 % | 10 | B |
| c2 | footprint-mib=8192,kernel=k3,placement=cpu,replicate=9,type=aa | 7.8874 | 7.8423 | -0.0453 [-0.0479, -0.0436] | -0.6 % | 10 | B |
