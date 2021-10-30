from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.goto(STARTING_POSITION)
        self.left(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def is_on_top(self):
        return self.ycor() > 280

    def start_from_bottom(self):
        self.goto(STARTING_POSITION)