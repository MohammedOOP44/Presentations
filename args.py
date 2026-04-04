def my_funtion(*nums):
    max_val = nums[0]
    for num in nums:
        if max_val < num :
            max_val = num 

    return max_val

print(my_funtion(1,2,93,4,5,6,7,8))
        
