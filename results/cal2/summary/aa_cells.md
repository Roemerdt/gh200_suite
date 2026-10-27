# A/A' cells: two identically prepared direct variants, recomputed from raw rows

Times are per pass in ms. The difference B - A within a repeat is the noise between identically prepared buffers, as median with its 95 % rank interval; its spread over the A/A' cells of a footprint is the floor for translation contrasts there. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | A ms | B ms | B - A ms [interval] | relative to A | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=1,type=aa | 433.5808 | 433.5421 | -0.0522 [-0.0895, -0.0266] | -0.0 % | 100 | yes | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=10,type=aa | 433.5543 | 433.5438 | -0.0323 [-0.0546, -0.0005] | -0.0 % | 100 | yes | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=2,type=aa | 432.8221 | 432.8510 | 0.0152 [-0.0292, 0.0497] | +0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=3,type=aa | 433.4416 | 433.4528 | -0.0263 [-0.0590, 0.0230] | -0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=4,type=aa | 433.5120 | 433.4957 | -0.0187 [-0.0594, 0.0223] | -0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=5,type=aa | 433.3901 | 433.4163 | 0.0112 [-0.0418, 0.0361] | +0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=6,type=aa | 433.4381 | 433.4251 | -0.0043 [-0.0558, 0.0317] | -0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=7,type=aa | 432.9110 | 432.9265 | 0.0169 [-0.0188, 0.0578] | +0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=8,type=aa | 433.4453 | 433.4766 | 0.0466 [-0.0054, 0.0624] | +0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=9,type=aa | 432.7603 | 432.8276 | 0.0637 [-0.0066, 0.1113] | +0.0 % | 100 | no | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=1,type=aa | 7.8902 | 7.8458 | -0.0448 [-0.0461, -0.0439] | -0.6 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=10,type=aa | 7.8893 | 7.8424 | -0.0463 [-0.0482, -0.0450] | -0.6 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=2,type=aa | 7.8892 | 7.8537 | -0.0351 [-0.0376, -0.0341] | -0.4 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=3,type=aa | 7.8896 | 7.8486 | -0.0406 [-0.0428, -0.0397] | -0.5 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=4,type=aa | 7.8901 | 7.8461 | -0.0446 [-0.0454, -0.0399] | -0.6 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=5,type=aa | 7.8884 | 7.8438 | -0.0440 [-0.0453, -0.0423] | -0.6 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=6,type=aa | 7.8906 | 7.8443 | -0.0453 [-0.0471, -0.0437] | -0.6 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=7,type=aa | 7.8893 | 7.8558 | -0.0353 [-0.0365, -0.0329] | -0.4 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=8,type=aa | 7.8902 | 7.8479 | -0.0423 [-0.0441, -0.0406] | -0.5 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=9,type=aa | 7.8889 | 7.8469 | -0.0417 [-0.0448, -0.0404] | -0.5 % | 10 | yes | pass |

## Per cell

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=1,type=aa

- first variant B, seed 37; repeats alternated as drawn: yes
- buffers: A at 0x485c40000000, B at 0x486100000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=10,type=aa

- first variant A, seed 37; repeats alternated as drawn: yes
- buffers: A at 0x50ca80000000, B at 0x50cf00000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=2,type=aa

- first variant A, seed 37; repeats alternated as drawn: yes
- buffers: A at 0x404cc0000000, B at 0x405140000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=3,type=aa

- first variant A, seed 37; repeats alternated as drawn: yes
- buffers: A at 0x59af40000000, B at 0x59b400000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=4,type=aa

- first variant A, seed 37; repeats alternated as drawn: yes
- buffers: A at 0x5950c0000000, B at 0x595580000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=5,type=aa

- first variant A, seed 37; repeats alternated as drawn: yes
- buffers: A at 0x4fa240000000, B at 0x4fa700000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=6,type=aa

- first variant B, seed 37; repeats alternated as drawn: yes
- buffers: A at 0x408d80000000, B at 0x409200000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=7,type=aa

- first variant A, seed 37; repeats alternated as drawn: yes
- buffers: A at 0x4ee200000000, B at 0x4ee6c0000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=8,type=aa

- first variant B, seed 37; repeats alternated as drawn: yes
- buffers: A at 0x403600000000, B at 0x403ac0000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=9,type=aa

- first variant B, seed 37; repeats alternated as drawn: yes
- buffers: A at 0x4183c0000000, B at 0x418880000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=1,type=aa

- first variant B, seed 37; repeats alternated as drawn: yes
- buffers: A at 0x5a7200000000, B at 0x5a74c0000000
- per repetition: home 5.369e+08 link read bytes and 4.423e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.432e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=10,type=aa

- first variant A, seed 37; repeats alternated as drawn: yes
- buffers: A at 0x482c00000000, B at 0x482ec0000000
- per repetition: home 5.369e+08 link read bytes and 4.432e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.454e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=2,type=aa

- first variant A, seed 37; repeats alternated as drawn: yes
- buffers: A at 0x584540000000, B at 0x5847c0000000
- per repetition: home 5.369e+08 link read bytes and 4.424e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.426e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=3,type=aa

- first variant A, seed 37; repeats alternated as drawn: yes
- buffers: A at 0x593440000000, B at 0x5936c0000000
- per repetition: home 5.369e+08 link read bytes and 4.422e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.426e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=4,type=aa

- first variant B, seed 37; repeats alternated as drawn: yes
- buffers: A at 0x4cec40000000, B at 0x4ceec0000000
- per repetition: home 5.369e+08 link read bytes and 4.423e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.43e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=5,type=aa

- first variant B, seed 37; repeats alternated as drawn: yes
- buffers: A at 0x5069c0000000, B at 0x506c80000000
- per repetition: home 5.369e+08 link read bytes and 4.424e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.447e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=6,type=aa

- first variant A, seed 37; repeats alternated as drawn: yes
- buffers: A at 0x42ab40000000, B at 0x42adc0000000
- per repetition: home 5.369e+08 link read bytes and 4.421e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.443e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=7,type=aa

- first variant A, seed 37; repeats alternated as drawn: yes
- buffers: A at 0x4bef00000000, B at 0x4bf1c0000000
- per repetition: home 5.369e+08 link read bytes and 4.427e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.436e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=8,type=aa

- first variant A, seed 37; repeats alternated as drawn: yes
- buffers: A at 0x584b40000000, B at 0x584dc0000000
- per repetition: home 5.369e+08 link read bytes and 4.424e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.446e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=9,type=aa

- first variant A, seed 37; repeats alternated as drawn: yes
- buffers: A at 0x4c9b80000000, B at 0x4c9e40000000
- per repetition: home 5.369e+08 link read bytes and 4.424e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.432e+04 SMMU translation requests; multiplexed rows voided: 0

