# logo = """
#  ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
# a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
# 8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
# "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
#  `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
#             88             88
#            ""             88
#                           88
#  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
# a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
# 8b         88 88       d8 88       88 8PP""""""" 88
# "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
#  `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
#               88
#               88
# """

from colorama import Fore, Style, init

# Initialize colorama
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Colorful version of the ASCII art
logo = (
    f"{Fore.RED} ,adPPYba, {Fore.YELLOW},adPPYYba,{Fore.RED}  ,adPPYba,{Fore.YELLOW} ,adPPYba,{Fore.RED} ,adPPYYba,{Fore.YELLOW} 8b,dPPYba,\n"
    f"{Fore.RED}a8\"     \"\" {Fore.YELLOW}\"\"     `Y8 {Fore.RED}a8P_____88 {Fore.YELLOW}I8[    \"\" {Fore.RED}\"\"     `Y8 {Fore.YELLOW}88P'   \"Y8\n"
    f"{Fore.RED}8b         {Fore.YELLOW},adPPPPP88 {Fore.RED}8PP\"\"\"\"\"\"\" {Fore.YELLOW}`\"Y8ba,  {Fore.RED},adPPPPP88 {Fore.YELLOW}88\n"
    f"{Fore.RED}\"8a,   ,aa {Fore.YELLOW}88,    ,88 {Fore.RED}\"8b,   ,aa {Fore.YELLOW}aa    ]8I {Fore.RED}88,    ,88 {Fore.YELLOW}88\n"
    f"{Fore.RED} `\"Ybbd8\"' {Fore.YELLOW}`\"8bbdP\"Y8 {Fore.RED}`\"Ybbd8\"' {Fore.YELLOW}`\"YbbdP\"' {Fore.RED}`\"8bbdP\"Y8 {Fore.YELLOW}88\n"
    f"{Fore.CYAN}            88             88\n"
    f"{Fore.CYAN}           \"\"             88\n"
    f"{Fore.CYAN}                          88\n"
    f"{Fore.GREEN} ,adPPYba,{Fore.MAGENTA} 88 8b,dPPYba, {Fore.GREEN} 88,dPPYba, {Fore.MAGENTA} ,adPPYba,{Fore.GREEN} 8b,dPPYba,\n"
    f"{Fore.GREEN}a8\"     \"\"{Fore.MAGENTA} 88 88P'    \"8a{Fore.GREEN} 88P'    \"8a {Fore.MAGENTA}a8P_____88{Fore.GREEN} 88P'   \"Y8\n"
    f"{Fore.GREEN}8b         {Fore.MAGENTA}88 88       d8{Fore.GREEN} 88       88 {Fore.MAGENTA}8PP\"\"\"\"\"\"\"{Fore.GREEN} 88\n"
    f"{Fore.GREEN}\"8a,   ,aa{Fore.MAGENTA} 88 88b,   ,a8\"{Fore.GREEN} 88       88 {Fore.MAGENTA}\"8b,   ,aa{Fore.GREEN} 88\n"
    f"{Fore.GREEN} `\"Ybbd8\"'{Fore.MAGENTA} 88 88`YbbdP\"'{Fore.GREEN}  88       88 {Fore.MAGENTA}`\"Ybbd8\"'{Fore.GREEN} 88\n"
    f"{Fore.MAGENTA}              88\n"
    f"{Fore.MAGENTA}              88\n"
)

def display_colored_logo():
    print(logo)

# Call the function to display the logo
#display_colored_logo()
