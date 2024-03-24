# ☕ Jython

Jython is an implementation of Python designed to run on the Java platform. It compiles Python code to Java bytecode, allowing Python programs to seamlessly integrate with Java modules and libraries. This offers a performance boost in environments where the Java Virtual Machine (JVM) is optimized.

**Features:**

- Runs on the JVM, allowing integration with Java libraries.
- Access to Java's concurrency features and large ecosystem.

**When to Use:**

Jython is a great choice when you need to integrate Python code with Java applications or take advantage of Java's rich ecosystem of libraries.

**Code Example:**

Using Jython typically involves invoking the Jython interpreter to run Python scripts or to integrate Python with Java code.

```shell
jython script.py
```

In Java, you can embed Jython as follows:

```java
PythonInterpreter interpreter = new PythonInterpreter();
interpreter.exec("print('Hello from Jython')");
```