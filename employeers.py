class Employeer:
    def __init__(self,id,name,salary,department):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department

    def calculate_emp_salary(self,salary,hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            Overtime_amount = (overtime * (salary/50))
            return self.salary + Overtime_amount
        return self.salary

    def emp_assign_department(self,new_department):
        self.department = new_department
        return self.department

    def print_employee_details(self):
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"salary: {self.salary}")
        print(f"department: {self.department}")

emp1 = Employeer(1221,"abbas",1000,"big data")
emp1.print_employee_details()
