import random
import string
def generate_passwords_simple(count=100):
    
    caps = string.ascii_uppercase
    
    others = string.ascii_letters + string.digits + "@#$%&"
    
    passwords = set()
    
    while len(passwords) < count:
        first_char = random.choice(caps)
        
        # 2. Pick the other 6 characters
        # random.choices (with an 's') picks multiple items at once
        remaining_chars = random.choices(others, k=6)
        
        # 3. Combine them into one string
        full_password = first_char + "".join(remaining_chars)
        
        # 4. Add to set (ensures uniqueness)
        passwords.add(full_password)
        
    return list(passwords)

# Implementation: Save to text file
final_list = generate_passwords_simple(100)
with open("passwords.txt", "w") as f:
    for p in final_list:
        f.write(p + "\n")

print("Done! Check passwords.txt")