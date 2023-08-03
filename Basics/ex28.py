def concatenate(lst):
    result = ""
    for i in lst:
        result = result + str(i)
    return result

print(concatenate([1,5,12,2]))
