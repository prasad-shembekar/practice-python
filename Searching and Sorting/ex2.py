# sequential/linear search 

def linear(list,target):
    i = 0
    found = False
    
    while i < len(list) and not found:
        if list[i] == target:
            found = True
        else:
            i += 1
    return found, i 

print(linear([11,23,58,31,56,77,43,12,65,19],31))

