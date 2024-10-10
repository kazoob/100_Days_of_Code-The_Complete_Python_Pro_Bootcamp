from art import logo, vs
from game_data import data
import random


def new_pick(data_set, opponent):
    """Returns a new pick from the data_set. If an opponent is provided, it will make sure to not return a duplicate."""
    # Set pick to provided opponent to start while loop.
    pick = opponent
    # Keep choosing a new pick until different from opponent.
    while pick == opponent:
        pick = random.choice(data_set)
    return pick


def print_game_over(score):
    """Print game over screen."""
    print("\n" * 20)
    print(logo)
    print(f"Game over. Final score: {score}\n")


def print_new_round(pick_a, pick_b, score):
    """Prints a new round."""
    print("\n" * 20)
    print(logo)

    # If not the first round, print "Correct"
    if score > 0:
        print(f"Correct!!\n")

    print(f"Current score: {score}\n")
    print(f"Compare A: {pick_a['name']}, a {pick_a['description']}, from {pick_a['country']}")
    print(vs)
    print(f"Against B: {pick_b['name']}, a {pick_b['description']}, from {pick_b['country']}\n")


def check_answer(choice, pick_a_count, pick_b_count):
    """Checks the user answer against the follower counts, returns True or False."""
    if choice == "A" and pick_a_count > pick_b_count:
        return True
    elif choice == "B" and pick_b_count > pick_a_count:
        return True
    else:
        return False


def game():
    """The game!"""
    # This will be pick A in the first round.
    pick_b = new_pick(data, None)

    score = 0
    game_over = False

    while not game_over:
        pick_a = pick_b
        pick_b = new_pick(data, pick_a)

        # Get follower counts.
        pick_a_follower_count = int(pick_a['follower_count'])
        pick_b_follower_count = int(pick_b['follower_count'])

        # Print a new round.
        print_new_round(pick_a, pick_b, score)

        # Get input from user.
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        # Check the user answer.
        # If correct, increase score.
        # If incorrect, end game.
        if check_answer(choice, pick_a_follower_count, pick_b_follower_count):
            score += 1
        else:
            game_over = True
            print_game_over(score)


play_again = "Y"
while play_again.startswith("Y"):
    game()
    # Ask the user if they want to play again.
    play_again = input("Do you want to play again? Type 'Y' or 'N': ").upper()
