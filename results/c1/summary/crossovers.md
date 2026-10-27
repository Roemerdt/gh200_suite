# Crossovers along the axes

Route difference (direct minus copy, ms) per level; signs are given only for resolvable levels (interval excludes zero, above the route floor, replicate agreeing where given). A bracket is reported for every sign change, with its width as a factor, a flag where the frozen tuning differs between its ends, and the factor between the bytes-and-bandwidth model's crossover and the bracket's middle.

| axis | kernel | placement | levels | route difference ms | signs | outcome | brackets | model crossover(s) |
|---|---|---|---|---|---|---|---|---|
| f | k1 | cpu | 1of1000 1of100 1of10 1of2 3of4 9of10 1of1 | -0.002 -0.014 -0.059 -0.156 -1.013 -0.608 -0.360 | ? ? ? ? - ? ? | no sign change on the grid |  |  |
| f | k1 | hbm | 1of1000 1of100 1of10 1of2 3of4 9of10 1of1 | -0.006 -0.023 -0.086 -0.355 -0.512 -0.601 -0.648 | ? ? ? ? ? ? ? | not resolvable |  |  |
| footprint | k1 | cpu | 256 1024 4096 8192 16384 19456 23296 24576 32768 | -0.129 -0.360 -0.946 0.088 -0.889 0.073 2.971 0.187 2.859 | ? ? - ? - ? ? ? + | 1 sign change(s) | [16384, 32768] width x2.00 (tuning changes inside: 4224x512x8, ce-registered-1-256m-pipe-whole, ce-registered-2-256m-pipe-whole); model: no crossover |  |
| footprint | k1 | hbm | 256 1024 4096 8192 16384 24576 | -0.654 -0.648 -2.499 -4.990 -8.915 -13.052 | ? ? - - - - | no sign change on the grid |  |  |
| footprint | k3 | cpu | 256 1024 1536 2048 4096 8192 9728 11520 16384 24576 32768 | 4.162 1.916 0.536 -0.839 -6.371 -15.738 101.084 207.597 385.880 529.757 598.032 | + + ? - - - + + + + + | 2 sign change(s) | [1024, 2048] width x2.00; model: no crossover; [8192, 9728] width x1.19 (tuning changes inside: 2112x128x8, ce-pageable-1-whole-none-whole, kernel-registered-1-whole-none-whole); model: no crossover |  |
| footprint | k3 | hbm | 256 1024 4096 8192 16384 24576 | -0.654 -0.650 2.097 2.242 415.037 574.256 | ? ? + + + + | no sign change on the grid |  |  |
| footprint | k4 | cpu | 256 1024 4096 8192 16384 24576 32768 | 6.370 26.656 111.358 222.804 435.319 678.221 880.633 | + + + + + + + | no sign change on the grid |  |  |
| footprint | k4 | hbm | 256 1024 4096 8192 16384 | -0.677 -0.496 -2.505 -5.064 -10.129 | ? ? - - - | no sign change on the grid |  |  |
| k | k2 | cpu | 1 2 4 16 64 | -0.028 0.058 0.240 1.313 5.577 | ? ? ? + + | no sign change on the grid |  | 1.306 |
| k | k2 | hbm | 1 2 4 16 64 | -0.101 -0.099 -0.099 -0.080 -0.032 | ? ? ? ? ? | not resolvable |  |  |
| sweeps | k5 | cpu | 1 2 4 8 16 64 | 0.006 2.730 8.575 19.778 42.829 185.824 | ? + + + + + | no sign change on the grid |  | 1.104 |
| sweeps | k5 | hbm | 1 2 4 8 16 64 | -0.650 -0.635 -0.616 -0.619 -0.571 -0.177 | ? ? ? ? ? ? | not resolvable |  |  |
