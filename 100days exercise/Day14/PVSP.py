import random
from celebritylist import instagram_celebrities

def ran_vip():
    return random.choice(instagram_celebrities)

def random_vip():
    for i in range(0,2):
        insta_cele.append(ran_vip())

def win_check(option,a,b,position):
    global score
    global flag
    if option == "a" and a > b or option == "b" and a < b:
        print("you win")
        insta_cele.append(ran_vip())
        insta_cele.pop(position)
        score += 1
    else:
        print("you lose, your score is",score)
        flag = False

def display(insta_cele):
    print("A for", insta_cele[0]["name"], "vs", "b for", insta_cele[1]["name"], "who has more followers in MILLION")
    a = insta_cele[0]["followers_millions"]
    b = insta_cele[1]["followers_millions"]
    return a,b


insta_cele=[]
random_vip()
print(insta_cele[1])
print(insta_cele[0])
if insta_cele[0]==insta_cele[1]:
    random_vip()
    print("changed")
# insta_cele=[]
# print(insta_cele)
score=0
flag=True
while flag:
    print(f"your score current is: {score}")
    a, b = display(insta_cele)
    # print(a, b)
    option=input("chose A or B : ")
    position=0
    if option == "a":
        position=1
    elif option == "b":
        position=0
    win_check(option,a,b,position)
