import random

for x in range(20):
    coin = random.randint (1,2)

    if coin == 1:
        print(f"{x}: Heads")
    else:
        print(f"{x}: Tails")
