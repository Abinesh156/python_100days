
bids={}
end=True
while end:
    print("Welcome to the secret bid auction")
    name=input("Enter your name :")
    bid_amount=input("Enter the Amount of bid :")
    # end=False
    bids[name] = int(bid_amount)

    more=input("enter yes or no if any biders left ?")
    if more == "no":
        end =False
winner=max(bids)

print(f"the winner is {winner},the amount you bid is {bids[winner]}")
# print(type(bids))


