from turtle import Turtle,Screen
import random


screen = Screen()
#
# def move_forward():
#     tim.forward(10)
#
# def move_backward():
#     tim.backward(10)
#
# def turn_right():
#     tim.right(10)
#
# def turn_left():
#     tim.left(10)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(move_forward, "w")
# screen.onkey(move_backward, "x")
# screen.onkey(turn_right, "d")
# screen.onkey(turn_left, "a")
# screen.onkey(clear, "c")
is_race_on = False
screen.setup(width= 500, height= 400)
users_bet = screen.textinput(title= "Make your bet ", prompt= "which turtle will win the race? Enter the color: ")
print(users_bet)
colors = ["black", "red", "orange", "yellow", "purple", "green"]
y_position = [150, 100, 50, 0, -50, -100]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtles = Turtle()
    new_turtles.shape("turtle")
    new_turtles.color(colors[turtle_index])
    new_turtles.penup()
    new_turtles.goto(x= -235, y=y_position[turtle_index])
    all_turtles.append(new_turtles)

if users_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == users_bet:
                print(f"you've won! the {winning_color} turtle is the winner")
            else:
                print(f"you've lost! the {winning_color} turtle is the winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()