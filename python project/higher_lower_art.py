# logo = """
#     __  ___       __
#    / / / (_)___ _/ /_  ___  _____
#   / /_/ / / __ `/ __ \/ _ \/ ___/
#  / __  / / /_/ / / / /  __/ /
# /_/ ///_/\__, /_/ /_/\___/_/
#    / /  /____/_      _____  _____
#   / /   / __ \ | /| / / _ \/ ___/
#  / /___/ /_/ / |/ |/ /  __/ /
# /_____/\____/|__/|__/\___/_/
# """
#
# vs = """
#  _    __
# | |  / /____
# | | / / ___/
# | |/ (__  )
# |___/____(_)
# """


from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Corrected and aligned logo with color for "Lower"
logo = (
    f"{Fore.CYAN}    __  ___       __             \n"
    f"{Fore.CYAN}   / / / (_)___ _/ /_  ___  _____ \n"
    f"{Fore.CYAN}  / /_/ / / __ `/ __ \\/ _ \\/ ___/ \n"
    f"{Fore.CYAN} / __  / / /_/ / / / /  __/ /     \n"
    f"{Fore.CYAN}/_/ /_/_/\\__, /_/ /_/\\___/_/      \n"
    f"{Fore.YELLOW}   / /  /____/_      _____  _____  \n"
    f"{Fore.YELLOW}  / /   / __ \\ | /| / / _ \\/ ___/  \n"
    f"{Fore.YELLOW} / /___/ /_/ / |/ |/ /  __/ /      \n"
    f"{Fore.YELLOW}/_____ /\\____/|__/|__/\\___/_/       \n"
)

vs = (
    f"{Fore.MAGENTA} _    __    \n"
    f"{Fore.MAGENTA}| |  / /____\n"
    f"{Fore.MAGENTA}| | / / ___/\n"
    f"{Fore.MAGENTA}| |/ (__  ) \n"
    f"{Fore.MAGENTA}|___/____(_)\n"
)

def display_colored_logo():
    print(logo)
   
def display_colored_logo2():

    print(vs)
# Call the function to display the logo and vs
# display_colored_logo()
