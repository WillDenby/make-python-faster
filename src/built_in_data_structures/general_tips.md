# 💡 General Tips

- Lists and Tuples: Good for ordered collections of items. Lists are mutable, whereas tuples are immutable.
- Dictionaries: Ideal for associative arrays where key-value pair mappings are needed.
- Sets: Useful for storing unique elements and performing set operations.

## General Memory Efficiency Tips

- Use tuples instead of lists for fixed-size collections because tuples have a smaller memory overhead.
- Consider using __slots__ for classes if you're creating many instances of a class. This can significantly reduce the memory overhead by preventing the creation of a __dict__ for each instance, at the cost of flexibility.
- Be mindful of container size and cleanup. Large collections can consume a lot of memory. Removing references to unneeded objects or using data structures with smaller overheads can help manage memory usage.
- Consider using specialized libraries or data structures for large datasets, such as arrays from the array module for homogeneous data or third-party libraries like NumPy, which can be more memory-efficient for certain tasks.