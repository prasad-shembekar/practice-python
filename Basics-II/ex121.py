def test(str):
	return str.translate(str.maketrans('PTSHA', '90168'))
str = "PHP"
print("Original string: ",str)
print("Coded string: ",test(str))
str = "JAVASCRIPT"
print("\nOriginal string: ",str)
print("Coded string: ",test(str))
