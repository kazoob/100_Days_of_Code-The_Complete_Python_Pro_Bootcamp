# Available menu, including recipe (ingredients) and cost.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Current resources inside coffee machine.
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# Valid commands for user input.
VALID_COMMANDS = [
    "off",
    "report",
    "espresso",
    "latte",
    "cappuccino",
]

# List of coins accepted and values.
COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}


def check_resources(coffee, resources):
    """Check whether there are enough resources inside the coffee machine to make the requested coffee. Returns True or False."""
    # Get the recipe for the ordered coffee.
    ingredients = MENU[coffee]["ingredients"]

    # Verify each ingredient.
    for i in ingredients:
        # If one of the resources are insufficient, return False.
        if resources[i] < ingredients[i]:
            print(f"Sorry there is not enough {i}.\n")
            return False

    # All ingredients are available, return True.
    return True


def make_coffee(coffee, resources):
    """Deducts the resources required to make the ordered coffee from the coffee machine."""
    # Get the recipe for the ordered coffee.
    ingredients = MENU[coffee]["ingredients"]

    # Deduct each ingredient from the available resources.
    for i in ingredients:
        resources[i] -= ingredients[i]


def coffee_maker(command):
    """Run the coffee maker command."""

    # Print resource report.
    if command == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${resources['money']:.2f}")
        print("")

    # Make coffee
    else:
        coffee_type = command
        coffee_cost = MENU[coffee_type]["cost"]
        money_collected = 0

        # Verify the coffee machine has enough resources to make the coffee.
        if check_resources(coffee_type, resources):

            # Ask the user for coins to pay for the coffee.
            print(f"Please insert coins to pay ${coffee_cost:.2f}\n")
            for coin in COINS:

                # Validate the user input, ensure int.
                while True:
                    coin_input = input(f"How many {coin}?: ")
                    try:
                        coin_input = int(coin_input)
                    except ValueError:
                        print("Invalid entry.")
                        continue
                    break

                # Total amount of money collected.
                money_collected += coin_input * COINS[coin]

            print("")

            # Calculate excess money collected (change).
            change = money_collected - coffee_cost

            # Check if enough money was collected for the coffee.
            if change < 0:
                print(f"Sorry that is not enough money. ${money_collected:.2f} refunded.\n")
            else:
                # Return change to the user (if any).
                if change > 0:
                    print(f"Here is ${change:.2f} dollars in change.\n")

                # Add the cost of the coffee to the profits.
                resources["money"] += coffee_cost

                # Make coffee
                make_coffee(coffee_type, resources)
                print(f"Here is your {coffee_type} ☕️. Enjoy!\n")


# Run the coffee machine until "off" is entered.
user_input = ""
while user_input != "off":

    user_input = ""

    # Get command from user. If an invalid choice is entered, ask again.
    while user_input not in VALID_COMMANDS:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    print("")

    if user_input != "off":
        coffee_maker(user_input)
