from machine import ADC, Pin
from neopixel import NeoPixel
from utime import sleep



# setup hardware
detector = ADC(28)

N_PIXELS = 1
MAX_VALUE = 255
N_REPEATS = 50

nps = NeoPixel(Pin(15), N_PIXELS, bpp=3)

pixel_values = [x for x in range(MAX_VALUE + 1)]  # create a list of pixel values from 0 to MAX_VALUE


for pixel_value in pixel_values[::8]:
    try:
        nps[0] = (0, pixel_value, 0)  # set pixel to green with varying brightness
        sleep(0.01)
        nps.write()  # send the data to the neopixel
        sleep(0.01)  # small delay to see the change in brightness    
        det_value = 0.0
        for repeat_idx in range(N_REPEATS):
            det_value += detector.read_u16()  # reading analog pin
            sleep(0.01)
        det_value /= N_REPEATS  # average the readings
        # print(f"led value = {pixel_value}, detector value = {det_value:.3f}")  # printing the ADC value
        print(f"{pixel_value}, {det_value:.3f}")  # printing the ADC value
    except KeyboardInterrupt:
        break
nps[0] = (0, 0, 0)  # turn off the pixel
nps.write()  # send the data to the neopixel

print("Finished.")
