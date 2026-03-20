a = "word1 word2 word3".split(" ")
print(a)
n = int(input("Enter n: "))
for i in range(n):
    x = a.pop()
    a.insert(0, x)
    print(a)

a = " ".join(a)
print(a)