# The Unix time Command

If you're on a Unix-like system, you can use the `time` command! This has several benefits, which we'll explore below.

Now there are actually two possible commands: a shell version (accessed through `time`) and a system command (accessed through `/usr/bin/time`). We want the latter.

Again, let's take our original, simplest script, saved as `test.py`:

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

Run it from the command line like this: `/usr/bin/time -p --verbose python test.py`

The `-p` flag puts our results on separate lines, which is prettier. You'll get something like this:

```shell
real 9.86 # this represents the total time taken
user 2.64 # this is how much time the CPU spent outside kernel functions
sys 1.09 # this is how much time spent on kernel functions
```

`real` - `user` - `sys` = time spent on IO tasks + any other system tasks.

We can see the advantage of using the Unix `time` command now: it allows us to strip away "background noise"; it also includes the time taken to load the Python executable, which may be relevant if you're profiling code that spawns lots of processes. 

Try adding `-l` on MacOS or `--verbose` on Linux for more info. `Page faults` are worth keeping an eye on - they suggest that you're using RAM and the kernel is resorting to disk access. 