from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
s = Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
s.title("pong")
s.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
score=Score()

s.listen()
s.onkey(r_paddle.go_to,"Up")
s.onkey(r_paddle.go_down,"Down")
s.onkey(l_paddle.go_to,"w")
s.onkey(l_paddle.go_down,"s")

end=True
while end:
    time.sleep(ball.mo_s)
    s.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()

    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.ycor()<-320:
        ball.boun_x()

    if ball.xcor()>380:
        ball.re_p()
        score.l_point()



    if ball.xcor()<-380:
        ball.re_p()
        score.r_point()

s.exitonclick()