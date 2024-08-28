# 🗝️ Dictionaries

Dictionaries are unordered collections of key-value pairs. They allow for fast data lookup by key and are mutable. Here’s an example of some dictionary operations:

```python
my_dict = {'apple': 5, 'banana': 3}
my_dict['cherry'] = 7  # Add a new key-value pair
my_dict['apple'] = 10  # Update an existing key-value pair
del my_dict['banana']  # Remove a key-value pair
print(my_dict)         # Output: {'apple': 10, 'cherry': 7}
```

## Performance and Memory Characteristics

Access, insertion, and deletion operations are O(1) on average, because dictionaries are implemented using hash tables.
However, in the worst-case scenario (e.g. many key collisions), these operations can degrade to O(n).

Hash tables involve using a sparse array to provide fast access paths to values based on unique keys. Each entry in the hash table holds the key, the value, and a hash of the key for fast comparison.

This overhead allows for fast access but means that, byte for byte, a dictionary will use more memory than a list or tuple storing the same data. The memory usage becomes more efficient as the dictionary grows larger, but sparse usage (many empty entries) can lead to wasted space.


[Get PDF/ePub](https://makepythonfaster.gumroad.com/l/get)
