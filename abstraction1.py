from abc import ABC , abstractmethod

class Person(ABC):
    def __init__(self,name, age ):
        self.name = name
        self.age = age

    @abstractmethod
    def get_role(self):
        pass # returns the role of the person

    @abstractmethod
    def show_details(self):
        pass # displays details of the person

class Student(Person):
    def __init__(self,name,age,student_id,major):
        super().__init__(name,age)
        self.student_id = student_id
        self.major = major

    def __repr__(self):
        return f"name: {self.name}, age: {self.age}, ID: {self.student_id}, major: {self.major}"

    def get_role(self):
        return "student"
    
    def show_details(self):
        return str(self)

class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject = subject

    def __str__(self):
        return f"name: {self.name}, age: {self.age}, subject: {self.subject}"
        
    def get_role(self):
        return "teacher"
    
    def show_details(self):
        return str(self)
    
class Course:
    def __init__(self,course_name,course_code,teacher):
        self.course_name = course_name
        self.course_code = course_code
        self.teacher = teacher 
        self.students = []

    def add_student(self,student):
        self.students.append(student)
        
    def show_course_details(self):
        return f"course_name: {self.course_name},course_code: {self.course_code},teacher: {self.teacher},students_enrolled: {self.students}"
    

teacher1 = Teacher("Ahmed",90,"math")

student1 = Student("mohammed",18,1,"big_data")
student2 = Student("Ali",19,2,"engineering_aplication")

course = Course("python","111",teacher1)

course.add_student(student1)
course.add_student(student2)

print(teacher1.show_details())
print(student1.show_details())
print(student2.show_details())
print(course.show_course_details())







