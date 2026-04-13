class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self,amount):
        if amount > 0 :
            self.__balance += amount
            print(f"deposited ${amount}. new balance: {self.__balance}")
        else:
            print("Invalid amount!")
    
    def calculate_interest(self):
        return 0
    

class SavingAccount(BankAccount):
    def __init__(self,owner,balance=0):
        super().__init__(owner,balance)
        self.interest_rate = 0.05

    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        return interest
    


class CurrentAccount(BankAccount):
    def __init__(self,owner,balance=0):
        super().__init__(owner,balance)
        self.interest_rate = 0.01
        
    def calculate_interest(self):
        return self.get_balance() * 0.01

if __name__ == "__main__":

    saving = SavingAccount("mohammed",100)
    current = CurrentAccount("Ali",200)

    saving.deposit(10)
    current.deposit(10)

    for acc in [saving,current]:
        print(f"owner : {acc.owner}")
        print(f"balance : {acc.get_balance()}")
        print(f"Interest : {acc.calculate_interest():.2f}")









