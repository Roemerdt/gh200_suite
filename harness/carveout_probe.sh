# Probes the shared-memory configuration the driver gives K2 and K5 per carveout hint
# the default hints in src/route/kernels/k2_reuse.cu and k5_stencil.cu come from it
# usage: bash harness/carveout_probe.sh (on the node)
N=/opt/nvidia/hpc_sdk/Linux_aarch64/25.9/profilers/13.0/Nsight_Compute/ncu
COMMON="--out /tmp/p.csv --cell probe --campaign probe --warmup 0 --n0 1 --step 1 --cap 1 --target-ms 1 --passes A=1,B=1 --first A --seed 1"
probe() { # label env-var value kernel-regex args...
  label=$1; var=$2; val=$3; rx=$4; shift 4
  cfg=$(env $var=$val $N --cache-control none --replay-mode application -k regex:$rx --launch-skip 0 --launch-count 1 --metrics launch__shared_mem_config_size --csv ./bin/route run "$@" $COMMON 2>/dev/null | grep launch__shared_mem_config_size | awk -F"," "{print \$(NF)}" | tr -d "\"")
  echo "$label $var=$val -> config $cfg"
}
for h in 25 30 40 50; do probe "K5 tiles" SUITE_CARVEOUT_K5_TILES $h k5_sweep --kernel k5 --placement cpu --footprint-mib 512 --sweeps 8 --tiling tiles; done
for h in 40 50 58; do probe "K5 none" SUITE_CARVEOUT_K5 $h k5_sweep --kernel k5 --placement cpu --footprint-mib 512 --sweeps 8 --tiling none; done
for h in 40 50 58; do probe "K2" SUITE_CARVEOUT_K2 $h k2_reuse --kernel k2 --placement cpu --footprint-mib 1024 --working-set-mib 8 --k 16; done
