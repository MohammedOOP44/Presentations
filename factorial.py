class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return f"stack: {self.stack}"

    def push(self,element):
        self.stack.append(element)
        return self.stack

    def pop(self):
        if self.is_empty():
            return "stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.stack[-1]
    
    def peep(self,i):
        top = len(self.stack)
        if top-i+1 <= 0:
            return "underflow, stack is not that deep"
        peep = self.stack[top-i]
        return peep

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.stack)
    
mystack = Stack()
mystack.push(9)
mystack.push(3)
mystack.push(32)
print(mystack)
print(mystack.peek())
mystack.pop()
print(mystack)
print(mystack.size())
print(mystack.peek())


