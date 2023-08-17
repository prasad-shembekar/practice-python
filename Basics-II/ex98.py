def increasing_trend(nums):
    if (sorted(nums) == nums):
        return True
    else:
        return False
    
print(increasing_trend([1,1,2,3,4]))