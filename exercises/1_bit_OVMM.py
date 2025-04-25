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
potval = m.set(0)

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

def my_input(prompt):
    print(prompt)
    return_input = sys.stdin.readline().rstrip()
    return return_input
def main():

    # receiving inputs 
    input_num1 = my_input("input the first of 2 binary digits:")
    print(f"digit 1 is: {input_num1}!")
    input_num2 = my_input("input the second of 2 binary digits")
    print(f"digit 2 is: {input_num2}!")
    #casting the string variables from the input to an integer
    input_num1 = int(input_num1)
    input_num2 = int(input_num2)

    #logic to set the LED on if input value 1 is a 1 or off if input value 1 is 0
    if input_num1 == (1):
        nps[0] = (ON_VALUE,ON_VALUE, ON_VALUE)
        nps.write()
        print("LED on")
    elif input_num1 == (0): 
        nps[0] = (0, 0, 0)
        nps.write()
        print("LED off")
    #logic to set the shutter off (make transparent) if input value 2  is a 1 or on (makes the shutter opaque) if input value 2 is 0
    if input_num2 == 1:
        potval = m.set(0)
    elif input_num2 == 0:
        potval = m.set(255)
    #I found the sleep useful as it took a little while for the dc value to be updated so the first value outputted was erroneous
    time.sleep(2)
    det_value = detector.read_u16()  # reading analog pin
    print(f"detector value = {det_value:.3f}")  # printing the ADC value
    if det_value > 2000:
        output = 1
    else: 
        output = 0
    print(f"your result is {output}")
    #This piece of code is used to just continuosly print light detector readings so that the LED can be tested
    # quit = False
    #while not quit:
        #time.sleep(1)
        #det_value = detector.read_u16()  # reading analog pin
        #print(f"detector value = {det_value:.3f}")
    #this piece of code is to ask the use if they would like to quit - if q will break
    _programme_end_ = my_input("type q to quit otherwise type any other letter")
    return _programme_end_
        
if __name__ == "__main__":
    while True:
        x = main()
        if x == "q":
            break

