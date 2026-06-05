import string
import random

def generate_password(count=100):
    caps = string.ascii_uppercase

    others = string.ascii_letters + string.digits + "@#$%&"

    password = set()

    while len(password) < count:
        first_char = random.choice(caps) 
        remaining_chars = random.choices(others,k=6)

        full_pass = first_char + "".join(remaining_chars)

        password.add(full_pass)

    return list(password) 

final_password = generate_password(100)
with open("password.txt","w") as file :
    for i in final_password:
        file.write(i + "\n")