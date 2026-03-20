students = {
    1001:{"name":"mohammed","grades":[77,88,92]},
    1002:{"name":"ahmed","grades":[80,9,52]},
    1003:{"name":"ali","grades":[90,100,99]}
}
def add_student(students,ID,name) :
    if ID in students :
        print("This ID is involved already")
    else : 
        students[ID] = {"name":name,"grades":[]}
def add_grade(students,ID,grade) :
    if ID in students :
        students[ID]["grades"].append(grade)
        
    else :
        print("EROR")
def student_average(students,ID) :
    if ID not in students :
        return 0
    grades = students[ID]["grades"]
    if len(grades) == 0 :
        return 0
    total = 0
    for grade in students[ID]["grades"] :
        total += grade
    return total / len(grades)
    
def top_student(students) :
    top_ave = 0
    top_name = ""
    for ID, info in students.items() :
        ave = student_average(students,ID)
        if top_ave < ave :
            top_ave = ave
            top_name = info["name"]
    return top_ave

print(top_student(students))
        