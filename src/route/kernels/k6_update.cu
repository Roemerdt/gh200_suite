#include <cstdio>
#include <memory>
#include <thread>
#include <vector>

#include <cuda/atomic>

#include "../host_phase.h"
#include "k6_update.h"

namespace suite {

enum K6UpdateKind { UPDATE_ATOMIC = 0, UPDATE_PLAIN = 1, UPDATE_RETURNED = 2, UPDATE_STADD = 3 };
static const u64 K6_INCREMENT = 3;
static const u64 K6_KEYS_PER_PASS = 1 << 24;  // updates per pass at the contended levels
static const size_t K6_MIN_UPDATE_BYTES =
    256ull << 20;  // a pass sweeps its table until this many bytes were updated

template <int UPDATE>
__device__ __forceinline__ u64 update_slot(u64* slot, u64 add) {
  if (UPDATE == UPDATE_ATOMIC) {
    atomicAdd((unsigned long long*)slot, (unsigned long long)add);
    return 0;
  }
  if (UPDATE == UPDATE_PLAIN) {
    cuda::atomic_ref<u64, cuda::thread_scope_device> r(*slot);
    r.store(r.load(cuda::std::memory_order_relaxed) + add, cuda::std::memory_order_relaxed);
    return 0;
  }
  return (u64)atomicAdd((unsigned long long*)slot, (unsigned long long)add);
}

// zero contention. Thread t updates slots t, t + n, ... in the warp layout, or one 128 B line per
// thread at slots t * 16, (t + n) * 16, ... in the line layout, each slot repeat times per sweep
// the returned values feed a sink that is never written, which keeps the round trip
template <int UPDATE>
__global__ void k6_update_kernel(u64* table, u64 slots, u64 stride, int repeat, int sweeps, u64 tag,
                                 u64* sink) {
  const u64 n = (u64)gridDim.x * blockDim.x;
  u64 acc = 0;
  for (int sweep = 0; sweep < sweeps; sweep++) {
    for (u64 i = (u64)blockIdx.x * blockDim.x + threadIdx.x; i * stride < slots; i += n) {
      for (int r = 0; r < repeat; r++) {
        acc += update_slot<UPDATE>(table + i * stride, K6_INCREMENT);
      }
    }
  }
  if (blockIdx.x == 0 && threadIdx.x == 0) { update_slot<UPDATE>(table, tag); }
  if (acc == 0x123456789ull) { sink[0] = acc; }
}

// contended, update u adds one to table[key[u]] directly, once per warp for the lanes sharing
// the key, or through a per-block copy in shared memory merged at the end
template <int STRATEGY>
__global__ void k6_contended_kernel(u64* table, u64 entries, const u64* keys, u64 updates,
                                    u64 tag) {
  extern __shared__ u64 priv[];
  if (STRATEGY == 2) {
    for (u64 e = threadIdx.x; e < entries; e += blockDim.x) { priv[e] = 0; }
    __syncthreads();
  }
  const u64 n = (u64)gridDim.x * blockDim.x;
  for (u64 u = (u64)blockIdx.x * blockDim.x + threadIdx.x; u < updates; u += n) {
    const u64 key = keys[u];
    if (STRATEGY == 0) {
      atomicAdd((unsigned long long*)&table[key], 1ull);
    } else if (STRATEGY == 1) {
      const unsigned peers = __match_any_sync(__activemask(), key);
      const int leader = __ffs((int)peers) - 1;
      if ((int)(threadIdx.x % 32) == leader) {
        atomicAdd((unsigned long long*)&table[key], (unsigned long long)__popc(peers));
      }
    } else {
      atomicAdd((unsigned long long*)&priv[key], 1ull);
    }
  }
  if (STRATEGY == 2) {
    __syncthreads();
    for (u64 e = threadIdx.x; e < entries; e += blockDim.x) {
      if (priv[e]) { atomicAdd((unsigned long long*)&table[e], (unsigned long long)priv[e]); }
    }
  }
  if (blockIdx.x == 0 && threadIdx.x == 0) {
    atomicAdd((unsigned long long*)table, (unsigned long long)tag);
  }
}

// UPDATE_ATOMIC is an LSE ldadd whose result is discarded, unlike the non-returning stadd
static inline void cpu_update(u64* p, u64 add, int kind, u64* sink) {
#if defined(__aarch64__)
  if (kind == UPDATE_PLAIN) {
    volatile u64* q = p;
    *q = *q + add;
  } else if (kind == UPDATE_STADD) {
    asm volatile("stadd %x0, [%x1]" : : "r"(add), "r"(p) : "memory");
  } else {
    u64 old;
    asm volatile("ldadd %x1, %x0, [%x2]" : "=&r"(old) : "r"(add), "r"(p) : "memory");
    if (kind == UPDATE_RETURNED) { *sink += old; }
  }
#else
  if (kind == UPDATE_PLAIN) {
    volatile u64* q = p;
    *q = *q + add;
  } else {
    const u64 old = __atomic_fetch_add(p, add, __ATOMIC_RELAXED);
    if (kind == UPDATE_RETURNED) { *sink += old; }
  }
#endif
}

class K6Update : public RouteKernel {
  u64 slots_, keys_, repeat_, sweeps_;
  int kind_, writers_;
  std::string update_, strategy_, layout_, issuer_;
  LaunchShape shape_;
  u64* d_keys_ = nullptr;
  u64* d_sink_ = nullptr;
  bool owns_device_ = true;
  u64 base_sum_ = 0, increment_sum_ = 0;
  // passes launched on the table so far, shared by every attached instance since the table
  // carries all their updates. Tags and the expected checksum follow this count
  std::shared_ptr<u64> launches_ = std::make_shared<u64>(0);

