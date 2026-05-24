def binary_search(arr,target):
    left = 0
    right = len(arr) - 1
   

    while left <= right:
        mid = (left + right)//2

        if arr[mid] == target:
            return mid
        
        if arr[mid] < target:
            left = mid + 1

        else:
            right = mid -1

    return -1

arr = [10, 23, 45, 70, 11, 15]
target = 11
print(binary_search(arr,target))
