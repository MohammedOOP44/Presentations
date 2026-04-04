user_text = input("Enter Text: ")
text = []
for char in user_text:
    if char.isalpha():
        base = ord('a') if char.islower() else ord('A')
        shifting = (ord(char) - base + 1) %26 + base
        text.append(chr(shifting))
    else :
        text.append(char)

print("".join(text))
