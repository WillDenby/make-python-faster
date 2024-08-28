# 🐻‍❄️ Dask and Polars

These are two libraries designed to address the shortcomings of Pandas - the fact that it struggles with very large datasets, and leaves some performance on the table.

## Dask

Dask is a flexible parallel computing library for analytics, enabling you to scale up to clusters or down to your laptop. It's well-suited for working with large datasets that don't fit into memory, as it breaks down complex computations into tasks which can be executed in parallel. 

Here's a simple example demonstrating how to use a Dask `Array` to parallelise a computation:

```python
import dask.array as da

# Create a large random dask array
x = da.random.random((10000, 10000), chunks=(1000, 1000))

# Compute the mean of the array
mean_result = x.mean().compute()

print(mean_result)
```

## Polars

Polars is a DataFrame library implemented in Rust, designed for high performance and efficiency. 

It's particularly notable for its “lazy” evaluation mode. This optimises performance, by only executing operations on data that it has to, enabling higher-speed manipulation, filtering, and aggregation. It works by building a computation graph prior to execution.

Polars has largely recreated the Pandas API, to encourage Pandas users/code to transition:

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