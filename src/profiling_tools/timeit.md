# ⏱️ timeit

`timeit` is a Python module designed to allow Python developers to time small bits of Python code with a minimal influence from the timing mechanism itself. It provides a more accurate timing mechanism than time.time() for small code snippets by taking into account setup code and running the code multiple times to calculate an average time.

**Usage Example:**

```python
import timeit

code_to_test = """
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
"""

elapsed_time = timeit.timeit(stmt=code_to_test, number=100000)
print(f"Elapsed time: {elapsed_time} seconds")
```

The function runs the code snippet specified by the stmt parameter number times and returns the total time taken.