# 🎁 Tuples

Tuples are similar to lists but are immutable, meaning that once a tuple is created, it cannot be modified. This makes tuples a good choice for representing fixed collections of items.

**Performance Characteristics:**

- Accessing an element by index is O(1).
- Since tuples are immutable, operations like adding or removing elements are not applicable.
- Searching for an element is O(n).

**Memory Implications**

Tuples are immutable and hence can be optimized by Python's runtime. Since they cannot change in size, Python knows exactly how much memory to allocate at creation time.

Therefore, generally, tuples are more memory-efficient than lists with the same elements because of their immutability and the absence of overhead associated with variable size. However, like lists, each element is a reference to another object, so the overall memory usage depends on what is stored in the tuple.

**Example:**

```python
my_tuple = (1, 2, 3)
print(my_tuple[1])  # Access an element, Output: 2
```