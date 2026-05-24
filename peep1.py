def peep(self,i):
    if i > len(self.stack) or i<0:
        return "Underflow"
    return self.stack[-i]
