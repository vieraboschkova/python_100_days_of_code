import random 
from turtle import Screen, Turtle
import time

DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = list()
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in range(0,3):
            self.add_segment((-position*20, 0))
    
    def add_segment(self, position):
        segment = Turtle('square')
        segment.speed(3)
        segment.penup()
        segment.color(random.randint(30,255), random.randint(30,255), random.randint(30,255))
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for position in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[position -1].xcor()
            new_y = self.segments[position -1].ycor()
            self.segments[position].goto(new_x, new_y)
        self.segments[0].forward(DISTANCE)

    def move_up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def move_down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def turn_left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def turn_right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
