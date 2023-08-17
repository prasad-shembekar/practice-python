def count_sum(nums):
    if not nums: return []
    return [len([n for n in nums if n<0]),sum(n for n in nums if n>0)]

nums = [1,2,3,4,5]
print(count_sum(nums))
