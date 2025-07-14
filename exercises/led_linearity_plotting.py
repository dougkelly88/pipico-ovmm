"""Get the data from the LED linearity exercise running on the Pico and plot it. 

Do this really dumb way for now by copying the data from the terminal to the clipboard and pasting it here."""

from tkinter import Tk
from pathlib import Path
import matplotlib.pyplot as plt


input("Copy the data from the terminal, then press Enter to continue...")
a = Tk()
a.withdraw()
data= a.clipboard_get()
print(data)


# parse the data
lines = data.strip().split('\n')
led_values = []
detector_values = []
for line in lines:
    if line.strip():  # skip empty lines
        led_value, detector_value = map(float, line.split(','))
        led_values.append(led_value)
        detector_values.append(detector_value)

# now plot the data
fig, ax = plt.subplots(1, 1, figsize=(10, 5))
ax.plot(led_values, detector_values, marker='o', linestyle='-', color='g')
ax.set_title('LED Linearity')
ax.set_xlabel('LED Value (0-255)')
ax.set_ylabel('Detector Value')
ax.set_xlim(0, 255)
ax.set_ylim(0, max(detector_values) * 1.1)  # add some padding to the y-axis
plt.show()

# ...and save the data to a file
print("Saving data to 'led_linearity_data.txt' in the 'data' directory.")
path = Path("data")
path.mkdir(exist_ok=True)
output_file = path.joinpath("led_linearity_data.txt")
with open(output_file, 'w', encoding="utf-8") as f:
    for led_value, detector_value in zip(led_values, detector_values):
        f.write(f"{led_value}, {detector_value:.3f}\n")
a.destroy()
