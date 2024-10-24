# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
# 
# logo = ''' 
#  _                                             
# | |                                            
# | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
# | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
# | | | | (_| | | | | (_| | | | | | | (_| | | | |
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                     __/ |                      
#                    |___/    '''
# 
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Colorful Hangman Logo
logo = f"""{Fore.YELLOW}
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/    
"""

# Colorful Hangman Stages
stages = [f"""{Fore.RED}
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
""", f"""{Fore.YELLOW}
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""", f"""{Fore.GREEN}
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""", f"""{Fore.CYAN}
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""", f"""{Fore.MAGENTA}
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""", f"""{Fore.BLUE}
  +---+
  |   |
  O   |
      |
      |
      |
=========
""", f"""{Fore.WHITE}
  +---+
  |   |
      |
      |
      |
      |
=========
"""]

def display_logo():
    print(logo)

def display_stage(stage_index):
    print(stages[stage_index])

# Call the functions to display the logo and a specific stage
# display_logo()
# display_stage(0)  # Display the first stage
