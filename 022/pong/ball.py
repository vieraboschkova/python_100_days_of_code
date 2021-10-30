from turtle import Turtle, backward, ycor

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(10)

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce(self):
        self.y_move *= -1

    def bounce_from_paddle(self):
        self.x_move *= -1