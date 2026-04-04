m=[[1, 2, 3],[4, 5, 6]]
n=[[7, 8],[9, 10], [11, 12]]
class Matrix:
    def __init__(self,data):
        self.data = data

    def display(self):
        for i in self.data:
            print('|',*i,'|')

    def __add__(self,other):
        if isinstance(other,Matrix):
            new_data = []
            for i in range(len(self.data)):
                row = []

                for j in range(len(self.data[0])):
                    result = self.data[i][j] + other.data[i][j]
                    row.append(result)
                new_data.append(row)
            return Matrix(new_data)

        elif isinstance(other,int):
            new_data = []

            for i in range(len(self.data)):
                row = []

                for j in range(len(self.data[0])):
                    result = self.data[i][j] + other
                    row.append(result)
                new_data.append(row)
            return Matrix(new_data)

        else:
            return NotImplemented
        
m_list = Matrix(m)
n_list = Matrix(n)
(m_list + m_list).display()
        

