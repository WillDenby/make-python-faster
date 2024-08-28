# 📦 The Collections Module

The `collections` module in Python provides specialised container datatypes, that are alternatives to Python's general-purpose containers like dicts, lists, sets, and tuples. 

These specialised containers are designed to provide additional functionality and can sometimes lead to more efficient code, both in terms of speed and memory usage.

## namedtuple()

Use these when you need to access elements by name to make the code more readable and self-documenting. Access is as fast as a normal tuple because `namedtuple` instances are just as lightweight. For example:

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
pt = Point(1, 2)
print(pt.x, pt.y)  # Output: 1 2
```

## deque

Use `deque` when you need to add or pop elements from both ends of a collection efficiently. It provides faster appends and pops from the left end but is slower than lists for random access:

```python
from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)  # Add to the left
dq.pop()  # Remove from the right
print(dq)  # Output: deque([0, 1, 2])
```

## Counter

Counters make counting the occurrence of elements in an iterable, and performing element-wise operations, more efficient than manually using a dictionary. For example:

```python
from collections import Counter

cnt = Counter('abracadabra')
print(cnt)  # Output: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
```

## OrderedDict

Prior to Python 3.7, normal dicts didn’t preserve insertion order. `OrderedDict` can be useful if your code still relies on earlier Python versions:

```python
from collections import OrderedDict

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od['d'] = 4
print(od)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
```

## defaultdict

When you need a dictionary that automatically initialises non-existent keys with a default value, `defaultdict` can help: 

```python
from collections import defaultdict

dd = defaultdict(list)
for i in ['a', 'b', 'a']:
    dd[i].append(1)
print(dd)  # Output: defaultdict(<class 'list'>, {'a': [1, 1], 'b': [1]})
```

## ChainMap

`ChainMap` lets you combine multiple dictionaries or mappings into a single view, avoiding potentially costly dictionary merges:

```python
from collections import ChainMap

defaults = {'color': 'red', 'user': 'guest'}
environment = {'user': 'admin', 'path': 'bin'}
cm = ChainMap(environment, defaults)
print(cm['color'])  # Output: red
print(cm['user'])  # Output: admin
```


[Get PDF/ePub](https://makepythonfaster.gumroad.com/l/get)
