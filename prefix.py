def evaluate_prefix(expression):
    char_stack = []
    int_stack = []

    for char in expression :
        if char != ' ':
            char_stack.append(char)

    while len(char_stack) > 0:
        current_char = char_stack.pop()

        if current_char.isdigit():
            # Push into the integer stack (we convert the string to an actual integer)
            int_stack.append(int(current_char))

        elif current_char in ['+','-','*',"^",'/']:
            # Pop a number from integer stack and assign it to op1
            op1 = int_stack.pop()

            # Pop another number from integer stack and assign it to op2
            op2 = int_stack.pop()

            # Calculate op1 op op2
            if current_char == '+':
                result = op1 + op2
            elif current_char == '-':
                result = op1 - op2
            elif current_char == '*':
                result = op1 * op2
            elif current_char == '/':
                result = op1 / op2
            elif current_char == '^':
                result = op1 ^ op2

            # Push the output into the integer stack
            int_stack.append(result)

    # Step 3: Pop the result from the integer stack and display the result
    final_result = int_stack.pop()
    return final_result 

test_expression = "* + 2 3 4"
answer = evaluate_prefix(test_expression)
print(f"the result of the prefix expression '{test_expression}' is: {answer}")
    
