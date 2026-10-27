#!/bin/bash -l
#SBATCH -J route-step0
#SBATCH -t 00:10:00
#SBATCH -p tutti
#SBATCH -w j21n14
#SBATCH --gpus=1
#SBATCH --mem=16G
#SBATCH --cpus-per-task=4
#SBATCH --chdir=/home/rblom/gh200_route
#SBATCH -o /home/rblom/gh200_route/results/step0/step0_%j.out
#SBATCH -e /home/rblom/gh200_route/results/step0/step0_%j.out
# Step 0 of docs/HANDOFF_IMPLEMENTATION.md: the node's configuration after the firmware update
# (SURF ticket SOIL-756), to compare with PILOT_FINDINGS.md A-1. Short non-exclusive probe.
# Reads only, except the administrator-settings check, which runs one minimal CUDA kernel and a
# 5 s clock check under load (the script of 17 Sep, unchanged).
SUITE=/home/rblom/gh200_route
source "$SUITE/harness/site.sh"
cd "$SUITE"
X=results/step0/env/${SLURM_JOB_ID}_a0
echo "step0 job=$SLURM_JOB_ID node=$(hostname) start=$(date -Is)"
# 1. the suite's environment capture (FR-10), unchanged
bash harness/envcapture.sh "$X"
# 2. items of A-1 and of the handoff's list that envcapture.sh does not record
cap(){ name=$1; shift; { "$@"; } > "$X/$name.txt" 2>&1; }
cap x_addressing bash -c "nvidia-smi -q | grep -i -E 'Addressing Mode|Compute Mode|Persistence Mode|VBIOS Version|Firmware|GSP|Driver Version|CUDA Version|Product Name|Image Version|Inforom|OEM Object|ECC Object'"
cap x_gpu_query nvidia-smi --query-gpu=name,driver_version,vbios_version,memory.total,memory.used,clocks.max.sm,clocks.sm,persistence_mode,compute_mode --format=csv
cap x_mthp bash -c 'ls /sys/kernel/mm/transparent_hugepage/; for d in /sys/kernel/mm/transparent_hugepage/hugepages-*; do echo "$d: $(cat $d/enabled 2>&1)"; done'
cap x_thp_misc bash -c 'grep -H . /sys/kernel/mm/transparent_hugepage/hpage_pmd_size /sys/kernel/mm/transparent_hugepage/khugepaged/defrag /sys/kernel/mm/transparent_hugepage/use_zero_page /sys/kernel/mm/transparent_hugepage/shmem_enabled 2>&1'
cap x_meminfo_huge grep -i huge /proc/meminfo
cap x_dmi bash -c 'grep -H . /sys/class/dmi/id/bios_version /sys/class/dmi/id/bios_date /sys/class/dmi/id/bios_release /sys/class/dmi/id/bios_vendor /sys/class/dmi/id/ec_firmware_release /sys/class/dmi/id/product_name /sys/class/dmi/id/product_version /sys/class/dmi/id/board_name /sys/class/dmi/id/board_version 2>&1'
cap x_kernel_config bash -c 'zcat /proc/config.gz 2>&1 | grep -E "INIT_ON_ALLOC_DEFAULT_ON|CONFIG_ARM64_64K_PAGES|ARM_SMMU_V3_PMU|CONFIG_NUMA_BALANCING|CONFIG_TRANSPARENT_HUGEPAGE"'
cap x_pmu_events bash -c 'for p in nvidia_nvlink_c2c0_pmu_0 nvidia_nvlink_c2c1_pmu_0 nvidia_scf_pmu_0 smmuv3_pmcg_16002; do echo "== $p cpumask=$(cat /sys/bus/event_source/devices/$p/cpumask 2>&1) type=$(cat /sys/bus/event_source/devices/$p/type 2>&1)"; ls /sys/bus/event_source/devices/$p/events 2>&1 | tr "\n" " "; echo; done'
cap x_tools bash -c 'which ncu nsys perf cuobjdump numactl objdump 2>&1; perf --version 2>&1; ncu --version 2>&1 | head -3'
cap x_boot bash -c 'uptime; who -b 2>&1; cat /proc/uptime'
cap x_sysctl bash -c 'grep -H . /proc/sys/vm/zone_reclaim_mode /proc/sys/vm/overcommit_memory /proc/sys/vm/compaction_proactiveness /proc/sys/vm/watermark_scale_factor /proc/sys/kernel/numa_balancing /proc/sys/kernel/perf_event_paranoid /proc/sys/kernel/kptr_restrict /proc/sys/kernel/randomize_va_space 2>&1'
cap x_uvm_procfs bash -c 'ls -la /proc/driver/nvidia-uvm/ 2>&1; ls /proc/driver/nvidia-uvm/gpus/ 2>&1'
cap x_node_meminfo bash -c 'grep -H -E "MemTotal|MemFree|AnonHugePages|HugePages_Total" /sys/devices/system/node/node0/meminfo /sys/devices/system/node/node1/meminfo 2>&1'
# 3. the administrator settings of 17 Sep, checked functionally (perf on the uncore PMUs, ncu, fault_stats, clock under load)
bash /home/rblom/check-sysadmin-j21n14.sh > "$X/x_check_sysadmin.txt" 2>&1
cat "$X/x_check_sysadmin.txt"
echo "STEP0 DONE $(date -Is) files=$(ls "$X" | wc -l)"
