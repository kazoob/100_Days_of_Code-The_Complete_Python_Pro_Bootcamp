from art import logo

def add(n1, n2):
    """Add n2 to n1."""
    return n1 + n2


def subtract(n1, n2):
    """Subtract n2 from n1."""
    return n1 - n2


def multiply(n1, n2):
    """Multiply n1 by n2."""
    return n1 * n2


def divide(n1, n2):
    """Divide n1 by n2."""
    return n1 / n2


# List of allowed operations, mapped to functions.
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

should_continue = True
num1 = None

# Run calculator until user wants to quit.
while should_continue:
    num2 = None
    operation = None
    result = None

    # Print the logo.
    print(logo)

    # Prompt user for num1, unless it was carried over from the previous calculation.
    if num1 is None:
        num1 = float(input("Enter the first number: "))
    else:
        print(f"The first number is: {num1}")

    # Prompt user for the operation, verifying against list of allowed operations.
    while not operation in operations:
        operation = input("Enter the operation (+,-,*,/): ")

    # Prompt user for num2.
    num2 = float(input("Enter the second number: "))

    # Perform and display the calculation.
    result = operations[operation](num1,num2)
    print(f"\nThe result of {num1} {operation} {num2} = {result}\n")

    # Prompt the user to quit, continue with carrying over num1 or continue with a new calculation.
    user_prompt = ""
    while not(user_prompt.startswith("q") or user_prompt.startswith("y") or user_prompt.startswith("n")):
        user_prompt = input(f"Type 'q' to quit, 'y' to continue calculating with {result}, or 'n' to start a new calculation. ").lower()

    # Quit
    if user_prompt.startswith("q"):
        should_continue = False
    # Continue with carrying over num1
    elif user_prompt.startswith("y"):
        num1 = result
    # Continue with new calculation
    else:
        num1 = None

    print("")
