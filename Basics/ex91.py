# Write a Python program to swap two variables.

a = 23
b = 34

a,b = b,a

temp = a
a = b
b = temp 

print(a,b)