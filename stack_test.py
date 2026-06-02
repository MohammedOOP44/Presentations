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
    ')':[0,None]
}

def get_precedence(symbol,is_input=True):
    if symbol in PRECEDENCE: 
        return PRECEDENCE[symbol][0] if is_input else PRECEDENCE[symbol][1]
    if symbol.isalnum():
        return 7 if is_input else 8
    return -1

def clean_and_tokenize(expr):
    return re.findall(r'\d+|[a-zA-Z]|[+*/%↑^()]',expr)

def infix_to_postfix(expression):
    tokens = clean_and_tokenize(expression)
    stack = ['#']
    output = []
    for token in tokens:
        # ── Operand ──────────────────────────────────────────────────────────
        if token.isalnum():
            output.append(token)
            continue

        # ── Right parenthesis ─────────────────────────────────────────────────
        if token == ')':
            while stack[-1] != '#':
                top = stack.pop()
                if top == '(':
                    break
                output.append(top)
            continue 

        # ── Operator ──────────────────────────────────────────────────────────
        while stack[-1] != '#':
            input_prec = get_precedence(token,is_input=True)
            stack_prec = get_precedence(stack[-1],is_input=False)
            if stack_prec >= input_prec :
                output.append(stack.pop())
            else:
                break 
        stack.append(token)

    # Drain the remaining stack 
    while stack[-1] != '#':
        output.append(stack.pop())

    return ' '.join(output)
    
def postfix_to_infix(expression):
    tokens = expression.split() if ' ' in expression else clean_and_tokenize(expression)
    stack = []

    for token in tokens :
        if token.isalnum():
            stack.append(token)
        else :
            if len(stack) < 2 :
                return "Error: malformed postfix expression"
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(f"{op1} {token} {op2}")

    return stack[0] if stack else ''

def postfix_to_prefix(expression):
    tokens = expression.split() if ' ' in expression else clean_and_tokenize(expression)
    stack = []

    for token in tokens :
        if token.isalnum():
            stack.append(token)

        else :
            if len(stack) < 2:
                return "Error: malformed postfix expression"
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(f"{token} {op1} {op2}")

    return stack[0] if stack else ''

def prefix_to_postfix(expression):
    tokens = expression.split() if ' ' in expression else clean_and_tokenize(expression)
    tokens.reverse()   # process right-to-left
    stack = []

    for token in tokens :
        if token.isalnum():
            stack.append(token)
        else :
            if len(stack) < 2:
                return "Error: malformed prefix expression"
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(f"{op1} {op2} {token}")

    return stack[0] if stack else ''

def prefix_to_infix(expression):
    tokens = expression.split() if ' ' in expression else clean_and_tokenize(expression)
    tokens.reverse()
    stack = []

    for token in tokens:
        if token.isalnum():
            stack.append(token)

        else : 
            if len(stack) < 2:
                return "Error: malformed prefix expression"
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(f"{op1} {token} {op2}")
    return stack[-1] if stack else ''

def main():
    print("=== Mathematical Expression Notation Converter ===")
    print("Notation types:")
    print("  1. Infix   - the usual form,   e.g.  A + B")
    print("  2. Postfix - operands first,   e.g.  A B +")
    print("  3. Prefix  - operator first,   e.g.  + A B")

    try : 
        from_type = int(input("select the notation of your INPUT expression (1-3): "))
        expr = input("Enter the Expression: ")
        to_type = int(input("convert to which notation? (1: Infix, 2: Postfix, 3: Prefix):"))

    except ValueError :
        print("Please enter valid integers for the notation choices.")
        return 

    if from_type == to_type :
        print(f"\nResult: The expression is already in the requested notation: {expr}")
        return

    print("\n" + "=" * 40)
    
    # ── From Infix ────────────────────────────────────────────────────────────
    if from_type == 1:
        postfix = infix_to_postfix(expr)
        if to_type == 2:
            print(f"Postfix result : {postfix}")
        elif to_type == 3:
            prefix = postfix_to_prefix(postfix)
            print(f"Prefix  result : {prefix}")
    
    # ── From Postfix ──────────────────────────────────────────────────────────
    elif from_type == 2:
        if to_type == 1:
            print(f"Infix   result : {postfix_to_infix(expr)}")
        elif to_type == 3:
            print(f"Prefix  result : {postfix_to_prefix(expr)}")
    
    # ── From Prefix ───────────────────────────────────────────────────────────
    elif from_type == 3:
        if to_type == 1:
            print(f"Infix   result : {prefix_to_infix(expr)}")
        elif to_type == 2:
            print(f"Postfix result : {prefix_to_postfix(expr)}")
    
    else:
        print("Invalid notation choice. Please choose 1, 2, or 3.")
    
    print("=" * 40)
 
main()







