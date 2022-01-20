from turtle import Turtle,Screen
t=Turtle()
t.shape("turtle")
'''for i in range(3):
    t.right(120)
    t.forward(100)
t.color("red")
for i in range(4):
    t.right(90)
    t.forward(100)
t.color("brown")
for i in range(5):
    t.right(72)
    t.forward(100)
t.color("green")
for i in range(6):
    t.right(60)
    t.forward(100)
t.color("blue")
for i in range(8):
    t.right(45)
    t.forward(100)'''

import random
colors=["red","blue","green","brown","black"]
dire=[0,90,270,180]

'''def tu(num):
    angle=360/num
    for i in range(num):
        t.forward(100)
        t.right(angle)
for s in range(3,11):
    t.color(random.choice(colors))
    tu(s)'''

t.speed("fastest")
'''for i in range(200):
    t.color(random.choice(colors))


    t.forward(20)
    t.setheading(random.choice(dire))'''
def draw(num):
    for i in range(int(360/num)):
        t.circle(50)
        t.setheading(t.heading()+num)
        t.color(random.choice(colors))
draw(5)
s=Screen()
s.exitonclick()
