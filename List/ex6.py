def last(n):
    return n[-1]

def sort_list(tuples):
    return sorted(tuples,key=last)

print(sort_list([(2,5),(1,2)]))