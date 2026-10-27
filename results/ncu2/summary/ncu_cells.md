# ncu cells

One variant's pass under Nsight Compute, summed over its launches; per-unit values per touched line, gather or update.

| cell | variant | launches | unit | units/pass | L1 hit % | shmem config | ld req/unit | ld sect/unit | L2 read sect/unit | L2 hit/unit | DRAM read/unit | RED/unit (sysmem, device) | ATOM/unit (sysmem, device) | sysmem read/unit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| footprint-mib=1024,k=1,kernel=k2,placement=cpu,variant=A,working-set-mib=128 | A | 1 | line | 1048476 | 0.0 | 135168 | 0.250 | 4.000 | 4.000 | 0.000 | 0.000 | 0.000 (0.000, 0.000) | 0.000 (0.000, 0.000) | 6.000 |
| footprint-mib=1024,k=1,kernel=k2,placement=cpu,variant=A,working-set-mib=32 | A | 1 | line | 262020 | 0.0 | 135168 | 0.250 | 4.000 | 4.000 | 0.000 | 0.000 | 0.000 (0.000, 0.000) | 0.000 (0.000, 0.000) | 6.000 |
| footprint-mib=1024,k=1,kernel=k2,placement=cpu,variant=A,working-set-mib=64 | A | 1 | line | 524172 | 0.0 | 135168 | 0.250 | 4.000 | 4.000 | 0.000 | 0.000 | 0.000 (0.000, 0.000) | 0.000 (0.000, 0.000) | 6.000 |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,variant=A,working-set-mib=128 | A | 1 | line | 1048476 | 0.0 | 135168 | 4.001 | 64.000 | 64.000 | 0.000 | 0.000 | 0.000 (0.000, 0.000) | 0.000 (0.000, 0.000) | 95.998 |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,variant=A,working-set-mib=32 | A | 1 | line | 262020 | 0.0 | 135168 | 4.006 | 64.000 | 63.995 | 0.000 | 0.000 | 0.000 (0.000, 0.000) | 0.000 (0.000, 0.000) | 96.000 |
| footprint-mib=1024,k=16,kernel=k2,placement=cpu,variant=A,working-set-mib=64 | A | 1 | line | 524172 | 0.0 | 135168 | 4.001 | 64.000 | 64.000 | 0.000 | 0.000 | 0.000 (0.000, 0.000) | 0.000 (0.000, 0.000) | 95.999 |
| footprint-mib=1024,k=2,kernel=k2,placement=cpu,variant=A,working-set-mib=128 | A | 1 | line | 1048476 | 0.0 | 135168 | 0.500 | 8.000 | 8.000 | 0.000 | 0.000 | 0.000 (0.000, 0.000) | 0.000 (0.000, 0.000) | 12.000 |
| footprint-mib=1024,k=2,kernel=k2,placement=cpu,variant=A,working-set-mib=32 | A | 1 | line | 262020 | 0.0 | 135168 | 0.501 | 8.000 | 8.000 | 0.000 | 0.000 | 0.000 (0.000, 0.000) | 0.000 (0.000, 0.000) | 12.000 |
| footprint-mib=1024,k=2,kernel=k2,placement=cpu,variant=A,working-set-mib=64 | A | 1 | line | 524172 | 0.0 | 135168 | 0.500 | 8.000 | 8.000 | 0.000 | 0.000 | 0.000 (0.000, 0.000) | 0.000 (0.000, 0.000) | 12.001 |
| footprint-mib=1024,k=4,kernel=k2,placement=cpu,variant=A,working-set-mib=128 | A | 1 | line | 1048476 | 0.0 | 135168 | 1.000 | 16.000 | 16.000 | 0.000 | 0.000 | 0.000 (0.000, 0.000) | 0.000 (0.000, 0.000) | 24.001 |
| footprint-mib=1024,k=4,kernel=k2,placement=cpu,variant=A,working-set-mib=32 | A | 1 | line | 262020 | 0.0 | 135168 | 1.002 | 16.000 | 16.000 | 0.000 | 0.000 | 0.000 (0.000, 0.000) | 0.000 (0.000, 0.000) | 23.998 |
| footprint-mib=1024,k=4,kernel=k2,placement=cpu,variant=A,working-set-mib=64 | A | 1 | line | 524172 | 0.0 | 135168 | 1.000 | 16.000 | 16.000 | 0.000 | 0.000 | 0.000 (0.000, 0.000) | 0.000 (0.000, 0.000) | 23.999 |
| footprint-mib=1024,k=64,kernel=k2,placement=cpu,variant=A,working-set-mib=128 | A | 1 | line | 1048476 | 0.0 | 135168 | 16.002 | 256.000 | 256.000 | 0.000 | 0.001 | 0.000 (0.000, 0.000) | 0.000 (0.000, 0.000) | 384.007 |
| footprint-mib=1024,k=64,kernel=k2,placement=cpu,variant=A,working-set-mib=32 | A | 1 | line | 262020 | 0.1 | 135168 | 16.024 | 256.000 | 255.833 | 0.000 | 0.001 | 0.000 (0.000, 0.000) | 0.000 (0.000, 0.000) | 383.643 |
| footprint-mib=1024,k=64,kernel=k2,placement=cpu,variant=A,working-set-mib=64 | A | 1 | line | 524172 | 0.0 | 135168 | 16.004 | 256.000 | 256.000 | 0.000 | 0.000 | 0.000 (0.000, 0.000) | 0.000 (0.000, 0.000) | 383.979 |
