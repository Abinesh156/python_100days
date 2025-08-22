# from turtle import Turtle, Screen
# timmy = Turtle()
# myscreen = Screen()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# myscreen.screensize(250, 300)
# myscreen.bgcolor("black")
# myscreen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Food type", ["briyani", "veg rice", "fish currey","mutton "])
table.add_column("price in $", ["$22", "$33", "$34", "$35"])

print(table)