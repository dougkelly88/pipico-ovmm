from machine import Pin
from utime import sleep

pin = Pin("LED", Pin.OUT)

print("LED starts flashing...")
while True:
    try:
        pin.toggle()
        sleep(1)  # sleep 1 sec
    except KeyboardInterrupt:
        break

    # sleep a very short time so that microcontroller
    # doesn't run too fast
    sleep(0.1)
pin.off()
print("Finished.")
