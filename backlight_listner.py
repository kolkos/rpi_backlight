"""
Author:         Anton van der Kolk
Version:        0.1

Simple trick to change the backlight level of the official rpi touchscreen
from domoticz. Because I wanted to change the display brightness from Dashticz

Preparation:
1. Install the rpi_backlight module with pip:
       pip install rpi_backlight
2. Add permissions to 

"""

import requests
import time
import rpi_backlight as bl

class Backlight(object):
    def __init__(self):
        self.backlight_level_domoticz = None
        self.backlight_level_device = None
        while(True):
            self.get_backlight_level_domoticz()
            self.get_rpi_backlight()
            time.sleep(1)

    def get_backlight_level_domoticz(self):
        domoticz_url = 'http://192.168.178.18:8080/json.htm'

        parameters = dict(
            type='devices',
            rid='344'
        )
        
        try:
            resp = requests.get(url=domoticz_url, params=parameters)
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



    def get_rpi_backlight(self):
        # get the actual brightness
        self.backlight_level_device = bl.get_actual_brightness()



    def evaluate_backlight(self):
        
        return

Backlight()
