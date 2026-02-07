from machine import Pin
import time

pb = Pin(32, Pin.IN, Pin.PULL_UP)
LED = Pin(22, Pin.OUT)

while True:
    
    PushButton_value = pb.value()
    
    if PushButton_value == 0:
    
        LED.on()
        print("button pressed")
        
    else:
        
        LED.off()
        
    time.sleep(0.3)