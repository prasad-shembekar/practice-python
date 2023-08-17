# Write a Python program to find the first missing positive integer that does not exist in a given list.

def first_missing(nums):
    if len(nums) == 0:
        return 1
    
    nums.sort()
    smallest = 0

    for i in range(len(nums)-1):
        if nums[i] <=0 or nums[i] == nums[i+1]:
            continue
        else:
            if nums[i+1] - nums[i] != 1:
                smallest = nums[i]+1
                return smallest
    if smallest == 0:
        smallest  = nums[-1] +1
    return smallest

print(first_missing_number([2, 3, 7, 6, 8, -1, -10, 15, 16]))        
    
