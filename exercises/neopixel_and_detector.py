from neopixel import NeoPixel
from machine import Pin
from utime import sleep
from machine import ADC
from time import sleep
N_PIXELS = 1
ON_VALUE = 255
nps = NeoPixel(Pin(4), N_PIXELS, bpp=3)
detector = ADC(28)
nps[0] = (128, 0, 0)
print("LED starts flashing...")
idx = 0
while True:
    try:
        if idx % 2 == 0:
            for pixel_idx in range(N_PIXELS):
                nps[pixel_idx] = (ON_VALUE, 0, 0)
                det_value = detector.read_u16()  # reading analog pin
                print(f"detector value = {det_value:.3f}") 
        else:
            for pixel_idx in range(N_PIXELS):
                sleep(0.5)
                nps[pixel_idx] = (0, 0, 0)
                det_value = detector.read_u16()  # reading analog pin
                print(f"detector value = {det_value:.3f}") 
        #det_value = detector.read_u16()  # reading analog pin
        #print(f"detector value = {det_value:.3f}") 
        nps.write()
        sleep(1)
        
    except KeyboardInterrupt:
        break
    idx = idx + 1

for pixel_idx in range(N_PIXELS):
    nps[pixel_idx] = (0, 0, 0)
nps.write()
print("Finished.")





