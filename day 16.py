import turtle
from turtle import Turtle,Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("yellow")
timmy.forward(152)
timmy.right(90)
timmy.forward(152)
timmy.right(90)
timmy.forward(152)
timmy.right(90)
timmy.forward(152)
timmy.right(90)
timmy.distance(56)
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("pokemon name", ["pikachu","squirtle","charmander",])
table.add_column("type", ["electric", "water", "fire",])

table.align = "l"
print(table)