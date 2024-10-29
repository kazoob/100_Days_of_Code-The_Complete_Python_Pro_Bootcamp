from art import logo

prompt_user = True
bids = {}

while prompt_user:
    print(logo)

    # Ask the user for input
    name = input("Please enter your name: ")
    bid = round(float(input("Please enter your bid: $")),2)

    # Save data into dictionary {name: price}
    bids[name] = bid

    # Whether if new bids need to be added
    prompt_user_input = ""
    while not (prompt_user_input.startswith("y") or prompt_user_input.startswith("n")):
        prompt_user_input = input("Are there any other bidders (y/n): ").lower()

    if prompt_user_input.startswith("n"):
        prompt_user = False

# Compare bids in dictionary using sorted()
#bids_ordered = sorted(bids.items(), key=lambda item: item[1], reverse=True)
#print(f"The winner is {bids_ordered[0][0]} with a bid of ${bids_ordered[0][1]:,.2f}")

# Compare bids in dictionary using max()
highest_bidder = max(bids, key=bids.get)
print(f"The winner is {highest_bidder} with a bid of ${bids[highest_bidder]:,.2f}")
