#  The Simplest Method: time.time() + print

Let's create a simple Python function with a time complexity of O(n<sup>2</sup>). This is a "CPU-bound" problem.

The function `print_all_pairs` takes a list of numbers as input and prints out all pairs of numbers from the list. The function `generate_random_numbers` returns a list of numbers as long as its input, in which all the numbers are between 1 and a 1000. Feel free to run it first, to make sure everything's working.

```python
import random

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

Now let's use Python's built-in time module to add some super-simple profiling! This involves adding a few lines of code, commented below

```python
import random
import time # import the time module

... # leave our functions as they are

random_numbers = generate_random_numbers(1000)

start_time = time.time() # start the clock
print_all_pairs(random_numbers)
end_time = time.time() # stop the clock

time_taken = end_time - start_time # calculate the time taken
print(time_taken) # print the result
```

Be aware that the `time_taken` will always vary - it's an approximation. Your computer might be doing other more- or less-intensive things, at any given time. 