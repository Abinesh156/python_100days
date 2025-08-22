def brown_tea():
    cost=30
    print(f"brown tea cost {cost}")
    water=50
    coffee=18
    milk=100
    flag=check_ingredients(water, coffee, milk)
    mw,mc,mm=coffee_capacity(water,coffee,milk)
    return mw,mc,mm,cost,flag

def black_tea():
    cost = 40
    print(f"black tea cost {cost}")
    water = 60
    coffee = 25
    milk = 90
    flag = check_ingredients(water, coffee, milk)
    mw, mc, mm = coffee_capacity(water, coffee, milk)
    return mw, mc, mm, cost, flag

def lemon_tea():
    cost = 55
    print(f"lemon tea cost {cost}")
    water = 20
    coffee = 30
    milk = 50
    flag = check_ingredients(water, coffee, milk)
    mw, mc, mm = coffee_capacity(water, coffee, milk)
    return mw, mc, mm, cost, flag

def coffee_capacity(water,coffee,milk):
    global m_water, m_coffee, m_milk
    m_water-=water
    m_coffee-=coffee
    m_milk-=milk
    return m_water,m_coffee,m_milk

def cash_tea(CUSTOMER_one,CUSTOMER_five,cost):
    one = 1
    five = 5
    CUSTOMER_one*=one
    CUSTOMER_five*=five
    total=CUSTOMER_one+CUSTOMER_five
    print("given Ruppees",total)
    cost-=total
    return -cost

def check_ingredients(water, coffee, milk):
    global m_water, m_coffee, m_milk
    return m_water >= water and m_coffee >= coffee and m_milk >= milk

def check_cash(total,cost):
    return total>=cost


menu={"1":brown_tea,"2":black_tea,"3":lemon_tea}
#machine capacity
m_water = 300
m_coffee = 200
m_milk = 180
flag=True
while flag:
    option=input("enter your choice:\n 1 for brown tea Rs 30 \n 2 for black tea Rs 40\n 3 for lemon tea Rs 55 \n:")
    CUSTOMER_one=int(input("NUMBER OF one ruppees :"))
    CUSTOMER_five=int(input("NUMBER OF five ruppeees :"))
    m_water,m_coffee,m_milk,cost,flag=menu[option]()
    total=cash_tea(CUSTOMER_one,CUSTOMER_five,cost)
    nocash = check_cash(total, cost)
    if not nocash:
        print("Not enough money. Please try again.")
        continue  # Go back to top of loop
    print(f"cash balance {total}")
    print(f"balance in five ruppees {round(total/5)}")
    print(f"balance in one ruppees{round(total%5)}")
print("Thank you for playing not enough internet run again to play again")
