from turtle import Screen, Turtle
import time
from snake import Snake
# initial screen setup
screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

snake = Snake()
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
    if snake.segments[0].xcor() < -260 or snake.segments[0].xcor() > 260 or snake.segments[0].ycor() < -260 or snake.segments[0].ycor() > 260:
        game_on = False
        
            






screen.exitonclick()