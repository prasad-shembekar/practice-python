def smallest(lst):
    min = lst[0]

    for a in lst:
        if a < min:
            min = a
    return min

print(smallest([1,2,-8,0]))