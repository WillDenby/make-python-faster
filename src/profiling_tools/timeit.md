# ⏱️ timeit

`timeit` provides a more accurate timing mechanism than `time.time()` for small code snippets, by taking into account setup code and by running the code multiple times to calculate an average time.

## Usage Example

You can use `timeit` like this:

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

The function runs the code snippet specified by the `stmt` parameter a `number` of times, and returns the average time taken.



[Get PDF](https://makepythonfaster.gumroad.com/l/get)
