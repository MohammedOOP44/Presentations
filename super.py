class shape:
    def __init__(self,color,filled):
        self.color = color 
        self.filled = filled

    def describe(self):
        print(f"color: {self.color}, is_filled: {"fiiled" if self.filled else "not filled"}")

class circle(shape):
    def __init__(self,color,filled,radius):
        super().__init__(color,filled)
        self.radius = radius

    def describe(self):
        print(f"it is the circle with an area of {3.14 * self.radius**2}")
        super().describe()

class square(shape):
    def __init__(self,color,filled,width):
        super().__init__(color,filled)
        self.width = width

    def describe(self):
        print(f"it is the square with an area of {self.width * self.width}")
        super().describe()


class triangle(shape):
    def __init__(self,color,filled,width,hight):
        super().__init__(color,filled)
        self.width = width
        self.hight = hight

    def describe(self):
        print(f"it is the triangle with an area of {self.width * self.hight}")
        super().describe()


circle1 = circle("red",True,5)
square1 = square("blue",False,12)
triangle1 = triangle("orange",True,44,88)

circle1.describe(  )


    