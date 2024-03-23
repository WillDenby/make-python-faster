# Cython: Pure C-based Compiling

Cython serves as an extension of Python, designed to give C-like performance with code that is written mostly in Python. It is a powerful tool for optimizing and speeding up Python code, especially in areas where performance is critical, such as scientific computing, data analysis, and machine learning. Cython achieves this by allowing the inclusion of static type declarations, which can then be compiled into C or C++ code. This compiled code can be executed much faster than the equivalent Python code. Additionally, Cython can be used to wrap C and C++ libraries, making it possible to use them from Python code.

Here's a simple overview of how Cython works:

Type Annotations: Unlike Python, Cython allows you to add C-style static type definitions to your Python code. These type definitions are optional but can significantly increase the speed of your code by reducing the overhead of Python's dynamic typing.
Compilation: The Cython compiler translates the annotated Cython code into C or C++ code. This code is then compiled by a C/C++ compiler to produce a shared library that can be imported into Python.
Integration: The compiled Cython module can now be used from Python, just like any Python module. This allows for seamless integration of performance-critical code with higher-level Python scripts.

## Using Cython

Cython, as an AOT compilation method, requires a bit of fiddly set-up.

You need to `pip install cython` to begin.

Cython files end in `.pyx`. Here's `sum_squares.pyx` as an example function:

```python
# Defining a function with Cython type annotations for C-level speed.
def sum_of_squares(int n):
    # Declaring a C int type for the loop variable.
    cdef int i
    cdef int sum = 0
    for i in range(n):
        sum += i * i
    return sum
```

Next, you need to create a `setup.py` file to compile the Cython module:

```python
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("sum_squares.pyx", annotate=True)
)
```

Compile the Cython module by running:

```shell
python setup.py build_ext --in-place
```

Finally, you can use the compiled module in Python:

```python
# Import the compiled Cython module
import sum_squares

# Call the Cython function
print(sum_squares.sum_of_squares(10))  # Output: 285
```

The key takeaway is that you need to add type annotations!