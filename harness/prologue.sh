#!/bin/bash
# Sourced by every measurement job before the runner, needs SUITE_DIR and CAMPAIGN
source "$SUITE_DIR/harness/site.sh"
cd "$SUITE_DIR"
ATTEMPT=${SLURM_RESTART_COUNT:-0}
TAG=${SLURM_JOB_ID}_a${ATTEMPT}
RES=results/$CAMPAIGN
mkdir -p "$RES/raw" "$RES/env" "$RES/guards"
echo "job=$SLURM_JOB_ID attempt=$ATTEMPT node=$(hostname) campaign=$CAMPAIGN start=$(date -Is)"
bash harness/envcapture.sh "$RES/env/$TAG"

# placement gate, GPU reads of GPU memory must beat those of CPU memory by SITE_GATE_FACTOR
./bin/shakedown bw 0 > "$RES/guards/gate_bw_node0_$TAG.csv"
./bin/shakedown bw 1 > "$RES/guards/gate_bw_node1_$TAG.csv"
n0=$(awk -F, '$2=="bw_read"{if($7+0>m)m=$7+0}END{print m}' "$RES/guards/gate_bw_node0_$TAG.csv")
n1=$(awk -F, '$2=="bw_read"{if($7+0>m)m=$7+0}END{print m}' "$RES/guards/gate_bw_node1_$TAG.csv")
echo "PLACEMENT GATE: node0=${n0} GB/s node1=${n1} GB/s factor=${SITE_GATE_FACTOR}"
if ! awk -v a="$n0" -v b="$n1" -v f="$SITE_GATE_FACTOR" 'BEGIN{exit !(b > f*a)}'; then
  echo "PLACEMENT GATE FAILED (node1 not > ${SITE_GATE_FACTOR}x node0): aborting job, no measurements taken" | tee "$RES/guards/GATE_FAILED_$TAG"
  exit 1
fi
echo "gate PASS node0=${n0} node1=${n1}" > "$RES/guards/gate_$TAG.txt"

# 1 Hz clock/power log for the whole job (joined to raw rows by timestamp in the analysis)
nvidia-smi --query-gpu=timestamp,clocks.sm,clocks.mem,power.draw,temperature.gpu --format=csv,noheader -l 1 > "$RES/guards/clocks_$TAG.csv" &
CLOCKPID=$!
trap 'kill $CLOCKPID 2>/dev/null || true' EXIT

# sustained load so the SM clock is at its maximum before the first timed interval
./bin/shakedown warmup ${WARMUP_S:-30} > "$RES/guards/warmup_$TAG.csv" 2>&1
echo "prologue done $(date -Is)"
