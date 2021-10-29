from turtle import Screen, Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize()
        self.penup()
        self.color("grey")
        self.speed(0)
        self.change_location()

    def change_location(self):
        self.goto(20*random.randint(-13, 13), 20*random.randint(-13, 13))