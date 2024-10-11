print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if not(size.upper() == "S" or size.upper() == "M" or size.upper() == "L"):
  print("Size was not entered correctly, assuming L.")
  size = "L"

if not(pepperoni.upper() == "Y" or pepperoni.upper() == "N"):
    print("Pepperoni was not entered correctly, assuming N.")
    pepperoni = "N"

if not(extra_cheese.upper() == "Y" or extra_cheese.upper() == "N"):
    print("Extra Cheese was not entered correctly, assuming N.")
    extra_cheese = "N"

price = 0

if size.upper() == "S":
    price += 15
elif size.upper() == "M":
    price += 20
else:
    price += 25

if pepperoni.upper() == "Y":
    if size.upper() == "S":
        price += 2
    else:
        price += 3

if extra_cheese.upper() == "Y":
    price += 1

print(f"Your final bill is: ${price}.")
