from turtle import Screen, Turtle, colormode
from random import randint

timy = Turtle()
timy.shape('turtle')
timy.color('pale turquoise')


# SQUARE
# for _ in range(4):
#     timy.forward(100)
#     timy.right(90)

# DASHED LINE
# for _ in range(4):
#     timy.forward(10)
#     timy.penup()
#     timy.forward(10)
#     timy.pendown()

# SHAPE SHIFTERS
def get_random_colors():
    return (randint(0,256),randint(0,256),randint(0,256))

colormode(255)
for position in range(3,10):
    timy.pencolor((get_random_colors()))
    for _ in range(position):
        timy.right(360/position)
        timy.forward(50)



screeny = Screen()
screeny.exitonclick()