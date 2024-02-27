# Let's Get Generating

In this chapter, we'll look at the comprehension, iteration, and evaluation of generators, as a way to lazily evluate and poll loops. 

Imagine we want to write a function that takes a integer `n` as input, and returns a `n` length list of square numbers, starting from 1<sup>2</sup>.

Here's a naive implementation:

```python
def naive_builder(n):
    square_numbers = []
    for _ in range(n):
        square_numbers.append((_+1)**2)
    return square_numbers
```

The issue is that when `n` gets big, so will the list `square_numbers`. We've seen how `list.append()` has compute overhead as an operation. We're also then going to have a memory-hogging array at the end of it. Great...

But if all we're going to do with this list is subsequently iterate over it, there's a better approach: using a generator function. In the following code, let's implement a naive builder and iterate over its list, and then a generator version. We'll do some time-profiling. Then we'll inspect more closely how the iterator version works. 

```python
import math
import time

n = int(input("How many iterations? "))

# This is the naive implementation again
def naive_builder(n):
    square_numbers = []
    for _ in range(n):
        square_numbers.append((_+1)**2)
    return square_numbers

# What's changed in our generator function?
def generator_builder(n):
    for _ in range(n):
        yield (_+1)**2 
        
# Let's iterate over each and time it!
naive_start_time = time.time()
for number in naive_builder(n):
    pass # do something
naive_end_time = time.time() 

gen_start_time = time.time() 
for number in generator_builder(n):
    pass # do something
gen_end_time = time.time()

# Calculate time taken
naive_time_taken = naive_end_time - naive_start_time
print("Naive: ", naive_time_taken) 

gen_time_taken = gen_end_time - gen_start_time 
print("Generator: ", gen_time_taken)
```

Here's what I got on my machine for running over 100m items - you'll see why generators are so good now!

```shell
How many iterations? 100000000
Naive:  26.604732751846313
Generator:  16.16110110282898
```

That's about a 40% speed improvement. 