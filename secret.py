import string
import random 


class Passwordword:
    def __init__(self,length):
        if length <= 0:
            raise ValueError("password length must be greater than zero")
        self.length = length
        self.use_uppercase = False
        self.use_lowercase = False
        self.use_digits = False
        self.use_symbols = False
        
    def ask_yes_no(self,question):
        answer = input(question).strip().lower()
        while answer not in ["yes","no","y","n"]:
            print("invalid input")
            answer = input(question).strip().lower()
        return answer in ["yes","no"]
    

    def set_preference(self):
        self.use_uppercase = self.ask_yes_no("Include uppercase? yes/no: ")
        self.use_lowercase = self.ask_yes_no("Include lowercase? yes/no: ")
        self.use_digits = self.ask_yes_no("Include digits? yes/no: ")
        self.use_symbols = self.ask_yes_no("Include symbols? yes/no: ")

    def build_char_bool(self):
        characters = ""
        if self.use_uppercase:
            characters += string.ascii_uppercase
        if self.use_lowercase:
            characters += string.ascii.lowercase
        if self.digits :
            characters += string.digits
        if self.symbols :
            characters += string.punctuation

        if characters == "": 
            raise ValueError("ya must select at one character type ")
        
        return characters 

    def generate_password(self):
        bool = self.build_char_bool()
        return "".join(random.choice(bool) for _ in range(self.length))
    
def main():


        



    
