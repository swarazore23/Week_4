from machine import Pin, TouchPad
import time
#Initialization
tp = TouchPad(Pin(4))
LED = Pin(12, Pin.OUT)
while True:
    touch_value = tp.read()
    if touch_value < 100 :
        LED.on()
        time.sleep(0.2)
        LED.off()
        print("touched")
    print(touch_value)
    time.sleep(0.2)
    