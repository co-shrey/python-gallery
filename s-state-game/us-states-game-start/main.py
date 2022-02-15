import turtle
import pandas

s=turtle.Screen()
s.title("state-game")
image="blank-states-img.gif"
s.addshape(image)
turtle.shape(image)
def get_mouse_click_coor(x,y):
    print(x,y)

data=pandas.read_csv("50_states.csv")
all_state=data.state.to_list()

guess_s=[]
while len(guess_s)<29:
    answer_t=s.textinput(title=f"{len(guess_s)}/28 state correct",prompt="what's another state name?").title()
    if answer_t=="Exit":
        break
    if answer_t in all_state:
        guess_s.append(answer_t)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_t]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_t)


