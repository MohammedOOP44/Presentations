def multiply_list(a,b):
    result = []
    for i in a :
        result.append(i*b)
    return result

list = [1,2,3]
n = 100
print(multiply_list(list,n))