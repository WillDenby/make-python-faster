# 🏃 Leaving Interpretation

Moving away from interpretation involves exploring alternative approaches to executing Python code, transcending the traditional interpreter-based execution model. The interpretation layer adds overhead and can slow down your code, especially if lots of the following are happening: 
- mathmatical operations
- loops
- temporary object creation

We've already seen how PyPy can help. But in this section, we'll be more explicit. This involves delving into the integration of C within Python environments and the compilation of Python code using other Ahead-Of-Time (AOT) and Just-In-Time (JIT) compilation methods. These techniques aim to enhance performance, efficiency, and the potential for Python applications by leveraging the strengths of compiled languages and dynamic compilation strategies.

Having said this, compiling Python can add complexity, potentially slowing you down from a development perspective. Refer to the earlier section, [When to Optimise](./when_to_optimise.md). Also, if your code is slow because of other factors, such as lots of I/O, network, disk, database, or external library calls, then compiling might not add much. Also, if you've already used some of the libraries previously discussed (NumPy etc.), then you're already probably tapping into under-the-hood optimisations. 

## Thinking in Types

Why is Python "slow"? One reason is that it's dynamically-typed and interpreted. The virtual machine incurs overhead, because it has to be prepared for the datatypes to potentially change. It also has to wrap up low-level types with higher-level functions like hashing and printing. This is why compilation can help for code that has lots of loops making lots of calls. 

In order to take advantage of compilation, you need to be more careful with specifying your datatypes (ints, floats, strings), so that you can remove the need for the flexibility of the interpreter. 