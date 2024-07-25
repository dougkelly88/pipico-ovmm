"""Control the opacity of a LC shutter device by sweeping
 the voltage across its pins with a digital pot"""

import sys
from select import poll
from utime import sleep
from machine import Pin, ADC, SPI

from components.digital_pot.mcp4131 import MCP4131

poll_obj = poll()
# Register sys.stdin (standard input) for monitoring read events with priority 1
poll_obj.register(sys.stdin, 1)


def parse_validate_string_to_int(input_str: str) -> int:
    """Convert a string to int, doing validation"""
    try:
        digital_pot_int = int(input_str.strip())
    # if the conversion fails, return 0
    except ValueError:
        print("Input should be an integer: returning 0")
        return 0
    # check if the values are in the correct range
    if digital_pot_int < 0 or digital_pot_int > 127:
        print("For a seven-bit digital pot range 0-127: return 0 instead...")
        return 0
    return digital_pot_int


def main():

    # configure digital pot control
    cs = Pin(17, Pin.OUT)
    spi = SPI(0, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
    digital_pot = MCP4131(spi, cs)

    print("Please enter a value for the digital pot wiper (0-127):")
    while True:
        try:
            # update digital pot value IFF poll object has anything to say
            if poll_obj.poll(20):
                input_str = sys.stdin.readline().rstrip()
                pot_value = parse_validate_string_to_int(input_str)
                digital_pot.set(pot_value)

                print("Please enter a value for the digital pot wiper (0-127):")

            sleep(0.1)
        except KeyboardInterrupt:
            break

    # Set digital pot value to zero before finishing
    # This is VITAL if the LC is being driven DC, rather
    # than via an oscillator circuit: otherwise you'll burn 
    # out the LC shutter
    digital_pot.set(0)
    
    print("Finished.")


if __name__ == "__main__":
    main()