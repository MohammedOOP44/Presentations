from turtle import Turtle , Screen
import random

class Food:
    def __init__(self):
        pass

    def create_food(self):
        f = Turtle("circle")
        f.color("red")
        f.penup()
        f.goto(random.randint(1,800),random.randint(1,800))