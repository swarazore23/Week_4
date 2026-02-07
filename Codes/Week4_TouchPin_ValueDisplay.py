from machine import Pin, TouchPad

import time

touch_pin = TouchPad(Pin(4))

while True:
    
    tp_value = touch_pin.read()
    
    print(tp_value)
    
    time.sleep(0.3)