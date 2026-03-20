from datetime import date

class students:
    def __init__(self,radius,ingredients): #instance method
        self.radius = radius
        self.ingredients = ingredients

    def describe(self):
        print(f"my name is {self.__name}, and my age is {self.__age}")
    
    @classmethod                 #class method
    def initFromBirthYear(cls,name,BirthYear):
        return cls(name, date.today().year - BirthYear)
    



class Pizza :
    def __init__(self,radius,ingredients) :
        self.radius = radius
        self.ingredients = ingredients


    def __str__(self):
        return f"radius: {self.radius} , ingredients: {self.ingredients}"
    
    def area(self):
        return Pizza.circle_area(self.radius)
    
    @staticmethod
    def circle_area(r):
        pi = 3.14
        return r**2 * pi
    
    
    
pizza1 = Pizza(7,["egg","tommato","dough"])
print(pizza1)
print(Pizza.circle_area(7))