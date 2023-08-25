def recursive(data_list):
    total = 0
    for element in data_list:
        if type(element)==type([]):
            total += recursive(element)
        else:
            total += element
    return total

print(recursive([1, 2, [3,4],[5,6]]))