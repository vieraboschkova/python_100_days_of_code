import turtle
import pandas
from state_name import State_Name
import time

screen = turtle.Screen()
screen.title("US QUIZ")
bg_image = "./025_us_state_quiz/blank_states_img.gif"
screen.addshape(bg_image)
turtle.shape(bg_image)

states_data = pandas.read_csv("./025_us_state_quiz/50_states.csv")
names = states_data.state.to_list()
print(names)
# is_game_on = True
# time_to_play = 10
guessed = 0

while guessed < 50:
    new_state = screen.textinput(title="Add a name", prompt="Guess next stata").title()
    if new_state == "Exit":
        guessed = 50
        break

    elif new_state in names:
        guessed += 1
        state_data = states_data[states_data.state == new_state]
        new_name_on_screen = State_Name(int(state_data.x), int(state_data.y), new_state)
    
    if guessed == 50:
        print("GOT IT ALL")

screen.exitonclick()