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

>See: [https://pypi.python.org/pypi/rpi_backlight](https://pypi.python.org/pypi/rpi_backlight).
>Note: You probably need to reboot afterwards, don't know for sure though.

3. Add a (dummy) Dimmer to Domoticz. Use the following settings:


| Field         | Value                                          |
| ------------- | ---------------------------------------------- |
| Hardware:     | Your dummy hardware                            |
| Device name:  | Backlight, or whatever you wish it to be named |
| Switch type:  | Dimmer                                         |
| Type:         | AC                                             |
| ID:           | Doesn't matter, as long as it is unique        |
| Unit code:    | Doesn't matter                                 |
| As:           | Main Device                                    |

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
After the installation, there are a few settings you'll have to change inside the script (for now). Maybe at a later moment I'll use a config file.
1. Change the Domoticz URL
```python
self.domoticz_url = 'http://your.ip.address.here:8080/json.htm'
```
2. Change the Dimmer IDX
```python
self.domoticz_bl_dimmer_idx = '999'
```
3. Save the file and exit your editor

## Running the script
To run the script, use the following command:
```
python /path/to/the/script/backlight_listener.py &
```

If you get a Permission Denied error, try the following
```
chmod +x /path/to/the/script/backlight_listener.py
```

## Adding the Backlight dimmer to Dashticz
Again, this is pretty straight forward, since you are using a Domoticz dimmer. 

1. Open CONFIG.js
2. Add the following code:

```javascript
columns[1] = {}
columns[1]['blocks'] = [999];
columns[1]['width'] = 6;
```

Change the number of the column, change the IDX of your device, change the width to match your needs...