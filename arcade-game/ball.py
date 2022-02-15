from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.mo_s=0.1

    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+ self.y_move
        self.goto(new_x,new_y)

    def bounce(self):
        self.y_move*=-1

    def boun_x(self):
        self.x_move*=-1
        self.mo_s *= 0.9

    def re_p(self):
        self.goto(0,0)
        self.mo_s=0.1
        self.boun_x()

