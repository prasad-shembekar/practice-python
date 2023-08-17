def test(str):
    return str.islower() or str.isupper()

str = "PHP"
print("Original string: ",str)
print("Coded string: ",test(str))
str = "javascript"
print("\nOriginal string: ",str)
print("Coded string: ",test(str))
str = "JavaScript"
print("\nOriginal string: ",str)
print("Coded string: ",test(str))
