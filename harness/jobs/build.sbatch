#!/bin/bash -l
#SBATCH -J suite-build
#SBATCH -o results/logs/build_%j.out
#SBATCH -e results/logs/build_%j.out
# Builds on the compute node, as the login node may be another architecture
# submit with harness/submit.sh <campaign> build
set -e
SUITE_DIR="${SUITE_DIR:-${SLURM_SUBMIT_DIR:-$PWD}}"
source "$SUITE_DIR/harness/site.sh"
cd "$SUITE_DIR"
echo "build on $(hostname) $(date -Is)"
make clean
make -j6 all
echo "NVCC BUILD OK"
set +e
make -j6 nvcpp
rc=$?
echo "NVCPP BUILD rc=$rc"
set -e
ls -la bin
cat build_flags.txt
echo "BUILD DONE"
