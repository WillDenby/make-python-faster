# 🔎 Profiling Tools

If your software or product is getting complaints about, say, speed, it’s tempting to dive into your code and start refactoring immediately! 

But you need to know where to look. If you start refactoring parts of your codebase that are already quite efficient, you may only achieve a tiny performance gain after several hours of work, but you’ll have completely missed the actual bottlenecks. 

That's why we start with profiling. In a product context, by figuring out *where* and *how bad* the problems are, you can also make an evidence-based request to spend more time on optimisation.

Here are resources you might want to profile in terms of usage:

- CPU
- Memory
- Network bandwidth
- Disk IO

In this book I’ll mostly focus on the first two, as optimising the latter can move into the realm of infrastructure, as well as code. But in general, these are good practices for profiling any resource:

**Isolate the code you want to benchmark**: Make sure that the code you're benchmarking is isolated from setup and teardown operations that you don't intend to measure. 

**Start at a higher altitude**: Start with micro-benchmarks, before moving into more detailed profiling.

**Warm up the runtime (or not!)**: Running your code a few times before benchmarking lets your interpreter perform its own optimisations, such as caching. The exception is if you want to measure “cold start” performance. 

**Run your code multiple times**: Taking the average smooths out any irregularities caused by background processes or other anomalies. But do also check the max - this may explain occasional user frustration.

**Use representative data and environments**: Benchmark in a way relevant to the originator of the performance complaint. You can make a judgement call about whether it’s worth worrying about certain hardware setups, for example. 

Finally, remember that profiling can add to the computer workload, and hence slow things down artificially. 


