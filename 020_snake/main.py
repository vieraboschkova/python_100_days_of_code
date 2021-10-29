from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score_board

# initial screen setup
screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.listen()
screen.tracer(0)
screen.colormode(255)

snake = Snake()
food = Food()
score_board = Score_board()

screen.update()

screen.onkey(snake.move_up, 'Up')
screen.onkey(snake.move_down, 'Down')
screen.onkey(snake.turn_left, 'Left')
screen.onkey(snake.turn_right, 'Right')

# print(snake_segments)
# start game
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 19:
        food.change_location()
        snake.extend()
        score_board.add_point()

    if snake.segments[0].xcor() < -280 or snake.segments[0].xcor() > 280 or snake.segments[0].ycor() < -280 or snake.segments[0].ycor() > 280:
        game_on = False
        score_board.end_game()

    # for segment in snake.segments[1:]:
    #     if snake.head.distance(segment) < 10:
    #         game_on = False
    #         score_board.end_game()
            






screen.exitonclick()