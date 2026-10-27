# Crossovers along the axes

Route difference (direct minus copy, ms) per level; signs are given only for resolvable levels (interval excludes zero, above the route floor, replicate agreeing where given). A bracket is reported for every sign change, with its width as a factor, a flag where the frozen tuning differs between its ends, and the factor between the bytes-and-bandwidth model's crossover and the bracket's middle.

| axis | kernel | placement | levels | route difference ms | signs | outcome | brackets | model crossover(s) |
|---|---|---|---|---|---|---|---|---|
| f | k1 | cpu | 1of1000 1of100 1of10 1of2 3of4 9of10 1of1 | -3.253 -2.893 -2.717 -1.697 -1.452 -2.383 -1.576 | - - - - - - - | no sign change on the grid |  |  |
| f | k1 | hbm | 1of1000 1of100 1of10 1of2 3of4 9of10 1of1 | -2.556 -2.551 -2.547 -2.546 -2.542 -2.550 -2.546 | - - - - - - - | no sign change on the grid |  |  |
| footprint | k1 | cpu | 256 1024 4096 8192 16384 24576 32768 | -0.313 -1.576 -0.887 -2.080 -5.327 -8.754 -12.136 | ? - - - - - - | no sign change on the grid |  |  |
| footprint | k1 | hbm | 256 1024 4096 8192 16384 24576 | -0.656 -2.546 -10.108 -20.332 -36.381 -54.586 | ? - - - - - | no sign change on the grid |  |  |
| footprint | k3 | cpu | 256 1024 4096 8192 16384 24576 32768 | 3.696 1.159 -5.505 -13.839 389.969 534.467 600.074 | + + - - + + + | 2 sign change(s) | [1024, 4096] width x4.00; model: no crossover; [8192, 16384] width x2.00; model: no crossover |  |
| footprint | k3 | hbm | 256 1024 4096 8192 16384 24576 | -0.641 -2.548 -5.455 -13.166 385.775 529.363 | ? - - - + + | 1 sign change(s) | [8192, 16384] width x2.00; model: no crossover |  |

## Bisection cells to run

- k3 footprint at cpu placement: level 2048 inside [1024, 4096]
- k3 footprint at cpu placement: level 11520 inside [8192, 16384]
- k3 footprint at hbm placement: level 11520 inside [8192, 16384]
