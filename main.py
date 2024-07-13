from turtle import Screen
import time
from snake import Snake
from food import Food
from score import ScoreBoard

X=280

sc=Screen()
sc.setup(width=600,height=600)
sc.bgcolor('black')
sc.title('Snake Game')
sc.tracer(0)

snake=Snake()
food=Food()
scoreBoard=ScoreBoard()

sc.listen()
sc.onkey(snake.up,'Up')
sc.onkey(snake.dwn,'Down')
sc.onkey(snake.lft,'Left')
sc.onkey(snake.rht,'Right')

game_on=True
while game_on:
    sc.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        scoreBoard.inc_score()
        snake.extend_snake()
        food.reloc_food()

    if snake.head.xcor()>X or snake.head.xcor()<-X or snake.head.ycor()>X or snake.head.ycor()<-X:
        # game_on=False
        scoreBoard.reset_score()
        snake.reset_snake()

    for seg in snake.segments[1:]:
        # if snake.head.distance(seg)<10 and seg!=snake.head:
        if snake.head.distance(seg)<10:
            # game_on=False
            scoreBoard.reset_score()
            snake.reset_snake()

sc.exitonclick()