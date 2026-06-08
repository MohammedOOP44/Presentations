import math 

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2
    
    def circumference(self):
        return 2 * math.pi * self.radius
    
    def scale(self,factor):
        self.radius *= factor

circle1 = Circle(5)
print(circle1.area())
print(circle1.circumference())
circle1.scale(2)
print(circle1.area())
