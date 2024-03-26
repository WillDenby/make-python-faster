# 💯 Easy Wins

## Loop Optimization

Loops, especially nested loops, can significantly affect performance. Avoiding or minimizing the use of nested loops can lead to substantial improvements. Use list comprehensions and generator expressions for more compact and faster code.

**Example: Using List Comprehension**

Instead of:

```python
result = []
for i in range(10):
    result.append(i * i)
```

Use:

```python
result = [i * i for i in range(10)]
```

## Data Structures

Choosing the right data structure can drastically improve performance. Python's built-in data structures like lists, sets, and dictionaries are highly optimized.

**Dictionaries and Sets:** Use dictionaries for quick lookups by key and sets for fast membership testing.
**Tuples:** Use tuples instead of lists for immutable sequences to save memory.

**Example: Using Set for Membership Testing**

Instead of:

```python
my_list = [1, 2, 3, 4, 5]
if 3 in my_list:  # O(n) time complexity
    print("Found!")
```

Use:

```python
my_set = {1, 2, 3, 4, 5}
if 3 in my_set:  # O(1) time complexity
    print("Found!")
```

## Algorithmic Improvements

Improving the algorithm itself is often the most effective way to optimize. This could mean choosing a more efficient sorting algorithm, using dynamic programming to avoid recalculating results, or employing algorithms with better time complexity.

**Example: Memoization in Fibonacci Sequence Calculation**

Instead of a simple recursive solution, use memoization:

```python
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
```

## Built-in Functions and Libraries (Or Not)

Python's standard library and third-party libraries like NumPy and Pandas are written in C, making them much faster than custom, pure Python code for certain operations, especially numerical computations and data processing.

**Example: Using NumPy for Array Operations**

Instead of:

```python
result = []
for i in range(10000):
    result.append(i * 2)
```

Use NumPy:

```python
import numpy as np
arr = np.arange(10000) * 2
```

## Profiling and Identifying Bottlenecks

Before optimizing, it's crucial to identify where the bottlenecks are. Python provides profiling tools like cProfile to analyze the performance of your code.

```python
import cProfile
def my_function():
    result = [i * i for i in range(10000)]
    return result

cProfile.run('my_function()')
```

## Avoiding Global Variables

Access to global variables is slower than local variable access. If you're using global variables within a loop or a frequently called function, consider passing them as arguments or using them as local variables.

## String Concatenation

Strings in Python are immutable, so every time you concatenate strings, a new string is created. For efficient string concatenation, especially in loops, use .join() or string formatting.

**Example: Using .join() for Efficient String Concatenation**

Instead of:

```python
result = ""
for i in range(100):
    result += str(i)
```

Use:

```python
result = "".join(str(i) for i in range(100))
```