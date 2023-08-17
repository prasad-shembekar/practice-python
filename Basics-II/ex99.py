def find_string(txt, str1):
	return txt.find(str1, txt.find(str1)+1)

print(find_string("The quick brown fox jumps over the lazy dog", "the"))
print(find_string("the quick brown fox jumps over the lazy dog", "the"))

