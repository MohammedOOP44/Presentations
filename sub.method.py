
class BankAccount:
    def __init__(self,balance):
        self.balance = balance
# isinstance(الشيء, النوع)
    def __sub__(self,other):
        if isinstance(other,BankAccount):
            return BankAccount(self.balance - other.balance)
        elif isinstance(other,int):
            return BankAccount(self.balance - other)
        else :
            return NotImplemented
        
        
    def __mul__(self,other):
        if isinstance(other,BankAccount):
            return BankAccount(self.balance * other.balance)
        elif isinstance(other,int):
            if other < 0:
                raise ValueError("No negative numbers allowed")
            return BankAccount(self.balance * other)
        else :
            return NotImplemented

    
    def __str__(self):
        return f"Balance: {self.balance}"
    
    def __add__(self,other):
        if isinstance(other,BankAccount):
            return BankAccount(self.balance + other.balance)
        elif isinstance(other,int):
            if other < 0:
                raise ValueError("No negative numbers allowed")
            return BankAccount(self.balance + other)
        else:
            return NotImplemented
        
print("___Welcome to Bank Account___")
print("choose the operations ya wanna:")
print("1.")
print("2.")
print("3.")
    
acc1 = BankAccount(100)
acc2 = acc1 + 44

print(acc2)
