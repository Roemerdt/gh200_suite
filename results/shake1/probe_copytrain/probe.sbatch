#!/bin/bash -l
#SBATCH -J route-probe
#SBATCH -t 00:10:00
#SBATCH -p tutti
#SBATCH -w j21n14
#SBATCH --exclusive
#SBATCH --mem=0
#SBATCH --gres=gpu:1
#SBATCH --chdir=/home/rblom/gh200_route
#SBATCH -o /home/rblom/gh200_route/results/shake1/probe_copytrain/probe_%j.out
#SBATCH -e /home/rblom/gh200_route/results/shake1/probe_copytrain/probe_%j.out
# Pilot probe of the shake-down (5 Oct 2026): why do some back-to-back copy-route calls of the K1
# cell at f = 1/2 take about 1.95 ms longer? Node not in configuration 1 (PILOT_FINDINGS A-7).
SUITE=/home/rblom/gh200_route
source "$SUITE/harness/site.sh"
cd "$SUITE"
D=results/shake1/probe_copytrain
echo "probe job=$SLURM_JOB_ID node=$(hostname) start=$(date -Is)"
nvcc -O2 -std=c++17 -arch=sm_90 -Isrc -Xcompiler -pthread -Xcompiler -march=armv9-a -o $D/copytrain $D/copytrain.cu -ldl
./bin/shakedown warmup 10 > $D/warmup_$SLURM_JOB_ID.csv 2>&1
echo "=== copytrain: 40 trains of 7 calls per configuration, host clock per call ==="
$D/copytrain $D/copytrain_$SLURM_JOB_ID.csv
echo "=== the instrument itself at more touched fractions (at most 40 counted repeats) ==="
for fr in "1 1 A" "9 10 A" "3 4 A" "1 2 A" "1 2 B" "1 4 A" "1 10 A"; do
  set -- $fr
  ./bin/route run --kernel k1 --placement cpu --footprint-mib 1024 --f-num $1 --f-den $2 --first $3 --seed 0 --cap 40 --out $D/route_f$1_$2_first$3.j$SLURM_JOB_ID.csv --cell "probe/f-num=$1,f-den=$2,first=$3" --campaign shake1probe --jobid $SLURM_JOB_ID 2>&1 | tail -1
done
echo "PROBE DONE $(date -Is)"
