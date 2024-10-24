# Consolidating all games into one Python file with an interactive UI
from colorama import Fore, Style, init
import colorsys
import random
import hangman_art
import hangman_words
import blackjack_art
from game_data import data

init(autoreset=True)
# HANG MAN GAME IS INTEGRATED
def hangman():
    print(Fore.CYAN + "Starting Hangman...")
    import random

    from hangman_words import word_list
    # from hangman_art import stages, logo
    import hangman_art
    lives = 6
    
    # print(logo)
    hangman_art.display_logo()

    chosen_word = random.choice(word_list)
    print(chosen_word)

    placeholder = ""
    word_length = len(chosen_word)
    for position in range(word_length):
        placeholder += "_"
    print("Word to guess: " + placeholder)

    game_over = False
    correct_letters = []

    while not game_over:

        print(f"****************************{lives}/6 LIVES LEFT****************************")
        guess = input("Guess a letter: ").lower()

        if guess in correct_letters:
            print(f"You've already guessed {guess}")

        display = ""

        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        print("Word to guess: " + display)

        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")

            if lives == 0:
                game_over = True

                print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

        if "_" not in display:
            game_over = True
            print("****************************YOU WIN****************************")

        # print(stages[lives])
        hangman_art.display_stage(lives)


def blackjack():
    import random
    import blackjack_art

    def deal_card():
        """Returns a random card from the deck"""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    def calculate_score(cards):
        """Take a list of cards and return the score calculated from the cards"""
        if sum(cards) == 21 and len(cards) == 2:
            return 0

        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)

    def compare(u_score, c_score):
        """Compares the user score u_score against the computer score c_score."""
        if u_score == c_score:
            return "Draw 🙃"
        elif c_score == 0:
            return "Lose, opponent has Blackjack 😱"
        elif u_score == 0:
            return "Win with a Blackjack 😎"
        elif u_score > 21:
            return "You went over. You lose 😭"
        elif c_score > 21:
            return "Opponent went over. You win 😁"
        elif u_score > c_score:
            return "You win 😃"
        else:
            return "You lose 😤"

    def play_game():
        #print(logo)
        blackjack_art.display_blackjack_logo()
        user_cards = []
        computer_cards = []
        computer_score = -1
        user_score = -1
        is_game_over = False

        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        while not is_game_over:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_game_over = True
            else:
                user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
                if user_should_deal == "y":
                    user_cards.append(deal_card())
                else:
                    is_game_over = True

        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))

    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        print("\n" * 20)
        play_game()


def number_guessing():
    import random
    import num_art

    def game():
        number_to_guess = random.randint(1, 100)
        game_attempts = 0

        # ---------------main section---------------
        game_continue = True
        # print(logo)
        #blackjack_art.display_blackjack_logo()
        num_art.display_colored_logo()

        print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
        # print(f"Pssst, the correct answer is {number_to_guess}")

        choice = input("Choose a difficulty. Type 'easy' or 'hard':").lower()

        def attempts(g_attempts):
            if choice == "hard":
                g_attempts = 5
            else:
                g_attempts = 10
            return g_attempts

        game_attempts = attempts(game_attempts)
        print(f"You have {game_attempts} attempts.")

        while game_continue:
            for i in range(game_attempts):

                user_guess = int(input("Make a guess: "))

                if user_guess == number_to_guess:
                    print("You guessed it right !!")
                    game_continue = False
                    break
                elif user_guess > number_to_guess:
                    print("Too high guess again")
                    game_attempts -= 1
                    print(f"You have {game_attempts} attempts left")
                else:
                    print("Too low guess again")
                    game_attempts -= 1
                    print(f"You have {game_attempts} attempts left")

                if game_attempts == 0:
                    print("You've run out of guesses, you lose.")
                    game_continue = False
                    break
            if not game_continue:
                break

        # if we want to restart game
        if input("DO you want to play again !! Type 'y' or 'no': ") == 'y':
            game()
        else:
            print("Thanks for playing.....")

    game()


