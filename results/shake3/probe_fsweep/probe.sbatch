#!/bin/bash -l
#SBATCH -J route-fsweep
#SBATCH -t 00:10:00
#SBATCH -p tutti
#SBATCH -w j21n14
#SBATCH --exclusive
#SBATCH --mem=0
#SBATCH --gres=gpu:1
#SBATCH --chdir=/home/rblom/gh200_route
#SBATCH -o /home/rblom/gh200_route/results/shake3/probe_fsweep/probe_%j.out
#SBATCH -e /home/rblom/gh200_route/results/shake3/probe_fsweep/probe_%j.out
# Check of the calibration fix (commit 358015c) on the node, 5 Oct 2026. Node not in configuration 1
# (PILOT_FINDINGS A-8). Not thesis data. Seven touched fractions, three processes each, so that some
# processes meet a slow copy call in calibration. Cells are run directly with the route counter set.
SUITE=/home/rblom/gh200_route
source "$SUITE/harness/site.sh"
cd "$SUITE"
D=results/shake3/probe_fsweep
EV="nvidia_nvlink_c2c0_pmu_0/rd_req_loc/,nvidia_nvlink_c2c0_pmu_0/rd_bytes_loc/,nvidia_nvlink_c2c0_pmu_0/wr_req_loc/,nvidia_nvlink_c2c0_pmu_0/wr_bytes_loc/,smmuv3_pmcg_16002/pcie_ats_trans_rq/"
echo "fsweep job=$SLURM_JOB_ID node=$(hostname) start=$(date -Is) paranoid=$(cat /proc/sys/kernel/perf_event_paranoid) numa_balancing=$(cat /proc/sys/kernel/numa_balancing)"
./bin/shakedown warmup 10 > $D/warmup_$SLURM_JOB_ID.csv 2>&1
for round in 1 2 3; do
  for fr in "1 100" "1 10" "1 4" "1 2" "3 4" "9 10" "1 1"; do
    set -- $fr
    O=$D/route_f$1_$2_r$round.j$SLURM_JOB_ID.csv
    ./bin/route run --kernel k1 --placement cpu --footprint-mib 1024 --f-num $1 --f-den $2 --first A --seed 0 --cap 20 --events "$EV" --out $O --cell "probe/f-num=$1,f-den=$2,round=$round" --campaign shake3probe --jobid $SLURM_JOB_ID > $O.log 2>&1
    echo "f=$1/$2 round=$round rc=$? $(grep -c '^calib' $O.log) calib lines: $(grep '^calib' $O.log | sed 's/calib variant=//' | tr '\n' ';' | cut -c1-230)"
  done
done
echo "FSWEEP DONE $(date -Is)"
