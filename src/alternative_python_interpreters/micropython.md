# 🤖 MicroPython

MicroPython is a lean and efficient implementation of Python 3, designed to run on microcontrollers and in constrained environments. Its goal is to be as compatible with standard Python as possible given the hardware limitations, making Python programming accessible for embedded systems development.

**Features:**

- Compact: Requires minimal resources, running in as little as 256KB of code space and 16KB of RAM.
- Peripheral Access: Includes libraries to access low-level hardware, such as digital and analog I/O, SPI, I2C, and more.
- Interactive Prompt: Offers a Python command line (REPL) on the device for interactive development and debugging.

**When to Use:**

MicroPython shines in embedded systems and IoT applications where resources are limited. It's ideal for developers looking to leverage Python's ease of use and readability in hardware projects, from hobbyist level to professional embedded systems.

**Code Example:**

Find download instructions here: [https://micropython.org](https://micropython.org)

A simple MicroPython script to blink an LED might look like this:

```python
from machine import Pin
import time

led = Pin(2, Pin.OUT) # Pin 2 is an LED on many boards

while True:
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
```

This script toggles an LED on and off on a board like the ESP8266 or ESP32, showcasing the simplicity of using Python for hardware programming.