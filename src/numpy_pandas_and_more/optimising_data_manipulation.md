# 🐼 Optimising Data Manipulation

Optimising your Pandas data manipulation logic makes it easier to process large datasets. I'll highlight some key strategies and provide code examples where relevant.

## Choose the Right Data Types

Pandas automatically assigns data types, but they might not always be the most memory-efficient. By converting columns to more appropriate data types, you can reduce memory usage. For example:

```python
import pandas as pd

# Assuming df is your DataFrame
# Convert to 'category' if the number of unique values is small
df['column_name'] = df['column_name'].astype('category')

# Use smaller numeric types
df['int_column'] = df['int_column'].astype('int32')
```

## Use Chunking for Large Datasets

When dealing with datasets that do not fit into memory, you can read and process the data in chunks, like this:

```python
chunk_size = 10000  # size of the chunk
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    # process each chunk
    pass
```

Alternatively, use Dask!

## Avoid Loops with Vectorisation

Loops in Python are slow. Pandas operations are optimised to use vectorised operations that are much faster than iterating through rows:

```python
# Bad: Looping through DataFrame rows
for index, row in df.iterrows():
    df.at[index, 'new_column'] = row['column'] * 2

# Good: Vectorized operation
df['new_column'] = df['column'] * 2
```

## Use Efficient Functions

For example, Pandas’ `apply()` function is versatile but can be slower than using vectorised operations or specific functions like `agg()`, `transform()`, or `groupby()`. Try comparing the following with a large `df`:

```python
# Using `apply()` - Less efficient
df.groupby('group_column').apply(lambda x: x['column'].sum())

# Using `agg()` - More efficient
df.groupby('group_column')['column'].agg('sum')
```

## Filter Data Early

Filter out unnecessary data as early as possible in your pipeline to reduce the size of your dataframe and speed up subsequent operations:

```python
# Filter before performing other operations
df_filtered = df[df['column'] > 100]
# Now work with df_filtered
```

## Use eval() and query() for Compound Expressions

For complex operations, `eval()` and `query()` can be faster because they operate at a lower level and can avoid intermediate data structures:

```python
result = df.query('column1 > 200 & column2 < 300')
```

## Cache Intermediate Results

If certain results are being used multiple times, it might be beneficial to cache them instead of recalculating. For instance:

```python
# Assuming calculating `expensive_operation()` is resource-intensive
df['expensive_column'] = expensive_operation(df['column'])
df['new_column'] = df['expensive_column'] + 100
```

## Utilise MultiIndex for Complex Data Structures

For grouping and unstacking operations on data with hierarchical structure, using MultiIndex can improve both performance and memory usage:

```python
# Setting a MultiIndex from columns
df.set_index(['level_0', 'level_1'], inplace=True)

# Accessing a slice
df.loc[('index_level_0_value', 'index_level_1_value')]
```

## Optimise I/O Operations

Reading and writing data can be a resource drain.Using the Parquet format can reduce both disk space usage and read/write times compared to CSV:

```python
# Writing to Parquet
df.to_parquet('data.parquet')

# Reading from Parquet
df = pd.read_parquet('data.parquet')
```

## Minimise Memory Use with Sparse Data Structures

If your dataset contains a lot of missing values or zeros, converting applicable columns to sparse data types can reduce memory usage:

```python
df['sparse_column'] = pd.arrays.SparseArray(df['sparse_column'])
```

## Enhance Performance with Swifter

For operations that are difficult to vectorise or when you're stuck with `apply()` for complex functions, consider using the `swifter` library. It automatically decides whether to use the original `.apply()` method, to vectorise the operation if possible, or to use parallel processing to speed up the computation:

```python
import swifter

# Apply a function more efficiently
df['result'] = df['column'].swifter.apply(lambda x: complex_function(x))
```

Optimising data manipulation and analysis in Pandas involves a combination of choosing the right data types, leveraging Pandas' powerful vectorised operations, and avoiding common pitfalls like unnecessary looping. By following these strategies, you can accelerate data processing pipelines where needed.










[Get PDF](https://makepythonfaster.gumroad.com/l/get)
