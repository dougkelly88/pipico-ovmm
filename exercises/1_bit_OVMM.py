from machine import Pin, ADC, SPI
from components.digital_pot.mcp4101 import MCP4101
import time
from neopixel import NeoPixel
from machine import Pin
from utime import sleep
from machine import ADC
from time import sleep
import sys
from select import poll

#shutter
a = ADC(0)
cs = Pin(17, Pin.OUT)
s = SPI(0, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
m = MCP4101(s, cs)

#neo
N_PIXELS = 1
ON_VALUE = 255
nps = NeoPixel(Pin(4), N_PIXELS, bpp=3)
nps[0] = (128, 0, 0)

#detector
detector = ADC(28)

poll_obj = poll()
# Register sys.stdin (standard input) for monitoring read events with priority 1
poll_obj.register(sys.stdin, 1)


def main():
    print("Please enter 2 binary 1 digit numbers: ")
    while True:
        try:
            # update vector values IFF poll object has anything to say
            if poll_obj.poll(10):
                print("something arrived in the poll object")
                global input_num1
                input_num1 = sys.stdin.readline().rstrip()
                print(f"digit 1 is: {input_num1}!")
                global input_num2
                input_num2 = sys.stdin.readline().rstrip()
                print(f"digit 2 is: {input_num2}!")
                break
            
            sleep(0.1)
        except KeyboardInterrupt:
            break
    
    print("Finished.")
    input_num1 = int(input_num1)
    input_num2 = int(input_num2)
    if input_num1 == (1):
        nps[0] = (ON_VALUE, 0, 0)
        nps.write()
        print("LED on")
    elif input_num1 == (0): 
        nps[0] = (0, 0, 0)
        nps.write()
        print("LED off")
    quit = False
    while not quit:
        time.sleep(1)
if __name__ == "__main__":
    main()

