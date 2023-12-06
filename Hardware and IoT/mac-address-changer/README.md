# MAC Address Changer

This is a Python script that allows users to change their MAC address on Windows machines. The script has several functionalities, including:

- Displaying a list of available network adapters and their current MAC addresses
- Allowing the user to select a network adapter and change its MAC address to a new randomly generated one
- Providing a GUI for users who prefer a visual interface to choose a network adapter and new MAC address
- Scanning for available Wi-Fi networks and connecting to the selected network
- Generating a vendor-specific MAC address daily at 3:00 AM using IEEE's registered OUIs

The script also logs all MAC address changes to a log file.

## Installation

To use this script, you will need to have the following installed on your system:

- Python 3.6 or later
- [Tkinter](https://docs.python.org/3/library/tkinter.html) (should be included with most installations of Python)
- [netifaces](https://pypi.org/project/netifaces/)
- [requests](https://pypi.org/project/requests/)
- [schedule](https://pypi.org/project/schedule/)
- [wifi](https://pypi.org/project/wifi/) (optional, for scanning and connecting to Wi-Fi networks)

## Usage

To run the script, open a command prompt or terminal and navigate to the directory containing the `mac_changer.py` file. Then run the following command:

```
python mac_changer.py
```

This will display a list of available network adapters and their current MAC addresses. You can then follow the prompts to change the MAC address of a specific network adapter, scan for and connect to a Wi-Fi network, or generate a vendor-specific MAC address.

You can also use the following optional command-line argument to display the current MAC address of a specific network adapter without making any changes:

```
python mac_changer.py --show-mac
```

## Contributing

Contributions are welcome! If you find a bug or would like to suggest an improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
