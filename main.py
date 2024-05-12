import random
import turtle
from turtle import Turtle, Screen

# colors = ["red", "blue", "green", "black", "pink", "grey", "brown", "orange", "yellow"]
directions = [0, 90, 180, 270]

tom = Turtle()
turtle.colormode(255)


def ran_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tom.hideturtle()
tom.pensize(10)
tom.speed('fastest')

for _ in range(500):
    tom.color(ran_color())
    tom.forward(30)
    tom.setheading(random.choice(directions))

scr = Screen()
scr.exitonclick()
