import math

class MathOperation:
    def __init__(self,operation_type):
        self.operation_type = operation_type

    def describe(self):
        return f"this a generic {self.operation_type} operation"
    
class Fraction(MathOperation):
    def __init__(self,numerator,denominator):
        super().__init__(operation_type='fraction')

        if denominator == 0 :
            raise ZeroDivisionError("Denominator can not be zero")
        
        self.__numerator = numerator
        self.__denominator = denominator

        self.__simplify()

        

    def __simplify(self):
        common_divisor = math.gcd(self.__numerator,self.__denominator)
        self.__numerator //= common_divisor 
        self.__denominator //= common_divisor

        if self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator

    # Getters (to access private attributes safely if needed)
    @property
    def numerator(self):
        return self.__numerator
    
    @property
    def denominator(self):
        return self.__denominator 
    
    # 3. Polymorphism / Method Overriding
    # Overriding the 'describe' method from MathOperation
    def describe(self):
        return f"this fraction object representing {self.__str__()}"
    
    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"
    
    def __add__(self,other):
        new_num = (self.__numerator * other.denominator) + (other.numerator * self.__denominator)
        new_den = self.__denominator * other.denominator
        return Fraction(new_num,new_den)
    
    def __sub__(self,other):
        new_num = (self.__numerator * other.denominator) - (other.numerator * self.__denominator)
        new_den = self.__denominator * other.denominator 
        return Fraction(new_num,new_den)
    
    def __mul__(self,other):
        new_num = self.__numerator * other.numerator
        new_den = self.__denominator * other.denominator  
        return Fraction(new_num,new_den)
    
    def __truediv__(self,other):
        if other.numerator == 0:
            raise ZeroDivisionError("cannot divide by a fraction equal to zero")
        new_num = self.__numerator * other.denominator
        new_den = self.__denominator * other.numerator
        return Fraction(new_num,new_den)
    
    
f1 = Fraction(1,2)
f2 = Fraction(5,8)


print("--- Testing Basic Operations & Special Methods ---")
print(f"fraction 1: {f1}")
print(f"fraction 2: {f2}")
print(f"Addition ({f1} + {f2}): {f1+f2}")
print(f"subtraction ({f1} - {f2}): {f1-f2}")
print(f"multiplication ({f1} * {f2}): {f1*f2}")
print(f"division ({f1} / {f2}): {f1/f2}")


print("\n--- Testing Polymorphism / Method Overriding ---")
generic_op = MathOperation("Basic Arthmatic")
print(generic_op.describe())
print(f1.describe())


print("\n--- 5. List of Objects & Iteration ---")
fraction_list = {
    Fraction(3,4),
    Fraction(7,1),
    Fraction(8,2),
    Fraction(1,3)
}

running_total = Fraction(0,1)
for frac in fraction_list :
    print(f"- {frac}")
    running_total += frac


print(f"total sum of the list: {running_total}")





