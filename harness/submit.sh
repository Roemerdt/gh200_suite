#!/bin/bash
# Submits one job with the settings of harness/site.env and records the scheduler's view of it
# usage: bash harness/submit.sh <campaign> build
#        bash harness/submit.sh <campaign> phase <name>
set -e
cd "$(dirname "$0")/.."
source harness/site.env
CAMPAIGN=$1; KIND=$2; PHASE=${3:-}
[ -n "$CAMPAIGN" ] && [ -n "$KIND" ] || { echo "usage: submit.sh <campaign> build|phase <name>" >&2; exit 2; }
mkdir -p results/logs "results/$CAMPAIGN/env"
COMMON="--parsable --chdir=$PWD $SITE_SBATCH_FLAGS -w $SITE_NODE -p $SITE_PARTITION"
case "$KIND" in
  build)   JOB=$(sbatch $COMMON -t "$SITE_BUILD_TIME" --export=ALL,SUITE_DIR=$PWD harness/jobs/build.sbatch) ;;
  phase)   [ -n "$PHASE" ] || { echo "phase name required" >&2; exit 2; }
           JOB=$(sbatch $COMMON -t "$SITE_PHASE_TIME" -J "$PHASE" --export=ALL,SUITE_DIR=$PWD,CAMPAIGN=$CAMPAIGN,PHASE=$PHASE harness/jobs/phase.sbatch) ;;
  *) echo "unknown kind $KIND" >&2; exit 2 ;;
esac
JOB=${JOB%%;*}
{ echo "# submitted $(date -Is) kind=$KIND phase=$PHASE campaign=$CAMPAIGN"
  echo "# sbatch $COMMON"
  scontrol show job "$JOB"; scontrol show partition "$SITE_PARTITION"; scontrol show node "$SITE_NODE"; } > "results/$CAMPAIGN/env/submit_${JOB}.txt" 2>&1
echo "$JOB"
