from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
s=Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("snake game")


s.tracer(0)
snake=Snake()
food=Food()
score=Score()
s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")
end = True
while end:
        s.update()
        time.sleep(0.1)
        snake.move()
        if snake.head.distance(food)<15:
                food.refresh()
                snake.extend()
                score.increase_score()


        if snake.head.xcor()>280 or snake.head.xcor()<-280  or snake.head.ycor()>280 or snake.head.xcor()<-280:
                end=False
                score.g_over()

        for segm in snake.seg:
                if segm==snake.head:
                        pass
                elif snake.head.distance(segm)<10:
                        end=False
                        score.g_over()












s.exitonclick()