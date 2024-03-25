# 🐼 Optimising Data Manipulation

Optimizing data manipulation and analysis with Pandas is crucial for handling large datasets efficiently and effectively. Pandas, being one of the most popular libraries in Python for data analysis, provides numerous ways to optimize performance. Below, I'll highlight some key strategies and provide code examples where relevant.

## Choosing the Right Data Types

Pandas automatically assigns data types, but they might not always be the most memory-efficient. By converting columns to more appropriate data types, you can significantly reduce memory usage.

**Example: Converting data types**

```python
import pandas as pd

# Assuming df is your DataFrame
# Convert to 'category' if the number of unique values is small
df['column_name'] = df['column_name'].astype('category')

# Use smaller numeric types
df['int_column'] = df['int_column'].astype('int32')
```

## Using Chunking for Large Datasets

When dealing with very large datasets that do not fit into memory, you can read and process the data in chunks.

**Example: Reading in chunks**

```python
chunk_size = 10000  # size of the chunk
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    # process each chunk
    pass
```

## Avoiding Loops with Vectorization

Loops in Python are slow. Pandas operations are optimized to use vectorized operations that are much faster than iterating through rows.

**Example: Vectorized operations**

```python
# Bad: Looping through DataFrame rows
for index, row in df.iterrows():
    df.at[index, 'new_column'] = row['column'] * 2

# Good: Vectorized operation
df['new_column'] = df['column'] * 2
```

## Using Efficient Functions

Pandas provides functions that are optimized for performance. For example, apply() is versatile but can be slower than using vectorized operations or specific functions like agg(), transform(), or groupby().

**Example: Efficient aggregation**

```python
# Using `apply()` - Less efficient
df.groupby('group_column').apply(lambda x: x['column'].sum())

# Using `agg()` - More efficient
df.groupby('group_column')['column'].agg('sum')
```

## Filtering Data Early

Filter out unnecessary data as early as possible in your pipeline to reduce the size of your DataFrame and speed up subsequent operations.

**Example: Early filtering**

```python
# Filter before performing other operations
df_filtered = df[df['column'] > 100]
# Now work with df_filtered
```

## Using eval() and query() for Compound Expressions

For complex operations, eval() and query() can be faster because they operate at a lower level and can avoid intermediate data structures.

**Example: Using query()**

```python
result = df.query('column1 > 200 & column2 < 300')
```

## Caching Intermediate Results

If certain results are used multiple times, it might be beneficial to cache them instead of recalculating.

**Example: Caching results**

```python
# Assuming calculating `expensive_operation()` is resource-intensive
df['expensive_column'] = expensive_operation(df['column'])
df['new_column'] = df['expensive_column'] + 100
```

## Utilize MultiIndex for Complex Data Structures

For data with hierarchical structures, using MultiIndex can significantly improve both performance and memory usage. It's particularly useful for grouping and unstacking operations.

**Example: Creating and using MultiIndex**

```python
# Setting a MultiIndex from columns
df.set_index(['level_0', 'level_1'], inplace=True)

# Accessing a slice
df.loc[('index_level_0_value', 'index_level_1_value')]
```

## Optimize I/O Operations

Reading and writing data efficiently can also be optimized. For example, using the Parquet format can significantly reduce both disk space usage and read/write times compared to CSV or Excel.

**Example: Reading and writing Parquet files**

```python
# Writing to Parquet
df.to_parquet('data.parquet')

# Reading from Parquet
df = pd.read_parquet('data.parquet')
```

## Minimizing Memory Use with Sparse Data Structures

If your dataset contains a lot of missing values or zeros, converting applicable columns to sparse data types can reduce memory usage.

**Example: Using sparse data type**

```python
df['sparse_column'] = pd.arrays.SparseArray(df['sparse_column'])
```

## Enhancing Performance with Swifter

For operations that are difficult to vectorize or when you're stuck with apply() for complex functions, consider using the swifter library. It automatically decides whether to use the original .apply() method, to vectorize the operation if possible, or to use parallel processing to speed up the computation.

**Example: Using swifter**

```python
import swifter

# Apply a function more efficiently
df['result'] = df['column'].swifter.apply(lambda x: complex_function(x))
```

Optimizing data manipulation and analysis in Pandas involves a combination of choosing the right data types, leveraging Pandas' powerful vectorized operations, and avoiding common pitfalls like unnecessary looping. By following these strategies, you can make your data processing pipelines more efficient and scalable.

You can also use techniques like parallel processing explicitly - we'll cover these later, as they apply more broadly.






