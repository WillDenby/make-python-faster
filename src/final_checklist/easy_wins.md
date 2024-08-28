# 💯 Easy Wins

## Loop Optimisation

Loops, especially nested loops, can significantly affect performance. Avoiding or minimising the use of nested loops can lead to substantial improvements. Use list comprehensions and generator expressions for more compact and faster code. Instead of:

```python
result = []
for i in range(10):
    result.append(i * i)
```

You can use:

```python
result = [i * i for i in range(10)]
```

## Data Structures

Choosing the right data structure can be an easy way to improve performance. Python's built-in data structures are robust in practice:

- Use dictionaries for quick lookups by key and sets for fast membership testing.
- Use tuples instead of lists for immutable sequences to save memory.

So instead of:

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

Improving your choice of algorithm is another effective way to optimise code. This could mean choosing a more efficient sorting algorithm, using dynamic programming to avoid recalculating results, or employing algorithms with better time complexity. This can also include manually caching strategies, like memoization. For example, instead of an expensive naive recursive solution, you can use memoization to calculate Fibonacci numbers:

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

Third-party libraries like NumPy and Pandas, written in C, are faster than pure Python code for certain operations, like numerical computations or data processing. You can often reimplement Python code in more concise NumPy, such as:

```python
result = []
for i in range(10000):
    result.append(i * 2)
```

In NumPy, this would be a line less:

```python
import numpy as np
arr = np.arange(10000) * 2
```

## Profiling and Identifying Bottlenecks

Before optimising, it's crucial to identify where the bottlenecks are. Python provides profiling tools like `cProfile` to analyse the performance of your code.

```python
import cProfile
def my_function():
    result = [i * i for i in range(10000)]
    return result

cProfile.run('my_function()')
```

## Avoiding Global Variables

Access to global variables is slower than local variable access. If you're using global variables within a loop or a regularly called function, consider passing them as arguments or using them as local variables.

## String Concatenation

Strings in Python are immutable, so every time you concatenate strings, a new string is created. For efficient string concatenation, especially in loops, use `.join()` or string formatting. Instead of:

```python
result = ""
for i in range(100):
    result += str(i)
```

Try:

```python
result = "".join(str(i) for i in range(100))
```