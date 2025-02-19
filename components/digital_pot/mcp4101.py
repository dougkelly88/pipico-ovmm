
import time
from micropython import const


_CMD_WRITE = const(0x11)  # b00010001
_CMD_READ = const(0x0F)  # b00001111 11111111 - Read  Data


class MCP4101:
    def __init__(self, spi, cs):
        self.spi = spi
        self.cs = cs
        self.spi.init()
        self.val = 128  # initialize at mid-range
        self.set(self.val)

    def set(self, v):
        self.val = v
        if self.val > 256:
            self.val = 256
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
        return self.val / 256.0

   
   

