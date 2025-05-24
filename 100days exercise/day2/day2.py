#Day-2 creating the new project there is no change
#tip calculator
totalamount=int(input("enter the bill amount: "))
spilt=int(input("enter the number of people to spilt the bill amount?: "))
percentage=int(input("enter the percentage for the tip?: "))
tips=(percentage/100)*totalamount
print(f"The tip amount is \n${tips}")
final=totalamount+tips
each=final/spilt
print(f"The total amount to pay!!!\n${final}")
print(f"The total amount to pay each!!!\n${each}")
####################