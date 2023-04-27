#!/usr/bin/python3
import os
import json

MENU = """+--------------------------------------------------------------------+
|                           MAIN MENU                                |
+--------------------------------------------------------------------+
| 1. Update: Update all installed packages to their latest version.  |
| 2. Upgrade: Upgrade the distribution to the latest version.        |
| 3. Install Linux Tools: Install the following tools.               |
| 4. Install Python3 Modules: Install the following Python3 modules. |
| 5. Install Software: Install the following software on Ubuntu:     |
| 6. Clone Repository: Clone a repository from Github.               |
| 7. Cleaning packages: Clean broken packages.                       |
| 8. Quit: Exit from this code.                                      |
+--------------------------------------------------------------------+"""

SOFTWARE = """+--------------------------------------+
|               SUB MENU               |
+--------------------------------------+
1. Ngrok: A secure tunneling service.  |
2. AnyDesk: A remote desktop software. |
3. VSCode: A source code editor.       |
+--------------------------------------+"""

REPOSITORY = """+----------------------------------------------+
|                  SUB MENU                    |
+----------------------------------------------+
1. Samba Config: Access all files and folders. |
2. Camphish: Access camera.                    |
3. Hound: Get device location.                 |
+----------------------------------------------+"""

# Colors for console output
RESET = "\033[0m"
RED = "\033[1;91m"
GREEN = "\033[1;92m"
YELLOW = "\033[1;93m"
ERROR = f"\n{RED}Invalid option! Please enter a valid option.{RESET}\n"

# Install Linux tools
def install_tools(user, tools):
    print(f"{GREEN}[+] Installing tools: {tools}{RESET}")
    os.system(f"{user} apt update")
    os.system(f"{user} apt install -y {tools}")
    print(f"{GREEN}[✓] Tools installation complete{RESET}")

# Install Python3 modules
def install_modules(user, modules):
    print(f"{GREEN}[+] Installing modules: {modules}{RESET}")
    os.system(f"{user} pip3 install -U {modules}")
    print(f"{GREEN}[✓] Modules installation complete{RESET}")

# Install software package
def install_software(user,software_url):
    print(f"{GREEN}[+] Installing software: {software_url}{RESET}")
    os.system(f"wget {software_url}")
    os.system(f"{user} dpkg -i *.deb")
    os.system(f"rm -frv *.deb")
    os.system(f"unzip *.zip")
    os.system(f"rm -frv *.zip")
    print(f"{GREEN}[✓] Software installation complete{RESET}")

# Clone a repository
def clone_repository(user, repo_url):
    print(f"{GREEN}[+] Cloning repository: {repo_url}{RESET}")
    os.system(f"git clone {repo_url}")
    print(f"{GREEN}[✓] Cloning repository complete{RESET}")

# Upgrade installed packages
def upgrade_packages(user):
    print(f"{GREEN}[+] Upgrading packages{RESET}")
    os.system(f"{user} apt -y update")
    os.system(f"{user} apt -y upgrade")
    print(f"{GREEN}[✓] Packages upgraded{RESET}")

# Clean up unused packages
def clean_packages(user):
    print(f"{GREEN}[+] Cleaning packages{RESET}")
    os.system(f"{user} apt -y autoremove")
    os.system(f"{user} apt -y autoclean")
    print(f"{GREEN}[✓] Packages cleaned{RESET}")

# Update repositories
def update_repositories(user):
    print(f"{GREEN}[+] Updating repositories{RESET}")
    os.system(f"{user} apt -y update")
    print(f"{GREEN}[✓] Repositories updated{RESET}")

# Detect the current user and return the appropriate command prefix
def detect_user():
    system_info = os.uname()
    operating_system = system_info.sysname
    if operating_system == "Linux":
        if "ubuntu" in system_info.version.lower():
            return "sudo"
        elif "termux" in system_info.version.lower():
            return ""
    print(f"{RED}[✓] UNSUPPORTED OPERATING SYSTEM{RESET}")
    return None

if __name__=='__main__':
    status = True
    os.system("clear")
    while status:
        config_file = "~/.config/system-config.json"
        with open(config_file) as f:
            config = json.load(f)
        pushbullet_token = config['tokens']['pushbullet']
        ngrok_parkplus_token = config['tokens']['ngrok']['parkplus']
        ngrok_private_token = config['tokens']['ngrok']['private']
        ubuntu_tools = config['ubuntu']['tools']
        ubuntu_modules = config['ubuntu']['modules']
        termux_tools = config['termux']['tools']
        termux_modules = config['termux']['modules']
        ngrok_url = config['urls']['ngrok']
        anydesk_url = config['urls']['anydesk']
        vscode_url = config['urls']['vscode']
        smb_conf = config['urls']['smb_conf']
        camphish = config['urls']['camphish']
        hound = config['urls']['hound']
        user = detect_user()
        try:
            print(f"{YELLOW}{MENU}{RESET}")
            user_input = int(input(f"{GREEN}Please enter your choice: {RESET}"))
            if user_input == 1:update_repositories(user)
            elif user_input == 2:upgrade_packages(user)
            elif user_input == 3:install_tools(user, ubuntu_tools)
            elif user_input == 4:install_modules(user, ubuntu_modules)
            elif user_input == 5:
                print(f"{YELLOW}{SOFTWARE}{RESET}")
                user_input = int(input(f"{GREEN}Please enter your choice: {RESET}"))
                if user_input == 1:install_software(user, ngrok_url)
                elif user_input == 2:install_software(user, anydesk_url)
                elif user_input == 3:install_software(user, vscode_url)
                else:print(ERROR)
            elif user_input == 6:
                print(f"{YELLOW}{REPOSITORY}{RESET}")
                user_input = int(input(f"{GREEN}Please enter your choice: {RESET}"))
                if user_input == 1:clone_repository(user, smb_conf)
                elif user_input == 2:clone_repository(user, camphish)
                elif user_input == 3:clone_repository(user, hound)
                else:print(ERROR)
            elif user_input == 7:clean_packages(user)
            elif user_input == 8:exit(0)
            else:print(ERROR)
            input(f"{YELLOW}Press enter to countinue.{RESET}")
            os.system("clear")
        except KeyboardInterrupt:
            os.system("clear")
            print(ERROR)
        except Exception as e:
            os.system("clear")
            print(f"\n{RED}Error: {e}{RESET}\n")
        finally:pass
