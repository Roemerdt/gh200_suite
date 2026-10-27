#!/bin/bash -l
#SBATCH -J suite-phase
#SBATCH --requeue
#SBATCH -o results/logs/phase_%x_%j.out
#SBATCH -e results/logs/phase_%x_%j.out
# One resumable phase of a campaign, submitted with harness/submit.sh <campaign> phase <name>
set -e
export SUITE_DIR="${SUITE_DIR:-${SLURM_SUBMIT_DIR:-$PWD}}"
export CAMPAIGN="${CAMPAIGN:-dev}"
source "$SUITE_DIR/harness/prologue.sh"
python3 harness/campaign.py --phase "$PHASE" --results "results/$CAMPAIGN" ${CAMPAIGN_ARGS:-}
echo "phase job done $(date -Is)"
