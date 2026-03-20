from turtle import Turtle , Screen
import random
import time
windows = Screen()
windows.setup(width=800,height=800)
windows.bgcolor("black")
windows.tracer(0)

positions = [(-40,0),(-20,0),(0,0),(20,0),(40,0),(60,0)]
colors = ("red","white","cyan","green","orange","brown")
angles =  (90,0,0,0,0,0,0,0,0,0,0,0)
turtles = []

for i in range(len(positions)):
    t = Turtle("square")
    t.color("white")
    t.penup() 
    t.goto(positions[i])
    turtles.append(t)

game_on = True
while game_on:
    for i in range(len(positions)-1):
        turtles[i].goto(turtles[i+1].pos())
    turtles[-1].forward(20)
    turtles[-1].left(random.choice(angles))
    windows.update()
    time.sleep(0.1)
    


        

windows.exitonclick()