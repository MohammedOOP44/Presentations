class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Patient(Person):
    def __init__(self,name,age,patient_ID,illness):
        super().__init__(name,age)
        self.patient_ID = patient_ID
        self.illness = illness 

    def __str__(self):
        return f"name: {self.name},age: {self.age},ID: {self.patient_ID},illness: {self.illness}"

class Doctor(Person):
    def __init__(self,name,age,specialization):
        super().__init__(name,age)
        self.specialization = specialization

    def __str__(self):
        return f"name: {self.name},age: {self.age},specialization: {self.specialization}"
    
class Appointment:
    def __init__(self,patient,doctor,date):
        self.patient = patient 
        self.doctor = doctor
        self.date = date

    def __str__(self):
        return f"Appointments: {self.patient.name} with {self.doctor.name} on {self.date}"
        
class Hospital:
    def __init__(self,name):
        self.name = name
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self,patient):
        self.patients.append(patient)

    def add_doctor(self,doctor):
        self.doctors.append(doctor)

    def add_appointment(self,appointment):
        self.appointments.append(appointment)

    def display_records(self):
        print(f"\npatients in {self.name}")
        for i in self.patients:
            print(i)

        print(f"\ndoctors in {self.name}")
        for i in self.doctors:
            print(i)

        print(f"\nAppointments in {self.name}")
        for i in self.appointments:
            print(i)

city_hospital = Hospital("city_hospital")

patient1 = Patient("essam",99,1001,"cough")
patient2 = Patient("ali",22,1001,"headeche")

doctor1 = Doctor("zaid",9,"cardiology")
doctor2 = Doctor("Ahmed",9,"neurologist")

appt1 = Appointment(patient1,doctor1,"11/1/2026")
appt2 = Appointment(patient2,doctor2,"11/1/2027")

city_hospital.add_patient(patient1)
city_hospital.add_patient(patient2)
city_hospital.add_doctor(doctor1)
city_hospital.add_doctor(doctor2)
city_hospital.add_appointment(appt1)
city_hospital.add_appointment(appt2)



city_hospital.display_records()