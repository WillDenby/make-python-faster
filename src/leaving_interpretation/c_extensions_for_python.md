# 🇨 C Extensions for Python

Lots of AI/ML libraries call C code under the hood, with Python serving as a lightweight “glue”. Writing C extensions for Python is a powerful technique for optimising critical performance paths in Python applications. 

## Writing a C Extension

A C extension needs to implement a set of initialisation functions that the Python interpreter calls when the module is imported.Here’s a simple example, that defines a function `fast_add`, which adds two numbers with type checking for performance.

```c
#include <Python.h>

/* The C function to add two numbers */
static PyObject* fast_add(PyObject* self, PyObject* args) {
    long a, b;
    if (!PyArg_ParseTuple(args, "ll", &a, &b)) {
        return NULL; // If the input isn't two longs, return NULL
    }
    return PyLong_FromLong(a + b);
}

/* Method definition object */
static PyMethodDef FastAddMethods[] = {
    {"fast_add", fast_add, METH_VARARGS, "Add two numbers quickly."},
    {NULL, NULL, 0, NULL} // Sentinel
};

/* Module definition */
static struct PyModuleDef fastaddmodule = {
    PyModuleDef_HEAD_INIT,
    "fastadd", // name of module
    "A module that adds two numbers quickly.", // module documentation
    -1,       // size of per-interpreter state of the module, or -1 if the module keeps state in global variables.
    FastAddMethods
};

/* Module initialization function */
PyMODINIT_FUNC PyInit_fastadd(void) {
    return PyModule_Create(&fastaddmodule);
}
```

To compile the extension, you'll need to create a `setup.py` file for your module. This file uses `setuptools` to compile your C code into a Python extension module:

```python
from setuptools import setup, Extension

module1 = Extension('fastadd',
                    sources = ['fastaddmodule.c'])

setup(name = 'FastAddPackage',
      version = '1.0',
      description = 'This is a demo package for adding two numbers.',
      ext_modules = [module1])
```

After creating the `setup.py` file, you can build the module by running the following command in your terminal:

```shell
python setup.py build_ext --inplace
```

Once the module is compiled, you can import and use it in Python like any other module:

```python
import fastadd

result = fastadd.fast_add(5, 10)
print(result)  # Output: 15
```

## Points to Remember

Writing C extensions can greatly improve the performance of your Python program, but it also introduces complexity and the potential for hard-to-debug errors. Here are some helpful pointers:

**Error Handling**: Proper error handling in C is crucial. Make sure to check for errors and return `NULL` in your C functions if any occur to avoid crashing the interpreter.

**Reference Counting**: Pay attention to reference counting when working with Python objects in C, to prevent memory leaks or crashes.

**Compatibility**: Keep in mind Python version compatibility, in case of variations in the API.



[Get PDF](https://makepythonfaster.gumroad.com/l/get)
