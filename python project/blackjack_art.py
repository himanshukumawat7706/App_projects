# logo = """
# .------.            _     _            _    _            _
# |A_  _ |.          | |   | |          | |  (_)          | |
# |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
# | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
# |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
# `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
#       |  \/ K|                            _/ |
#       `------'                           |__/
# """
#
#


from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

blackjack_logo = f"""
{Fore.RED}.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( {Fore.YELLOW}\\/{Fore.RED} ).-----.     | |__ | | __ _  {Fore.GREEN}___{Fore.RED}| | ___  __ _  {Fore.GREEN}___{Fore.RED}| | __
| {Fore.YELLOW}\\  /{Fore.RED}|K /\\  |     | '_ \\| |/ _` |{Fore.GREEN}/ __{Fore.RED}| |/ / |/ _` |{Fore.GREEN}/ __{Fore.RED}| |/ /
|  {Fore.YELLOW}\\/ {Fore.RED}| /  \\ |     | |_) | | (_| |{Fore.GREEN} (__{Fore.RED}|   <| | (_| |{Fore.GREEN} (__{Fore.RED}|   < 
`-----| {Fore.YELLOW}\\  /{Fore.RED} |     |_.__/|_|\\__,_|{Fore.GREEN}\\___{Fore.RED}|_|\\_\\_|\\__,_|{Fore.GREEN}\\___{Fore.RED}|_|\\_\\
      |  {Fore.YELLOW}\\/{Fore.RED} K|                            _/ |                
      `------'                           |__/           
"""

def display_blackjack_logo():
    print(blackjack_logo)
#logo = display_blackjack_logo()
# Call the function to display the logo
#display_blackjack_logo()
