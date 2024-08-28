# 🔗 IronPython

IronPython is an open-source implementation of Python that runs on the .NET Framework, allowing Python developers to interoperate with .NET languages like C# and VB.NET, and make use of .NET libraries. 

IronPython aims to be a true and full implementation of Python, but by supporting dynamic compilation to .NET bytecode, it potentially offers the performance benefits of the .NET runtime.

You can download it from: [https://ironpython.net](https://ironpython.net)

Running a Python script with IronPython is similar to using the standard Python interpreter, but you use the `ipy` command instead.

```shell
ipy script.py
```

To integrate Python code within a C# application using IronPython, you use the following syntax:

```csharp
var engine = Python.CreateEngine();
var scope = engine.CreateScope();
engine.ExecuteFile("script.py", scope);
```

