from machine import ADC, Pin, SPI
from neopixel import NeoPixel
from utime import sleep


from components.digital_pot.mcp41010 import MCP41010

a = ADC(0)
cs = Pin(1, Pin.OUT)
s = SPI(0, sck=Pin(2), mosi=Pin(3), miso=Pin(0))
m = MCP41010(s, cs) 

potval: int = 0
potval = m.set(potval)

# setup hardware
detector = ADC(28)

N_PIXELS = 1
TEST_PIXEL_VALUE = 255
N_REPEATS = 50
LC_MAX_VALUE = 255  # maximum value for the LC shutter
INCREMENT = 4  # increment value for the LC shutter

nps = NeoPixel(Pin(15), N_PIXELS, bpp=3)

nps[0] = (TEST_PIXEL_VALUE, TEST_PIXEL_VALUE, TEST_PIXEL_VALUE)  # set pixel to green with test_value brightness
nps.write()  # send the data to the neopixel

lc_values = [x for x in range(LC_MAX_VALUE + 1)] 

for lc_value in lc_values[::INCREMENT]:
    try:
        sleep(0.01)
        potval = m.set(lc_value)
        sleep(0.01)  # small delay to see the change in brightness    
        det_value = 0.0
        for repeat_idx in range(N_REPEATS):
            det_value += detector.read_u16()  # reading analog pin
            sleep(0.01)
        det_value /= N_REPEATS  # average the readings
        # print(f"led value = {pixel_value}, detector value = {det_value:.3f}")  # printing the ADC value
        print(f"{lc_value}, {det_value:.3f}")  # printing the ADC value
    except KeyboardInterrupt:
        break
nps[0] = (0, 0, 0)  # turn off the pixel
m.set(255)  # set the potentiometer to min voltage before exiting
nps.write()  # send the data to the neopixel

print("Finished.")
