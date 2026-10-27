# A/A' cells: two identically prepared direct variants, recomputed from raw rows

Times are per pass in ms. The difference B - A within a repeat is the noise between identically prepared buffers, as median with its 95 % rank interval; its spread over the A/A' cells of a footprint is the floor for translation contrasts there. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | A ms | B ms | B - A ms [interval] | relative to A | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=1,type=aa | 433.5604 | 433.5746 | 0.0137 [-0.0235, 0.0353] | +0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=10,type=aa | 433.4782 | 433.5009 | 0.0338 [-0.0075, 0.0588] | +0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=2,type=aa | 433.5700 | 433.5747 | -0.0107 [-0.0464, 0.0398] | -0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=3,type=aa | 433.5309 | 433.4767 | -0.0733 [-0.1048, -0.0388] | -0.0 % | 100 | yes | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=4,type=aa | 433.5315 | 433.5578 | 0.0441 [0.0013, 0.0986] | +0.0 % | 100 | yes | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=5,type=aa | 433.5458 | 433.5267 | 0.0053 [-0.0532, 0.0576] | +0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=6,type=aa | 433.5323 | 433.5007 | -0.0263 [-0.0732, 0.0019] | -0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=7,type=aa | 433.4865 | 433.5389 | 0.0490 [0.0093, 0.0778] | +0.0 % | 100 | yes | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=8,type=aa | 433.4767 | 433.4929 | 0.0432 [-0.0278, 0.0795] | +0.0 % | 100 | no | pass |
| footprint-mib=16384,kernel=k3,placement=cpu,replicate=9,type=aa | 433.4646 | 433.4897 | 0.0276 [-0.0014, 0.0871] | +0.0 % | 100 | no | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=1,type=aa | 7.8909 | 7.8450 | -0.0460 [-0.0490, -0.0419] | -0.6 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=10,type=aa | 7.8863 | 7.8478 | -0.0381 [-0.0408, -0.0362] | -0.5 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=2,type=aa | 7.8900 | 7.8477 | -0.0419 [-0.0440, -0.0397] | -0.5 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=3,type=aa | 7.8899 | 7.8475 | -0.0417 [-0.0445, -0.0397] | -0.5 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=4,type=aa | 7.8909 | 7.8487 | -0.0416 [-0.0437, -0.0407] | -0.5 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=5,type=aa | 7.8898 | 7.8429 | -0.0461 [-0.0496, -0.0451] | -0.6 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=6,type=aa | 7.8892 | 7.8549 | -0.0353 [-0.0370, -0.0331] | -0.4 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=7,type=aa | 7.8908 | 7.8421 | -0.0475 [-0.0509, -0.0453] | -0.6 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=8,type=aa | 7.8816 | 7.8545 | -0.0268 [-0.0283, -0.0232] | -0.3 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=9,type=aa | 7.8893 | 7.8307 | -0.0587 [-0.0611, -0.0567] | -0.7 % | 10 | yes | pass |

## Per cell

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=1,type=aa

- first variant B, seed 31; repeats alternated as drawn: yes
- buffers: A at 0x445500000000, B at 0x445980000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=10,type=aa

- first variant B, seed 31; repeats alternated as drawn: yes
- buffers: A at 0x530140000000, B at 0x530600000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=2,type=aa

- first variant B, seed 31; repeats alternated as drawn: yes
- buffers: A at 0x428f00000000, B at 0x429380000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=3,type=aa

- first variant A, seed 31; repeats alternated as drawn: yes
- buffers: A at 0x5641c0000000, B at 0x564680000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=4,type=aa

- first variant B, seed 31; repeats alternated as drawn: yes
- buffers: A at 0x4f1500000000, B at 0x4f19c0000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.212e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=5,type=aa

- first variant B, seed 31; repeats alternated as drawn: yes
- buffers: A at 0x59f300000000, B at 0x59f780000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=6,type=aa

- first variant B, seed 31; repeats alternated as drawn: yes
- buffers: A at 0x5ac440000000, B at 0x5ac8c0000000
- per repetition: home 5.369e+08 link read bytes and 1.212e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=7,type=aa

- first variant B, seed 31; repeats alternated as drawn: yes
- buffers: A at 0x5b6fc0000000, B at 0x5b7480000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=8,type=aa

- first variant A, seed 31; repeats alternated as drawn: yes
- buffers: A at 0x526700000000, B at 0x526b80000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=16384,kernel=k3,placement=cpu,replicate=9,type=aa

- first variant B, seed 31; repeats alternated as drawn: yes
- buffers: A at 0x5172c0000000, B at 0x517780000000
- per repetition: home 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; level 5.369e+08 link read bytes and 1.211e+08 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=1,type=aa

- first variant A, seed 31; repeats alternated as drawn: yes
- buffers: A at 0x528800000000, B at 0x528ac0000000
- per repetition: home 5.369e+08 link read bytes and 4.436e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.439e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=10,type=aa

- first variant A, seed 31; repeats alternated as drawn: yes
- buffers: A at 0x4ac780000000, B at 0x4aca00000000
- per repetition: home 5.369e+08 link read bytes and 4.434e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.426e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=2,type=aa

- first variant A, seed 31; repeats alternated as drawn: yes
- buffers: A at 0x4f3640000000, B at 0x4f3900000000
- per repetition: home 5.369e+08 link read bytes and 4.425e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.44e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=3,type=aa

- first variant A, seed 31; repeats alternated as drawn: yes
- buffers: A at 0x56c3c0000000, B at 0x56c640000000
- per repetition: home 5.369e+08 link read bytes and 4.427e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.429e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=4,type=aa

- first variant B, seed 31; repeats alternated as drawn: yes
- buffers: A at 0x417e00000000, B at 0x418080000000
- per repetition: home 5.369e+08 link read bytes and 4.423e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.423e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=5,type=aa

- first variant A, seed 31; repeats alternated as drawn: yes
- buffers: A at 0x557240000000, B at 0x557500000000
- per repetition: home 5.369e+08 link read bytes and 4.424e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.443e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=6,type=aa

- first variant A, seed 31; repeats alternated as drawn: yes
- buffers: A at 0x5ff780000000, B at 0x5ffa00000000
- per repetition: home 5.369e+08 link read bytes and 4.423e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.447e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=7,type=aa

- first variant A, seed 31; repeats alternated as drawn: yes
- buffers: A at 0x41d240000000, B at 0x41d500000000
- per repetition: home 5.369e+08 link read bytes and 4.421e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.443e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=8,type=aa

- first variant A, seed 31; repeats alternated as drawn: yes
- buffers: A at 0x48ecc0000000, B at 0x48ef40000000
- per repetition: home 5.369e+08 link read bytes and 4.425e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.429e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=9,type=aa

- first variant B, seed 31; repeats alternated as drawn: yes
- buffers: A at 0x544c80000000, B at 0x544f40000000
- per repetition: home 5.369e+08 link read bytes and 4.434e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.443e+04 SMMU translation requests; multiplexed rows voided: 0

