#THE AVG HEIGHT CALCULATOR
people=input("enter the people height")
people=people.split(",")
print(people)
total_height=0
len=0
for avg in people:
    len=len+1
    total_height=int(avg)+total_height
print("The avg Height of the students",total_height,'cm')
print("The total number of the People",len)
avg_height=total_height/len
print("The average height is ",round(avg_height),"cm")