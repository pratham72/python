from turtle import Turtle, Screen
import random

tom = Turtle()

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    tom.color(R, G, B)

def motion():
    angle = [0, 90, 180, 270]
    new_angle = random.choice(angle)
    return tom.seth(new_angle)

tom.speed("fastest")

for _ in  range(75):
    change_color()
    tom.circle(100)
    tom.right(5)

screen = Screen()
screen.exitonclick()
