def is_prime(x):
        for j in range(2,int(x**0.5)+1):
            if x % j == 0:
                return False
            
        else:
            return True
        
for i in range(2,100):
    if is_prime(i):
        print(i)


        
