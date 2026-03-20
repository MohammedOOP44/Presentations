 
def is_sqaure(num):
    root = (num)**0.5
    return root == int(root) 


num = int(input("Enter the number: "))
print(is_sqaure(num))
