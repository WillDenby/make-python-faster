# 📝 Lists

Lists are ordered collections of items (elements) that can be of different types. They are mutable, meaning that their elements can be changed, added, or removed, like so:

```python
my_list = [1, 2, 3]
my_list.append(4)  # Add an element
my_list[1] = 20    # Modify an element
del my_list[0]     # Remove an element
print(my_list)     # Output: [20, 3, 4]
```

## Performance and Memory Characteristics

Accessing an element by index is O(1). Adding/removing elements at the end is also O(1), but inserting/removing elements elsewhere can be O(n) because it may require shifting elements. And searching for an element is O(n) because it requires a linear search.

Lists are dynamic arrays and thus have some overhead for memory allocation to support their mutability and variable size. Each item in a list holds a reference to an object (which could be anything), and there's additional memory overhead for maintaining the size of the list and the pointers to each item.

So the memory usage of a list grows with the number of elements. However, because Python preallocates memory in chunks (to avoid frequent resizing), a list might use more memory than the actual data it stores.


[Get PDF/ePub](https://makepythonfaster.gumroad.com/l/get)
