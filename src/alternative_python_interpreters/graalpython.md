# 🌌 GraalPython

GraalPython is part of the GraalVM ecosystem, offering a high-performance Python 3 interpreter. It's designed to execute Python code efficiently by leveraging the GraalVM's advanced JIT compiler. GraalPython aims to support Python 3.8 language features and a wide range of Python libraries, making it an attractive option for running existing Python code at higher speeds.

**Features:**

- High-performance execution through GraalVM's JIT compilation.
- Compatibility with Python 3.8 features and a broad set of third-party libraries.
- Interoperability with other languages supported by GraalVM, such as JavaScript, Ruby, and R, enabling polyglot applications.

**When to Use:**

GraalPython is a good choice for projects that require high performance and are running in environments where GraalVM can be used. It's also beneficial for applications that need to interoperate with other programming languages supported by GraalVM, making it ideal for complex, multi-language systems.

**Code Example:**

Get started here: [https://github.com/oracle/graalpython](https://github.com/oracle/graalpython)

To run a Python script using GraalPython, you typically use the `graalpython` command provided by GraalVM.

```shell
graalpython script.py
```

For polyglot applications, you can access Python code from Java like this:

```java
Context context = Context.newBuilder().allowAllAccess(true).build();
context.eval("python", "print('Hello from GraalPython')");
```