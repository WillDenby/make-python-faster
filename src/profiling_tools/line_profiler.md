# 📈 line_profiler

`line_profiler` is an 3rd party tool that goes into more detail than `cProfile`, by showing how much time is spent on each line of your code. 

## Usage Example

Install it with: `pip install line_profiler`, and then run:

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

This code snippet wraps the function to profile, and then prints the statistics to the terminal. 

