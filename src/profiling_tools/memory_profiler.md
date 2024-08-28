# 🧠 memory_profiler

`memory_profiler` monitors the memory usage of your application, enabling you to find functions that use more memory than expected, or use memory in an inefficient way. 

## Usage Example

Install it with: `pip install memory_profiler`

This snippet decorates a function to profile its memory usage line by line.

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

You can thereby use `memory_profiler` to identify where the space complexity of your code may need consideration. 


[Get PDF/ePub](https://makepythonfaster.gumroad.com/l/get)
