def adjacent_num_product(list_nums):
   return max(a*b for a, b in zip(list_nums, list_nums[1:]))
nums = [1,2,3,4,5,6]
print("Original list: ",nums)