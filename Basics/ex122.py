# Write a Python program to empty a variable without destroying it. type() returns the type of an object, which when called produces an 'empty' new value.

n = 20
d = {"x":200}
l = [1,3,5]
t= (5,7,8)
print(type(n)())
print(type(d)())
print(type(l)())
print(type(t)())