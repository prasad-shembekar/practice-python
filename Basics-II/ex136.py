def test(txt):
	return ' '.join(i[::-1] if len(i)%2 else i for i in txt.split())
 
text = "The quick brown fox jumps over the lazy dog"
print("Original string:")
print(text)
print("Reverse all the words of the said string which have odd length:")
print(test(text))
text = "Python Exercises"
print("\nOriginal string:")
print(text)
print("Reverse all the words of the said string which have odd length:")
print(test(text))
