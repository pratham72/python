from turtle import Turtle

STAR = [(0,0), (-20,0), (-40,0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    
    
    def __init__(self):
        self.objects = []
        self.create_snake()
        self.head = self.objects[0]

    def create_snake(self):
        for spot in  STAR:
            self.add_objects(spot)

    def add_objects(self, spot):
        object = Turtle("square")
        object.color("white")
        object.penup()
        object.goto(spot)
        self.objects.append(object)

    def extend(self):
        self.add_objects(self.objects[-1].position())
        
        
    def move(self):
        for object_num in range(len(self.objects) -1, 0, -1):
            new_x = self.objects[object_num - 1].xcor()
            new_y = self.objects[object_num - 1].ycor()
            self.objects[object_num].goto(new_x, new_y)
        self.head.forward(MOVE_DIS)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    
    
        



