from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("PONG")
screen.listen()

left_paddle = Paddle()
right_paddle = Paddle()
left_paddle.goto(-350, 0)
right_paddle.goto(350,0)

screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')
screen.onkey(right_paddle.go_up, 'o')
screen.onkey(right_paddle.go_down, 'l')

screen.exitonclick()