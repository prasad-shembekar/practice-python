# Write a Python program that replaces all but the last five characters of a string with "*" and returns the modified string. 

def new_str(str1):
    return '*'*(len(str1)-5) + str1[-5:]

text = "12345abcdef"
print("\nOriginal String: ",text)
print("new string: ",new_str(text))