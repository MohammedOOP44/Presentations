all_student = []
class User:
    def __init__(self,first_name,last_name,email,password,status="inactive"):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.status = status

    def users_display(self):
        print(f"first name: {self.first_name}")
        print(f"last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"password: {self.password}")
        

def add_user():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter the Email: ")
    password = input("Enter the password: ")

    new_student = User(first_name,last_name,email,password)
    return new_student

while(True):

    print("""
choose an action:
1.add an student
2.display all users
3.Exit
 
""")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        new1 = add_user()
        print("____________________________")
        new1.users_display()
        all_student.append(new1)
    elif choice == 2:
    
        for student in all_student:
            student.users_display()
    else:
        break

    