# Write a Python program to find the total number of even or odd divisors of a given integer.

def divisor(n):
    x = len([i for i in range(1,n+1) if not n%i])
    return x

print(divisor(15))