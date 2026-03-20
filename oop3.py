import os
import time
new_members = []
def clear_screen():
    os.system('cls')
class Membership :
    def __init__(self,first_name,last_name,ID,status='inactive'):
        self.first_name = first_name
        self.last_name = last_name
        self.ID = ID
        self.status = status
    def members_display(self):
        print(f"first name: {self.first_name}")
        print(f"last name: {self.last_name}")
        print(f"ID: {self.ID}")
        print(f"status: {self.status}")
def create_membership():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    ID = input("Enter ID: ")
    status = input("Enter status (or click enter): ")
    if not status :
        status = 'inactive'
    return Membership(first_name,last_name,ID,status)

def search_members(new_members):
    clear_screen()
    found_members = []
    print("search by\n")
    print("1.ID")
    print("2.name")
    print("3.status\n")
    option = int(input("Enter your choice: "))
    print("_"*20)
    if option == 1:
        id = input("Enter the ID: ")
        for i in new_members:
            if id == i.ID:
                i.members_display()
                found_members.append(i)
    elif option == 2:
        name = input("Enter the name: ")
        for i in new_members :
            if name.lower() == i.first_name.lower() :
                i.members_display()
                found_members.append(i)
                

    elif option == 3:
        state = input ("Enter the status")
        for i in new_members:
            if state == i.status:
                i.members_display()
                found_members.append(i)
    else:
        print("invalid choice, please try again")

    if not found_members:
        print("sorry, the member isn't exist")
        time.sleep(2)

    
while True:
    print("\n___ welcome to GYM membership mangement ___\n")
    print("choose an action: \n")
    print("1.Add new member ")
    print("2.display all members")
    print("3.search for a member")
    print("4.Exit\n") 

    choice = int(input("Enter your choice: "))
    if choice == 1:
        clear_screen()
        new_members.append(create_membership())
        print("member added successfully")
        print("_"*20)
        time.sleep(2) 
    elif choice == 2 :
        clear_screen()
        
        if new_members:
            for i in new_members:
                i.members_display()
                time.sleep(1)
                print("_"*20)
        else:
            print("sorry, there no members yet")
            time.sleep(2)
    elif choice == 3:
        search_members(new_members)
    else :
        print("Exiting...")
        break


        

       
    

