def avg(nums):
    result = [sum(x) / len(x) for x in zip(*nums)]
    return result

print(avg(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))))