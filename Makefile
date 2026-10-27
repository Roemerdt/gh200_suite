# HOST_ARCH armv9-a for the inline LSE atomics
# SITE_DEFS for -DSUITE_...=... topology overrides (src/common/topology.h)
NVCC      ?= nvcc
ARCH      ?= sm_90
HOST_ARCH ?= armv9-a
SITE_DEFS ?=
SITE_SMMU_PMU ?= $(shell sh -c '. harness/site.env && printf %s "$$SITE_SMMU_PMU"')
SITE_FLAGS  = -DSUITE_SMMU_PMU=\"$(SITE_SMMU_PMU)\" $(SITE_DEFS)
NVCCFLAGS ?= -O2 -std=c++17 -arch=$(ARCH) -Isrc -Xcompiler -pthread -Xcompiler -march=$(HOST_ARCH) -lineinfo $(SITE_FLAGS)
NVCPP     ?= nvc++
NVCPPFLAGS?= -cuda -gpu=$(patsubst sm_%,cc%,$(ARCH)) -O2 -std=c++17 -Isrc -tp=neoverse-v2 --diag_suppress=cuda_compile $(SITE_FLAGS)
LDLIBS     = -ldl
INSTR      = shakedown
HEADERS    = $(wildcard src/common/*.h)
ROUTE_SRC  = $(wildcard src/route/*.cu src/route/kernels/*.cu)
ROUTE_HDR  = $(wildcard src/route/*.h src/route/kernels/*.h)
vpath %.cu src/tools

all: $(INSTR:%=bin/%) bin/route build_flags.txt

bin/%: %.cu $(HEADERS)
	@mkdir -p bin
	$(NVCC) $(NVCCFLAGS) -o $@ $< $(LDLIBS)

# the driver plus one file per kernel
bin/route: $(ROUTE_SRC) $(ROUTE_HDR) $(HEADERS)
	@mkdir -p bin
	$(NVCC) $(NVCCFLAGS) -Isrc/route -o $@ $(ROUTE_SRC) $(LDLIBS)

# compiler spot check, shakedown through NVHPC (the route binary is nvcc only)
nvcpp: $(INSTR:%=bin/%_nvcpp)
bin/%_nvcpp: %.cu $(HEADERS)
	@mkdir -p bin
	$(NVCPP) $(NVCPPFLAGS) -o $@ $< $(LDLIBS)

build_flags.txt: Makefile
	@{ echo "NVCC=$(NVCC)"; echo "NVCCFLAGS=$(NVCCFLAGS)"; echo "NVCPP=$(NVCPP)"; echo "NVCPPFLAGS=$(NVCPPFLAGS)"; \
	   $(NVCC) --version 2>/dev/null | tail -2; $(NVCPP) --version 2>/dev/null | head -2; \
	   gcc --version | head -1; } > $@

clean:
	rm -rf bin build_flags.txt

# clang-format with the repository's .clang-format
CLANG_FORMAT ?= clang-format
SOURCES       = $(wildcard src/*/*.cu src/*/*.h src/*/*/*.cu src/*/*/*.h)
format:
	$(CLANG_FORMAT) -i $(SOURCES)
format-check:
	$(CLANG_FORMAT) --dry-run -Werror $(SOURCES)

.PHONY: all nvcpp clean format format-check
