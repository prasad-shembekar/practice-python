# Write a Python program to add two objects if both objects are integers.

def add_num(x, y):
    if (isinstance(x, int) and isinstance(y, int)):
        return x + y
    return "Input must be integer"


print(add_num(10, 20))
print(add_num(10, 20.23))
print(add_num('5', 6))
