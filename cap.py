binary_bits = [0,1,0,1,0,1,1,0,0,0,0,0,1]
pos_counter = 0
neg_counter = 0 
for i in range(len(binary_bits) - 1) : 
    if binary_bits[i] == 0 and binary_bits[i+1] == 1 :
        pos_counter += 1
    elif binary_bits[i] == 1 and binary_bits[i+1] == 0 :
        neg_counter += 1

print(f"positive changes: {pos_counter}")
print(f"negative changes: {neg_counter}")