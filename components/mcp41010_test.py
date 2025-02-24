"""Test code to control the digital potentiometer, which in turn controls the opacity of the LC shutter, goes here."""
from machine import Pin, ADC, SPI

from components.digital_pot.mcp41010 import MCP41010
import time

a = ADC(0)
cs = Pin(17, Pin.OUT)
s = SPI(0, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
m = MCP41010(s, cs)

potval: int = 0
potval = m.set(potval)
direction: int = 1
try: 
    while True:
        time.sleep(0.1)
        v = a.read_u16()
        print("Target value: %d" % potval)
        # print("[ %5.3f %5.3f %5.3f ]" % (0.0, 3.3 * v / 65536, 3.3))
        potval = potval + direction
        potval = m.set(potval)
        if potval == 128:
            direction = -1
        if potval == 0:
            direction = 1
except KeyboardInterrupt:
    # set the potentiometer to zero before exiting
    m.set(0)
    print("Finished.")
finally:
    # set the potentiometer to zero before exiting in case of some non-KeyboardInterrupt exception
    m.set(0)
