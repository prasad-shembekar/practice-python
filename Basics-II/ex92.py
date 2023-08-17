# Write a Python program to compute the cumulative sum of numbers in a given list.

def nums_sum(nums):
    return [sum(nums[:i+1]) for i in range(len(nums))]

print(nums_sum([10,20,30,40,50]))