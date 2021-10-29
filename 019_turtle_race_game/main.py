from turtle import Turtle, Screen
import random

is_race_on = False
colors = ["blue", "red", "yellow", "green", "purple"]
turtles_y_coordinates = [100, 50, 0, -50, -100]
screen = Screen()
screen.setup(width=600, height=500)
bet = screen.textinput(title="BET!", prompt="chooose a color").lower()
print(bet)
turtles = list()

for position in range(0, len(colors)):
    tim = Turtle(shape="turtle")
    tim.color(colors[position])
    tim.penup()
    tim.goto(x=-280,y=turtles_y_coordinates[position])
    turtles.append(tim)

if bet:
    is_race_on = True

while is_race_on:
    for single_turtle in turtles:
        distance_to_move = random.randint(1,20)
        single_turtle.forward(distance_to_move)
        if single_turtle.xcor() > 260:
            print(f"!!!{single_turtle.pencolor()} won!!!")
            if single_turtle.pencolor() == bet:
                print("YOU WERE RIGHT!")
            else:
                print("SORRY, WROOOOOONG!")
            is_race_on = False

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

# colors = []
# screen.setup(600,400)
# bet = screen.textinput("Choose the winner", "Which rainbow color turtle is going to win? Type a turtle color: ")
# print(bet)



screen.exitonclick()