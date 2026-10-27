#!/bin/bash -l
#SBATCH -J step2-e4
#SBATCH -t 00:10:00
#SBATCH -p tutti
#SBATCH -w j21n14
#SBATCH --exclusive
#SBATCH --mem=0
#SBATCH --gres=gpu:1
#SBATCH --chdir=/home/rblom/gh200_route
#SBATCH -o /home/rblom/gh200_route/results/step2/e4_migration/job_%j.out
#SBATCH -e /home/rblom/gh200_route/results/step2/e4_migration/job_%j.out
# Step 2 node check E-4, PREVIEW: migration pace of unbound memory for a K2-like kernel at 8 GiB, with
# the streaming series of B-13 as control. Pilot probe, 5 Oct 2026. The node ran with AutoNUMA ON
# (PILOT_FINDINGS A-8); the series length for the migration row must come from configuration 1.
SUITE=/home/rblom/gh200_route
source "$SUITE/harness/site.sh"
cd "$SUITE"
D=results/step2/e4_migration
echo "job=$SLURM_JOB_ID node=$(hostname) start=$(date -Is) numa_balancing=$(cat /proc/sys/kernel/numa_balancing) migration_param=$(cat /sys/module/nvidia_uvm/parameters/uvm_perf_access_counter_migration_enable)"
nvcc -O2 -std=c++17 -arch=sm_90 -Isrc -Xcompiler -pthread -Xcompiler -march=armv9-a -o $D/migpace $D/migpace.cu -ldl
echo "build rc=$?"
./bin/shakedown warmup 5 > $D/warmup_$SLURM_JOB_ID.csv 2>&1
$D/migpace > $D/migpace_$SLURM_JOB_ID.csv
echo "rc=$?"
grep -e "^SMs" -e "^RESULT" $D/migpace_$SLURM_JOB_ID.csv
echo "JOB DONE $(date -Is)"
