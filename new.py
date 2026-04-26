class Students:
    def __init__(self,ID,st_name=None,st_class=None):
        self.ID = ID
        self.st_name = st_name 
        self.st_class = st_class 

    def display_info(self):
        print(f"ID: {self.ID}")
        print(f"name: {self.st_name}")
        print(f"class: {self.st_class}")
def create_student():
    ID = int(input("Enter ID: "))
    st_name = input("Enter name: ")
    st_class = input("Enter class: ")
    if not st_name:
        st_name = None
    if not st_class:
        st_class = None

    return Students(ID,st_name,st_class)



student1 = create_student()
print("_"*20)
student1.display_info()