# Write a Python program to check whether a number is "happy" or not.

def happy(n):
    past = set()
    while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
    return True

print(happy(932))