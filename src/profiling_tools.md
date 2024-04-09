# 🔎 Profiling Tools

It's tempting to just dive into your code and start refactoring immediately! But you might end up spending lots of time eeking out tiny performance gains on parts of your code that are already pretty efficient - and completely missing the real bottlenecks. That's why we start with profiling. 

Figure out **where** and **how bad** the problems are. Then, you can make an evidence-based request for more time from your manager. 

Here are resources you might want to profile in terms of usage:

- CPU
- Memory
- Network bandwidth
- Disk IO

And here are some best practices:

1. **Isolate the Code You Want to Benchmark** - Make sure that the code you're benchmarking is isolated from setup and teardown operations that you don't intend to measure. 
2. **Choose the Right Tool for the Job** - As we'll see, `timeit` is great for micro-benchmarks, while `cProfile` and `line_profiler` can help with more detailed profiling.
3. **Warm-up the Python Runtime** - Before running your benchmarks, "warm up" the Python interpreter by running your code a few times without measuring it. This process can help mitigate the impact of caching and other optimizations that the interpreter might perform.
4. **Run Benchmarks Multiple Times** - To get a more accurate measure, run your benchmarks multiple times and consider using the average time. This approach helps smooth out any irregularities caused by background processes or other anomalies.
5. **Consider Systematic Variations** - Be aware of external factors that can affect benchmark results, such as other running processes, system load, and hardware differences. Try to minimize these variations when benchmarking.
6. **Benchmark with Realistic Data** - Test your code with data that closely resembles what you expect in production. The performance can greatly differ based on the type, size, and complexity of the input data.

One thing to always remember is that profiling can add to the computer workload, and hence slow things down artificially. 

There are many tools and techniques available for profiling, each with their own strengths and use cases. In the next few pages we'll check out some of the most commonly used ones, along with code examples.
