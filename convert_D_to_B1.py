def dicemal_to_binary(num):
    if num == 0:
        return 0
    
    stack = []

    while num > 0:
        digit = num % 2
        stack.append(digit)
        num = num // 2

    binary_string = ""

    while len(stack) > 0:
        digit = stack.pop()
        binary_string += str(digit)

    return binary_string

print(dicemal_to_binary(100))