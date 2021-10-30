from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2
PLUS_OR_MINUS = [-1, 1]

class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(0,10) == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(280, 20*random.randint(1,13)*random.choice(PLUS_OR_MINUS))
            new_car.color(random.choice(COLORS))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT