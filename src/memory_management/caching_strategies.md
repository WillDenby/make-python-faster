# 💾 Caching Strategies

You can also use caching strategies (i.e. ways of storing data in a temporary area) to serve future requests for the same data faster. Caching is useful in situations where retrieving data, or computing it, is resource-intensive. You don’t want to perform these operations more than once! Python provides various tools for caching, as described below. 

## LRU (Least Recently Used) Cache

The LRU caching strategy removes the “least recently used” items first. It’s useful in applications where you want to cache a limited number of items and when the likelihood of accessing recently used items is high.

Python's `functools` module provides an `@lru_cache` decorator to implement LRU caching. It can be applied to any function whose output you want to cache:

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def expensive_function(param):
    # Simulate an expensive operation
    return some_expensive_computation(param)
```

## Memoization

Memoization is a specific form of caching that involves storing the results of expensive function calls and returning the cached result when the same inputs occur again. Memoization is a form of LRU caching but is specifically applied to function calls. The `@lru_cache` can also be used for memoization:

```python
from functools import lru_cache

@lru_cache(maxsize=None)  # No limit on cache size
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

## TTL (Time To Live) Cache

TTL caching invalidates cache entries after a set period. This strategy is suitable when the data changes over time or if you want to ensure that data doesn't become stale. The `cachetools` library offers TTL caching capabilities:

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

When you are dealing with large amounts of data or you need to persist a cache across program restarts, disk-based caching help. Libraries such as `joblib` provide mechanisms for storing cache data on disk:

```python
from joblib import Memory
memory = Memory("./cachedir", verbose=0)

@memory.cache
def expensive_function(param):
    # Operations that take a lot of resources
    return some_expensive_computation(param)
```

## Choosing the Right Strategy

Implementing caching can significantly improve the performance of Python applications by reducing the need to recompute results or re-fetch data. However, it's important to choose the right caching strategy based on the application's requirements and the nature of the data being cached. To summarise:

- LRU caching is useful for fixed-size caches, and when recent data is more likely to be accessed
- Memoization is best for optimising expensive functions with a limited set of inputs
- TTL caching is suitable for data that changes over time, which needs a degree of “freshness”
- Disk-based caching is ideal for large amounts of data, or when you need cache persistence. 



[Get PDF](https://makepythonfaster.gumroad.com/l/get)
