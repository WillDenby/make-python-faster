# 💨 Compiling with Cython

Cython (not to be confused with CPython) allows Python code to be compiled to C, offering significant performance enhancements for computational heavy tasks or when integrating with C libraries. 

First, you need to install Cython. It can be installed via pip: `pip install cython`

Let's start with a basic example of a Python function that sums the squares of numbers up to a given value. Here’s how you might write it in pure Python:

```python
def sum_of_squares(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total
```

To optimise this with Cython, you'd create a `.pyx` file, say `example_cy.pyx`, and include the types:

```cython
def sum_of_squares(int n):
    cdef int total = 0
    cdef int i
    for i in range(n):
        total += i ** 2
    return total
```

To compile the Cython code, you need a setup script, `setup.py`, containing:

```python
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize("example_cy.pyx"))
```

Run the compilation process with:

```shell
python setup.py build_ext --inplace
```

This generates a shared object file (`.so` or `.pyd`, depending on the OS) that you can import into Python.

## Using Cython in Jupyter Notebooks

For quick experiments, Cython can be used directly in Jupyter notebooks with the `%load_ext Cython` magic. Here’s how you can use it:

```python
%load_ext Cython

%%cython
def sum_of_squares(int n):
    cdef int total = 0
    cdef int i
    for i in range(n):
        total += i ** 2
    return total
```

## Profiling and Annotating

Cython can also generate an HTML file showing which lines of code are converted to pure C and which ones invoke the Python C-API (potentially slowing down execution). Compile with the `-a` option in your setup script, or use the `%%cython -a` magic in Jupyter notebooks to generate this annotation. Lines highlighted in yellow indicate Python interactions.