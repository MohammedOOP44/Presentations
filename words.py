import turtle
lis = [[0,0],[6,8],[3,4],[0,6],[5,0],[9,9],[4,2],[7,8],[1,1],[5,5]]
t = turtle.Turtle()
t.penup()
for point in lis :
    x, y = point
    t.goto(x,y)
    t.pendown()
turtle.done()




