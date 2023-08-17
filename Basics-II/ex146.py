def test(nums):
    x = nums[0]
    y = nums[1]
    t = y**0.5
    if(x == t*t*t):
        return True
    else:
        return False         
nums = [8, 4]
print("Original list of positive numbers:")
print(nums)
print(test(nums))
print("Check square root and cube root of the said numbers:")
nums = [64, 16]
print("Original list of positive numbers:")
print(nums)
print("Check square root and cube root of the said numbers:")
print(test(nums))
nums = [64, 36]
print("Original list of positive numbers:")
print(nums)
print("Check square root and cube root of the said numbers:")
print(test(nums)) 
