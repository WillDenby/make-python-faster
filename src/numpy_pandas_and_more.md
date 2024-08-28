# ⚙️ NumPy and Numpy

NumPy and Pandas are two common libraries for data manipulation and analysis. Compared to Python’s built-in data structures, they can offer more efficient and intuitive storage and data operations, especially when dealing with large datasets or complex numerical computations. 

## The Problem with Lists

Python's native list structure has a problem with vector operations and matrix manipulations. Lists don't actually hold the data - instead, they hold pointers to the data location. The advantage of this is that the contents of a list can be heterogenous. However, this introduces a fetch/look-up overhead, which adds up if you are doing lots of operations.

(What does this look like in hardware terms? In brief, there's a cost in moving data from memory to the CPU. If you want to get into the weeds, you can use the Linux `perf` tool to look for `cache-misses` and `page-faults` when manipulating lists.)

## The Array Module?

Python offers an `array` module, which partially overcomes lists’ memory fragmentation issue by storing items sequentially. Iterating through an `array` doesn't require multiple look-ups, as data can be cached (making it closer in terms of spatial and temporal locality to the CPU). 

But then we run into a different issue: Python, as a high-level interpreted language, isn't optimised for vector operations, and isn't good at communicating with the low-level implementation of `array`.

## NumPy to the Rescue

NumPy is a library for numerical computing in Python. It introduces an array object (`ndarray`), which is a multidimensional container of items of the same type and size. NumPy has the following benefits over built-in lists:

**Efficiency**: NumPy arrays are stored at one continuous place in memory, maximising locality. This is particularly beneficial for operations involving large data sets.

**Convenience**: NumPy offers comprehensive mathematical functions that can be applied to arrays without writing loops. This makes code cleaner and faster.

**Functionality**: NumPy supports an extensive range of operations including shape manipulation, sorting, selecting discrete Fourier transforms, linear algebra, random simulation, and much more.

It has a special but not totally alien syntax:

```python
import numpy as np

# With NumPy
numpy_array = np.array([1, 2, 3, 4])
print(np.sum(numpy_array))  # Output: 10

# With built-in Python list
python_list = [1, 2, 3, 4]
print(sum(python_list))  # Output: 10
```

## Pandas

Pandas is a library built on top of NumPy, which introduces two new data structures to Python: `Series` and `DataFrame`. These enable the following:

**More intuitive data representation**: Pandas provides a fast, flexible, and expressive data structure, designed to make working with "relational" or "labeled" data easier.

**Functionality**: Pandas offers expressive and flexible data operations for the loading, cleaning, transforming, merging, reshaping, aggregation, and selection of data.

For example, here’s how to load a CSV file into a `DataFrame`

```python
import pandas as pd

# Using Pandas
data = pd.read_csv('file.csv')
print(data.head())  # Displays the first 5 rows of the file

# The equivalent using built-in Python would require manually parsing the CSV file into lists or dictionaries,
# handling the header separately, and not having the convenient data manipulation functions that Pandas offers.
```

**Handling missing data**: Pandas is designed to handle missing data using `numpy.nan`, making it incredibly versatile for data analysis tasks, where absent data is common. 

While Python's built-in data structures are incredibly powerful and useful for a wide range of programming tasks, Numpy and Pandas offer specialised features that are better suited for numerical computing and data analysis. 

Let's explore them further!


