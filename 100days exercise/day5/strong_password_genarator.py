import random
from typing import final

numbers = ["0", '1', '2', '3', '4', '5', '6', '7', '8','9']
letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special_characters = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
    '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"', ',', '<', '.', '>',
    '/', '?', '`', '~'
]

pass_letter=int(input("enter the number of letter in password :"))
pass_spec1=int(input("enter the number of spec in password :"))
pass_num1=int(input("enter the number of number in password :"))
pas_let=""
pass_spec=""
pass_num=""

for i in range (0,pass_letter):
    ranchar=random.choice(letter)#for letter
    pas_let+=ranchar

for i in range(0,pass_spec1):
    ranspec=random.choice(special_characters)#for special char
    pass_spec+=ranspec

for i in range(0,pass_num1):
    rannum=random.choice(numbers)
    pass_num+=rannum


total=pas_let+pass_spec+str(pass_num)
word=list(total)
random.shuffle(word)
password=""
for char in word:
     password+=char
print(f"Your very strong password with {pass_letter} numbers, {pass_num1} letters, {pass_spec1} special_character is  {password}")