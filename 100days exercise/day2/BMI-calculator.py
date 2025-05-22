w=float(input("enter the weight??(kg)"))
h=0
h=float(input("enter the height ?? (cm)"))
h=h/100
print(h)
TH=h**2
bmi=w/(h**2)
print("bmi",bmi)
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 25:
    print("You have a normal weight.")
elif 25 <= bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")
