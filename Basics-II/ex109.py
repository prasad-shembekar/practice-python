def indices_in_list(nums_list, n):
           return [idx for idx, i in enumerate(nums_list) if i == n]
nums = [1,2,3,4,5,2]
print("Original list of numbers:",nums)
n = 2
print("Given Number",n)
print("Indices of all occurrences of the said item in the given list:")
print(indices_in_list(nums, n))
nums = [3,1,2,3,4,5,6,3,3]
print("\nOriginal list of numbers:",nums)
n = 3
print("Given Number",n)
print("Indices of all occurrences of the said item in the given list:")
print(indices_in_list(nums, n))
nums = [1,2,3,-4,5,2,-4]
print("\nOriginal list of numbers:",nums)
n = -4
print("Given Number",n)
print("Indices of all occurrences of the said item in the given list:")
print(indices_in_list(nums, n))
nums = [1,2,3,4,5,2]
print("\nOriginal list of numbers:",nums)
n = 7
print("Given Number",n)
print("Indices of all occurrences of the said item in the given list:")
print(indices_in_list(nums, n))
