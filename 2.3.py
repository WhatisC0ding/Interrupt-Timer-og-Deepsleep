from machine import Pin, deepsleep
from time import sleep
import esp32

wake_pin1 = Pin(27, Pin.IN, Pin.PULL_UP)
wake_pin2 = Pin(26, Pin.IN, Pin.PULL_UP)
print("hello again, pin 1 value is:",
      wake_pin1.value(), "and pin 2 value is: ",
      wake_pin2.value())
sleep(4)
esp32.wake_on_ext1(pins = (wake_pin1, wake_pin2),
                 level = esp32.WAKEUP_ALL_LOW)
deepsleep(100000)
