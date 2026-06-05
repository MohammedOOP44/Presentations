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

    def get_role(self):
        return "STUDENT."
    
    def show_details(self):
        return f"name: {self.name},age: {self.age},student_id: {self.student_id},major: {self.major}"
    
class teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject = subject

    def get_role(Person):
        return "TEACHER."
    
    def show_details(self):
        return f"name: {self.name},age: {self.age},subject: {self.subject}"

class course :
    def __init__(self,course_name, course_code, teacher):
        self.course.name = course_name
        self.course_code = course_code
        self.teacher = teacher
        self.students = []

    def add_student(self,st_name):
        self.students.append(st_name)

    def show_course_details(self):
        
