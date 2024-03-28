# 🐻‍❄️ Dask and Polars

These are two libraries designed to address the shortcomings of `Pandas`.

## Dask

`Dask` is a flexible parallel computing library for analytics, enabling you to scale up to clusters or down to your laptop. It's particularly well-suited for working with large datasets that don't fit into memory, as it breaks down complex computations into manageable tasks, which are executed in parallel. Dask provides dynamic task scheduling optimized for computation. It's designed to integrate seamlessly with existing Python libraries like `NumPy`, `Pandas`, and `Scikit-Learn`, allowing you to scale those libraries' functionality across multiple cores or machines.

Here's a simple example that demonstrates how to use `Dask` `Array` to perform a computation that is automatically parallelized:

```python
import dask.array as da

# Create a large random dask array
x = da.random.random((10000, 10000), chunks=(1000, 1000))

# Compute the mean of the array
mean_result = x.mean().compute()

print(mean_result)
```

## Polars

`Polars` is a fast `DataFrame` library implemented in Rust, designed for high performance and efficiency. It's capable of handling large datasets with ease and speed, focusing on lazy computations for optimal performance. `Polars` leverages Rust's memory safety and speed, bringing efficient data processing capabilities to Python. It's especially good for tasks involving large datasets that require high-speed manipulation, filtering, and aggregation.

`Polars` operates with both eager and lazy evaluation. The lazy evaluation allows for more optimized computations by building a computation graph and optimizing it before execution, which can lead to significant performance improvements.

It's largely recreated the `Pandas` API, for ease-of-transition:

```python
import polars as pl

# Read a CSV file into a Polars DataFrame
df = pl.read_csv("your_data.csv")

# Select columns and compute the mean of a column
mean_value = df.select([
    pl.col("your_column_name").mean()
])

print(mean_value)
```