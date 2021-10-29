from turtle import Screen, Turtle

screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')

snake_segments = list()
head_coordinates = [0, 0]
for position in range(0,3):
    print(position)
    segment = Turtle('square')
    segment.penup()
    segment.color('white')
    segment.backward(position*20)
    snake_segments.append(segment)









screen.exitonclick()