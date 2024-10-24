# logo = '''
#                          ___________
#                          \         /
#                           )_______(
#                           |"""""""|_.-._,.---------.,_.-._
#                           |       | | |               | | ''-.
#                           |       |_| |_             _| |_..-'
#                           |_______| '-' `'---------'` '-'
#                           )"""""""(
#                          /_________\\
#                        .-------------.
#                       /_______________\\
# '''
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Corrected logo with proper f-string formatting
logo = (
    f"{Fore.YELLOW}                         ___________\n"
    f"{Fore.YELLOW}                         \\         /\n"
    f"{Fore.YELLOW}                          )_______(\n"
    f"{Fore.CYAN}                          |\"\"\"\"\"\"\"|{Fore.GREEN}_.-._,{Fore.CYAN}---------{Fore.GREEN}.,_.-._\n"
    f"{Fore.CYAN}                          |       |{Fore.WHITE} | |               | | {Fore.GREEN}''-.\n"
    f"{Fore.CYAN}                          |       |{Fore.WHITE}_| |_             _| |_..-'\n"
    f"{Fore.CYAN}                          |_______|{Fore.WHITE} '-' `'---------'` '-'\n"
    f"{Fore.YELLOW}                          )\"\"\"\"\"\"(\n"
    f"{Fore.YELLOW}                         /_________\\\n"
    f"{Fore.YELLOW}                       .-------------.\n"
    f"{Fore.YELLOW}                      /_______________\\\n"
)

def display_colored_logo():
    print(logo)

# Call the function to display the logo
#display_colored_logo()
