from machine import Pin
from time import sleep_ms

led = Pin(26, Pin.OUT)
pir = Pin(17, Pin.IN)

def motion_sensor(pir):
    print("btn pressed", pir.value())
    led.value(1)
    sleep_ms(2000)
    led.value(0)

pir.irq(trigger=Pin.IRQ_RISING, handler=motion_sensor)