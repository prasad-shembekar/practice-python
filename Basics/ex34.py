# Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.

def sum_int(x, y, z):
    if x == y or y == z or x == z:
        sum = 0
        return sum
    else:
        return x + y + z


print(sum_int(2, 5, 2))
print(sum_int(2, 5, 8))
print(sum_int(3, 2, 2))
