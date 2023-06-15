from turtle import Turtle, Screen
import random

is_game_on = False
screen = Screen()
screen.setup(600, 600)
user_input = screen.textinput(title="Make a bet", prompt="which turtle will win the race? choose colour:" )

colors = ["red", "green", "orange", "yellow", "blue", "purple"]
y_position = [-300,-200, -100, 0, 100, 200]
all_turtle = []

for _ in  range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[_])
    new_turtle.penup()
    new_turtle.goto(x=-300,y=y_position[_])
    all_turtle.append(new_turtle)

if user_input:
    is_game_on = True

while is_game_on == True:
    for turtle in all_turtle:
        if turtle.xcor() > 270:
            is_game_on = False
            win_turtle = turtle.pencolor()
            if win_turtle == user_input:
                print(f"you win! The {win_turtle} turtle  is winner.")
            else:
                print(f"you lose! The {win_turtle} turtle  is winner.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()