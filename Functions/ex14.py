import string,sys
def ispangram(str1,alphabet=string.ascii_lowercase):
    alphabet = set(alphabet)
    return alphabet <= set(str1.lower())

print(ispangram('The quick brown fox jumps over the lazy dog'))