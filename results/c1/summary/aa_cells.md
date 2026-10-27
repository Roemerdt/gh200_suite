# A/A' cells: two identically prepared direct variants, recomputed from raw rows

Times are per pass in ms. The difference B - A within a repeat is the noise between identically prepared buffers, as median with its 95 % rank interval; its spread over the A/A' cells of a footprint is the floor for translation contrasts there. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | A ms | B ms | B - A ms [interval] | relative to A | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=1,type=aa | 432.8821 | 432.9494 | 0.0552 [0.0196, 0.0838] | +0.0 % | 100 | yes | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=10,type=aa | 433.5367 | 433.5509 | -0.0020 [-0.0380, 0.0379] | -0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=2,type=aa | 432.9193 | 432.9364 | 0.0108 [-0.0126, 0.0554] | +0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=3,type=aa | 432.9029 | 432.8996 | 0.0108 [-0.0387, 0.0499] | +0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=4,type=aa | 432.9091 | 432.9223 | 0.0201 [-0.0187, 0.0521] | +0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=5,type=aa | 432.9018 | 432.8703 | -0.0287 [-0.0556, 0.0168] | -0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=6,type=aa | 432.9178 | 432.9101 | 0.0170 [-0.0192, 0.0493] | +0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=7,type=aa | 432.9073 | 432.9092 | 0.0042 [-0.0229, 0.0591] | +0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=8,type=aa | 433.5312 | 433.5955 | 0.0513 [0.0209, 0.1025] | +0.0 % | 100 | yes | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=9,type=aa | 433.5160 | 433.5926 | 0.0360 [-0.0151, 0.0941] | +0.0 % | 100 | no | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=1,type=aa | 7.8827 | 7.8539 | -0.0288 [-0.0315, -0.0276] | -0.4 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=10,type=aa | 7.8867 | 7.8427 | -0.0444 [-0.0455, -0.0434] | -0.6 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=2,type=aa | 7.8891 | 7.8456 | -0.0431 [-0.0452, -0.0424] | -0.5 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=3,type=aa | 7.8778 | 7.8461 | -0.0317 [-0.0343, -0.0300] | -0.4 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=4,type=aa | 7.8890 | 7.8523 | -0.0372 [-0.0382, -0.0355] | -0.5 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=5,type=aa | 7.8880 | 7.8525 | -0.0356 [-0.0368, -0.0347] | -0.5 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=6,type=aa | 7.8901 | 7.8451 | -0.0449 [-0.0465, -0.0440] | -0.6 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=7,type=aa | 7.8864 | 7.8592 | -0.0267 [-0.0297, -0.0254] | -0.3 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=8,type=aa | 7.8877 | 7.8445 | -0.0429 [-0.0455, -0.0404] | -0.5 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=9,type=aa | 7.8871 | 7.8534 | -0.0338 [-0.0346, -0.0318] | -0.4 % | 10 | yes | pass |

## Per cell

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=1,type=aa

- first variant B, seed 71; repeats alternated as drawn: yes
- buffers: A at 0x427980000000, B at 0x427e40000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=10,type=aa

- first variant A, seed 71; repeats alternated as drawn: yes
- buffers: A at 0x4b12c0000000, B at 0x4b1780000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=2,type=aa

- first variant B, seed 71; repeats alternated as drawn: yes
- buffers: A at 0x5778c0000000, B at 0x577d40000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=3,type=aa

- first variant B, seed 71; repeats alternated as drawn: yes
- buffers: A at 0x5759c0000000, B at 0x575e40000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=4,type=aa

- first variant A, seed 71; repeats alternated as drawn: yes
- buffers: A at 0x5dfe00000000, B at 0x5e0280000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=5,type=aa

- first variant A, seed 71; repeats alternated as drawn: yes
- buffers: A at 0x478480000000, B at 0x478900000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=6,type=aa

- first variant B, seed 71; repeats alternated as drawn: yes
- buffers: A at 0x5b9900000000, B at 0x5b9d80000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=7,type=aa

- first variant A, seed 71; repeats alternated as drawn: yes
- buffers: A at 0x56f800000000, B at 0x56fcc0000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=8,type=aa

- first variant B, seed 71; repeats alternated as drawn: yes
- buffers: A at 0x578840000000, B at 0x578d00000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=9,type=aa

- first variant B, seed 71; repeats alternated as drawn: yes
- buffers: A at 0x52df80000000, B at 0x52e440000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=1,type=aa

- first variant B, seed 71; repeats alternated as drawn: yes
- buffers: A at 0x4dfa40000000, B at 0x4dfd00000000
- per repetition: home 5.369e+08 link read bytes and 4.428e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.445e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=10,type=aa

- first variant A, seed 71; repeats alternated as drawn: yes
- buffers: A at 0x542ec0000000, B at 0x543140000000
- per repetition: home 5.369e+08 link read bytes and 4.424e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.428e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=2,type=aa

- first variant B, seed 71; repeats alternated as drawn: yes
- buffers: A at 0x42d940000000, B at 0x42dc00000000
- per repetition: home 5.369e+08 link read bytes and 4.419e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.442e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=3,type=aa

- first variant B, seed 71; repeats alternated as drawn: yes
- buffers: A at 0x40e680000000, B at 0x40e940000000
- per repetition: home 5.369e+08 link read bytes and 4.426e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.426e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=4,type=aa

- first variant A, seed 71; repeats alternated as drawn: yes
- buffers: A at 0x533b00000000, B at 0x533d80000000
- per repetition: home 5.369e+08 link read bytes and 4.43e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.428e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=5,type=aa

- first variant A, seed 71; repeats alternated as drawn: yes
- buffers: A at 0x480580000000, B at 0x480800000000
- per repetition: home 5.369e+08 link read bytes and 4.426e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.437e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=6,type=aa

- first variant A, seed 71; repeats alternated as drawn: yes
- buffers: A at 0x55e880000000, B at 0x55eb40000000
- per repetition: home 5.369e+08 link read bytes and 4.42e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.431e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=7,type=aa

- first variant B, seed 71; repeats alternated as drawn: yes
- buffers: A at 0x4a9fc0000000, B at 0x4aa240000000
- per repetition: home 5.369e+08 link read bytes and 4.422e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.436e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=8,type=aa

- first variant A, seed 71; repeats alternated as drawn: yes
- buffers: A at 0x4767c0000000, B at 0x476a40000000
- per repetition: home 5.369e+08 link read bytes and 4.429e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.441e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=9,type=aa

- first variant A, seed 71; repeats alternated as drawn: yes
- buffers: A at 0x5086c0000000, B at 0x508980000000
- per repetition: home 5.369e+08 link read bytes and 4.423e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.434e+04 SMMU translation requests; multiplexed rows voided: 0

