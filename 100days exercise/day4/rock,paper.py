#rock paper scissors
import random
rock="""
rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors="""
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
#----------------------------------------------------#
usr_value=input("Can you win ^-^ Type 0 for rock,Type 1 for Paper,Type 2 for scissors : ")
game=[rock,paper,scissors]
human=game[int(usr_value)]
print("user",human)
computer=random.randint(0,2)
bot=game[computer]
print("BOT",bot)
#if conditions for the bot
#win posibility
#if human rock 0 scissors 2 win
#if human paper 1 rock 0 win
#if human scissors 2 paper 1

if int(usr_value)==0 and computer==2:
    print("your win human")
elif int(usr_value)==1 and computer==0:
    print("you win human")
elif int(usr_value)==2 and computer==1:
    print("you win human")
elif int(usr_value)==computer:
    print("Draw its a match")
else:
    print("you lose!!! better luck next time!!!!")