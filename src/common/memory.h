// Buffers bound to a NUMA node, or device memory, and checks of where their pages are
#pragma once
#include <errno.h>
#include <linux/mempolicy.h>
#include <sys/mman.h>
#include <sys/syscall.h>
#include <unistd.h>

#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>

#include <cuda_runtime.h>

#include "cuda_check.h"
#include "topology.h"

#if !defined(SYS_mbind) || !defined(SYS_move_pages)
#error "SYS_mbind / SYS_move_pages not provided by <sys/syscall.h> on this system"
#endif
#ifndef MADV_HUGEPAGE
#error "MADV_HUGEPAGE not provided by <sys/mman.h> on this system"
#endif

namespace suite {

static const int RESIDENCY_SAMPLES = 256;  // pages checked with move_pages around every interval

static inline size_t page_bytes() {
  static const size_t p = (size_t)sysconf(_SC_PAGESIZE);
  return p;
}

static inline size_t round_up(size_t value, size_t multiple) {
  return (value + multiple - 1) / multiple * multiple;
}

enum class Alloc { System, Device };

struct Buffer {
  void* p = nullptr;    // usable base
  void* raw = nullptr;  // mmap base (system memory only)
  size_t mapsz = 0;     // bytes mapped (system memory only)
  size_t size = 0;      // bytes the binary uses
  Alloc kind = Alloc::System;
  int node = -1;  // NUMA node the memory is bound to
  int thp = 0;    // 1: 512 MB transparent huge pages requested
};

[[noreturn]] static inline void fail(const char* what) {
  perror(what);
  exit(1);
}

static inline size_t mapping_alignment(int thp, size_t align_bytes) {
  const size_t natural = thp ? THP_BYTES : page_bytes();
  if (align_bytes == 0) { return natural; }
  if ((align_bytes & (align_bytes - 1)) != 0 || align_bytes < natural) {
    fprintf(stderr, "alignment %zu is not a power of two of at least %zu bytes\n", align_bytes,
            natural);
    exit(2);
  }
  return align_bytes;
}

// mmap, then mbind(MPOL_BIND, node). A huge page only backs a mapping that holds it whole, so
// under thp the used range is whole 512 MB-aligned pages (a 256 MiB footprint maps 512 MiB),
// madvised and bound as a whole. The kernel allocates the huge pages on first touch
// an aligned start maps one alignment unit extra and takes the first aligned address inside
// node -1 leaves the mapping unbound
static inline Buffer sys_alloc(size_t size, int node, int thp, size_t align_bytes = 0,
                               size_t offset_bytes = 0, void* hint = nullptr) {
  const int max_node = 8 * (int)sizeof(unsigned long) - 1;  // mbind takes the node as one bit
  if (node < -1 || node > max_node) {
    fprintf(stderr, "NUMA node %d is outside 0..%d\n", node, max_node);
    exit(2);
  }
  const size_t align = mapping_alignment(thp, align_bytes);
  const size_t len = thp ? round_up(size, THP_BYTES) : size;
  const bool over_map = thp || align_bytes != 0 || offset_bytes != 0;
  if (offset_bytes % (thp ? THP_BYTES : page_bytes()) != 0) {
    fprintf(stderr, "start offset %zu is not a multiple of the page size\n", offset_bytes);
    exit(2);
  }

  Buffer b;
  b.kind = Alloc::System;
  b.node = node;
  b.thp = thp;
  b.size = size;
  b.mapsz = len + offset_bytes + (over_map ? align : 0);
  b.raw = mmap(hint, b.mapsz, PROT_READ | PROT_WRITE,
               MAP_PRIVATE | MAP_ANONYMOUS | MAP_NORESERVE, -1, 0);
  if (b.raw == MAP_FAILED) { fail("mmap"); }
  b.p = (char*)(((uintptr_t)b.raw + (align - 1)) & ~(uintptr_t)(align - 1)) + offset_bytes;

  if (thp && madvise(b.p, len, MADV_HUGEPAGE) != 0) { fail("madvise(MADV_HUGEPAGE)"); }
  if (node < 0) { return b; }
  unsigned long node_mask = 1ul << node;
  if (syscall(SYS_mbind, b.p, len, MPOL_BIND, &node_mask, sizeof(node_mask) * 8, 0) != 0) {
    fail("mbind");
  }
  return b;
}

static inline Buffer device_alloc(size_t size) {
  Buffer b;
  b.kind = Alloc::Device;
  b.size = size;
  b.node = GPU_NODE;
  CU(cudaMalloc(&b.p, size));
  return b;
}

static inline void free_buffer(Buffer& b) {
  if (!b.p) { return; }
  if (b.kind == Alloc::System) {
    munmap(b.raw, b.mapsz);
  } else {
    CU(cudaFree(b.p));
  }
  b.p = nullptr;
  b.raw = nullptr;
}

// detail: OK | NA_DEVICE | MOVED[k/n;first=i:status] | move_pages_errno=N
struct Residency {
  bool ok;
  std::string detail;
};

// RESIDENCY_SAMPLES page addresses spread evenly over the buffer, first and last page included
static inline std::vector<void*> sampled_pages(const Buffer& b) {
  const size_t pages_in_buffer = b.size / page_bytes() > 0 ? b.size / page_bytes() : 1;
  const size_t samples =
      pages_in_buffer < (size_t)RESIDENCY_SAMPLES ? pages_in_buffer : (size_t)RESIDENCY_SAMPLES;
  std::vector<void*> pages;
  pages.reserve(samples);
  for (size_t i = 0; i < samples; i++) {
    const size_t page = (samples == 1) ? 0 : (pages_in_buffer - 1) * i / (samples - 1);
    pages.push_back((char*)b.p + page * page_bytes());
  }
  return pages;
}

// device memory is not a process mapping, hence NA_DEVICE
static inline Residency residency_check(const Buffer& b) {
  if (b.kind == Alloc::Device) { return Residency{true, "NA_DEVICE"}; }
  std::vector<void*> pages = sampled_pages(b);
  std::vector<int> node_of_page(pages.size(), 0);
  if (syscall(SYS_move_pages, 0, (unsigned long)pages.size(), pages.data(), (void*)0,
              node_of_page.data(), 0) != 0) {
    return Residency{false, "move_pages_errno=" + std::to_string(errno)};
  }
  size_t moved = 0, first_moved = 0;
  int first_status = 0;
  for (size_t i = 0; i < pages.size(); i++) {
    if (node_of_page[i] == b.node) { continue; }
    if (moved == 0) {
      first_moved = i;
      first_status = node_of_page[i];
    }
    moved++;
  }
  if (moved == 0) { return Residency{true, "OK"}; }
  char detail[96];
  snprintf(detail, sizeof detail, "MOVED[%zu/%zu;first=%zu:%d]", moved, pages.size(), first_moved,
           first_status);
  return Residency{false, detail};
}

// MemFree of a NUMA node in bytes, 0 if unreadable
static inline size_t node_free_bytes(int node) {
  char path[96];
  snprintf(path, sizeof path, "/sys/devices/system/node/node%d/meminfo", node);
  FILE* f = fopen(path, "r");
  if (!f) { return 0; }
  size_t kb = 0;
  char line[256];
  while (fgets(line, sizeof line, f)) {
    const char* key = strstr(line, "MemFree:");
    if (key && sscanf(key + 8, "%zu", &kb) == 1) { break; }
  }
  fclose(f);
  return kb * 1024;
}

// AnonHugePages in kB of the smaps entry holding addr, -1 if not found
static inline long smaps_anon_huge_kb(void* addr) {
  FILE* f = fopen("/proc/self/smaps", "r");
  if (!f) { return -1; }
  const uintptr_t a = (uintptr_t)addr;
  bool inside = false;
  long kb = -1;
  char line[512];
  while (fgets(line, sizeof line, f)) {
    unsigned long lo, hi;
    if (strchr(line, '-') && sscanf(line, "%lx-%lx", &lo, &hi) == 2) {
      inside = (a >= lo && a < hi);
    } else if (inside && strncmp(line, "AnonHugePages:", 14) == 0) {
      sscanf(line + 14, "%ld", &kb);
      break;
    }
  }
  fclose(f);
  return kb;
}

}  // namespace suite
