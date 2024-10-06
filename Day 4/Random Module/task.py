import random

heads = 0
tails = 0

for x in range(1000):
    coin = random.randint (1,2)

    if coin == 1:
        heads += 1
        print(f"{x}: Heads")
    else:
        tails += 1
        print(f"{x}: Tails")

print(f"\nHeads: {heads}, Tails: {tails}")
