import turtle
import random
t = turtle.Turtle()
points = [[0,1000],[500,0],[-500,0]]
t.penup()
t.goto(points[0][0] , points[0][1])
t.pendown()
t.goto(points[1][0],points[1][1])
t.goto(points[2][0],points[2][1])
t.goto(points[0][0] , points[0][1])
t.penup()
t.speed(0)
p = points[0]
turtle.tracer(0)
for i in range(100) :
    for j in range(100) :
        t.goto(p)
        t.dot(size=2)
        r = random.randint(0,2)
        p = []

