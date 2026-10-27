// The cell's configuration from the command line and the variants it gives
#pragma once
#include <unistd.h>

#include <cstdint>
#include <cstdlib>
#include <memory>
#include <string>
#include <utility>
#include <vector>

#include "common/common.h"
#include "copy.h"
#include "host_phase.h"
#include "kernel.h"

namespace suite {

static const size_t HOME_ALIGN_BYTES = 1ull << 30;  // start of every host buffer at home
static const size_t WINDOW_ALIGN_BYTES = 16ull
                                         << 30;  // the offset level counts from a 16 GiB boundary
static const size_t OFFSET_LEVEL_BYTES = 512ull << 20;  // and starts this far past it
static const size_t CPU_CURSOR_BYTES =
    8ull << 20;  // at CPU placement, smaller touched sets use the cursor
static const size_t CAPACITY_MARGIN_BYTES = 2ull << 30;  // GPU-node memory a cell must leave free
static const int CAPACITY_SETTLE_MIN_POLLS = 6;  // free memory is read at least this often and then
static const int CAPACITY_SETTLE_POLLS = 60;     // until it stops rising, at most this often,
static const useconds_t CAPACITY_SETTLE_US = 500000;  // this far apart
static const long MAX_PASSES_PER_INTERVAL = 100000;   // bound for the smallest touched sets
static const long STATE_PHASE_PASSES = 50;  // passes per interval of a cache-state cell, fixed
static const long HOST_PHASE_MAX_PASSES =
    50;  // passes per interval of a CPU-writes or CPU-reads cell, at most
static const u64 RECOPY_MAX_RUNS = 4096;  // copy calls per pass of the per-run re-copy, at most

static const double STATE_CHECK_CPU_NS = 110,
                    STATE_CHECK_GPU_NODE_NS = 250;      // cached below, uncached above
static const char* const POPULATION_RECIPE = "cpuall";  // the CPU populates on all cores
static const int EXIT_NO_HUGE_PAGES = 4;  // a variant asked for 512 MB pages and did not get them
static const int EXIT_DECLARED_GAP = 5;   // the cell does not fit in GPU-node memory
static const char* const HOME_LEVEL = "home";
static const char* const ROUTE_FLAGS[] = {"kernel",
                                          "placement",
                                          "footprint-mib",
                                          "page-size",
                                          "alignment",
                                          "type",
                                          "vary",
                                          "at",
                                          "vary2",
                                          "at2",
                                          "replicate",
                                          "sequence",
                                          "tune",
                                          "shape",
                                          "shape-hbm",
                                          "copy-shape",
                                          "copy-shape-hbm",
                                          "copy",
                                          "copy-hbm",
                                          "copy-at",
                                          "copies",
                                          "host",
                                          "w",
                                          "pattern",
                                          "writers",
                                          "state",
                                          "sharing",
                                          "recopy"};

enum Route { DIRECT = 0, COPY = 1 };
inline const char* route_name(int r) {
  return r == DIRECT ? "direct" : "copy";
}

// route   direct and copy at home
// factor  direct at home and at the level
// four    direct and copy, each at home and at the level
// kvar    direct at home and at every level
// cross   direct at home, at each of two factors' levels, and at both
// aa      two identically prepared direct variants
// tune    one route at home in every configuration of a tuning space, on shared buffers
enum CellType { ROUTE_CELL, FACTOR_CELL, FOUR_CELL, KVAR_CELL, CROSS_CELL, AA_CELL, TUNE_CELL };

inline int placement_node(const std::string& placement) {
  return placement == "hbm" ? GPU_NODE : CPU_NODE;
}

struct VariantSpec {
  int route = DIRECT;
  std::string placement;
  int node = CPU_NODE;
  size_t input_bytes = 0;
  std::string page_size = "64k";
  int thp = 0;
  std::string alignment = "1g";
  size_t align_bytes = HOME_ALIGN_BYTES, offset_bytes = 0;
  std::vector<std::pair<std::string, std::string>> kernel_levels;
  LaunchShape shape;
  CopyConfig copy;
  std::string recopy = "none";  // none (basic copy) | runs | pitched | gather
  HostPhaseSpec host;           // the host phase between passes, control or shared
  std::string level =
      HOME_LEVEL;  // <vary level>[+<vary2 level>], or a tuning variant's configuration
};

struct Config {
  const KernelEntry* kernel = nullptr;
  std::string placement, page_size, alignment;  // home
  size_t input_bytes = 0;                       // home
  HostPhaseSpec host;                           // home, for every variant
  std::string sharing = "control", recopy = "none";
  LaunchShape shape, shape_hbm, copy_shape,
      copy_shape_hbm;                  // frozen shapes of both routes at both placements
  CopyConfig copy, copy_hbm, copy_at;  // frozen copies at both placements and at the level
  bool has_copy_hbm = false, has_copy_at = false;
  CellType type = ROUTE_CELL;
  std::string type_name = "route", vary, at, vary2, at2, tune;  // as given, echoed in every row
  std::vector<std::string> levels, levels2;                     // the levels of --at and --at2
  std::vector<std::string>
      copies;  // a copy tuning cell restricted to these configurations (the held-out block)
  std::string replicate = "1";  // a label that tells otherwise identical cells apart
  std::string sequence;  // fixed A/B pattern for the carry-over check, empty for the paired loop
  bool shared_buffers = false;  // a tuning cell's variants share the host buffers
  std::vector<VariantSpec> variants;
};

inline bool rounds(const Config& c) {
  return c.type == FOUR_CELL || c.type == KVAR_CELL || c.type == CROSS_CELL || c.type == TUNE_CELL;
}

inline const KernelEntry* find_kernel(const std::string& name) {
  for (const KernelEntry& k : kernels()) {
    if (name == k.name) { return &k; }
  }
  fprintf(stderr, "--kernel=%s is not one of {", name.c_str());
  for (const KernelEntry& k : kernels()) { fprintf(stderr, " %s", k.name); }
  fprintf(stderr, " }\n");
  exit(2);
}

inline std::vector<std::string> split(const std::string& s, char sep) {
  std::vector<std::string> parts;
  size_t start = 0;
  for (size_t end; (end = s.find(sep, start)) != std::string::npos; start = end + 1) {
    parts.push_back(s.substr(start, end - start));
  }
  parts.push_back(s.substr(start));
  return parts;
}

inline size_t footprint_bytes(double mib) {
  return (size_t)(mib * 1024.0 * 1024.0) / GPU_LINE_BYTES * GPU_LINE_BYTES;
}

// <blocks>x<threads>x<load bytes>
inline LaunchShape parse_shape(const std::string& text, const char* flag) {
  LaunchShape s;
  char tail;
  if (sscanf(text.c_str(), "%dx%dx%d%c", &s.blocks, &s.threads, &s.load_bytes, &tail) != 3 ||
      s.blocks < 1 || s.threads < 1 || s.threads > 1024 ||
      (s.load_bytes != 8 && s.load_bytes != 16)) {
    bad_flag_value(flag, text, "is not <blocks>x<threads>x<8|16>");
  }
  return s;
}

// default tuning space of the direct route, resident warps set through the blocks per SM
inline std::vector<LaunchShape> shape_space(const std::vector<int>& load_widths) {
  std::vector<LaunchShape> shapes;
  for (int threads : {128, 256, 512, 1024}) {
    for (int warps : {8, 16, 32, 64}) {
      const int blocks_per_sm = warps * 32 / threads;
      if (blocks_per_sm < 1 || blocks_per_sm * threads > 2048) { continue; }
      for (int waves : {1, 2, 4, 8}) {
        for (int load : load_widths) {
          shapes.push_back({waves * SMS * blocks_per_sm, threads, load});
        }
      }
    }
  }
  return shapes;
}

inline bool kernel_factor(const Config& c, const std::string& factor) {
  for (const char* f : c.kernel->factors) {
    if (factor == f) { return true; }
  }
  return false;
}

inline bool driver_factor(const std::string& factor) {
  return factor == "placement" || factor == "footprint" || factor == "page-size" ||
         factor == "alignment" || factor == "sharing";
}

inline void set_page_size(VariantSpec& v, const std::string& level, const char* flag) {
  if (level != "64k" && level != "512m") { bad_flag_value(flag, level, "is not 64k or 512m"); }
  v.page_size = level;
  v.thp = level == "512m" ? 1 : 0;
}

inline void set_alignment(VariantSpec& v, const std::string& level, const char* flag) {
  if (level != "1g" && level != "off512m") { bad_flag_value(flag, level, "is not 1g or off512m"); }
  v.alignment = level;
  v.align_bytes = level == "1g" ? HOME_ALIGN_BYTES : WINDOW_ALIGN_BYTES;
  v.offset_bytes = level == "1g" ? 0 : OFFSET_LEVEL_BYTES;
}

// a kernel factor is only recorded here and applied in make_kernels
inline void apply_level(const Config& c, VariantSpec& v, const std::string& factor,
                        const std::string& level) {
  if (factor == "placement") {
    if (level != "cpu" && level != "hbm") { bad_flag_value("at", level, "is not cpu or hbm"); }
    v.placement = level;
    v.node = placement_node(level);
  } else if (factor == "footprint") {
    char* end;
    const double mib = strtod(level.c_str(), &end);
    if (end == level.c_str() || *end != '\0' || mib <= 0) {
      bad_flag_value("at", level, "is not a footprint in MiB");
    }
    v.input_bytes = footprint_bytes(mib);
  } else if (factor == "page-size") {
    set_page_size(v, level, "at");
  } else if (factor == "alignment") {
    set_alignment(v, level, "at");
  } else if (factor == "sharing") {
    if (level != "shared" && level != "control") {
      bad_flag_value("at", level, "is not shared or control");
    }
    if (c.host.kind == "none") {
      fprintf(stderr, "--vary=sharing needs a host phase (--host writes|state|reads)\n");
      exit(2);
    }
    v.host.control = level == "control";
  } else if (kernel_factor(c, factor)) {
    v.kernel_levels.push_back({factor, level});
  } else {
    fprintf(stderr,
            "--vary=%s is not placement, footprint, page-size, alignment or a factor of %s\n",
            factor.c_str(), c.kernel->name);
    exit(2);
  }
}

inline void apply_frozen(const Config& c, VariantSpec& v, bool at_level) {
  const bool hbm = v.placement == "hbm";
  if (v.route == DIRECT) {
    v.shape = hbm ? c.shape_hbm : c.shape;
  } else {
    v.shape = hbm ? c.copy_shape_hbm : c.copy_shape;
    v.copy =
        (at_level && c.has_copy_at) ? c.copy_at : (hbm && c.has_copy_hbm ? c.copy_hbm : c.copy);
  }
}

inline VariantSpec variant_at(const Config& c, int route, const std::string& level,
                              const std::string& level2 = HOME_LEVEL) {
  VariantSpec v;
  v.route = route;
  v.placement = c.placement;
  v.node = placement_node(c.placement);
  v.input_bytes = c.input_bytes;
  set_page_size(v, c.page_size, "page-size");
  set_alignment(v, c.alignment, "alignment");
  v.host = c.host;
  v.host.control = c.sharing == "control";
  v.recopy = route == COPY ? c.recopy : "none";
  if (level != HOME_LEVEL) { apply_level(c, v, c.vary, level); }
  if (level2 != HOME_LEVEL) { apply_level(c, v, c.vary2, level2); }
  v.level = c.vary2.empty() ? level : level + "+" + level2;
  apply_frozen(c, v, level != HOME_LEVEL);
  return v;
}

inline void check_levels(const Config& c, const std::string& factor,
                         const std::vector<std::string>& levels, const std::string& flag) {
  for (const std::string& level : levels) {
    const bool same_as_home = (factor == "placement" && level == c.placement) ||
                              (factor == "page-size" && level == c.page_size) ||
                              (factor == "alignment" && level == c.alignment) ||
                              (factor == "sharing" && level == c.sharing);
    if (level.empty() || level == HOME_LEVEL || same_as_home) {
      bad_flag_value(flag.c_str(), level, "is the home level");
    }
  }
}

inline void build_tuning_variants(Config& c, const RouteKernel& probe) {
  c.shared_buffers = true;
  if (c.tune == "direct" || c.tune == "copy-kernel") {
    std::vector<LaunchShape> shapes = probe.shape_space();
    if (shapes.empty()) { shapes = shape_space(probe.load_widths()); }
    for (const LaunchShape& shape : shapes) {
      VariantSpec v = variant_at(c, c.tune == "direct" ? DIRECT : COPY, HOME_LEVEL);
      v.shape = shape;
      v.level = shape.label();
      c.variants.push_back(v);
    }
  } else {
    std::vector<CopyConfig> space;
    if (c.copies.empty()) {
      space = CopyConfig::space(probe);
    } else {
      for (const std::string& label : c.copies) {
        space.push_back(CopyConfig::parse(label, "copies"));
      }
    }
    for (const CopyConfig& copy : space) {
      VariantSpec v = variant_at(c, COPY, HOME_LEVEL);
      v.copy = copy;
      v.level = copy.label();
      c.variants.push_back(v);
    }
  }
}

inline void build_variants(Config& c, const RouteKernel& probe) {
  const bool varies = c.type != ROUTE_CELL && c.type != AA_CELL && c.type != TUNE_CELL;
  if (!varies && (!c.vary.empty() || !c.at.empty() || !c.vary2.empty() || !c.at2.empty())) {
    fprintf(stderr, "a %s cell varies nothing: drop --vary, --at, --vary2 and --at2\n",
            c.type_name.c_str());
    exit(2);
  }
  if (c.type == TUNE_CELL) {
    build_tuning_variants(c, probe);
    return;
  }
  if (!c.tune.empty()) {
    fprintf(stderr, "--tune belongs to --type=tune\n");
    exit(2);
  }
  if (varies && (c.vary.empty() || c.at.empty())) {
    fprintf(stderr, "--type=%s needs --vary <factor> and --at <level>[+<level>...]\n",
            c.type_name.c_str());
    exit(2);
  }
  if (c.type == CROSS_CELL && (c.vary2.empty() || c.at2.empty())) {
    fprintf(stderr, "--type=cross needs --vary2 <factor> and --at2 <level> as well\n");
    exit(2);
  }
  if (c.type != CROSS_CELL && (!c.vary2.empty() || !c.at2.empty())) {
    fprintf(stderr, "--vary2 and --at2 belong to --type=cross\n");
    exit(2);
  }
  if (varies && !driver_factor(c.vary) && !kernel_factor(c, c.vary)) {
    fprintf(stderr,
            "--vary=%s is not placement, footprint, page-size, alignment or a factor of %s\n",
            c.vary.c_str(), c.kernel->name);
    exit(2);
  }
  if (c.type == CROSS_CELL &&
      (c.vary2 == c.vary || (!driver_factor(c.vary2) && !kernel_factor(c, c.vary2)))) {
    fprintf(stderr, "--vary2=%s must be a second factor\n", c.vary2.c_str());
    exit(2);
  }
  const size_t levels = c.levels.size();
  if ((c.type == FACTOR_CELL || c.type == FOUR_CELL || c.type == CROSS_CELL) && levels != 1) {
    fprintf(stderr, "--type=%s takes exactly one level in --at\n", c.type_name.c_str());
    exit(2);
  }
  if (c.type == CROSS_CELL && c.levels2.size() != 1) {
    fprintf(stderr, "--type=cross takes exactly one level in --at2\n");
    exit(2);
  }
  if (c.type == KVAR_CELL && levels < 2) {
    fprintf(stderr, "--type=kvar takes at least two levels in --at (one level is a factor cell)\n");
    exit(2);
  }
  check_levels(c, c.vary, c.levels, "at");
  check_levels(c, c.vary2, c.levels2, "at2");

  c.variants.push_back(variant_at(c, DIRECT, HOME_LEVEL));
  if (c.type == ROUTE_CELL || c.type == FOUR_CELL) {
    c.variants.push_back(variant_at(c, COPY, HOME_LEVEL));
  }
  if (c.type == AA_CELL) { c.variants.push_back(variant_at(c, DIRECT, HOME_LEVEL)); }
  for (const std::string& level : c.levels) {
    c.variants.push_back(variant_at(c, DIRECT, level));
    if (c.type == FOUR_CELL) { c.variants.push_back(variant_at(c, COPY, level)); }
  }
  if (c.type == CROSS_CELL) {
    c.variants.push_back(variant_at(c, DIRECT, HOME_LEVEL, c.levels2[0]));
    c.variants.push_back(variant_at(c, DIRECT, c.levels[0], c.levels2[0]));
  }
}

inline Config parse_config(const Args& args) {
  Config c;
  c.kernel = find_kernel(args.get("kernel", "k1"));
  std::vector<const char*> known(std::begin(ROUTE_FLAGS), std::end(ROUTE_FLAGS));
  known.insert(known.end(), c.kernel->knobs.begin(), c.kernel->knobs.end());
  args.check_known(known);
  c.placement = args.enum_arg("placement", "cpu", {"cpu", "hbm"});
  c.input_bytes = footprint_bytes(args.getf("footprint-mib", 1024));
  c.page_size = args.enum_arg("page-size", "64k", {"64k", "512m"});
  c.alignment = args.enum_arg("alignment", "1g", {"1g", "off512m"});
  c.shape = parse_shape(args.get("shape", LaunchShape().label()), "shape");
  c.shape_hbm = parse_shape(args.get("shape-hbm", c.shape.label()), "shape-hbm");
  c.copy_shape = parse_shape(args.get("copy-shape", c.shape_hbm.label()), "copy-shape");
  c.copy_shape_hbm =
      parse_shape(args.get("copy-shape-hbm", c.copy_shape.label()), "copy-shape-hbm");
  c.copy = CopyConfig::parse(args.get("copy", CopyConfig().label()), "copy");
  c.has_copy_hbm = args.has("copy-hbm");
  c.copy_hbm = c.has_copy_hbm ? CopyConfig::parse(args.get("copy-hbm"), "copy-hbm") : c.copy;
  c.has_copy_at = args.has("copy-at");
  c.copy_at = c.has_copy_at ? CopyConfig::parse(args.get("copy-at"), "copy-at") : c.copy;
  c.type_name =
      args.enum_arg("type", "route", {"route", "factor", "four", "kvar", "cross", "aa", "tune"});
  c.type = c.type_name == "factor"  ? FACTOR_CELL
           : c.type_name == "four"  ? FOUR_CELL
           : c.type_name == "kvar"  ? KVAR_CELL
           : c.type_name == "cross" ? CROSS_CELL
           : c.type_name == "aa"    ? AA_CELL
           : c.type_name == "tune"  ? TUNE_CELL
                                    : ROUTE_CELL;
  c.tune = c.type == TUNE_CELL ? args.enum_arg("tune", "direct", {"direct", "copy-kernel", "copy"})
                               : args.get("tune", "");
  c.vary = args.get("vary", "");
  c.at = args.get("at", "");
  c.vary2 = args.get("vary2", "");
  c.at2 = args.get("at2", "");
  c.replicate = args.get("replicate", "1");
  c.sequence = args.get("sequence", "");
  c.host.kind = args.enum_arg("host", "none", {"none", "writes", "state", "reads"});
  c.host.w = args.getf("w", 1.0);
  c.host.pattern = args.enum_arg("pattern", "word", {"word", "line"});
  c.host.writers = (int)args.geti("writers", c.placement == "hbm" ? 32 : 16);
  c.host.state = args.enum_arg("state", "dirty", {"dirty", "clean", "evicted"});
  c.sharing = args.enum_arg("sharing", "control", {"control", "shared"});
  c.recopy = args.enum_arg("recopy", "none", {"none", "runs", "pitched", "gather"});
  if (c.host.w <= 0 || c.host.w > 1 || c.host.writers < 1 || c.host.writers > 64) {
    fprintf(stderr, "--w must be in (0, 1] and --writers in 1..64\n");
    exit(2);
  }
  if (c.recopy != "none" && c.host.kind != "writes") {
    fprintf(stderr, "--recopy is the copy route under CPU writes (--host writes)\n");
    exit(2);
  }
  if (!c.at.empty()) { c.levels = split(c.at, '+'); }
  if (!c.at2.empty()) { c.levels2 = split(c.at2, '+'); }
  if (args.has("copies")) {
    if (c.tune != "copy") {
      fprintf(stderr, "--copies restricts a copy tuning cell (--type tune --tune copy)\n");
      exit(2);
    }
    c.copies = split(args.get("copies"), '+');
  }
  const std::unique_ptr<RouteKernel> probe = c.kernel->make(args, c.input_bytes, c.shape);
  if (probe->input_is_window()) {  // the kernel's basic copy is the copy of its window
    if (!args.has("copy")) { c.copy.form = "touched"; }
    if (!c.has_copy_hbm) { c.copy_hbm = c.copy; }
    if (!c.has_copy_at) { c.copy_at = c.copy; }
  }
  build_variants(c, *probe);
  if (c.variants.size() > 26 && c.type != TUNE_CELL) {
    fprintf(stderr, "a cell has at most 26 variants\n");
    exit(2);
  }
  if (!c.sequence.empty()) {
    if (c.variants.size() != 2) {
      fprintf(stderr,
              "--sequence runs a two-variant cell (route, factor or aa) in a fixed pattern\n");
      exit(2);
    }
    for (char letter : c.sequence) {
      if (letter != 'A' && letter != 'B') {
        bad_flag_value("sequence", c.sequence, "is not a pattern over A and B");
      }
    }
  }
  return c;
}

// smaller touched sets would meet the previous pass's cache state (twice the L2 at HBM)
inline size_t cursor_threshold_bytes(int node) {
  if (node != GPU_NODE) { return CPU_CURSOR_BYTES; }
  static const size_t l2_bytes = [] {
    cudaDeviceProp p;
    CU(cudaGetDeviceProperties(&p, 0));
    return (size_t)p.l2CacheSize;
  }();
  return 2 * l2_bytes;
}

// one kernel per variant with its levels and launch shape, the cursor on for small touched sets
inline std::vector<std::unique_ptr<RouteKernel>> make_kernels(const Config& c, const Args& args) {
  std::vector<std::unique_ptr<RouteKernel>> made;
  for (const VariantSpec& v : c.variants) {
    Args a = args;
    for (const auto& fl : v.kernel_levels) { c.kernel->set_level(a, fl.first, fl.second); }
    std::unique_ptr<RouteKernel> k = c.kernel->make(a, v.input_bytes, v.shape);
    if (k->cpu_issued() && v.route == COPY) {
      fprintf(stderr, "passes issued by CPU threads run the direct route only: cell refused\n");
      exit(2);
    }
    const size_t threshold = cursor_threshold_bytes(v.node);
    // a cache-state cell re-prepares the lines before every pass, so it needs no cursor
    if (k->touched_lines() * GPU_LINE_BYTES <= threshold && !k->enable_cursor() &&
        c.host.kind != "state") {
      fprintf(stderr,
              "variant %zu touches %llu bytes, at most %zu, and %s has no cursor for this setting: "
              "cell refused\n",
              made.size(), k->touched_lines() * GPU_LINE_BYTES, threshold, k->name());
      exit(2);
    }
    made.push_back(std::move(k));
  }
  return made;
}

// in a four cell A-B and C-D are the route difference at home and at the level. In a cross cell
// B-A and D-C are the first factor's effect at both levels of the second, C-A the second's at home
inline std::vector<Contrast> cell_contrasts(const Config& c) {
  std::vector<Contrast> contrasts;
  if (c.type == FOUR_CELL) {
    contrasts.push_back({"A-B", {{0, 1}, {1, -1}}});
    contrasts.push_back({"C-D", {{2, 1}, {3, -1}}});
    contrasts.push_back({"(C-D)-(A-B)", {{2, 1}, {3, -1}, {0, -1}, {1, 1}}});
  } else if (c.type == KVAR_CELL) {
    for (int v = 1; v < (int)c.variants.size(); v++) {
      contrasts.push_back({variant_letter(v) + "-A", {{v, 1}, {0, -1}}});
    }
  } else if (c.type == CROSS_CELL) {
    contrasts.push_back({"B-A", {{1, 1}, {0, -1}}});
    contrasts.push_back({"D-C", {{3, 1}, {2, -1}}});
    contrasts.push_back({"(D-C)-(B-A)", {{3, 1}, {2, -1}, {1, -1}, {0, 1}}});
    contrasts.push_back({"C-A", {{2, 1}, {0, -1}}});
  }
  return contrasts;
}

}  // namespace suite
