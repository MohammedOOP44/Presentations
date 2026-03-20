numbers = [[5, 7, 10], [4, 9, 15], [11, 20, 17]]
user_num = int(input("enter n: "))
counter = 0
for i in numbers :
    for j in i :
        if j % user_num == 0 :
            counter += 1
print(counter)