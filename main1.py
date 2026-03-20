from snake1 import Snake
from turtle import Turtle , Screen
window = Screen()
window.setup(800,800)
window.bgcolor("black")
window.title('SNAKE GAME')

peek = Snake()


#loop
game_on = True
while game_on :
    peek.move()

window.exitonclick()