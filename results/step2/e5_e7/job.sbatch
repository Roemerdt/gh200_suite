#!/bin/bash -l
#SBATCH -J step2-e5e7
#SBATCH -t 00:10:00
#SBATCH -p tutti
#SBATCH -w j21n14
#SBATCH --exclusive
#SBATCH --mem=0
#SBATCH --gres=gpu:1
#SBATCH --chdir=/home/rblom/gh200_route
#SBATCH -o /home/rblom/gh200_route/results/step2/e5_e7/job_%j.out
#SBATCH -e /home/rblom/gh200_route/results/step2/e5_e7/job_%j.out
# Step 2 node checks E-5 (state of the SM clock) and E-7 (SCF events and GPU reads, streaming pattern).
# Pilot probes, 5 Oct 2026. Node in the state of PILOT_FINDINGS A-8 (AutoNUMA on).
SUITE=/home/rblom/gh200_route
source "$SUITE/harness/site.sh"
cd "$SUITE"
D=results/step2/e5_e7
echo "job=$SLURM_JOB_ID node=$(hostname) start=$(date -Is) paranoid=$(cat /proc/sys/kernel/perf_event_paranoid) numa_balancing=$(cat /proc/sys/kernel/numa_balancing)"
echo "=== E-5: what nvidia-smi exposes about clocks ==="
nvidia-smi --help-query-gpu | grep -i -E '^"?clocks' | tr '\n' ' '
echo
nvidia-smi --query-gpu=clocks.sm,clocks.mem,clocks.max.sm,clocks.max.mem,clocks.applications.graphics,clocks.default_applications.graphics,clocks_event_reasons.active,clocks_event_reasons.supported,clocks_event_reasons.applications_clocks_setting,clocks_event_reasons.sw_power_cap,persistence_mode --format=csv
nvidia-smi -q | sed -n '/^    Clocks$/,/Clock Policy/p'
nvidia-smi -q | grep -A3 "Clock Policy"
nvidia-smi -q | sed -n '/Clocks Event Reasons Counters/,/HW Power Braking/p'
echo "sudo rule for nvidia-smi: $(sudo -n -l 2>/dev/null | grep -c nvidia-smi)"
echo "=== E-5: clockstate probe ==="
nvcc -O2 -std=c++17 -arch=sm_90 -Isrc -Xcompiler -pthread -Xcompiler -march=armv9-a -o $D/clockstate $D/clockstate.cu -ldl
$D/clockstate > $D/clockstate_$SLURM_JOB_ID.csv
sed -n '/^summary/,$p' $D/clockstate_$SLURM_JOB_ID.csv
nvidia-smi -q | sed -n '/Clocks Event Reasons Counters/,/HW Power Braking/p'
echo "=== E-7: K1 at f = 1 with seven SCF events (GPU kernel reads and copy engine reads of CPU memory) ==="
./bin/shakedown warmup 5 > $D/warmup_$SLURM_JOB_ID.csv 2>&1
EV="nvidia_nvlink_c2c0_pmu_0/rd_req_loc/,nvidia_nvlink_c2c0_pmu_0/rd_bytes_loc/,nvidia_scf_pmu_0/cmem_rd_access/,nvidia_scf_pmu_0/cmem_rd_data/,nvidia_scf_pmu_0/cmem_wr_access/,nvidia_scf_pmu_0/scf_cache_refill/,nvidia_scf_pmu_0/scf_cache_wb/,nvidia_scf_pmu_0/gmem_rd_access/,nvidia_scf_pmu_0/cycles/,r57,r58"
for round in 1 2; do
  O=$D/route_scf_r$round.j$SLURM_JOB_ID.csv
  ./bin/route run --kernel k1 --placement cpu --footprint-mib 1024 --f-num 1 --f-den 1 --first A --seed 0 --cap 20 --events "$EV" --out $O --cell "step2/e7,round=$round" --campaign step2 --jobid $SLURM_JOB_ID > $O.log 2>&1
  echo "round $round rc=$? $(tail -1 $O.log | cut -c1-160)"
done
echo "JOB DONE $(date -Is)"
