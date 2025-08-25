from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on=True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

print("Welcome to Coffee Machine!")
while is_on:
    option=menu.get_items()
    choices=input(f"What would you like? {option} :")
    if choices=="off":
        is_on=False
    elif choices=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choices)
        if coffee_maker.is_resource_sufficient(drink)and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

