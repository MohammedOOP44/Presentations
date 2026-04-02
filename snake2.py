from turtle import Turtle
class Snake :
    def __init__(self):
        self.turtles = []
        self.coordinates = [(-40,0),(-20,0),(0,0)]
        self.create_turtles()
        self.head = self.turtles[-1]

    def create_turtles(self):
        for i in range(len(self.coordinates)):
            t = Turtle("square")
            t.color("white")
            t.penup()
            t.goto(self.coordinates[i])
            self.turtles.append(t)

    def move(self):
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.head.forward(20)

    def extend(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        
        self.turtles.insert(0,new_segment)
        
        

    def up(self):
        self.head.setheading(90)
    def down(self):
        self.head.setheading(270)
    def right(self):
        self.head.setheading(0)
    def left(self):
        self.head.setheading(180)

    