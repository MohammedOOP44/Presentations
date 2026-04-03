from turtle import Turtle , Screen 

window = Screen()
window.setup(width=1000,height=900)
window.bgcolor("black")

t = Turtle("turtle")
t.color("white")
t.pensize(3)
t.speed("fastest")

def draw_circles():
    t.penup()
    t.goto(-300,-300)
    t.pendown()
    for _ in range(10):
        t.circle(50)
        t.right(360/10)

def draw_squares():
    t.penup()
    t.goto(0,0)
    t.pendown()
    for _ in range(10):
        for _ in range(4):
            t.forward(60)
            t.left(90)
        t.left(360/10)

def draw_triangles():
    t.penup()
    t.goto(300,300)
    t.pendown()
    for _ in range(10):
        for _ in range(3):
            t.forward(100)
            t.left(120)
        t.left(360/10)


draw_circles()
draw_squares()
draw_triangles()

window.exitonclick()
