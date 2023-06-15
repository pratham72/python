from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

    def count(self):
        self.hideturtle()
        self.goto(0, 290)
        self.color("white")
        self.write(f"Score = {self.score}", move = False, align = "center", font = ('Arial', 18, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over.", move = False, align = "center", font = ('Arial', 18, 'normal'))