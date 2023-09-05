list1  = [[1,3],[5,7]]
list2 = [[2,4],[6,8]]
result = list(map(list.__add__,list1,list2))
print(str(result))