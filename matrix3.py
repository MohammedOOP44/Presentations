class Matrix:
    def __init__(self,n,m):
        self.__data__ = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(0.0)
            self.__data__.append(row)

    def __str__(self):
        return "\n".join(
            "| " + " ".join(str(item) for item in row) +" |"
            for row in self.__data__
        )
    
    def get(self,i,j):
        return self.__data__[i-1][j-1]
    
    def set(self,i,j,v):
        self.__data__[i-1][j-1] = v

    def __add__(self,other):
        n = len(self.__data__)
        m = len(self.__data__[0])
        if n != len(other.__data__) or m != len(other.__data__[0]):
            raise ValueError("cannot add two matrix with different sizes")
        T = Matrix(n,m)
        for i in range(n):
            for j in range(m):
                T.set(i+1,j+1,self.__data__[i][j]+other.__data__[i][j])
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
        n = len(self.__data__)
        m = len(self.__data__[0])
        if isinstance(other,(int,float)):   
            T = Matrix(n,m)
            for i in range(n):
                for j in range(m):
                    T.set(i+1,j+1,self.__data__[i][j] * other)
            return T
        elif isinstance(other,Matrix):
            n = len(self.__data__)
            m = len(self.__data__[0])

            p = len(other.__data__)
            q = len(other.__data__[0])

            if m != p:
                raise ValueError("number of col in the first matrix must equal ")
    
            T = Matrix(n,q)
            for i in range(n):
                for j in range(q):

                    s = 0

                    for k in range(p):
                        s += self.__data__[i][k] * other.__data__[k][j]

                    T.set(i+1,j+1,s)

            return T 
        
N = Matrix(4,5)
for i in range(4):
    for j in range(5):
        if i == j :
            N.set(i+1,j+1,1)
        else:
            N.set(i+1,j+1,0)

M = Matrix(4,5)
for i in range(4):
    for j in range(5):
        if i == j :
            M.set(i+1,j+1,3)
        else:
            M.set(i+1,j+1,0)

print(N)
print("\n")
print(M)
print("\n")
print(M.transpose())