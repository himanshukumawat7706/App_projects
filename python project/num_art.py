# logo = """
#   / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
#  / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
# / /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
# \____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
# """
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Colorful version of the ASCII art logo
logo = (
    f"{Fore.CYAN}  / _ \\_   _  ___  ___ ___  /__   \\ |__   ___    {Fore.YELLOW}/\\ \\ \\_   _ _ __ ___ | |__   ___ _ __ \n"
    f"{Fore.CYAN} / /_\\/ | | |/ _ \\/ __/ __|   / /\\/ '_ \\ / _ \\  {Fore.YELLOW}/  \\/ / | | | '_ ` _ \\| '_ \\ / _ \\ '__|\n"
    f"{Fore.CYAN}/ /_\\\\| |_| |  __/\\__ \\__ \\  / /  | | | |  __/  {Fore.YELLOW}/ /\\  /| |_| | | | | | |_) |  __/ |   \n"
    f"{Fore.CYAN}\\____/ \\__,_|\\___||___/___/   \\/   |_| |_|\\___|{Fore.YELLOW} \\_\\/  \\__,_|_| |_| |_|_.__/ \\___|_|   \n"
)

def display_colored_logo():
    print(logo)

# Call the function to display the logo
# display_colored_logo()
