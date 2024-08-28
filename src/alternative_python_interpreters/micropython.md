# 🤖 MicroPython

MicroPython is a lean and efficient implementation of Python, designed to run on microcontrollers and in constrained environments. Its goal is to be as compatible with standard Python as possible given the hardware limitations, making Python programming accessible for embedded systems development. 

MicroPython is compact, running in as little as 256KB of code space and 16KB of RAM; includes libraries to access low-level hardware, such as digital and analog I/O, SPI, I2C, and more; and offers a Python command line (REPL) on the device for interactive development and debugging.

Find download instructions here: [https://micropython.org](https://micropython.org). A simple MicroPython script to blink an LED might look like this:

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


[Get PDF/ePub](https://makepythonfaster.gumroad.com/l/get)
