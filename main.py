import turtle
import pandas
screen = turtle.Screen()

screen.title("U.S. States Game")
image = 'blank_states_img.gif'

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []
#
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

while len(guessed_state) < 50:
    answer_state = (screen.textinput(title=f'{len(guessed_state)}/ 50States Correct.',
                                     prompt="What's another states name")).title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_states.append(state)
        new_data = pandas.DataFrame()
        new_data.to_csv("States_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        # or you can write
        # t.write(state_data.state.item())







