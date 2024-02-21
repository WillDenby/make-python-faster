# The timeit Module: Profiling from the Terminal

We can also use Python's built-in `timeit` module to test our script from the command line. This helps solve for any CPU fluctuations in our profiling time, by running several loops and iterations. 

Let's go back to our original Python script:

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

Then, in your terminal, you'll want to run the following:

```shell
python -m timeit -v -s "import test; random_numbers = test.generate_random_numbers(1000)" "test.print_all_pairs(random_numbers)"
```

I've included the `-v` (i.e. `--verbose`) flag, because I want to see the cumulative time spent, from which I can calculate an average variability. This will output something like:

```shell 
raw times: 10.8 sec, 9.85 sec, 8.05 sec, 9.03 sec, 10 sec

1 loop, best of 5: 8.05 sec per loop
```

**Pretty consistent! 😎**
**But timeit seems to have slowed me down vs the decoractor method 😞**

Other flags you might want to include are `-n` (number of loops) and `-r` (number of repetitions). If you leave this out, timeit will use its defaults. 

## The %timeit Magic: Profiling in Jupyter

If you're using a Jupyter Notebook, you can do something similar with the `%timeit` magic. Stick it before what you want to profile:

```python
%timeit print_all_pairs(random_numbers)
```

N.B. the methodology behind the Python `timeit` module and the Jupyter `%timeit` magic is a little different: the former picks the quickest time; the latter gives the mean and standard deviation.
