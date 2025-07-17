
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

Some of these parts come with pre-soldered headers, some don't. If you don't have a bunch of 2.54 mm headers and a soldering station, it's worth shopping around for pre-soldered alternatives. Alternatively: I've not tried these [press-fit headers](https://thepihut.com/products/2-54mm-0-1-pitch-press-fit-male-pin-header) myself but they look like they might work, subject to all the warnings in the product description. 

| Part | Link | Price/pack (July '25) | Units/Pack | Units/Build | Cost/Build (July 25) | Notes |
|------|------|----------------------|------------|-------------|------------|-------|
| Pi pico 2 *with pre-soldered headers* | https://www.digikey.co.uk/en/products/detail/raspberry-pi/SC1632/26241102 | £4.41 | 1 | 1 | £4.41 |  |
| Neopixel RGB LED | https://www.digikey.co.uk/en/products/detail/adafruit-industries-llc/1312/6565388 | £5.84 | 4 | 1 | £1.46 | [1] |
| 8-bit 10k digital potentiometer | https://www.digikey.co.uk/en/products/detail/microchip-technology/MCP41010-E-P/593689 | £1.63 | 1 | 1 | £1.63 |  |
| Solderless breadboard | https://www.digikey.co.uk/en/products/detail/dfrobot/FIT0096/7597069 | £2.08 | 1 | 1 | £2.08 | [2] |
| M-M jumper wire "dupont-style" | https://www.digikey.co.uk/en/products/detail/adafruit-industries-llc/1957/6827090 | £1.43 | 20 | 10 | £0.715 |  |
| M-F jumper wire "dupont-style" | https://www.digikey.co.uk/en/products/detail/adafruit-industries-llc/1954/6827087 | £1.43 | 20 | 4 | £0.286 |  |
| 4k7 resistor (through-hole) | https://www.digikey.co.uk/en/products/detail/stackpole-electronics-inc/CF12JT4K70/1741152 | £0.07 | 1 | 1 | £0.07 |  |
| LC shutter | https://thepihut.com/products/small-liquid-crystal-light-valve-controllable-shutter-glass | £2.80 | 1 | 1 | £2.80 |  |
| Phototransistor | https://thepihut.com/products/photo-transistor-light-sensor | £1.00 | 1 | 1 | £1.00 |  |
| Preformed jumper wire kit | https://thepihut.com/products/jumper-wire-kit-140-piece | £4.00 | 10 | 2 | £0.80 |  |
| Breakaway 2.54 mm header pins | https://thepihut.com/products/break-away-0-1-36-pin-strip-male-header-black-10-pack | £3.50 | 360 | 10 | £0.097 |  |
| | | | | | | |
| **Project cost/build (July '25)** | | | | | **£15.35** |  |

[1] I can't source these anywhere pre-soldered 🫤 I've not tried them myself but these push fit headers might be a reasonable solder-free alternative: https://thepihut.com/products/2-54mm-0-1-pitch-press-fit-male-pin-header

[2] All the bits for the project should fit on this form factor, but a larger board gives more space to work with. [A version with markup for pico](https://thepihut.com/products/breadboard-for-pico) makes pin placement easier without constantly looking at the pin diagram, but isn't essential.

Optomechanical bits not included here: four each of M3x18 mm hex socket cap bolts + M3 nuts, and 3D printed parts (see optomech\july_2025_build_stls). Worst case, just use blu tack 🙂

## Work experience exercises
TODO: these are currently in a ppt, at some point I'll migrate to md and link from here. 

## Disclaimer
There are hazards associated with any electronics project, and any light source. If you don't understand the risks, don't build it. If you're building this without my explicit supervision, I take no reponsibility etc etc. 

## A tip to handle dependencies inside the project
e.g. to access hardware modules that sit in `.\components` from a script that lives in `.\exercises`
* Delete `.mypy_cache` folder from the project root - it'll come back again, so don't worry.
* Or: depend on changes to `settings.json` to ensure that stuff like `.mypy_cache` doesn't get pushed to the microcontroller. 
* Right click any file in the project in Explorer view and select "Upload project to Pico"
* Should get confirmation of successful upload in lower right of VSCode window
* Sometimes needs restart of VS Code to get this to work 🤷‍♂️
* Note that [Thonny](https://thonny.org/) is a useful tool to browse what's actually on the Pico and to do any clearing up of old project files.