# Sensible Loop Design

In a second, we'll go on to vector computation, and see why Python's built-in lists aren't great for handling these. 

But before that, it's worth looking more closely at the loop construct, and considering two ways in which we can easily optimise our programs. The first of these involves a built-in `generator`!

```python
def slow_sum_of_squares(numbers):
    result = 0
    for num in numbers:
        result += num ** 2
    return result

def fast_sum_of_squares(numbers):
    result = sum(num ** 2 for num in numbers)
    return result

# Example usage:
numbers = list(range(1, 1000000))
slow_result = slow_sum_of_squares(numbers)
fast_result = fast_sum_of_squares(numbers)
```

Let's run it from the command line, with our trusty friend `cProfile` (described back [here](../profiling/function_calls_with_cprofile.md)):

```shell
python -m cProfile -s cumulative test.py
```

You'll see that the `fast_sum_of_squares` number is astonishingly quick!

## Avoiding Unnecessary Calculations

Let's look at an even more explicit and simple example.

Imagine we're collecting money for a charity, and a company has promised to match what's raised. Let's go and collect a million donations, where everyone gives up to $1m (aren't people wonderful). Now we want to know the final amount!

We could:
- multiple every donation by two before adding it to the running total
- add every donation to the running total, and then double it at the end

Obviously the below is a stuipdly inefficient way of calculating, but I was trying to come up with an artificial example to make a point!

```python
import random

def slow_match(donations):
    total = 0
    for donation in donations:
        total += donation * 2
    return total

def fast_match(n):
    total = 0
    for donation in donations:
        total += donation
    return total * 2

donations = list(random.randint(1, 1000000) for _ in range(1000000))

slow_method = slow_match(donations)
fast_method = fast_match(donations)
```

Again, run it with `cProfile`. On my machine, I knock off 30% by using fast_match. Computers are fast, but operations obviously still take time! So you might as well avoid repetitive code when possible. 

Above was a trite example. But you may have more complex calculations being reused. There's no need to keep computing and then reallocating the result to a place in memory if it's unchanging.