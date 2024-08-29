# 🐍 Python's Execution Model

In this chapter, we’ll explore how CPython, the default implementation of Python, works under the hood. This will help to contextualise optimisation techniques mentioned later on. 

Python is an *interpreted* language. This means that your Python code isn’t directly executed by your computer. Instead, another program like CPython (i.e. an interpreter) parses your code, compiles it into an intermediate representation, and then executes the relevant instructions. 

As a rule, interpreted languages like Python or Ruby are slower than compiled alternatives, like C or Rust, because of the additional overheads introduced by the execution model.

## Parsing

CPython begins by parsing your code into an Abstract Syntax Tree (AST). The AST represents the code's structure in a tree-like form, making it easier to understand and manipulate.

Try running the following code, which uses the `ast` module to parse a simple function:

```python
import ast

code = """
def greet(name):
    return f'Hello, {name}!'
"""

tree = ast.parse(code)
print(ast.dump(tree, indent=4))
```

## Compilation

After parsing, the AST is compiled into bytecode, which is a low-level, platform-independent representation of your code. It contains instructions which can be executed by CPython’s virtual machine.

The following code snippet compiles a string of Python code into bytecode, and then disassembles it to inspect the bytecode instructions:

```python
import dis

def greet(name):
    return f'Hello, {name}!'

# Compile the function into bytecode
compiled_code = compile('greet("World")', '<string>', 'exec')

# Disassemble to see the bytecode
dis.dis(compiled_code)
```

## Execution

The Python Virtual Machine (PVM) is the runtime engine of CPython. It executes the bytecode produced by the compilation stage, by going through the instructions one by one and performing the specified operations.

## In Summary

The execution model of CPython can be summarised as follows:

1. Source Code: The Python source code (`.py` files) is written by the programmer.
2. AST: The source code is parsed into an Abstract Syntax Tree, representing the syntactical structure.
3. Bytecode Compilation: The AST is compiled into bytecode, a lower-level, platform-independent code.
4. PVM Execution: The Python virtual machine executes the bytecode, performing operations as specified.

The efficiency and performance of CPython can be further affected by factors such as the structural complexity of the Python code, or the interaction with external modules and libraries.

While CPython is the standard Python interpreter, other implementations exist, such as PyPy (which focuses on performance through Just-In-Time compilation) or GraalPy (which runs on the GraalVM Java platform). These implementations have different execution models, optimised for different use cases and performance characteristics. We'll explore these later on in the *Alternative Python Interpreters* chapter.




[Get PDF](https://makepythonfaster.gumroad.com/l/get)
