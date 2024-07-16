import sys
from select import poll
from utime import sleep
from neopixel import NeoPixel
from machine import Pin

N_PIXELS = 1
ON_VALUE = 255

nps = NeoPixel(Pin(4), N_PIXELS, bpp=3)
# start off @ 50% brightness in red channel
nps[0] = (128, 0, 0)

poll_obj = poll()
# Register sys.stdin (standard input) for monitoring read events with priority 1
poll_obj.register(sys.stdin, 1)


def parse_string_to_rgb(input_str: str) -> tuple[int, ...]:
    """Convert a comma-separated string to a tuple of integers representing RGB values."""
    # split the string into 3 parts, each representing a color channel
    rgb_str_list = input_str.split(",")
    if len(rgb_str_list) != 3:
        raise ValueError("Input string must have 3 parts separated by comma")
    # convert the strings to integers
    try:
        rgb_int_list = [int(color_str.strip()) for color_str in rgb_str_list]
    # if the conversion fails, return (0, 0, 0)
    except ValueError:
        print("Each part must be an integer: return (0, 0, 0) instead...")
        return 0, 0, 0
    # check if the values are in the correct range
    for color in rgb_int_list:
        if color < 0 or color > 255:
            print("Each part must be in the range 0-255: return (0, 0, 0) instead...")
            return 0, 0, 0
    assert len(rgb_int_list) == 3
    return tuple(rgb_int_list)


def main():
    print("Please enter R, G, B values separated by commas (0-255): ")
    while True:
        try:
            # update neopixel values IFF poll object has anything to say
            if poll_obj.poll(20):
                print("something arrived in the poll object")
                input_str = sys.stdin.readline().rstrip()
                rgb_tuple = parse_string_to_rgb(input_str)
                print(f"RGB values: {rgb_tuple}")
                for pixel_idx in range(N_PIXELS):
                    nps[pixel_idx] = rgb_tuple
                nps.write()

                print("Please enter R, G, B values separated by commas (0-255): ")

            sleep(0.1)
        except KeyboardInterrupt:
            break

    # turn off before finishing
    for pixel_idx in range(N_PIXELS):
        nps[pixel_idx] = (0, 0, 0)
    nps.write()
    print("Finished.")


if __name__ == "__main__":
    main()
