# import colorgram

# rgb = []
# colors = colorgram.extract('image.jpg', 64)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb.append(new_color)

# print(rgb)
import random
from turtle import Turtle, Screen

color = [ (202, 163, 98), (45, 97, 147), (168, 49, 80), (222, 210, 108), (141, 92, 64), (118, 172, 203), (173, 163, 40), (210, 133, 171), (208, 67, 105), (223, 78, 56), (91, 106, 193), (143, 33, 60), (31, 139, 94), (57, 172, 105), (124, 218, 205), (228, 170, 186), (47, 186, 197), (126, 191, 168), (100, 50, 42), (34, 61, 117), (223, 208, 22), (148, 207, 225), (169, 187, 225), (233, 173, 163), (49, 57, 66), (41, 75, 78), (74, 47, 41), (24, 91, 88), (85, 32, 52), (30, 62, 61)]

def rand_color():
    return random.choice(color)

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    tom.color(R, G, B)

tom = Turtle()
# tom.setheading(225)
# tom.pu()
# tom.forward(300)
tom.hideturtle()

for _ in range(11):
    tom.setpos(0,_ * 35)
    for _ in range(10):
        change_color()
        tom.pu()
        tom.fd(15)
        tom.dot(20)
        tom.pu()
        tom.fd(15)


screen = Screen()
screen.exitonclick()