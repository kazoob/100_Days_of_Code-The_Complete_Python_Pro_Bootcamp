import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# Create a "placeholder" with the same number of blanks as the chosen_word

placeholder = ""
for letter in chosen_word:
    placeholder += "_"

print(placeholder)

guess = input("Guess a letter: ").lower()

# Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
        print("Right")
    else:
        display += "_"
        print("Wrong")

print(display)

placeholder = display
