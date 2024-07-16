from machine import ADC
from time import sleep

detector = ADC(28)

while True:
    try:
        det_value = detector.read_u16()  # reading analog pin
        print(f"detector value = {det_value:.3f}")  # printing the ADC value
        sleep(0.5)
    except KeyboardInterrupt:
        break

print("Finished.")
