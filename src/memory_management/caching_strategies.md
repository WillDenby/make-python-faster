# 💾 Caching Strategies

Caching in Python is a technique used to store data in a temporary storage area (cache) so that future requests for that data can be served faster. This is particularly useful in situations where data retrieval or computation is resource-intensive. Python provides various strategies and tools for caching, which can be applied depending on the specific requirements of your application.

## LRU (Least Recently Used) Cache

The LRU caching strategy removes the least recently used items first. This is useful in applications where you want to cache a limited number of items and the likelihood of accessing recently used items is high.

Python's functools module provides an `@lru_cache` decorator to implement LRU caching easily. It can be applied to any function whose output you want to cache.

**Example:**

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def expensive_function(param):
    # Simulate an expensive operation
    return some_expensive_computation(param)
```

## Memoization

Memoization is a specific form of caching that involves storing the results of expensive function calls and returning the cached result when the same inputs occur again. Memoization is a form of LRU caching but is specifically applied to function calls.

Python's functools module `@lru_cache` can also be used for memoization.

**Example:**

```python
from functools import lru_cache

@lru_cache(maxsize=None)  # No limit on cache size
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

## TTL (Time To Live) Cache

TTL caching invalidates cache entries after a set period. This strategy is suitable when the data changes over time or if you want to ensure that data doesn't become stale.

The `cachetools` library offers TTL caching capabilities.

**Example:**

```python
from cachetools import TTLCache
from cachetools.decorators import cached

ttl_cache = TTLCache(maxsize=100, ttl=300) # Cache up to 100 items, each for 300 seconds

@cached(ttl_cache)
def get_data(key):
    # Fetch data that changes over time
    return fetch_some_data(key)
```

## Disk-based Caching

When dealing with large amounts of data or needing to persist cache across program restarts, disk-based caching can be used. Libraries such as `joblib` provide mechanisms for storing cache data on disk.

**Example:**

```python
from joblib import Memory
memory = Memory("./cachedir", verbose=0)

@memory.cache
def expensive_function(param):
    # Operations that take a lot of resources
    return some_expensive_computation(param)
```

## Choosing the Right Strategy

- **LRU Cache**: Use when working with a fixed-size cache and accessing recently used items is more probable.
- **TTL Cache**: Suitable for data that changes over time or where freshness is critical.
- **Memoization**: Best for optimizing expensive, deterministic functions with a limited set of inputs.
- **Disk-based Caching**: Ideal for very large datasets or when cache persistence is necessary.

Implementing caching can significantly improve the performance of Python applications by reducing the need to recompute results or re-fetch data. However, it's important to choose the right caching strategy based on the application's requirements and the nature of the data being cached.