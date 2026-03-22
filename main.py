
from turtle import Turtle , Screen 
from snake import Snake
from food import Food
import time
window = Screen()
window.setup(800,800)
window.bgcolor("black")
window.title("Snake Game")
window.tracer(0)


sam = Snake()      # make object
food = Food()


# Loop
game_on = True
while game_on :
    sam.move()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(sam.up,"Up")
    window.onkey(sam.down,"Down")
    window.onkey(sam.right,"Right")
    window.onkey(sam.left,"Left")

    if sam.head.distance(food) < 15:
        food.appear()
        sam.extend()


window.exitonclick()