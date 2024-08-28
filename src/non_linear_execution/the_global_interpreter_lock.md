# 🔒 The Global Interpreter Lock (GIL)

The GIL is a *mutex* feature (meaning “mutual exclusion”) that protects access to Python objects. It prevents multiple threads from simultaneously executing bytecodes. This lock is necessary because CPython's memory management is not thread-safe. The GIL ensures that only one thread runs in the interpreter at any given time. But it can have performance implications.

## Implications for Multi-threaded Applications

The existence of the GIL has significant implications for developers writing multi-threaded applications in Python.

While the GIL allows for concurrency (multiple threads can be created and managed), it does not allow for true parallelism (multiple threads executing simultaneously) in a single Python process. This means that multi-threaded programs that are CPU-bound may not see a performance improvement. Instead, they might even run slower due to the new overhead.

For I/O-bound applications (waiting for input/output operations to complete), the GIL has less impact. The GIL is released while waiting for I/O, allowing other threads to run. Therefore, Python's threading module can be an excellent choice for I/O-bound applications.

To achieve true parallelism, Python developers often use multiprocessing instead of multithreading. The `multiprocessing` module creates separate Python processes for each task, each with its own Python interpreter and, by extension, its own GIL. This allows tasks to run in parallel on multiple cores.

## Examples to Try

This example demonstrates how the GIL can limit the performance of CPU-bound multi-threaded programs.

```python
import threading
import time

# A simple CPU-bound function
def cpu_bound_task():
    count = 0
    while count < 10000000:
        count += 1

start_time = time.time()
threads = []
for _ in range(2):  # Create 2 threads
    thread = threading.Thread(target=cpu_bound_task)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end_time = time.time()
print(f"Duration with threads: {end_time - start_time} seconds")
```

The next example demonstrates how multi-threading can be beneficial for I/O-bound tasks, as the GIL is released during I/O operations, allowing other threads to run:

```python
import threading
import time

# A simple I/O-bound function that waits for some time, simulating an I/O operation
def io_bound_task():
    print("Task start")
    time.sleep(2)  # Simulate an I/O operation
    print("Task complete")

start_time = time.time()
threads = []
for _ in range(2):  # Create 2 threads
    thread = threading.Thread(target=io_bound_task)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end_time = time.time()
print(f"Duration with threads: {end_time - start_time} seconds")
```

In the CPU-bound example, you might not notice a significant performance improvement from using threads due to the GIL. In contrast, the I/O-bound example can benefit from multi-threading, as threads waiting for I/O allow others to run.


[Get PDF/ePub](https://makepythonfaster.gumroad.com/l/get)
