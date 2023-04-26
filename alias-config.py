#!/usr/bin/python3
import os

RED = "\33[1;91m"
GREEN = "\33[1;92m"
RESET = "\33[0m"

# Define aliases
aliases = [
    "adesh=\"notify-send --urgency=low 'Welcome Back' 'Mr. Adesh Singh'\"",
    "banner=\"python3 ~/Python-Projects/System/banner.py\"",
    "panel=\"python3 ~/Python-Projects/ParkPlus/panel-config.py\"",
    "server=\"python3 ~/Python-Projects/ParkPlus/server-config.py\"",
    "clear=\"banner\""
]

# Check if alias is already present in .bashrc file
def is_alias_present(alias):
    with open(os.path.expanduser("~/.bashrc"), "r") as file:
        return any(alias in line for line in file)

# Append aliases to .bashrc file
try:
    with open(os.path.expanduser("~/.bashrc"), "a") as file:
        for alias in aliases:
            if not is_alias_present(alias):
                file.write(f"alias {alias}\n")
    print(f"{GREEN}Aliases added successfully!{RESET}")
except FileNotFoundError:print(f"{RED}Error: The .bashrc file could not be found.{RESET}")
except PermissionError:print(f"{RED}Error: You do not have permission to modify the .bashrc file.{RESET}")
except Exception as e:print(f"{RED}Error: {e}{RESET}")
except KeyboardInterrupt:print(f"{RED}Keyboard Interruption{RESET}")
finally:pass
