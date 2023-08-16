# Write a Python program to add two positive integers without using the '+' operator.

def add(a,b):
    while b !=0:
        data = a & b
        a = a ^ b
        b = data << 1
    return a

print(add(2,10))