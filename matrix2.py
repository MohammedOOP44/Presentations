class Matrix:
    def __init__(self,n,m):
        self.__data__ = []
        for i in range(n):
            self.__data__.append([])
            for j in range(m):
                self.__data__[i].append(float('nan'))

    def __str__(self):
        s = ''
        for row in self.__data__:
            s = s + '|'
            for item in row:
                s += ' ' + str(item)
            s = s + " |\n"
        return s

    def printMat(self):
        print(self.__data__)

    def set(self,i,j,v):
        self.__data__[i-1][j-1] = v

    def __add__(self,other):
        n = len(self.__data__)
        m = len(self.__data__[0])
        if n != len(other.__data__) or m != len(other.__data__[0]):
            raise TypeError("can not add two matrix with different sizes!")
        T = Matrix(n,m)
        for i in range(n):
            for j in range(m):
                T.set(i+1,j+1,self.__data__[i][j] + other.__data__[i][j])
        return T
    
    def transpose(self): 
        n = len(self.__data__)  
        m = len(self.__data__[0]) 
        T = Matrix(m,n)
        for i in range(m):
            for j in range(n):
                T.set(i+1,j+1,self.__data__[j][i])

        return T
    
    def __mul__(self,other):
        if not isinstance(other,(int,float)):  # other must be a number
            raise TypeError("multiplication is defined on int and float only!")
        n = len(self.__data__)
        m = len(self.__data__[0])
        T = Matrix(n,m)
        for i in range(n):
            for j in range(m):
                T.set(i+1,j+1,self.__data__[i][j] * other)
        return T
    
    def get(self,i,j):
        return self.__data__[i-1][j-1]

N = Matrix(4,5)
for i in range(4):
    for j in range(5):
        if i == j: 
            N.set(i+1,j+1,1)
        else:
            N.set(i+1,j+1,0)

M = Matrix(4,5)
for i in range(4):
    for j in range(5):
        if i == j :
            M.set(i+1,j+1,1)
        else:
            M.set(i+1,j+1,0)


print(N)
print(M)
print(N + M)
print(N * 3)
print(N.transpose())


