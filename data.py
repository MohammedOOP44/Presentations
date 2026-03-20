print("wellcome to place rabbit")
leafs = [["🌿","🌿","🌿"]
        ,["🌿","🌿","🌿"]
        ,["🌿","🌿","🌿"]]
print("where should the rubbit go?🐇")
position = input("please choose a row and a column (e.g. 1,2): ")

row = int(position[0])
column = int(position[1])
leafs[row][column] =  '🐇' 
print(f"{leafs[0]} \n{leafs[1]} \n{leafs[2]}")