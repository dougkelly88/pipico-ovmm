"""The code to control the digital potentiometer, which in turn controls the opacity of the LC shutter, goes here."""

from machine import Pin, ADC, SPI

# import mcp4131
import time
from micropython import const

_CMD_INCREMENT = const(0x04)  # b00000100 - Increment Wiper
_CMD_DECREMENT = const(0x08)  # b00001000 - Decrement Wiper
_CMD_WRITE = const(0x00)  # b00000011 11111111 - Write Data
# can't get read to work
_CMD_READ = const(0x0F)  # b00001111 11111111 - Read  Data


class MCP4131:
    def __init__(self, spi, cs):
        self.spi = spi
        self.cs = cs
        self.spi.init()
        self.val = 64  # initialize at mid-range
        self.set(self.val)

    def set(self, v):
        self.val = v
        if self.val > 128:
            self.val = 128
        if self.val < 0:
            self.val = 0
        self.cs.value(0)
        self.spi.write(bytes([_CMD_WRITE, self.val]))
        self.cs.value(1)
        return self.val

    def get(self):
        return self.val

    def value(self):
        return self.val

    def ratio(self):
        return self.val / 128.0

    def inc(self):
        self.cs.value(0)
        self.spi.write(bytes([_CMD_INCREMENT]))
        self.cs.value(1)
        self.val = self.val + 1
        if self.val > 128:
            self.val = 128
        return self.val

    def dec(self):
        self.cs.value(0)
        self.spi.write(bytes([_CMD_DECREMENT]))
        self.cs.value(1)
        self.val = self.val - 1
        if self.val < 0:
            self.val = 0
        return self.val


a = ADC(0)
cs = Pin(17, Pin.OUT)
s = SPI(0, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
m = MCP4131(s, cs)


potval = m.set(0)
direction = 1
while True:
    time.sleep(0.1)
    v = a.read_u16()
    print("[ %5.3f %5.3f %5.3f ]" % (0.0, 3.3 * v / 65536, 3.3))
    if direction == 1:
        potval = m.inc()
    else:
        potval = m.dec()
    if potval == 128:
        direction = -1
    if potval == 0:
        direction = 1
