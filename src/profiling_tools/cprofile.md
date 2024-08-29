# 📊 cProfile

`cProfile` is a built-in profiler that provides a detailed breakdown of how much time your program spends in each function. It's great for getting an overview of which functions are the most time-consuming.

## Usage Example

Here’s a simple example of using `cProfile`:

```python
import cProfile
import re

def example_function():
    return re.compile("foo|bar")

if __name__ == "__main__":
    cProfile.run('example_function()')
```

This will output statistics about the time spent in each function, allowing you to identify which parts of your code are the slowest.



[Get PDF](https://makepythonfaster.gumroad.com/l/get)
