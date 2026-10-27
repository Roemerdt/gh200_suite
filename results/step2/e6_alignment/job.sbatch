#!/bin/bash -l
#SBATCH -J step2-e6
#SBATCH -t 00:10:00
#SBATCH -p tutti
#SBATCH -w j21n14
#SBATCH --exclusive
#SBATCH --mem=0
#SBATCH --gres=gpu:1
#SBATCH --chdir=/home/rblom/gh200_route
#SBATCH -o /home/rblom/gh200_route/results/step2/e6_alignment/job_%j.out
#SBATCH -e /home/rblom/gh200_route/results/step2/e6_alignment/job_%j.out
# Step 2 node check E-6: a first look at C-1 (start address and translation at 8 GiB) and C-2 (spread
# among fast buffers by population recipe), with the address controlled. Pilot probe, 5 Oct 2026.
# Node in the state of A-8 (AutoNUMA on; the buffers are bound to node 0).
SUITE=/home/rblom/gh200_route
source "$SUITE/harness/site.sh"
cd "$SUITE"
D=results/step2/e6_alignment
echo "job=$SLURM_JOB_ID node=$(hostname) start=$(date -Is) numa_balancing=$(cat /proc/sys/kernel/numa_balancing) paranoid=$(cat /proc/sys/kernel/perf_event_paranoid)"
cat /proc/buddyinfo
nvcc -O2 -std=c++17 -arch=sm_90 -Isrc -Xcompiler -pthread -Xcompiler -march=armv9-a -o $D/align $D/align.cu -ldl
echo "build rc=$?"
./bin/shakedown warmup 5 > $D/warmup_$SLURM_JOB_ID.csv 2>&1
for run in 1 2 3; do
  $D/align > $D/align_p$run.j$SLURM_JOB_ID.csv
  echo "process $run rc=$? rows=$(wc -l < $D/align_p$run.j$SLURM_JOB_ID.csv)"
done
cat /proc/buddyinfo
echo "JOB DONE $(date -Is)"
