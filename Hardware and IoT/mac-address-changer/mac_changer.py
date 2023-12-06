import subprocess
import random
import time
import winreg
import logging
import wifi
import tkinter as tk
import netifaces
import requests
import schedule
import argparse

log_file = "mac_changer.log"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--show-mac", help="display the current MAC address without making any changes", action="store_true")
    args = parser.parse_args()

    # Get a list of available network adapters and their MAC addresses
    mac_addresses = get_mac_addresses()

    # Display the list of available network adapters and their MAC addresses
    print("Available network adapters:")
    for index, item in enumerate(mac_addresses):
        print(f"{index}) {item[0]} - {item[1]}")

    if args.show_mac:
        # Display the current MAC address without making any changes
        mac_address = get_current_mac_address()
        print(f"Current MAC address: {mac_address}")
    else:
        # Prompt the user to select a network adapter to change the MAC address for
        option = input("Enter the number of the network adapter you want to change the MAC address for: ")

        # Get the MAC addresses that can be changed for the selected network adapter
        mac_addresses_to_change_to = get_available_mac_addresses(mac_addresses[int(option)][1])

        # Display the available MAC addresses that can be used to change the selected network adapter's MAC address
        print("Available MAC addresses:")
        for index, item in enumerate(mac_addresses_to_change_to):
            print(f"{index}) {item}")

        # Prompt the user to select a new MAC address
        update_option = input("Enter the number of the MAC address you want to change to: ")

        # Change the MAC address of the selected network adapter
        old_mac_address = mac_addresses[int(option)][0]
        new_mac_address = mac_addresses_to_change_to[int(update_option)]
        change_mac_address(mac_addresses[int(option)][1], new_mac_address)

        # Log the old and new MAC addresses
        logging.info(f"Changing MAC address from {old_mac_address} to {new_mac_address}")

def get_mac_addresses():
    mac_addresses = []

    # Get a list of available network adapters and their MAC addresses
    output = subprocess.check_output(["ipconfig", "/all"]).decode()
    for block in output.split("\n\n"):
        if "Physical Address" in block:
            transport_name_find = re.search(r"^[^\r\n]*", block)
            transport_name = transport_name_find.group(0).rstrip(":")
            mac_address_find = re.search(r"(([0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2})", block)
            mac_address = mac_address_find.group(0).replace("-", ":")
            mac_addresses.append((mac_address, transport_name))

    return mac_addresses

def get_current_mac_address():
    # Get the current MAC address of the first network adapter
    mac_address = None
    output = subprocess.check_output(["getmac"]).decode().split("\n")
    if len(output) > 2:
        mac_address = output[2].strip().replace("-", ":")
    
    return mac_address

def get_available_mac_addresses(transport_name):
    # Get the available MAC addresses that can be used to change the MAC address of the specified network adapter
    key_path = f"SYSTEM\\CurrentControlSet\\Control\\Class\\{{4d36e972-e325-11ce-bfc1-08002be10318}}\\{transport_name}\\"
    try:
        regkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS)
        old_mac_address = winreg.QueryValueEx(regkey, "NetworkAddress")[0]
        new_mac_addresses = []
        for i in range(10):
            random_mac_address = ':'.join(['{:02x}'.format(random.randint(0x00, 0xff)) for _ in range(6)])
            if random_mac_address != old_mac_address:
                new_mac_addresses.append(random_mac_address)
        winreg.SetValueEx(regkey, "NetworkAddress", 0, winreg.REG_SZ, old_mac_address)
        return new_mac_addresses
    except Exception as e:
        logging.error(str(e))
        return []

def change_mac_address(transport_name, new_mac_address):
    # Disable and enable the specified network adapter
    try:
        # Disable the network adapter
        disable = subprocess.run(["wmic", "path", "win32_networkadapter", "where", f"name= '{transport_name}'", "call", "disable"], capture_output=True)
        if disable.returncode == 0:
            logging.info(f"Disabled {transport_name}")
        else:
            logging.error(f"Failed to disable {transport_name}: {disable.stderr.decode()}")

        # Change the MAC address of the network adapter
        key_path = f"SYSTEM\\CurrentControlSet\\Control\\Class\\{{4d36e972-e325-11ce-bfc1-08002be10318}}\\{transport_name}\\"
        regkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(regkey, "NetworkAddress", 0, winreg.REG_SZ, new_mac_address)
        winreg.CloseKey(regkey)

        # Enable the network adapter
        enable = subprocess.run(["wmic", "path", "win32_networkadapter", "where", f"name='{transport_name}'", "call", "enable"], capture_output=True)
        if enable.returncode == 0:
            logging.info(f"Enabled {transport_name}")
        else:
            logging.error(f"Failed to enable {transport_name}: {enable.stderr.decode()}")
    except Exception as e:
        logging.error(str(e))

def generate_mac_address():
    # Generate a random MAC address
    return ':'.join(['{:02x}'.format(random.randint(0x00, 0xff)) for _ in range(6)])

