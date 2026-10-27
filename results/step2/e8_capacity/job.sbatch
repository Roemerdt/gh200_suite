#!/bin/bash -l
#SBATCH -J step2-e8
#SBATCH -t 00:10:00
#SBATCH -p tutti
#SBATCH -w j21n14
#SBATCH --exclusive
#SBATCH --mem=0
#SBATCH --gres=gpu:1
#SBATCH --chdir=/home/rblom/gh200_route
#SBATCH -o /home/rblom/gh200_route/results/step2/e8_capacity/job_%j.out
#SBATCH -e /home/rblom/gh200_route/results/step2/e8_capacity/job_%j.out
# Node check E-8: how much node-1 memory a process can bind and touch (64 KB and 512 MB pages), what
# the node, the cgroup and CUDA report along the way, and how fast freed memory comes back.
# Written 7 Oct 2026 after two cells of campaign cal1 were OOM-killed on node 1 (jobs 239892).
SUITE=/home/rblom/gh200_route
source "$SUITE/harness/site.sh"
cd "$SUITE"
D=results/step2/e8_capacity
echo "job=$SLURM_JOB_ID node=$(hostname) start=$(date -Is)"
echo "slurm mem: SLURM_MEM_PER_NODE=$SLURM_MEM_PER_NODE"
nvcc -O2 -std=c++17 -arch=sm_90 -o $D/capacity $D/capacity.cpp -x cu
echo "build rc=$?"
echo "===== 64 KB pages, 8 GiB steps to 96 GiB"
$D/capacity 8 96 0
echo "rc=$?"
echo "===== 512 MB pages, 8 GiB steps to 96 GiB"
$D/capacity 8 96 1
echo "rc=$?"
echo "===== 512 MB pages again, right after (release lag)"
$D/capacity 16 80 1
echo "rc=$?"
echo "JOB DONE $(date -Is)"
