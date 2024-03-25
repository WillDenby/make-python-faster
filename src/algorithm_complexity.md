# 🧠 Algorithm Complexity

We should also briefly recap algorithm complexity.

Algorithm complexity encompasses both time complexity and space complexity. I.e. it measures the efficiency of an algorithm in terms of the time it takes to run (time complexity) and the amount of memory it consumes (space complexity) as a function of the size of the input data. 

Understanding algorithm complexity is essential for writing efficient code, especially in languages like Python, where execution speed and resource management can be vital considerations in the development of scalable and performant applications.

## Time Complexity

Time complexity measures how the runtime of an algorithm changes as the size of the input data increases. It's often expressed using Big O notation, which provides an upper bound on the growth rate of the algorithm's runtime, helping to understand its worst-case scenario.

**Constant Time (O(1))**: The execution time remains constant regardless of the input size. For example, accessing any element in an array by index.

**Linear Time (O(n))**: The execution time increases linearly with the size of the input. For example, searching for an element in an unsorted list.

```python
def find_element(lst, key):
    for item in lst:
        if item == key:
            return True
    return False
```

**Logarithmic Time (O(log n))**: The execution time grows logarithmically with the size of the input. Binary search is a classic example.

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

**Quadratic Time (O(n^2))**: The execution time grows quadratically with the input size. A common example is the bubble sort algorithm.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

## Space Complexity

Space complexity measures the total amount of memory that an algorithm needs to run as a function of the size of the input data. Like time complexity, it's often expressed in Big O notation.

**Constant Space (O(1))**: The algorithm requires a fixed amount of memory space regardless of the input size.

**Linear Space (O(n))**: The space required by the algorithm increases linearly with the size of the input data.

For example, merging two lists requires additional space proportional to the sum of both lists' sizes, making its space complexity O(n).

```python
def merge_lists(lst1, lst2):
    return lst1 + lst2  # Creates a new list with elements of lst1 followed by elements of lst2
```

Understanding and optimizing the complexity of algorithms can significantly impact the performance of Python applications. Lower complexity often translates to faster execution times and lower resource consumption, which is particularly important in resource-constrained environments or applications that handle large volumes of data.