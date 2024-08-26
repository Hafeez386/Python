import random
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("arrow")
timmy_the_turtle.color("black")


is_moving = True
while is_moving:
   timmy_the_turtle.forward(200)
   timmy_the_turtle.right(90)

for _ in range(4):
    timmy_the_turtle.forward(230)
    timmy_the_turtle.left(120)

import heroes
print(heroes.gen())
for _ in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()
    timmy_the_turtle.pensize(12)

num_side = 5
def draw_shapes(num_side):
    angle = 360 / num_side
    for _ in range(num_side):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)
for shape_side_n in range(6, 18):
    draw_shapes(shape_side_n)
direction = [0, 90, 180, 270]
timmy_the_turtle.pensize(6)
timmy_the_turtle.speed(5777)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for _ in range(200):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(direction))

is_moving = True
while is_moving:
    timmy_the_turtle.circle(100)
    current_heading = timmy_the_turtle.heading()
    timmy_the_turtle.setheading(current_heading + 10)
    timmy_the_turtle.circle(100)

screen = Screen()
screen.exitonclick()