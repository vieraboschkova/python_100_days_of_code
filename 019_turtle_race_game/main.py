from turtle import Turtle, Screen, clear

# tim = Turtle()
screen = Screen()
screen.listen()

# def move_forward():
#     tim.forward(10)
# def move_backwards():
#     tim.back(10)
# def turn_left():
#     tim.left(10)
# def turn_right():
#     tim.right(10)

# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# SKETCH
# screen.onkey(move_forward, 'w')
# screen.onkey(turn_left, 'a')
# screen.onkey(move_backwards, 's')
# screen.onkey(turn_right, 'd')
# screen.onkey(clear, 'c')

colors = []
screen.setup(600,400)
bet = screen.textinput("Choose the winner", "Which rainbow color turtle is going to win? Type a turtle color: ")
print(bet)



screen.exitonclick()