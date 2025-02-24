""" Modified from https://github.com/fmilburn3/DigitalPot_MCP41010/blob/master/DigiPot.cpp

MicroPython driver for a MCP41010 digital potentiometer.
Requires an SPI bus and a CS pin.

/*
  DigiPot.cpp - Library for MCP41010 digital potentiometer.
  Created by Frank Milburn, 17 June 2015
  Released into the public domain.
*/

Potentiometer data sheet: https://docs.rs-online.com/e6b5/0900766b81380c8b.pdf

"""

from micropython import const


_CMD_WRITE = const(0x11)  # B00010001 from line 17 of DigiPot.cpp
_MAX_VALUE = const(256)


class MCP41010:
    """Class to control a MCP41010 digital potentiometer."""
    def __init__(self, spi, cs):
        self.spi = spi
        self.cs = cs
        self.spi.init()
        self.val = _MAX_VALUE // 2  # initialize at mid-range
        self.set(self.val)

    def set(self, v: int) -> int:
        self.val = v
        if self.val > _MAX_VALUE:
            self.val = _MAX_VALUE
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


