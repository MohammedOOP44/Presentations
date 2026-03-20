attendees_input = input("Enter the names of attendees separated by commas: ")
attendees = attendees_input.split(",")
print(attendees)
for person in attendees :
    print(person)
    asking = input("is this peron attending (yes or no)").lower()
    if asking == "yes":
        print("Attendance confitmed")
    if asking == "no":
        print("Attendance not confitmed")