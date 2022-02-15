from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car=[]
        self.c_speed=STARTING_MOVE_DISTANCE

    def create_c(self):
        r_chance=random.randint(1,6)
        if r_chance==1:
            n_car=Turtle("square")
            n_car.shapesize(stretch_wid=2,stretch_len=1)
            n_car.penup()
            n_car.color(random.choice(COLORS))
            ran_y=random.randint(-250,250)
            n_car.goto(300,ran_y)
            self.car.append(n_car)


    def move_c(self):
        for c in self.car:
            c.backward(STARTING_MOVE_DISTANCE)


    def lvel_up(self):
        self.c_speed+=MOVE_INCREMENT

