def average_two_list(num1,num2):
    result = sum(num1 + num2) / len(num1+num2)
    return result

nums1 = [1, 1, 3, 4, 4, 5, 6, 7]
nums2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]
print("Original list:")
print(nums1)
print(nums2)

print("\nAverage of two lists:")
print(average_two_lists(nums1, nums2))