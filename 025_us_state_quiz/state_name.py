from turtle import Turtle

class State_Name(Turtle):

    def __init__(self, x, y, name):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(f"{name}", align="center", font=("Arial", 12, "normal"))
       
