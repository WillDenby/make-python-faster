# 🐍 Python's Execution Model

Before we start considering how to make our code faster, it's worth recapping how Python programs typically work. 

CPython is the default and most widely used implementation of the Python programming language. It is written in C and Python, providing a foundation for executing Python programs. CPython compiles Python code into bytecode, which is then executed by the Python virtual machine. The execution model of CPython involves several key components and processes, including parsing, compilation, and interpretation. 

## Parsing

The Python interpreter first reads your Python code. This stage involves parsing the code into an Abstract Syntax Tree (AST). The AST represents the code's structure in a tree-like form, making it easier for the compiler to understand and manipulate.

Try running the following code, which uses the ast module to parse a simple function into an AST, illustrating what happens at the beginning of the Python code execution process:

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

After parsing, the AST is compiled into bytecode. Bytecode is a low-level, platform-independent representation of your code that can be executed by the Python virtual machine (PVM).

The following code compiles a string of Python code into bytecode and then disassembles it to inspect the bytecode instructions that the Python virtual machine will execute:

```python
import dis

def greet(name):
    return f'Hello, {name}!'

# Compile the function into bytecode
compiled_code = compile('greet("World")', '<string>', 'exec')

# Disassemble to see the bytecode
dis.dis(compiled_code)
```

## Python Virtual Machine (PVM)

The Python virtual machine is the runtime engine of CPython. It executes the bytecode produced during the compilation stage. The PVM is an interpreter for the bytecode, going through the instructions one by one and performing the specified operations.

### In Conclusion

The execution model of CPython can be summarized as follows:

1. Source Code: The Python source code (.py files) is written by the programmer.
2. AST: The source code is parsed into an Abstract Syntax Tree, representing the syntactical structure.
3. Bytecode Compilation: The AST is compiled into bytecode, a lower-level, platform-independent code.
4. PVM Execution: The Python virtual machine executes the bytecode, performing operations as specified.

The efficiency and performance of CPython can be affected by factors such as the complexity of the Python code, the use of built-in functions (which are typically optimized C functions), and the interaction with external modules and libraries.

It's also worth noting that while CPython is the standard and most commonly used Python interpreter, other implementations exist, such as PyPy (which focuses on performance through Just-In-Time compilation) and Jython (which runs on the Java platform). Each implementation has its execution model, optimized for different use cases and performance characteristics.

We'll explore more of these things in subsequent chapters. 