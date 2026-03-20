import random
print("wellcome to ' whose wallet'")
print("you will gimme a list of names ,and I will pick a person to pay")
names_string = input("If you are ready enter the separated by names: ")
names = names_string.split(", ")
length = len(names) - 1
random_num = random.randint(0,length)
random_person = names[random_num]
print(random_person)




