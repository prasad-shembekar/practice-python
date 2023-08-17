def check(str1):
    return len(str1) == len(set(str1.lower()))

print(check_isogram("w3resource"))
print(check_isogram("w3r"))
print(check_isogram("Python"))
print(check_isogram("Java"))