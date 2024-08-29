# 🐲 Snakeviz

Snakeviz is a browser-based GUI for visualising the output of Python’s cProfile module.

## Usage Example

Install Snakeviz with: `pip install snakeviz`

First, you’ll need to generate a profile file using `cProfile`:

```python
import cProfile
cProfile.run('example_function()', 'profile_output')
```

Then, you can visualise the performance with Snakeviz:

```shell
snakeviz profile_output
```

This will open a browser tab with an interactive visualisation. 



[Get PDF](https://makepythonfaster.gumroad.com/l/get)
