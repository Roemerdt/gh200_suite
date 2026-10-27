#!/bin/bash -l
#SBATCH -J route-probe2
#SBATCH -t 00:10:00
#SBATCH -p tutti
#SBATCH -w j21n14
#SBATCH --exclusive
#SBATCH --mem=0
#SBATCH --gres=gpu:1
#SBATCH --chdir=/home/rblom/gh200_route
#SBATCH -o /home/rblom/gh200_route/results/shake1/probe_copytrain/probe2_%j.out
#SBATCH -e /home/rblom/gh200_route/results/shake1/probe_copytrain/probe2_%j.out
# Second pilot probe of the shake-down (5 Oct 2026): does direct access in the same process switch the
# pageable copy-in into its slow mode, and which counters move? Node not in configuration 1 (A-7).
SUITE=/home/rblom/gh200_route
source "$SUITE/harness/site.sh"
cd "$SUITE"
D=results/shake1/probe_copytrain
echo "probe2 job=$SLURM_JOB_ID node=$(hostname) start=$(date -Is)"
nvcc -O2 -std=c++17 -arch=sm_90 -Isrc -Xcompiler -pthread -Xcompiler -march=armv9-a -o $D/copytrain2 $D/copytrain2.cu -ldl
./bin/shakedown warmup 10 > $D/warmup_$SLURM_JOB_ID.csv 2>&1
echo "=== run 1 ==="
$D/copytrain2
echo "=== run 2 (a second process) ==="
$D/copytrain2
echo "PROBE2 DONE $(date -Is)"
