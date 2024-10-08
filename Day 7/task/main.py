import random

debug = True

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
if debug:
    print(f"Chosen word: {chosen_word}")

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Please guess a letter: ").lower()
if debug:
    print(f"Player guess: {guess}")

# Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
guess_correct = False

for letter in chosen_word:
    if guess == letter:
        guess_correct = True

if guess_correct:
    print("Right")
else:
    print("Wrong")
