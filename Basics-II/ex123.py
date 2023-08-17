def test(str):
    return str if len(str) < 3 else str[1:-1]
str = "PHP"
print("Original string: ",str)
print("Removing the first and last elements from the said string: ",test(str))

