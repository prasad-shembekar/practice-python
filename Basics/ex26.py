def find(lst, target):
    for i in lst:
        if i == target:
            return True
    return False


print(find([1, 2, 3, 4, 5], 5))
