students = {
    1:{"name":"Ahmed", "age":20},
    2:{"name":"Ali", "age":22}
}
def print_student(students) :
    for ID, info in students.items():
        print("ID:", ID)
        for key, value in info.items():
            print(key.capitalize() ,":", value)
        print("--------")

print_student(students)
