# Sierpinski Triangle
import turtle
import random

points = [[100, 200],[100, 0],[-100, 0]]
t =turtle.Turtle()
t.penup()
t.goto(points[0][0], points[0][1])
t.pendown()
t.goto(points[1][0], points[1][1])
t.goto(points[2][0], points[2][1])
t.goto(points[0][0], points[0][1])
t.penup()
t.speed(0)
p = points[0]
turtle.tracer(0)
for j in range(100):
    for i in range(100):
        t.goto(p)
        t.dot(size=2)
        r = random.randint(0, 2)
        p = [(points[r][0] + p[0])//2 , (points[r][1] + p[1])//2] 
    turtle.update()

turtle.done()