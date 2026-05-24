def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    return -1

my_list = [10, 23, 45, 70, 11, 15]
target = 70

print(linear_search(my_list,target))
