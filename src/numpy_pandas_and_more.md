# ⚙️ NumPy, Pandas, and More

`Numpy` and `Pandas` are two widely used libraries in Python for data manipulation and analysis. Compared to built-in data structures, they offer more efficient storage and data operations, especially when dealing with large datasets or complex numerical computations. Later in this section, we'll also explore related libraries like Dask and Polars, which further extend these capabilities. 

## Numpy

Python's native list structure has a problem with vector operations and matrix manipulations. Lists don't actually hold the data - instead, they hold pointers to the data location. The advantage of this is that the contents of a list can be heterogenous. However, it introduces a fetch/look-up overhead, and if you are doing lots of operations, this adds up.

What does this look like in hardware terms? In brief, there's a cost in moving data from memory to the CPU. Modern computers can have tiered architectures, with DRAM, SRAM, external caches, and on-chip caches. CPUs can also do things like branch prediction, speculation, overlapped instruction fetching, pipelining, and superscalar execution. If you want to get into the weeds, you can use the Linux perf tool to do some profiling, looking for `cache-misses` (memory bound) and `page-faults` (disk/network bound). But we might as well be sensible with how we do things.

### The Array Module?

Python offers an `array` module, that overcomes the memory fragementation issue by storing items sequentially. Iterating through an `array` therefore doesn't require multiple look-ups, as data can be cached (i.e. closer in terms of spatial and temporal locality to the CPU). But then we run into a different issue: Python, as a high-level interpreted language, isn't optimised for vector operations, and isn't good at dealing with the low-level implementation of `array`.

### Enter NumPy

`Numpy` is a library for numerical computing in Python. It introduces an array object (ndarray), which is a multidimensional container of items of the same type and size. Here's why you might use Numpy arrays over Python lists:

**Efficiency**: `Numpy` arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently. This is particularly beneficial for operations involving large data sets.

**Convenience**: `Numpy` offers comprehensive mathematical functions that can be applied on arrays without writing loops. This makes code cleaner and faster.

**Functionality**: `Numpy` supports an extensive range of operations including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation, and much more.

**Example: Summing Elements**

```python
import numpy as np

# With Numpy
numpy_array = np.array([1, 2, 3, 4])
print(np.sum(numpy_array))  # Output: 10

# With built-in Python list
python_list = [1, 2, 3, 4]
print(sum(python_list))  # Output: 10
```

The `Numpy` version is much faster and more efficient, especially with larger arrays.

## Pandas

`Pandas` is built on top of `Numpy` and is crucial for data manipulation and analysis. It introduces two new data structures to Python: `Series` and `DataFrame`, which are built on `Numpy` arrays.

**Data Representation**: `Pandas` provides a fast, flexible, and expressive data structure designed to make working with "relational" or "labeled" data both easy and intuitive.

**Functionality**: It offers powerful, expressive, and flexible data operations for cleaning, transforming, merging, reshaping, aggregation, and selection of data.

**Handling Missing Data**: `Pandas` is designed to handle missing data using `numpy.nan`, making it incredibly versatile for data analysis tasks where missing data is a common issue.

**Example: Handling CSV Files**

```python
import pandas as pd

# Using Pandas
data = pd.read_csv('file.csv')
print(data.head())  # Displays the first 5 rows of the file

# The equivalent using built-in Python would require manually parsing the CSV file into lists or dictionaries,
# handling the header separately, and not having the convenient data manipulation functions that Pandas offers.
```

`Pandas` abstracts away much of the complexity of handling tabular data, making it invaluable for data analysis.

While Python's built-in data structures are incredibly powerful and useful for a wide range of programming tasks, `Numpy` and `Pandas` offer specialized features that are better suited for numerical computing and data analysis. 

Let's explore them further!
