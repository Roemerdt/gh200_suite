# Measuring-equipment checks

`shakedown timers` prints the timer table (CPU clock, CUDA events, `%globaltimer`: resolution and overhead); `shakedown warmup <s>` runs a sustained load so the SM clock is at its maximum; `shakedown bw <node>` measures the GPU's read bandwidth from a node's memory, the placement gate of every job (GPU memory must beat CPU memory by the factor in `harness/site.env`).
