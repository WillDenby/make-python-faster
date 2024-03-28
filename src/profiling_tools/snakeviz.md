# 🐲 Snakeviz

`Snakeviz` is a browser-based graphical viewer for the output of Python’s `cProfile` module.

**Usage Example:**

Install it with: `pip install snakeviz`

First, generate a profile file using `cProfile`:

```python
import cProfile
cProfile.run('example_function()', 'profile_output')
```

Then, visualize it with `Snakeviz`:

```shell
snakeviz profile_output
```

This will open up a browser tab with an interactive visualization of your profiling data.