  u64 stride() const { return layout_ == "line" ? GPU_LINE_WORDS : 1; }
  u64 updated_slots() const { return (slots_ + stride() - 1) / stride(); }
  // sum of the tags after n passes, each pass adds its own
  u64 tags_through(u64 n) const { return n * (n + 1) / 2; }

  // whole lines per writer thread, so no line is shared between threads
  void cpu_pass(u64* table, u64 tag) const {
    std::vector<std::thread> threads;
    std::vector<u64> sinks(writers_, 0);
    for (int w = 0; w < writers_; w++) {
      threads.emplace_back([this, table, w, &sinks]() {
        pin_to_core(WRITER_CORE_FIRST + w);
        const u64 st = stride(), n = updated_slots();
        const u64 per_line = GPU_LINE_WORDS / st, lines = (n + per_line - 1) / per_line;
        const u64 begin = std::min(n, lines * w / writers_ * per_line),
                  end = std::min(n, lines * (w + 1) / writers_ * per_line);
        for (u64 sweep = 0; sweep < sweeps_; sweep++) {
          for (u64 i = begin; i < end; i++) {
            for (u64 r = 0; r < repeat_; r++) {
              cpu_update(table + i * st, K6_INCREMENT, kind_, &sinks[w]);
            }
          }
        }
      });
    }
    for (std::thread& t : threads) { t.join(); }
    u64 sink = 0;
    cpu_update(table, tag, kind_ == UPDATE_PLAIN ? UPDATE_PLAIN : UPDATE_ATOMIC, &sink);
    volatile u64 keep = sinks[0];
    (void)keep;
  }

