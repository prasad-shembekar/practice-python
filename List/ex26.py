list1 = [10,10,0,0,10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

print(''.join(map(str,list2)) in ''.join(map(str,list1*2)))
