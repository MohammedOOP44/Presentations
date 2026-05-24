import matplotlib.pyplot as plt

class Vector:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @x.setter
    def x(self,value):
        self.__x = value

    @y.setter
    def y(self,value):
        self.__y = value

    def __str__(self):
        return f"<{self.__x},{self.__y}>"
    
    def draw(self):
        plt.quiver(0,0 , self.__x,self.__y , angles="xy" , scale_units="xy" , scale=1)
        plt.xlim(-10,10)
        plt.ylim(-10,10)
        plt.axhline(0)
        plt.axvline(0)
        plt.grid()
        plt.show()

    def __mul__(self,scalar):
        return Vector(self.__x * scalar , self.__y * scalar)
    
    def __add__(self,other):
        return Vector(self.__x + other.x , self.__y + other.y)
    
v1 = Vector(3,6)
v2 = Vector(7,10)

print(v1)
print(v2)

print(v1*3)
print(v1+v2)

(v1*3).draw()