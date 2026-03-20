A = ["a","x","c","z","t"]
B = [1,5,2,7,11]
for letter , number in zip(A,B) :
    print(letter * number , end="")