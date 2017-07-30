# rpi_backlight
Python script to change the official rpi touchscreen backlight via domoticz.

## Prerequisites
This script requires the following:
* The official Raspberry Touch Screen
* A Raspberry Pi
* Probably Raspbian (I haven't tested it with another OS)
* Python (shouldn't be a problam when running Unix)
* Git

## Preperation
Before you get this script working, you'll need to follow these steps
1. Install the python rpi_backlight module with pip
```
pip install rpi_backlight
```
2. Add permissions to the backlight driver by changing rules.d

...[See: https://pypi.python.org/pypi/rpi_backlight](https://pypi.python.org/pypi/rpi_backlight)
...You probably need to reboot afterwards, don't know for sure though.
3. Add a (dummy) Dimmer to Domoticz. Use the following settings:
>Hardware:     Your dummy hardware
>Device name:  Backlight, or whatever you wish it to be named
>Switch type:  Dimmer
>Type:         AC
>ID:           Doesn't matter, as long as it is unique
>Unit code:    Doesn't matter
>As:           Main Device
4. Now get the IDX of the dimmer by going to Setup -> Devices. You'll need this IDX in a later stage

## Installation
Installing this script is pretty straight forward.
1. Go to a directory of your choise. 
```
cd /home/pi/python
```
2. Create a clone to this repository
```
git clone https://github.com/kolkos/rpi_backlight.git
``` 

## Configuration
After the installation, there are a few settings you'll have to change in the script.
