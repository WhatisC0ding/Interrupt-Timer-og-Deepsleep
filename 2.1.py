from machine import Pin, deepsleep
from time import sleep
import esp32

led = Pin(26, Pin.OUT, value=0)

print("ESP32 active now")

led.value(1)
sleep(5)
led.value(0)

print("ESP32 going to sleep")
deepsleep(10000)