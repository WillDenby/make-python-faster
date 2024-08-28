# ⏲️ Unix's time Command

The Unix `time` command is used to measure the time taken by a program to execute. This is not a Python-specific tool, so you may find it useful elsewhere too.

## Usage Example

To time a Python script named `script.py`, you would use the time command like so:

```shell
time python script.py
```

This will output something like:

```shell
real    0m0.123s
user    0m0.084s
sys     0m0.036s
```

- `real` indicates the total elapsed time (wall clock).
- `user` shows the total time spent in user mode.
- `sys` represents the total time spent in kernel mode.