# 🔢 Using numexpr

Numexpr is a Python library that enables you to evaluate numerical expressions on arrays faster than NumPy can. How so?

**A more efficient use of memory**: Numexpr avoids allocating full temporary arrays that result from intermediate calculations in complex expressions. This means it can handle larger arrays and use less memory, which is particularly useful when working with large datasets that don't fit into your computer's RAM.

**More efficient utilisation of modern CPUs**: Numexpr leverages modern CPU features, such as multiple cores and vector operations (e.g. SIMD - Single Instruction, Multiple Data). NumPy does not parallelise operations to the same level.

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

In the example above, both snippets achieve the same result, but Numexpr can execute the operation faster on large arrays due to its efficient memory use and parallel computation capabilities.




[Get PDF/ePub](https://makepythonfaster.gumroad.com/l/get)
