# spe cells

The samples of the measured loop in the cell's input and output: the classes with at least 1 % of a cell's samples, and the total latency of their operations in core cycles.

| cell | samples | TLB miss | source | share | p50 | p90 | p99 |
|---|---|---|---|---|---|---|---|
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=atomic | 8349 | 0.000 | all | 1.000 | 224 | 228 | 232 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=atomic | 8349 | 0.000 | input LOAD L1 hit | 1.000 | 224 | 228 | 232 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 32675 | 0.000 | all | 1.000 | 15 | 19 | 23 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 32675 | 0.000 | input STORE N/A | 0.503 | 14 | 17 | 20 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 32675 | 0.000 | input LOAD L1 hit | 0.497 | 17 | 20 | 24 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=returned | 4335 | 0.000 | all | 1.000 | 177 | 181 | 4095 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=returned | 4335 | 0.000 | input LOAD L1 hit | 1.000 | 177 | 181 | 4095 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=stadd | 8537 | 0.000 | all | 1.000 | 110 | 220 | 380 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=stadd | 8537 | 0.000 | input STORE N/A | 1.000 | 110 | 220 | 380 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=atomic | 8334 | 0.000 | all | 1.000 | 224 | 228 | 232 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=atomic | 8334 | 0.000 | input LOAD L1 hit | 1.000 | 224 | 228 | 232 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 32403 | 0.000 | all | 1.000 | 15 | 19 | 22 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 32403 | 0.000 | input STORE N/A | 0.502 | 14 | 17 | 19 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 32403 | 0.000 | input LOAD L1 hit | 0.498 | 17 | 20 | 23 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=returned | 1718 | 0.000 | all | 1.000 | 177 | 362 | 4095 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=returned | 1718 | 0.000 | input LOAD L1 hit | 1.000 | 177 | 362 | 4095 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=stadd | 8533 | 0.000 | all | 1.000 | 103 | 226 | 353 |
| footprint-mib=0.0625,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=stadd | 8533 | 0.000 | input STORE N/A | 1.000 | 103 | 226 | 353 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=atomic | 8482 | 0.000 | all | 1.000 | 225 | 228 | 230 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=atomic | 8482 | 0.000 | input LOAD L1 hit | 1.000 | 225 | 228 | 230 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 32414 | 0.000 | all | 1.000 | 16 | 20 | 23 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 32414 | 0.000 | input STORE N/A | 0.502 | 15 | 17 | 20 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 32414 | 0.000 | input LOAD L1 hit | 0.498 | 18 | 21 | 24 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=returned | 1873 | 0.000 | all | 1.000 | 177 | 239 | 4095 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=returned | 1873 | 0.000 | input LOAD L1 hit | 1.000 | 177 | 239 | 4095 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=stadd | 8483 | 0.000 | all | 1.000 | 108 | 224 | 376 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=stadd | 8483 | 0.000 | input STORE N/A | 1.000 | 108 | 224 | 376 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=atomic | 8368 | 0.000 | all | 1.000 | 225 | 228 | 229 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=atomic | 8368 | 0.000 | input LOAD L1 hit | 1.000 | 225 | 228 | 229 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 32634 | 0.000 | all | 1.000 | 16 | 20 | 24 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 32634 | 0.000 | input LOAD L1 hit | 0.501 | 17 | 21 | 25 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 32634 | 0.000 | input STORE N/A | 0.499 | 15 | 17 | 20 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=returned | 1810 | 0.000 | all | 1.000 | 177 | 180 | 4095 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=returned | 1810 | 0.000 | input LOAD L1 hit | 1.000 | 177 | 180 | 4095 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=stadd | 8413 | 0.000 | all | 1.000 | 109 | 230 | 371 |
| footprint-mib=1,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=stadd | 8413 | 0.000 | input STORE N/A | 1.000 | 109 | 230 | 371 |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,sharing=shared,type=aa | 26 | 0.000 | all | 1.000 | 16 | 96 | 178 |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=cpu,sharing=shared,type=aa | 26 | 0.000 | output LOAD L1 hit | 1.000 | 16 | 96 | 178 |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,sharing=shared,type=aa | 1451 | 0.000 | all | 1.000 | 64 | 641 | 1002 |
| footprint-mib=1024,generator=uniform,host=reads,kernel=k4,placement=hbm,sharing=shared,type=aa | 1451 | 0.000 | output LOAD L1 hit | 1.000 | 64 | 641 | 1002 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=atomic | 8348 | 0.000 | all | 1.000 | 226 | 229 | 383 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=atomic | 8348 | 0.000 | input LOAD L1 hit | 1.000 | 226 | 229 | 383 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 32796 | 0.000 | all | 1.000 | 17 | 22 | 27 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 32796 | 0.000 | input LOAD L1 hit | 0.501 | 19 | 23 | 28 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 32796 | 0.000 | input STORE N/A | 0.498 | 15 | 19 | 22 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=returned | 4432 | 0.000 | all | 1.000 | 177 | 361 | 4095 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=returned | 4432 | 0.000 | input LOAD L1 hit | 1.000 | 177 | 361 | 4095 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=stadd | 8479 | 0.000 | all | 1.000 | 109 | 225 | 372 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=stadd | 8479 | 0.000 | input STORE N/A | 1.000 | 109 | 225 | 372 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=atomic | 8273 | 0.000 | all | 1.000 | 226 | 228 | 374 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=atomic | 8273 | 0.000 | input LOAD L1 hit | 1.000 | 226 | 228 | 374 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 32454 | 0.000 | all | 1.000 | 17 | 21 | 25 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 32454 | 0.000 | input STORE N/A | 0.504 | 15 | 18 | 21 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 32454 | 0.000 | input LOAD L1 hit | 0.496 | 19 | 22 | 27 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=returned | 4376 | 0.000 | all | 1.000 | 177 | 421 | 4095 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=returned | 4376 | 0.000 | input LOAD L1 hit | 1.000 | 177 | 421 | 4095 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=stadd | 8359 | 0.000 | all | 1.000 | 110 | 227 | 374 |
| footprint-mib=16,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=stadd | 8359 | 0.000 | input STORE N/A | 1.000 | 110 | 227 | 374 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=atomic | 8344 | 0.000 | all | 1.000 | 226 | 344 | 924 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=atomic | 8344 | 0.000 | input LOAD L1 hit | 1.000 | 226 | 344 | 924 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 32535 | 0.000 | all | 1.000 | 17 | 21 | 27 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 32535 | 0.000 | input STORE N/A | 0.504 | 15 | 18 | 21 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=plain | 32535 | 0.000 | input LOAD L1 hit | 0.496 | 18 | 22 | 47 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=returned | 4265 | 0.000 | all | 1.000 | 177 | 1490 | 4095 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=returned | 4265 | 0.000 | input LOAD L1 hit | 1.000 | 177 | 1490 | 4095 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=stadd | 8474 | 0.000 | all | 1.000 | 120 | 262 | 566 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=cpu,type=aa,update=stadd | 8474 | 0.000 | input STORE N/A | 1.000 | 120 | 262 | 566 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=atomic | 8370 | 0.000 | all | 1.000 | 226 | 744 | 2040 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=atomic | 8370 | 0.000 | input LOAD L1 hit | 1.000 | 226 | 744 | 2040 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 32556 | 0.000 | all | 1.000 | 17 | 22 | 171 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 32556 | 0.000 | input LOAD L1 hit | 0.500 | 19 | 25 | 305 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=plain | 32556 | 0.000 | input STORE N/A | 0.500 | 15 | 19 | 22 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=returned | 4398 | 0.000 | all | 1.000 | 177 | 1790 | 4095 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=returned | 4398 | 0.000 | input LOAD L1 hit | 1.000 | 177 | 1790 | 4095 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=stadd | 8309 | 0.000 | all | 1.000 | 124 | 334 | 1571 |
| footprint-mib=256,issuer=cpu,kernel=k6,placement=hbm,type=aa,update=stadd | 8309 | 0.000 | input STORE N/A | 1.000 | 124 | 334 | 1571 |
| footprint-mib=512,host=reads,kernel=k5,placement=cpu,sharing=shared,sweeps=8,tiling=tiles,type=aa | 1744 | 0.000 | all | 1.000 | 12 | 110 | 227 |
| footprint-mib=512,host=reads,kernel=k5,placement=cpu,sharing=shared,sweeps=8,tiling=tiles,type=aa | 1744 | 0.000 | output LOAD L1 hit | 1.000 | 12 | 110 | 227 |
| footprint-mib=512,host=reads,kernel=k5,placement=hbm,sharing=shared,sweeps=8,tiling=tiles,type=aa | 25169 | 0.000 | all | 1.000 | 57 | 591 | 1070 |
| footprint-mib=512,host=reads,kernel=k5,placement=hbm,sharing=shared,sweeps=8,tiling=tiles,type=aa | 25169 | 0.000 | output LOAD L1 hit | 1.000 | 57 | 591 | 1070 |
