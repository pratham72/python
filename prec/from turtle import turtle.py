# from turtle import Turtle, Screen

# tom = Turtle()
# print(tom)
# tom.shape("turtle")
# tom.color("red","green")
# tom.forward(200)
# tom.backward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["pokemon Name", "Type"]

table.add_rows(
    [
        ["pikachu", "electric"],
        ["squirtle", "water"],
        ["Charmander", "fire"]
    ]
)

table.align = "l"
print(table)