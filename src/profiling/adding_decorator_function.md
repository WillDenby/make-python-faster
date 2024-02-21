# Adding a Decorator Function

Using `time.time()` and some `print` statements is a quick-and-dirty way to do some initial profiling. But it can get messy! Using a decorator is both neater and more extendable. 

Let's reuse our code from before, but add a decorator method! 

```python
import random
import time
from functools import wraps # add this import, so that we can access the decorated functions

# here's our profiler function
def time_profiler(function): 
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{function.__name__}' took {execution_time:.6f} seconds to execute.")
        return result
    return wrapper

@time_profiler # add our decoractor for profiling
def print_all_pairs(numbers):
    n = len(numbers)
    for i in range(n):        
        for j in range(n):    
            print(numbers[i], numbers[j])

def generate_random_numbers(length):
    return [random.randint(1, 1000) for _ in range(length)]

random_numbers = generate_random_numbers(1000)
print_all_pairs(random_numbers)
```

Run this from your terminal and you'll get something like: `Function 'print_all_pairs' took 7.186900 seconds to execute.`

If we're wanting to profile multiple functions in a more complex piece of code, we can just add the `@time_profiler` decorator above any of the function names.