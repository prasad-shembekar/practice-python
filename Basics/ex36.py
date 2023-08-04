# Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.

def diff(x, y):
    if x == y or abs(x - y) == 5 or (x + y) == 5:
        return True
    return False


print(diff(7, 2))
print(diff(3, 2))
print(diff(27, 53))
