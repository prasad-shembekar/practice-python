# Write a Python program to calculate the median from a list of numbers. 

def median(nums):
    nums.sort()
    n = len(nums)
    m = n//2
    if n%2 == 0:
        return (nums[m-1] + nums[m]) /2
    else:
        return nums[m]
    
print(median([1.0,2.11,3.3,4.2,5.22,6.55]))