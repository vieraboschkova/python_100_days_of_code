from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score_board
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.listen()
screen.tracer(0)

is_game_on = True

left_paddle = Paddle()
right_paddle = Paddle()

left_paddle.goto(-350, 0)
right_paddle.goto(350,0)

screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')
screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, 'Down')

board = Score_board()
ball = Ball()

while is_game_on:
    screen.update()
    ball.move()
    time.sleep(.1)

    if ball.ycor() > 280 or ball.ycor() < -280:
        print('bouncing!')
        ball.bounce()

    if ball.distance(right_paddle) > 20 and ball.xcor() > 370:
        is_game_on = False
        print("GAME OVER!")
    elif ball.distance(left_paddle) > 20 and ball.xcor() < -370:
        is_game_on = False
        print("GAME OVER!")
    elif ball.distance(left_paddle) < 20 and ball.xcor() > -370:
        ball.bounce_from_paddle()
        board.add_point_l()
    elif ball.distance(right_paddle) < 20 and ball.xcor() < 370:
        ball.bounce_from_paddle()
        board.add_point_r()
    # else:
    #     print("Game on")


screen.exitonclick()