print("welcome electronic piggy bank")
balance = int(input("How much you have in The Piggy Bank: "))
amount = int(input("How much do want to save today"))
balance += amount
print(f"Done! your balance now is: {balance}")
withdraw = int(input("How much do you want to withdraw: "))
if withdraw <= balance : 
    withdraw -= balance 
    print(f"successfully withdraw , remaining balance {balance}")
else :
    print("Denied! you don't have enough money")
print(f"Final balance: {balance}")
