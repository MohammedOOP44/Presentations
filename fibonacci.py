class Mathclass:
    def __init__(self,last_result=None):
        self.__last_result = last_result

    def get_last_result(self):
        return self.__last_result
    
    def set_last_result(self,new_result):
        self.__last_result = new_result
        return self.__last_result
    
class fibonacci(Mathclass):
    def calculate(self,n):
        l = []
        a = 0
        b = 1
        for i in range(n):
            l.append(a)
            a,b = b,a+b
        return a
        
    
h = fibonacci()
print(h.calculate(20))
  

    

        