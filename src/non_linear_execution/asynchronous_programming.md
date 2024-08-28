# ⏰ Asynchronous Programming

AsyncIO is a Python library for writing concurrent code using the async/await syntax. It's designed to handle asynchronous IO tasks, such as network and file I/O, and make effective use of wait times. 

## Key Concepts

**Asynchronous programming**: Asynchronous programming enables the program to start a task and move on to another one before the first one finishes.

**Coroutines**: Coroutines are special functions that work asynchronously. They are defined with `async def` and are used to pause and resume execution using the await keyword.

**Task**: A task is used to schedule coroutines concurrently. When a coroutine is wrapped into a task with functions like `asyncio.create_task()`, it's scheduled to run on the event loop.

**Event loop**: The event loop is the core of every `asyncio` application. It runs in a loop, executing asynchronous tasks and callbacks, and handles all the switching between tasks.

## Event Loop Workflow

1. The event loop starts with `asyncio.run()` or manually with `loop = asyncio.get_event_loop()` and `loop.run_until_complete()`.
2. Tasks are scheduled to run in an event loop. They can be coroutines or other future-like objects.
3. While executing tasks wait for an I/O operation to complete, the event loop can switch and execute other tasks.
4. Once all tasks are completed, the event loop is stopped and closed.

## Practical Applications

AsyncIO is ideal for I/O-bound and high-level structured network code. Examples include:

- Web scraping
- Web servers and client applications
- Database query handling
- Network servers and clients
- File I/O operations

## Code Examples

Here’s an example of a basic coroutine:

```python
import asyncio

async def hello_world():
    print("Hello")
    await asyncio.sleep(1)  # Simulate I/O operation
    print("World")

asyncio.run(hello_world())
```

What about multiple coroutines?

```python
import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)
    print("Data fetched")
    return {'data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    # Wait for all tasks to complete
    await task1
    await task2

asyncio.run(main())
```

You can even use the event loop directly (but this is less common in modern `asyncio` code):

```python
import asyncio

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    loop = asyncio.get_event_loop()
    task = loop.create_task(say_after(1, 'hello'))
    await task

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
```

These examples illustrate the basic usage of AsyncIO for concurrent programming in Python. AsyncIO's power lies in its ability to handle many tasks simultaneously, making it a valuable tool for any I/O-bound application.


[Get PDF/ePub](https://makepythonfaster.gumroad.com/l/get)
