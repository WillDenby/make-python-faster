# 🪢 concurrent.futures

The `concurrent.futures` module in Python provides a high-level interface for asynchronously executing callables. It abstracts away many of the lower-level details of thread or process management. 

The module offers two main executor classes - `ThreadPoolExecutor` and `ProcessPoolExecutor`. The former is used for executing tasks in separate threads, making it ideal for I/O-bound tasks. The latter runs each task in a separate process, circumventing the Global Interpreter Lock (GIL), and is more suitable for CPU-bound tasks.

## Basic Usage

Tasks can be submitted for execution using the `submit()` method, which schedules the callable to be executed and returns a `Future` object. A `Future` represents the eventual result of a computation:

```python
from concurrent.futures import ThreadPoolExecutor

def task(n):
    return n ** 2

# Create a ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=3) as executor:
    future = executor.submit(task, 5)
    print(future.result())  # Prints: 25
```

The `map()` function is similar to the built-in `map`, but it executes the function across multiple threads or processes in parallel. It returns an iterator that yields the results of the function calls:

```python
from concurrent.futures import ThreadPoolExecutor

def task(n):
    return n ** 2

# Using ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, [1, 2, 3, 4, 5])
    for result in results:
        print(result)  # Prints the squares of the numbers
```

## Handling Future Results

The `Future` object allows you to check if the task has completed (`done()`), wait for its completion (`result()`), and even cancel the task (`cancel()`). It encapsulates the asynchronous execution of a callable and provides methods to check its status and retrieve its result:

```python
from concurrent.futures import ThreadPoolExecutor
import time

def task():
    time.sleep(1)
    return "Task completed"

with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(task)
    print(future.done())  # False, the task is not completed yet.
    time.sleep(1.5)
    print(future.done())  # True, the task is now completed.
    print(future.result())  # "Task completed"
```

## Exception Handling

When the callable raises an exception, the `Future` object catches it. The exception will be re-raised when you call `result()`:

```python
from concurrent.futures import ThreadPoolExecutor

def task():
    raise Exception("Task error")

with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(task)
    try:
        result = future.result()  # This will raise the exception thrown by task()
    except Exception as e:
        print(e)  # Prints: Task error
```

## Choosing Between ThreadPoolExecutor and ProcessPoolExecutor

To summarise, the `concurrent.futures` module abstracts the complexity of thread and process management, providing an easy-to-use interface for executing tasks concurrently.

Use `ThreadPoolExecutor` for I/O-bound tasks or when executing a large number of small tasks. Use `ProcessPoolExecutor` for CPU-bound tasks to take advantage of multiple CPU cores.