# Make sure you install the Kasa Smart Home Python library
# pip3 install pyHS100

from pyHS100 import Discover
from pyHS100 import SmartBulb
from pyHS100 import PowerState, LightState

# Discover all TP-Link smart bulbs on the network
bulbs = Discover.discover()

if len(bulbs) == 0:
    print("No TP-Link smart bulbs found on the network.")
else:
    # Connect to the first bulb found
    bulb = bulbs[0]
    bulb_device = SmartBulb(bulb.host)

    # Turn on the light
    bulb_device.turn_on()

    # Set the brightness to 50%
    bulb_device.set_brightness(50)

    # Set the color temperature to 2700K (warm white)
    bulb_device.set_color_temp(2700)

    # Set the power state to "soft" (fade in and out gradually)
    bulb_device.set_power_state(PowerState.SOFT)

    # Set the bulb's HSB values to red with 50% brightness
    bulb_device.set_hsb(0, 100, 50)

    # Turn off the light with a 1-second transition
    bulb_device.toggle(transition=1000)

    # Set the bulb's color temperature to 3500K
    bulb_device.set_color_temp_kelvin(3500)

    # Get the bulb's firmware version
    firmware_version = bulb_device.hw_info['sw_ver']
    print(firmware_version)

    # Set the power state to "off" immediately
    bulb_device.set_power_state(PowerState.OFF)

    # Get the current light state
    light_state = bulb_device.get_light_state()

    # Print the current light state
    print(light_state)
