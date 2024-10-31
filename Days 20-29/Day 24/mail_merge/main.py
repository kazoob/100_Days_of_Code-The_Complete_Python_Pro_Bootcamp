NAME_PLACEHOLDER = "[name]"
STARTING_LETTER_PATH = "Input/Letters/starting_letter.txt"
INVITED_NAMES_PATH = "Input/Names/invited_names.txt"
READY_TO_SEND_PATH = "Output/ReadyToSend/"

with open(STARTING_LETTER_PATH) as letter_file:
    starting_letter = letter_file.read()

with open(INVITED_NAMES_PATH) as names_file:
    names = names_file.readlines()

for name in names:
    name = name.strip()
    new_letter = starting_letter.replace(NAME_PLACEHOLDER, name)

    with open(f"{READY_TO_SEND_PATH}{name}.txt", mode="w") as file:
        file.write(new_letter)

# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
