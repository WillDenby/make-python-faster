# 🎯 Sets

Sets are unordered collections of unique elements. They are mutable and provide efficient ways to perform common set operations like union, intersection, and difference.

**Performance Characteristics:**

- Like dictionaries, set operations such as adding, removing, and checking for membership are O(1) on average.

**Memory Implications**

Sets are conceptually similar to dictionaries with only keys and no values. They are also backed by a hash table, providing fast operations for checking membership, adding, and removing elements. They are memory-efficient for operations involving large numbers of elements but might use more memory than lists or tuples for the same number of elements, due to the hash table mechanism.

**Example:**

```python
my_set = {1, 2, 3}
my_set.add(4)    # Add an element
my_set.remove(2) # Remove an element
print(my_set)    # Output: {1, 3, 4}
```