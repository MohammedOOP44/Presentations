from turtle import Screen 
from snake2 import Snake
from food2 import Food
from scoreboard2 import Score
import time
window = Screen()
window.setup(width=800,height=800) 
window.bgcolor("black")
window.title("Snake Game")
window.tracer(0)

   
tan = Snake()
food = Food()
score = Score()

game_on = True
while game_on :
    tan.move()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(tan.up,"Up")
    window.onkey(tan.down,"Down")
    window.onkey(tan.right,"Right")
    window.onkey(tan.left,"Left")
    if tan.head.distance(food) < 15 :
        food.appear()
        tan.extend()
        score.score_increase()
        score.update()

    if tan.head.xcor() > 370 or tan.head.ycor() > 370 or tan.head.xcor() < -370 or tan.head.ycor() < -370:
        score.game_over()
        game_on = False


window.exitonclick()