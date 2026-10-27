# A/A' cells: two identically prepared direct variants, recomputed from raw rows

Times are per pass in ms. The difference B - A within a repeat is the noise between identically prepared buffers, as median with its 95 % rank interval; its spread over the A/A' cells of a footprint is the floor for translation contrasts there. 'excludes zero' is the interval rule only: resolvability also needs the run-to-run floor from a repeat campaign.

| cell | A ms | B ms | B - A ms [interval] | relative to A | pairs | excludes zero | checks |
|---|---|---|---|---|---|---|---|
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=1,type=aa | 7.8898 | 7.8414 | -0.0468 [-0.0509, -0.0444] | -0.6 % | 10 | yes | pass |
| footprint-mib=8192,kernel=k3,placement=cpu,replicate=2,type=aa | 7.8885 | 7.8439 | -0.0449 [-0.0461, -0.0427] | -0.6 % | 10 | yes | pass |

## Per cell

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=1,type=aa

- first variant B, seed 29; repeats alternated as drawn: yes
- buffers: A at 0x5487c0000000, B at 0x548a80000000
- per repetition: home 5.369e+08 link read bytes and 4.427e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.429e+04 SMMU translation requests; multiplexed rows voided: 0

### route/footprint-mib=8192,kernel=k3,placement=cpu,replicate=2,type=aa

- first variant B, seed 29; repeats alternated as drawn: yes
- buffers: A at 0x5cdf40000000, B at 0x5ce200000000
- per repetition: home 5.369e+08 link read bytes and 4.423e+04 SMMU translation requests; level 5.369e+08 link read bytes and 4.441e+04 SMMU translation requests; multiplexed rows voided: 0

