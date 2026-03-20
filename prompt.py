def added_matrix(A,B,c):
    for row_a,row_b in zip(A,B):
        new_row = []
        for x,y in zip(row_a,row_b):
            new_row.append(x+y)
        c.append(new_row)
    return c
        
A = [[1,2],[3,4]]
B = [[5,6],[7,100]]
c = []
print(added_matrix(A,B,c))