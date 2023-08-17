def string_check(str1,str2):
    return all([char in str1.lower() for char in str2.lower()])

print(string_check("python","ypth"))

