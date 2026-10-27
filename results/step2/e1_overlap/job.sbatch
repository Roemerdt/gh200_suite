#!/bin/bash -l
#SBATCH -J step2-e1
#SBATCH -t 00:10:00
#SBATCH -p tutti
#SBATCH -w j21n14
#SBATCH --exclusive
#SBATCH --mem=0
#SBATCH --gres=gpu:1
#SBATCH --chdir=/home/rblom/gh200_route
#SBATCH -o /home/rblom/gh200_route/results/step2/e1_overlap/job_%j.out
#SBATCH -e /home/rblom/gh200_route/results/step2/e1_overlap/job_%j.out
# Step 2 node check E-1: replicate B-2 (asynchronous copies beside a kernel) with a kernel on one SM,
# on all SMs, and a memory-reading kernel. Pilot probe, 5 Oct 2026. Node in the state of A-8.
SUITE=/home/rblom/gh200_route
source "$SUITE/harness/site.sh"
cd "$SUITE"
D=results/step2/e1_overlap
echo "job=$SLURM_JOB_ID node=$(hostname) start=$(date -Is) numa_balancing=$(cat /proc/sys/kernel/numa_balancing)"
nvcc -O2 -std=c++17 -arch=sm_90 -Isrc -Xcompiler -pthread -Xcompiler -march=armv9-a -o $D/overlap $D/overlap.cu -ldl
echo "build rc=$?"
./bin/shakedown warmup 10 > $D/warmup_$SLURM_JOB_ID.csv 2>&1
for run in 1 2; do
  echo "##### process $run"
  $D/overlap > $D/overlap_p$run.j$SLURM_JOB_ID.txt
  echo "rc=$?"
  sed -n '1,3p;/^medians/,$p' $D/overlap_p$run.j$SLURM_JOB_ID.txt
done
echo "JOB DONE $(date -Is)"
