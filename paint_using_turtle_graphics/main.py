from turtle import Turtle, Screen

tom = Turtle()

Screen = Screen()

def move_forward():
    tom.forward(10)

def move_backward():
    tom.backward(10)

def move_leftside():
    tom.left(10)

def move_rightside():
    tom.right(10)

Screen.listen()
Screen.onkey(key="w", fun=move_forward)

Screen.onkey(key="s", fun=move_backward)

Screen.onkey(key="a", fun=move_leftside)

Screen.onkey(key="d", fun=move_rightside)

Screen.exitonclick()