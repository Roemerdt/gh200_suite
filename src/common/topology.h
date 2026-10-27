// node topology, fixed at build time and overridden by -DSUITE_... in the Makefile's SITE_DEFS
#pragma once
#include <cstddef>

#ifndef SUITE_CPU_NODE
#define SUITE_CPU_NODE 0
#endif
#ifndef SUITE_GPU_NODE
#define SUITE_GPU_NODE 1
#endif
#ifndef SUITE_TIMED_CORE
// core of the timed thread
// core 0 also takes the node's interrupts
#define SUITE_TIMED_CORE 0
#endif
#ifndef SUITE_THP_BYTES
#define SUITE_THP_BYTES (512ull << 20)
#endif
#ifndef SUITE_SMS
// streaming multiprocessors of the GPU, for launch shapes in waves
#define SUITE_SMS 132
#endif

namespace suite {

static const int CPU_NODE = SUITE_CPU_NODE;
static const int GPU_NODE = SUITE_GPU_NODE;
static const int TIMED_CORE = SUITE_TIMED_CORE;
static const size_t THP_BYTES = SUITE_THP_BYTES;
static const int SMS = SUITE_SMS;

}  // namespace suite