 public:
  K6Update(size_t input_bytes, const std::string& update, long keys, const std::string& strategy,
           const std::string& layout, long repeat, const std::string& issuer, int writers,
           LaunchShape shape)
      : slots_(input_bytes / 8),
        keys_((u64)keys),
        repeat_((u64)repeat),
        writers_(writers),
        update_(update),
        strategy_(strategy),
        layout_(layout),
        issuer_(issuer),
        shape_(shape) {
    sweeps_ = std::max((u64)1, (u64)(K6_MIN_UPDATE_BYTES / input_bytes));
    kind_ = update == "plain"      ? UPDATE_PLAIN
            : update == "returned" ? UPDATE_RETURNED
            : update == "stadd"    ? UPDATE_STADD
                                   : UPDATE_ATOMIC;
    if (keys_ > 0 && keys_ > slots_) {
      fprintf(stderr, "--keys exceeds the table\n");
      exit(2);
    }
    if (keys_ > 0 && strategy_ == "private" && keys_ > 1024) {
      fprintf(stderr, "--strategy private needs a table of at most 1024 entries\n");
      exit(2);
    }
    if (issuer_ == "cpu" && keys_ > 0) {
      fprintf(stderr, "CPU-issued updates run the zero-contention level only\n");
      exit(2);
    }
    if (issuer_ != "cpu" && update_ == "stadd") {
      fprintf(stderr, "--update stadd is a CPU instruction (--issuer cpu)\n");
      exit(2);
    }
  }
  ~K6Update() {
    if (!owns_device_) { return; }
    if (d_keys_) { CU(cudaFree(d_keys_)); }
    if (d_sink_) { CU(cudaFree(d_sink_)); }
  }

  const char* name() const override { return "k6"; }
  std::string knob_header() const override {
    return "update,keys,strategy,layout,repeat,issuer,sweeps,slots";
  }
  std::string knob_values() const override {
    return update_ + "," + std::to_string(keys_) + "," + strategy_ + "," + layout_ + "," +
           std::to_string(repeat_) + "," + issuer_ + "," + std::to_string(sweeps_) + "," +
           std::to_string(slots_);
  }
  u64 touched_lines() const override {
    return keys_ > 0 ? (keys_ * 8 + GPU_LINE_BYTES - 1) / GPU_LINE_BYTES
                     : slots_ * 8 / GPU_LINE_BYTES;
  }
  size_t output_words() const override { return (size_t)slots_; }
  bool updates_in_place() const override { return true; }
  bool cpu_issued() const override { return issuer_ == "cpu"; }
  size_t device_bytes() const override { return keys_ > 0 ? K6_KEYS_PER_PASS * sizeof(u64) : 0; }
  // accepts the cell without a cursor, every pass updates the whole table
  // a table below the cursor threshold is the L2-resident or cache-resident level
  bool enable_cursor() override { return true; }
  std::vector<LaunchShape> shape_space() const override {
    if (keys_ > 0 && strategy_ == "private") {
      return {{SMS * 8, 256, 8}};
    }  // fixed by the private table
    return {};
  }

  void populate(u64* input) override {
    parallel_ranges(slots_, [&](unsigned, u64 begin, u64 end) {
      for (u64 i = begin; i < end; i++) { input[i] = word_value(i); }
    });
    std::vector<u64> sums(fill_workers(), 0);
    parallel_ranges(slots_, [&](unsigned worker, u64 begin, u64 end) {
      for (u64 i = begin; i < end; i++) { sums[worker] += word_value(i); }
    });
    base_sum_ = 0;
    for (u64 s : sums) { base_sum_ += s; }
    if (keys_ > 0) {
      std::vector<u64> keys(K6_KEYS_PER_PASS);
      uint64_t state = fnv1a64("k6:" + std::to_string(keys_));
      for (u64 u = 0; u < K6_KEYS_PER_PASS; u++) { keys[u] = splitmix64(state) % keys_; }
      CU(cudaMalloc(&d_keys_, K6_KEYS_PER_PASS * sizeof(u64)));
      CU(cudaMemcpy(d_keys_, keys.data(), K6_KEYS_PER_PASS * sizeof(u64), cudaMemcpyHostToDevice));
      increment_sum_ = K6_KEYS_PER_PASS;
    } else {
      increment_sum_ = updated_slots() * repeat_ * sweeps_ * K6_INCREMENT;
    }
    CU(cudaMalloc(&d_sink_, sizeof(u64)));
  }
  void attach(const RouteKernel& populated) override {
    const K6Update& other = dynamic_cast<const K6Update&>(populated);
    if (other.slots_ != slots_ || other.keys_ != keys_ || other.repeat_ != repeat_ ||
        other.layout_ != layout_) {
      refuse_attach("table or level");
    }
    d_keys_ = other.d_keys_;
    d_sink_ = other.d_sink_;
    owns_device_ = false;
    base_sum_ = other.base_sum_;
    increment_sum_ = other.increment_sum_;
    launches_ = other.launches_;
  }

