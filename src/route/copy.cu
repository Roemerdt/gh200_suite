#include <cstdio>
#include <cstdlib>

#include "config.h"
#include "copy.h"

namespace suite {

static const int COPY_KERNEL_BLOCKS = SMS * 8, COPY_KERNEL_THREADS = 256;

size_t CopyConfig::chunk_bytes() const {
  if (chunk == "whole") { return 0; }
  return (size_t)atoi(chunk.c_str()) << 20;
}

std::string CopyConfig::label() const {
  return mechanism + "-" + memory + "-" + std::to_string(streams) + "-" + chunk + "-" + pipeline +
         "-" + form + (out == "kernel" ? "-kernel" : "");
}

CopyConfig CopyConfig::parse(const std::string& label, const char* flag) {
  const std::vector<std::string> f = split(label, '-');
  const char* reason =
      "is not "
      "<ce|kernel>-<pageable|registered>-<1|2|4>-<whole|4m|16m|64m|256m>-<none|pipe>-<whole|"
      "touched>[-kernel]";
  if (f.size() != 6 && f.size() != 7) { bad_flag_value(flag, label, reason); }
  CopyConfig c;
  c.mechanism = f[0];
  c.memory = f[1];
  c.streams = atoi(f[2].c_str());
  c.chunk = f[3];
  c.pipeline = f[4];
  c.form = f[5];
  c.out = f.size() == 7 ? f[6] : "ce";
  const bool ok = (c.mechanism == "ce" || c.mechanism == "kernel") &&
                  (c.memory == "pageable" || c.memory == "registered") &&
                  (c.streams == 1 || c.streams == 2 || c.streams == 4) &&
                  (c.chunk == "whole" || c.chunk == "4m" || c.chunk == "16m" || c.chunk == "64m" ||
                   c.chunk == "256m") &&
                  (c.pipeline == "none" || c.pipeline == "pipe") &&
                  (c.form == "whole" || c.form == "touched") &&
                  (c.out == "kernel" || (f.size() == 6 && c.out == "ce"));
  if (!ok) { bad_flag_value(flag, label, reason); }
  if (c.streams > 1 && (c.memory != "registered" || c.mechanism != "ce")) {
    bad_flag_value(flag, label,
                   "uses several streams, which only registered memory with the copy engine does");
  }
  if (c.pipeline == "pipe" && c.chunk == "whole") {
    bad_flag_value(flag, label, "pipelines without chunks");
  }
  return c;
}

bool CopyConfig::copy_out_matters(const RouteKernel& kernel) {
  const size_t delivered = kernel.delivered_words() * sizeof(u64);
  return delivered >= ((size_t)1 << 20) &&
         delivered * 64 >= kernel.touched_lines() * GPU_LINE_BYTES;
}

std::vector<CopyConfig> CopyConfig::space(const RouteKernel& kernel) {
  std::vector<CopyConfig> all;
  u64 period, width, offset;
  const bool touched = kernel.touched_window(0, &period, &width, &offset);
  const std::vector<std::string> forms = kernel.input_is_window()
                                             ? std::vector<std::string>{"touched"}
                                         : touched ? std::vector<std::string>{"whole", "touched"}
                                                   : std::vector<std::string>{"whole"};
  const std::vector<std::string> outs = copy_out_matters(kernel)
                                            ? std::vector<std::string>{"ce", "kernel"}
                                            : std::vector<std::string>{"ce"};
  for (const char* mechanism : {"ce", "kernel"}) {
    for (const char* memory : {"pageable", "registered"}) {
      for (int streams : {1, 2, 4}) {
        if (streams > 1 &&
            (std::string(memory) != "registered" || std::string(mechanism) != "ce")) {
          continue;
        }
        for (const char* chunk : {"whole", "4m", "16m", "64m", "256m"}) {
          for (const char* pipeline : {"none", "pipe"}) {
            if (std::string(pipeline) == "pipe" &&
                (std::string(chunk) == "whole" || !kernel.supports_parts())) {
              continue;
            }
            for (const std::string& form : forms) {
              for (const std::string& out : outs) {
                CopyConfig c;
                c.mechanism = mechanism;
                c.memory = memory;
                c.streams = streams;
                c.chunk = chunk;
                c.pipeline = pipeline;
                c.form = form;
                c.out = out;
                all.push_back(c);
              }
            }
          }
        }
      }
    }
  }
  return all;
}

// pair by pair, grid-stride, thread 0 takes an odd last word
__global__ void copy_whole_kernel(const u64* src, u64* dst, u64 words) {
  const u64 n = (u64)gridDim.x * blockDim.x, pairs = words / 2;
  const ulonglong2* s2 = (const ulonglong2*)src;
  ulonglong2* d2 = (ulonglong2*)dst;
  for (u64 i = (u64)blockIdx.x * blockDim.x + threadIdx.x; i < pairs; i += n) { d2[i] = s2[i]; }
  if (words % 2 && blockIdx.x == 0 && threadIdx.x == 0) { dst[words - 1] = src[words - 1]; }
}

// pair p lies in touched line q = p / 8 of the region, which is line
// (q / width) * period + (q % width + offset) mod period
__global__ void copy_touched_kernel(const u64* src, u64* dst, u64 lines, u64 period, u64 width,
                                    u64 offset, u64 pairs_to_visit) {
  const u64 n = (u64)gridDim.x * blockDim.x;
  for (u64 p = (u64)blockIdx.x * blockDim.x + threadIdx.x; p < pairs_to_visit; p += n) {
    const u64 q = p / (GPU_LINE_WORDS / 2);
    const u64 group = q / width;
    u64 r = q - group * width + offset;
    if (r >= period) { r -= period; }
    const u64 line = group * period + r;
    if (line < lines) {
      const u64 w = line * GPU_LINE_WORDS + (p % (GPU_LINE_WORDS / 2)) * 2;
      *(ulonglong2*)(dst + w) = *(const ulonglong2*)(src + w);
    }
  }
}

// one pitched copy of width lines per group, two when the window wraps, then the partial group
static void copy_touched_engine(const u64* host, u64* device, const CopyRegion& r, cudaStream_t s) {
  const u64 groups = r.count / r.period, tail_lines = r.count % r.period;
  auto piece = [&](u64 from, u64 lines_per_group) {
    if (groups > 0) {
      CU(cudaMemcpy2DAsync(device + (r.first + from) * GPU_LINE_WORDS, r.period * GPU_LINE_BYTES,
                           host + (r.first + from) * GPU_LINE_WORDS, r.period * GPU_LINE_BYTES,
                           lines_per_group * GPU_LINE_BYTES, groups, cudaMemcpyHostToDevice, s));
    }
    // the window's lines that exist in the partial last group
    for (u64 l = from; l < from + lines_per_group && l < tail_lines; l++) {
      const u64 line = r.first + groups * r.period + l;
      CU(cudaMemcpyAsync(device + line * GPU_LINE_WORDS, host + line * GPU_LINE_WORDS,
                         GPU_LINE_BYTES, cudaMemcpyHostToDevice, s));
    }
  };
  if (r.offset + r.width <= r.period) {
    piece(r.offset, r.width);
  } else {
    piece(r.offset, r.period - r.offset);
    piece(0, r.offset + r.width - r.period);
  }
}

void copy_region(const CopyConfig& c, const u64* host, u64* device, const CopyRegion& r,
                 cudaStream_t s) {
  if (r.count == 0) { return; }
  const u64 first_word = r.first * GPU_LINE_WORDS, words = r.count * GPU_LINE_WORDS;
  if (c.form == "whole") {
    if (c.mechanism == "ce") {
      CU(cudaMemcpyAsync(device + first_word, host + first_word, words * sizeof(u64),
                         cudaMemcpyHostToDevice, s));
    } else {
      copy_whole_kernel<<<COPY_KERNEL_BLOCKS, COPY_KERNEL_THREADS, 0, s>>>(
          host + first_word, device + first_word, words);
    }
    return;
  }
  if (c.mechanism == "ce") {
    copy_touched_engine(host, device, r, s);
  } else {
    const u64 pairs = (r.count + r.period - 1) / r.period * r.width * (GPU_LINE_WORDS / 2);
    copy_touched_kernel<<<COPY_KERNEL_BLOCKS, COPY_KERNEL_THREADS, 0, s>>>(
        host + first_word, device + first_word, r.count, r.period, r.width, r.offset, pairs);
  }
}

void copy_out_words(const CopyConfig& c, const u64* device, u64* host, u64 words, cudaStream_t s) {
  if (words == 0) { return; }
  if (c.out == "ce") {
    CU(cudaMemcpyAsync(host, device, words * sizeof(u64), cudaMemcpyDeviceToHost, s));
  } else {
    copy_whole_kernel<<<COPY_KERNEL_BLOCKS, COPY_KERNEL_THREADS, 0, s>>>(device, host, words);
  }
}

}  // namespace suite
