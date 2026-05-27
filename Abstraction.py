from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,name,age):
        self.name = name 
        self.age = age

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def show_details(self):
        pass

class Student(Person):
    def __init__(self,name,age,student_id,major):
        super().__init__(name,age)
        self.student_id = student_id
        self.major = major 

    def __str__(self):
        return f"name: {self.name},age: {self.age},ID: {self.student_id},major: {self.major}"

    def get_role(self):
        return "STUDENT"
    
    def show_details(self):
        return str(self)

class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject = subject

    def __str__(self):
        return f"name: {self.name},age: {self.age},subject: {self.subject}"
    
    def get_role(self):
        return "TEACHER"
    
    def show_details(self):
        return str(self)
    
class Course:
    def __init__(self,course_name,course_code,teacher):
        self.course_name = course_name
        self.course_code = course_code
        self.teacher = teacher
        self.students = []

    def __str__(self):
        return f"course: {self.course_name},course_code: {self.course_code},teacher: {self.teacher},students_enrolled: {self.students}"

    def add_student(self,student):
        self.students.append(student)
        
    def show_course_details(self):
        output = f"course: {self.course_name},course_code: {self.course_code},teacher: {self.teacher}\n"
        output += "students_enrolled\n"

        for student in self.students:
            output += f"{student}\n"
        return output 
    

teacher1 = Teacher("Adel",55,"scince")

student1 = Student("Mohammed",19,1,"Big Data")
student2 = Student("Ali",18,2,"Engineering application")

course1 = Course("python",111,teacher1)

course1.add_student(student1)
course1.add_student(student2)

#print(teacher1.show_details())
#print(student1.show_details())
#print(student2.show_details())
print(course1.show_course_details())