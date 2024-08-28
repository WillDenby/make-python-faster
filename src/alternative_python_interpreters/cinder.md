# 🔥 Cinder

Cinder is Meta's performance-oriented fork of CPython 3.8. It incorporates several enhancements aimed at improving the performance of Python code, notably in highly concurrent server environments. It features an experimental, opt-in type system in order to compile Python to more efficient code. Modules can be declared with strict performance characteristics, to allow for further optimisation. 

You can find installation instructions here: [https://github.com/facebookincubator/cinder](https://github.com/facebookincubator/cinder)

Using Cinder is similar to standard Python, but benefiting from its features can require adopting specific patterns or annotations in your code, such as using static types:

```python
from static import int64

def fib(n: int64) -> int64:
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```



