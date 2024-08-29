# 🧹 Easy Losses

## Using Lists in the Wrong Place

**Anti-pattern**: Using lists for operations that require frequent lookups, insertions, and deletions:

```python
# Inefficient for frequent lookups
my_list = [1, 2, 3, 4, 5]
if 4 in my_list:
    print("Found!")
```

**Solution**: Using sets or dicts for frequent lookups and insertions:

```python
my_set = {1, 2, 3, 4, 5}
if 4 in my_set:  # Much faster lookup
    print("Found!")
```

## Avoiding List Comprehensions / Generator Expressions

**Anti-pattern**: Using loops to generate lists or to iterate over collections increases complexity:

```python
result = []
for i in range(100):
    if i % 2 == 0:
        result.append(i*i)
```

**Solution**: Use list comprehensions for more concise and faster code:

```python
result = [i*i for i in range(100) if i % 2 == 0]
```

When the result list is not needed all at once, use generator expressions to save memory:

```python
result = (i*i for i in range(100) if i % 2 == 0)
```

## Misusing the Global Interpreter Lock (GIL)

**Anti-pattern**: Relying solely on threads for concurrency in CPU-bound tasks can be inefficient, due to the GIL:

```python
from threading import Thread

# This might not speed up due to GIL in CPU-bound tasks
def compute_heavy():
    # Some heavy computation
    pass

threads = [Thread(target=compute_heavy) for _ in range(4)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
```

**Solution**: Use `multiprocessing` or libraries like `concurrent.futures.ProcessPoolExecutor` for CPU-bound tasks:

```python
from multiprocessing import Pool

def compute_heavy():
    # Some heavy computation
    pass

with Pool(4) as p:
    p.map(compute_heavy, [1, 2, 3, 4])
```

## Under-Utilising Built-in Functions / Libraries

**Anti-pattern**: Reimplementing functionality that is already provided (and optimised) by Python's built-in functions or standard libraries.

```python
# Custom implementation of a feature that exists in standard library
def manual_sort(my_list):
    return sorted(my_list)  # Inefficient and reinventing the wheel

# Correct approach
my_list = [3, 1, 4, 1, 5]
print(sorted(my_list))
```

**Solution**: Always check the Python standard library and built-in functions before implementing common algorithms and data structures.

## Deeply Nested Functions

**Anti-pattern**: Writing deeply nested functions or loops, which can make code hard to read, debug, and optimise.

```python
def deeply_nested(data):
    for i in data:
        for j in i:
            # ... more nested loops or conditions
            pass
```

**Solution**: Refactor deeply nested loops into separate functions or use more efficient data structures or algorithms to simplify the logic.

By being aware of these common anti-patterns and applying the suggested solutions, you can quickly improve the performance and maintainability of your Python code.



[Get PDF](https://makepythonfaster.gumroad.com/l/get)
