from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

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
            my_money.report()
            print()
        else:
            drink = my_menu.find_drink(choice)
            money_collected = 0

            if my_coffee.is_resource_sufficient(drink):
                if my_money.make_payment(drink.cost):
                    my_coffee.make_coffee(drink)
