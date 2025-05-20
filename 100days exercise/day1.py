import re
from datetime import datetime
print("welcome to the rollercoaster")
#calculating the age
dob=(input("enter your DOB in the format like day/month/year"))
# Regex to match format DD/MM/YYYY with basic range checks
pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/([0-9]{4})$"
age=0
if re.match(pattern, dob):
    day, month, year = (dob.split("/"))
    TDyear = datetime.today().year
    age=int(year)-TDyear
    print("your age is ",abs(age))
else:
    print("❌ Invalid format! Please enter DOB as DD/MM/YYYY (e.g., 15/06/2002)")
# age=int(input("Enter Your Age!!"))
age=abs(age)
bill=0
if age <= 11:
    print("Not able to ride❌,your age should be above 12 ")
elif age<=17:
    bill=3
    print(f"your are is child cater.. bill is ${bill} Dollar")
elif age > 18:
    bill=7
    print(f"your are in adult cater... ${bill} Dollar")
photo=(input("Do you need photo?"))
if photo=="y":
    bill+=3
    print(f"additional of 3 dollor will be charged total bill = ${bill} Dollar\nSay chesseee!!!!!!!!!")
print(f"your total bill is ${bill} Dollar")

