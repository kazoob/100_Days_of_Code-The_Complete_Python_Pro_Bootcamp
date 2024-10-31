import random
from art import logo

# Colors for console text.
class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

LOW_RANGE = 1
HIGH_RANGE = 100

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!\n")
    print(f"I'm thinking of a number between {LOW_RANGE} and {HIGH_RANGE}.\n")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    print("")

    attempts_left = 0
    game_over = False
    answer = random.randint(LOW_RANGE, HIGH_RANGE)

    if difficulty.startswith('e'):
        attempts_left = EASY_ATTEMPTS
    else:
        attempts_left = HARD_ATTEMPTS

    while attempts_left > 0 and not game_over:
        print(f"You have {bcolors.BLUE}{attempts_left}{bcolors.ENDC} attempts remaining to guess the number.\n")
        guess = int(input("Make a guess: "))
        print("")

        if guess == answer:
            print(f"You got it! 😀 The answer was {answer}.\n")
            game_over = True
        else:
            if guess < answer:
                print(f"{bcolors.GREEN}Too low.{bcolors.ENDC} 👇\n")
                attempts_left -= 1
            else:
                print(f"{bcolors.YELLOW}Too high.{bcolors.ENDC} 👆\n")
                attempts_left -= 1

            if attempts_left > 0:
                print("Guess again.\n")
            else:
                print(f"{bcolors.RED}You have run out of guesses, you lose 😢.{bcolors.ENDC}\n")
                game_over = True

play_again = "yes"
while play_again.startswith("y"):
    game()
    play_again = input("Would you like to play again? Type 'yes' or 'no': ").lower()
