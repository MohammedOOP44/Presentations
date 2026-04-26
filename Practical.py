class Matrix :
    def __init__(self,data):
        self.data= data
        self.rows = len(data)
        self.col = len(data[0])

    def __add__(self,other):
        if self.rows != other.rows or self.col != other.col:
            raise ValueError("Dimensions must match for addition")
        
        result = []
        for i in range(self.rows):
            row = []

            for j in range(self.col):
                sum_val = self.rows[i][j] + other.col[i][j]
                row.append(sum_val)
            result.append(row)
        return result
    
    def __mul__(self, other):
        if self.col != other.row:
            raise ValueError("Invalid dimensions for multiplication! (col A != rows B)")
        
        for i in range(self.rows):
            row = []

            for j in range():
                



M = [(1,2,3),
     (4,5,6),
     (7,8,9)]
N = [(1,2,3),
     (4,5,6),
     (7,8,9)]
r = M + N 
print(r)