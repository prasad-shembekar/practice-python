# Write a Python program that counts the number of prime numbers that are less than a given non-negative number.

def count(n):
    ctr = 0
    for num in range(n):
        if num <=1 :
            continue
        for i in range(2,num):
            if (num%i) == 0:
                break
        else:
            ctr += 1
    return ctr

print(count(10))