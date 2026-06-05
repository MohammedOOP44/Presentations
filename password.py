import string
import random

def generate_(count=100):
    caps = string.ascii_uppercase

    others = string.ascii_letters + string.digits + "@#$%&"

     = set()

    while len() < count:
        first_char = random.choice(caps) 
        remaining_chars = random.choices(others,k=6)

        full_pass = first_char + "".join(remaining_chars)

        .add(full_pass)

    return list() 

final_ = generate_(100)
with open(".txt","w") as file :
    for i in final_:
        file.write(i + "\n")

    
