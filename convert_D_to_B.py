def decimal_to_binary(num):
    if num == 0:
        return 0
    
    stack = []

    while num > 0:
        digit = num % 2       # 3.1 Get remainder
        stack.append(digit)   # 3.2 Push digit into stack
        num = num // 2        # 3.5 Divide number by 2 (using integer division)

    binary_string = ""

    while len(stack) > 0:
        digit = stack.pop()
        binary_string += str(digit)

    return binary_string 

result = decimal_to_binary(4)
print(result)
