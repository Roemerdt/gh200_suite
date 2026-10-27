// raw rows, one per timed interval and written as they happen, then a .done marker for the cell
// status: OK | RECORDED (residency is the measurand) | WARMUP | DISCARDED_MIGRATION |
//         VOID_CHECKSUM | DISCARDED (cold diagnostic row)
#pragma once
#include <sys/stat.h>

#include <cstdio>
#include <cstdlib>
#include <string>

#include "args.h"
#include "clocks.h"
#include "counters.h"
#include "memory.h"
#include "timing.h"

namespace suite {

struct Interval {
  double interval_ns = 0;                       // the timed span
  long batch = 0;                               // repetitions in the span
  std::string res_pre = "NA", res_post = "NA";  // residency before and after
  int cold = 0;  // 1: a cold first repetition, excluded from the statistics
  std::string status = "OK";
  std::string extra;  // the binary's own columns, comma separated, no leading comma

  double per_op() const { return interval_ns / (double)batch; }

  void set_timed(double ns, long repetitions, const Residency& pre, const Residency& post) {
    interval_ns = ns;
    batch = repetitions;
    res_pre = pre.detail;
    res_post = post.detail;
    status = (pre.ok && post.ok) ? "OK" : "DISCARDED_MIGRATION";
  }
};

static const char* COMMON_HEADER =
    "ts_epoch,instrument,campaign,jobid,attempt,cell_id,pair_id,alloc_id,member,rep,batch,"
    "interval_ns,ns_per_op,sm_clock_mhz,cpu_khz,residency_pre,residency_post,cold,status";

struct Recorder {
  FILE* f = nullptr;
  std::string path;
  RunCtl rc;
  ClockReader clocks;
  const Counters* counters = nullptr;

  void open(const RunCtl& r, const std::string& extra_header, const Counters& ctr, int timed_core) {
    rc = r;
    path = r.out;
    counters = &ctr;
    clocks.init(timed_core);
    struct stat st;
    const bool fresh = (stat(path.c_str(), &st) != 0) || st.st_size == 0;
    f = fopen(path.c_str(), "a");
    if (!f) {
      perror("open raw csv");
      exit(1);
    }
    if (fresh) {
      std::string columns = extra_header;
      if (!counters->empty()) { columns += "," + counters->header(); }
      fprintf(f, "%s,%s\n", COMMON_HEADER, columns.c_str());
      flush_or_exit();
    }
  }

  // A write that failed (disk full, quota) stops the cell before a .done marker can claim it
  void flush_or_exit() {
    if (fflush(f) != 0 || ferror(f)) {
      perror("write raw csv");
      exit(1);
    }
  }

  // microsecond timestamps, so sub-millisecond intervals still order A before B
  // ns_per_op to 8 significant digits
  void row(const std::string& pair_id, const std::string& alloc_id, const std::string& member, int rep,
           const Interval& iv) {
    std::string columns = iv.extra;
    if (!counters->empty()) { columns += "," + counters->values(); }
    fprintf(f, "%.6f,%s,%s,%s,%d,\"%s\",\"%s\",\"%s\",%s,%d,%ld,%.0f,%.7e,%d,%ld,%s,%s,%d,%s,%s\n",
            now_epoch_s(), rc.instrument.c_str(), rc.campaign.c_str(), rc.jobid.c_str(), rc.attempt,
            rc.cell_id.c_str(), pair_id.c_str(), alloc_id.c_str(), member.c_str(), rep, iv.batch,
            iv.interval_ns, iv.per_op(), clocks.sm_mhz(), clocks.cpu_khz(), iv.res_pre.c_str(),
            iv.res_post.c_str(), iv.cold, iv.status.c_str(), columns.c_str());
    flush_or_exit();
  }

  // <out>.done holds the binary's own summary line
  void done(const std::string& summary) {
    if (fclose(f) != 0) {
      perror("close raw csv");
      exit(1);
    }
    f = nullptr;
    FILE* marker = fopen((path + ".done").c_str(), "w");
    if (!marker) {
      perror("done marker");
      exit(1);
    }
    fprintf(marker, "%s\n", summary.c_str());
    if (fclose(marker) != 0) {
      perror("done marker");
      exit(1);
    }
  }
};

}  // namespace suite
