from turtle import Turtle 

class Snake:
    def __init__(self):
        self.squares = []
        self.coordinates = [(-40,0),(-20,0),(0,0)]
        self.create_square()

    def create_square(self):
        for i in range(len(self.coordinates)):
            t = Turtle("square")
            t.color("white")
            t.penup()
            t.goto(self.coordinates[i])
            self.squares.append(t)

    def move(self):
        for i in range(len(self.coordinates) - 1):
            self.squares[i].goto(self.squares[i+1].pos())
        self.squares[-1].forward(20)

    def up(self):
        self.squares[-1].setheading(90)
    def down(self):
        self.squares[-1].setheading(270)
    def right(self):
        self.squares[-1].setheading(0)
    def left(self):
        self.squares[-1].setheading(180)

        
