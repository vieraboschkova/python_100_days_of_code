from turtle import Turtle, ycor

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.penup()

    def go_up(self):
        if self.ycor() > 350:
            return
        else:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() < -350:
            return
        else:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)