import random
import random as r
import pygame
from is_even import is_even
tose=int(input("odd(1) or even(2):"))
user_tose=int(input("enter a number(1-6):"))

random1=r.randint(1,2) #random number by robot
tose_value=user_tose+random1
user_pick=""

######
print(f"YOU:{user_tose}")
print(f"ROBOT:{random1}")
print(f"Total{tose_value}")
#############################
if is_even(tose_value)==is_even(tose): #human
    print("You WON THE TASE")
    user_pick=int(input("pick one Bating(0) or Bowling(1):"))

else:                                   #robot
    print("You lose the tose")
    num=["bat","bowl"]
    robo_pick=r.randint(0,1)
    print(f"I choose {num[robo_pick]},Lets play!!!!")


if user_pick==0:
    hum_score=int(input("Play enter number 0-6"))
    robot_play=random.randint(0,6)
    print(f"Robo bowl {robot_play}")
    if hum_score==robot_play:
        print("game over")
    else:
        hum_score+=hum_score
elif user_pick==1:
    robot_play = random.randint(0, 6)
    human_play=int(input("Bowl number (0-6)"))
    if robot_play==human_play:
        print("robot out")
    else:
        robot_play+=robot_score





