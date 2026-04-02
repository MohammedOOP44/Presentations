import random
from turtle import Turtle 
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(0.5)
        self.appear()
        

    def appear(self):
        x = random.randint(-350,350)
        y = random.randint(-350,350)
        self.goto(x,y)
