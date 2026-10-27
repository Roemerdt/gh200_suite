#!/bin/bash -l
#SBATCH -J step2-e2
#SBATCH -t 00:10:00
#SBATCH -p tutti
#SBATCH -w j21n14
#SBATCH --exclusive
#SBATCH --mem=0
#SBATCH --gres=gpu:1
#SBATCH --chdir=/home/rblom/gh200_route
#SBATCH -o /home/rblom/gh200_route/results/step2/e2_population/job_%j.out
#SBATCH -e /home/rblom/gh200_route/results/step2/e2_population/job_%j.out
# Step 2 node check E-2: replicate the population check behind B-10 (page size obtained when the GPU
# populates a mapping with MADV_HUGEPAGE). Pilot probe, 5 Oct 2026. Node in the state of A-8: the
# unbound rows run with AutoNUMA on.
SUITE=/home/rblom/gh200_route
source "$SUITE/harness/site.sh"
cd "$SUITE"
D=results/step2/e2_population
echo "job=$SLURM_JOB_ID node=$(hostname) start=$(date -Is) numa_balancing=$(cat /proc/sys/kernel/numa_balancing)"
echo "thp: $(cat /sys/kernel/mm/transparent_hugepage/enabled) defrag: $(cat /sys/kernel/mm/transparent_hugepage/defrag) khugepaged defrag: $(cat /sys/kernel/mm/transparent_hugepage/khugepaged/defrag) pages_to_scan: $(cat /sys/kernel/mm/transparent_hugepage/khugepaged/pages_to_scan) scan_sleep_ms: $(cat /sys/kernel/mm/transparent_hugepage/khugepaged/scan_sleep_millisecs) use_zero_page: $(cat /sys/kernel/mm/transparent_hugepage/use_zero_page)"
nvcc -O2 -std=c++17 -arch=sm_90 -Isrc -Xcompiler -pthread -Xcompiler -march=armv9-a -o $D/pop $D/pop.cu -ldl
echo "build rc=$?"
$D/pop > $D/pop_$SLURM_JOB_ID.csv
echo "rc=$?"
cat $D/pop_$SLURM_JOB_ID.csv
echo "JOB DONE $(date -Is)"
