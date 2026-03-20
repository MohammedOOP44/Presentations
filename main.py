
from turtle import Turtle , Screen 
from snake import Snake
window = Screen()
window.setup(800,800)
window.bgcolor("black")
window.title("Snake Game")


sam = Snake()      # make object

# Loop
game_on = True
while game_on :
    sam.move( )


window.exitonclick()