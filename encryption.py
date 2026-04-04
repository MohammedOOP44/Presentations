text_user = input("Enter the text: ")
result_enc = []
result_dec = []
for char in text_user :
    if char.isalpha() :
        base = ord('a') if char.islower() else ord('A')
        shiftedToFront = (ord(char) - base + 1) % 26 + base 
        shiftedToBehind = (ord(char) - base - 1) % 26 + base
        result_enc.append(chr(shiftedToFront))
        result_dec.append(chr(shiftedToBehind))
    else :
        result_enc.append(char)
        result_dec.append(char)
choice = int(input("What did you want: 1.encrypted , 2.decrypted: "))
if choice == 1:
    print("".join(result_enc))
elif choice == 2:
    print("".join(result_dec))
