"""Do a one-bit calculation with light :)"""

import sys
from select import poll
from utime import sleep
from neopixel import NeoPixel
from machine import ADC, Pin, SPI
from components.digital_pot.mcp41010 import MCP41010

# CHANGE THESE VALUES AS NEEDED (BY EXPERIMENTING)
N_REPEATS: int = 50  # number of repeats for averaging the detector value
BINARY_THRESHOLD: int = 5000  # threshold for binary decision (0 or 1)

poll_obj = poll()
# Register sys.stdin (standard input) for monitoring read events with priority 1
poll_obj.register(sys.stdin, 1)


def get_input(symbol_name: str) -> int | None:
    """Get a single bit input from the user."""
    print(f"Please enter enter a value for {symbol_name} (0 or 1): ")
    while True:
        try:
            # update vector values IFF poll object has anything to say
            if poll_obj.poll(10):
                input_str = sys.stdin.readline().rstrip()
                if input_str not in ('0', '1'):
                    print(f"Please enter either 0 or 1 for {symbol_name}.")
                    continue
                return int(input_str)
            sleep(0.1)
        except KeyboardInterrupt:
            return None

def hardware_setup() -> tuple[NeoPixel, MCP41010, ADC]:
    """Return the hardware setup"""
    # setup the hardware
    nps = NeoPixel(Pin(15), 1, bpp=3)  # 1 pixel, 3 bytes per pixel (RGB)
    cs = Pin(1, Pin.OUT)
    s = SPI(0, sck=Pin(2), mosi=Pin(3), miso=Pin(0))
    m = MCP41010(s, cs) 
    detector = ADC(28)  # ADC pin for the detector
    return nps, m, detector


def do_optical_calculation(x: int, y: int, neo_pixel: NeoPixel, digital_pot: MCP41010, det: ADC) -> int:
    """Perform a one-bit calculation using light."""
    # Set the pixel
    if x == 1:
        neo_pixel[0] = (255, 255, 255)
    else:
        neo_pixel[0] = (0, 0, 0)
    neo_pixel.write()  # send the data to the neopixel
    sleep(0.1)

    # Set the digital potentiometer
    pot_value = 255 if y == 1 else 0
    digital_pot.set(pot_value)
    sleep(0.1)  # small delay to see the change in brightness
    det_value = 0.0
    for repeat_idx in range(N_REPEATS):
        det_value += det.read_u16()  # reading analog pin
        sleep(0.01)
    det_value /= N_REPEATS  # average the readings
    # Determine the result based on the detector value
    if det_value > BINARY_THRESHOLD:
        result = 1
    else:
        result = 0
    return result


    

def main():
    """Main function to perform the one-bit calculation."""
    # get the input values
    x = get_input('x')
    if x is None:
        print("Exiting due to keyboard interrupt.")
        return
    y = get_input('y')
    if y is None:
        print("Exiting due to keyboard interrupt.")
        return
    expected_result = x * y
    print(f"The result of {x} x {y} *should be*: {expected_result}")

    # setup the hardware
    nps, m, detector = hardware_setup()
    
    # get the actual result
    result = do_optical_calculation(x, y, nps, m, detector)
    print(f"The result of {x} x {y} *using optics* is: {result}")

    # cleanup and shut down
    nps[0] = (0, 0, 0)
    nps.write()  # send the data to the neopixel

    print("Finished.")


if __name__ == "__main__":
    main()
