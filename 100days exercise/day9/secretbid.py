bids = []

print("Welcome to the secret bid auction")

def secret_bid(user, amount):
    temp = {
        "name": user,
        "bid_amount": amount,
    }
    bids.append(temp)

while True:
    name = input("Enter your name: ")
    bid_amount = int(input("Enter the Amount of bid: "))
    secret_bid(name, bid_amount)
    more = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if more == "no":
        break

# Find the winner
if bids:
    winner = max(bids, key=lambda x: x["bid_amount"])
    print(f"The winner is {winner['name']}, the amount you bid is {winner['bid_amount']}")
else:
    print("No bids were placed.")