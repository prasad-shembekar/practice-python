def multiple(nums):
    temp = list(nums)
    product = 1
    for x in temp:
        product *= x
    return product

print(multiple((4,3,2,2,1,-1,18)))
