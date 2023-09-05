def remove(list,l):
    return list[:l-1] + list[l:]

list =[1,1,2,3,4,4,5,1]
print(remove(list,3))