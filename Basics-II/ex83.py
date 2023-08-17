# Write a Python program to test whether a given number is symmetrical or not.

def symmetrical(n):
    return str(n) == str(n)[::-1]

print(symmetrical(121))
