# Write a Python program to calculate the hypotenuse of a right angled triangle.

from math import sqrt
print("Enter Triangle Sides:")
a = int(input("a: "))
b = int(input("b: "))
c = sqrt(a**2 + b**2)
print("Hypotenuse length is:", c)
