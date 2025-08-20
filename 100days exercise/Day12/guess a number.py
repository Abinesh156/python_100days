import random
NUMBER=random.randint(1,100)
print(NUMBER)
print("welcome number guessing game")
print("i am going to think a number between 1 and 100 you guess it")
level=input("chose the level to be hard or easy?")

def user_level(level):
    if level == "hard":
         attemts=5
    elif level == "easy":
        attemts=10
    while attemts > 0:
        print(f"You have {attemts} attempts left")
        player_guess=int(input("enter your guess: "))
        if player_guess!=NUMBER:
            print("you guess is incorrect")
        if player_guess<NUMBER:
            print("your guess is too low")
        elif player_guess>NUMBER:
            print("your guess is too high")
        elif player_guess==NUMBER:
            print("your guess is correct,YOU WIN!!!!!!!")
            break
        attemts=attemts-1
    if attemts==0:
        print("you lose the game")

# def level_easy():
#     attemts = 10
#     while attemts > 0:
#         print(NUMBER)
#         print(f"You have {attemts} attempts left")
#         player_guess = int(input("enter your guess: "))
#         if player_guess != NUMBER:
#             print("you guess is incorrect")
#         if player_guess < NUMBER:
#             print("your guess is too low")
#         elif player_guess > NUMBER:
#             print("your guess is too high")
#         elif player_guess == NUMBER:
#             print("your guess is correct,YOU WIN!!!!!!!")
#             break
#         else:
#             print("you guess is incorrect")
#         attemts = attemts - 1
#     if attemts == 0:
#         print("you lose the game")
user_level(level)