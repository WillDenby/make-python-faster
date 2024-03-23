# ⚙️ Compiling Python

When you run a Python script, the Python interpreter automatically compiles the code into Python bytecode, which is a lower-level, platform-independent representation of your source code. This bytecode is then executed by the Python virtual machine (PVM). The msot widely used Python implementation is CPython (not to be confused with Cython, which we'll cover in the next chapter).

But this interpretation layer adds overhead and can slow down your code, especially if lots of the following are happening: 
- mathmatical operations
- loops
- temporary object creation

Compiling our Python code down into machine code means that the interpretation level can be skipped out entirely. 

Having said this, compiling Python can add complexity, potentially slowing you down from a development perspective. Refer to the earlier section, [When to Optimise](./when_to_optimise.md).

Also, if your code is slow because of other factors, such as lots of I/O, network, disk, database, or external library calls, then compiling might not add much. Also, if you've already used some of the libraries previously discussed (NumPy etc.), then you're already probably tapping into under-the-hood optimisations. 

## Ahead of Time (AOT) vs Just in Time (JIT)

There are two approaches to compilation: AOT vs JIT.

An AOT method like Cython compiles your code down to a static set of files, which will only run on your machine (or equivalent). It's a "once and done" approach, that you can then re-use over and over again, without suffering from "cold starts". However, the end result isn't portable, and if you change your code, you'll have to perform a recompilation step before you can use it again. 

A JIT approach is typically easier and requires less manual effort. The computer handles the compilation step, which occurs before the actual running of the code. This means you can rapidly iterate your code and make changes, without having to specify a manual recompilation. However, if you have some code that is frequently spun up, you might start suffering from a "cold start" problem, incurring a time penalty (the "just in time" compilation step) whenever the code is run.

## Thinking in Types

Why is Python "slow"? One reason is that it's dynamically-typed and interpreted. The virtual machine incurs overhead, because it has to be prepared for the datatypes to potentially change. It also has to wrap up low-level types with higher-level functions like hashing and printing. This is why compilation can help for code that has lots of loops making lots of calls. 

In order to take advantage of compilation, you need to be more careful with specifying your datatypes (ints, floats, strings), so that you can remove the need for the flexibility of the interpreter. 

