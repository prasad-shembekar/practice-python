def test(str1):
    return str1[::-1].lower()
str = "PHP"
print("Original string:",str)
print("Reverse the said string in lower case:",test(str))
str = "JavaScript"
print("\nOriginal string:",str)
print("Reverse the said string in lower case:",test(str))
str = "PHPP"
print("\nOriginal string:",str)
print("Reverse the said string in lower case:",test(str)) 
