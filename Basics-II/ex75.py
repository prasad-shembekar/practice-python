# Write a Python program to remove all instances of a given value from a given array of integers and find the length of the newly created array.

def remove_element(array_nums,val):
    i = 0
    while i < len(array_nums):
        if array_nums[i] == val:
            array_nums.remove(array_nums[i])
        else:
            i += 1
    return len(array_nums)

print(remove_element([10,10,10,10,10,20], 10))