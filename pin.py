import random 
pin = random.randint(1000,9999)
user_input = int(input("Enter the pin: "))
if user_input == pin :
    print("great, your guessing is true")
elif len(str(user_input)) > 4 or len(str(user_input)) < 4:

    print("please, Enter 4 digits")
else :
    print("Failure! PIN code didn't match")
    print(f"the pin is {pin}")
