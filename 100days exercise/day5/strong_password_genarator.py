import random
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special_characters = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
    '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"', ',', '<', '.', '>',
    '/', '?', '`', '~'
]

len=int(input("enter the lenth of the password"))
pass_letter=int(input("enter the number of letter in password"))
pass_spec=int(input("enter the number of spec in password"))
passlet=0
for i in range (0,pass_letter):
    random1=random.randint(0,int(pass_letter))
    passlet=letter[random1]
    print(passlet)
