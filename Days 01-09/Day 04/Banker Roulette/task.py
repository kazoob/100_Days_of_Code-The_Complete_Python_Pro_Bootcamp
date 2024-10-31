import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Solution 1
chosen_friend = random.randint(0, len(friends) - 1)
print(f"{friends[chosen_friend]} must pay the bill.")

# Solution 2
print(f"{random.choice(friends)} must pay the bill.")
