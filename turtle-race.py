from turtle import Turtle,Screen
import random
s=Screen()
end=False
s.setup(width=500,height=400)
user_b=s.textinput(title="make a bet:",prompt="who will be the winner:")
print(user_b)
colors=["red","yellow","blue","green","purple","brown"]
y_p=[-70,-40,-10,20,50,80]
all_t = []
for i in range(0,6):
    new_t=Turtle(shape="turtle")
    new_t.color(colors[i])
    new_t.penup()
    new_t.goto(x=-230, y=y_p[i])
    all_t.append(new_t)

if user_b:
    end=True

while end:
    for turtle in all_t:
        if turtle.xcor()>230:
            end=False
            w_co=turtle.pencolor()
            if w_co==user_b:
                print(f"You've won! The {w_co} turtle is the winner!")
            else:
                print(f"You've lost! The {w_co} turtle is the winner!")

        r_distance=random.randint(0, 10)
        turtle.forward(r_distance)

s.exitonclick()