def higher_lower():
    import higher_lower_art
    from game_data import data
    import random

    # Generating random number in range of dictionary
    def random_generator():
        num = random.randint(0, len(data) - 1)
        return num

    score = 0

    # Printing the logo "HIGHER LOWER"
    print(higher_lower_art.display_colored_logo())

    # Function for getting random comparison for A
    def compare_a():
        """Participant A"""
        num = random_generator()

        # Retrieve the details of the participant
        name = data[num]["name"]
        followers = data[num]["follower_count"]
        description = data[num]["description"]
        country = data[num]["country"]

        # Print the details of the participant
        print(f"Compare A: {name}, a {description}, from {country}")
        return {
            "name": name,
            "followers": followers,
            "description": description,
            "country": country
        }

    # Function for getting random comparison for B
    def compare_b():
        """Opponent of A"""
        num = random_generator()

        # Retrieve the details of the opponent
        name = data[num]["name"]
        followers = data[num]["follower_count"]
        description = data[num]["description"]
        country = data[num]["country"]

        # Print the details of the opponent
        print(f"Compare B: {name}, a {description}, from {country}")
        return {
            "name": name,
            "followers": followers,
            "description": description,
            "country": country
        }

    # Call the compare A function
    opponentA = compare_a()

    # Print the versus logo
    print(higher_lower_art.display_colored_logo2())

    # Call the compare B function
    againstB = compare_b()

    game_start = True

    # Start the game now
    while game_start:
        if score > 0:
            print("\n" * 20)  # Clear screen for better readability
            print(higher_lower_art.display_colored_logo())
            print(f"Compare A: {opponentA['name']}, a {opponentA['description']}, from {opponentA['country']}")
            print(higher_lower_art.display_colored_logo2())
            againstB = compare_b()

        choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if choice == "a":
            if opponentA["followers"] == againstB["followers"]:
                print("It's a tie!")
            elif opponentA["followers"] > againstB["followers"]:
                score += 1

            else:
                game_start = False
                print(f"You're wrong! Final score: {score}.")

        elif choice == "b":
            if opponentA["followers"] == againstB["followers"]:
                print("It's a tie!")
            elif opponentA["followers"] < againstB["followers"]:
                opponentA = againstB  # Update opponentA to the winner
                score += 1
                print(f"You're right! Current score: {score}.")
            else:
                game_start = False
                print(f"You're wrong! Final score: {score}.")


def rock_paper_scissors():
    import random
    from colorama import Fore, Style, init

    # Initialize colorama
    init(autoreset=True)

    # Colorized Rock, Paper, Scissors ASCII Art

    rock = f'''
    {Fore.YELLOW}        _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
    '''

    paper = f'''
    {Fore.CYAN}        _______
        ---'   ____)____
                  ______)
                  _______)
                 _______)
        ---.__________)
    '''

    scissors = f'''
    {Fore.RED}        _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
    '''

    def display_r():
        print(f"{Fore.YELLOW}Rock:\n{rock}")

    def display_p():

        print(f"{Fore.CYAN}Paper:\n{paper}")

    def display_s():
        print(f"{Fore.RED}Scissors:\n{scissors}")



    # creating user sequence
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    # user input sequence
    if user_choice == 0:
        display_r()
    elif user_choice == 1:
        display_p()
    elif user_choice == 2:
        display_s()
    else:
        print("Wrong input choice")

    # computer game sequence

    print("Computer choose\n\n")
    # creating computer sequence
    computer_choice = random.randint(0, 2)

    rock_paper_scissor = [rock, paper, scissors]
    if computer_choice == user_choice:
        print(rock_paper_scissor[user_choice])
        print("ohh tied match")
    elif computer_choice == 0 and user_choice == 1:
        print(rock)
        print("You won!!")

    elif computer_choice == 1 and user_choice == 2:
        print(paper)
        print("You won!!")
    elif computer_choice == 2 and user_choice == 0:
        print(scissors)
        print("You won!!")
    else:
        print(rock_paper_scissor[computer_choice])
        print("You loose")


