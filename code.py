import random 
list_name = input("Enter the names")
names = list_name.split(", ")
length = len(names) - 1
random_person = random.randint(0,length)
print(random_person) 2