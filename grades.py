
students = {
    "name":"mohammed",
    "grades": [70 , 55 , 60]
}
def average_grades(students) :
    total = 0
    for grade in students["grades"] :
        total += grade
    return total / len(students["grades"])
    
print(average_grades(students))