# 🌌 GraalPy

GraalPy is part of the GraalVM ecosystem, designed to execute Python code by leveraging GraalVM's Just-In-Time (JIT) compiler, or compile your code ahead of time (AOT) to a smaller “Native Image” executable. It also enables interoperability with other languages supported by GraalVM, such as JavaScript and Ruby, enabling polyglot applications.

To run a Python script using GraalPy, you can use the `graalpy` command as a drop-in replacement:

```shell
graalpy script.py
```

For polyglot applications, you can access Python code from Java like this:

```java
Context context = Context.newBuilder().allowAllAccess(true).build();
context.eval("python", "print('Hello from GraalPython')");
```



[Get PDF](https://makepythonfaster.gumroad.com/l/get)
