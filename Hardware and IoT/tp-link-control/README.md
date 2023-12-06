# TP-Link Smart Bulb Control Script

This is a Python script for controlling TP-Link smart bulbs using the `pyHS100` library. The script allows you to turn on/off the light, set its brightness and color temperature, set the power state to fade in/out gradually, set the bulb's HSB values, toggle the light on/off with a transition, set the color temperature in Kelvin, get the device's firmware version, and get the current light state.

## Getting Started

### Prerequisites

To use this script, you'll need to install the `pyHS100` library:

```
pip3 install pyHS100
```

### Usage

1. Clone or download the repository to your local machine.
2. Open the terminal and navigate to the directory where the script is located.
3. Run the script with the following command:

   ```
   python3 tp-link-bulb-control.py
   ```

The script will discover all TP-Link smart bulbs on the network and connect to the first one found. If there are no bulbs found, the script will print a message saying so.

### Features

Here's a list of the features that the script currently supports:

- Turn on/off the light
- Set the brightness to a percentage value (0-100%)
- Set the color temperature in Kelvin (2000K-6500K)
- Set the power state to fade in/out gradually
- Set the bulb's HSB values (hue, saturation, brightness)
- Toggle the light on/off with a transition
- Set the color temperature in Kelvin
- Get the device's firmware version
- Get the current light state

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script uses the `pyHS100` library by GadgetReactor.
