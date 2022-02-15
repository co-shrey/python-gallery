import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
p=Player()
c=CarManager()
s=Scoreboard()
screen.listen()
screen.onkey(p.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    c.create_c()
    c.move_c()

    for ca in c.car:
        if ca.distance(p)<20:
            game_is_on=False
            s.end_g()

    if p.is_fin():
        p.start_po()
        c.lvel_up()
        s.inc_level()



screen.exitonclick()
