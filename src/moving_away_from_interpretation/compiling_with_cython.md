# 💨 Compiling with Cython

Cython is a powerful tool that allows Python code to be compiled to C, offering significant performance enhancements, especially for computational heavy tasks or when integrating with C libraries. It's particularly useful for optimizing bottlenecks in Python code. Here’s an overview of how you can use Cython to achieve these performance gains:

## Basic Example

First, you need to install Cython. It can usually be installed via pip: `pip install cython`

Let's start with a basic example of a Python function that sums the squares of numbers up to a given value. Here’s how you might write it in pure Python:

```python
def sum_of_squares(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total
```

To optimize this with Cython, you'd create a .pyx file, say example_cy.pyx, and type the variables for C-level performance:

```cython
def sum_of_squares(int n):
    cdef int total = 0
    cdef int i
    for i in range(n):
        total += i ** 2
    return total
```

## Compilation

To compile the Cython code, you need a setup script, setup.py, containing:

```python
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize("example_cy.pyx"))
```

Run the compilation process with:

```shell
python setup.py build_ext --inplace
```

This generates a shared object file (.so or .pyd, depending on the OS) that you can import in Python.

## Using Cython in Jupyter Notebooks

For quick experiments, Cython can be used directly in Jupyter notebooks with the %load_ext Cython magic command. Here’s how you can use it:

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

Cython can generate an HTML file showing which lines of code are converted to pure C and which ones invoke the Python C-API (potentially slowing down execution). Compile with the -a option in your setup script or use the %%cython -a magic command in Jupyter notebooks to generate this annotation. Lines highlighted in yellow indicate Python interactions, urging a closer look for potential optimization.

## Tips for Optimization

- **Typing Variables**: Use cdef to declare C static types for variables.
- **Function Definitions**: Use cpdef for functions you want to call both from Python and Cython-compiled C code. It generates both a C-callable function and a Python wrapper.
- **Avoiding Python Objects**: Whenever possible, operate on C types rather than Python objects to avoid overhead.
- **Loop Unrolling**: In some cases, manually unrolling loops can lead to performance gains.

Cython is a vast topic, and these examples just scratch the surface. For deeper computational tasks, integrating with C libraries, or further optimizations, the Cython documentation is an excellent resource.