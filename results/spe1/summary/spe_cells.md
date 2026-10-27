# spe cells

The samples of code in the route binary per cell: the classes with at least 1 % of a cell's samples, and the total latency of their operations in core cycles.

| cell | samples | TLB miss | source | share | p50 | p90 | p99 |
|---|---|---|---|---|---|---|---|
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=atomic | 151334 | 0.000 | all | 1.000 | 8 | 217 | 228 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=atomic | 151334 | 0.000 | LOAD L1 hit | 1.000 | 8 | 217 | 228 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 292342 | 0.000 | all | 1.000 | 14 | 18 | 21 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 292342 | 0.000 | LOAD L1 hit | 0.888 | 14 | 18 | 21 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 292342 | 0.000 | STORE N/A | 0.112 | 14 | 17 | 19 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=returned | 39240 | 0.000 | all | 1.000 | 8 | 168 | 4095 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=returned | 39240 | 0.000 | LOAD L1 hit | 0.910 | 8 | 174 | 4095 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=returned | 39240 | 0.000 | STORE N/A | 0.090 | 9 | 10 | 12 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=stadd | 151352 | 0.000 | all | 1.000 | 46 | 162 | 273 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=stadd | 151352 | 0.000 | LOAD L1 hit | 0.889 | 40 | 150 | 258 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=stadd | 151352 | 0.000 | STORE N/A | 0.111 | 104 | 216 | 358 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=atomic | 151812 | 0.000 | all | 1.000 | 8 | 217 | 228 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=atomic | 151812 | 0.000 | LOAD L1 hit | 1.000 | 8 | 217 | 228 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 292902 | 0.000 | all | 1.000 | 14 | 18 | 22 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 292902 | 0.000 | LOAD L1 hit | 0.889 | 14 | 18 | 22 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 292902 | 0.000 | STORE N/A | 0.111 | 14 | 17 | 20 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=returned | 39377 | 0.000 | all | 1.000 | 8 | 169 | 3351 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=returned | 39377 | 0.000 | LOAD L1 hit | 0.911 | 8 | 174 | 4095 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=returned | 39377 | 0.000 | STORE N/A | 0.089 | 9 | 10 | 11 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=stadd | 151012 | 0.000 | all | 1.000 | 45 | 166 | 288 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=stadd | 151012 | 0.000 | LOAD L1 hit | 0.889 | 39 | 155 | 269 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=stadd | 151012 | 0.000 | STORE N/A | 0.111 | 102 | 223 | 358 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=atomic | 151980 | 0.000 | all | 1.000 | 8 | 218 | 228 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=atomic | 151980 | 0.000 | LOAD L1 hit | 1.000 | 8 | 218 | 228 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 328478 | 0.000 | all | 1.000 | 15 | 19 | 23 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 328478 | 0.000 | LOAD L1 hit | 0.889 | 15 | 19 | 23 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 328478 | 0.000 | STORE N/A | 0.111 | 15 | 18 | 20 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=returned | 94962 | 0.000 | all | 1.000 | 8 | 169 | 4095 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=returned | 94962 | 0.000 | LOAD L1 hit | 0.907 | 8 | 174 | 4095 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=returned | 94962 | 0.000 | STORE N/A | 0.092 | 9 | 10 | 11 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=stadd | 151868 | 0.000 | all | 1.000 | 48 | 166 | 284 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=stadd | 151868 | 0.000 | LOAD L1 hit | 0.890 | 42 | 154 | 265 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=stadd | 151868 | 0.000 | STORE N/A | 0.110 | 109 | 226 | 373 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=atomic | 151854 | 0.000 | all | 1.000 | 8 | 218 | 228 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=atomic | 151854 | 0.000 | LOAD L1 hit | 1.000 | 8 | 218 | 228 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 293490 | 0.000 | all | 1.000 | 14 | 18 | 22 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 293490 | 0.000 | LOAD L1 hit | 0.888 | 14 | 18 | 22 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 293490 | 0.000 | STORE N/A | 0.111 | 14 | 17 | 20 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=returned | 39192 | 0.000 | all | 1.000 | 8 | 169 | 4095 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=returned | 39192 | 0.000 | LOAD L1 hit | 0.905 | 8 | 175 | 4095 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=returned | 39192 | 0.000 | STORE N/A | 0.094 | 9 | 10 | 11 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=stadd | 152215 | 0.000 | all | 1.000 | 48 | 168 | 287 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=stadd | 152215 | 0.000 | LOAD L1 hit | 0.888 | 41 | 155 | 269 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=stadd | 152215 | 0.000 | STORE N/A | 0.112 | 108 | 226 | 367 |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,sharing=shared,type=aa | 3808 | 0.001 | all | 1.000 | 9 | 160 | 305 |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,sharing=shared,type=aa | 3808 | 0.001 | LOAD L1 hit | 0.611 | 8 | 19 | 96 |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,sharing=shared,type=aa | 3808 | 0.001 | STORE N/A | 0.262 | 11 | 23 | 29 |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,sharing=shared,type=aa | 3808 | 0.001 | LOAD L3 miss | 0.069 | 246 | 324 | 620 |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,sharing=shared,type=aa | 3808 | 0.001 | LOAD L3 hit | 0.054 | 165 | 245 | 297 |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,sharing=shared,type=aa | 8776 | 0.000 | all | 1.000 | 16 | 368 | 1040 |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,sharing=shared,type=aa | 8776 | 0.000 | LOAD L1 hit | 0.832 | 14 | 449 | 1012 |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,sharing=shared,type=aa | 8776 | 0.000 | STORE N/A | 0.112 | 7 | 21 | 26 |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,sharing=shared,type=aa | 8776 | 0.000 | LOAD L3 miss | 0.031 | 240 | 1129 | 2126 |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,sharing=shared,type=aa | 8776 | 0.000 | LOAD L3 hit | 0.024 | 150 | 233 | 364 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=atomic | 151621 | 0.000 | all | 1.000 | 8 | 218 | 229 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=atomic | 151621 | 0.000 | LOAD L1 hit | 1.000 | 8 | 218 | 229 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 295050 | 0.000 | all | 1.000 | 15 | 19 | 24 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 295050 | 0.000 | LOAD L1 hit | 0.890 | 15 | 20 | 24 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 295050 | 0.000 | STORE N/A | 0.110 | 15 | 18 | 21 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=returned | 95809 | 0.000 | all | 1.000 | 8 | 172 | 4095 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=returned | 95809 | 0.000 | LOAD L1 hit | 0.909 | 8 | 175 | 4095 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=returned | 95809 | 0.000 | STORE N/A | 0.090 | 9 | 10 | 12 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=stadd | 151991 | 0.000 | all | 1.000 | 48 | 164 | 277 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=stadd | 151991 | 0.000 | LOAD L1 hit | 0.888 | 41 | 152 | 259 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=stadd | 151991 | 0.000 | STORE N/A | 0.112 | 107 | 224 | 350 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=atomic | 151881 | 0.000 | all | 1.000 | 8 | 218 | 229 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=atomic | 151881 | 0.000 | LOAD L1 hit | 1.000 | 8 | 218 | 229 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 295332 | 0.000 | all | 1.000 | 15 | 20 | 24 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 295332 | 0.000 | LOAD L1 hit | 0.888 | 15 | 20 | 24 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 295332 | 0.000 | STORE N/A | 0.112 | 15 | 18 | 21 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=returned | 39380 | 0.000 | all | 1.000 | 8 | 174 | 2755 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=returned | 39380 | 0.000 | LOAD L1 hit | 0.907 | 8 | 175 | 2988 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=returned | 39380 | 0.000 | STORE N/A | 0.092 | 9 | 10 | 12 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=stadd | 151798 | 0.000 | all | 1.000 | 47 | 166 | 286 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=stadd | 151798 | 0.000 | LOAD L1 hit | 0.889 | 41 | 155 | 268 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=stadd | 151798 | 0.000 | STORE N/A | 0.111 | 107 | 223 | 365 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=atomic | 155744 | 0.000 | all | 1.000 | 8 | 217 | 500 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=atomic | 155744 | 0.000 | LOAD L1 hit | 0.999 | 8 | 217 | 501 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 298858 | 0.000 | all | 1.000 | 15 | 19 | 25 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 298858 | 0.000 | LOAD L1 hit | 0.890 | 15 | 20 | 25 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 298858 | 0.000 | STORE N/A | 0.110 | 15 | 18 | 21 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=returned | 99787 | 0.000 | all | 1.000 | 8 | 174 | 4095 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=returned | 99787 | 0.000 | LOAD L1 hit | 0.909 | 8 | 175 | 4095 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=returned | 99787 | 0.000 | STORE N/A | 0.090 | 9 | 11 | 21 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=stadd | 155849 | 0.000 | all | 1.000 | 50 | 185 | 366 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=stadd | 155849 | 0.000 | LOAD L1 hit | 0.890 | 43 | 173 | 336 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=stadd | 155849 | 0.000 | STORE N/A | 0.110 | 115 | 255 | 511 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=atomic | 116291 | 0.000 | all | 1.000 | 8 | 218 | 1237 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=atomic | 116291 | 0.000 | LOAD L1 hit | 0.998 | 8 | 218 | 1239 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 299561 | 0.000 | all | 1.000 | 15 | 20 | 60 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 299561 | 0.000 | LOAD L1 hit | 0.890 | 15 | 20 | 83 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 299561 | 0.000 | STORE N/A | 0.110 | 15 | 18 | 22 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=returned | 99535 | 0.000 | all | 1.000 | 8 | 175 | 4095 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=returned | 99535 | 0.000 | LOAD L1 hit | 0.908 | 8 | 176 | 4095 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=returned | 99535 | 0.000 | STORE N/A | 0.091 | 9 | 11 | 21 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=stadd | 154709 | 0.000 | all | 1.000 | 53 | 227 | 1190 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=stadd | 154709 | 0.000 | LOAD L1 hit | 0.891 | 45 | 211 | 1125 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=stadd | 154709 | 0.000 | STORE N/A | 0.109 | 120 | 330 | 1550 |
| footprint-mib=512,host=reads,kernel=k5,placement=cpu,sharing=shared,sweeps=8,tiling=tiles,type=aa | 32105 | 0.000 | all | 1.000 | 9 | 16 | 306 |
| footprint-mib=512,host=reads,kernel=k5,placement=cpu,sharing=shared,sweeps=8,tiling=tiles,type=aa | 32105 | 0.000 | LOAD L1 hit | 0.823 | 9 | 16 | 343 |
| footprint-mib=512,host=reads,kernel=k5,placement=cpu,sharing=shared,sweeps=8,tiling=tiles,type=aa | 32105 | 0.000 | STORE N/A | 0.145 | 5 | 6 | 15 |
| footprint-mib=512,host=reads,kernel=k5,placement=cpu,sharing=shared,sweeps=8,tiling=tiles,type=aa | 32105 | 0.000 | LOAD L1 miss | 0.032 | 15 | 19 | 22 |
| footprint-mib=512,host=reads,kernel=k5,placement=hbm,sharing=shared,sweeps=8,tiling=tiles,type=aa | 83271 | 0.000 | all | 1.000 | 12 | 429 | 1005 |
| footprint-mib=512,host=reads,kernel=k5,placement=hbm,sharing=shared,sweeps=8,tiling=tiles,type=aa | 83271 | 0.000 | LOAD L1 hit | 0.932 | 13 | 464 | 1018 |
| footprint-mib=512,host=reads,kernel=k5,placement=hbm,sharing=shared,sweeps=8,tiling=tiles,type=aa | 83271 | 0.000 | STORE N/A | 0.055 | 5 | 7 | 16 |
| footprint-mib=512,host=reads,kernel=k5,placement=hbm,sharing=shared,sweeps=8,tiling=tiles,type=aa | 83271 | 0.000 | LOAD L1 miss | 0.013 | 15 | 19 | 24 |
