from turtle import Screen, Turtle, colormode
from random import choice, randint
import colorgram

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


def get_random_colors():
    return (randint(0,255),randint(0,255),randint(0,255))

colormode(255)
# SHAPE SHIFTERS
# for position in range(3,10):
#     timy.pencolor((get_random_colors()))
#     for _ in range(position):
#         timy.right(360/position)
#         timy.forward(50)

def get_random_direction():
    return randint(0,1)

def get_random_length():
    return randint(10,50)

def get_random_angle():
    return randint(1,360)

# number_of_steps_done = 0
# timy.pensize(10)
# while number_of_steps_done < 50:
#     timy.pencolor((get_random_colors()))
#     timy.speed('fastest')
    
#     direction = get_random_direction()
#     length_of_step = get_random_length()
#     # angle = get_random_angle()
#     if direction == 0:
#         timy.left(90)
#     else:
#         timy.right(90)
#     timy.forward(length_of_step)
#     number_of_steps_done += 1

# timy.setheading()

# SPIROGRAPH

# angle = 0
# timy.speed('fastest')

# while angle < 360:
#     timy.pencolor((get_random_colors()))
#     timy.circle(50)
#     timy.left(10)
#     angle += 10

# DOT PAINTING

colors = colorgram.extract('dots.jpg', 20)
print(colors)
def get_rgb_tuple(color_in_rgb):
    return(color_in_rgb.r, color_in_rgb.g, color_in_rgb.b)

rgb_colors = []
for color in colors:
    rgb_colors.append(get_rgb_tuple(color.rgb))

# print(rgb_colors)

number_of_circles = 0
timy.penup()
timy.hideturtle()
timy.setpos(-280,-280)
while number_of_circles < 100:
    number_of_circles_in_row = 0
    while number_of_circles_in_row < 20:
        # timy.dot(20, 'blue')
        timy.dot(20,(choice(rgb_colors)))
        # timy.forward(60)
        number_of_circles_in_row += 1
        number_of_circles += 1
        # print(number_of_circles_in_row)
        # print(number_of_circles)
        if number_of_circles_in_row == 10:
            timy.left(90)
            timy.fd(60)
            timy.left(90)
        elif number_of_circles_in_row == 20:
            timy.right(90)
            timy.fd(60)
            timy.right(90)
        else:
            timy.forward(60)




screeny = Screen()
screeny.exitonclick()