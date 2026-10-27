#!/bin/bash
# usage: envcapture.sh <outdir>   (run on the compute node)
# Slurm's records of the job, partition and node come from submit.sh on the login node, which has scontrol
OUT=$1; mkdir -p "$OUT"
cap(){ name=$1; shift; { "$@"; } > "$OUT/$name.txt" 2>&1; }
cap uname uname -a
cap date date
cap hostname hostname
cap cmdline cat /proc/cmdline
cap os_release cat /etc/os-release
cap nvidia_version cat /proc/driver/nvidia/version
cap nvidia_params cat /proc/driver/nvidia/params
cap uvm_params grep -rH . /sys/module/nvidia_uvm/parameters/
cap nvidia_smi_q nvidia-smi -q
cap nvidia_smi_topo nvidia-smi topo -m
cap numa_balancing cat /proc/sys/kernel/numa_balancing
cap perf_event_paranoid cat /proc/sys/kernel/perf_event_paranoid
cap interrupts cat /proc/interrupts
cap nvidia_rm_params grep -H . /proc/driver/nvidia/params
cap pmus ls /sys/bus/event_source/devices/
cap nvidia_smi_clocks nvidia-smi --query-gpu=clocks.sm,clocks.applications.graphics,clocks.max.sm,persistence_mode --format=csv
cap thp_enabled cat /sys/kernel/mm/transparent_hugepage/enabled
cap thp_defrag cat /sys/kernel/mm/transparent_hugepage/defrag
cap hugepages grep -H . /sys/kernel/mm/hugepages/*/nr_hugepages /sys/kernel/mm/hugepages/*/free_hugepages
cap meminfo cat /proc/meminfo
cap numactl numactl --hardware
cap lscpu lscpu
cap cpu0_cache grep -H . /sys/devices/system/cpu/cpu0/cache/index*/level /sys/devices/system/cpu/cpu0/cache/index*/type /sys/devices/system/cpu/cpu0/cache/index*/size /sys/devices/system/cpu/cpu0/cache/index*/ways_of_associativity /sys/devices/system/cpu/cpu0/cache/index*/coherency_line_size
cap cpufreq grep -H . /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor /sys/devices/system/cpu/cpu0/cpufreq/scaling_driver /sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
cap page_size getconf PAGE_SIZE
cap modules bash -lc "module list"
cap nvcc_version nvcc --version
cap nvcpp_version nvc++ --version
cap gcc_version gcc --version
cap python_version python3 --version
cap build_flags cat build_flags.txt
if command -v scontrol > /dev/null 2>&1; then
  cap slurm_job scontrol show job "$SLURM_JOB_ID"
  cap slurm_partition scontrol show partition "$SLURM_JOB_PARTITION"
  cap slurm_node scontrol show node "$(hostname)"
else
  echo "scontrol is not installed on the compute node; see env/submit_${SLURM_JOB_ID}.txt (captured on the login node by harness/submit.sh)" > "$OUT/slurm_job.txt"
fi
cap slurm_env env
