import math
from turtle import Turtle

class Shape:
    def __init__(self,name,length):
        self.name = name
        self.length = length

class Rect(Shape):
    def __init__(self,name,length=0,width=0,x=0,y=0):
        super().__init__(name,length*width)
        self.length = length
        self.width = width

        def __str__(self):
            return "Rect: " + super().__str__() + str(self.__erea__) 
        
        def __mul__(self,k):
            k = Rect(name)

    
class Circle(Shape):
    def __init__(self,name,rad=0):
        super().__init__(name,math.pi*rad**2)
        self.rad = rad

r = Rect()

c = Circle("roundabout",50)
print(c)
print(c.area())

