def test(str1):
    return any(c1 == c2 for c1, c2 in zip(str1, str1[1:]))
str = "PHP"
print("Original string: ",str)
print("Check for consecutive similar letters! ",test(str))
str = "PHHP"
print("\nOriginal string: ",str)
print("Check for consecutive similar letters! ",test(str))
str = "PHPP"
print("\nOriginal string: ",str)
print("Check for consecutive similar letters! ",test(str))
