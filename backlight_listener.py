"""
Author:         Anton van der Kolk
Version:        0.1

Simple trick to change the backlight level of the official rpi touchscreen
from domoticz. Because I wanted to change the display brightness from Dashticz

Note: this script must be run from the device with the official RPI Touch Screen

Preparation/Installation:
    1. Install the rpi_backlight module with pip:
        pip install rpi_backlight
    2. Add permissions by changing the rules.d
        see https://pypi.python.org/pypi/rpi_backlight
    3. Add a dummy dimmer to Domoticz
        a. Add a Switch manually (Manual Switch)
        b. Use the following values:
            Hardware:     Your dummy hardware
            Device name:  Backlight, or whatever you wish it to be named
            Switch type:  Dimmer
            Type:         AC
            ID:           Doesn't matter, as long as it is unique
            Unit code:    Doesn't matter
            As:           Main Device
    4. Get the device IDX (Setup -> Devices)
    5. Change the variables below
    5. Make this script executable
        chmod +x backlight_listener.py

"""

import requests
import time
import rpi_backlight as bl

class Backlight(object):
    def __init__(self):
        # change these values to match your settings:
        self.domoticz_bl_dimmer_idx = '344'
        self.domoticz_url = 'http://192.168.178.18:8080/json.htm'
        
        self.backlight_level_domoticz = None
        self.backlight_level_device = None
        
        while(True):
            self.get_backlight_level_domoticz()
            self.get_rpi_backlight()
            time.sleep(1)

    def get_backlight_level_domoticz(self):
        """
        This method gets the level from Domoticz.
        """

        parameters = dict(
            type='devices',
            rid=self.domoticz_bl_dimmer_idx
        )
        
        try:
            resp = requests.get(url=self.domoticz_url, params=parameters)
            data = resp.json()
        except requests.exceptions.RequestException as error:
            # e = sys.exc_info()[0]
            print error
            data = None

        if data is None:
            return

        level = data["result"][0]["Level"]
        
        # now transform it to a value the backlight can work with
        max_value = bl.get_max_brightness()
        self.backlight_level_domoticz = int(round((level * max_value) / 100, 0))

        return


    def get_rpi_backlight(self):
        """
        Method to get the current backlight level from the device
        """
        self.backlight_level_device = bl.get_actual_brightness()
        return


    def evaluate_backlight(self):
        """
        This method evaluates if the backlight of the device has to be changed
        """
        if self.backlight_level_device != self.backlight_level_domoticz:
            # there is a difference between the backlight level and the level
            # in domoticz, let's change the backlight
            bl.set_brightness(self.backlight_level_domoticz)
        return

Backlight()