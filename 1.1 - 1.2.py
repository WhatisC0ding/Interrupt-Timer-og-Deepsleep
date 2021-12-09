from machine import Pin
from time import sleep_ms

led = Pin(26, Pin.OUT)
button = Pin(27, Pin.IN, value=0)

def button_press(button):
    print("button pressed")
    led.value(1)
    sleep_ms(2000)
    led.value(0)
    sleep_ms(2000)

button.irq(trigger=Pin.IRQ_RISING, handler=button_press)