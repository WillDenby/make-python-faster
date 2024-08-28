# ⚡ Just-in-Time with Numba

We’ve seen how PyPy uses JIT as an alternative Python interpreter / runner. Numba, however, uses decorators to indicate which functions should be compiled. When a decorated function is called, Numba compiles it to machine code ahead of execution. This compiled code can be directly executed by the CPU, unlocking significant performance improvements for intense computational tasks.

Numba is particularly effective for functions that perform operations on NumPy arrays, or for loops that can't be easily vectorised. It works cross-platform, on all major OSes and architectures.

## Using Numba 

Let’s look at a basic example, comparing the performance of standard Python vs. A JIT-compiled Python using Numba:

Here’s the standard Python function:

```python
import numpy as np
from time import time

def sum_array(arr):
    result = 0
    for x in arr:
        result += x
    return result

arr = np.arange(100000000)
start_time = time()
sum_array(arr)
print("Standard Python:", time() - start_time, "seconds")
```

Now let’s use Numba. Install it with pip: `pip install numba`

Then, modify the function with Numba's JIT decorator:

```python
from numba import jit
import numpy as np
from time import time

@jit(nopython=True)
def sum_array_numba(arr):
    result = 0
    for x in arr:
        result += x
    return result

arr = np.arange(100000000)
start_time = time()
sum_array_numba(arr)
print("Numba JIT:", time() - start_time, "seconds")
```

In this example, `@jit(nopython=True)` is used to ensure that the function runs in "nopython”, and throws an error if it tries to fall back to the use of Python objects and functions. 

The performance gain with JIT compilation can be significant, especially for more complex numerical computations. And because the compilation can be selectively applied to performance-critical parts of the code, it allows a mix of rapid development and high execution speed.

## Considerations:

JIT compilation introduces a one-time, up-front overhead, which means Numba might not be beneficial for functions that are only called once, or if you are processing small datasets. And Numba does not support all Python features and libraries, so some code might need adaptation.

But in general, Numba can help you achieve execution speeds that rival or exceed those of code written in more traditionally performant languages like C or Fortran, without sacrificing the ease of use and flexibility of Python.


[Get PDF/ePub](https://makepythonfaster.gumroad.com/l/get)
