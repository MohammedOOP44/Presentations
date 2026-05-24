
class Matrix:
    def __init__(self,data):
        self.data = data
        self.row = len(data)
        self.col = len(data[0])

    def __str__(self):
        result = ""
        for r in self.data:
            result += str(r) + "\n"
        return result 

    def __mul__(self,other):
        if isinstance(other , int):
            new_data = []

            for i in range(self.row) :
                new_row = []

                for j in range(self.col):
                    new_row.append(self.data[i][j] * other)
                new_data.append(new_row)
            return Matrix(new_data)
        
        elif isinstance(other,Matrix):
            new_data = []

            for i in range(self.row):
                new_row = []

                for j in range(other.col):
                    cell_sum = 0
                    for k in range(self.col):
                        cell_sum += (self.data[i][k] * other.data[k][j]) 
                    new_row.append(cell_sum)
                new_data.append(new_row)
            return Matrix(new_data)
        
    def __rmul__(self,other):
        return self.__mul__(other)
        
    def __add__(self,other):
        if isinstance(other,int):
            new_data = []
            for i in range(self.row):
                new_row = []

                for j in range(self.col):
                    new_row.append(self.data[i][j] + other)
                new_data.append(new_row)
            return Matrix(new_data)
        
        elif isinstance(other,Matrix):
            new_data = []

            for i in range(self.row):
                new_row = []

                for j in range(other.col):
                    sum_val = self.data[i][j] + other.data[i][j]
                    new_row.append(sum_val)
                new_data.append(new_row)
            return Matrix(new_data)
                    
            
m = Matrix([[1, 2, 3], [4, 5, 6]])
n = Matrix([[7, 8], [9, 10], [11, 12]])

print(m*n)
print(m+m)





