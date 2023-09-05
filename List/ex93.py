def count(input,x):
    ctr = 0
    for i in range(len(input)):
        if x in input[i]:
            ctr += 1
    return ctr

list1 = [[1, 3], [5, 7], [1, 11], [1, 15, 7]] 
print("Original list:")
print(list1)
print("\nCount 1 in the said list:")
print(count(list1, 1)) 