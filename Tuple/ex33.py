def test(lst_tuple):
    result = [list(el) for el in lst_tuple]
    return result

lst_tuple = [(1,2),(3,4)]
print(test(lst_tuple))