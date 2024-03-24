# 📈 line_profiler

`line_profiler` is an external tool that goes into more detail than cProfile by showing how much time is spent on each line of your code. This is especially useful for fine-tuning performance by identifying slow lines in functions.

**Usage Example:**

Install it with: `pip install line_profiler`

```python
from line_profiler import LineProfiler

def do_some_operations():
    [x**2 for x in range(10000)]  # Example operation

if __name__ == '__main__':
    lp = LineProfiler()
    lp_wrapper = lp(do_some_operations)
    lp_wrapper()
    lp.print_stats()
```

You need to wrap the function you want to profile and then print the statistics.