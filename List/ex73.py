from itertools import groupby

def compress(nums):
    return [k for k,g in groupby(nums)]

list = [0,0,1,2,3,4,4,5,6,6,6]
print(compress(list))