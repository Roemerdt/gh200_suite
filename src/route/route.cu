// runs one kernel in one cell (cell types in config.h, route transient in transient.h)
//
// usage: route run --kernel <name> --placement cpu|hbm --footprint-mib F [--shape <B>x<T>x<8|16>]
//                  [--page-size 64k|512m] [--alignment 1g|off512m]
//                  [--type route|factor|four|kvar|cross|aa --vary <factor> --at <level>[+<level>...]
//                   [--vary2 <factor> --at2 <level>]] [--replicate N] [--sequence AABB]
//                  <the kernel's own flags> <the run-control flags>
#include <cstdio>
#include <cstdlib>
#include <memory>
#include <string>

#include "common/common.h"
#include "measurement.h"
#include "transient.h"

using namespace suite;

// the round order needs the campaign seed as a number, so na is refused
static uint64_t numeric_seed(const RunCtl& rc) {
  char* end;
  const unsigned long long seed = strtoull(rc.seed.c_str(), &end, 10);
  if (end == rc.seed.c_str() || *end != '\0') {
    fprintf(stderr, "--seed=%s: a cell with rounds needs the campaign seed as a number\n",
            rc.seed.c_str());
    exit(2);
  }
  return seed;
}

int main(int argc, char** argv) {
  Args args(argc, argv);
  if (argc >= 2 && std::string(argv[1]) == "transient") { return run_transient(args); }
  if (argc < 2 || std::string(argv[1]) != "run") {
    fprintf(stderr, "usage: route run|transient --kernel <name> ...\n");
    return 2;
  }
  const Config cfg = parse_config(args);
  const RunCtl rc = RunCtl::from(args, "route");

  CU(cudaSetDevice(0));
  CU(cudaFree(0));
  const Kernels kernels = make_kernels(cfg, args);
  pin_self(TIMED_CORE);
  Counters counters;
  std::vector<CounterRole> roles = {{"timed", {TIMED_CORE}}};
  // writer cores for the writes and cache-state event sets, also where CPU-issued passes run
  if (cfg.host.kind != "none" || kernels[0]->cpu_issued()) {
    CounterRole writers{"writers", {}};
    for (int w = 0; w < cfg.host.writers; w++) { writers.cores.push_back(WRITER_CORE_FIRST + w); }
    roles.push_back(writers);
  }
  counters.open(rc.events, roles);

  RouteCell cell(cfg, kernels);
  Calibration calib(cfg, rc.target_ns, rc.passes);
  if (!calibrate(cell, calib)) { return 3; }

  Recorder rec;
  rec.open(rc, row_header(*kernels[0]), counters, TIMED_CORE);
  Measurement measure(cfg, rc, cell, calib, counters);
  std::string loop_line;
  if (!cfg.sequence.empty()) {
    const RoundsResult result =
        run_sequence(rec, rc, cfg.sequence, [&](int v, int pos) { return measure(v, pos); });
    loop_line = rounds_summary_line(rc, result, {});
  } else if (!rounds(cfg)) {
    const int first = rc.first_b ? 1 : 0;
    const LoopResult result = run_loop(rec, rc, true, rc.cell_id + "#A", rc.cell_id + "#B",
                                       [&](int v) { return measure(v, v == first ? 0 : 1); });
    loop_line = loop_summary_line(rc, result, true);
  } else {
    const uint64_t seed = numeric_seed(rc);
    const int k = cell.variants();
    const std::vector<Contrast> contrasts = cell_contrasts(cfg);
    const RoundsResult result = run_rounds(
        rec, rc, k, contrasts,
        [&](int round) { return round_order(seed, rc.cell_id, (uint64_t)round, k); },
        [&](int v, int pos) { return measure(v, pos); });
    loop_line = rounds_summary_line(rc, result, contrasts);
  }

  const std::string summary = cell_summary(cell, loop_line);
  rec.done(summary);
  fprintf(stderr, "%s\n", summary.c_str());
  return 0;
}
