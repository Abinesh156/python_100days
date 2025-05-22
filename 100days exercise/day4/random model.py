#Randomisation
import random
input("chose h or t ")
random=random.randint(1,100)
value=random**2
value=value%2
print(value)
if value==0:
    print("head")
else:
    print("tails")