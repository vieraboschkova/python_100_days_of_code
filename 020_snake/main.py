from turtle import Screen, Turtle
import time

# initial screen setup
screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

# initial snake setup
snake_segments = list()
head_coordinates = [0, 0]
for position in range(0,3):
    segment = Turtle('square')
    segment.penup()
    segment.color('white')
    segment.backward(position*20)
    snake_segments.append(segment)
screen.update()

# print(snake_segments)
# start game
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    for position in range(len(snake_segments) - 1, 0, -1):
        new_x = snake_segments[position -1].xcor()
        new_y = snake_segments[position -1].ycor()
        snake_segments[position].goto(new_x, new_y)
    snake_segments[0].forward(20)
    if snake_segments[0].xcor() < -260 or snake_segments[0].xcor() > 260 or snake_segments[0].ycor() < -260 or snake_segments[0].ycor() > 260:
        game_on = False
        
            






screen.exitonclick()