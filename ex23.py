# Write a Python program that accepts a positive number and subtracts from it the sum of its digits, and so on. Continue this operation until the number is positive.

def repeat_time(n):
    str1 = str(n)
    while (n > 0):
        n -= sum([int(i) for i in list(str1)])
        str1 = list(str(n))
    return n 

print(repeat_time(5674))