def treasure_island():
    from colorama import Fore, Style, init

    # Initialize colorama
    init(autoreset=True)

    # Colorized version of the ASCII art
    treasure_island_map = f'''
    {Fore.YELLOW}    *******************************************************************************
    {Fore.YELLOW}              |                   |                  |                     |
    {Fore.CYAN}     _________|________________.=""_;=.______________|_____________________|_______
    {Fore.YELLOW}    |                   |  ,-"_,=""     `"=.|                  |
    {Fore.CYAN}    |___________________|__"=._o`"-._        `"=.______________|___________________
    {Fore.YELLOW}              |                `"=._o`"=._      _`"=._                     |
    {Fore.CYAN}     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    {Fore.YELLOW}    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    {Fore.CYAN}    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
    {Fore.YELLOW}              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    {Fore.CYAN}     _________|___________| ;`-.o`"=._; ." ` '`." ` . "-._ /_______________|_______
    {Fore.YELLOW}    |                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
    {Fore.CYAN}    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    {Fore.YELLOW}    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    {Fore.CYAN}    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    {Fore.YELLOW}    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    {Fore.CYAN}    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    {Fore.YELLOW}    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    {Fore.CYAN}    /______/______/______/______/______/______/______/______/______/______/_____ /
    {Fore.YELLOW}    *******************************************************************************
    '''

    def display_treasure_island_map():
        print(treasure_island_map)

    # Call the function to display the treasure map
    display_treasure_island_map()

    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    start = input(f"You're at a cross road. Where do you want to go? Type left or right\n").lower()
    if start == 'left':
        # move left
        print("You've come to a lake. There is an island in the middle of the lake."
              )
        # create the move variable  t store the movement

        move = input("Type wait to wait for a boat.\n Type swim to swim across.\n").lower()
        if move == 'wait':
            print("You arrive at the island unharmed.")
            final_move = input("There is a house with 3 doors.One red, one yellow and one blue."
                               " Which colour do you choose?\n").lower()
            if final_move == 'yellow':
                print("congrats you won")
            elif final_move == 'red':
                print("You fell into a volcano")
            elif final_move == 'blue':
                print("You met Kirmada")
        else:
            print("You became a delicious dinner of crocodile")
    else:
        print("You Fell into a hole.", "Game Over")


def blind_auction():
    import bind_art
    bind_art.display_colored_logo()
    def find_highest_bidder(bidding_record):
        highest_bid = 0
        winner = ""
        for bidder in bidding_record:
            bid_amount = bidding_record[bidder]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = bidder
        print(f"The winner is {winner} with a bid of ${highest_bid}")

    bids = {}
    continue_bidding = True
    while continue_bidding:
        name = input("What is your name?: ")
        price = int(input("What is your bid?: $"))
        bids[name] = price
        should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
        if should_continue == "no":
            continue_bidding = False
            find_highest_bidder(bids)
        elif should_continue == "yes":
            print("\n" * 20)


def caesar_cipher():
    from math import trunc

    from caesar_art import logo
    # TODO-1: Import and print the logo from art.py when the program starts.

    print(logo)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    # TODO-2: What happens if the user enters a number/symbol/space?

    def caesar(original_text, shift_amount, encode_or_decode):
        output_text = ""
        if encode_or_decode == "decode":
            shift_amount *= -1
        for letter in original_text:

            if letter in alphabet:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)

                output_text += alphabet[shifted_position]
            else:
                output_text += letter
        print(f"Here is the {encode_or_decode}d result: {output_text}")

    # TODO-3: Can you figure out a way to restart the cipher program?
    begin = True
    while begin:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

        check = input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()
        if check == "no":
            begin = False


# Main Menu
def main_menu():
    while True:
        print(Fore.CYAN + Style.BRIGHT + "\nWelcome to Python Gaming Centre! Select a game to play:")
        print(Fore.YELLOW + "***************************************")
        print(Fore.GREEN + "1. Hangman")
        print(Fore.CYAN + "2. Blackjack")
        print(Fore.YELLOW + "3. Number Guessing")
        print(Fore.MAGENTA + "4. Higher Lower")
        print(Fore.BLUE + "5. Rock, Paper, Scissors")
        print(Fore.RED + "6. Treasure Island")
        print(Fore.WHITE + "7. Blind Auction")
        print(Fore.CYAN + "8. Caesar Cipher")
        print(Fore.RED + Style.BRIGHT + "9. Exit")
        print(Fore.YELLOW + "***************************************")

        choice = input(Fore.CYAN + "Enter the number of the game you want to play: ")

        if choice == "1":
            hangman()
        elif choice == "2":
            blackjack()
        elif choice == "3":
            number_guessing()
        elif choice == "4":
            higher_lower()
        elif choice == "5":
            rock_paper_scissors()
        elif choice == "6":
            treasure_island()
        elif choice == "7":
            blind_auction()
        elif choice == "8":
            caesar_cipher()
        elif choice == "9":
            print(Fore.RED + "Thanks for playing! Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice, please enter a number from 1 to 9.")

        input(Fore.GREEN + "\nPress Enter to return to the main menu...")


# Run the main menu
if __name__ == "__main__":
    main_menu()