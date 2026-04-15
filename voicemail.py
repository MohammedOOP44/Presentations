count = 0 
passwords = []

for letter in "ABCDEFGHIJKLMNOPQRSTUVUXYZ":
    for hundred in range(0,6):
        for tens in range(0,10):
            for units in range(0,10):
                number = hundred*100 + tens*10 + units
                password = f"{letter}{number:03d}"
                passwords.append(password)
                count += 1

print(passwords)
print(count)
