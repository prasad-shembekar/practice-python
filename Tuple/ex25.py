def string_tuple(str1):
    result = tuple(x for x in str1 if not x.isspace())
    return result 

str1 = "Python Hello"
print(string_tuple(str1))

