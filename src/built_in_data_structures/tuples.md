# 🎁 Tuples

Tuples are similar to lists but are immutable, meaning that once a tuple is created, it cannot be modified. This makes tuples a good choice for representing fixed collections of items, such as:

```python
my_tuple = (1, 2, 3)
print(my_tuple[1])  # Access an element, Output: 2
```

## Performance and Memory Characteristics

Accessing an element by index is O(1), and searching for an element is O(n). 

Since tuples are immutable, operations like adding or removing elements are not applicable. And because they cannot change in size, Python knows exactly how much memory to allocate at creation time.

This makes them more memory-efficient than lists with the same elements. Nevertheless, like lists, each element is a reference to another object, so the overall memory usage still depends on what is stored in the tuple.



[Get PDF](https://makepythonfaster.gumroad.com/l/get)
