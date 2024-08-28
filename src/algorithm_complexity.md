# 🧠 Algorithm Complexity

Reducing the algorithmic complexity of your code can be the key to optimisation, especially in languages like Python, whose interpreted nature means that suboptimal algorithm choice or design can incur significant performance costs. Complexity can refer to both time and space.

## Time Complexity

Time complexity measures how the runtime of an algorithm changes as the size of the input data increases. It's normally expressed in Big O notation, which indicates the upper bound of the growth rate. 

**Constant Time - O(1)**: The execution time remains constant regardless of the input size. For example, accessing an element in an array by its index.

**Logarithmic Time - O(log n)**: The execution time grows logarithmically with the size of the input. Binary search is a classic example:

```python
def binary_search(arr, low, high, key):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, low, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, high, key)
    else:
        return -1
```

**Linear Time - O(n)**: The execution time increases linearly with the size of the input. For example, searching for an element in an unsorted list:

```python
def find_element(lst, key):
    for item in lst:
        if item == key:
            return True
    return False
```

**Quadratic Time - O(n^2)**: The execution time grows quadratically with the input size. A common example is the bubble sort algorithm (Obama’s favourite algorithm!):

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

## Space Complexity

Space complexity, on the other hand, measures the total amount of memory that an algorithm needs to run as a function of the size of the input data. Like time complexity, it can be expressed in Big O notation.

**Constant Space - O(1)**: The algorithm requires a fixed amount of memory space regardless of the input size.

**Linear Space - O(n)**: The space required by the algorithm increases linearly with the size of the input data.

For example, in Python, merging two lists requires additional space proportional to the sum of both lists' sizes, giving it a space complexity of O(n):

```python
# Creates a new list with elements of lst1 followed by elements of lst2
def merge_lists(lst1, lst2):
    return lst1 + lst2  
```

I’ll refer to both time and space complexity throughout the rest of the book. 


[Get PDF/ePub](https://makepythonfaster.gumroad.com/l/get)
