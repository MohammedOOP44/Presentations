
class BankAccount:
    def __init__(self,balance):
        self.balance = balance
# isinstance(الشيء, النوع)
    def __sub__(self,other):
        if isinstance(other,BankAccount):
            return BankAccount(self.balance - other.balance)
        elif isinstance(other,int):
            return BankAccount(self.balance - other)
    
    def __str__(self):
        return f"Balance: {self.balance}"
    

acc1 = BankAccount(100)
acc2 = acc1 - 90

print(acc2)