  void launch(const u64* input, u64* output, u64, cudaStream_t s) const override {
    u64* table = output;  // updated in place, output is the input buffer
    (void)input;
    const u64 pass = (*launches_)++;
    if (issuer_ == "cpu") {
      cpu_pass(table, tag_of(pass));
      return;
    }
    if (keys_ > 0) {
      const size_t shared = strategy_ == "private" ? keys_ * sizeof(u64) : 0;
      if (strategy_ == "warp") {
        k6_contended_kernel<1><<<shape_.blocks, shape_.threads, 0, s>>>(
            table, keys_, d_keys_, K6_KEYS_PER_PASS, tag_of(pass));
      } else if (strategy_ == "private") {
        k6_contended_kernel<2><<<shape_.blocks, shape_.threads, shared, s>>>(
            table, keys_, d_keys_, K6_KEYS_PER_PASS, tag_of(pass));
      } else {
        k6_contended_kernel<0><<<shape_.blocks, shape_.threads, 0, s>>>(
            table, keys_, d_keys_, K6_KEYS_PER_PASS, tag_of(pass));
      }
      return;
    }
    if (kind_ == UPDATE_PLAIN) {
      k6_update_kernel<UPDATE_PLAIN><<<shape_.blocks, shape_.threads, 0, s>>>(
          table, slots_, stride(), (int)repeat_, (int)sweeps_, tag_of(pass), d_sink_);
    } else if (kind_ == UPDATE_RETURNED) {
      k6_update_kernel<UPDATE_RETURNED><<<shape_.blocks, shape_.threads, 0, s>>>(
          table, slots_, stride(), (int)repeat_, (int)sweeps_, tag_of(pass), d_sink_);
    } else {
      k6_update_kernel<UPDATE_ATOMIC><<<shape_.blocks, shape_.threads, 0, s>>>(
          table, slots_, stride(), (int)repeat_, (int)sweeps_, tag_of(pass), d_sink_);
    }
  }
  u64 expected_checksum(u64) const override {
    const u64 n = *launches_;
    return base_sum_ + n * increment_sum_ + tags_through(n);
  }
};

static std::unique_ptr<RouteKernel> make_k6(const Args& args, size_t input_bytes,
                                            LaunchShape shape) {
  const long keys = args.geti("keys", 0), repeat = args.geti("repeat", 1),
             writers = args.geti("writers", 16);
  if (keys < 0 || repeat < 1 || writers < 1 || writers > 64) {
    fprintf(stderr, "--keys must be 0 or more, --repeat at least 1 and --writers in 1..64\n");
    exit(2);
  }
  return std::unique_ptr<RouteKernel>(new K6Update(
      input_bytes, args.enum_arg("update", "atomic", {"atomic", "plain", "returned", "stadd"}),
      keys, args.enum_arg("strategy", "atomic", {"atomic", "warp", "private"}),
      args.enum_arg("layout", "warp", {"warp", "line"}), repeat,
      args.enum_arg("issuer", "gpu", {"gpu", "cpu"}), (int)writers, shape));
}

static void k6_set_level(Args& args, const std::string& factor, const std::string& level) {
  for (const char* f : {"update", "keys", "strategy", "layout", "repeat", "issuer"}) {
    if (factor == f) {
      args.set(factor, level);
      return;
    }
  }
  bad_flag_value("vary", factor,
                 "is not a factor of k6 (update, keys, strategy, layout, repeat, issuer)");
}

const KernelEntry K6_UPDATE = {"k6",
                               {"update", "keys", "strategy", "layout", "repeat", "issuer"},
                               {"update", "keys", "strategy", "layout", "repeat", "issuer"},
                               make_k6,
                               k6_set_level};

}  // namespace suite
