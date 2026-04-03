
m=[[1, 2, 3],[4, 5, 6]]
n=[[7, 8],[9, 10], [11, 12]]
class MyMatrix:
    def __init__(self,data):
        self.data = data
        

    def display(self):
        for i in self.data :
            print("|",*i,"|")

    def __add__(self,other):
        new_data = []

        for i in range(len(self.data)):
            new_row = []

            for j in range(len(self.data[0])):
                sum_val = self.data[i][j] + other.data[i][j]
                new_row.append(sum_val)

            new_data.append(new_row)
        return MyMatrix(new_data)
    
    def __mul__(self,other):
        if isinstance(other,MyMatrix):
            result_arr = []

            for i in range(len(self.data)):
                row = []

                for j in range(len(other.data[0])):
                    total = 0

                    for k in range(len(other.data)):
                        total += self.data[i][k] * other.data[k][j]

                    row.append(total)

                result_arr.append(row)
            return MyMatrix(result_arr)
        
        else:
            result_arr = []
            for row in self.data:
                result_arr.append([x * other for x in row])
            return MyMatrix(result_arr)
        
    def __rmul__(self,other):
        return self.__mul__(other)
    

# --- (Testing Ground) ---
m = MyMatrix(m)
n = MyMatrix(n)

(m + m).display()
(m * n).display()
(4*n).display()
