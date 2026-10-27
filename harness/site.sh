#!/bin/bash
# Toolchain and path setup, sourced by every job script
source "$(dirname "${BASH_SOURCE[0]}")/site.env"
if [ -n "$SITE_MODULES" ]; then module load $SITE_MODULES; fi
export PATH="$PATH:/usr/bin:/bin${SITE_SLURM_PATH:+:$SITE_SLURM_PATH}"
