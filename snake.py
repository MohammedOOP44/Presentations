#Snake slass
#method: cereate snake()
#method: move snake()

from turtle import Turtle

class Snake:
    def __init__(self):
        self.turtles = []
        self.positions = [(-40,0),(-20,0),(0,0)]
        self.create_snake()

    def create_snake(self):
        for i in range(len(self.positions)):
            t = Turtle("square")
            t.color("white")
            t.penup()
            t.goto(self.positions[i])
            self.turtles.append(t)

    def move(self):
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.turtles[-1].forward(50)
        self.turtles[-1].left(90)
