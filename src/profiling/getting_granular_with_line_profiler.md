# Getting Granular with line-profiler

Now we're going to get even more granular, going from `script -> function-by-function -> line-by-line`! We can use the awesome little tool, `line-profiler`. It provides way more detail, at the cost of some overhead. We can get it from PyPI: `pip install line-profiler`. 

Let's go back to our original script, with the nested loops:

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

We need to add a decorator above our function:

```python
import random 

@profile
def print_all_pairs(numbers):
    ... # same as before
```

To use `line-profiler`, we'll run the bundled `kernprof` CLI script. We include two flags: `-l` for "line-by-line" and `-v` for printing the output to the console.

```shell
python -m kernprof -lv test.py
```

And kernprof says...!

```shell
Wrote profile results to test.py.lprof
Timer unit: 1e-06 s

Total time: 6.6159 s
File: test.py
Function: print_all_pairs at line 3

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     3                                           @profile
     4                                           def print_all_pairs(numbers):
     5         1          2.0      2.0      0.0      n = len(numbers)
     6      1001        423.0      0.4      0.0      for i in range(n):
     7   1001000     423059.0      0.4      6.4          for j in range(n):
     8   1000000    6192419.0      6.2     93.6              print(numbers[i], numbers[j])
```

I'm starting to think our problem might be all this `print`-ing 😅😅







