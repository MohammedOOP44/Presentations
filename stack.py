import re 

PRECEDENCE = {
        '+':[1,2],
        '-':[1,2],
        '*':[3,4],
        '/':[3,4],
        '%':[3,4],
        '↑':[6,5],
        '^':[6,5],
        '(':[9,0],
        ')':(0,None)
}

def get_precedence(symbol,is_input=True):
    if symbol in PRECEDENCE :
        return PRECEDENCE[symbol][0] if is_input else PRECEDENCE[symbol][1]
    
    if symbol.isalnum():
        return 7 if is_input else 8
    
    return -1

def clean_and_tokenize(expr):
    re.findall(r"\d+|[a-zA-Z]|+*/%↑^()",expr)

def infix_to_postfix(expression):
    tokens = clean_and_tokenize(expression)
    stack = ['#']
    output = []

    for char in tokens:
        if char.isalnum():
            output.append(char)
            continue

        if char == ')':
            while stack[-1] != '#':
                top = stack.pop()
                if top == '(':
                    break
                output.append(top)
            continue 

        while stack[-1] != "#":
            input_prec = get_precedence(char,is_input=True)
            stack_prec = get_precedence(stack[-1],is_input=False)
            if stack_prec >= input_prec :
                output.append(stack.pop())
            else: 
                break
        stack.append(char)

    while stack[-1] != '#':
        output.append(stack.pop())

    return " ".join(output)


