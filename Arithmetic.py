import math
class Math:
    def __init__(self,last_result=None):
        self.__last_result = last_result

    def get_last_result(self):
        return self.__last_result
    
    def set_last_result(self,new_result):
        self.__last_result = new_result
        return self.__last_result
    
class PrimeCheck(Math):
    def calculate(self,num):
        if num < 2 :
            return self.set_last_result(False)
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                return self.set_last_result(False)
        return self.set_last_result(True)
    
num = PrimeCheck()
print("Is 17 prime? ",num.calculate(17))
    


