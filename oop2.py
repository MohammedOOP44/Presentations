import os
import time
new_user = []
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
class User :
    def __init__(self,first_name,last_name,email,password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email 
        self.password = password
    def users_display(self):
        print(f"first name: {self.first_name}")
        print(f"last name: {self.last_name}")
        print(f"email: {self.email}")
        print(f"password: {self.password}")
def create_user():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    print("___________________________________ ")
    return User(first_name,last_name,email,password)

while True :
    print("___ Welcom to user mangment ___\n")
    print("choose an Action :")
    print("1.Add new user")
    print("2.Display all users")
    print("3.Exit\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        new_user.append(create_user())
        print("user added successfully\n")
        time.sleep(2)
    elif choice == 2:
        clear_screen()
        if new_user:
            print("Displaying all users...")
            time.sleep(2)
            for i in new_user:
                i.users_display()
                print("_"*20)
                time.sleep(1)
        else:
            print("sorry, there didin't any user to display")
    else:
        print("Exiting...")
        break

            


        

    