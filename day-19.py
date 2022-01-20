from turtle import Turtle,Screen
t=Turtle()
s=Screen()

def move_f():
    t.forward(10)

def move_b():
    t.backward(10)

def move_l():
    t.left(10)
def move_r():
    t.right(10)
def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
s.listen()
s.onkey(move_f,"w")
s.onkey(move_b,"b")
s.onkey(move_l,"l")
s.onkey(move_r,"r")
s.onkey(clear,"c")
s.exitonclick()