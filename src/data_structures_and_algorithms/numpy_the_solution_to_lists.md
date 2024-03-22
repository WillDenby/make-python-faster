# Numpy: the Solution to Lists

Python's native list structure has a problem for vector operations and matrix manipulations. Lists don't actually hold the data - instead, they hold **pointers** to the data location. The advantage of this is that the contents of a list can be heterogenous. However, it introduces a fetch/look-up overhead, and if you are doing lots of operations, this fragmentation adds up. 

What does this look like in hardware terms? Data needs to be moved from memory to the CPU. Modern computers can have tiered architectures, with DRAM, SRAM, external caches, and on-chip caches. CPUs can also do things like branch prediction, speculation, overlapped instruction fetching, pipelining, and superscalar execution. If you want to get into the weeds, you can use the Linux `perf` tool to do some profiling, looking for `cache-misses` (memory bound) and `page-faults` (disk/network bound). But we might as well be sensible with how we do things. 

### The Array Module?

Python offers an `array` module, that overcomes the memory fragementation issue by storing items sequentially. Iterating through an array therefore doesn't require multiple look-ups, as data can be cached (i.e. closer in terms of spatial and temporal locality to the CPU). But then we run into a different issue: Python, as a high-level interpreted language, isn't optimised for vector operations, and isn't good at dealing with the low-level implementation of `array`.

## Enter NumPy

NumPy stores items sequentially in memory AND offers optimised vector operations. It requires orders of magnitude less instructions, and gets more data onto the cache, closer to the CPU. It also has a relatively concise syntax, which can make code cleaner too.

Let's compare generating two million-item lists and doing multitiplication. First, in native Python:

```python
import random
# Generating two vectors of a million items each
vector_a = [random.random() for _ in range(1_000_000)]
vector_b = [random.random() for _ in range(1_000_000)]

# Calculate dot product using a loop
result = 0
for i in range(len(vector_a)):
    result += vector_a[i] * vector_b[i]
```

Here's the equivalent in `NumPy`:

```python
import numpy as np

# Generating two vectors of a million items each
vector_a = np.random.rand(1_000_000)
vector_b = np.random.rand(1_000_000)

# Perform dot product
result = np.dot(vector_a, vector_b)
```

On my local machine, the second block of code took 0.025 seconds, versus 0.443 for the native Python. That's almost a 17x speed-up! And the NumPy syntax is much cleaner than a foreloop with array indexing. 

## Using `numexpr`

An issue you might face with `NumPy` is that it processes operations one by one, and stores intermediate results in temporary arrays. `numexpr` lets you compile a multi-step vector expression into something more efficient. It even supports parallelism. 

Let's imagine we want to calculate the following: `(a * b) + sqrt(a + b)`. Here's how we'd do it in NumPy:

```python
import numpy as np
import time

vector_a = np.random.rand(1_000_000)
vector_b = np.random.rand(1_000_000)

result_np = (vector_a * vector_b) + np.sqrt(vector_a + vector_b)
```

This took a little longer on my machine: 0.028 seconds. To use `numexpr`, we have to enter the calculation as a string:

```python
import numpy as np
import numexpr as ne

# Generating two vectors of a million items each
vector_a = np.random.rand(1_000_000)
vector_b = np.random.rand(1_000_000)

result_ne = ne.evaluate("(vector_a * vector_b) + sqrt(vector_a + vector_b)")
```

This was a blazing fast 0.006 seconds, a further 4.7x speedup... 