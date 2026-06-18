import random 
import string 

class PasswordGenerator:
    def __init__(self,length):
        if length <= 0:
            raise ValueError("Password length must be greater then zero")
        self.length = length 
        self.use_uppercase = False
        self.use_lowercase = False
        self.use_digits = False
        self.use_symbols = False 
        self.set_preference()

    def ask_yes_no(self,question):
        answer = input(question).strip().lower()
        while answer not in ["yes","no","y","n"]:
            print("invalid input")
            answer = input(question).strip().lower()
        return answer in ["yes","y"]
    
    def set_preference(self):
        self.use_uppercase = self.ask_yes_no("Include upper case? yes/no: ")
        self.use_lowercase = self.ask_yes_no("Include lower case? yes/no: ")
        self.use_digits = self.ask_yes_no("Include digits? yes/no: ")
        self.use_symbols = self.ask_yes_no("Include sympols? yes/no: ")


    def build_character_pool(self):
        characters = ""
        if self.use_uppercase:
            characters += string.ascii_uppercase
        if self.use_lowercase:
            characters += string.ascii_lowercase
        if self.use_digits:
            characters += string.digits 
        if self.use_symbols:
            characters += string.punctuation

        if characters == "": 
            raise ValueError("ya must select at least one character type")
        
        return characters

    def generate_password(self):
        pool = self.build_character_pool()
        return "".join(random.choice(pool) for i in range(self.length))
    
def main():
    try:
        print("password generator: ")
        length = int(input("Enter the length: "))
        gen = PasswordGenerator(length)
        pas = gen.generate_password()
        print(f"Generated Password: {pas}")
    except ValueError as e:
        print("Error: ",e)

if __name__ == "__main__":
    main()

        

