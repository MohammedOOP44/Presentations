word = input("Enter the word you want to encrypt: ")
encrypted_word = []
for x in word :
    if x == 'z' :
        encrypted_word.append('a')
    elif x == 'Z' :
        encrypted_word.append('A')
    elif 'a'<=x<'z':
        n = chr(ord(x) + 1)
        encrypted_word.append(n)
    elif 'A'<=x<'Z':
        n = chr(ord(x) + 1)
        encrypted_word.append(n)
    else:
        encrypted_word.append(x)


print("".join(encrypted_word))