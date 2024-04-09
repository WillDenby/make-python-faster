# 🏗️ Built-in Data Structures

Python provides several built-in data structures that are highly versatile, enabling you to store and manipulate data efficiently. These data structures include lists, tuples, dictionaries, and sets, each with their own unique features and performance characteristics. They are, in general, lower-level and hence faster than custom data structures. Choosing the right one depends on the specific requirements of your algorithm, including the types of operations you need to perform and their frequency. 

A rule of thumb to remember is that "generic" structures containing multiple data types will tend to incur greater overhead when being manipulated than those of a single type. Before we dive into them in more detail, here are some other useful tips:

## General Tips

- **Lists** and **Tuples**: Good for ordered collections of items. Lists are mutable, whereas tuples are immutable.
- **Dictionaries**: Ideal for associative arrays where key-value pair mappings are needed.
- **Sets**: Useful for storing unique elements and performing set operations.

## Memory Efficiency Tips

- Use tuples instead of lists for fixed-size collections because tuples have a smaller memory overhead.
- Consider using `__slots__` for classes if you're creating many instances of a class. This can significantly reduce the memory overhead by preventing the creation of a `__dict__` for each instance, at the cost of flexibility.
- Be mindful of container size and cleanup. Large collections can consume a lot of memory. Removing references to unneeded objects or using data structures with smaller overheads can help manage memory usage.
- Consider using specialized libraries or data structures for large datasets, such as arrays from the array module for homogeneous data or third-party libraries like NumPy, which can be more memory-efficient for certain tasks.
