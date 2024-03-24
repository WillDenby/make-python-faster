# 🕵️‍♂️ Py-Spy

Py-Spy is a sampling profiler for Python programs that can profile running Python processes without modifying them or needing program restarts.

**Usage Example:**

Install it with: `pip install py-spy`

Run it in your terminal:

```shell
py-spy top --pid <pid of your python program>
```

Or to generate a flame graph:

```shell
py-spy record --pid <pid of your python program> --output profile.svg
```