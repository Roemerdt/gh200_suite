// kernels the route binary can run
#include "kernel.h"
#include "kernels/k1_stream.h"
#include "kernels/k2_reuse.h"
#include "kernels/k3_gather.h"
#include "kernels/k3p_page_sparse.h"
#include "kernels/k4_graph.h"
#include "kernels/k5_stencil.h"
#include "kernels/k6_update.h"

namespace suite {

const std::vector<KernelEntry>& kernels() {
  static const std::vector<KernelEntry> all = {K1_STREAM, K2_REUSE,   K3_GATHER, K3P_PAGE_SPARSE,
                                               K4_GRAPH,  K5_STENCIL, K6_UPDATE};
  return all;
}

}  // namespace suite
