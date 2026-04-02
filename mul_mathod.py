
m=[[1, 2, 3],[4, 5, 6]]
n=[[7, 8],[9, 10], [11, 12]]
class MyMatrix:
    def __init__(self,data):
        self.data = data
        

    def display(self):
        for i in self.data :
            print("|",*i,"|")
    
test = MyMatrix(m)
test.display()