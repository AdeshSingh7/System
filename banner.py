#!/usr/bin/python3 python3
import os
import time
import pyautogui

RED = "\33[1;91m"
GREEN = "\33[1;92m"
YELLOW = "\33[1;93m"
BLUE = "\33[1;94m"
RESET = "\33[0m"
DARK_RED = "\33[1;7;91m"
RIGHT = "\u2714"

# Get the system's IP addresses.
def get_ip_address():
    ip_addresses = os.popen("hostname -I").read().strip().replace(" ", " | ")
    if ip_addresses:return ip_addresses.upper()
    else:return "___.___.___.___"

# Get the system's MAC addresses.
def get_mac_address():
    mac_addresses = os.popen("ifconfig | grep 'ether' | awk '{print $2}'").read().strip().split()
    if len(mac_addresses) > 1:return mac_addresses
    else:return [mac_addresses[0],"___.___.___.___"]

# Print main banner.
def banner(terminal_size=86):
    print(f"{DARK_RED} ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛  {RESET}".center(terminal_size))
    print(f"{DARK_RED}   █████╗ ██████╗ ███████╗███████╗██╗  ██╗    ███████╗██╗███╗   ██╗ ██████╗ ██╗  ██╗  {RESET}".center(terminal_size))
    print(f"{DARK_RED}  ██╔══██╗██╔══██╗██╔════╝██╔════╝██║  ██║    ██╔════╝██║████╗  ██║██╔════╝ ██║  ██║  {RESET}".center(terminal_size))
    print(f"{DARK_RED}  ███████║██║  ██║█████╗  ███████╗███████║    ███████╗██║██╔██╗ ██║██║  ███╗███████║  {RESET}".center(terminal_size))
    print(f"{DARK_RED}  ██╔══██║██║  ██║██╔══╝  ╚════██║██╔══██║    ╚════██║██║██║╚██╗██║██║   ██║██╔══██║  {RESET}".center(terminal_size))
    print(f"{DARK_RED}  ██║  ██║██████╔╝███████╗███████║██║  ██║    ███████║██║██║ ╚████║╚██████╔╝██║  ██║  {RESET}".center(terminal_size))
    print(f"{DARK_RED}  ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝  {RESET}".center(terminal_size))
    print(f"{DARK_RED} ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾  https://github.com/AdeshSingh7 ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾  {RESET}".center(terminal_size))

# Print system information.
def system_info(terminal_size=86):
    vendor_name = os.popen("sudo dmidecode -s bios-vendor").read().strip()
    os_name = os.popen("uname -n -o").read().strip()
    serial_number = os.popen("sudo dmidecode -s system-serial-number").read().strip()
    uptime = os.popen("uptime -p").read().strip()
    lan_mac = get_mac_address()[1].upper()
    wlan_mac = get_mac_address()[2].upper()
    ip_address = get_ip_address()
    print(f"".center(terminal_size,"❄"))
    print(f"{RED}{RIGHT} Operating System {BLUE}⟶  {GREEN} {vendor_name}-{os_name}{RESET}")
    print(f"{RED}{RIGHT} Serial Number    {BLUE}⟶  {GREEN} {serial_number}{RESET}")
    print(f"{RED}{RIGHT} System Uptime    {BLUE}⟶  {GREEN} {uptime}{RESET}")
    print(f"{RED}{RIGHT} LAN MAC Address  {BLUE}⟶  {GREEN} {lan_mac}{RESET}")
    print(f"{RED}{RIGHT} WLAN MAC Address {BLUE}⟶  {GREEN} {wlan_mac}{RESET}")
    print(f"{RED}{RIGHT} LAN IP Address   {BLUE}⟶  {GREEN} {ip_address}{RESET}")
    print(f"".center(terminal_size,"❄"))

if __name__=='__main__':
    try:
        pyautogui.hotkey("win", "up")
        time.sleep(.2)
        os.system("clear")
        terminal_size = os.get_terminal_size()[0]
        banner(terminal_size)
        system_info(terminal_size)
    except Exception as err:print(f"{RED}[!]{YELLOW}{err}{RESET}")
    except KeyboardInterrupt:pass
    finally:pass
