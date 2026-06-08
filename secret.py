import random 
import string 

class PasswordGenerator:
    def __init__(self,length):
        if length <= 0:
            raise ValueError("password length must generater greater than zero")
        self.length = length
        self.use_uppercase = False
        self.use_lowercase = False
        self.use_digits = False
        self.use_symbols = False

    def ask_yes_no(self,question):
        answer = input(question).strip().lower()
        while answer not in ['yes','no','y','n']:
            print("invalid input , please enter yes or no")
            answer = input(question).strip().lower()
        return answer in ['yes','y']
    
    def set_preferences(self):
        self.use_uppercase = self.ask_yes_no("include upper case? yes/no: ")
        self.use_lowercase = self.ask_yes_no("include lower case? yes/no: ")
        self.use_digits = self.ask_yes_no("include digits? yes/no: ")
        self.use_symbols = self.ask_yes_no("include symbols? yes/no: ")

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
            raise ValueError("you must select at least one character type")
        return characters
    
    def generate_password(self):
        pool = self.build_character_pool()
        return "".join(random.choice(pool) for _ in range(self.length))
    

def main():
    print("password generator")
    try:
        length = int(input("Enter password length: "))
        generator = PasswordGenerator(length)
        generator.set_preferences()
        password = generator.generate_password()
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Fuckin Error",e)

if __name__ == "__main__":
    main()




    
