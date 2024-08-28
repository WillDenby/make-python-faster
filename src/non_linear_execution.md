# 😵‍💫 Non-Linear Execution

A strictly sequential, or linear, flow of execution in Python (or any programming language) can have several drawbacks in terms of code speed, as the complexity and scale of the tasks increase. Here are the key issues:

**Single-core utilisation**: Modern computers can have multiple cores, which allow them to perform several operations in parallel. But sequential code occupies one core at a time, leaving other cores idle and underutilised. 

**I/O bound processes**: In a strictly sequential execution, the program waits for I/O operations (like reading from a file or network requests) to complete before proceeding to the next step. This reduces CPU utilisation efficiency. 

**Inefficient handling of large data sets**: Similarly, when scaling up to operate on large data sets, sequential processing can become time-consuming because each item is processed one after the other.

As the amount of data or the complexity of the problem increases, the execution time increases linearly (or sometimes even more than linearly). In contrast, parallel or concurrent execution models can scale better by distributing work across available resources.

Why can it be difficult to avoid sequential execution? CPython’s Global Interpreter Lock (GIL), which we’ll explore in the next chapter, helps to ensure your code’s memory safety, at the cost of introducing barriers to parallelism. 