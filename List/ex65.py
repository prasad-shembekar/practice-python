def test(lst):
    result = sorted(lst,key=lambda x: not x)
    return result

nums = [3,4,5,6,0,0,0,67,0,0,0,6,6,5,4,3,3,10]
print(test(nums))