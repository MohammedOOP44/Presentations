def evaluate_prefix(expression):
    char_stack = []
    int_stack = []

    for char in expression :
        if char != ' ':
            char_stack.append(char)

    while len(char_stack) > 0:
        current_char = char_stack.pop()

        if current_char.isdigit():
            int_stack.append(int(current_char))

        elif current_char in ['+','-','*','^','/']:
            op1 = int_stack.pop()
            op2 = int_stack.pop()

            if current_char == '+':
                result = op1 + op2
            elif current_char == '-':
                result = op1 - op2
            elif current_char == '^':
                result = op1 ^ op2
            elif current_char == '/':
                result = op1 / op2
            elif current_char == '*':
                result = op1 * op2

            int_stack.append(result)

    final_answer = int_stack.pop()
    return final_answer

test_expression = "+ - 1 2 5"
print(evaluate_prefix(test))
