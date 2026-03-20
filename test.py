numbers = [[9,3,7],[3,2,2],[9,1,0]]
for row in numbers :
    min_value = min(row)
    col_idx = row.index(min_value)
    is_saddle = True
    for col in numbers :
        if min_value < col[col_idx] :
            is_saddle = False
            break
    if is_saddle :
        print(f"saddle point is {min_value}")
