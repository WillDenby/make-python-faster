# Arrays: Tuples (Static) and Lists (Dynamic)

An array is a class of data structure which stores elements in order and contiguously in memory, and provides constant-time access them. This means that, if we know an elements position in the index, we can find it super-quick in O(1). Python has two flavours of array: `tuples` and `lists`. We can recognise them by `[]` vs `()` respectively. 

When an array is created, the computer has to allocate a block of system memory to store it (hence, in some programming languages, arrays are fixed-size). This is "metaphorically" the `tuple`: a static array with immutable elements. But because `tuples` are static and immutable, Python can cache them, meaning it can skip out on *actually* speaking to the kernel for system memory. Python gives us the `list` as a helpful abstraction to make modifying arrays easier ... at a cost. We call them dynamic arrays. 

When to use a `tuple` vs a `list` is often dictated by the nature of your data: does it *need* to change, or is it *fixed*? But if performance is a concern, it's worth asking the question: can I use a `tuple` instead of a `list`? This is because the former require less memory and CPU overhead. Try the [timeit](../profiling/the_timeit_module.md) profiling method on the initialisation examples below!

```python
# Initializing a list
example_list = [1, 2, 3, 4, 5]
print("Example list:", example_list)

# Initializing a tuple
example_tuple = (1, 2, 3, 4, 5)
print("Example tuple:", example_tuple)
```

## Extending Arrays

Consider this operation:

```python
example_list = [1, 2, 3, 4, 5]
example_list.append(6)
```

Under the hood, Python has to create a new array to hold the original elements of `example_list` PLUS the new element. Doing this often would be very expensive: allocating memory is **expensive**.

In reality, Python sort-of knows this. Rather than creating an array of `len(example_list)+1`, CPython will assume that some more `.append` method calls are coming, so it will *overallocate* approximately 115% percent (following a growth pattern of 0, 4, 8, 16, 25, 35, 46, 58, 72, 88, ...), and then fill it up until it needs to resize again. Still, if you are constantly appending to a list, expect an ongoing memory cost. On the flipside, it's an O(1) operation. 

The `tuple` doesn't let you have this problem, by design! There's no `.append(x)` ... -ish. You can hack your way around it by *adding* two tuples together, to create a new tuple. Which is not a in-place operation, and also a slower O(n). 🤦🤦🤦

## Finding Things (Sorting and Searching)

This book has an interest in straightforward performant programming. We're not going to go into the depths of comparing sorting algorithms and time complexities. Instead, my recommendation is to make use of Python's built-in methods for lists. The Python team has spent time optimising these. 

For instance, `list.sort()` uses "Timsort", invented by Tim Peters (who also wrote the famous [Zen of Python](https://en.wikipedia.org/wiki/Zen_of_Python)). 

```python
import random

random_numbers = [random.randint(1, 1000) for _ in range(100)]

random_numbers.sort()

print("Sorted list using sorted():", sorted_numbers)
print("Sorted list using sort():", random_numbers)
```

Similarly, take the case of searching for an item, with the aim of returning the index. In Python, you can use the `.index()` method, which is highly optimised and has a worst case time complexity of O(n). It's only worth implementing something like binary search, which is O(log n), if the list is *already* sorted, as otherwise you'll be incurring the sorting cost too. 

```python
import random

random_numbers = [random.randint(1, 100) for _ in range(100)]

try:
    index = random_numbers.index(42)
    print("There is a 42 at index", index)
except ValueError:
    print("42 is not in the list.")
```