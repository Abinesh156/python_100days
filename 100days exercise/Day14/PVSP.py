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

def equal_check():
    global insta_cele
    while insta_cele[0] == insta_cele[1]:
        insta_cele = []
        random_vip()

insta_cele=[]
random_vip()
equal_check()


# insta_cele=[]
# print(insta_cele)
score=0
flag=True
while flag:
    print(f"your score current is: {score}")
    if insta_cele[0]==insta_cele[1]:
        equal_check()
    a, b = display(insta_cele)
    # print(a, b)
    option=input("chose A or B : ")
    position=0
    if option == "a":
        position=1
    elif option == "b":
        position=0
    win_check(option,a,b,position)
