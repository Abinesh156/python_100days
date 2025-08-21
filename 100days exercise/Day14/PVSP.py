import random
instagram_celebrities = [
    {"name": "Cristiano Ronaldo", "followers_millions": 661},
    {"name": "Lionel Messi", "followers_millions": 506},
    {"name": "Selena Gomez", "followers_millions": 420},
    {"name": "Dwayne 'The Rock' Johnson", "followers_millions": 394},
    {"name": "Kylie Jenner", "followers_millions": 393},
    {"name": "Ariana Grande", "followers_millions": 375},
    {"name": "Kim Kardashian", "followers_millions": 356},
    {"name": "Beyoncé", "followers_millions": 311},
    {"name": "Khloé Kardashian", "followers_millions": 302},
    {"name": "Justin Bieber", "followers_millions": 294},
    {"name": "Kendall Jenner", "followers_millions": 287},
    {"name": "Taylor Swift", "followers_millions": 281},
    {"name": "Virat Kohli", "followers_millions": 274},
    {"name": "Jennifer Lopez", "followers_millions": 248},
    {"name": "Neymar Jr.", "followers_millions": 231},
    {"name": "Nicki Minaj", "followers_millions": 225},
    {"name": "Miley Cyrus", "followers_millions": 212},
    {"name": "Katy Perry", "followers_millions": 204},
    {"name": "Zendaya", "followers_millions": 178},
    {"name": "Lisa (BLACKPINK)", "followers_millions": 106}
]

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
        print("you lose")
        flag = False
def display(insta_cele):
    print("A for", insta_cele[0]["name"], "vs", "b for", insta_cele[1]["name"], "who has more followers")
    a = insta_cele[0]["followers_millions"]
    b = insta_cele[1]["followers_millions"]
    return a,b


insta_cele=[]
random_vip()
# print(insta_cele)
score=0
flag=True
while flag:
    print(f"your score is: {score}")
    a, b = display(insta_cele)
    # print(a, b)
    option=input("chose A or B : ")
    position=0
    if option == "a":
        position=1
    elif option == "b":
        position=0
    win_check(option,a,b,position)
