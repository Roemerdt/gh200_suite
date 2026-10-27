// K3P page-sparse gather of one 128 B line per 64 KB page, seeded offset and page order
// the cursor moves the offset one line per pass
#pragma once
#include "../kernel.h"

namespace suite {

extern const KernelEntry K3P_PAGE_SPARSE;

}  // namespace suite
