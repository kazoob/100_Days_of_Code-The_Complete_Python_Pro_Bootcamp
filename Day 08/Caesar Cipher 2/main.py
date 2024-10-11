alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
def caesar(operation, original_text, shift_amount):
    output = ""

    if operation.startswith("e") or operation.startswith("d"):
        if operation.lower().startswith("d"):
            shift_amount *= -1
        for letter in original_text:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output += alphabet[shifted_position]
        print(f"Here is the result: {output}")
    else:
        print(f"Error - invalid direction: {operation}")

caesar(operation=direction, original_text=text, shift_amount=shift)
