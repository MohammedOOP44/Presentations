balance = 0 
print("--- wellcome to the smart biggy bank ---")
while True :
    print(""" what you want to do today
          1.Deposit
          2.whithdraw
          3.exit  
          """)
    choice = int(input("enter your choice (1,2,3)"))
    if choice == 1 :
        deposit = int(input("Enter the amount you want to deposit: "))
        balance += deposit
    elif choice == 2 :
        withdraw = int(input("Enter the amount you want to withdraw: "))
        if withdraw <= balance:
            balance -= withdraw
        else :
            print("Denied! you don't have enough money")
    elif choice == 3:
        break
    else :
        print("invalid choice! please try again")
    print(f"your balance now is: {balance}")