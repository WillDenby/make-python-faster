# 🏗️ Built-in Data Structures

So you’ve profiled your code and found areas to improve. Now what?

First, it’s worth considering how you are handling the data that’s moving through your system. Python provides several built-in data structures, including lists, tuples, dictionaries, and sets, each with their own unique features and performance characteristics. Choosing the right one depends on the specific requirements of your system, including the types of operations you need to perform and their frequency. 

## General Tips

- Lists and Tuples are good for ordered collections of items. Lists are mutable, whereas tuples are immutable. Use tuples instead of lists for fixed-size collections, because tuples have a smaller memory overhead.
- Dictionaries are ideal for associative arrays where key-value pair mappings are needed.
- Sets are useful for storing unique elements and performing set operations.
- Generic structures (i.e. those containing multiple data types, such as floats and strings) tend to incur greater overhead when being manipulated than those of a single type.
