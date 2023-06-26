<!-- ABOUT THE PROJECT -->
## About The Project
This is a simple set of scripts that allow you to turn an ESP32-S3 running Circuit Python into an HID that you can then control via get requests on the application's exposed local webserver. This can be useful when an application is blocking mouse input from pyautogui or PyDirectInput.

<!-- GETTING STARTED -->
## Getting Started

You will need an ESP32 or other controller running CircuitPython, any controller that has wifi and can run Circuit Python should be fine. 
[Link below to the one I like.](https://www.adafruit.com/product/5691)

A settings.toml
[Review the "Simple Test" example](https://docs.circuitpython.org/projects/httpserver/en/latest/examples.html)

[Appropriate Circuity Python Libraries](https://circuitpython.org/libraries), [Adafruit_CircuitPython_HID](https://github.com/adafruit/Adafruit_CircuitPython_HID)

## Routes

/, API Reference

/leftclick

/rightclick

/move

/drag