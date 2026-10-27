#pragma once
#include <cstdio>
#include <string>

#include "cell.h"
#include "config.h"
#include "kernel.h"

namespace suite {

inline std::string row_header(const RouteKernel& kernel) {
  return "kernel,route,placement,node,footprint_bytes," + kernel.knob_header() +
         ",touched_lines,passes,blocks,threads,align_bytes,addr,off_1g,off_16g,out_addr,anon_huge_"
         "kb,pop,"
         "first,seed,checksum,expected,copyin_ns,kernel_ns,copyout_ns,wall_ns,type,vary,at,level,"
         "pos,cursor,floor_ns,passes_frozen,page_size,alignment,vary2,at2,replicate,sequence,load,"
         "copy,tune,"
         "host,w,pattern,writers,state,sharing,recopy,cpu_ns,state_check_ns";
}

// first is the variant that leads every repeat of a two-variant cell, a dash in a round cell
// passes_frozen is 1 when the harness froze the repetitions per interval
inline std::string row_values(const Config& cfg, const RouteCell& cell, const RunCtl& rc, int v,
                              int pos, long passes, bool passes_frozen, u64 checksum,
                              double wall_ns) {
  const VariantSpec& s = cfg.variants[v];
  const RouteKernel& kernel = cell.kernel(v);
  const u64 addr = (u64)(uintptr_t)cell.host(v).input.p;
  char first_call[96] = "nan,nan,nan";
  if (s.route == COPY) {
    const double* c = cell.first_call_ns();
    snprintf(first_call, sizeof first_call, "%.0f,%.0f,%.0f", c[0], c[1], c[2]);
  }
  const char first = (rounds(cfg) || !cfg.sequence.empty()) ? '-' : (rc.first_b ? 'B' : 'A');
  char buf[1792];
  snprintf(buf, sizeof buf,
           "%s,%s,%s,%d,%zu,%s,%llu,%ld,%d,%d,%zu,0x%llx,%llu,%llu,0x%llx,%ld,%s,%c,%s,0x%016llx,"
           "0x%016llx,%s,%.0f,%s,%s,%s,%s,%d,%d,%.0f,%d,%s,%s,%s,%s,%s,%s,%d,%s,%s,%s,%g,%s,%d,%s,%"
           "s,%s,%.0f,%.1f",
           kernel.name(), route_name(s.route), s.placement.c_str(), s.node, s.input_bytes,
           kernel.knob_values().c_str(), kernel.touched_lines(), passes, s.shape.blocks,
           s.shape.threads, s.align_bytes, addr, addr % (1ull << 30), addr % (16ull << 30),
           (u64)(uintptr_t)cell.host(v).output.p, cell.host(v).anon_huge_kb, POPULATION_RECIPE,
           first, rc.seed.c_str(), checksum, cell.expected_checksum(v), first_call, wall_ns,
           cfg.type_name.c_str(), cfg.vary.c_str(), cfg.at.c_str(), s.level.c_str(), pos,
           (int)kernel.cursor(), rc.floor_ns, (int)passes_frozen, s.page_size.c_str(),
           s.alignment.c_str(), cfg.vary2.c_str(), cfg.at2.c_str(), cfg.replicate.c_str(),
           cfg.sequence.c_str(), s.shape.load_bytes, s.route == COPY ? s.copy.label().c_str() : "-",
           cfg.tune.c_str(), s.host.kind.c_str(), s.host.w, s.host.pattern.c_str(), s.host.writers,
           s.host.state.c_str(),
           s.host.kind == "none" ? "-" : (s.host.control ? "control" : "shared"), s.recopy.c_str(),
           cell.cpu_ns(v), cell.state_check_ns(v));
  return buf;
}

}  // namespace suite
