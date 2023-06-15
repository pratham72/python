from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("snake game")
screen.bgcolor("Black")
screen.screensize(800, 800)
screen.tracer(0)

starting_position = [(0,0), (-20,0), (-40,0)]
objects = []

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()  
    score.count()
      
    
    if snake.head.distance(food) < 15:
        score.clear()
        snake.extend()
        score.score += 1
        food.refresh()
        
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        game_is_on = False
        score.game_over()

    for object in snake.objects:
        if object == snake.head:
            pass
        elif snake.head.distance(object) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
