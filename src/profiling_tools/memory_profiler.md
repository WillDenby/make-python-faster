# 🧠 memory_profiler

`memory_profiler` monitors the memory usage of your application, which can be crucial for identifying memory leaks or functions that use more memory than expected.

**Usage Example:**

Install it with: `pip install memory_profiler`

```python
from memory_profiler import profile

@profile
def my_func():
    a = [1] * (10**6)
    b = [2] * (2 * 10**7)
    del b
    return a

if __name__ == '__main__':
    my_func()
```

This decorates a function to profile its memory usage line by line.