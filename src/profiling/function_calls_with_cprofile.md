# Splitting Function Calls with cProfile

Perhaps you don't want to manage a system of decorator functions, and you just want to see the breakout times for all the functions in your code. `cProfile` is a built-in tool to help. 

It adds some computational overhead, but it helps you profile which parts of your code are being called the most and quantify what time penalty they are incurring.

To demonstrate this utility, let's break our nested loop script into two functions, and remove our use of `random` to avoid any `import` overhead, as below:

```python
def inner_loop(numbers, i):
    n = len(numbers)
    for j in range(n):
        print(numbers[i], numbers[j])

def outer_loop(numbers):
    n = len(numbers)
    for i in range(n):
        inner_loop(numbers, i)

numbers = list(range(1, 1001))  # List of numbers from 1 to 1000
outer_loop(numbers)
```

Now let's run it from the command line, with `cProfile`:

```shell
python -m cProfile -s cumulative test.py
```

The `-s cumulative` flag sorts the output by cumulative time spent. It should look something like this:

```shell
1002005 function calls in 7.515 seconds

Ordered by: cumulative time

  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      1    0.000    0.000    7.515    7.515 {built-in method builtins.exec}
      1    0.000    0.000    7.515    7.515 test.py:1(<module>)
      1    0.002    0.002    7.515    7.515 test.py:6(outer_loop)
   1000    0.437    0.000    7.513    0.008 test.py:1(inner_loop)
1000000    7.075    0.000    7.075    0.000 {built-in method builtins.print}
   1001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

Makes sense! What's really costing us time is not the loops per se, but all the `print` statements.

## Plotting cProfile with SnakeViz

Everyone loves some pretty pictures! SnakeViz is 'a viewer for Python profiling data that runs as a web application in your browser'. Let's get it from PyPI: `pip install snakeviz`

To use SnakeViz, you need to have generated an output file (`-o`) using `cProfile`. So let's try something like this:

```shell
python -m cProfile -o program.prof test.py
snakeviz program.prof
```

... which will open up the SnakeViz page in your browser. At the top is a waterfall diagram. Here's my hovering over the middle bar, displaying information about the `outer_loop` function:

![SnakeViz visualisation of Python script](../assets/SnakeVizTop.png)

At the bottom is a filterable table, allowing you to interact with the conventional cProfile output:

![SnakeViz tabular representation of Python script](../assets/SnakeVizBottom.png)