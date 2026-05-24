class Matrix:
    def __init__(self,n,m):
        self.__data__ = []
        for i in range(n):
            self.__data__.append([])
            for j in range(m):
                self.__data__[i].append(float("nan"))

    def __str__(self):
        s = ""
        for row in self.__data__:
            s += "|"
            for item in row:
                s += " " + str(item) 
            s += " |\n"
        return s
    
    def printMat(self):
        print(self.__data__)

    def set(self,i,j,v):
        self.__data__[i-1][j-1] = v

    def __add__(self,other):
        if len(self.__data__) != len(other.__data__) or len(self.__data__[0]) != len(other.__data__[0]):
            raise TypeError("Can not add two matrices with different sizes!")
        
        M = Matrix(len(self.__data__),len(self.__data__[0]))
        for i in range(len(self.__data__)):
            for j in range(len(self.__data__[0])):
                M.set(i+1,j+1,self.__data__[i][j] + other.__data__[i][j])
        return M
    
    def transpose(self):
        n = len(self.__data__)
        m = len(self.__data__[0])
        M = Matrix(m,n)
        for i in range(m):
            for j in range(n):
                M.set(i+1,j+1,self.__data__[j][i])
        return M
    
    def __mul__(self,other):
        if type(other) != int and type(other) != float :
            raise TypeError("multiplication is defined on int and float only")
        n = len(self.__data__)
        m = len(self.__data__[0])
        M = Matrix(n,m)
        for i in range(n):
            for j in range(m):
                M.set(i+1,j+1,self.__data__[i][j]*other)
        return M
    
n = Matrix(4,5)
for i in range(4):
    for j in range(5):
        if i==j:
            n.set(i+1,j+1,1)
        else:
            n.set(i+1,j+1,0)

m = Matrix(4,5)
for i in range(4):
    for j in range(5):
        if i==j:
            m.set(i+1,j+1,1)
        else:
            m.set(i+1,j+1,0)

l = n+m
p = l.transpose()
q = p*3
print(n)
print(m)
print(l)
print(p)
print(q)
n *= 100
print(n)
