def unique(input):
    result = {}
    for l in input:
        result.setdefault(tuple(l),list()).append(1)
    for a,b in result.items():
        result[a] = sum(b)
    return result

list1 = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] 
print("Original list:")
print(list1)  
print("Number of unique lists of the said list:")
print(unique(list1)) 