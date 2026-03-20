def is_prime(num) :
    check = 1
    if num<= 1 :
        check = 0
    else:
        for i in range (2,num):
            if num%i == 0:
                check = 0
                break
            
    if check == 1:
        return True
    else:
        return False
num = int(input("Enter n:"))   
if is_prime(num):
    print("it's a prime number")
else :
    print("it's not a prime number")

print(ord('A'))
