import itertools
num = [[10,20],[40],[30,56,25]]
print(num)
num.sort()
new = list(num for num,_ in itertools.groupby(num))
print(new)