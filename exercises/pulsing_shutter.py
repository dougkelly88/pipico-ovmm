from machine import Pin
from utime import sleep

shutter_external = Pin(16, machine.Pin.OUT)
while True:
    try:
        shutter_external.toggle()
        sleep(1)  
    except KeyboardInterrupt:
        break
    sleep(0.1)
Pin.off()
print("Finished.")