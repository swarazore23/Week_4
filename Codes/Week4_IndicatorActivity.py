from machine import Pin
import time

pb1 = Pin(5, Pin.IN, Pin.PULL_UP)
pb2 = Pin(21, Pin.IN, Pin.PULL_UP)
red = Pin(14, Pin.OUT)
yellow = Pin(32, Pin.OUT)
blue = Pin(33, Pin.OUT)
green = Pin(25, Pin.OUT)

while True:
    
    con = pb1.value()
    print(con)
    if con == 0:
        green.on()
        time.sleep(0.2)
        red.on()
        time.sleep(0.2)
        yellow.on()
        time.sleep(0.2)
        blue.on()
        time.sleep(0.2)
    else :
        green.off()
        red.off()
        yellow.off()
        blue.off()
        
        
        lol = pb2.value()
    print(lol)
    if lol == 0:
        blue.on()
        time.sleep(0.2)
        yellow.on()
        time.sleep(0.2)
        red.on()
        time.sleep(0.2)
        green.on()
        time.sleep(0.2)
    else :
        blue.off()
        yellow.off()
        red.off()
        green.off()
        
    
    
        
        
        