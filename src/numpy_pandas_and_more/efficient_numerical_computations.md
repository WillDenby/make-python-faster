# ⚡ Efficient Numerical Computations

Here's an overview of how NumPy can be leveraged for efficient numerical computations, along with some code examples.

## Basic Array Operations

NumPy arrays support a wide range of mathematical operations that can be performed efficiently and with concise syntax.

**Creating Arrays:**

```python
import numpy as np

# Create a 1D array
a = np.array([1, 2, 3])

# Create a 2D array (matrix)
b = np.array([[1, 2, 3], [4, 5, 6]])

# Create an array filled with zeros
c = np.zeros((2, 3))

# Create an array filled with ones
d = np.ones((3, 2))

# Create an identity matrix
e = np.eye(3)
```

**Arithmetic Operations:**

Operations are element-wise and can be used to efficiently perform computations across arrays.

```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Addition
print(x + y)

# Subtraction
print(x - y)

# Multiplication
print(x * y)

# Division
print(x / y)
```

## Advanced Array Operations

NumPy provides advanced functionalities, including broadcasting, vectorized operations, and complex slicing.

**Broadcasting:**

Broadcasting allows NumPy to work with arrays of different shapes during arithmetic operations.

```python
a = np.array([1, 2, 3])
b = np.array([[0], [10], [20], [30]])

# Broadcasting allows these to be added even though they're different shapes
print(a + b)
```

**Vectorized Operations:**

Vectorized operations enable operations to be performed on arrays without explicit loops, which can significantly improve performance.

```python
# Calculate the sine of each element
angles = np.array([0, np.pi/2, np.pi])
print(np.sin(angles))
```

## Linear Algebra

NumPy provides a set of functions for linear algebra operations, making it simple to perform tasks like matrix multiplication, finding determinants, solving linear systems, and more.

```python
# Matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))

# Determinant
print(np.linalg.det(A))

# Solve linear system Ax = b
b = np.array([1, 2])
x = np.linalg.solve(A, b)
print(x)
```

## Statistical Functions

NumPy also includes functions for performing statistical operations on arrays, such as finding the mean, median, standard deviation, etc.

```python
data = np.array([1, 2, 3, 4, 5])

# Mean
print(np.mean(data))

# Median
print(np.median(data))

# Standard deviation
print(np.std(data))
```