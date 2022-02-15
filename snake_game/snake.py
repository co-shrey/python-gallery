from turtle import  Turtle
POSITION=[(0, 0), (-20, 0), (-40, 0)]
MOVE_D = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.seg = []
        self.create_snake()
        self.head=self.seg[0]

    def create_snake(self):
        for po in POSITION:
            self.add_s(po)

    def add_s(self,po):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(po)
        self.seg.append(t)

    def extend(self):
        self.add_s(self.seg[-1].position())

    def move(self):

            for i in range(len(self.seg) - 1, 0, -1):
                new_x = self.seg[i - 1].xcor()
                new_y = self.seg[i - 1].ycor()

                self.seg[i].goto(new_x, new_y)
            self.head.forward(MOVE_D)


    def up(self):
        if self.head.heading()!= DOWN:
             self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
           self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


