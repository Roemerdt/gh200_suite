#!/bin/bash -l
#SBATCH -J route-fsweep
#SBATCH -t 00:10:00
#SBATCH -p tutti
#SBATCH -w j21n14
#SBATCH --exclusive
#SBATCH --mem=0
#SBATCH --gres=gpu:1
#SBATCH --chdir=/home/rblom/gh200_route
#SBATCH -o /home/rblom/gh200_route/results/shake2/probe_fsweep/probe_%j.out
#SBATCH -e /home/rblom/gh200_route/results/shake2/probe_fsweep/probe_%j.out
# Trial run of 5 Oct 2026 (node not in configuration 1: AutoNUMA on, PILOT_FINDINGS A-8): the K1
# route cell with the route counter set at the touched fractions the slice phase does not hold.
# Not thesis data. The binary is the committed build; cells are run directly, at most 40 counted repeats.
SUITE=/home/rblom/gh200_route
source "$SUITE/harness/site.sh"
cd "$SUITE"
D=results/shake2/probe_fsweep
EV="nvidia_nvlink_c2c0_pmu_0/rd_req_loc/,nvidia_nvlink_c2c0_pmu_0/rd_bytes_loc/,nvidia_nvlink_c2c0_pmu_0/wr_req_loc/,nvidia_nvlink_c2c0_pmu_0/wr_bytes_loc/,smmuv3_pmcg_16002/pcie_ats_trans_rq/"
echo "fsweep job=$SLURM_JOB_ID node=$(hostname) start=$(date -Is) paranoid=$(cat /proc/sys/kernel/perf_event_paranoid) numa_balancing=$(cat /proc/sys/kernel/numa_balancing)"
./bin/shakedown warmup 10 > $D/warmup_$SLURM_JOB_ID.csv 2>&1
for fr in "1 100" "1 10" "1 4" "3 4" "9 10"; do
  set -- $fr
  ./bin/route run --kernel k1 --placement cpu --footprint-mib 1024 --f-num $1 --f-den $2 --first A --seed 0 --cap 40 --events "$EV" --out $D/route_f$1_$2.j$SLURM_JOB_ID.csv --cell "probe/f-num=$1,f-den=$2" --campaign shake2probe --jobid $SLURM_JOB_ID 2>&1 | tail -1 | cut -c1-260
done
echo "FSWEEP DONE $(date -Is)"
