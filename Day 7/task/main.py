import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# Use a while loop to let the user guess again.

gameover = False

while not gameover:
    guess = input("Guess a letter: ").lower()

    display = ""

    # Change the for loop so that you keep the previous correct letters in display.

    for x in range(0, len(chosen_word)):
        letter = chosen_word[x]

        if placeholder[x] == "_":
            if letter == guess:
                display += letter
            else:
                display += "_"
        else:
            display += placeholder[x]

    print(display)

    placeholder = display

    if placeholder == chosen_word:
        gameover = True

print("Game over!")
