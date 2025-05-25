number=input("enter a seires of numbers with , ")
number=number.split(',')
# number=['45','110','22','44']
high=0
for avg in number:
    avg=int(avg)
    if avg>high:
        high=avg
print(high)