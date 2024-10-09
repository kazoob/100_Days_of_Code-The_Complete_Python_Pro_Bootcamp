import random
from art import logo

# Colors for console text.
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# Contents of a new deck of cards
# TODO Expand cards in deck.
deck_new = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(deck):
    """Deal a card from the deck. Does not remove the card from the deck."""
    # TODO Remove dealt card from deck.
    return random.choice(deck)

def score_hand(hand):
    """Returns the best score for the hand. Will count Aces as 1 or 11 as needed."""

    # Count the number of Aces.
    aces = hand.count(11)

    # If the hand exceeds 21 and there are Aces, calculate optimal mix of 1 or 11 Ace values.
    if sum(hand) > 21 and aces > 0:
        # All possible score options <= 21.
        score_options = []

        # Calculate options for each Ace.
        for x in range(1, aces + 1):
            # If Blackjack, return.
            if sum(hand) - x * 10 == 21:
                return 21
            # If hand under 21, include in possible score option.
            elif sum(hand) - x * 10 < 21:
                score_options.append(sum(hand) - x * 10)

        # Check if any possible score options were calculated. If none, return score with all Aces = 1.
        if score_options:
            return max(score_options)
        else:
            return sum(hand) - aces * 10
    # If the hand has no Aces, return score.
    else:
        return sum(hand)


def print_hands(player_hand, dealer_hand, dealer_hidden):
    """Print the player and dealer hands, including score. Option to only display the dealer's first card."""
    print("")
    print(f"Your cards: {bcolors.HEADER}{player_hand}{bcolors.ENDC}, score: {bcolors.OKBLUE}{score_hand(player_hand)}{bcolors.ENDC}")

    # Only display the dealer's first card if requested.
    if dealer_hidden:
        print(f"Dealer's first card: {bcolors.OKBLUE}{dealer_hand[0]}{bcolors.ENDC}")
    else:
        print(f"Dealer's cards: {bcolors.HEADER}{dealer_hand}{bcolors.ENDC}, score: {bcolors.OKBLUE}{score_hand(dealer_hand)}{bcolors.ENDC}")

    print("")


def blackjack():
    """Blackjack!"""

    # Print logo
    print(logo)

    # Make a copy of a new deck.
    deck_current = deck_new.copy()

    # Player and dealer hands start empty.
    player_hand = []
    dealer_hand = []

    # Deal 2 cards to player and dealer.
    for _ in range(2):
        player_hand.append(deal_card(deck_current))
        dealer_hand.append(deal_card(deck_current))

    # While the player has not passed or been forced to pass (Blackjack or bust), proceed with player turn.
    player_pass = False
    while not player_pass:
        print_hands(player_hand, dealer_hand, True)

        # Check for Blackjack, if yes force pass.
        if score_hand(player_hand) == 21:
            print(f"{bcolors.WARNING}** Hand is 21, forcing pass. **{bcolors.ENDC}\n")
            player_pass = True
        else:
            # Get choice from player, new card or pass.
            player_choice = ""
            while not(player_choice.startswith("y") or player_choice.startswith("n")):
                player_choice = input("Type 'y' to get another card, 'n' to pass: ").lower()

            if player_choice.startswith("y"):
                player_hand.append(deal_card(deck_current))
            else:
                player_pass = True

            # If player has bust, force pass.
            if score_hand(player_hand) > 21:
                player_pass = True

    # If the player has bust, game over.
    if score_hand(player_hand) > 21:
        print_hands(player_hand, dealer_hand, False)
        print(f"{bcolors.FAIL}** You went over. You lose. :( **{bcolors.ENDC}\n")
    else:
        # Dealer turn, deal all necessary cards.
        while score_hand(dealer_hand) < 17:
            dealer_hand.append(deal_card(deck_current))

        print_hands(player_hand, dealer_hand, False)

        # Dealer has Blackjack, dealer wins.
        if score_hand(dealer_hand) == 21:
            print(f"{bcolors.FAIL}** Dealer has Blackjack! You lose. :( **{bcolors.ENDC}\n")
        # Player has Blackjack, player wins.
        elif score_hand(player_hand) == 21:
            print(f"{bcolors.OKGREEN}** You have Blackjack! You win! :) **{bcolors.ENDC}\n")
        # Dealer bust, player wins.
        elif score_hand(dealer_hand) > 21:
            print(f"{bcolors.OKGREEN}** Dealer went over. You win! :) **{bcolors.ENDC}\n")
        # Player and dealer tie.
        elif score_hand(player_hand) == score_hand(dealer_hand):
            print(f"{bcolors.WARNING}** It's a draw. **{bcolors.ENDC}\n")
        # Player hand beats dealer, player wins.
        elif score_hand(player_hand) > score_hand(dealer_hand):
            print(f"{bcolors.OKGREEN}** You win! :) **{bcolors.ENDC}\n")
        # Dealer hand beats player, dealer wins.
        else:
            print(f"{bcolors.FAIL}** You lose. :( **{bcolors.ENDC}\n")

    # Ask the player if they want to play again.
    question_play_again = ""
    while not(question_play_again.startswith("y") or question_play_again.startswith("n")):
        question_play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    # Start a new game.
    if question_play_again.startswith("y"):
        print("\n" * 20)
        blackjack()

# Ask the player if they want to play.
question_play = ""
while not(question_play.startswith("y") or question_play.startswith("n")):
    question_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

# Start a game.
if question_play.startswith("y"):
    print("")
    blackjack()
