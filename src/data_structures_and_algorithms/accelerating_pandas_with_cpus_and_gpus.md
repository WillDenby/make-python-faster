# Accelerating Pandas with CPUs and GPUs

If you've done any data work with Python, you'll probably have come across the Pandas DataFrame. It's built on top of NumPy, and is friendly for datasets up to 10GB or so. Beyond this, you need to have lots of RAM! 

1. Beware of datatypes in Pandas. Numeric columns reference the NumPy data types; strings reference the Python implementation (slower).
2. Avoid repeated `.concat` methods, because this requires building lots of new objects.
3. Filter data before doing compute intensive activities; drop things you don't need. 

## Modin

This is a drop-in replacement for Pandas which scales to use all your cores:

```python
import pandas as pd
import modin.pandas as pd
```

## cuDF 

This enables you to easily augment your code with GPUs (provided they're NVIDIA!). This is `Rapids cuDF pandas Accelerator Mode`. 

If you're using a Jupyter notebook, check out the magic extension: `%load_ext cudf.pandas`. You can get access to an NVIDIA GPU for free on Colab. It attempts to offload whatever it can onto a GPU, falling back to the CPU with minimal cost if it can't.

Check out an example here: [https://colab.research.google.com/drive/1XTKHiIcvyL5nuldx0HSL_dUa8yopzy_Y](https://colab.research.google.com/drive/1XTKHiIcvyL5nuldx0HSL_dUa8yopzy_Y)

## Vaex

This lets you tackle bigger datasets (than your RAM can handle) by using lazy evaluation: [https://github.com/vaexio/vaex](https://github.com/vaexio/vaex)

