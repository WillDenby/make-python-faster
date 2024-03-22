# Ready: Sets, Dictionaries

The order of elements was important in `lists` and `tuples`, but what if we don't care about that? As long as every element is unique (or at least the keys are), we can use another two native data structures in Python: `sets` and `dictionaries`. The relationship between them can be summarised as follows:

|     | Sets    | Dictionaries    |
| ----------- | ----------- | ----------- |
| **Keys**   | ✅    | ✅    |
| **Values**   | ❌    | ✅    |

I.e. a `set` is a data structure containing unique elements; a `dictionary` is a data structure containing unique elements (it's keys), each of which have some associated data (their values). 

Let's summarise the pros and cons of `sets`/`dictionaries` vs `lists/tuples`, on average time complexities for operations and needs:

| | Sets/Dictionaries | Lists/Tuples | Who Wins? |
| ----------- | ----------- | ----------- | ----------- |
| **Search** | O(1) | O(n) | Sets/Dictionaries |
| **Membership (x in y)** | O(1) | O(n) | Sets/Dictionaries |
| **Insertion** | O(1) | O(1) | Lists/Tuples (just) |
| **Iteration** | O(n) | O(n) | Lists/Tuples (just) |
| **Sorting** | N/A | O(n log n) | Lists/Tuples (obvs) |
| **Deletion** | O(1) | O(n) | Sets/Dictionaries |
| **Memory** | More (Hashing) | Less | Lists/Tuples |

Why do sets/dictionaries use more memory? In simple terms, creating one requires an allocation of a block of memory. A hash function then enables the key to be used as an index, allowing for O(1) look-up - just as `list[index]` is O(1) too. Python does some further optimising under the hood by putting the keys/values into their own array. But still, hash tables are bigger because by nature they contain empty buckets. Also, when a hash table becomes more than 2/3rds full, there's a compute cost of expanding the table (to `3 * len(set)`). 

One other thing to note is that the O(1)s in the Sets/Dictionaries column can also disguise a potential constant factor - how quick the hashing algorithm is. But in general, sets and dictionaries outperform if you're just wanting to add, check, and delete unique elements from groups. Try running the code below to see what I mean!

```python
import time

# Create our list and set
unique_list = list(range(100000))
unique_set = set(unique_list)

# Let's iterate through the list and perform membership tests
start_time = time.time()
for i in unique_list:
    _ = i in unique_list
list_time = time.time() - start_time
print("List lookup time:", list_time)

# Compare this with the set
start_time = time.time()
for i in unique_set:
    _ = i in unique_set
set_time = time.time() - start_time
print("Set lookup time:", set_time)
```

Here were my results 😲

```shell
List lookup time: 49.48573088645935
Set lookup time: 0.010624885559082031
```

## A Note about Imports and Namespace Dictionary Look-Ups

It's obvious to avoid unneccesary `import` statements in your script. It's also faster to be explicit with your imports, due to how Python finds things from its namespaces. 

It does dictionary look-ups to find things in this order: `locals() -> globals() -> __builtin__` - and stops when it finds what it's looking for. 

Hence the results of this code:

```python
import random
from random import randint

def func1(n):
    result = 0
    for _ in range(n):
        result += random.randint(1, 100)
    return result

def func2(n):
    result = 0
    for _ in range(n):
        result += randint(1, 100)
    return result

def func3(n, randint=random.randint):
    result = 0
    for _ in range(n):
        result += randint(1, 100)
    return result

# Testing the functions
print(func1(1000000))
print(func2(1000000))
print(func3(1000000))
```

Let's use our trusty friend [cProfile](../profiling/function_calls_with_cprofile.md):

```python
python -m cProfile test.py
```

Here's the bit of the output we're interested in:

| tottime | function |
| ----- | ----- |
0.381 | test.py:4(func1) |
0.358 | test.py:10(func2) |
0.353 | test.py:16(func3) |

Why's this happened? Let's look at the code more closely:

- In func1, we explicitly ask to look at the `random` library, so Python has to go all the way to the __builtin__ map to find what it needs. That requires the most dictionary look-ups, and takes the longest time.
- func2 leverages the `from random import randint` line so that it can now find the `randint` function in `globals()`. But it's still traversing the `locals()` map and doing a dictionary look-up. 
- func3 brings `randint` into the `locals()` namespace, minimising Python's search. It looks clunky, but if you're writing code where every millisecond counts... 






