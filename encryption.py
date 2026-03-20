text_user = input("Enter the text: ")
result = []
for char in text_user :
    if char.isalpha() :
        base = ord('a') if char.islower() else ord('A')
        shifted = (ord(char) - base + 1) % 26 + base 
        result.append(chr(shifted))
    else :
        result.append(char)
print("".join(result))
