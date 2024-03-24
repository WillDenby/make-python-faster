# ⏲️ Unix's time Command

The Unix `time` command is used to measure the time taken by a program to execute, providing a simple way to time the execution duration of command-line programs and scripts. This is not a Python-specific tool but can be used with Python scripts or any other executable program.

**Usage Example:**

To time a Python script named script.py, you would use the time command like so:

```shell
time python script.py
```

This will output something similar to:

```shell
real    0m0.123s
user    0m0.084s
sys     0m0.036s
```

- `real` indicates the total elapsed time (wall clock).
- `user` shows the total time spent in user mode.
- `sys` represents the total time spent in kernel mode.

Using the time command is beneficial for getting a quick overview of the time taken by an entire program or script, including any Python scripts you might be running.