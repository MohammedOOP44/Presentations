def dicimal_to_binary(num):
    if num == 0:
        return 0
    
    stack = []
    while num > 0 :
        digit = num % 2 
        stack.append(digit)
        num //= 2

    return "".join(str(stack.pop()) for _ in range(len(stack)))

print(dicimal_to_binary(5))