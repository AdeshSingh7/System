#!/usr/bin/env python3
import json
import os

RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
RESET = "\033[0m"
LINE = f"{YELLOW}**********************************************{RESET}"
count = 1
file_location = "passwords.json"

try:
    with open(file_location) as file:
        data = json.load(file)
        keys = data.keys()
        print(LINE)
        for key in keys:
            print(f"{BLUE}{count}. {list(keys)[count-1].capitalize()}{RESET}")
            count += 1
        print(LINE)
        selected_key = input(f"{BLUE}[*] Please enter the number of the key you want to display data for: {RESET}")
        selected_key = int(selected_key)
        if selected_key > 0 and selected_key <= len(keys):
            key = list(keys)[selected_key-1]
            os.system("clear")
            print(f"{LINE}\n{YELLOW}[+] Data for: {key.capitalize()}{RESET}\n{LINE}")
            for key, value in data[key].items():
                print(f"{YELLOW}Username: {GREEN}{key}{RESET}")
                print(f"{YELLOW}Password: {GREEN}{value}{RESET}\n{LINE}")
        else:print(f"\n{RED}[!] Selected key not found in data{RESET}\n")
except Exception as er:print(f"\n{RED}[!] {er}{RESET}\n")
except KeyboardInterrupt:pass
finally:pass
