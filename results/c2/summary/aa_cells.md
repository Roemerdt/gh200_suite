# A/A' cells: two identically prepared direct variants, recomputed from raw rows

Times are per pass in ms. The difference B - A within a repeat is the noise between identically prepared buffers, as median with its 95 % rank interval; its spread over the A/A' cells of a footprint is the floor for translation contrasts there. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | A ms | B ms | B - A ms [interval] | relative to A | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=1,type=aa | 432.9270 | 432.9206 | -0.0198 [-0.0544, 0.0422] | -0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=10,type=aa | 432.8881 | 432.9299 | -0.0117 [-0.0464, 0.0341] | -0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=2,type=aa | 432.9246 | 432.9475 | 0.0235 [-0.0109, 0.0768] | +0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=3,type=aa | 432.9406 | 432.9440 | 0.0022 [-0.0355, 0.0416] | +0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=4,type=aa | 433.0094 | 433.0753 | 0.0758 [0.0269, 0.1160] | +0.0 % | 100 | yes | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=5,type=aa | 433.5736 | 433.6315 | 0.0509 [0.0248, 0.0729] | +0.0 % | 100 | yes | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=6,type=aa | 433.5999 | 433.6344 | 0.0672 [0.0133, 0.1177] | +0.0 % | 100 | yes | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=7,type=aa | 433.6102 | 433.6183 | 0.0170 [-0.0176, 0.0718] | +0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=8,type=aa | 432.9245 | 432.9910 | 0.0482 [0.0018, 0.0762] | +0.0 % | 100 | yes | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=9,type=aa | 432.8981 | 432.9111 | -0.0012 [-0.0368, 0.0555] | -0.0 % | 100 | no | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=1,type=aa | 7.8874 | 7.8453 | -0.0419 [-0.0439, -0.0401] | -0.5 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=10,type=aa | 7.8877 | 7.8532 | -0.0351 [-0.0376, -0.0320] | -0.4 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=2,type=aa | 7.8868 | 7.8447 | -0.0414 [-0.0433, -0.0401] | -0.5 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=3,type=aa | 7.8874 | 7.8484 | -0.0391 [-0.0431, -0.0371] | -0.5 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=4,type=aa | 7.8886 | 7.8544 | -0.0345 [-0.0355, -0.0325] | -0.4 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=5,type=aa | 7.8892 | 7.8177 | -0.0712 [-0.0732, -0.0689] | -0.9 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=6,type=aa | 7.8872 | 7.8446 | -0.0421 [-0.0433, -0.0408] | -0.5 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=7,type=aa | 7.8887 | 7.8454 | -0.0424 [-0.0452, -0.0400] | -0.5 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=8,type=aa | 7.8862 | 7.8469 | -0.0397 [-0.0411, -0.0369] | -0.5 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=9,type=aa | 7.8874 | 7.8423 | -0.0453 [-0.0479, -0.0436] | -0.6 % | 10 | yes | pass |

## Per cell

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=1,type=aa

- first variant B, seed 73; repeats alternated as drawn: yes
- buffers: A at 0x532e80000000, B at 0x533340000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=10,type=aa

- first variant B, seed 73; repeats alternated as drawn: yes
- buffers: A at 0x5da740000000, B at 0x5dac00000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=2,type=aa

- first variant B, seed 73; repeats alternated as drawn: yes
- buffers: A at 0x4ac280000000, B at 0x4ac700000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=3,type=aa

- first variant A, seed 73; repeats alternated as drawn: yes
- buffers: A at 0x52cfc0000000, B at 0x52d440000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=4,type=aa

- first variant A, seed 73; repeats alternated as drawn: yes
- buffers: A at 0x4454c0000000, B at 0x445980000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=5,type=aa

- first variant A, seed 73; repeats alternated as drawn: yes
- buffers: A at 0x488800000000, B at 0x488c80000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=6,type=aa

- first variant B, seed 73; repeats alternated as drawn: yes
- buffers: A at 0x5f4000000000, B at 0x5f44c0000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=7,type=aa

- first variant B, seed 73; repeats alternated as drawn: yes
- buffers: A at 0x5df700000000, B at 0x5dfbc0000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=8,type=aa

- first variant A, seed 73; repeats alternated as drawn: yes
- buffers: A at 0x56bbc0000000, B at 0x56c080000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=9,type=aa

- first variant B, seed 73; repeats alternated as drawn: yes
- buffers: A at 0x4c9580000000, B at 0x4c9a40000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=1,type=aa

- first variant B, seed 73; repeats alternated as drawn: yes
- buffers: A at 0x5a24c0000000, B at 0x5a2740000000
- per repetition: home 5.369e+08 link read bytes and 4.425e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.428e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=10,type=aa

- first variant B, seed 73; repeats alternated as drawn: yes
- buffers: A at 0x5f60c0000000, B at 0x5f6340000000
- per repetition: home 5.369e+08 link read bytes and 4.424e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.432e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=2,type=aa

- first variant B, seed 73; repeats alternated as drawn: yes
- buffers: A at 0x44db80000000, B at 0x44de00000000
- per repetition: home 5.369e+08 link read bytes and 4.419e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.427e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=3,type=aa

- first variant B, seed 73; repeats alternated as drawn: yes
- buffers: A at 0x42b740000000, B at 0x42ba00000000
- per repetition: home 5.369e+08 link read bytes and 4.421e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.424e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=4,type=aa

- first variant B, seed 73; repeats alternated as drawn: yes
- buffers: A at 0x5b31c0000000, B at 0x5b3480000000
- per repetition: home 5.369e+08 link read bytes and 4.428e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.438e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=5,type=aa

- first variant B, seed 73; repeats alternated as drawn: yes
- buffers: A at 0x5a5480000000, B at 0x5a5740000000
- per repetition: home 5.369e+08 link read bytes and 4.425e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.435e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=6,type=aa

- first variant B, seed 73; repeats alternated as drawn: yes
- buffers: A at 0x56b840000000, B at 0x56bac0000000
- per repetition: home 5.369e+08 link read bytes and 4.42e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.43e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=7,type=aa

- first variant B, seed 73; repeats alternated as drawn: yes
- buffers: A at 0x5e5ec0000000, B at 0x5e6180000000
- per repetition: home 5.369e+08 link read bytes and 4.427e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.441e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=8,type=aa

- first variant B, seed 73; repeats alternated as drawn: yes
- buffers: A at 0x581480000000, B at 0x581740000000
- per repetition: home 5.369e+08 link read bytes and 4.424e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.438e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=9,type=aa

- first variant B, seed 73; repeats alternated as drawn: yes
- buffers: A at 0x5e2700000000, B at 0x5e2980000000
- per repetition: home 5.369e+08 link read bytes and 4.427e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.441e+04 SMMU translation requests; multiplexed rows voided: 0

