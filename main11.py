from snake11 import Snake
from turtle import Turtle , Screen
import time

window = Screen()
window.setup(800,800)
window.bgcolor("black")
window.title("SNAKE GAME")
window.tracer(0)

seeb = Snake()

game_on = True 
while game_on :
    seeb.move()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(seeb.up,"Up")
    window.onkey(seeb.down,"Down")
    window.onkey(seeb.right,"Right")
    window.onkey(seeb.left,"Left")
  