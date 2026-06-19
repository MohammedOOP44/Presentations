def decimal_to_binary(num):
    if num == 0:
        return 0
    
    stack = []

    while num > 0:
        digit = num % 2       # 3.1 Get remainder
        stack.append(digit)   # 3.2 Push digit into stack
        num = num // 2        # 3.5 Divide number by 2 (using integer division)


    return "".join(str(stack.pop()) for _ in range(len(stack)))

result = decimal_to_binary(4)
print(result)
