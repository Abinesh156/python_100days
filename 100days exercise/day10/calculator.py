#calculator app


# add function
def add(n1,n2):
    return n1+n2


#subraction function
def sub(n1,n2):
    return n1-n2


#multipication
def mul(n1,n2):
    return n1*n2


#division function
def div(n1,n2):
    return n1/n2


opration={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}




num_1=float(input("enter a number to calculate :"))


for opt in opration:
    print(opt)

user_op=input("choose the opration you like to do :")
calculator=opration[user_op]
num_2=float(input("enter a second number to calculate :"))
answer=calculator(num_1,num_2)


print(f"{num_1} {user_op} {num_2} :{answer}")
#calculation second
while True:
    end = input("press Enter to continue calculating type n to end :")
    if end == "n":
        break
    for opt in opration:
        print(opt)
    user_op=input(f"choose the opration you like to do {answer}:")
    num_1=float(input(f"enter a number to calculate with {answer} {user_op}:"))
    answer1=answer
    calculator=opration[user_op]
    answer=calculator(answer,num_1)

    print(f"{answer1} {user_op} {num_1} :{answer}")
