# 🏃 Leaving Interpretation

We’ve seen how the process of interpretation can slow down code execution, if lots of the following are happening:

- mathematical operations
- loops
- temporary object creation

We’ve also seen how PyPy and other alternatives can help. But we can go further. In this section, we’ll explore more explicit strategies for compiling Python code and integrating C code into Python environments. A caution, however. These strategies can add complexity, slowing your overall development velocity down. They are best used in cases of extreme requirement. 

And if your code is slow because of factors like lots of I/O, network, disk, database, or external library calls, then compiling might not improve performance much. Equally, if you’re using libraries like NumPy, then you're already tapping into under-the-hood optimisations. 

## Thinking in Types

Before exploring these strategies, it’s worth considering another reason for why Python is slow: it's dynamically-typed. The virtual machine has to be prepared for datatypes to potentially change, from e.g. a string to an integer. It also has to wrap up low-level types with higher-level functions like hashing and printing. This is why compilation can help for code that has lots of loops, making lots of calls. 

In order to take advantage of compilation, you often need to specify your datatypes (ints, floats, strings), so that you can remove the need for the flexibility of the interpreter. We saw a bit of this with Cinder. 


