from art import logo, vs
from game_data import data
import random


def new_pick(data_set, opponent):
    pick = opponent
    while pick == opponent:
        pick = random.choice(data_set)
    return pick


def print_game_over(score):
    print("\n" * 20)
    print(logo)
    print(f"Game over. Final score: {score}\n")


def print_new_round(pick_a, pick_b, score):
    print("\n" * 20)
    print(logo)

    if score > 0:
        print(f"Correct!!\n")

    print(f"Current score: {score}\n")
    print(f"Compare A: {pick_a['name']}, a {pick_a['description']}, from {pick_a['country']}")
    print(vs)
    print(f"Compare B: {pick_b['name']}, a {pick_b['description']}, from {pick_b['country']}\n")


def game():
    pick_a = new_pick(data, None)
    pick_b = new_pick(data, pick_a)

    score = 0
    game_over = False

    while not game_over:
        pick_a_follower_count = int(pick_a['follower_count'])
        pick_b_follower_count = int(pick_b['follower_count'])

        print_new_round(pick_a, pick_b, score)

        choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        if (choice == "A" and pick_a_follower_count > pick_b_follower_count) or (choice == "B" and pick_b_follower_count > pick_a_follower_count):
            score += 1
            pick_a = pick_b
            pick_b = new_pick(data, pick_a)
        else:
            game_over = True
            print_game_over(score)


play_again = "Y"
while play_again.startswith("Y"):
    game()
    play_again = input("Do you want to play again? Type 'Y' or 'N': ").upper()
