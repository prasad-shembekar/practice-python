def third_largest(nums):
    nums = set(nums)
    if len(nums) < 3:
        return None
    nums = list(nums)
    nums.sort(reverse=True)
    return nums[2]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original list of numbers:")
print(nums)
print("Third largest number of the said list of numbers:")
print(third_largest(nums))
nums = [1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9, 10]
print("Original list of numbers:")
print(nums)
print("Third largest number of the said list of numbers:")
print(third_largest(nums))
nums = [1, 2, 3]
print("Original list of numbers:")
print(nums)
print("Third largest number of the said list of numbers:")
print(third_largest(nums))
nums = [1, 2, 2]
print("Original list of numbers:")
print(nums)
print("Third largest number of the said list of numbers:")
print(third_largest(nums))
nums = [1, 2]
print("Original list of numbers:")
print(nums)
print("Third largest number of the said list of numbers:")
print(third_largest(nums))
