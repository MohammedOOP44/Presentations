from abc import ABC , abstractmethod

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

    def __repr__(self):
        return f"name: {self.name},age: {self.age},student_id: {self.student_id},major: {self.major}"

    def get_role(self):
        return "STUDENT."
    
    def show_details(self):
        return str(self)
    
class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject = subject

    def __str__(self):
        return f"name: {self.name},age: {self.age},subject: {self.subject}"

    def get_role(Person):
        return "TEACHER."
    
    def show_details(self):
        return str(self)

class Course :
    def __init__(self,course_name, course_code, teacher):
        self.course_name = course_name
        self.course_code = course_code
        self.teacher = teacher
        self.students = []

    def add_student(self,st):
        self.students.append(st)

    def show_course_details(self):
        return f"course name: {self.course_name},course code: {self.course_code},TEACHER: {self.teacher},STUDENT_ENROLLED: {self.students}"

teacher1 = Teacher("Haider",100,"IT")

student1 = Student('Ahmed',23,1001,'Big Data')
student2 = Student('Mohammed',11,1002,"Enginering application")

course1 = Course("Bython",1221,teacher1)

course1.add_student(student1)
course1.add_student(student2)

print(course1.show_course_details())



