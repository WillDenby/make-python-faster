# 🔢 Using numexpr

Numexpr is a Python library that provides a way to evaluate numerical expressions on arrays at a faster rate than NumPy can, in some cases. It achieves this speedup by using a faster evaluator that utilizes the capabilities of modern CPUs more efficiently, including their vector units and multiple cores. Numexpr compiles the array expressions you give it into optimized, intermediate code that it then executes more efficiently than NumPy's default methods. This can lead to significant performance improvements, especially on operations that involve large arrays.

## How Numexpr Works

Numexpr takes a string expression describing a numerical operation and evaluates it much faster than if you were to directly use NumPy for two main reasons:

- **Efficient Use of Memory**: It avoids allocating full temporary arrays that result from intermediate calculations in complex expressions. This means it can handle larger arrays and use less memory, which is particularly useful when working with large datasets that don't fit into your computer's RAM.
- **Utilization of CPU Features**: Numexpr is designed to make efficient use of CPU features, such as multiple cores and vector operations (SIMD - Single Instruction, Multiple Data). This allows it to perform calculations faster than NumPy, which does not parallelize operations at the level Numexpr does.

**Why Use Numexpr:**

- **Performance**: For complex expressions, especially those involving large arrays, Numexpr can significantly outperform NumPy in terms of speed by utilizing CPU features more efficiently and reducing memory usage.
- **Handling Large Data**: By minimizing memory consumption through avoiding temporary arrays, Numexpr can work with larger datasets more effectively than NumPy alone.

**Example Usage**

Let's compare a NumPy operation with its Numexpr counterpart to illustrate the usage and performance difference:

NumPy:

```python
import numpy as np

a = np.random.rand(1000000)
b = np.random.rand(1000000)

# Using NumPy
c = 2*a + 3*b + 1
```

Numexpr:

```python
import numexpr as ne
import numpy as np

a = np.random.rand(1000000)
b = np.random.rand(1000000)

# Using Numexpr
c = ne.evaluate('2*a + 3*b + 1')
```

In the example above, both snippets achieve the same result, but numexpr can execute the operation faster on large arrays due to its efficient memory use and parallel computation capabilities.

