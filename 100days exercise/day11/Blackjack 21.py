import random

computer=[]
player=[]
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10]
    return random.choice(cards)

for _ in range(2) :
    # deal_card()
    computer.append(deal_card())
    player.append(deal_card())


print(computer)
print(player)


