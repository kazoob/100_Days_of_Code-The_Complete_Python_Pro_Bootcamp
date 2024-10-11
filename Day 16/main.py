from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# List of coins accepted and values.
COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

valid_commands = [
    "off",
    "report",
]

my_coffee = CoffeeMaker()
my_menu = Menu()
my_money = MoneyMachine()

valid_commands.extend(my_menu.get_items().split("/"))

choice = None
while choice != "off":
    choice = None
    while choice not in valid_commands:
        choice = input(f"What would you like? ({my_menu.get_items()}): ").lower()

    print("")

    if choice != "off":
        if choice == "report":
            my_coffee.report()
            print()
        else:
            drink = my_menu.find_drink(choice)
            money_collected = 0

            if my_coffee.is_resource_sufficient(drink):
                if my_money.make_payment(drink.cost):
                    my_coffee.make_coffee(drink)
