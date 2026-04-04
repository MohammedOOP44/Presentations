for i in range(2,99):
    is_prime = True
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            break
        
    else:
        print(i)

        
