import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
board = Scoreboard()
screen.onkey(player.go_up, 'Up')
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            board.end_game()
            
    if player.is_on_top():
        board.add_point()
        car_manager.speed_up()
        player.start_from_bottom()

screen.exitonclick()