
class Point:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 

    def __sub__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x - other.x, self.y - other.y)
    
p1 = Point(99,18)
p2 = 4 
p3 = p1 - p2
print(p3.x,p3.y)