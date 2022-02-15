from turtle import  Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level=1
        self.penup()
        self.color("white")
        self.goto(-280,250)
        self.up_scor()



    def up_scor(self):
        self.clear()
        self.write(f"level:{self.level}", align="left", font=FONT)

    def inc_level(self):
        self.level+=1
        self.up_scor()

    def end_g(self):
        self.goto(0,0)
        self.write(f"Game Over!", align="center", font=FONT)