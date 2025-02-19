from neopixel import NeoPixel
from machine import Pin
from utime import sleep
N_PIXELS = 1
ON_VALUE = 255
nps = NeoPixel(Pin(4), N_PIXELS, bpp=3)
# start off @ 50% brightness in red channel
nps[0] = (128, 0, 0)
print("LED starts flashing...")
idx = 0
while True:
    try:
        if idx % 2 == 0:
            for pixel_idx in range(N_PIXELS):
                nps[pixel_idx] = (ON_VALUE, 0, 0)
        else:
            for pixel_idx in range(N_PIXELS):
                nps[pixel_idx] = (0, 0, 0)
        nps.write()
        sleep(1)
    except KeyboardInterrupt:
        break
    idx = idx + 1

for pixel_idx in range(N_PIXELS):
    nps[pixel_idx] = (0, 0, 0)
nps.write()
print("Finished.")
