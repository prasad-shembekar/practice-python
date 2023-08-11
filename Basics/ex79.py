# Write a Python program to get the size of an object in bytes.

import sys

str1 = "Hello"
str2 = "Prasad"

num = 12345

print("Size of",str1,"=",str(sys.getsizeof(str1))+"bytes")
print("Size of",str2,"=",str(sys.getsizeof(str2))+"bytes")
print("Size of",num,"=",str(sys.getsizeof(num))+"bytes")
