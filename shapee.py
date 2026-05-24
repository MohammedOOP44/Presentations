import turtle 
import math

class Shape:
    def __init__(self,name,area=0):
        self.name = name
        self.__area__ = area

    def __str__(self):
        return self.name
    
    def area(self):
        return self.__area__
    
class Rect(Shape) :
    def __init__(self,name,length=0,width=0,x=0,y=0,color='black'):
        super().__init__(name,length*width)
        self.length = length 
        self.width = width 
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return "Rect: " + super().__str__() + " (" + str(self.__area__) + ")"
    
    def __mul__(self,k):
        t = Rect(self.name,self.length*k,self.width*k)
        return t
    
    def draw(self):
        t = turtle.Turtle()
        t.color(self.color)
        t.penup()
        t.goto(self.x,self.y)
        t.pendown()
        for i in range(2):
            t.forward(self.length)
            t.right(90)
            t.forward(self.width)
            t.right(90)
        
    def shift(self,change_x,change_y):
        self.x += change_x
        self.y += change_y

class Circle(Shape):
    def __init__(self,name,redius=0,x=0,y=0,color="black"):
        super().__init__(name,math.pi*redius**2)
        self.redius = redius
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return "circle: " + self.name + " (" + str(self.__area__) + ")"
    
    def __mul__(self,k):
        t = Circle(self.name,self.redius*k,20,20)
        return t       

    def draw(self):
        t = turtle.Turtle()
        t.color(self.color) 
        t.penup()
        t.goto(self.x,self.y)
        t.pendown()
        t.circle(self.redius)

r = Rect("field",100,50)
print(r)
r.draw()
r = r * 2
print(r)
r.shift(-100,-10)
r.color = "red"
r.draw()

c = Circle("roundabout",50)
print("\n\n" ,c)
c.draw()
c = c*5
print(c.area())
c.draw()




        