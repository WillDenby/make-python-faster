# 🏎️ PyPy

PyPy stands out as the most popular alternative Python interpreter, known for its ability to improve the execution speed of applications through Just-In-Time (JIT) compilation. It can also use less memory than CPython, thanks to its more efficient garbage collector, and supports Stackless Python, an enhanced version of Python aimed at concurrency and micro-threads. PyPy offers versions of Python 2.7, 3.9, and 3.10 (at time of writing), and supports most of the Python standard library and many third-party modules.

PyPy is best suited for long-running applications where the overhead of JIT compilation can be amortised over time. It's beneficial for applications with heavy numerical computations or extensive use of loops (but you may not need it if using NumPy!). However, if you are frequently running short scripts, the upfront compilation overhead can outweigh the execution gains. 

You can download it from [https://www.pypy.org/](https://www.pypy.org/), and run Python scripts with it by using the `pypy` command instead of `python`:

```shell
pypy script.py
```


[Get PDF/ePub](https://makepythonfaster.gumroad.com/l/get)
