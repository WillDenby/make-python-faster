# 🔗 IronPython

IronPython is an open-source implementation of Python that runs on the .NET Framework and Mono. It is designed to seamlessly integrate with .NET, allowing Python developers to make use of .NET libraries and frameworks. IronPython aims to be a true implementation of Python, while also providing the additional performance and integration capabilities of .NET.

**Features:**

- Full integration with the .NET Framework, enabling access to a vast library of .NET functionality.
- Allows Python code to interoperate with .NET languages like C# and VB.NET.
- Supports dynamic compilation to .NET bytecode, potentially offering performance benefits on the .NET runtime.

**When to Use:**

IronPython is ideal for Python developers working in a .NET environment or needing to integrate Python code with .NET applications. It's particularly useful for projects that can benefit from the .NET framework's features, such as Windows-based desktop applications or web services.

**Code Example:**

Download IronPython first: [https://ironpython.net](https://ironpython.net)

Running a Python script with IronPython is similar to using the standard Python interpreter, but you use the `ipy` command instead.

```shell
ipy script.py
```

To integrate Python code within a C# application using IronPython, you can do something like the following:

```csharp
var engine = Python.CreateEngine();
var scope = engine.CreateScope();
engine.ExecuteFile("script.py", scope);
```