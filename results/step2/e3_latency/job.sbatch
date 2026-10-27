#!/bin/bash -l
#SBATCH -J step2-e3
#SBATCH -t 00:10:00
#SBATCH -p tutti
#SBATCH -w j21n14
#SBATCH --exclusive
#SBATCH --mem=0
#SBATCH --gres=gpu:1
#SBATCH --chdir=/home/rblom/gh200_route
#SBATCH -o /home/rblom/gh200_route/results/step2/e3_latency/job_%j.out
#SBATCH -e /home/rblom/gh200_route/results/step2/e3_latency/job_%j.out
# Step 2 node check E-3: calibrate the CPU load-latency probe (B-18) and find the state each store
# pattern leaves (C-4). Pilot probe, 5 Oct 2026. Node in the state of A-8 (AutoNUMA on).
SUITE=/home/rblom/gh200_route
source "$SUITE/harness/site.sh"
cd "$SUITE"
D=results/step2/e3_latency
echo "job=$SLURM_JOB_ID node=$(hostname) start=$(date -Is) numa_balancing=$(cat /proc/sys/kernel/numa_balancing) governor=$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor)"
nvcc -O2 -std=c++17 -arch=sm_90 -Isrc -Xcompiler -pthread -Xcompiler -march=armv9-a -o $D/latency $D/latency.cu -ldl
echo "build rc=$?"
./bin/shakedown warmup 5 > $D/warmup_$SLURM_JOB_ID.csv 2>&1
for run in 1 2; do
  $D/latency > $D/latency_p$run.j$SLURM_JOB_ID.csv
  echo "process $run rc=$? rows=$(wc -l < $D/latency_p$run.j$SLURM_JOB_ID.csv)"
done
echo "JOB DONE $(date -Is)"