def revert_mac_address(transport_name, old_mac_address):
    # Revert back to the original MAC address
    try:
        key_path = f"SYSTEM\\CurrentControlSet\\Control\\Class\\{{4d36e972-e325-11ce-bfc1-08002be10318}}\\{transport_name}\\"
        regkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(regkey, "NetworkAddress", 0, winreg.REG_SZ, old_mac_address)
        winreg.CloseKey(regkey)
        logging.info(f"Reverted MAC address for {transport_name} back to {old_mac_address}")
    except Exception as e:
        logging.error(str(e))

def gui():
    # Create a simple GUI using Tkinter
    root = tk.Tk()
    root.title("MAC Changer")

    # Add labels and buttons to the GUI
    label = tk.Label(root, text="Select the network adapter you want to change:")
    label.pack()

    mac_addresses = get_mac_addresses()
    for index, item in enumerate(mac_addresses):
        button = tk.Button(root, text=f"{item[0]} - {item[1]}", command=lambda index=index: select_network_adapter(index))
        button.pack()

    def select_network_adapter(index):
        root.destroy()
        network_adapter_gui(mac_addresses[index][1])

    root.mainloop()

def network_adapter_gui(transport_name):
    # Create a simple GUI for choosing a new MAC address
    root = tk.Tk()
    root.title(f"Change MAC address of {transport_name}")

    # Add labels and buttons to the GUI
    label = tk.Label(root, text="Select a new MAC address:")
    label.pack()

    new_mac_addresses = get_available_mac_addresses(transport_name)
    for index, item in enumerate(new_mac_addresses):
        button = tk.Button(root, text=item, command=lambda index=index: change_mac_address_gui(transport_name, new_mac_addresses[index]))
        button.pack()

    root.mainloop()

def change_mac_address_gui(transport_name, new_mac_address):
    # Confirm the new MAC address with the user
    root = tk.Tk()
    root.title(f"Confirm MAC address change for {transport_name}")

    label = tk.Label(root, text=f"The new MAC address for {transport_name} will be set to:\n{new_mac_address}\n\nAre you sure?")
    label.pack()

    confirm_button = tk.Button(root, text="Yes", command=lambda: change_mac_address(transport_name, new_mac_address))
    confirm_button.pack(side=tk.LEFT)

    cancel_button = tk.Button(root, text="No", command=root.destroy)
    cancel_button.pack(side=tk.RIGHT)

    root.mainloop()

def scan_wifi_networks():
    # Scan for available Wi-Fi networks
    wifi_scanner = wifi.WiFi()
    networks = wifi_scanner.scan()

    # Display a list of available Wi-Fi networks
    print("Available Wi-Fi networks:")
    for network in networks:
        print(f"{network.ssid} ({network.signal})")

    # Prompt the user to select a Wi-Fi network
    selected_network = input("Enter the name of the Wi-Fi network you want to connect to: ")

    # Connect to the selected Wi-Fi network
    wifi_scanner.connect(selected_network)

    # Check if the connection was successful
    if wifi_scanner.isconnected():
        # Display the IP address of the connected Wi-Fi network
        ip_address = wifi_scanner.get_ip_address()
        print(f"Connected to {selected_network} ({ip_address})")
    else:
        print("Failed to connect to the selected Wi-Fi network")

def generate_vendor_specific_mac_address():
    # Get the list of registered OUIs from IEEE's website
    url = "https://www.ieee.org/content/dam/ieee-org/ieee/web/org/ops/oui/oui.txt"
    response = requests.get(url)

    # Parse the response to extract the OUIs
    ouis = []
    for line in response.iter_lines():
        if "(hex)" in line.decode():
            ouis.append(line.decode().split("(hex)")[0].strip())

    # Generate a random MAC address with a vendor-specific OUI
    random_oui = ouis[random.randint(0, len(ouis)-1)]
    random_mac = f"{random_oui}:{':'.join(['{:02x}'.format(random.randint(0x00, 0xff)) for _ in range(3)])}"

    # Prompt the user to confirm the new MAC address
    new_mac_address = random_mac
    input(f"Your new MAC address will be {new_mac_address}. Press Enter to continue or Ctrl+C to cancel")

    # Change the MAC address of the first available network adapter
    mac_addresses = get_mac_addresses()
    if len(mac_addresses) > 0:
        old_mac_address = mac_addresses[0][0]
        change_mac_address(mac_addresses[0][1], new_mac_address)
        logging.info(f"Changing MAC address from {old_mac_address} to {new_mac_address}")

if __name__ == "__main__":
    # Schedule the script to run every day at 3:00 AM
    schedule.every().day.at("03:00").do(generate_vendor_specific_mac_address)

    while True:
        # Run the scheduled jobs
        schedule.run_pending()

        # Run the GUI if the user wants to change the MAC address using a GUI
        gui()
