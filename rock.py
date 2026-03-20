import random
print("*** wellcom to rock paper scissors Game ***")
user_choice = input("choose 1.rock 2.paper 3.scissors: ").capitalize()
list = ["Rock","Paper","Scissor"]
computer_choice = list[(random.randint(1,3))-1]


print(f"you choose {user_choice}")
print(f"computer choose {computer_choice}")
if user_choice == computer_choice :
    print("draw")
elif user_choice == "rock" and computer_choice == "paper": 
    print("COMPUTER WIN")
elif user_choice == "scissors" and computer_choice == "rock": 
    print("COMPUTER WIN")
elif user_choice == "paper" and computer_choice == "scissors": 
    print("COMPUTER WIN")
else :
    print("YOU WIN")
    