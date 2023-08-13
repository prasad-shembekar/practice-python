# Write a Python program to prove that two string variables of the same value point to the same memory location.

str1 = "Python"
str2 = "Python"

print("Memory addr of str1 =", hex(id(str1)))
print("Memory addr of str2 =", hex(id(str2)))