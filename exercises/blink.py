from neopixel import NeoPixel
from machine import Pin
from utime import sleep


        
pin = Pin("LED", Pin.OUT)

# print("LED starts flashing...")
while True:
    try:
        pin.toggle()
        sleep(1)  # sleep 1 sec
    except KeyboardInterrupt:
        break
    sleep(0.1)
pin.off()
print("Finished.")
