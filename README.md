
# July 2024 work experience tutorials

On [Project AOC](https://www.microsoft.com/en-us/research/project/aim/) we are exploring using an analog-optical computer as alternative hardware to GPUs to accelerate machine learning inference and solving difficult optimisation problems. 


A key part of this machine is the *optical vector-matrix multiplier* (OVMM): here, we will use a Raspberry Pi Pico microcontroller and some simple, cheap electronics to build an example OVMM machine - in this case, a 1-element vector multiplied by a 1x1 matrix 🙂

## Getting started
Raspberry Pi Pico doesn't play well with Codespaces 😭 so:
* Get Python 3.11 from [here](https://apps.microsoft.com/detail/9nrwmjp3717k?hl=en-us&gl=GB)
* Download and install Git from [here](https://git-scm.com/download/win)
* Download and install VSCode from [here](https://code.visualstudio.com/Download)
* Open VS Code
* Clone the repo from the remote on [Github](https://github.com/dougkelly88/pipico-ovmm):
    
    * In the github browser window, hit the green "Code" button
    * Copy the URL
    * In VS Code, hit `Ctrl+Shift+P` and start typing `Git: Clone`
    * Paste the URL in the box that pops up and hit enter
    * Choose a location on your computer to save the repo
    
* VS Code should show a "recommended extensions" popup: you should install these. If it doesn't, go to the extensions tab on the left of the VS Code screen and search for "MicroPico"

## Hardware shopping list

Some of these parts come with pre-soldered headers, some don't. If you don't have a bunch of 2.54 mm headers and a soldering station, it's worth shopping around for pre-soldered alternatives. 

| Part | Link | Comment |
| --- | --- | --- |
| Solderless breadboard | https://thepihut.com/products/breadboard-for-pico | All the bits for the project should fit on this form factor, but a larger board gives more space to work with. Version with markup for pico makes pin placement easier without constantly looking at the pin diagram, but isn't essential. |
| Fixed length jumper wires | | |
| M-F jumper wires | | |
| M-M jumper wires | | Can use fixed length wires instead, which *most of the time* will result in a tidier build, but these are handy for debugging/first pass. |
| Raspberry Pi Pico | https://proto-pic.co.uk/product/raspberry-pi-pico-one-tiny-fast-microcontroller | |
| Breadboard-compatible Neopixel | https://proto-pic.co.uk/product/breadboard-friendly-rgb-smart-neopixel-pack-of-4 | These are nice to use in this project, but could equally drive other Neopixel form factors: these [8 pixel sticks](https://thepihut.com/products/adafruit-neopixel-stick-8-x-5050-rgbw-leds-natural-white-4500k) are pretty neat, and a way to extend the project. | 
| Light sensor | https://thepihut.com/products/photo-transistor-light-sensor | |
| Digital potentiometer | https://proto-pic.co.uk/product/sparkfun-com-10613-digital-potentiometer-10k | Versions with more channels/more bit depth available |

## Work experience exercises
TODO: these are currently in a ppt, at some point I'll migrate to md and link from here. 

## Disclaimer
There are hazards associated with any electronics project, and any light source. If you don't understand the risks, don't build it. If you're building this without my explicit supervision, I take no reponsibility etc etc. 