print("wellcome to place rabbit")
field = [["🌿","🌿","🌿"],["🌿","🌿","🌿"],["🌿","🌿","🌿"]]
print("where should rabbit go?🐇")
position = input("enter the number of row and column (e.g. 12): ")
row = int(position[0])
column = int(position[1])

field[row][column] = '🐇'
print(f"{field[0]} \n{field[1]} \n{field[2]} \n")