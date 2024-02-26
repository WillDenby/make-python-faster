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

But if all we're going to do with this list is subsequently iterate over it, there's a better approach: using a generator function. In the following code, let's implement a naive builder and iterator, and then a generator version. We'll do some time-profiling. Then we'll inspect more closely how the iterator version works. 


```python
import math

# This is the naive implementation again
def naive_builder(n):
    square_numbers = []
    for _ in range(n):
        square_numbers.append((_+1)**2)
    return square_numbers

# Now we're iterating over it. For banter, let's find the square roots.
for number in naive_builder(10000):
    print("The square root of ", number, "is ", int(math.sqrt(number)))

# Now let's implement the naive function as a generator
def generator_builder(n):
    for _ in range(n):
        yield (_+1)**2 # See what's changed!

for number in generator_builder(10000):
    print("The square root of ", number, "is ", int(math.sqrt(number)))
```

