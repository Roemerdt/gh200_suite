// K2 reuse, one block per SM rereading its slice of an input window k times per pass
#pragma once
#include "../kernel.h"

namespace suite {

extern const KernelEntry K2_REUSE;

}  // namespace suite
