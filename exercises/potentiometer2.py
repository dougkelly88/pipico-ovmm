from machine import Pin, ADC, SPI
import mcp4131
import time
a = ADC(0)
cs = Pin(17, Pin.OUT)
s = SPI(0, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
m = mcp4131.MCP4131(s, cs)


def pot_set(val):
    if val < 0: val = 0
    if val > 255: val = 255
    cs.value(0)
    s.write(bytes([0x11, val]))
    cs.value(1)

while True:
    time.sleep(.1)
    v = a.read_u16()
    print("[ %5.3f %5.3f %5.3f ]" % (0.0, 3.3*v/65536, 3.3))

    for i in range (0,256,5):
        pot_set(i)
        time.sleep(0.05)
    for i in range (255, -1, 5):
        pot_set(i)
        time.sleep(0.05)
voltage = (adc.read_u16() / 65535) * 3.3
print(f"voltage: {voltage:.2f} V")
