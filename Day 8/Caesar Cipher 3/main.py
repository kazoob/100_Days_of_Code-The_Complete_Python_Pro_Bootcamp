# Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    if encode_or_decode.startswith("e") or encode_or_decode.startswith("d"):
        output_text = ""

        if encode_or_decode.startswith("d"):
            shift_amount *= -1

        for letter in original_text:
            # What happens if the user enters a number/symbol/space?
            if letter in alphabet:
                shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
                output_text += alphabet[shifted_position]
            else:
                output_text += letter

        print(f"Here is the result: {output_text}")
    else:
        print(f"Error - invalid direction: {encode_or_decode}")

# Can you figure out a way to restart the cipher program?
cont = "y"

while cont == "y":
    direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    cont = ""
    while cont != "y" and cont != "n":
        cont = input("Type 'y' if you want to go again. Otherwise, type 'n'.\n")
